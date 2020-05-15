# -*- coding: utf-8 -*-
# This file is part of Open-Tamil package unittests
# (C) 2018 Muthu Annamalai

# setup the paths
from opentamiltests import *
import unicodedata
import codecs
from tamil.utf8 import *
from tamil import tace16
if PYTHON3:
    from functools import cmp_to_key

class LetterTests(unittest.TestCase):
    def test_indian_rupee_symbol(self):
        print((get_letters("₹ 500")))
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

    def test_tace16(self):
       muttram = "முற்றம்"
       word = [ord(x) for x in ["","","",""]]
       im = ord("") #ம்
       u = ord("") #உ
       mei,uyir = tace16.splitMeiUyir(word[0])
       self.assertEqual( mei, im)
       self.assertEqual( uyir, u)
       
if __name__ == "__main__":
    unittest.main()
