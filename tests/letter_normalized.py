# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from __future__ import print_function
from opentamiltests import *

class TestSummarizer(unittest.TestCase):
    def test_float_like_butterfly_sting_like_a_bee(self):
        title = u"""
    குத்துச்சண்டை ஜாம்பவான் முகமது அலி மறைவு
        """
        
        content = u"""
    அமெரிக்காவின் முன்னாள் ஹெவி வெயிட் குத்துச்சண்டை வீரர் முகமது அலி காலமானார். அவருக்கு வயது 74. சுவாசக்கோளாறு காரணமாக முகமது அலி மரணமடைந்ததாக அவரது குடும் பத்தினர் வெளியிட்டுள்ள அறிக்கையில் கூறியுள்ளனர்.
    உலக குத்துச்சண்டை சாம்பியன் பட்டத்தை 3 முறை வென்று சாதனை படைத்தவர் முகமது அலி. அமெரிக்காவின் கென்டகி மாநிலத்தில் 1942-ம் ஆண்டு பிறந்த முகமது அலியின் இயற்பெயர் காசியஸ் க்ளே. தனது 18 வயதில் குத்துசண்டை களத்தில் இறங்கிய முகமது அலி 1960-ல் ஹெவிவெயிட் ஒலிம்பிக் தங்கப் பதக்கத்தை பெற்றார். இதைத்தொடர்ந்து குத்துச்சண்டை என்றாலே முகமது அலி என்று சொல்லும் அளவுக்கு புகழ்பெற்றார். குத்துச்சண்டை களத்தில் மட்டுமின்றி அமெரிக்காவில் அக்காலத்தில் தீவிரமாக பரவியிருந்த இனவெறிக்கு எதிராகவும் அவர் போராடினார். அவர் குவிக்கும் வெற்றிகள் கறுப்பின மக்களிடையே புதிய எழுச்சியை ஏற்படுத்தின.
    1960-ல் இருந்து 1981 வரை முகமது அலி குத்துச்சண்டை உலகின் முடிசூடா மன்னனாக இருந்தார். 61 தொழில்முறை குத்துச்சண்டை போட்டிகளில் 56-ல் வெற்றி பெற்று அனைவரையும் ஆச்சரியத்தில் ஆழ்த்தினார். இதில் 37 போட்டிகளில் நாக் அவுட் முறையில் வென்றதால் ‘நாக் அவுட் நாயகன்’ என்று அழைக்கப்பட்டார். 3 முறை உலக குத்துச்சண்டை சாம்பியன் பட்டத்தை வென்றார்.
    ஒரு தேனீயைப் போல களத்தில் வேகமாக செயலாற்றி கண்ணிமைக்கும் நேரத்தில் சரமாரியான குத்துகளை விட்டு எதிரிகளை நிலைகுலையச் செய்வது அவரது பாணியாக இருந்தது. இதனாலேயே தனது நாடான அமெரிக்காவில் மட்டுமின்றி உலகம் முழுவதும் அவர் புகழ்பெற்றார்.
    குத்துச்சண்டை களத்தில் இருந்து ஓய்வுபெற்ற அவரை 1980-களின் தொடக்கத்தில் பார்கின்சன் நோய் தாக்கியது. பார்கின்சன் என்பது மத்திய நரம்பு மண்டலத்தில் பாதிப்பை ஏற்படுத்தி அதன்மூலம் மனிதனின் இயக்கத்தை முடக்கக்கூடிய ஒருவிதமான வாத நோயாகும். குத்துச்சண்டை போட்டி களுக்காக கடுமையான பயிற்சிகளை மேற்கொண்டதால் அவரை இந்த நோய் தாக்கியதாக கூறப்படுகிறது.
    30 ஆண்டுகளுக்கும் மேலாக பார்கின்சன் நோயுடன் போராடி வந்த அவர் கடந்த ஆண்டு மூச்சுத்திணறல் மற்றும் சிறுநீரகத் தொற்று உள்ளிட்ட உபாதைகளால் பாதிக்கப்பட்டார். இந்நிலையில் சுவாசப் பிரச்சினை காரணமாக பீனிக்ஸில் உள்ள மருத்துவமனையில் அனுமதிக்கப்பட்டார்.
    முகமது அலி அனுமதிக்கப்பட்டதைத் தொடர்ந்து அவரது ரசிகர்கள் மருத்துவ மனையைச் சூழ்ந்தனர். அவர் நலம் பெற்று வர வேண்டும் என்பதற்காக பிரார்த் தனைகளிலும் ஈடுபட்டனர்.
    இந்நிலையில் நேற்று முன் தினம் இரவு அவர் மருத்துவ மனையில் காலமானார். இது குறித்து அவரது குடும்பத்தினர் வெளியிட்டுள்ள அறிக்கையில் சுவாசப் பிரச்சினை காரணமாக அவர் மரணமடைந்ததாக கூறப்பட்டுள்ளது.
    முகமது அலிக்கு 9 குழந் தைகள். அவரது மகள் லைலா அலி குத்துச்சண்டையில் உலக சாம்பியன் பட்டத்தை வென்றவர். முகமது அலியின் உடல் அடக்கம் சொந்த நகரான லூயிவிலியில் நடைபெற உள்ளது. அவரது மறைவுக்கு பிரதமர் மோடி இரங்கல் தெரிவித்துள்ளார்.
        """

        # Create a SummaryTool object
        st = tamil.utils.SummaryTool()

        # Build the sentences dictionary
        sentences_dic = st.get_sentences_ranks(content)
        
        # Build the summary with the sentences dictionary
        summary = st.get_summary(title, content, sentences_dic)
        
        # Print the summary
        if LINUX:
            print(summary)
        
        # Test for following:
        #1) 1/2 compression ratio
        self.assertTrue( len(content) > 2*len(summary))
        #2) ensure 'முகமது அலி' is part of summary
        self.assertTrue( u"முகமது அலி" in summary )

