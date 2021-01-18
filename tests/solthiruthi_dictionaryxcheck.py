# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.datastore import RTrie, TamilTrie, DTrie, Queue
from solthiruthi.dictionary import (
    SimpleDictionary,
    EnglishLinux,
    VatamozhiMonierWilliams,
)
from solthiruthi.resources import DICTIONARY_DATA_FILES
import sys
import copy
import codecs
from pprint import pprint
import string


class VatamozhiDictionaryTest(unittest.TestCase):
    def test_load(self):
        self.simple_skt = SimpleDictionary(DICTIONARY_DATA_FILES["vatamozhi"])
        self.simple_skt.loadWordFile()
        self.trie_skt = VatamozhiMonierWilliams()
        self.trie_skt.loadWordFile()


class XCheckEnglishDictionaryTest(unittest.TestCase):
    def setUp(self):
        self.simple_english = SimpleDictionary(DICTIONARY_DATA_FILES["english"])
        self.simple_english.loadWordFile()
        self.trie_english = EnglishLinux()
        self.trie_english.loadWordFile()

    def __unused__(self):
        self.trie_english = DTrie.buildEnglishTrie()
        with codecs.open(DICTIONARY_DATA_FILES["english"], "r", "utf-8") as fp:
            for l in fp.readlines():
                l = l.strip()
                self.trie_english.add(
                    filter(lambda lx: lx in string.letters, l.lower())
                )

    def test_english_count(self):
        n_trie = len(self.trie_english.getAllWords())
        n_english = len(self.simple_english.getAllWords())
        print("N trie = %d, N_simple = %d" % (n_trie, n_english))
        self.assertEqual(n_trie, 45373)
        self.assertEqual(n_english, 45402)

    # @unittest.skip("skip")
    def test_english_words(self):
        w_trie = set(self.trie_english.getAllWords())
        w_english = set(self.simple_english.getAllWords())
        residue = w_trie.symmetric_difference(w_english)
        # for w in residue:
        #    print(u"F -> %s"%w)
        print("len trie words = %d" % len(w_english))
        self.assertEqual(len(residue), 0)


if __name__ == "__main__":
    unittest.main()
