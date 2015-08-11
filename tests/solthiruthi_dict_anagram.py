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

class TestWordSplitterEnglish(unittest.TestCase):
    def setUp(self):
        self.ENG,self.ENG_size = DictionaryBuilder.create(EnglishLinux)
        self.ENG.add(u'erin')
        
    def test_anagram_challenge(self):
        word = 'draw'
        expected = ['draw','ward']
        actual = list(wordutils.anagrams(word,self.ENG))
        self.assertEqual(sorted(expected),sorted(actual))
        
    def test_word_split_EN(self):
        word = 'wordlist';
        parts = [['word','list']]
        actual = wordutils.word_split(word,self.ENG)
        self.assertEqual(parts,actual)
    
    def test_word_split_EN2(self):
        word = 'wordlist';
        parts = ['word','list']
        actual = wordutils.greedy_split(word,self.ENG)
        self.assertEqual(parts,actual)

    def test_nosplit_1(self):
        word = 'motherr';'nastia';
        parts = []
        actual = wordutils.greedy_split(word,self.ENG)
        self.assertEqual(parts,actual)
    
    def test_conjunctions(self):
        word = u"motherrand"
        parts = [[u'moth',u'errand'],[u'mother',u'rand']]
        actual = wordutils.word_split(word,self.ENG)
        self.assertEqual(parts,actual)
        return
    
    def test_twoway_EN2(self):
        word = u'motherinlaw';
        parts = [[u'moth',u'erin',u'law'],[u'mother',u'in',u'law']]
        actual = wordutils.word_split(word,self.ENG)
        self.assertEqual(parts,actual)
        
class TestGreedyWordSplitter(unittest.TestCase):
    def setUp(self):
        self.TVU,self.VocabSize = DictionaryBuilder.create(TamilVU)
        
    def test_greedy_split_TA(self):
        word_parts = ((u"தாய்நாடு", [u"தாய்",u"நாடு"]),
                       (u"தமிழ்நாடு", [u"தமிழ்",u"நாடு"]),
                       (u"தமிழ்நாடுஆமை",[u"தமிழ்",u"நாடு",u"ஆமை"]),
                       (u"பாரதமாதா",[u"பா",u"ர",u"த",u"மாதா"]),
                       (u"பல்கலைகழகம்",[u"பல்",u"கலை",u"கழகம்"])
                      );
        
        for word,parts in word_parts:
            if LINUX:
                pass
                #print(u"######################## %s"%word)
                #print(u"/".join(parts))
            actual = wordutils.greedy_split(word,self.TVU)
            self.assertEqual(parts,actual)
        return
    
    def test_greedy_split_TA2(self):
        word2,parts2 = u"ஒருதலைகாதல்", [u"ஒருதலை",u"காதல்"]
        actual2 = wordutils.greedy_split(word2,self.TVU)
        self.assertTrue( u"காதல்" )
        self.assertEqual(parts2,actual2)
        return

class TestTotalWordSplitter(unittest.TestCase):
    def setUp(self):
        self.TVU,self.VocabSize = DictionaryBuilder.create(TamilVU)
        self.TVU.add(u"ஆங்கிலம்நாடு")
        self.TVU.add(u"ஆங்கிலம்")
        
    def test_word_split_TA0(self):
        self.assertTrue(self.TVU.isWord(u"ஆங்கிலம்நாடு"))
        word = u"ஆங்கிலம்நாடுஆமை"
        parts = [[u"ஆங்கிலம்நாடு",u"ஆ",u"மை"],[u"ஆங்கிலம்நாடு",u"ஆமை"],
                 [u"ஆங்கிலம்",u"நாடு",u"ஆமை"],[u"ஆங்கிலம்",u"நாடு",u"ஆ",u"மை"]];
        actual = wordutils.word_split(word,self.TVU)
        self.assertEqual(sorted(parts),sorted(actual))
        for lst in actual:
            jn_wrd = u"".join(lst)
            self.assertEqual( jn_wrd,word )
        return
    
    def test_word_split_TA(self):
        word=u"ஒருதலைகாதல்"
        parts = [[u"ஒரு",u"தலை",u"காதல்"],[u"ஒருதலை",u"காதல்"]]
        actual = wordutils.word_split(word,self.TVU)
        self.assertEqual(parts,actual)

class TestPalindromes(unittest.TestCase):
    def setUp(self):
        self.wlist = ["1","121","1331","14641","15AA51","1729"]
        self.Dictionary,self.VocabSize = DictionaryBuilder.createUsingWordList(self.wlist)
    
    def test_palindromes(self):
        all = list(wordutils.all_plaindromes(self.Dictionary))
        self.assertEqual(all,self.wlist[:-1])

if __name__ == "__main__":
    unittest.main()
