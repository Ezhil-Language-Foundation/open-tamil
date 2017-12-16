#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# (C) 2013-2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
import codecs
import re
from opentamiltests import *
from tamil.utils.santhirules import joinWords
from tamil.regexp import make_pattern

class SantheeRules(unittest.TestCase):
    def test_filebased_conjugation_tests( self ):
        # write to file
        with codecs.open('out.txt','r','utf-8') as FP:
            data = FP.readlines()
            for no,combo in enumerate(data):
                print("testing #",no)
                word = combo.split('=')
                parts = word[0].split('+')
                joind = word[1].strip()
                a = parts[0].strip()
                b = parts[1].strip()
                jword = joinWords(a,b)
                
                if ( LINUX ):
                    print(a + u' + ' + b + u' = ' + jword+u'\n')
                    print(jword,u'|',joind)
                self.assertEqual( joind, jword )
        return

    def test_grammar_conjugation( self ):
        a = u'என்ன'
        b = u'என்ன'
        w = joinWords(a, b).encode('utf8')
        
        print( w )
        self.assertTrue( w.decode('utf-8') == u'என்னென்ன')
        

class TamilRegex(unittest.TestCase):
    def test_basic_A2Z( self ):
        pattern = u"[அ-ஔ]+"
        expected = u"[அ,ஆ,இ,ஈ,உ,ஊ,எ,ஏ,ஐ,ஒ,ஓ,ஔ]+"
        [cpattern,opattern] = make_pattern( pattern )
        self.assertEqual( opattern, expected )
    
    def test_basic_no2_A2Z( self ):
        pattern = u"^[அ-உ]+"
        expected = u"^[அ,ஆ,இ,ஈ,உ]+"
        [cpattern,opattern] = make_pattern( pattern )
        self.assertEqual( opattern, expected )
    
    def test_basic_no3_A2Z( self ):
        pattern = u"^[அ-ஔ][0-9]+"
        expected = u"^[அ,ஆ,இ,ஈ,உ,ஊ,எ,ஏ,ஐ,ஒ,ஓ,ஔ][0-9]+"
        [cpattern,opattern] = make_pattern( pattern )
        self.assertEqual( opattern, expected )
    
    def test_basic_no4_A2Z( self ):
        pattern = u"^[அ-ஔ][0-9]+"
        expected = u"^[அ,ஆ,இ,ஈ,உ,ஊ,எ,ஏ,ஐ,ஒ,ஓ,ஔ][0-9]+"
        [cpattern,opattern] = make_pattern( pattern )
        self.assertEqual( opattern, expected )

    def test_basic_no5_A2Z( self ):
        pattern = u"^[க்-ம்]+"
        expected = u"^[க்,ச்,ட்,த்,ப்,ற்,ஞ்,ங்,ண்,ந்,ம்]+"
        [cpattern,opattern] = make_pattern( pattern )
        self.assertEqual( opattern, expected )

    def test_uyirmei_no6_A2Z( self ):
        pattern = u"[ப-பௌ]+"
        expected = u"[ப,பா,பி,பீ,பு,பூ,பெ,பே,பை,பொ,போ,பௌ]+"
        [cpattern,opattern] = make_pattern( pattern )
        self.assertEqual( opattern, expected )
    
class GrepTests(unittest.TestCase):
    def setUp(self):
        self.data = codecs.open('data/richmond.txt','r','utf-8').readlines()
        print("\ndata size = %d L"%len(self.data))
    def cleanUp(self):
        if self.data:
            try:
                self.data.close()
            except:
                pass
        
    def search_test(self,pattern,expected):
        return self.match_test(pattern,expected,fcn=re.search)
    
    def match_test(self,pattern,expected,data=None,fcn=re.match):
        [repatt,ymp] = make_pattern( pattern )
        word_matches = []
        if not data:
            data = self.data
        for idx,line in enumerate(data):
            q = fcn(repatt,line.strip())
            if q:
                print("matched @ %d"%idx)
                word_matches.append( idx )
        self.assertEqual( word_matches, expected )
        return
   
    def test_exprs(self):
        pattern = u"^ரிச்.*[க்-ழ்]$"
        expected = [0,1,2,3,7,8,10]
        self.match_test( pattern, expected )
    
    def test_match_letterend_exprs(self):
        pattern = u"டு$"
        expected = [5,6]
        self.search_test(pattern,expected)
        return
                
    def test_match_exprs(self):
        pattern = u".*[^க்-ழ்]$"
        expected = [4,5,6,9]
        self.match_test(pattern,expected)
        return
    
    def test_demo_regex(self):
        pattern = u"^[க-ள].+[க்-ள்]$"
        data = [u"இந்த",u"தமிழ்",u"ரெகேஸ்புல்",u"\"^[க-ள].+[க்-ள்]$\"",u"இத்தொடரில்", u"எதை", u"பொருந்தும்"]
        expected = [1,2,6] # i.e.தமிழ்
        self.match_test(pattern,expected,data)
        return
    
if __name__ == '__main__':    
    unittest.main()
