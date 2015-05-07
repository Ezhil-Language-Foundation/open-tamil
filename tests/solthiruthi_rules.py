# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.heuristics import AdjacentVowels, AdjacentConsonants, RepeatedLetters

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

class AdjacentMeiAgaram(unittest.TestCase):
    def test_word_in_error(self):
        obj = AdjacentConsonants()
        rval = obj.apply(u"அஇங்ங்ஞாடி")
        self.assertEqual(len(rval),2)
        self.assertFalse(rval[0])
        self.assertTrue(rval[1])
        
    def test_word(self):
        obj = AdjacentConsonants()
        in_words = u"டைட்டானிக் படத்தில் அஇங்ஞாடி அஇங்ங்ஞாடி அங்ஞாடிஇ ஜேக் மற்றும் ஆஅக்காள் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        actual = [obj.apply(word)[0] for word in in_words]
        expected = [True for i in range(0,len(in_words))]
        expected[1] = False
        expected[3] = False
        expected[-1] = False
        self.assertEqual( expected, actual )

class RepeatedLettersTest(unittest.TestCase):
    def test_word_in_error(self):
        obj = RepeatedLetters()
        rval = obj.apply(u"அஇங்ங்ஞாடி")
        self.assertEqual(len(rval),2)
        self.assertFalse(rval[0])
        self.assertTrue(rval[1])
        
    def test_word(self):
        obj = RepeatedLetters()
        in_words = u"டைட்டானிக்க் பபடத்தில் அஇங்ஞாடி அஇங்ங்ஞாடி அங்ஞாடிஇ ஜேக் மற்றும் ஆஅக்காள் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        actual = [obj.apply(word)[0] for word in in_words]
        expected = [True for i in range(0,len(in_words))]
        expected[0] = False
        expected[1] = False
        expected[3] = False
        self.assertEqual( expected, actual )
    
if __name__ == "__main__":
    unittest.main()
