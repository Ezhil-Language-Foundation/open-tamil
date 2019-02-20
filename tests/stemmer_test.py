# -*- coding: utf-8 -*-
## (C) 2019 Muthiah Annamalai,
from opentamiltests import *
from tamilstemmer import TamilStemmer

class TamilTest(unittest.TestCase):
    def __init__(self,*args):
        unittest.TestCase.__init__(self,*args)
        self.ta_stemmer = TamilStemmer()
        self.assertTrue( self.ta_stemmer != None )
        
    def test_suffix(self):
        wordlist = [u'மலைகள்',u'பாடுதல்',u'ஓடினான்']
        expected = [u'மலை',u'பாடு', u'ஓடி']
        stems = [self.ta_stemmer.stemWord(word) for word in wordlist]
        self.assertSequenceEqual( stems, expected )

if __name__ == "__main__":
    unittest.main()
