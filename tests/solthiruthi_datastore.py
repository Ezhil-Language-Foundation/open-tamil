# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.data_parser import *
from solthiruthi.datastore import TamilTrie, DTrie
from solthiruthi.Ezhimai import *
from solthiruthi.resources import DICTIONARY_DATA_FILES
import sys
import copy

class EzhimaiTest(unittest.TestCase):
    def test_pattiyal(self):
        obj = PattiyalThiruthi('std')
        in_words = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        rval = map( obj.process_word, in_words )
        actual = [obj['is_error'] for obj in rval]
        expected = [True,True,True,True,False,True,True,False,True,True,False,True]
        self.assertEqual( actual, expected )
    
class DTrieTest(unittest.TestCase):
    """ takes 6s to load 63000+ words inmemory + readout sorted via 
        DTrie as implemented (includes file I/O time) """
    def test_pattiyal(self):
        obj = DTrie()
        in_words = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        list(map( obj.add, in_words )) # Python 2-3
        all_words_and_reverse = copy.copy(in_words)
        all_words_and_reverse.extend( [utf8.reverse_word( word)  for word in in_words] )
        actual = [obj.isWord(word) for word in all_words_and_reverse]
        expected = [i<len(in_words) for i in range(0,2*len(in_words))]
        self.assertEqual( actual, expected )
    
    def test_load_dictionary(self):
        obj = DTrie()
        obj.loadWordFile(DICTIONARY_DATA_FILES['tamilvu'])
        self.assertEqual(len(obj.getAllWords()),63896)
        count = 0
        for word in obj.getAllWordsIterable():
            count = count + 1
        self.assertEqual(count,63896)

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
