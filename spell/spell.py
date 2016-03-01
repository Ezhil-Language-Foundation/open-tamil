# -*- coding: utf-8 -*-
# (C) 2016 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package
# It implements a data-driven spell checker for Tamil language
# 
from __future__ import print_function
from solthiruthi.suggestions import norvig_suggestor
from solthiruthi.morphology import RemoveCaseSuffix, RemovePluralSuffix, RemovePrefix, RemoveVerbSuffixTense, CaseFilter
from solthiruthi.dictionary import DictionaryBuilder, TamilVU, EnglishLinux
import tamil
import sys
import re
import codecs
import threading
import time
import string
import argparse
import json
import functools
import operator
from ngram.Distance import Dice_coeff

# Make Bi-Lingual dictionary

PYTHON3 = ( sys.version_info[0] == 3 )
if PYTHON3:
    unicode = str

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

class Speller(object):
    TVU_dict = None
    ENL_dict = None
    def __init__(self,filename=None,lang="ta",mode="non-web"):
        object.__init__(self)
        self.lang = lang.lower()
        self.filename = filename
        self.user_dict = set()
        self.case_filter = CaseFilter( RemovePluralSuffix(), RemoveVerbSuffixTense(), RemoveCaseSuffix(), RemovePrefix() )
        if self.lang == u"en":
            self.alphabets = [a for a in string.ascii_lowercase]
        else:
            self.alphabets = None
        
        if mode != "web":
            if not self.filename:
                self.interactive()
            else:
                self.spellcheck(self.filename)
        pass
    
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
        if self.lang == "ta":
            return "tamil"
        return "english"
        
    def checklang(self,word):
        if self.lang == "ta":
            return tamil.utf8.all_tamil(word)
        for w in word.lower():
            if not ( w in string.ascii_lowercase ):
                return False
        return True
    
    # Ref: https://www.tinymce.com/docs/plugins/spellchecker/
    def REST_interface(self,word):
        # returns JSON data in TinyMCE format
        ok,suggs = self.check_word_and_suggest( word )
        if ok:
            return ok, {}
        return ok, suggs
        
    def interactive(self):
        try:
            while( True ):
                if PYTHON3:
                    word = input(u">> ")
                else:
                    word = raw_input(u">> ")
                    word = word.decode("utf-8").strip()
                word = re.sub(u"\s+","",word)
                if not self.checklang(word):
                    print(u"EXCEPTION \"%s\" is not a %s Word"%(word,self.language()))
                    continue
                ok,suggs = self.check_word_and_suggest( word )
                if not ok:
                    option_str = u", ".join( [ u"(%d) %s"%(itr,wrd) for itr,wrd in enumerate(suggs)] )
                    print(u"SUGGESTIONS for \"%s\"\n\t %s"%(word,option_str))
                else:
                    print(u"OK")
        except KeyboardInterrupt as ke:
            pass
        except EOFError as eof:
            pass
        finally:
            print("\nBYE!")
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
                    # FIXME: User optiions to include DONTREPLACE/KEEP, DELETE WORD, etc.
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
        if self.lang == u"en":
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
        # remove punctuation
        for x in string.punctuation:
            word = word.replace(x,u"")
        # remove digits
        word = re.sub(u'\d+',u'',word)
        letters = tamil.utf8.get_letters(word)
        TVU_dict = self.get_lang_dictionary()
        
        if not self.checklang(word):
            return (False,[u''])
        
        if len(word) < 1:
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
        
        # sort the options
        if self.lang == u"en":
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
        
        # score by Dice coefficients
        options_score = [0.0 for i in range(len(options2))]
        for itr,sugg_word in enumerate(options2):
            options_score[itr] = Dice_coeff( word, sugg_word )
        options = zip( options2, options_score)
        
        # limit options by score
        options = sorted(options,key=operator.itemgetter(1),reverse=True)
        options = [word_pair[0] for word_pair in options]
        
        L = 20
        # limit to first top -L=20 only which is good enough
        options = options[0:min(len(options),L)]
        
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
