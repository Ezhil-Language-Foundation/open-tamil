# -*- coding: utf-8 -*-
# (C) 2015-2016 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.morphology import RemoveCaseSuffix, RemovePluralSuffix
from solthiruthi.morphology import RemovePrefix, CaseFilter
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
        expected = [u"பதிவி",u"கட்டளை",u"அவர்",u"ஜாதி",u"மரம்",u"சொல்",u"சிற்பம்"] 
        words_list = [u"பதிவில்",u"கட்டளைகள்",u"அவர்கள்",u"ஜாதிகள்",u"மரங்கள்",u"சொற்கள்",u"சிற்பங்கள்"]
        for w,x in zip(words_list,expected):
            rval = obj.removeSuffix(w)
            self.assertTrue(rval[1])
            #if not PYTHON3: print(utf8.get_letters(w),u'->',rval[1])
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

class RemovePrefixTest(unittest.TestCase):
    def test_basic_prefix_stripper(self):
        obj = RemovePrefix()
        #பேரின்பம் ->   இன்பம், 
        #u"":u"",u"":u"",u"":u"",u"":u"",u"":u"",u"":u"",
        prefix_removal_map = {u"எக்காலம்":u"காலம்",u"இக்காலம்":u"காலம்",u"அக்காலம்":u"காலம்",\
                            u"மாமனிதன்":u"மனிதன்",u"சின்னஜமீன்":u"ஜமீன்",u"அதிவேகம்":u"வேகம்",\
                            u"சிறுகுன்றம்":u"குன்றம்",u"மாமரம்":u"மரம்"}
        
        no_removal_map = {}
        # update no-prefix-to-be-removed / no-change values
        for v in prefix_removal_map.values():
            no_removal_map[v] = v
        
        # prefix removal does not happen for these words
        words_list = list(no_removal_map.keys())
        for idx,w in enumerate(words_list):
            rval = obj.removePrefix(w)
            self.assertFalse(rval[1])
            expected = no_removal_map[w]
            self.assertEqual(rval[0], expected)
        
        # prefix removal to happen as expected
        words_list = list(prefix_removal_map.keys())
        for idx,w in enumerate(words_list):
            rval = obj.removePrefix(w)
            self.assertTrue(rval[1])
            expected = prefix_removal_map[w]
            self.assertEqual(rval[0], expected)
        return

class CaseFilterTest(unittest.TestCase):
    def test_basic_case_(self):
        obj = RemovePluralSuffix()
        objf = CaseFilter(obj)
        expected = [u"பதிவி",u"கட்டளை",u"அவர்"]
        words_list = [u"பதிவில்",u"கட்டளைகள்",u"அவர்கள்"]
        for w,x in zip(words_list,expected):
            rval = obj.removeSuffix(w)
            trunc_word = objf.apply( w )
            self.assertEqual( trunc_word ,rval[0] )
        return
        
if __name__ == "__main__":
    unittest.main()
