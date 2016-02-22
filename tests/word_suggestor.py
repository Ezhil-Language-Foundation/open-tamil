# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

from __future__ import print_function
from opentamiltests import *

from solthiruthi.suggestions import norvig_suggestor

class WordsSuggestor(unittest.TestCase):
    def test_Norvig_suggestor( self ):
        word = u"ஆங்கிலம்"
        opts1 = norvig_suggestor( word, None, 1)
        #too much memory
        #opts2 = norvig_suggestor( word, None, 2)
        opts2 = []
        self.assertEqual( list( map(len,[opts1, opts2])),  [5150, 0] )
        return

if __name__ == '__main__':
    unittest.main()
