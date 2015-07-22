# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from __future__ import print_function
from opentamiltests import *
from tamil import wordutils

import math

class TestWordUtils(unittest.TestCase):
    def test_perms( self ):
        res = [u'123',u'132',u'213',u'231',u'312',u'321']
        self.assertEqual( list(wordutils.permutations(u'1 2 3'.split(u' '))),res)
    def test_perms_length(self):
        count = 0
        for perm in wordutils.permutations('1 2 3 4 5 6'.split(' ')):
            count += 1
        self.assertEqual(count,math.factorial(6))
    def test_tamil_perms( self ):
        res = [u'\u0ba4\u0bae\u0bbf\u0bb4\u0bcd', u'\u0ba4\u0bb4\u0bcd\u0bae\u0bbf', u'\u0bae\u0bbf\u0ba4\u0bb4\u0bcd', u'\u0bae\u0bbf\u0bb4\u0bcd\u0ba4',u'\u0bb4\u0bcd\u0ba4\u0bae\u0bbf', u'\u0bb4\u0bcd\u0bae\u0bbf\u0ba4']

        self.assertEqual( list(wordutils.permutations([u'த',u'மி',u'ழ்'])),res)
        
if __name__ == '__main__':        
    unittest.main()
