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
    
    def getAllWordsIterable(self):
        for word in self.getAllWords():
            yield word
        raise StopIteration
    
    @staticmethod
    def mk_empty_trie(alpha_len):
        return [[False,None] for i in range(alpha_len)]
        
    def loadWordFile(self,filename):
        # words will be loaded from the file into the Trie structure
        with codecs.open(filename,'r','utf-8') as fp:
            map( lambda word: self.add(word.strip()), fp.readlines() )
        return

class Node:
    def __init__(self):
        self.__dict__={'alphabets':{},'is_word':{}}
    
class DTrie(Trie):
    """ trie where number of alphabets at each nodes grows with time; 
        implementation uses a dictionary
    """
    def __init__(self):
        self.trie = Node() #root node
    
    def isWord(self,word):
        ref_trie = self.trie
        letters = utf8.get_letters(word)
        wLen = len(letters)
        rval = False
        for idx,letter in enumerate(letters):
            #print(ref_trie.alphabets.get(letter,"?"))
            rval = ref_trie.is_word.get(letter,False)
            ref_trie = ref_trie.alphabets.get(letter,None)
            if not ref_trie:
                return False
        return rval
    
    def add(self,word):
        ref_trie = self.trie
        letters = utf8.get_letters(word)
        wLen = len(letters)
        for idx,letter in enumerate(letters):                
            value = ref_trie.alphabets.get(letter,None)
            if not value:
                ref_trie.alphabets[letter] = Node()
                ref_trie.is_word[letter]=False
            if idx < (wLen-1): 
                ref_trie = ref_trie.alphabets[letter]
        ref_trie.is_word[letter] = True
        return
    
    def getAllWords(self):
        # list all words in the trie structure in DFS fashion
        all_words = []
        self.getAllWordsHelper(self.trie,prefix=[],all_words=all_words)
        return all_words
        
    def getAllWordsHelper(self,ref_trie,prefix,all_words):
        for letter in sorted(ref_trie.alphabets.keys()):
            prefix.append( letter )
            if ref_trie.is_word[letter]:
                all_words.append( u"".join(prefix) )
            if ref_trie.alphabets[letter]:
                # DFS
                self.getAllWordsHelper(ref_trie.alphabets[letter],prefix,all_words)
            prefix.pop()
        return
        
    def getAllWordsIterable(self):
        return self.getAllWordsIterableHelper(self.trie,[])
        
    def getAllWordsIterableHelper(self,ref_trie,prefix):
        for letter in sorted(ref_trie.alphabets.keys()):
            prefix.append( letter )
            if ref_trie.is_word[letter]:
                yield u"".join(prefix)
            if ref_trie.alphabets[letter]:
                # DFS
                for word in self.getAllWordsIterableHelper(ref_trie.alphabets[letter],prefix):
                    yield word
            prefix.pop()
        raise StopIteration
        
    
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
                prefix.pop()
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
    obj = DTrie() #TamilTrie.buildEnglishTrie()
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
    obj = DTrie() #TamilTrie()
    obj.loadWordFile('data/tamilvu_dictionary_words.txt')
    print(len(obj.getAllWords()))

if __name__ == u"__main__":
    do_load()
