# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
from ngram.Corpus import Corpus
from ngram import LetterModels

import tamil.utf8 as utf8

class Letters(unittest.TestCase):
    def test_basic_unigram_counts(self):
        z = Corpus("data/ex.unicode")
        for letter in z.next_tamil_letter():
            if ( LINUX ): print(letter)
        
        q = LetterModels.Unigram( "data/ex.unicode" )
        q.frequency_model( )
        if not PYTHON3:
            if ( LINUX ): print(unicode(q))
        else:
            if ( LINUX ): print( q )
        assert( q.letter[u"ஷை"] + q.letter[u"சி"] == q.letter[u"ந"] )
        del z, q

    def test_bigram_counts(self):
        q=LetterModels.Bigram("data/ex.unicode")
        q.language_model(verbose=LINUX) #suppress output
        assert( q.letter2[u"த்"][u"து"] == 7 )
        assert( q.letter2[u"சி"][u"சி"] == 0 )        
    
if __name__ == '__main__':
    if not PYTHON3:
        test_support.run_unittest(Letters)
    else:
        unittest.main()
