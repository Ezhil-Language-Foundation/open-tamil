#!/usr/bin/python
# (C) 2015 Muthiah Annamalai, <ezhillang@gmail.com>
#     Ezhil Language Foundation
#     
from __future__ import print_function
import sys
import codecs
import tamil
import json

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

class WordList:
    @staticmethod
    def extract_words(filename):
        ht = json.load( codecs.open(filename,'r','utf-8') )
        for word in sorted(ht.keys()):
            print(word)
        return
    
    @staticmethod
    def pull_words_from_json():
        for itr in range(1,25):
            filename = u"v%02d.json"%itr
            WordList.extract_words(filename)
        return

class WordFilter:
    @staticmethod
    def filter_and_save(word_size=4):
        match_word_length = lambda word: len(tamil.utf8.get_letters(word.strip().replace(' ',''))) == word_size
        filename = u'tamilvu_dictionary_words.txt'
        matches = []
        with codecs.open(filename,'r','utf-8') as fp:
            matches = filter( match_word_length, fp.readlines())
        with codecs.open('word_filter_%02d.txt'%word_size,'w','utf-8') as fp:
            for word in matches:
                fp.write(u'%s\n'%word.replace(' ','').strip())
        print(u'we found  %d words of length %d\n'%(len(matches),word_size))
        return
        
if __name__ == u"__main__":
    # WordList.pull_words_from_json()
    for wlen in range(3,20):
        WordFilter.filter_and_save( wlen )
    