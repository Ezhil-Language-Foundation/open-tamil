# -*- coding: utf-8 -*-
# (C) 2016 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 
from __future__ import print_function
from solthiruthi.suggestions import norvig_suggestor
from solthiruthi.morphology import RemoveCaseSuffix, RemovePluralSuffix, RemovePrefix, CaseFilter
from solthiruthi.dictionary import DictionaryBuilder, TamilVU
import tamil
import sys
import codecs 

class Speller(object):
    TVU_dict = None
    def __init__(self,filename):
        object.__init__(self)
        self.filename = filename
        self.user_dict = set()
        self.case_filter = CaseFilter( RemovePluralSuffix(), RemoveCaseSuffix(), RemovePrefix() )
        self.spellcheck(self.filename)
    
    @staticmethod
    def get_dictionary():
        if not Speller.TVU_dict:
            Speller.TVU_dict,_ = DictionaryBuilder.create(TamilVU)
        return Speller.TVU_dict
    
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
                    option_str = u",".join( [ u"%d) %s"%(itr,wrd) for itr,wrd in enumerate(suggs)] )
                    print(u"In line, \"%s\""%line.strip())
                    
                    print(u" Replace word %s \n\t Options => %s\n"%(word, option_str))
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

    def check_word_and_suggest( self,word ): 
        TVU_dict = Speller.get_dictionary()
        letters = tamil.utf8.get_letters(word)

        # Plain old dictioary checks
        in_user_dict = word in self.user_dict
        if in_user_dict or TVU_dict.isWord(word):
            return (True,[],None)
        
        # Remove case and redo the dictionary + user check
        word = self.case_filter.apply( word )
        
        # Consider splitting the word and see if it has 2 sub-words
        # e.g. செயல்பட => செயல் + பட
        alt = tamil.wordutils.greedy_split(word,TVU_dict)
        if len(alt) >= 1:
            return (False, alt)

        # TODO: Noun Declension - ticket-
    
        # suggestions at edit distance 1
        norvig_suggests = filter( TVU_dict.isWord, norvig_suggestor( word, None, 1))
        combinagram_suggests = list(tamil.wordutils.combinagrams(word,TVU_dict)) 
        pfx_options = TVU_dict.getWordsStartingWith( u"".join( letters[:-1] ) )

        # FIXME: score  the options
        options = norvig_suggests
        options.extend( combinagram_suggests )
        options.extend( pfx_options )
        
        return (False, options )

if __name__ == u'__main__':
    if len(sys.argv) < 2:
        print(u"usage: python spell.py <filename 1>  ... <filename n>")
        sys.exit(0)
    for file_name in sys.argv[1:]:
        Speller(file_name)
