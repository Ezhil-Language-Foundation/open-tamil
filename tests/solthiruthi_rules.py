# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.heuristics import AdjacentVowels, AdjacentConsonants, RepeatedLetters, BadIME
import re
import codecs
from tamil import utf8

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

class BadIMETest(unittest.TestCase):
    def test_invalid_word_det(self):
        not_a_word = u"ஆாள்"
        #print(utf8.get_letters(not_a_word))
        obj = BadIME()
        self.assertEqual( obj.apply(not_a_word),(False,BadIME.reason) )
    
    def test_invalid_word2(self):    
        obj = BadIME()
        not_a_word = u"தக்ஏூளா"
        self.assertEqual( obj.apply(not_a_word),(False,BadIME.reason) )
    
    def test_invalid_word3(self):
        obj = BadIME()
        not_a_word = u"தூூக்"
        self.assertEqual( obj.apply(not_a_word),(False,BadIME.reason) )
        not_a_word = u"ஏூூளா"
        self.assertEqual( obj.apply(not_a_word),(False,BadIME.reason) )
        
    def test_valid_word_det(self):
        for a_word in [u"ஆள்",u"ஏனையோருக்கும்"]:
            obj = BadIME()
            #print(utf8.get_letters(a_word))
            self.assertEqual( obj.apply(a_word), (True,None) )
        return
        
    def test_all_valid(self):
        data,DEBUG = [],False
        with codecs.open("data/project_madurai_utf8.txt","r","utf-8") as f:
            data = filter(lambda x: len(x)>2, f.readlines())
        obj = BadIME()
        for idx,line in enumerate(data):
            for col,word in enumerate( re.split(u'\s+',line) ):
                if DEBUG: 
                    print(idx,col)
                    print(utf8.get_letters(word))
                self.assertEqual(obj.apply(word),(True,None))
            pass
        pass
    
    def test_invalid_pulli_seq(self):
        not_a_word = u"ஆள்்ஆ"
        #from tamil import utf8
        #print(utf8.get_letters(not_a_word))
        obj = BadIME()
        self.assertEqual( obj.apply(not_a_word), (False,BadIME.reason) )

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
