# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.data_parser import *
from solthiruthi.datastore import RTrie, TamilTrie, DTrie, Queue
from solthiruthi.Ezhimai import *
from solthiruthi.resources import DICTIONARY_DATA_FILES
import sys
import copy
from pprint import pprint

class RevTrieTest(unittest.TestCase):
    def test_rev_trie(self):
        rt = RTrie()
        ing_words = [u'riding',u'booking',u'dashing']
        list(map(rt.add,ing_words))
        words_endwith_ing = list(rt.getAllWordsPrefix(u'ing'))
        similar = list(rt.getWordsEndingWith(u'ing'))
        #pprint(similar)
        self.assertEqual(words_endwith_ing,similar)
        self.assertEqual(sorted(words_endwith_ing),sorted(ing_words))
        #for x,y in zip(ing_words,words_endwith_ing):
        #    print("%s|%s"%(x,y))
        return
        
    def test_missing(self):
        rt = RTrie()
        ing_words = [u'riding',u'booking',u'dashing','penny','farthing']
        list(map(rt.add,ing_words))
        similar = list(rt.getWordsEndingWith(u'---'))
        #pprint(similar)
        self.assertEqual(len(similar),5)

class TamilRevTrieTest(unittest.TestCase):
    def setUp(self):
        rt = RTrie(is_tamil=True)
        rhymie = [u"மாங்குயில்", u"பூங்குயில்", u"அல்லவா", u"செல்வாயா", u"சொல்வாயா"]
        for wrd in rhymie:
            rt.add(wrd)
        self.rt = rt
        self.len = len(rhymie)
        
        return
        
    def test_size(self):
        self.assertEqual(len(self.rt.getAllWords()),self.len)
        
    def test_tamil_rhymes(self):
        rt = self.rt
        # solvaaya/selvayaa
        vayaa = set(rt.getWordsEndingWith(u"வாயா"))
        self.assertEqual(len(vayaa),2)
        self.assertEqual(sorted(vayaa),sorted([u"செல்வாயா", u"சொல்வாயா"]))
        
    def test_tamil_rhymes_two(self):
        rt = self.rt
        # cuckoo koovum kuyil
        kuyil_expected = [u"பூங்குயில்",u"மாங்குயில்"]
        kuyil = list(rt.getAllWordsPrefix(u"குயில்"))
        self.assertEqual(len(kuyil),2)
        for word in kuyil:
            #print(u"word -> 1 %s"%word)
            self.assertTrue( word in kuyil_expected)
        return
    
class TamilDTriesForward(unittest.TestCase):
    def setUp(self):
        rhymie = [(u"மாங்குயில்",u"ல்யிகுங்மா"),(u"பூங்குயில்",u"ல்யிகுங்பூ"),(u"அல்லவா",u"வாலல்அ"),\
                  (u"செல்வாயா",u"யாவால்செ"),(u"சொல்வாயா",u"யாவால்சொ")]
        self.obj = DTrie()
        self.count = len(rhymie)
        for k,v in rhymie:
            self.obj.add(v)
        return
        
    def test_all_words(self):
        self.assertTrue(len(self.obj.getAllWords()),self.count)
        
    def word_n_prefix_test(self,pfx,wordlist,no):
        itr = 0
        for word in self.obj.getAllWordsPrefix(pfx):
            itr = itr + 1
            self.assertTrue(word in wordlist)
        self.assertEqual(itr,no)
        return
    
    def test_fwd_dictionaries(self):
        kuyils = [u"ல்யிகுங்பூ",u"ல்யிகுங்மா"]
        pfx = u"ல்யிகு"
        self.word_n_prefix_test(pfx,kuyils,2)
        
    def test_fwd_dictionaries_two(self):
        verbie = [u"யாவால்செ",u"யாவால்சொ"]
        pfx = u"யாவா"
        self.word_n_prefix_test(pfx,verbie,2)
        
if __name__ == "__main__":
    unittest.main()
