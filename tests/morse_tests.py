#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# (C) 20195 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 
import unittest
import tamilmorse

class MorseUnitTest(unittest.TestCase):
    def test_fwd(self):
        data = tamilmorse.encode(u'அடி')
        expected = u'--.-.. ...-...'
        self.assertEqual( expected, data )
        
    def test_back(self):
        expected = u'அ டி'
        data = tamilmorse.decode( u'--.-.. ...-...' )
        self.assertEqual( data, expected )        

if __name__ == "__main__":
    unittest.main()
