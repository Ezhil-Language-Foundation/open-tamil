# -*- coding: utf-8 -*-
# 
# (C) முத்தையா அண்ணாமலை 2013-2015
# 
# N-gram language model for Tamil letters

import tamil
import copy
from .Corpus import Corpus

class Letters:
    def __init__(self,filename):
        self.letter = dict()
        self.letter.update(zip( tamil.utf8.tamil_letters,
                                map(lambda x : 0, tamil.utf8.tamil_letters) ) )
        self.corpus = Corpus( filename )

    def __del__(self):
        try:
            del self.corpus
        except Exception:
            pass

    def __unicode__( self ):
        op = u""
        for lett,freq in self.letter.items():
            op = op + u"%s => %d\n"%(lett,freq)
        print(max(self.letter.values()))
        return op

class Unigram(Letters):
    def __init__(self,filename):
        Letters.__init__(self,filename)
        
    def frequency_model( self ):
        """ build a letter frequency model for Tamil letters from a corpus """
        # use a generator in corpus
        for next_letter in self.corpus.next_tamil_letter():
            # update frequency from corpus
            self.letter[next_letter] = self.letter[next_letter] + 1
        
class Bigram(Unigram):
    def __init__(self,filename):
        Unigram.__init__(self,filename)
        self.letter2 = dict()
        for k in tamil.utf8.tamil_letters:
            self.letter2[k] = copy.copy( self.letter )
    
    def language_model(self,verbose=True):
        """ builds a Tamil bigram letter model """
        # use a generator in corpus
        prev = None
        for next_letter in self.corpus.next_tamil_letter():
            # update frequency from corpus
            if prev:
                self.letter2[prev][next_letter] += 1
                if ( verbose ) :
                    print(prev)
                    print(next_letter)
                    print( self.letter2[prev][next_letter] )
            prev = next_letter #update always
        return
