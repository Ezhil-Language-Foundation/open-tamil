## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
## 
from __future__ import print_function
import abc
import sys
import codecs
from pprint import pprint

PYTHON3 = (sys.version[0] == '3')

# TODO: add methods for loading TamilVU, Wikipedia and Project Madurai
#       cleaned up data

# specify dictionary interface without specifying storage
class Dictionary:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def add(self,word,defns):
        return
    
    @abc.abstractmethod
    def isWord(self,word):
        return
    
    @abc.abstractmethod
    def getAllWords(self):
        return
        
    @abc.abstractmethod
    def getAllWordsIterable(self):
        for word in self.getAllWords():
            yield word
        raise StopIteration
    
    def loadWordFile(self,filename):
        # words will be loaded from the file into the Trie structure
        with codecs.open(filename,'r','utf-8') as fp:
            # 2-3 compatible
            for word in fp.readlines():
                self.add(word.strip())
        return

class TamilVU(Dictionary):
    def __init__(self):
        self.store = dict()
    
