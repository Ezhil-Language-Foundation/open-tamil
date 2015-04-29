## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
## 
from __future__ import print_function
import abc
import sys
import codecs
import argparse
from tamil import utf8
from pprint import pprint

PYTHON3 = (sys.version[0] == '3')

class Trie:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def add(self,word):
        return
    
    @abc.abstractmethod
    def isWord(self,word):
        return
    
    @abc.abstractmethod
    def getAllWords(self):
        return

    @staticmethod
    def mk_empty_trie(alpha_len):
        return [[False,None] for i in range(alpha_len)]
        
    def loadWordFile(self,filename):
        # words will be loaded from the file into the Trie structure
        with codecs.open(filename,'r','utf-8') as fp:
            map( lambda word: self.add(word.strip()), fp.readlines() )
        return

class SlowTrie(Trie):
    " deque trie where number of nodes grows with time "
    pass
    
class TamilTrie(Trie):
    "Store a list of words into the Trie data structure"
    
    @staticmethod
    def buildEnglishTrie(nalpha=26):
        # utility method
        to_eng = lambda x: chr(x+ord('a'))
        eng_idx = lambda x: ord(x) - ord('a')
        obj = TamilTrie(eng_idx,to_eng,nalpha)
        return obj
        
    def __init__(self, get_idx = utf8.getidx, invert_idx = utf8.tamil, alphabet_len = utf8.TA_LETTERS_LEN):
        self.L = alphabet_len
        self.trie = Trie.mk_empty_trie(self.L)
        self.word_limits = Trie.mk_empty_trie(self.L)
        self.getidx = get_idx
        self.invertidx = invert_idx
        
    def getAllWords(self):
        # list all words in the trie structure in DFS fashion
        all_words = []
        self.getAllWordsHelper(self.trie,self.word_limits,prefix=[],all_words=all_words)
        return all_words
        
    def getAllWordsHelper(self,ref_trie,ref_word_limits,prefix,all_words):
        for letter_pos in range(0,len(ref_trie)):
            if ref_trie[letter_pos][0]:
                letter = self.invertidx( letter_pos )
                prefix.append( letter )
                if ref_word_limits[letter_pos][0]:
                    all_words.append( u"".join(prefix) )
                if ref_trie[letter_pos][1]:
                    # DFS
                    self.getAllWordsHelper(ref_trie[letter_pos][1],ref_word_limits[letter_pos][1],prefix,all_words)
                if len(prefix) > 0:
                    prefix.pop()
            else:
                pass
        return
    
    def isWord(self,word):
        # see if @word is present in the current Trie; return True or False
        letters = utf8.get_letters(word)
        wLen = len(letters)
        ref_trie = self.trie
        ref_word_limits = self.word_limits
        for itr,letter in enumerate(letters):
            idx = self.getidx( letter )
            #print(idx, letter)
            if itr == (wLen-1):
                break
            if not ref_trie[idx][1]:
                return False #this branch of Trie did not exist
            ref_trie = ref_trie[idx][1]
            ref_word_limits = ref_word_limits[idx][1]
        return ref_word_limits[idx][0]
        
    def add(self,word):
        # trie data structure is built here
        #print("*"*30,"adding","*"*30)
        letters = utf8.get_letters(word)
        wLen = len(letters)
        ref_trie = self.trie
        ref_word_limits = self.word_limits
        for itr,letter in enumerate(letters):
            try:
                idx = self.getidx( letter )
            except Exception as exp:
                continue
            #print(idx, itr)
            ref_trie[idx][0] = True
            if itr == (wLen-1):
                break
            if not ref_trie[idx][1]:
                ref_trie[idx][1] = Trie.mk_empty_trie(self.L)
                ref_word_limits[idx][1] = Trie.mk_empty_trie(self.L)
            ref_trie = ref_trie[idx][1]
            ref_word_limits = ref_word_limits[idx][1]
        ref_word_limits[idx][0] = True
        #pprint( self.trie )
        #pprint( self.word_limits )
        
def do_stuff():
    from pprint import pprint    
    obj = TamilTrie.buildEnglishTrie()
    #pprint( obj.trie )
    [obj.add(w) for w in ['apple','amma','appa','love','strangeness']]
    all_words = ['apple','amma','appa','love','strangeness','purple','yellow','tail','tuna','maki','ammama']
    print("###### dostuff ################################")
    for w in all_words:
        print(w,str(obj.isWord(w)))    
    #pprint( obj.trie )
    pprint( obj.getAllWords() )
    return obj
    
def do_load():
    " 4 GB program - very inefficient "
    obj = TamilTrie()
    obj.loadWordFile('data/tamilvu_dictionary_words.txt')
    print(len(obj.getAllWords()))

if __name__ == u"__main__":
    do_stuff()
