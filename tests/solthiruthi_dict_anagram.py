# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.dictionary import *
from tamil import wordutils, utf8
import math

class TestAnagramsWDict(unittest.TestCase):
    def setUp(self):
        self.AllTrueDictionary = wordutils.DictionaryWithPredicate(lambda x: True)
        self.TVU,self.TVU_size = DictionaryBuilder.create(TamilVU)
        self.word = u"சவால்"
        self.length = len(utf8.get_letters(self.word))
    
    def tearDown(self):
        del self.TVU
    
    def test_anagram_everything(self):
        actual = list(wordutils.anagrams(self.word,self.AllTrueDictionary))
        self.assertEqual( len(actual), math.factorial(self.length) )
        self.assertEqual( math.factorial(self.length), 3*2*1 )
    
    def test_anagram_challenge(self):
        expected = [u"சவால்",u"வாசல்"]
        actual = list(wordutils.anagrams(self.word,self.TVU))
        self.assertEqual(sorted(expected),sorted(actual))
    
    def test_combinagrams(self):
        word = u"சவால்";
        expected = 5;
        actual = list(wordutils.combinagrams(word,self.TVU))
        self.assertEqual( len(actual), expected )
        
if __name__ == "__main__":
    unittest.main()
