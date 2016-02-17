# -*- coding: utf-8 -*-
# (C) 2016 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package
# It implements a data-driven spell checker for Tamil language
# 
from __future__ import print_function
from solthiruthi.suggestions import norvig_suggestor
from solthiruthi.morphology import RemoveCaseSuffix, RemovePluralSuffix, RemovePrefix, RemoveVerbSuffixTense, CaseFilter
from solthiruthi.dictionary import DictionaryBuilder, TamilVU
import tamil
import sys
import re
import codecs
import threading
import time


# save 6s for the code on a old machine
class LoadDictionary(threading.Thread):
    DEBUG = False
    lock = threading.Lock()
    def __init__(self):
        threading.Thread.__init__(self,name="LoadDictionaryInBackground")
        
    def run(self):
        start = time.time()
        Speller.get_dictionary()
        if LoadDictionary.DEBUG: print("LOADED DICTIONARY in  %g (s)"%(time.time() - start))
        return

class Speller(object):
    TVU_dict = None
    def __init__(self,filename=None):
        object.__init__(self)
        self.filename = filename
        self.user_dict = set()
        self.case_filter = CaseFilter( RemovePluralSuffix(), RemoveVerbSuffixTense(), RemoveCaseSuffix(), RemovePrefix() )
        if not self.filename:            
            self.interactive()
        else:
            self.spellcheck(self.filename)

    @staticmethod
    def get_dictionary():        
        LoadDictionary.lock.acquire()
        if not Speller.TVU_dict:
            Speller.TVU_dict,_ = DictionaryBuilder.create(TamilVU)
        LoadDictionary.lock.release()
        return Speller.TVU_dict
    
    def interactive(self):
        try:
            while( True ):
                word = raw_input(u">> ")
                word = word.decode("utf-8").strip()
                word = re.sub(u"\s+","",word)
                if not tamil.utf8.all_tamil(word):
                    print(u"EXCEPTION \"%s\" is not a Tamil Word"%word)
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
        
    def isWord(self, word):
        # Plain old dictioary checks
        TVU_dict = Speller.get_dictionary()
        in_user_dict = word in self.user_dict or TVU_dict.isWord(word)
        return in_user_dict
        
    def check_word_and_suggest( self,word ):         
        letters = tamil.utf8.get_letters(word)
        TVU_dict = Speller.get_dictionary()        
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
            results = [u" ".join(alt)]
            results.extend(alt)
            return (False, results )
        
        # TODO: Noun Declension - ticket-
        
        # suggestions at edit distance 1
        norvig_suggests = filter( TVU_dict.isWord, norvig_suggestor( word, None, 1,limit=50))
        combinagram_suggests = list(tamil.wordutils.combinagrams(word,TVU_dict,limit=50)) 
        pfx_options = TVU_dict.getWordsStartingWith( u"".join( letters[:-1] ) )
        
        # FIXME: score  the options
        options = norvig_suggests
        options.extend( combinagram_suggests )
        options.extend( pfx_options )
        
        # score by 
        
        # sort the options
        options = sorted( options, cmp=tamil.utf8.compare_words_lexicographic )
        
        return (False, options )

if __name__ == u'__main__':
    if len(sys.argv) < 2:
        print(u"usage: python spell.py [<filename 1>  ... <filename n> | -i[nteractive] ]")
        sys.exit(0)
    LoadDictionary().start()
    if sys.argv[1].find("-i") == 0:
        Speller()
        sys.exit(0)
    else:
        for file_name in sys.argv[1:]:
            Speller(file_name)
