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
        print("tscii2unicode test passed 'OK'")

    def test_unicode2tscii(self):        
        tscii_words = """¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû  """
        uni_words = tscii2unicode(tscii_words)
        tscii_from_uni = unicode2tscii(uni_words)
        uni_from_tscii = tscii2unicode(tscii_from_uni)
        self.assertTrue( uni_words == uni_from_tscii )
        print("unicode2tscii test passed 'OK'")
        
    def test_unicode2auto(self):
        uni_words = """திருவள்ளுவர் அருளிய திருக்குறள்    """
        tscii = unicode2tscii(uni_words)
        tscii_sample = tscii.split(' ')[0]
        tscii_from_auto = unicode2auto(uni_words, tscii_sample)
        self.assertTrue( tscii == tscii_from_auto )
        print("unicode2auto test passed 'OK'")
        
    def test_auto2unicode(self):
        uni_words = """திருவள்ளுவர் அருளிய திருக்குறள்    """
        tscii = unicode2tscii(uni_words)
        tscii_sample = tscii.split(' ')[0]
        tscii_from_auto = unicode2auto(uni_words, tscii_sample)
        uni_from_auto = auto2unicode(tscii_from_auto)
        self.assertTrue( uni_words == uni_from_auto )
        print("auto2unicode test passed 'OK'")
        
    def test_unicode2tscii_single(self):       
        tscii_words = """¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû """
        uni_words = """திருவள்ளுவர் அருளிய திருக்குறள் """
        tscii_words_from_unicode2tscii = unicode2tscii(uni_words)        
        self.assertTrue( tscii_words == tscii_words_from_unicode2tscii)
        print("unicode2tscii_single test passed 'OK'")
        
if __name__ == '__main__':
    if PYTHON3:
        print("####### TEST FILTERED FOR PYTHON 3 #############")
    else:
        test_support.run_unittest(Valluvar)   
