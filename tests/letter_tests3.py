# This file is part of Open-Tamil package unittests

# setup the paths
from opentamiltests import *
from tamil.utf8 import *

class LetterTests(unittest.TestCase):
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
        asorted = sorted(agaram_letters,compare_words_lexicographic)
        consonants = sorted(list(set(consonants)),compare_words_lexicographic)
        #print(u"%d - %d"%(len(asorted),len(consonants)))
        self.assertEqual(asorted,consonants)
        
    
    def test_named_kombugal(self):
        kombugal = [accent_aa, accent_i, accent_u, accent_uu, accent_e, accent_ee, accent_ai, accent_o, accent_oo, accent_au ]
        self.assertTrue( accent_symbols[1:10], kombugal )
        
if __name__ == u"__main__":
    unittest.main()

