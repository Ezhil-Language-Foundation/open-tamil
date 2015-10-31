# -*- coding: utf-8 -*-
# (C) 2013-2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
import tamil.utf8 as utf8 
from tamil.tscii import TSCII
import codecs

class NumeralBugsTest(unittest.TestCase):
    def runTest(self,var,nos):
        for numerStr,num in zip(var,nos):
            print('Testing ---> ',num)
            self.assertEqual( numerStr, tamil.numeral.num2tamilstr( num ), num )
        return
    
    def test_float_USA(self):
        # used to convert with actual numeral + suffix "பூஜ்ஜியம்"
        aspen = int('1234')
        swayambu_int = tamil.numeral.num2tamilstr( aspen )
        expected = u"ஓர் ஆயிரத்தி இருநூற்றி முப்பத்தி நான்கு"
        self.assertEqual( swayambu_int, expected )

        # used to convert with actual numeral + suffix "பூஜ்ஜியம்"
        aspen_float = float('1234')
        swayambu = tamil.numeral.num2tamilstr( aspen_float )
        expected = u"ஓர் ஆயிரத்தி இருநூற்றி முப்பத்தி நான்கு"
        self.assertEqual( swayambu, swayambu_int )
    
if __name__ == '__main__':        
    unittest.main()
