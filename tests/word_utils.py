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
        res = [u'தமிழ்',u'தழ்மி',u'மிதழ்',u'மிழ்த',u'ழ்தமி',u'ழ்மித']
        self.assertEqual( list(wordutils.permutations([u'த',u'மி',u'ழ்'])),res)
        
    def test_tamil_perms2( self ):
        res = [u'தமிழ்',u'தழ்மி',u'மிதழ்',u'மிழ்த',u'ழ்தமி',u'ழ்மித']
        self.assertEqual( list(wordutils.tamil_permutations(res[0])),res)
        
    def test_perms_xception(self):
        if PYTHON2_6:
            # exception API is different in Python 2.6
            return
        with self.assertRaises(Exception):
            list( wordutils.permutations( u'அது சரம் (str) வகையாக இருந்தால் tamil.utf8.get_letters() பயன்பாட்டை முதலில் உபயொகிக்க!' ) )
        
if __name__ == '__main__':        
    unittest.main()
