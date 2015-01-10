# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

import tamil.utf8 as utf8

class Letters(unittest.TestCase):
    def test_basic_unigram_counts(self):
        z = ngram.Corpus("data/ex.unicode")
        for letter in z.next_tamil_letter():
            print(letter)
        
        q = ngram.LetterModels.Unigram( "data/ex.unicode" )
        q.frequency_model( )
        if not PYTHON3:
            print(unicode(q))
        else:
            print( q )
        assert( q.letter[u"ஷை"] + q.letter[u"சி"] == q.letter[u"ந"] )

    def test_bigram_counts(self):
        q=ngram.LetterModels.Bigram("data/ex.unicode")
        q.language_model()
        assert( q.letter2[u"த்"][u"து"] == 7 )
        assert( q.letter2[u"சி"][u"சி"] == 0 )        
    
if __name__ == '__main__':
    test_support.run_unittest(Letters)
