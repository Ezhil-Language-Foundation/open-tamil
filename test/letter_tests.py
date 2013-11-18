# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

import tamil.utf8 as utf8

class Letters(unittest.TestCase):
    def test_uyirmei(self):     
        print(utf8.uyirmei(2))
        assert( utf8.uyirmei(2)  == u"கி" )

    def test_letter_extract_from_code_pts(self):
        letters = utf8.get_letters(u"கூவிளம் என்பது என்ன சீர்")
        #print "len ==== > " , len(letters)
        assert( len(letters) == 15 )
        for pos,letter in  enumerate(letters):
            print(u"%d %s"%(pos,letter))
        assert( letter == (u"ர்") )
    
    def test_tamil_letter_sizes( self ):
        assert( len(utf8.uyir_letters) == 12 )
        assert( len(utf8.mei_letters) == 18 )
        assert( len(utf8.uyir_letters) == (len(utf8.accent_symbols)-1) )
        assert( len(utf8.uyirmei_letters) == 18*12 )
        assert( len(utf8.sanskrit_letters) == 4 )
        assert( len(utf8.tamil_letters) == 321 )

    def test_get_letters2( self ):
        letters = utf8.get_letters(u"hello world  தெரிந்த அல்லது தெரியாத")
        assert( len(letters) == 26 )
        assert( letters[13] == u"தெ" )
        
    def test_istamil( self ):
        zz = u"முத்தையா அண்ணாமலை எந்த ஒரு தெரிந்த அல்லது தெரியாத எழுத்துருவாகவிருந்தாலும் அதனை மேல்தட்டில் உள்ளிட்டு கீழே உள்ள முடியும்"
        for z in zz.split(u" "):
            print("********** t/f ********")
            for x,y in zip(map(utf8.istamil,utf8.get_letters(z)),utf8.get_letters(z)):
                print("%s => %s"%(y,x))        
                assert( all( map( utf8.istamil, utf8.get_letters( z ) ) ) )
        
        z = u"முத்தையா அண்ணாமலை"
        assert( any( map( utf8.istamil, utf8.get_letters( z ) ) ) )
        
        correct = [True, True, True, True, False, True, True, True, True, True, False, False, False, False, False]
        assert( map(utf8.istamil,utf8.get_letters(u"முத்தையா அண்ணாமலை 2013")) == correct )


class TSCII(unittest.TestCase):
    def test_vowels(self):
        TSCII = tamil.tscii.TSCII
        assert( TSCII[0xAB] == u"அ" )
        assert( TSCII[0xAC] == u"ஆ" )
        
    def test_sanskrit(self):
        TSCII = tamil.tscii.TSCII
        assert( TSCII[0x82] == u"ஶ்ரீ")
        assert( TSCII[0x83] == u"ஜ")
        assert( TSCII[0x84] == u"ஷ")
        
    def test_basic_lookup2UTF8( self ):
        TSCII = tamil.tscii.TSCII
        assert( TSCII[0xAB]+TSCII[0xF4]+TSCII[0xC0]+TSCII[0xA1] == u"அப்பா" )

    def test_TSCII_to_UTF8_part1( self ):        
        str=open("data/Sample.TSCII").read()
        output = tamil.tscii.convert_to_unicode( str )
        print(output)
        needle = u"""உடுப்பி ஒட்டலுக்குப் போய் மசாலா தோசை சாப்பிட்டு வரலாமா"""
        assert( output.find(needle) >= 0 )

    def test_TSCII_to_UTF8_part2( self ):
        str=open("data/dumb.tscii").read()
        output = tamil.tscii.convert_to_unicode( str )
        assert( output.find(u"அப்பா") >= 0 )
        
if __name__ == '__main__':
    test_support.run_unittest(Letters,TSCII)
