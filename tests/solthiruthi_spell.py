# -*- coding: utf-8 -*-
# (C) 2016-17 Muthiah Annamalai

from opentamiltests import *
from spell import Speller, LoadDictionary, OttruSplit, Mayangoli
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
        
    def test_ottru_split(self):
        expect = [[u"ய்",u"ஆரிகழ்ந்து"], [u"யார்",u"இகழ்ந்து"] , [u"யாரிக்",u"அழ்ந்து"], [u"யாரிகழ்ந்த்",u"உ"]]
        ottru = OttruSplit(u"யாரிகழ்ந்து")
        ottru.generate_splits()
        self.assertEqual(ottru.results,expect)

    def test_mayangoli_suggests_simple(self):
        alt = Mayangoli.run(u"பளம்")
        expect = [u"பளம்",u"பழம்",u"பலம்"]
        alt = sorted(alt)
        expect = sorted(expect)
        self.assertEqual(len(alt),len(expect))
        self.assertEqual(alt,expect)
    
    def test_mayangoli_suggests_notsimple(self):
        expect_l = 3
        for w in [u"கண்ணன்",u"அப்பளம்"]:
            alt = Mayangoli.run(w)
            self.assertEqual(len(alt),expect_l)
        
    def test_mayangoli_suggests_none(self):
        expect_l = 0
        w = u"குதிகால்"
        alt = Mayangoli.run(w)
        self.assertEqual(len(alt),expect_l)
        
if __name__ == "__main__":
    unittest.main()
