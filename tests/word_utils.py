# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from __future__ import print_function
from opentamiltests import *
from tamil import wordutils, tweetparser

import math

class TestTweetParse(unittest.TestCase):
    def test_tweety( self ):
        tweet = u"ஈர்ப்பு அலைகள் உருவாக்கும் அலைகள் #LIGO #tamil @nsf | SBS Your Language http://www.sbs.com.au/yourlanguage/tamil/ta/content/iirppu-alaikll-uruvaakkum-alaikll?language=ta"
        tobj = tweetparser.TamilTweetParser(timeline_owner = "@ezhillang",tweet=tweet)
        self.assertEqual(tobj.Hashtags[0],"#LIGO")
        self.assertEqual(tobj.Hashtags[1],"#tamil")
        self.assertTrue(tobj.URLs[0].find("sbs.com.au") >= 0 )
        self.assertTrue(u"அலைகள்" in tobj.TAWords)
        
class TestWordUtils(unittest.TestCase):
    def test_perms( self ):
        res = [u'123',u'132',u'213',u'231',u'312',u'321']
        self.assertEqual( list(wordutils.permutations(u'1 2 3'.split(u' '))),res)
    
    def test_perms_with_prefix_filters( self ):
        s = lambda x:x.startswith('1')
        gen = list(tamil.wordutils.permutations('123'))
        filt = list(tamil.wordutils.permutations('123',s))
        
        self.assertEqual(len(gen),math.factorial(3))
        self.assertEqual(filt,['123','132'])
        
        # filter perms that have second letter as '2' or '3'
        def bigrams(x):
            if len(x) >= 2:
                return x[1] == '2' or x[1] == '3'
            return True
        filt2 = list(tamil.wordutils.permutations('123',bigrams))
        
        self.assertEqual(filt2,['123','132','231','321'])
    
    def test_perms_length(self):
        count = 0
        for perm in wordutils.permutations('1 2 3 4 5 6'.split(' ')):
            count += 1
        self.assertEqual(count,math.factorial(6))
        
    def test_tamil_perms( self ):
        res = [u'தமிழ்',u'தழ்மி',u'மிதழ்',u'மிழ்த',u'ழ்தமி',u'ழ்மித']
        self.assertEqual( list(wordutils.permutations([u'த',u'மி',u'ழ்'])),res)
     
    def test_tamil_perms2( self ):
        res = [u'தமிழ்',u'தழ்மி',u'மிதழ்',u'மிழ்த',u'ழ்தமி',u'ழ்மித']
        self.assertEqual( list(wordutils.tamil_permutations(res[0])),res)
        
    def test_greedy_split( self ):
        twoDict = wordutils.DictionaryFixedWordList([u"செயல்",u"பட"])
        word = u"செயல்பட"
        parts = tamil.wordutils.greedy_split(word,twoDict)
        self.assertEqual( parts, [u"செயல்",u"பட"] )
        
    @skip_python2_6
    def test_anagram_xception(self):
        mtObj = wordutils.DictionaryWithPredicate( False )
        with self.assertRaises(Exception):
            list( wordutils.anagrams( u'உபயொகிக்க!',mtObj) )
    
    def test_anagram_all_or_nothing(self):
        # all words are in dictionary..
        dictPred = wordutils.DictionaryWithPredicate(lambda x: True)
        self.assertTrue( dictPred.isWord('not a word but OK to slack off!') )
        
        res = [u'தமிழ்',u'தழ்மி',u'மிதழ்',u'மிழ்த',u'ழ்தமி',u'ழ்மித']
        self.assertEqual( list(wordutils.anagrams(u'தமிழ்',dictPred)), res )
        
        # none of words match
        negDictPred = wordutils.DictionaryWithPredicate(lambda x: False)
        self.assertEqual( list(wordutils.anagrams(res[0],negDictPred)),[] )
        
    def test_perms_as_string_is_OK(self):
        actual = list( wordutils.permutations( u'அதுசரம்' ) )
        self.assertEqual(len(actual),math.factorial(5))
    
    def test_combinations(self):
        word = u"சவால்";
        self.assertEqual( len(list(filter(len,list(wordutils.combinations(word))))), 8-1 )

    def test_palindrome(self):
        words = [u"a",u"abba","xkcd","vinavi","1001",u"அதுஅ",u"சரம்ரச"]
        expected = [u"a",u"abba","1001",u"அதுஅ",u"சரம்ரச"]
        actual = list(filter(wordutils.palindrome,words))
        self.assertEqual(actual,expected)
    
    def test_palindrome_false(self):
        words = [u"ab",u"abbax","xxkcd","xvinavi","103_301","10010",u"அxதுஅ",u"சரxம்xxரச"]
        expected = ['103_301']
        actual = list(filter(wordutils.palindrome,words))
        self.assertEqual(actual,expected)
    
    def test_ispalindrome(self):
        expected = [u"a",u"abba","1001",u"அதுஅ",u"சரம்ரச"]
        self.assertTrue( all(list(map(wordutils.is_palindrome,expected))) )
    
    def test_isanagram(self):
        w1 = u'சவால்'
        w2 = u'வாசல்'
        self.assertTrue( wordutils.is_anagram(w1,w2) )
        
        w3 = '123'
        w4 = '213'
        self.assertTrue( wordutils.is_anagram(w3,w4) )

        self.assertFalse( wordutils.is_anagram(w3,w1) )
        self.assertFalse( wordutils.is_anagram(w2,w4) )
        
if __name__ == '__main__':
    unittest.main()