class Utf8Normalized(unittest.TestCase):
    def test_simple_check_normalized(self):
        self.assertFalse( tamil.utf8.is_normalized(u"தொ") ) #த ெ ா 
        self.assertTrue( tamil.utf8.is_normalized(u"தொ")) # த ொ
    
    def test_next_check_normalized(self):
        self.assertFalse( tamil.utf8.is_normalized(u"கெள"))  #க ெ ள -> கெள
        self.assertTrue( tamil.utf8.is_normalized(u"கௌ")) #க ௌ
    
    def test_simple_split(self):
        l,r = u"த்",u"ஒ"
        #non-normalized case
        a,b=tamil.utf8.splitMeiUyir(u"தொ")
        self.assertEqual( (a,b) , (l,r) )
        
    def test_simple_split_regular(self):
        l,r = u"த்",u"ஒ"
        #normalized case
        a1,b1 = tamil.utf8.splitMeiUyir(u"தொ")
        self.assertEqual( (a1,b1) , (l,r) )

class Words(unittest.TestCase):
    def test_lexico_compare( self ):
        res = [0,1,-1]
        self.assertEqual( list(map( lambda x: tamil.utf8.compare_words_lexicographic( u"சம்மத", x),[u"சம்மத",u"சம்த",u"தசம்"])),res)

    def test_unicode_tamil(self):
        val = []
        str_in = u'LnX3.14-சம்மதசம்ததசம்'
        for i in range(0,len(str_in)):
            letter = str_in[i]
            val.append( tamil.utf8.is_tamil_unicode( letter ) )
        
        act = [False,
               False,
               False,
               False,
               False,
               False,
               False,
               False,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True,
               True]
        
        self.assertEqual( val, act )
        return
    
    def test_isalnum( self ):
        self.assertTrue( tamil.utf8.istamil_alnum('LiNuX') )
        self.assertFalse( tamil.utf8.istamil_alnum('3.14159') )
    
    def test_all_tamil( self ):
        non_norm = u"ப" +  u"ெ" + u"ா" + u"பொ"
        self.assertTrue( tamil.utf8.is_normalized(u"சம்மதம்") )
        self.assertTrue( tamil.utf8.is_normalized(non_norm[0]) )
        self.assertTrue( tamil.utf8.is_normalized(non_norm[0:1]) )
        self.assertTrue( tamil.utf8.is_normalized(non_norm[0:2]) )
        self.assertFalse( tamil.utf8.is_normalized(non_norm[0:3]) )
        self.assertFalse( tamil.utf8.is_normalized(non_norm) )
        return

    def test_long_str_embedded( self ):
        o_data = "This file is part of 'open-tamil' package tests"
        long_non_norm = u"ப" +  u"ெ" + u"ா" + u"பொ"
        data = o_data + long_non_norm + o_data
        self.assertFalse( tamil.utf8.is_normalized( data ) )
        self.assertTrue(tamil.utf8.is_normalized( o_data ) )
        self.assertFalse(tamil.utf8.is_normalized( long_non_norm ) )
        return

    def test_rev_words(self):
        rhymie = [(u"மாங்குயில்",u"ல்யிகுங்மா"),(u"பூங்குயில்",u"ல்யிகுங்பூ"), (u"அல்லவா",u"வாலல்அ"),\
                  (u"செல்வாயா",u"யாவால்செ"), (u"சொல்வாயா",u"யாவால்சொ")]
        for k,v in rhymie:
            self.assertEqual( tamil.utf8.reverse_word(k), v)
            self.assertEqual( tamil.utf8.reverse_word(v), k)
        return

if __name__ == '__main__':        
    unittest.main()
