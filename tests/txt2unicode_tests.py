# -*- coding: utf-8 -*-
# (C) 2014 Arulalan.T
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
from tamil.txt2unicode import *

class Valluvar(unittest.TestCase):
    def test_tscii2unicode(self):        
        tscii_words = """¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû  """
        uni_words = tscii2unicode(tscii_words)
        tscii_from_uni = unicode2tscii(uni_words)
        self.assertTrue( tscii_words == tscii_from_uni)
        if ( LINUX ): print("tscii2unicode test passed 'OK'")

    def test_unicode2tscii(self):        
        tscii_words = """¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû  """
        uni_words = tscii2unicode(tscii_words)
        tscii_from_uni = unicode2tscii(uni_words)
        uni_from_tscii = tscii2unicode(tscii_from_uni)
        self.assertTrue( uni_words == uni_from_tscii )
        if ( LINUX ): print("unicode2tscii test passed 'OK'")
        
    def test_unicode2auto(self):
        uni_words = """திருவள்ளுவர் அருளிய திருக்குறள்    """
        tscii = unicode2tscii(uni_words)
        tscii_sample = tscii.split(' ')[0]
        tscii_from_auto = unicode2auto(uni_words, tscii_sample)
        self.assertTrue( tscii == tscii_from_auto )
        if ( LINUX ): print("unicode2auto test passed 'OK'")
        
    def test_auto2unicode(self):
        uni_words = """திருவள்ளுவர் அருளிய திருக்குறள்    """
        tscii = unicode2tscii(uni_words)
        tscii_sample = tscii.split(' ')[0]
        tscii_from_auto = unicode2auto(uni_words, tscii_sample)
        uni_from_auto = auto2unicode(tscii_from_auto)
        self.assertTrue( uni_words == uni_from_auto )
        if ( LINUX ): print("auto2unicode test passed 'OK'")
        
    def test_unicode2tscii_single(self):       
        tscii_words = """¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû """
        uni_words = """திருவள்ளுவர் அருளிய திருக்குறள் """
        tscii_words_from_unicode2tscii = unicode2tscii(uni_words)        
        self.assertTrue( tscii_words == tscii_words_from_unicode2tscii)
        if ( LINUX ): print("unicode2tscii_single test passed 'OK'")

    def test_indica2unicode(self):
        indica_words = """]Úk^”kÏ ∂ÚÑB ]Ú¬z≈^"""
        uni_words = indica2unicode(indica_words)
        indica_from_uni = unicode2indica(uni_words)
        self.assertTrue(indica_words == indica_from_uni)
        if ( LINUX ): print("indica2unicode test passed 'OK'")

    def test_unicode2indica(self):
        indica_words = """]Úk^”kÏ ∂ÚÑB ]Ú¬z≈^"""
        uni_words = indica2unicode(indica_words)
        indica_from_uni = unicode2indica(uni_words)
        uni_from_indica = indica2unicode(indica_from_uni)
        self.assertTrue(uni_words == uni_from_indica)
        if ( LINUX ): print("unicode2indica test passed 'OK'")

    def test_anu2unicode(self):
        anu_words = """]òk^Ókì ¶ò¹B ]òÂzÅ^"""
        uni_words = anu2unicode(anu_words)
        anu_from_uni = unicode2anu(uni_words)
        self.assertTrue(anu_words == anu_from_uni)
        if ( LINUX ): print("anu2unicode test passed 'OK'")

    def test_unicode2anu(self):
        anu_words = """]òk^Ókì ¶ò¹B ]òÂzÅ^"""
        uni_words = anu2unicode(anu_words)
        anu_from_uni = unicode2anu(uni_words)
        uni_from_anu = anu2unicode(anu_from_uni)
        self.assertTrue(uni_words == uni_from_anu)
        if ( LINUX ): print("unicode2anu test passed 'OK'")

    def test_shreelipiavid2unicode(self):
        shreelipiavid_words = """v¸ÁÒ™Áº A¸Î¯ v¸USÓÒ"""
        uni_words = shreelipiavid2unicode(shreelipiavid_words)
        shreelipiavid_from_uni = unicode2shreelipiavid(uni_words)
        self.assertTrue(shreelipiavid_words == shreelipiavid_from_uni)
        if ( LINUX ): print("shreelipiavid2unicode test passed 'OK'")

    def test_unicode2shreelipiavid(self):
        shreelipiavid_words = """v¸ÁÒ™Áº A¸Î¯ v¸USÓÒ"""
        uni_words = shreelipiavid2unicode(shreelipiavid_words)
        shreelipiavid_from_uni = unicode2shreelipiavid(uni_words)
        uni_from_shreelipiavid = shreelipiavid2unicode(shreelipiavid_from_uni)
        self.assertTrue(uni_words == uni_from_shreelipiavid)
        if ( LINUX ): print("unicode2shreelipiavid test passed 'OK'")
        
if __name__ == '__main__':
    unittest.main()
