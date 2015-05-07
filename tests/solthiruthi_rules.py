# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.heuristics import AdjacentVowels

class AdjacentUyirgalTest(unittest.TestCase):
    def test_word_in_error(self):
        obj = AdjacentVowels()
        rval = obj.apply(u"அஇங்ஞாடி")
        self.assertEqual(len(rval),2)
        self.assertTrue(rval[1])
        self.assertFalse(rval[0])
        
    def test_word(self):
        obj = AdjacentVowels()
        in_words = u"டைட்டானிக் படத்தில் அஇங்ஞாடி அங்ஞாடிஇ வரும் ஜேக் மற்றும் ஆஅக்காள் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        actual = [obj.apply(word)[0] for word in in_words]
        expected = [True for i in range(0,len(in_words))]
        expected[2] = False
        expected[7] = False
        self.assertEqual( actual, expected )
    
if __name__ == "__main__":
    unittest.main()
