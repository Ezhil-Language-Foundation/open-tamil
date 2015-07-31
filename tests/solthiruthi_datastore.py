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

class EzhimaiTest(unittest.TestCase):
    def test_pattiyal(self):
        obj = PattiyalThiruthi('std')
        in_words = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        rval = map( obj.process_word, in_words )
        actual = [obj['is_error'] for obj in rval]
        expected = [True,True,True,True,False,True,True,False,True,True,False,True]
        self.assertEqual( actual, expected )
    
class DTrieTest(unittest.TestCase):
    """ takes 6s to load 63000+ words in-memory + readout sorted via 
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
    
    def test_count(self):
        obj = DTrie()
        foundE = False
        try:
            self.assertEqual(obj.getWordCount('foo'),0)
        except Exception as e:
            foundE = str(e).find("does not exist in Trie") >= 0
        self.assertTrue( foundE )
        obj = DTrie()
        words = ['foo','bar','bar','bar','baz']
        [obj.add(w) for w in words]
        self.assertEqual(obj.getWordCount('bar'),3)
        self.assertEqual(obj.getWordCount('foo'),1)
        self.assertEqual(obj.getWordCount('baz'),1)
        
    def test_words_n_count(self):
        obj = DTrie()
        words = ['foo','bar','bar','bar','baz']
        [obj.add(w) for w in words]
        actual = {'foo':1,'bar':3,'baz':1}
        self.assertEqual(obj.getAllWordsAndCount(),actual)
        
    def test_trie_neg(self):
        obj = DTrie()
        self.assertEqual( obj.getAllWords(), [] )
        self.assertEqual( obj.getAllWordsPrefix('none'), [] )
        self.assertFalse( obj.isWord('fubar',True)[0] )
        self.assertTrue( obj.isWord('fubar',True)[1] )
    
    def test_stuff_3letter(self):
        obj = DTrie()
        self.assertFalse( obj.isWord('apple') )
        try:
            obj.add('')
        except AssertionError as exp: 
            pass
        actual_words = ['a','ab','abc','bbc']
        [obj.add(w) for w in actual_words]
        for w in actual_words:
            self.assertTrue( obj.isWord(w) )
        self.assertEqual( sorted(obj.getAllWords()),sorted(actual_words))
        self.assertEqual( obj.getAllWordsPrefix('ab'), ['ab','abc'] )
        return

    def test_trie_counts_and_prefix(self):
        obj = DTrie()
        actual_words = ['a','ab','abc','abc','bbc']
        [obj.add(w) for w in actual_words]
        for w in actual_words:
            self.assertTrue(obj.isWord(w))
        self.assertEqual(len(obj.getAllWords()),4)
        self.assertEqual( obj.getAllWordsPrefix('ab'),['ab','abc'] )
        self.assertEqual(obj.getWordCount('abc'),2)
        obj = DTrie()
        list(map(obj.add,['foo','bar','bar','baz']))
        self.assertEqual((obj.getWordCount('bar'),\
                         obj.getWordCount('baz'),\
                         obj.getWordCount('foo')),(2,1,1))
        
    def test_load_dictionary(self):
        obj = DTrie()
        obj.loadWordFile(DICTIONARY_DATA_FILES['tamilvu'])
        self.assertEqual(len(obj.getAllWords()),63896)
        count = 0
        for word in obj.getAllWordsIterable():
            count = count + 1
        self.assertEqual(count,63896)
        words = obj.getAllWordsPrefix(u'பெரு')
        print(len(words))
        #for w in words:
        #    print(w)
        self.assertEqual( len(words), 215 )

# Test the Trie data structure
class EnglishTrieTest(unittest.TestCase):
    def test_stuff_3letter(self):
        obj = TamilTrie.buildEnglishTrie(3)
        actual_words = ['a','ab','abc','bbc']
        [obj.add(w) for w in actual_words]
        self.assertEqual( sorted(obj.getAllWords()),sorted(actual_words))
	#self.assertEqual( obj.getAllWordsPrefix('a'), ['ab','abc'] )
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

class TriePrefixTest(unittest.TestCase):
    def test_prefix(self):
        obj = DTrie()
        actual_words = ['abx','abc','abcd','bbc']
        [obj.add(w) for w in actual_words]
        for w in actual_words:
            self.assertTrue(obj.isWord(w))
        self.assertEqual(len(obj.getAllWords()),4)
        
        for w in actual_words:
            self.assertFalse( obj.isWord( w+'NA' ) )
            self.assertFalse( obj.isWord( w+'DA' ) )
        
        for pfx in ["ab","bb","bd"]:
            self.assertFalse( obj.isWord( pfx ) )

        for pfx in ['a','ab','b','bb']:
            self.assertTrue( obj.hasWordPrefix(pfx) )
        
        val = []
        for pfx in ['c','ac','ad','cb','z']:
            #print("===> last/test ==> %s"%pfx)
            val.append( obj.hasWordPrefix(pfx) )
        self.assertFalse( any(val) )
        
        return

class QueueTest(unittest.TestCase):
    def test_load(self):
        q = Queue()
        for i in range(0,10):
            q.insert( i**2 )
        # verify 10 elements are found in queue
        self.assertEqual( len(q), 10)
        self.assertEqual( q[0], 0)
        self.assertEqual( q[9], 81)
        self.assertEqual( q[-1], 81)
        foundInExcept = False
        try:
            q[5]
        except Exception as exp:
            foundInExcept = str(exp).find(u"index") >= 0
        self.assertEqual( foundInExcept, True )
        print(len(q))
        for i in range(len(q)):
            self.assertEqual( q.pop(), i**2 )
        self.assertTrue( q.isempty() )
        
    def test_list_methods(self):
        q = Queue()
        found_exception = False
        try:
            q.append(5)
        except Exception as e:
            found_exception = str(e).find(u"Queue does not support") >= 0
        self.assertEqual( found_exception, True)
    
    def test_q(self):
        q = Queue()
        data = u"நெற்ஸ்கேப் பதிப்புகளில் இந்த செயலி தானிறங்கி எழுத்துரு இல்லாமையினால் முழுமையாக வேலைசெய்யாது என்பதை கருத்திலெடுக்கவும்."
        words = data.split()
        for word in words:
            q.insert(word)
        self.assertEqual(len(q),11)
        datum_peek = q.peek()
        self.assertEqual(words[0],datum_peek)
        self.assertEqual(q.pop(),words[0])
        [q.pop() for i in range(5)]
        
        self.assertEqual(q[-1],words[-1])
        
if __name__ == "__main__":
    unittest.main()
