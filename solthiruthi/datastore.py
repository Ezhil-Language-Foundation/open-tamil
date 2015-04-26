## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
## 
from __future__ import print_function

import sys
import copy
import argparse
from tamil import utf8
from pprint import pprint

PYTHON3 = (sys.version[0] == '3')

def getidx(letter):
    for itr in range(0,utf8.TA_LETTERS_LEN):
        if utf8.tamil_letters[itr] == letter:
            return itr
    raise Exception("Cannot find letter in Tamil arichuvadi")    
    
class TamilTrie:
    "Store a list of words into the Trie data structure"
    @staticmethod
    def mk_empty_trie(alpha_len):
        return [[False,None] for i in range(alpha_len)]
    
    def __init__(self, get_idx = getidx, alphabet_len = utf8.TA_LETTERS_LEN):
        self.L = alphabet_len
        self.trie = TamilTrie.mk_empty_trie(self.L)
        self.word_limits = TamilTrie.mk_empty_trie(self.L)
        self.getidx = get_idx
    def isWord(self,word):
        # see if @word is present in the current Trie; return True or False
        letters = utf8.get_letters(word)
        wLen = len(letters)
        ref_trie = self.trie
        ref_word_limits = self.word_limits
        for itr,letter in enumerate(letters):
            idx = self.getidx( letter )
            print(idx, letter)
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
            idx = self.getidx( letter )
            #print(idx, letter)
            ref_trie[idx][0] = True
            if itr == (wLen-1):
                break
            if not ref_trie[idx][1]:
                ref_trie[idx][1] = TamilTrie.mk_empty_trie(self.L)
                ref_word_limits[idx][1] = TamilTrie.mk_empty_trie(self.L)
            ref_trie = ref_trie[idx][1]
            ref_word_limits = ref_word_limits[idx][1]
        ref_word_limits[idx][0] = True
        #pprint( self.trie )
        #pprint( self.word_limits )
        
def do_stuff_3letter():    
    eng_idx = lambda x: ord(x) - ord('a')
    obj = TamilTrie(eng_idx,3)
    pprint( obj.trie )
    [obj.add(w) for w in ['a','ab','abc','bbc']]#['apple','amma','appa','love','strangeness']]    
    return obj

def do_stuff():    
    eng_idx = lambda x: ord(x) - ord('a')
    obj = TamilTrie(eng_idx,26)
    pprint( obj.trie )
    [obj.add(w) for w in ['apple','amma','appa','love','strangeness']]
    all_words = ['apple','amma','appa','love','strangeness','purple','yellow','tail','tuna','maki','ammama']
    print("###### fooooooooooooooooooooooooooooooo ################################")
    for w in all_words:
        print(w,str(obj.isWord(w)))
    #pprint( obj.trie )
    return obj
    
if __name__ == u"__main__":
    do_stuff()
