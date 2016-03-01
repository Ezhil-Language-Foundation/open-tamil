# -*- coding: utf-8 -*-
# (C) 2016 Muthiah Annamalai

from opentamiltests import *
from spell import Speller, LoadDictionary
from pprint import pprint
import os
from tamil import utf8

class SpellTestTamil(unittest.TestCase):
    def setUp(self):
        self.speller =  Speller(lang=u"TA",mode="web")
        
    def test_words_in_dictionary(self):
        # test if all the words are in the dictionary
        for w in [u"சவால்",u"மகதம்",u"ஆரதம்", u"பல்லவன்",u"பாதம்",u"கவணம்", u"செயல்"]:
            ok,_ = self.speller.check_word_and_suggest(w)
            self.assertTrue( ok, w )
        return
    
    def test_words_in_error(self):
        # test if the words in error are flagged
        # further test if suggestion contains the right word
        debug = False
        words_and_fixes = { u"எந்திர" : u"எந்திரம்",
                            u"செயல்பட":u"செயல்"}
        for w,right_word in words_and_fixes.items():
            notok,suggs = self.speller.check_word_and_suggest( w )
            if ( debug ):
                pprint(notok)
                pprint(suggs)
            self.assertFalse( notok, w )
            self.assertTrue( right_word in suggs, u"%s -> (%s)"%(right_word,u", ".join(suggs) ))
        return

if __name__ == "__main__":
    unittest.main()
