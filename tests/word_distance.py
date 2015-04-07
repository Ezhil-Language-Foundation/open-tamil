# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from __future__ import print_function
from opentamiltests import *

class WordsSimilarityLevenshtein(unittest.TestCase):
    def test_Levenshtein_distance( self ):
        values = [ [u'setting',u'kitten', 4], \
                   [u'object',u'object', 0], \
                   [u'veil',u'vail', 1], \
                   [u'தேங்காய்',u'மாங்காய்', 1] ]
        for items in values:
            k = items[0:2]
            v = items[2]
            self.assertEqual( ngram.Distance.edit_distance(k[0],k[1]),v)
        return
    
    def test_Levenshtein_dist_matrix(self):
        val = [u"food",u"allergy",u"வார்த்தை",u"இது",u"ஒரு",u"ஒருங்குறி", u"வரிசை"]
        L = len(val)
        
        dists = [ [0 for i in range(0,L)] for i in range(0,L)]
        trueDists = [[0, 7, 4, 4, 4, 5, 4],
            [7, 0, 7, 7, 7, 7, 7],
            [4, 7, 0, 4, 4, 5, 4],
            [4, 7, 4, 0, 2, 5, 3],
            [4, 7, 4, 2, 0, 3, 3],
            [5, 7, 5, 5, 3, 0, 5],
            [4, 7, 4, 3, 3, 5, 0]]
        
        for i in range(0,L):
            for j in range(0,L):
                if i == j:
                    continue
                wA,wB = val[i],val[j]
                dists[i][j] = ngram.Distance.edit_distance(wA,wB)
        
        self.assertEqual(dists,trueDists)
        return
    
class WordsSimilarityDiceJaccard(unittest.TestCase):
    def test_Dice_distance( self ):
        for word in [u"food",u"allergy",u"வார்த்தை",u"இது",u"ஒரு",u"ஒருங்குறி", u"வரிசை"]:
            self.assertEqual( ngram.Distance.Dice_coeff(word,word),1.0)
        return
    def test_Dice_in_the_middle( self ):
        wordA,wordB = u"நிரலாக்க",u"உதாரணம்" #only common letter = ர.
        # n_A = 5, n_B = 5, n_AB = 1; dist = 2*1/(5+5)
        dist = ngram.Distance.Dice_coeff(wordA,wordB)
        self.assertEqual(dist,0.2)
    
    def test_Dice_random( self ):
        for wordA in [u"food",u"allergy",u"வார்த்தை",u"இது",u"ஒரு",u"ஒருங்குறி", u"வரிசை"]:
            for wordB in u"இது ஒரு எழில் தமிழ் நிரலாக்க மொழி உதாரணம்".split(u" "):
                dist = ngram.Distance.Dice_coeff(wordA,wordB)
                self.assertTrue( dist <= 1.0 and dist >= 0.0)
        return

class WordsSimilarityJaccard(unittest.TestCase):
    def test_Dice_distance( self ):
        for word in [u"food",u"allergy",u"வார்த்தை",u"இது",u"ஒரு",u"ஒருங்குறி", u"வரிசை"]:
            self.assertEqual( ngram.Distance.Jaccard_coeff(word,word),0.0)
        return
    def test_Dice_in_the_middle( self ):
        wordA,wordB = u"நிரலாக்க",u"உதாரணம்" #only common letter = ர.
        # n_A = 5, n_B = 5, n_AB = 1; dist = 2*1/(5+5)
        dist = ngram.Distance.Jaccard_coeff(wordA,wordB)
        self.assertEqual(dist,0.8)
    
    def test_Dice_random( self ):
        for wordA in [u"food",u"allergy",u"வார்த்தை",u"இது",u"ஒரு",u"ஒருங்குறி", u"வரிசை"]:
            for wordB in u"இது ஒரு எழில் தமிழ் நிரலாக்க மொழி உதாரணம்".split(u" "):
                dist = ngram.Distance.Jaccard_coeff(wordA,wordB)
                self.assertTrue( dist <= 1.0 and dist >= 0.0)
        return

if __name__ == '__main__':
    unittest.main()
