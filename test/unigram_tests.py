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
            print letter
        
        q = ngram.LetterModels.Unigram( "data/ex.unicode" )
        q.frequency_model( )
        print unicode(q)
        assert( q.letter[u"ஷை"] + q.letter[u"சி"] == q.letter[u"ந"] )
    
if __name__ == '__main__':
    test_support.run_unittest(Letters)
