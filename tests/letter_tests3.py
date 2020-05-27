# -*- coding: utf-8 -*-
# This file is part of Open-Tamil package unittests
# (C) 2018 Muthu Annamalai

# setup the paths
from opentamiltests import *
import unicodedata
import codecs
from tamil.utf8 import *
from tamil import tace16
import tamiltts
from functools import cmp_to_key

class TTSTests(unittest.TestCase):
    def test_normalize_symbols(self):
        text = ["இரு","நண்பர்கள்","௹","100","கொடுத்து","உணவு","உண்டனர்."]
        text_out = tamiltts.normalize_punctuation_text(text)
        expected = ['இரு', 'நண்பர்கள்', 'ரூபாய்', '100', 'கொடுத்து', 'உணவு', 'உண்டனர்.']
        self.assertEqual(text_out,expected)

    def test_normalize_numerals(self):
        text = ["இரு","நண்பர்கள்","௹","100","கொடுத்து","உணவு","உண்டனர்."]
        text_out = tamiltts.normalize_numeral_text(text)
        expected = ['இரு', 'நண்பர்கள்', '௹', 'நூறு', 'கொடுத்து', 'உணவு', 'உண்டனர்.']
        self.assertEqual(text_out,expected)

class LetterTests(unittest.TestCase):
    def test_GOI_encoding(self):
        coded = "baaba4bc1-b85bb1bbfbb5bc1ba4bcd-ba4b95bb5bb2bcdb95bb3bcd/baaba9bcdba9bbeb9fbcdb9fbc1baabcd-baabb2bb5b95bc8baabcd-baabafba3bbfb95bb3bcd-b92bb0bcd-b95ba3bcdba3b9fbcdb9fbaebcd"
        decoded=['பது',  'அறிவுத்',  'தகவல்கள்',  'பன்னாட்டுப்',  'பலவகைப்',
                        'பயணிகள்',  'ஒர்',  'கண்ணட்டம்']
        actual=hex2unicode(coded)
        self.assertListEqual(decoded,actual)

    def test_unicode2hex(self):
        actual = unicode2hex('கர்ப்ப-சுகாதாரம்')
        self.assertEqual(actual,'b95bb0bcdbaabcdbaa-b9abc1b95bbeba4bbebb0baebcd')

    def test_indian_rupee_symbol(self):
        self.assertTrue( "₹" in  get_letters("₹ 500") )

    def test_tamil247(self):
        self.assertEqual( len(tamil247), 247 )

    def test_has_english(self):
        expected = [True,True,False,False]
        result = list(map(has_english, ['Tamil','Telugu','தமிழ்','கிரேக்கம்'] ))
        self.assertEqual(result,expected)

    def test_named_vowels(self):
        vowels = [vowel_a, vowel_aa, vowel_i, vowel_ii, vowel_u, vowel_uu, vowel_e, vowel_ee, vowel_ai, vowel_o, vowel_oo, vowel_au]
        self.assertEqual( vowels, uyir_letters )

    def test_named_consonants(self):
        consonants = [consonant_ka,
                      consonant_nga,
                      consonant_ca,
                      #consonant_ja,
                      consonant_nya,
                      consonant_tta,
                      consonant_nna,
                      consonant_nnna,
                      consonant_ta,
                      consonant_tha,
                      consonant_na,
                      consonant_pa,
                      consonant_ma,
                      consonant_ya,
                      consonant_ra,
                      consonant_rra,
                      consonant_la,
                      consonant_lla,
                      consonant_llla,
                      consonant_zha,
                      consonant_va] #this array has a few duplicates
        if PYTHON3:
            asorted = tamil_sorted(agaram_letters)
            consonants = sorted(list(set(consonants)),key=cmp_to_key(compare_words_lexicographic))
        else:
            asorted = tamil_sorted(agaram_letters)
            consonants = sorted(list(set(consonants)),cmp=compare_words_lexicographic)
        self.assertEqual(asorted,consonants)

    def test_named_kombugal(self):
        kombugal = [accent_aa, accent_i, accent_u, accent_uu, accent_e, accent_ee, accent_ai, accent_o, accent_oo, accent_au ]
        self.assertTrue( accent_symbols[1:10], kombugal )

    def test_utf16(self):
        # as long as data are in unicode format we dont care the encoding in the file as UTF-8 or UTF-16.
        # see: SO #10288016
        word_lengths = [69, 65, 64, 79, 62, 62, 71, 61, 70, 63]
        with codecs.open(os.path.join(os.path.dirname(__file__),'data','utf16-demo.txt'),'r','utf-16') as fp:
            t = fp.readlines()
        self.assertSequenceEqual( word_lengths, list(map(len,list(map(get_letters,t)))) )
        self.assertEqual( unicodedata.name(t[1][11]), 'TAMIL LETTER E' )

class TaceTests(unittest.TestCase):
    def test_tace16(self):
       muttram = "முற்றம்"
       word = [tace16.rebase_ord(x) for x in ["","","",""]]
       im = tace16.rebase_ord("") #ம்
       u = tace16.rebase_ord("") #உ
       mei,uyir = tace16.splitMeiUyir(word[0])
       self.assertEqual( mei, im)
       self.assertEqual( uyir, u)
       _mu = tace16.joinMeiUyir(im , u)
       self.assertEqual( _mu, word[0] )

    def test_tace16_letters(self):
        text_utf8 = "தமிழ் இயற்கை மொழி பகுப்பாய்வு நிரல்தொகுப்பு"
        text = "    "
        letters = tace16.get_letters([tace16.rebase_ord(c) for c in text])
        self.assertEqual(len(letters),len(get_letters(text_utf8)))

    def test_is_tace16_codepoint(self):
        actual = [b'\x1c', b'\x1d', b'\x18', b'\x19', b'\x84', b'\x88', b'\x89', b'\x8a', b'\x8b', b'\x8d']
        self.assertListEqual( list(tace16.to_bytes(tace16.TACE16[0:10])), actual )

    def test_tace16_as_bytes(self):
       muttram = "முற்றம்"
       _word = [tace16.rebase_ord(x) for x in ["","","",""]]
       word = list(tace16.to_bytes(_word))
       im = list(tace16.to_bytes(tace16.rebase_ord("")))[0] #ம்
       u = list(tace16.to_bytes(tace16.rebase_ord("")))[0] #உ
       mei,uyir = tace16.splitMeiUyir(tace16.rebase_ord(word[0]))
       self.assertEqual( mei, tace16.rebase_ord(im))
       self.assertEqual( uyir, tace16.rebase_ord(u))
       _mu = tace16.joinMeiUyir(tace16.rebase_ord(im) , tace16.rebase_ord(u))
       self.assertEqual( _mu, tace16.rebase_ord(word[0]) )

if __name__ == "__main__":
    unittest.main()
