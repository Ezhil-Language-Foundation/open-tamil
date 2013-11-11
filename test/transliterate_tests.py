# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

from transliterate import *

class Yazhpanam(unittest.TestCase):
    def test_vandemataram(self):     
        tamil_words = u"வன்தே மாதரம்"
        eng_string = u'vanthE mAtharam'
        tamil_tx = iterative_transliterate(jaffna.Transliteration.table,eng_string)
        #print "]"+tamil_tx+"[", len(tamil_words), len(tamil_tx),type(tamil_tx),type(tamil_words)
        print "]"+tamil_words+"["
        assert( tamil_words == tamil_tx )
    
if __name__ == '__main__':    
    test_support.run_unittest(Yazhpanam)
