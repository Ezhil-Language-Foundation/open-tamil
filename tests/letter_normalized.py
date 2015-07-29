# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from __future__ import print_function
from opentamiltests import *

class Words(unittest.TestCase):
    def test_lexico_compare( self ):
        res = [0,1,-1]
        self.assertEqual( list(map( lambda x: tamil.utf8.compare_words_lexicographic( u"சம்மத", x),[u"சம்மத",u"சம்த",u"தசம்"])),res)
    
    def test_unicode_tamil(self):
        val = []
        str_in = u'LnX3.14-சம்மதசம்ததசம்'
        for i in range(0,len(str_in)):
            letter = str_in[i]
            val.append( tamil.utf8.is_tamil_unicode( letter ) )
        
        act = [False,
               False,
               False,
               False,
               False,
               False,
               False,
               False,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True]
        
        self.assertEqual( val, act )
        return
    
    def test_isalnum( self ):
        self.assertTrue( tamil.utf8.istamil_alnum('LiNuX') )
        self.assertFalse( tamil.utf8.istamil_alnum('3.14159') )
    
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

    def test_rev_words(self):
        rhymie = [(u"மாங்குயில்",u"ல்யிகுங்மா"),(u"பூங்குயில்",u"ல்யிகுங்பூ"), (u"அல்லவா",u"வாலல்அ"),\
                  (u"செல்வாயா",u"யாவால்செ"), (u"சொல்வாயா",u"யாவால்சொ")]
        for k,v in rhymie:
            self.assertEqual( tamil.utf8.reverse_word(k), v)
            self.assertEqual( tamil.utf8.reverse_word(v), k)
        return

if __name__ == '__main__':        
    unittest.main()
