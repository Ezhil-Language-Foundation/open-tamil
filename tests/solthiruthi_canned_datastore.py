# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

import os
from opentamiltests import *
from solthiruthi.dictionary import *
from solthiruthi.datastore import Trie

# Test the canned English dictionary with data structure
class TestEnglishDictionary(unittest.TestCase):
    def setUp(self):
        self.ENG,self.ENG_size = DictionaryBuilder.create(EnglishLinux)        
        print(u"Loading EnglishLinux dictionary @ size = %d"%self.ENG_size)
        
    def tearDown(self):
        del self.ENG
        
    def test_factory_EnglishLinux(self):
        words = [u'Car',u'Rabbit',u'COdE',u'CoMpUtEr',u'UnIx',u'InDiA']
        for w in words:
            print(u"Verifying ... %s"%w)
            self.assertTrue(self.ENG.isWord(w.lower()))
            self.assertTrue(self.ENG.isWord(w.upper()))
            self.assertTrue(self.ENG.isWord(w))
            self.assertFalse(self.ENG.isWord(w+'31'))    
        return

class TestDictionarySaveLoad(unittest.TestCase):
    def setUp(self):
        self.fname = 'data.dot'
        self.wl = [u'abelian',u'commutative',u'monoid',u'rings',u'groups']
        self.TMP,self.TMPVocabSize = DictionaryBuilder.createUsingWordList(self.wl)
        Trie.serializeToFile(self.TMP,self.fname)
                
    def tearDown(self):
        os.unlink(self.fname)
        
    def test_wordlist_dictionary(self):
        self.assertEqual(self.TMPVocabSize,len(self.wl))
        self.assertTrue(self.TMP.isWord(u'groups'))
        self.assertTrue(self.TMP.isWord(u'rings'))
        self.assertFalse(self.TMP.isWord(u'trefoil'))
 
    def test_load_n_save(self):
        reloadTMP = Trie.deserializeFromFile(self.fname)
        self.assertEqual(reloadTMP.getSize(),len(self.wl))
        self.assertTrue(reloadTMP.isWord(u'groups'))
        self.assertTrue(reloadTMP.isWord(u'rings'))
        self.assertEqual(list(reloadTMP.getAllWords()),list(self.TMP.getAllWords()))
        for wl in reloadTMP.getAllWords():
            print(wl)
        return
    
# Test the canned dictionary with data structure
class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.TVU,self.TVU_size = DictionaryBuilder.create(TamilVU)
        
    def tearDown(self):
        del self.TVU

    def test_wordlist_dictionary(self):
        TMP,TMPVocabSize = DictionaryBuilder.createUsingWordList(['word','list','wo','rdli','st'])
        self.assertEqual(TMPVocabSize,5)
        self.assertTrue(TMP.isWord(u'word'))
        self.assertFalse(TMP.isWord(u'wor'))
    
    def test_factory_TVU(self):
        TVU_agarathi,size = self.TVU,self.TVU_size
        self.assertTrue(isinstance(TVU_agarathi,TamilVU))
        self.assertEqual(size,63896)
        return

    def test_isword(self):
        words = u"தமிழ் நாட்டில் சங்ககாலத்திலேயே ஒட்டியாணம் போன்ற இடையணிகள் இருந்தமைக்கான சான்றுகளும் பெண்".split(" ")
        self.assertEqual(len(list(filter(self.TVU.isWord,words))),3)
        self.assertTrue(self.TVU.isWord(u"தமிழ்"))
        
if __name__ == "__main__":
    unittest.main()
