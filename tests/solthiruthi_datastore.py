# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.data_parser import *
from solthiruthi.datastore import TamilTrie
import sys

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
    
if __name__ == "__main__":
    unittest.main()
