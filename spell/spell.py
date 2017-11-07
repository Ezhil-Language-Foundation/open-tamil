# -*- coding: utf-8 -*-
# (C) 2016 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package
# It implements a data-driven spell checker for Tamil language
# 
from __future__ import print_function

import argparse
import copy
import codecs
import functools
import itertools
import json
import operator
import pprint
import re
import string
import sys
import threading
import time

import tamil

from solthiruthi.suggestions import norvig_suggestor
from solthiruthi.morphology import RemoveCaseSuffix, RemovePluralSuffix, RemovePrefix, RemoveVerbSuffixTense, CaseFilter
from solthiruthi.dictionary import DictionaryBuilder, TamilVU, EnglishLinux
from ngram.Distance import Dice_coeff, edit_distance

# Make Bi-Lingual dictionary

PYTHON3 = ( sys.version_info[0] == 3 )
if PYTHON3:
    unicode = str

_DEBUG = False

# save 6s for the code on a old machine
class LoadDictionary(threading.Thread):
    DEBUG = False
    lock = threading.Lock()
    def __init__(self):
        threading.Thread.__init__(self,name="LoadDictionaryInBackground")
        
    def run(self):
        start = time.time()
        Speller.get_dictionary()
        Speller.get_english_dictionary()
        if LoadDictionary.DEBUG: print("LOADED DICTIONARY in  %g (s)"%(time.time() - start))
        return

class Mayangoli:
    varisai = [[ u"ல்", u"ழ்",u"ள்"],[u"ர்", u"ற்"],[u"ந்",u"ன்",u"ண்"],[u"ங்",u"ஞ்"]]#வரிசை.
    
    def __init__(self,word):
        self.word = word
        self.letters = tamil.utf8.get_letters(word)
        self.matches_and_positions = []
        self.alternates = []
        self.pos_classes = []
        
    @staticmethod
    def run(word):
        obj = Mayangoli(word)
        obj.find_letter_positions()
        if len(obj.matches_and_positions) == 0:
            return []
        obj.find_correspondents()
        obj.generate_word_alternates()
        return obj.alternates
    
    def find_letter_positions(self):
        for idx,letter in enumerate(self.letters):
            p = tamil.utf8.splitMeiUyir(letter)
            if len(p) == 1:
                continue
            mei,uyir=p
            for r in range(0,len(Mayangoli.varisai)):
                for c in range(0,len(Mayangoli.varisai[r])):
                    if mei == Mayangoli.varisai[r][c]:
                        self.matches_and_positions.append((idx,r,c))
        return len(self.matches_and_positions) > 0
    
    def find_correspondents(self):
        for pos,r,c in self.matches_and_positions:
            src_letter  = self.letters[pos]
            _,src_uyir = tamil.utf8.splitMeiUyir(src_letter)
            alt_letters = []
            for alternate_mei in Mayangoli.varisai[r]:
                alt_letters.append( tamil.utf8.joinMeiUyir(alternate_mei,src_uyir) )
            self.pos_classes.append(alt_letters)
        return True
    
    def _generate_combinations(self):
        return itertools.product(*self.pos_classes)
    
    def generate_word_alternates(self):
        # find matches in Mayangoli classes
        # if there are no Mayangoli matches then we return []
        # for each match we find the class and find corresponding uyirmei alternates
        # generate the combinations of these alternates in the said word positions
        # caller will filter the new word alternates (returned)
        # based on substituting these correspondents
        for position_sub in self._generate_combinations():
            alt_letters = copy.copy(self.letters)
            if _DEBUG: pprint.pprint(position_sub)
            idx =0
            for pos,r,c in self.matches_and_positions:
                alt_letters[pos] = position_sub[idx]
                idx += 1
            word_alt = u''.join(alt_letters)
            self.alternates.append(word_alt)
        return True
    
