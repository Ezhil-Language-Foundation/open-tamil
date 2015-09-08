# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.morphology import RemoveCaseSuffix, RemovePluralSuffix
import re
import codecs
from tamil import utf8

class RemoveSuffixTest(unittest.TestCase):
    def test_basic_suffix_stripper(self):
        obj = RemoveCaseSuffix()
        actual = []
        expected = [u"பதிவிற்",u"கட்டளைக",u"அவர்"]
        words_list = [u"பதிவிற்க்கு",u"கட்டளைகளை",u"அவர்கள்"]
        for w,x in zip(words_list,expected):
            rval = obj.removeSuffix(w)
            actual.append(rval[0])
            #self.assertTrue(rval[1])
            #print(utf8.get_letters(w),'->',rval[1])
        self.assertEqual(actual,expected)

class RemovePluralTest(unittest.TestCase):
    def test_basic_plural_stripper(self):
        obj = RemovePluralSuffix()
        expected = [u"பதிவி",u"கட்டளை",u"அவர்",u"ஜாதி",u"மரம்",u"சொல்"] 
        words_list = [u"பதிவில்",u"கட்டளைகள்",u"அவர்கள்",u"ஜாதிகள்",u"மரங்கள்",u"சொற்கள்"]
        for w,x in zip(words_list,expected):
            rval = obj.removeSuffix(w)
            self.assertTrue(rval[1])
            if not PYTHON3: print(utf8.get_letters(w),u'->',rval[1])
            self.assertEqual(rval[0], x)
        return
    
    def test_pannmai_nxt_level(self):
        #வாழ்த்துக்கள் -> வாழ்த்து
        # --- possesive noun ---
        # அவரது  -> அவர 
        #பெண்களை  -> பெண்கள்
        #ஆளுமைகளை  -> ஆளுமைகள்
        #சொற்களால் -> 
        return
    
if __name__ == "__main__":
    unittest.main()
