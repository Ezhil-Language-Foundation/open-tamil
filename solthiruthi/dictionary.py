## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
## 
from __future__ import print_function
import abc
import sys
import codecs
from pprint import pprint

from . import resources
from . import datastore

PYTHON3 = (sys.version[0] == '3')
    
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
    def getDictionaryPath(self):
        return
    
    def getSize(self):
        count = 0
        for word in self.getAllWordsIterable():
            count += 1
        return count
    
    def getAllWordsIterable(self):
        for word in self.getAllWords():
            yield word
        raise StopIteration
    
    def loadWordFile(self,pre_processor=None):
        filename = self.getDictionaryPath()
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
    def __init__(self,dictionary_path):
        self.dictionary_path = dictionary_path
        self.store = datastore.DTrie()
        self.Finalized = False
    
    def add(self,word):
        if self.Finalized:
            raise Exception("dictionary is finalized. cannot add more")
        self.store.add(word)
        return
    
    def isWord(self,word):
        return self.store.isWord(word)
    
    def finalize(self):
        self.Finalized = True
    
    def getDictionaryPath(self):
        return self.dictionary_path
    
    def getAllWords(self):
        return self.store.getAllWords()
    
    def getAllWordsIterable(self):
        for word in self.store.getAllWordsIterable():
            yield word
        raise StopIteration

class TamilVU(Agarathi):
    def __init__(self):
        Agarathi.__init__(self,resources.DICTIONARY_DATA_FILES['tamilvu'])
        
class Madurai(Agarathi):
    def __init__(self):
        Agarathi.__init__(self,resources.DICTIONARY_DATA_FILES['projmad'])
        
class Wikipedia(Agarathi):
    def __init__(self):
        Agarathi.__init__(self,resources.DICTIONARY_DATA_FILES['wikipedia'])

# Methods for loading TamilVU, Wikipedia and Project Madurai cleaned up data
class DictionaryBuilder:
    @staticmethod
    def create(DType):
        if not callable(DType):
            raise Exception(u"input @DType should be a class reference, or a factory function")
        obj = DType()
        obj.loadWordFile()
        return [obj,obj.getSize()]
