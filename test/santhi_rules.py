#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# (C) 2013-2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
from tamil.utils.santhirules import joinWords

class SantheeRules(unittest.TestCase):
    def test_grammar_conjugation( self ):
        a = u'என்ன'
        b = u'என்ன'
        w = joinWords(a, b).encode('utf8')
        
        print( w )
        self.assertTrue( w.decode('utf-8') == u'என்னென்ன')
        
        # write to file
        # A = a.encode('utf8')
        # B = b.encode('utf8')
        # 
        # f = open('out1.txt', 'a')
        # f.write(A + ' + ' + B + ' = ' + w+'\n')
        # f.close()

if __name__ == '__main__':    
    if not PYTHON3:
        test_support.run_unittest(SantheeRules)
    else:
        unittest.main()
