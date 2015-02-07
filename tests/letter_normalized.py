# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from __future__ import print_function
from opentamiltests import *

class Words(unittest.TestCase):
    def test_all_tamil( self ):
        non_norm = u"ப" +  u"ெ" + u"ா" + u"பொ"
        self.assertTrue( tamil.utf8.is_normalized(u"சம்மதம்") )
        self.assertTrue( tamil.utf8.is_normalized(non_norm[0]) )
        self.assertTrue( tamil.utf8.is_normalized(non_norm[0:1]) )
        self.assertTrue( tamil.utf8.is_normalized(non_norm[0:2]) )
        self.assertFalse( tamil.utf8.is_normalized(non_norm[0:3]) )
        self.assertFalse( tamil.utf8.is_normalized(non_norm) )
        return

    def test_long_str_embedded( self ):
        o_data = "This file is part of 'open-tamil' package tests"
        long_non_norm = u"ப" +  u"ெ" + u"ா" + u"பொ"
        data = o_data + long_non_norm + o_data
        self.assertFalse( tamil.utf8.is_normalized( data ) )
        self.assertTrue(tamil.utf8.is_normalized( o_data ) )
        self.assertFalse(tamil.utf8.is_normalized( long_non_norm ) )
        return

if __name__ == '__main__':        
    unittest.main()
