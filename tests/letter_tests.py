# -*- coding: utf-8 -*-
# (C) 2013-2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
import tamil.utf8 as utf8 
from tamil.tscii import TSCII
import codecs
        
if PYTHON3:
    class long(int):
        pass

class Arichuvadi(unittest.TestCase):
    def test_fcns(self):
        self.assertEqual( utf8.mei(0), u"க்" )
        self.assertEqual( utf8.uyir(0), u"அ" )
        self.assertEqual( utf8.uyirmei_constructed(1,1), u"\u0b9a\u0bbe" )
        self.assertEqual( utf8.agaram(0), u"க" )
        self.assertEqual( utf8.istamil_prefix(u"not a tamil word"),False)
        karuppan = utf8.uyirmei_constructed(1,1)+u"nottamil"
        self.assertEqual( utf8.istamil_prefix(karuppan),True)
    
    def test_watson(self):
        """ elementary - watson """
        parts = [letter for letter in utf8.get_letters_elementary_iterable(u'கழுதை')]
        actual = [u'க்', u'அ', u'ழ்', u'உ', u'த்', u'ஐ']
        self.assertEqual(parts,actual)
        parts2 = utf8.get_letters_elementary(u'கழுதை')
        self.assertEqual(parts2,actual)
        
    def test_split_uyirmei(self):
        p1 = utf8.grantha_uyirmei_splits[u'ழு']
        p2 = utf8.grantha_uyirmei_splits[u'தை']
        a1 = [u'ழ்',u'உ']
        a2 = [u'த்', u'ஐ']
        self.assertEqual(p1,a1)
        self.assertEqual(p2,a2)
    
    def test_assertions(self):
        ## some assertions, languages dont change fast.
        self.assertEqual ( tamil.utf8.TA_ACCENT_LEN , len(tamil.utf8.accent_symbols) )
        self.assertEqual ( tamil.utf8.TA_AYUDHA_LEN , 1 )
        self.assertEqual (  tamil.utf8.TA_UYIR_LEN , len( tamil.utf8.uyir_letters ) )
        self.assertEqual (  tamil.utf8.TA_MEI_LEN, len(  tamil.utf8.mei_letters ) )
        self.assertEqual (  tamil.utf8.TA_AGARAM_LEN, len(  tamil.utf8.agaram_letters ) )
        self.assertEqual (  tamil.utf8.TA_SANSKRIT_LEN, len(  tamil.utf8.sanskrit_letters )) 
        self.assertEqual (  tamil.utf8.TA_UYIRMEI_LEN, len(  tamil.utf8.uyirmei_letters ) )
        self.assertEqual (  tamil.utf8.TA_GRANTHA_UYIRMEI_LEN, len(  tamil.utf8.grantha_uyirmei_letters) )
        self.assertEqual (  tamil.utf8.TA_LETTERS_LEN, len(  tamil.utf8.tamil_letters) )
    
    def test_nos(self):
        self.assertEqual(utf8.tamil_len(),323)
        self.assertEqual(utf8.uyir_len(),12)
        self.assertEqual(utf8.mei_len(),18)
        self.assertEqual(utf8.agaram_len(),18)
        self.assertEqual(utf8.accent_len(),13)
        self.assertEqual(utf8.ayudha_len(),1)
    def test_repr(self):
        self.assertEqual( utf8.to_unicode_repr( u"அ" ), "u'\\u0b85'")
        
    
