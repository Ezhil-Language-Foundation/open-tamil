# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

import tamil.utf8 as utf8

class Letters(unittest.TestCase):
    def test_uyirmei(self):     
        print(utf8.uyirmei(2))
        assert( utf8.uyirmei(2)  == u"கி" )

    def test_letter_extract_from_code_pts(self):
        letters = utf8.get_letters(u"கூவிளம் என்பது என்ன சீர்")
        #print "len ==== > " , len(letters)
        assert( len(letters) == 15 )
        for pos,letter in  enumerate(letters):
            print(u"%d %s"%(pos,letter))
        assert( letter == (u"ர்") )
    
    def test_tamil_letter_sizes( self ):
        assert( len(utf8.uyir_letters) == 12 )
        assert( len(utf8.mei_letters) == 18 )
        assert( len(utf8.uyir_letters) == (len(utf8.accent_symbols)-1) )
        assert( len(utf8.uyirmei_letters) == 18*12 )
        assert( len(utf8.sanskrit_letters) == 4 )
        assert( len(utf8.tamil_letters) == 321 )
        
        
if __name__ == '__main__':    
    test_support.run_unittest(Letters)
