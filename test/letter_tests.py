# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
import tamil.utf8 as utf8 
from tamil.tscii import TSCII

if PYTHON3:
    class long(int):
        pass

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
        self.assertEqual( actual, len(letters) )
    
    def test_word_no2_length( self ):
        actual = 6
        letters = utf8.get_letters(u'[\u0baa-\u0baa\u0bcc]+')
        self.assertEqual( actual, len(letters) )
    
    def test_grantha( self ):
        self.assertEqual( 22, len(utf8.grantha_mei_letters) )
        self.assertEqual( 22, len(utf8.grantha_agaram_letters) )
        
    def test_unicode_repr( self ):    
        print("********* unicode repr ******")
        actual = utf8.to_unicode_repr(u'எழில்') 
        if PYTHON3:
            wanted = u"'\u0b8e\u0bb4\u0bbf\u0bb2\u0bcd'"
        else:
            wanted = "u'\\u0b8e\\u0bb4\\u0bbf\\u0bb2\\u0bcd'"
        if ( LINUX ):
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
        if ( LINUX ):
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
        if ( LINUX ): print(utf8.uyirmei(2))
        assert( utf8.uyirmei(2)  == u"கி" )
    
    def test_letter_extract_from_code_pts(self):
        letters = utf8.get_letters(u"கூவிளம் என்பது என்ன சீர்")
        #print "len ==== > " , len(letters)
        assert( len(letters) == 16 )
        for pos,letter in  enumerate(letters):
            if ( LINUX ): print(u"%d %s"%(pos,letter))
        assert( letter == (u"ர்") )

    def test_letter_extract_with_ascii(self):
        letters = utf8.get_letters(u"கூவிளம் is என்பது also என்ன a சீர்")
        print( "len ==== > " , len(letters) )
        assert(len(letters) == 26 )
        for pos,letter in  enumerate(letters):
            if ( LINUX ): print(u"%d %s"%(pos,letter))
        assert( letters[-4] == u"a" )

    def test_words(self):
        _str = u"உடனே random elevator jazz உடனே எழுதினால் செய்திப் பத்திரிகை போஆகிவிடும் அசோகமித்திரன் நேர்காணல்"
        words = _str.split(u" ")

        letters = utf8.get_letters( _str )
        outWords = utf8.get_words( letters )
        if ( LINUX ):
            print( u"|".join(words) )
            print( u"|".join(outWords) )
        assert( outWords == words )

    def test_tamil_only_words(self):
        s = u"உடனே உடனே seventh heaven எழுதினால் செய்திப் பத்திரிகை போஆகிவிடும் அசோகமித்திரன் நேர்காணல்"
        words = s.replace(u"seventh heaven ",u"").split(u" ")
        letters = utf8.get_letters( s )
        outWords = utf8.get_tamil_words( letters )        
        if ( LINUX ):
            print( u"|".join(words) )
            print( u"|".join(outWords) )
        self.assertEqual( outWords, words )
        
    def test_letter_extract_yield_with_ascii(self):
        letters = []
        ta_str = u"கூவிளம் is என்பது also என்ன a சீர்"
        for l in  utf8.get_letters_iterable(ta_str):
            letters.append( l )
        act_letters = utf8.get_letters(ta_str)
        print( "len ==== > " , len(letters),"get_letters CALL = ",len(act_letters) )
        assert(len(letters) == len(act_letters) )
        for pos,letter in  enumerate(letters):
            if ( LINUX ): print( u"%d %s"%(pos,letter) )
        self.assertEqual( letters[-4], u"a" )
        
    def test_letter_extract_yield(self):
        ta_str = u"கூவிளம் என்பது என்ன சீர்"
        act_letters = utf8.get_letters(ta_str)
        letters = []
        for l in utf8.get_letters_iterable(ta_str):
            letters.append( l )
        print( "len ==== > " , len(letters) )
        assert( len(letters) == 16 )
        print( "len ==== > " , len(letters),"get_letters CALL = ",len(act_letters) )
        assert(len(letters) == len(act_letters) )
        for pos,letter in  enumerate(letters):
            if ( LINUX ): print(u"%d %s"%(pos,letter))
        assert( letter == (u"ர்") )

    def test_reverse_words( self ):
        """ unittest for reverse a Tamil string"""
        if ( LINUX ):
            print( utf8.get_letters(u"இந்த") )
            print( u"".join(utf8.get_letters(u"இந்த")) )
        for word in u"இந்த (C) tamil முத்தையா அண்ணாமலை 2013 இந்த ஒரு எழில் தமிழ் நிரலாக்க மொழி உதாரணம்".split():
            rword = utf8.reverse_word(word)
            if ( LINUX ):
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
        assert( len(letters) == 27 )
        self.assertTrue( letters[13] == u"தெ" )
        
    def test_mei_vaggupu( self ):
        vaguppu = list()
        for cat in [utf8.vallinam_letters, utf8.mellinam_letters, utf8.idayinam_letters]:
            self.assertTrue( len(cat), 6 ) 
            vaguppu.extend( cat )
        
        self.assertEqual( len(vaguppu), len(utf8.mei_letters) )
        # assert mei = sum of all 3
        self.assertTrue( all( [ mei in vaguppu for mei in utf8.mei_letters] ) )                
    
    def test_istamil( self ):
        zz = u"முத்தையா அண்ணாமலை எந்த ஒரு தெரிந்த அல்லது தெரியாத எழுத்துருவாகவிருந்தாலும் அதனை மேல்தட்டில் உள்ளிட்டு கீழே உள்ள முடியும்"
        for z in zz.split(u" "):
            print("********** t/f ********")
            for x,y in zip(map(utf8.istamil,utf8.get_letters(z)),utf8.get_letters(z)):
                if ( LINUX ): print(u"%s => %s"%(y,x))        
                assert( all( map( utf8.istamil, utf8.get_letters( z ) ) ) )
        
        z = u"முத்தையா அண்ணாமலை"
        assert( any( map( utf8.istamil, utf8.get_letters( z ) ) ) )
        
        correct = [True, True, True, True, False, True, True, True, True, True, False, False, False, False, False]
        print ( list(map(utf8.istamil,utf8.get_letters(u"முத்தையா அண்ணாமலை 2013"))) )
        print ( correct )
        assert( list(map(utf8.istamil,utf8.get_letters(u"முத்தையா அண்ணாமலை 2013"))) == correct )
    
    def test_kuril_nedil(self):
        letters = list()
        letters.extend( utf8.kuril_letters )
        self.assertEqual( len(letters), 5)
        letters.extend( utf8.nedil_letters )
        self.assertEqual( len(letters), 10)
        letters.extend( [u"ஐ",u"ஔ"] )
        self.assertTrue( all( [x in letters for x in utf8.uyir_letters ] ) )
        return
    
