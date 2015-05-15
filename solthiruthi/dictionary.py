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

# TODO: add methods for loading TamilVU, Wikipedia and Project Madurai
#       cleaned up data

# specify dictionary interface without specifying storage
class Dictionary:
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

    @abc.abstractmethod
    def getAllWordsIterable(self):
        for word in self.getAllWords():
            yield word
        raise StopIteration
    
    def loadWordFile(self,filename,pre_processor=None):
        # words will be loaded from the file into the Trie structure
        with codecs.open(filename,'r','utf-8') as fp:
            # 2-3 compatible
            for word in fp.readlines():
                if pre_processor:
                    self.add( pre_processor(word.strip()) )
                else:
                    self.add(word.strip())
        return

class Agarathi(Dictionary):
    def __init__(self):
        self.store = list()
        self.Finalized = False

    def add(self,word):
        if self.Finalized:
            raise Exception("dictionary is finalized. cannot add more")
        self.store.append(word)
        return

    def isWord(self,word):
        return word in self.store

    def finalize(self):
        self.store = set(self.store)

    @abc.abstractmethod
    def getAllWords(self):
        return

    @abc.abstractmethod
    def getAllWordsIterable(self):
        for word in self.getAllWords():
            yield word
        raise StopIteration

    def loadWordFile(self,filename,pre_processor=None):
        # words will be loaded from the file into the Trie structure
        with codecs.open(filename,'r','utf-8') as fp:
            # 2-3 compatible
            for word in fp.readlines():
                if pre_processor:
                    self.add( pre_processor(word.strip()) )
                else:
                    self.add(word.strip())
        return

class TamilVU(Agarathi):
    def __init__(self):
        self.store = dict()

class Wikipedia(Agarathi):
    def __init__(self):
        self.store = dict()
