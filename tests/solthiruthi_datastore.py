# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.data_parser import *
from solthiruthi.datastore import TamilTrie
from solthiruthi.Ezhimai import *
import sys

class EzhimaiTest(unittest.TestCase):
    def test_(self):
        obj = PattiyalThiruthi('std')
        in_words = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        rval = map( obj.process_word, in_words )
        actual = [obj['is_error'] for obj in rval]
        expected = [True,True,True,True,False,True,True,False,True,True,False,True]
        self.assertEqual( actual, expected )
    
# Test the Trie data structure
class EnglistTrieTest(unittest.TestCase):
    def test_stuff_3letter(self):
        obj = TamilTrie.buildEnglishTrie(3)
        actual_words = ['a','ab','abc','bbc']
        [obj.add(w) for w in actual_words]
        self.assertEqual( sorted(obj.getAllWords()),sorted(actual_words))
        return
    
    def test_letters_isword(self):
        obj = TamilTrie.buildEnglishTrie()
        [obj.add(w) for w in ['apple','amma','appa','love','strangeness']]
        all_words = ['apple','amma','appa','love','strangeness','purple','yellow','tail','tuna','maki','ammama']
        actual = [obj.isWord(w) for w in all_words]
        expected = [i < 5 for i in range(0,11)]
        self.assertEqual(actual,expected)
        return

class TamilTrieTest(unittest.TestCase):
    def test_letter(self):
        obj = TamilTrie()
        actual_words = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        [obj.add(w) for w in actual_words]
        self.assertEqual( sorted(obj.getAllWords()),sorted(actual_words))
        return
    
    def test_letters_isword(self):
        obj = TamilTrie()
        xkcd = [u'ஆப்பிள்', u'அம்மா', u'அப்பா', u'காதல்', u'தெரியாதவர்களை']
        [obj.add(w) for w in xkcd]
        all_words = [u'ஆப்பிள்', u'அம்மா', u'அப்பா', u'காதல்', u'தெரியாதவர்களை', u'ஊதா', u'மஞ்சள்', u'வால்', u'சூரை', u'மகி', u'பாட்டி']
        actual = [obj.isWord(w) for w in all_words]
        expected = [i < 5 for i in range(0,11)]
        self.assertEqual(actual,expected)
        return
    
if __name__ == "__main__":
    unittest.main()