class Speller(object):
    TVU_dict = None
    ENL_dict = None
    def __init__(self,filename=None,lang="ta",mode="non-web"):
        object.__init__(self)
        self.lang = lang.lower()
        self.filename = filename
        self.user_dict = set()
        self.case_filter = CaseFilter( RemovePluralSuffix(), RemoveVerbSuffixTense(), RemoveCaseSuffix(), RemovePrefix() )
        if not self.in_tamil_mode():
            self.alphabets = [a for a in string.ascii_lowercase]
        else:
            self.alphabets = None
        
        if mode == "web":
            return
        
        if not self.filename:
            self.interactive()
        else:
            self.spellcheck(self.filename)
    
    def in_tamil_mode(self):
        return self.lang != u"en"
    
    @staticmethod
    def get_dictionary():
        LoadDictionary.lock.acquire()
        if not Speller.TVU_dict:
            Speller.TVU_dict,_ = DictionaryBuilder.create(TamilVU)
        LoadDictionary.lock.release()
        return Speller.TVU_dict
    
    @staticmethod
    def get_english_dictionary():
        LoadDictionary.lock.acquire()
        if not Speller.ENL_dict:
            Speller.ENL_dict,_ = DictionaryBuilder.create(EnglishLinux)
        LoadDictionary.lock.release()
        return Speller.ENL_dict    
    
    def language(self):
        if self.in_tamil_mode():
            return "tamil"
        return "english"
        
    def checklang(self,word):
        if self.in_tamil_mode():
            return tamil.utf8.all_tamil(word)
        for w in word.lower():
            if not ( w in string.ascii_lowercase ):
                return False
        return True
    
    # Ref: https://www.tinymce.com/docs/plugins/spellchecker/
    def REST_interface(self,word):
        # returns JSON data in TinyMCE format
        ok,suggs = self.check_word_and_suggest( word )
        if _DEBUG:
            print("REST => %d"%ok)
            pprint.pprint(suggs)
        if ok:
            return ok, {}
        return ok, suggs
    
    @staticmethod
    def dice_comparison(ref_word,word):
        """ use this class method for SORTED"""
        val = Dice_coeff(ref_word,word)
        if ( val == 1 ):
            return 0
        return (2*(val - 0.5) > 0) and 1 or -1
        
    def suggestion_policy(self,word,suggs):
        # pick suggestions that are only +/- 2 letter length different
        filter_suggs = []
        tamil_length = lambda w: len(tamil.utf8.get_letters(w))
        ref_wl = tamil_length(word)
        accept_min_max = [max(ref_wl-2,1),ref_wl+1]
        filter_suggs = filter(lambda w: tamil_length(w) >= accept_min_max[0] and len(w) <= accept_min_max[1], suggs)
        # sort the suggestions by Dice coefficient
        filter_suggs = set(filter_suggs)
        if len(filter_suggs) == 0:
            # guess!
            filter_suggs = suggs
            filter_suggs=sorted(filter_suggs,cmp=tamil.utf8.compare_words_lexicographic)
            filter_suggs[min(10,len(filter_suggs)-1):]=[]
            return filter_suggs
        filter_suggs=sorted(filter_suggs,cmp=Speller.dice_comparison)
        return filter_suggs
    
    def str_suggestions(self,word):
        if self.in_tamil_mode():
            return u"சொல் \"%s\" மாற்றங்கள்"%word
        return u"SUGGESTIONS for \"%s\""%word
    
    def mayangoli_suggestions(self,word):
        alternates = Mayangoli.run(word)
        alternates = filter(lambda w: w != word, alternates)
        if _DEBUG:
            for idx,w in enumerate(alternates):
                pprint.pprint(["Myangoli",idx,w])
        return copy.copy(alternates)
    
    def interactive(self):
        try:
            while( True ):
                if PYTHON3:
                    word = input(u">> ")
                else:
                    word = raw_input(u">> ")
                    word = word.decode("utf-8").strip()
                word = re.sub(u"\s+","",word)
                
                # skip empty words
                if len(word) < 1:
                    continue
                
                if not self.checklang(word):
                    print(u"EXCEPTION \"%s\" is not a %s Word"%(word,self.language()))
                    continue
                ok,suggs = self.check_word_and_suggest( word )
                suggs = self.suggestion_policy(word,suggs)
                if not ok:
                    words_per_row = 4
                    option_str = u", ".join( [ u"(%d) %s"%(itr,wrd) + ((itr > 0 and itr%words_per_row == 0) and u"\n" or u"") for itr,wrd in enumerate(suggs)] )
                    print(u"%s\n\t %s"%(self.str_suggestions(word),option_str))
                else:
                    print(self.in_tamil_mode() and  u"சரி" or u"OK")
        except KeyboardInterrupt as ke:
            pass
        except EOFError as eof:
            pass
        finally:
            print(self.in_tamil_mode() and  u"\nவணக்கம்!" or "\nBYE!")
        return
    
    def spellcheck(self,filename):
        new_document = []
        data = codecs.open(filename,u"r",u"utf-8")
        lines = data.readlines()
        for line in lines:
            words = tamil.utf8.get_words( tamil.utf8.get_letters(line) )
            for word  in words:
                # FIXME : handle punctuation
                #word = filter( tamil.utf8.is_tamil_unicode_predicate, word )
                ok,suggs = self.check_word_and_suggest( word )
                if not ok:
                    option = suggs[0]
                    # take user input.
                    # FIXME: User options to include DONTREPLACE/KEEP, DELETE WORD, etc.
                    option_str = u", ".join( [ u"(%d) %s"%(itr,wrd) for itr,wrd in enumerate(suggs)] )
                    print(u"In line, \"%s\""%line.strip())
                    print(u" Replace word %s with\n\t => %s\n"%(word, option_str))
                    try:
                        choice = input(u"option [-1 ignore, 0-%d replace]: "%(len(suggs)-1))
                        if PYTHON3:
                            choice = int(choice)
                        if choice == -1:
                            print(u"Not replacing word")
                            option = word
                            self.user_dict.add(word)
                        else:
                            option = suggs[choice]
                    except Exception as ie:
                        print (str(ie))
                    print(u" replacing word %s -> %s\n"%(word,option))
                    new_document.append( unicode(option) )
                else:
                    new_document.append( word )
            new_document.append(u"\n")
        print(u"*********** cleaned up document **********")
        print(u" ".join(new_document))
        
    def get_lang_dictionary(self):
        if not self.in_tamil_mode():
            return Speller.get_english_dictionary()
        return Speller.get_dictionary()
    
    def isWord(self, word):
        # Plain old dictionary checks
        LANG_dict = self.get_lang_dictionary()
        is_dict_word = LANG_dict.isWord(word)
        in_user_dict = word in self.user_dict or is_dict_word
        return in_user_dict
        
    def check_word_and_suggest( self,word ):         
        word = word.strip()
        orig_word = u'%s'%word
        # remove punctuation
        for x in string.punctuation:
            word = word.replace(x,u"")
        # remove digits
        word = re.sub(u'\d+',u'',word)
        letters = tamil.utf8.get_letters(word)
        TVU_dict = self.get_lang_dictionary()
        
        if not self.checklang(word):
            print("Word is not in desired language!")
            return (False,[u''])
        
        if len(word) < 1:
            print("Word is too small")
            return (False,[u''])
        
        # plain old dictionary + user dictionary check
        if self.isWord(word):
            return (True,word)
        
        # Remove case and redo the dictionary + user check
        word_nocase = self.case_filter.apply( word )
        if ( self.isWord( word_nocase ) ):
            return (True,word_nocase)
        else:
            word = word_nocase
        
        # Consider splitting the word and see if it has 2 sub-words
        # e.g. செயல்பட => செயல் + பட
        alt = tamil.wordutils.greedy_split(word,TVU_dict)
        if len(alt) >= 1:
            greedy_results = [u" ".join(alt),u"-".join(alt)]
            greedy_results.extend(alt)
        #return (False, results )
        else:
            greedy_results = list()
        
        # TODO: Noun Declension - ticket-
        
        # suggestions at edit distance 1
        norvig_suggests = filter( TVU_dict.isWord, norvig_suggestor( word, self.alphabets, 2,limit=50))
        combinagram_suggests = list(tamil.wordutils.combinagrams(word,TVU_dict,limit=50)) 
        pfx_options = TVU_dict.getWordsStartingWith( u"".join( letters[:-1] ) )
        
        # FIXME: score  the options
        options = greedy_results
        options.extend( list(norvig_suggests))
        options.extend( combinagram_suggests )
        options.extend( pfx_options )
        
        # filter the options against a dictionary!
        options = filter(TVU_dict.isWord,options )
        if PYTHON3:
            options = list(options)
        
        if self.in_tamil_mode():
            options.extend( self.mayangoli_suggestions(orig_word) )
            
        # sort the options
        if not self.in_tamil_mode():
            options.sort()
        else:
            if PYTHON3:
                options = sorted( options, key=functools.cmp_to_key(tamil.utf8.compare_words_lexicographic) )
            else:
                options = sorted( options, cmp=tamil.utf8.compare_words_lexicographic )
        
        # remove replacements with single-letter words
        WL = len(tamil.utf8.get_letters(word))
        if WL > 3:
            options = filter( lambda x:  len(tamil.utf8.get_letters(x)) > 2, options )
        
        # remove dupes in list
        options2 = []
        prev = None
        for val in options:
            if val.strip() != prev:
                options2.append(val.strip())
            prev = val.strip()
        del options
        if _DEBUG:
            print("@deduplication")
            pprint.pprint(options2)
                
        # score by Dice or Edit-Distance coefficients
        options_score = [0.0 for i in range(len(options2))]
        for itr,sugg_word in enumerate(options2):
            #options_score[itr] = Dice_coeff( word, sugg_word )
            options_score[itr] = (len(word)-edit_distance(word,sugg_word))/(1.0*len(orig_word))*Dice_coeff( word, sugg_word )/3.0 #dice coeff is weighted down
        options = zip( options2, options_score)
        
        # limit options by score
        options = sorted(options,key=operator.itemgetter(1),reverse=True)
        options = [word_pair[0] for word_pair in options]
        #L = 40
        # limit to first top -L=20 only which is good enough
        #options = options[0:min(len(options),L)]
        if _DEBUG: 
            pprint.pprint("@after scoring/sorting")
            pprint.pprint(options)
        
        # eliminate single letter options
        options = filter(lambda x : not( x in tamil.utf8.tamil_letters), options)
        
        # Due to suggestion policy we may have words which are found in error but we dont have
        # replacements for them!
        
        # TBD: options should not have the 'word'!
        return (False, options )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(u"files",nargs='*',default=[])
    parser.add_argument(u"-debug",action=u"store_true",\
                        default=False,\
                        help=u"enable debugging information on screen")
    parser.add_argument(u"-l",u"--lang",default=u"TA",choices=(u"TA",u"EN"),\
                        help=u"option to specify English or Tamil (default) language")
    parser.add_argument(u"-i",u"--interactive",help=u"use the interactive mode",\
                        default=False,action=u"store_true")
    args = parser.parse_args()
    
    if not args.interactive and len(args.files) < 1:
        parser.print_help()
        sys.exit(0)
    LoadDictionary().start()
    
    if args.interactive:
        lang = args.lang.lower()
        Speller(filename=None,lang=lang)
        sys.exit(0)
    else:
        for file_name in args.files:
            Speller(file_name,lang="ta")

if __name__ == u'__main__':
    main()
#TBD: colors, cities, places, countries, currencies to be added
#TBD: proper nouns common names etc.