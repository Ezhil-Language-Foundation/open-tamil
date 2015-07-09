# -*- coding: utf-8 -*-
# (C) 2013-2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 
from __future__ import print_function
# setup the paths
from opentamiltests import *
import tamil

class PesumYengalTest(unittest.TestCase):
    def test_friend_of_rama( self ):
        ramanujan = 1729
        actual_fn = []
        gometra = tamil.numeral.num2tamilstr( ramanujan, actual_fn )
        expected_fn = ['one_thousand_prefix','thousands_1','hundreds_suffix_6','tens_suffix_0','units_9']
        expected = u"ஓர் ஆயிரத்தி எழுநூற்று இருபத்தி ஒன்பது"
        self.assertEqual( gometra, expected )
        self.assertEqual( expected_fn, actual_fn )
    
    def test_1000_45(self):
        # Python3 has some rounding issues
        number = 1000.45
        numerale = u'ஓர் ஆயிரம் புள்ளி நான்கு ஐந்து'
        exp_filenames = ['one_thousand_prefix','thousands_0','pulli','units_4','units_5']
        actual_fn = []
        numeral = tamil.numeral.num2tamilstr( number, actual_fn )
        #print("numeral",numeral)
        #print("/".join(actual_fn))
        self.assertEqual( numeral[0:len(numerale)], numerale )
        self.assertEqual( exp_filenames, actual_fn[0:len(exp_filenames)] )

if __name__ == "__main__":
    unittest.main()
