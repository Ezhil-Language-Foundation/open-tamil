# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.dictionary import *
from solthiruthi.datastore import DTrie
from tamil import wordutils, utf8
import math
from pprint import pprint

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

    def test_all_anagrams_of_dict(self):
        wordutils.anagrams_in_dictionary(self.TVU)

class TestRevDictionary(unittest.TestCase):
    def setUp(self):
        self.ReverseTVU,self.VocabSize = DictionaryBuilder.create(reverse_TamilVU)
        self.word = u"சவால்"
        
    def test_rhymes_with(self):
        words = wordutils.rhymes_with(self.word,self.ReverseTVU)
        expected = set([u"வால்",u"சவால்",u"கொத்தவால்",u"அல்",u"நகாஅல்"])
        #for idx,x in enumerate(words):
        #   print(x)
        self.assertEqual(words,expected)

class TestWordSplitter(unittest.TestCase):
    def setUp(self):
        self.TVU,self.VocabSize = DictionaryBuilder.create(TamilVU)
        #self.TVU,self.VocabSize = DictionaryBuilder.createUsingWordList([u"தமிழ்",u"நாடு"])
        self.TMP,self.TMPVocabSize = DictionaryBuilder.createUsingWordList(['word','list','wo','rdli','st'])
        
    def test_word_split_TA(self):
        self.skipTest(u"test word split TA"))
        word = u"தமிழ்நாடு"
        parts = [[u"தமிழ்",u"நாடு"]]
        actual = wordutils.word_split(word,self.TVU)
        self.assertEqual(parts,actual)
        return
        
    def test_word_split_EN(self):
        self.skipTest("")
        word = 'wordlist';
        parts = [['wo','rdli','st'],['word','list']]
        actual = wordutils.word_split(word,self.TMP)
        self.assertEqual(parts,actual)

if __name__ == "__main__":
    unittest.main()