class NumeralTestAmerican(unittest.TestCase):
    def runTest(self,var,nos):
        for numerStr,num in zip(var,nos):
            print('Testing ---> ',num)
            self.assertEqual( numerStr, tamil.numeral.num2tamilstr_american( num ), num )
        return

    def test_friend_of_rama( self ):
        ramanujan = 1729
        gometra = tamil.numeral.num2tamilstr( ramanujan )
        expected = u"ஓர் ஆயிரத்தி எழுநூற்று இருபத்தி ஒன்பது"
        self.assertEqual( gometra, expected )
    
    def test_units( self ):
        units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
        self.runTest( units, range(0,11) )
        return

        
    def test_units( self ):
        units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
        self.runTest( units, range(0,11) )
        return
        
    def test_teens( self ):
        teens = (u'பதினொன்று', u' பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து',u'பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19    
        self.runTest( teens, range(11,20) )
        return
        
    def test_tens ( self ):
        tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது',u'அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
        self.runTest( tens, range(10,100,10) )
        return
        
    def test_100s( self ):
        hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு','ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 - 900
        self.runTest( hundreds, range(100,1000,100) )
        return
        
    def test_max( self ):
        maxno = long(1e15 - 1)
        expected = u'தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது டிரில்லியன் தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது பில்லியன் தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது மில்லியன் தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது'
        self.assertEqual( tamil.numeral.num2tamilstr_american( maxno ), expected )
        return
    
    def test_numerals(self):
        var = {0:u"பூஜ்ஜியம்",
        long(1e7):u"பத்து மில்லியன்",
        long(1e9-1):u"தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது மில்லியன் தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது",
        3060:u"மூன்று ஆயிரத்தி அறுபது",
        1:u"ஒன்று",
        2:u"இரண்டு",
        3:u"மூன்று",
        5:u"ஐந்து",
        10:u"பத்து",
        11:u"பதினொன்று",
        17:u"பதினேழு",
        19:u"பத்தொன்பது",
        20:u"இருபது",
        21:u"இருபத்தி ஒன்று",
        1051:u"ஓர் ஆயிரத்தி ஐம்பத்தி ஒன்று",
        100000:u"நூறு ஆயிரம்",
        100001:u"நூறு ஆயிரத்தி ஒன்று",
        10011:u"பத்து ஆயிரத்தி பதினொன்று",
        49:u"நாற்பத்தி ஒன்பது",
        50:u"ஐம்பது",
        55:u"ஐம்பத்தி ஐந்து",
        1000001:u"ஒரு மில்லியன் ஒன்று",
        90:u"தொன்னூறு",
        99:u"தொன்னூற்றி ஒன்பது",
        100:u"நூறு",
        101:u"நூற்றி ஒன்று",
        1000:u"ஓர் ஆயிரம்",
        111:u"நூற்றி பதினொன்று",
        1000000000000:u"ஒரு டிரில்லியன்",
        1011:u"ஓர் ஆயிரத்தி பதினொன்று"}
        
        for k,actual_v in var.items():
            v = tamil.numeral.num2tamilstr_american(k)
            print('verifying => # %d'%k)
            self.assertEqual(v,actual_v,k)
        return

class NumeralTest(unittest.TestCase):
    def runTest(self,var,nos):
        for numerStr,num in zip(var,nos):
            print('Testing ---> ',num)
            self.assertEqual( numerStr, tamil.numeral.num2tamilstr( num ), num )
        return

    def test_units( self ):
        units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
        self.runTest( units, range(0,11) )
        return

        
    def test_units( self ):
        units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
        self.runTest( units, range(0,11) )
        return
        
    def test_teens( self ):
        teens = (u'பதினொன்று', u' பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து',u'பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19    
        self.runTest( teens, range(11,20) )
        return
        
    def test_tens ( self ):
        tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது',u'அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
        self.runTest( tens, range(10,100,10) )
        return
        
    def test_100s( self ):
        hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு','ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 - 900
        self.runTest( hundreds, range(100,1000,100) )
        return
        
    def test_max( self ):
        maxno = long(1e12 - 1 )
        expected = u'தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது கோடியே தொன்னூற்றி ஒன்பது இலட்சத்தி தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது'
        self.assertEqual( tamil.numeral.num2tamilstr( maxno ), expected )
        return
    
    def test_numerals(self):
        var = {0:u"பூஜ்ஜியம்",
        3060:u"மூன்று ஆயிரத்தி அறுபது",
        1:u"ஒன்று",
        2:u"இரண்டு",
        3:u"மூன்று",
        5:u"ஐந்து",
        10:u"பத்து",
        11:u"பதினொன்று",
        17:u"பதினேழு",
        19:u"பத்தொன்பது",
        20:u"இருபது",
        21:u"இருபத்தி ஒன்று",
        1051:u"ஓர் ஆயிரத்தி ஐம்பத்தி ஒன்று",
        100000:u"ஒரு இலட்சம்",
        100001:u"ஒரு இலட்சத்தி ஒன்று",
        10011:u"பத்து ஆயிரத்தி பதினொன்று",
        49:u"நாற்பத்தி ஒன்பது",
        50:u"ஐம்பது",
        55:u"ஐம்பத்தி ஐந்து",
        1000001:u"பத்து இலட்சத்தி ஒன்று",
        90:u"தொன்னூறு",
        99:u"தொன்னூற்றி ஒன்பது",
        100:u"நூறு",
        101:u"நூற்றி ஒன்று",
        1000:u"ஓர் ஆயிரம்",
        111:u"நூற்றி பதினொன்று",
        1000000000000:u"ஒரு இலட்சம் கோடி",
        1011:u"ஓர் ஆயிரத்தி பதினொன்று"}
        
        for k,actual_v in var.items():
            v = tamil.numeral.num2tamilstr(k)
            print('verifying => # %d'%k)
            self.assertEqual(v,actual_v,k)
        return

class CodecTSCII(unittest.TestCase):
    def test_vowels(self):
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
        with open("data/Sample.TSCII") as fp:
            str = fp.read()
        output = tamil.tscii.convert_to_unicode( str )
        if ( LINUX ): print(output)
        needle = u"""உடுப்பி ஒட்டலுக்குப் போய் மசாலா தோசை சாப்பிட்டு வரலாமா"""
        assert( output.find(needle) >= 0 )

    def test_TSCII_to_UTF8_part2( self ):
        if PYTHON3:
            print("#### TEST NOT RUN FOR PYTHON3 #######")
            return
        with open("data/dumb.tscii") as fp: str = fp.read()
        output = tamil.tscii.convert_to_unicode( str )
        assert( output.find(u"அப்பா") >= 0 )

if __name__ == '__main__':        
    unittest.main()
