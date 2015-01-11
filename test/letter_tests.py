# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

import tamil.utf8 as utf8

class Words(unittest.TestCase):
    def test_all_tamil( self ):
        self.assertTrue( tamil.utf8.all_tamil(u"சம்மதம்") )
        self.assertFalse( tamil.utf8.all_tamil(u"சம்மதம்1") )
        self.assertTrue( tamil.utf8.all_tamil( [u"பொ", u"ம", u"த"]))
    
    
    def test_word_xsection( self ):
        pos1 = utf8.word_intersection( u"தேடுக",u"தடங்கல்")
        self.assertTrue( pos1[0] == (2,3) )
        
        pos2 = utf8.word_intersection( u"தேடுக",u"சொல்")
        self.assertFalse(  pos2 )

        pos3 = utf8.word_intersection(u"மென்பொருள்",u"யுனிகோட்")
        self.assertFalse( pos3 )
        

class Letters(unittest.TestCase):
    def test_word_length( self ):
        actual = 5
        letters = utf8.get_letters(u"மென்பொருள்")
        self.assertTrue( actual == len(letters) )
    
    def test_unicode_repr( self ):    
        print("********* unicode repr ******")
        actual = utf8.to_unicode_repr(u'எழில்') 
        if PYTHON3:
            wanted = u"'\u0b8e\u0bb4\u0bbf\u0bb2\u0bcd'"
        else:
            wanted = "u'\\u0b8e\\u0bb4\\u0bbf\\u0bb2\\u0bcd'"
        print(wanted,actual)
        print(len(wanted),len(actual))
        self.assertTrue( actual == wanted )
    
    def test_alltamil( self ):
        self.assertTrue( utf8.all_tamil(u"அஆஇஈஉ") )
        self.assertFalse( utf8.all_tamil(u"அஆஇNotTamilஈஉ") )

    def test_lexicographic( self ):        
        # check if sorting works with a new predicate
        expected =  [ u"அப்பா",u"அம்மா",u"காகம்",u"நீம்"]
        words = [ u"நீம்",u"காகம்",u"அம்மா",u"அப்பா",]
        
        if PYTHON3:            
            ## FIXME : __CMP__ and CMP are gone in Python3
            ## Ref: http://python3porting.com/problems.html#unorderable-types-cmp-and-cmp
            self.assertTrue( PYTHON3 )
            return
        
        words.sort( utf8.compare_words_lexicographic )
        self.assertEqual( words, expected )
        
        print( utf8.compare_words_lexicographic( u"அப்பா",u"அம்மா" ) )

        # dad comes before mom, atleast in dictionary...
        self.assertTrue( utf8.compare_words_lexicographic( u"அப்பா",u"அம்மா" ) == -1 )
        # same words compare equally as in dictionary...
        self.assertTrue( utf8.compare_words_lexicographic( u"அப்பா",u"அப்பா" ) == 0  )
        # symmetry is preserved upon negation equally as in dictionary...
        self.assertTrue( utf8.compare_words_lexicographic( u"அம்மா",u"அப்பா")  == 1 )

        # compare two other words,
        self.assertTrue( utf8.compare_words_lexicographic( u"நீம்",u"காகம்") == 1 )
        
    def test_lettertopy(self):
        round_trip = eval(utf8.letters_to_py( utf8.mei_letters ))
        assert( round_trip == utf8.mei_letters )

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

    def test_letter_extract_with_ascii(self):
        letters = utf8.get_letters(u"கூவிளம் is என்பது also என்ன a சீர்")
        print( "len ==== > " , len(letters) )
        assert(len(letters) == 25 )
        for pos,letter in  enumerate(letters):
            print(u"%d %s"%(pos,letter))
        assert( letters[-4] == u"a" )

    def test_words(self):
        string = u"உடனே random elevator jazz உடனே எழுதினால் செய்திப் பத்திரிகை போஆகிவிடும் அசோகமித்திரன் நேர்காணல்"
        words = string.split(u" ")

        letters = utf8.get_letters( string )
        outWords = utf8.get_words( letters )
        
        print( u"|".join(words) )
        print( u"|".join(outWords) )
        
        assert( outWords == words )

    def test_tamil_only_words(self):
        string = u"உடனே உடனே seventh heaven எழுதினால் செய்திப் பத்திரிகை போஆகிவிடும் அசோகமித்திரன் நேர்காணல்"
        words = string.replace(u"seventh heaven ",u"").split(u" ")

        letters = utf8.get_letters( string )
        outWords = utf8.get_tamil_words( letters )
        
        print( u"|".join(words) )
        print( u"|".join(outWords) )
        
        assert( outWords == words )

    def test_letter_extract_yield_with_ascii(self):
        letters = []
        for l in  utf8.get_letters_iterable(u"கூவிளம் is என்பது also என்ன a சீர்"):
            letters.append( l )
        print( "len ==== > " , len(letters) )
        assert(len(letters) == 25 )
        for pos,letter in  enumerate(letters):
            print( u"%d %s"%(pos,letter) )
        assert( letters[-4] == u"a" )
        
    def test_letter_extract_yield(self):
        letters = []
        for l in utf8.get_letters_iterable(u"கூவிளம் என்பது என்ன சீர்"):
            letters.append( l )
        print( "len ==== > " , len(letters) )
        assert( len(letters) == 15 )
        for pos,letter in  enumerate(letters):
            print(u"%d %s"%(pos,letter))
        assert( letter == (u"ர்") )

    def test_reverse_words( self ):
        """ unittest for reverse a Tamil string"""
        print( utf8.get_letters(u"இந்த") )
        print( u"".join(utf8.get_letters(u"இந்த")) )
        for word in u"இந்த (C) tamil முத்தையா அண்ணாமலை 2013 இந்த ஒரு எழில் தமிழ் நிரலாக்க மொழி உதாரணம்".split():
            rword = utf8.reverse_word(word)
            print( word,rword )
            self.assertTrue( utf8.get_letters(rword)[0] == utf8.get_letters(word)[-1] )
        return

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
        self.assertTrue( letters[13] == u"தெ" )
        
    def test_istamil( self ):
        zz = u"முத்தையா அண்ணாமலை எந்த ஒரு தெரிந்த அல்லது தெரியாத எழுத்துருவாகவிருந்தாலும் அதனை மேல்தட்டில் உள்ளிட்டு கீழே உள்ள முடியும்"
        for z in zz.split(u" "):
            print("********** t/f ********")
            for x,y in zip(map(utf8.istamil,utf8.get_letters(z)),utf8.get_letters(z)):
                print(u"%s => %s"%(y,x))        
                assert( all( map( utf8.istamil, utf8.get_letters( z ) ) ) )
        
        z = u"முத்தையா அண்ணாமலை"
        assert( any( map( utf8.istamil, utf8.get_letters( z ) ) ) )
        
        correct = [True, True, True, True, False, True, True, True, True, True, False, False, False, False, False]
        print ( list(map(utf8.istamil,utf8.get_letters(u"முத்தையா அண்ணாமலை 2013"))) )
        print ( correct )
        assert( list(map(utf8.istamil,utf8.get_letters(u"முத்தையா அண்ணாமலை 2013"))) == correct )


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
        if PYTHON3:
            print("#### TEST NOT RUN FOR PYTHON3 #######")
            return
        str=open("data/Sample.TSCII").read()
        output = tamil.tscii.convert_to_unicode( str )
        print(output)
        needle = u"""உடுப்பி ஒட்டலுக்குப் போய் மசாலா தோசை சாப்பிட்டு வரலாமா"""
        assert( output.find(needle) >= 0 )

    def test_TSCII_to_UTF8_part2( self ):
        if PYTHON3:
            print("#### TEST NOT RUN FOR PYTHON3 #######")
            return
        str=open("data/dumb.tscii").read()
        output = tamil.tscii.convert_to_unicode( str )
        assert( output.find(u"அப்பா") >= 0 )
        
if __name__ == '__main__':    
    if not PYTHON3:
        test_support.run_unittest(Letters,Words,TSCII)
    else:
        unittest.main()