class Words(unittest.TestCase):
    def test_titanic(self):
        ta_parts = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள் பூஜ்ஜியம்".split()
        wlen_expected = [5, 5, 3, 2, 4, 2, 3, 2, 3, 8, 2, 5, 5]
        wlen = map( lambda x: len( tamil.utf8.get_letters( x) ), ta_parts)
        if PYTHON3:
            wlen = list(wlen)
        self.assertEqual( wlen, wlen_expected )
        
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
    def test_odd_case(self):
        # truly mal-formed inputs get mangled by get-letters
        not_a_word = u"ஆாள்"
        self.assertEqual(utf8.get_letters(not_a_word),[u"ஆா",u"ள்"])
        not_a_word = u"ஆள்்ஆ"
        self.assertEqual(utf8.get_letters(not_a_word),[u"ஆ",u"ள்்",u"ஆ"])
        
    def test_word_length( self ):
        actual = 5
        letters = utf8.get_letters(u"மென்பொருள்")        
        self.assertEqual( actual, len(letters) )
    
    def test_word_no2_length( self ):
        actual = 6
        letters = utf8.get_letters(u'[\u0baa-\u0baa\u0bcc]+')
        self.assertEqual( actual, len(letters) )
    
    def test_grantha( self ):
        self.assertEqual( 24, len(utf8.grantha_mei_letters) )
        self.assertEqual( 24, len(utf8.grantha_agaram_letters) )
        
    def test_unicode_repr( self ):    
        print("********* unicode repr ******")
        actual = utf8.to_unicode_repr(u'எழில்') 
        wanted = "u'\\u0b8e\\u0bb4\\u0bbf\\u0bb2\\u0bcd'"
        if ( LINUX ):
            print(wanted,actual)
            print(len(wanted),len(actual))
        self.assertEqual( actual, wanted )
    
    def test_getidx_n_tamil(self):
        for itr in range(0,utf8.tamil_len()):
            self.assertEqual(itr,utf8.getidx(utf8.tamil(itr)))
        
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
        
    def test_mei_to_agaram(self):
        na = utf8.mei_to_agaram(u"ன்")
        self.assertEqual( na, u"ன" )
        
    def test_words(self):
        _str = u"உடனே random elevator jazz உடனே எழுதினால் செய்திப் பத்திரிகை போஆகிவிடும் அசோகமித்திரன் நேர்காணல்"
        words = _str.split(u" ")
        
        letters = utf8.get_letters( _str )
        outWords = utf8.get_words( letters, tamil_only = False )
        if ( LINUX ):
            print( u"|".join(words) )
            print( u"|".join(outWords) )
        self.assertEqual( outWords, words )

    def test_tamil_only_words2(self):
        text = u'கல்பாக்கத்தை சேர்ந்தவர் தற்போது'
        expected = [u'கல்பாக்கத்தை', u'சேர்ந்தவர்', u'தற்போது']
        actual = tamil.utf8.get_tamil_words(tamil.utf8.get_letters(text))
        self.assertEqual(actual,expected)

    def test_get_words_neg(self):
        text = u'கல்பாக்கத்தை சேர்ந்தவர் தற்போது'
        self.assertRaises(Exception,lambda : tamil.utf8.get_tamil_words(text))

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

    def test_shamikshu( self ):
        word = u"க்ஷமிக்ஷூ"
        self.assertTrue( all( map( utf8.istamil, utf8.get_letters(word))) )
        self.assertTrue( all( map( utf8.istamil_alnum, utf8.get_letters(word))) )
    
    def test_tamil_letter_sizes( self ):
        self.assertEqual( len(utf8.uyir_letters), 12 )
        self.assertEqual( len(utf8.mei_letters) , 18 )
        self.assertEqual( len(utf8.uyir_letters),  (len(utf8.accent_symbols)-1) )
        self.assertEqual( len(utf8.uyirmei_letters) , 18*12 )
        self.assertEqual( len(utf8.sanskrit_letters) , 6 )
        self.assertEqual( len(utf8.tamil_letters) , 323 )

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
        
class CodecTSCII(unittest.TestCase):
    def test_vowels(self):
        assert( TSCII[0xAB] == u"அ" )
        assert( TSCII[0xAC] == u"ஆ" )
        
    def test_sanskrit(self):
        TSCII = tamil.tscii.TSCII
        assert( TSCII[0x82] == u"ஶ்ரீ")
        assert( TSCII[0x83] == u"ஜ")
        assert( TSCII[0x84] == u"ஷ")
    
    def test_arivuri(self):
        arivuri = '\x97\xC8\xA2\xD7\xC3\xA2'
        uArivuri = tamil.tscii.convert_to_unicode( arivuri )
        self.assertEqual( u"௮றிவுரி", uArivuri )
        
    def test_basic_lookup2UTF8( self ):
        TSCII = tamil.tscii.TSCII
        self.assertEqual( TSCII[0xAB]+TSCII[0xF4]+TSCII[0xC0]+TSCII[0xA1], u"அப்பா" )

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
    
    def test_project_MADURAI( self ):
        fname = "data/project_madurai_tscii.txt"
        fexact = "data/project_madurai_utf8.txt"
        
        # expected 
        with codecs.open( fexact , 'r', 'utf-8') as fileHandle:
            exact = fileHandle.read()            
        
        # convert 
        with codecs.open(fname,'r','utf-8') as fileHandle:
            output = tamil.tscii.convert_to_unicode( fileHandle.read() )
        self.maxDiff = None
        
        self.assertEqual( output, exact[:-1] )

if __name__ == '__main__':        
    unittest.main()
