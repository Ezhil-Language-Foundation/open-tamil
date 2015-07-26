# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.dictionary import *

# Test the canned dictionary with data structure
class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.TVU,self.TVU_size = DictionaryBuilder.create(TamilVU)
        
    def tearDown(self):
        del self.TVU
        
    def test_factory_TVU(self):
        TVU_agarathi,size = self.TVU,self.TVU_size
        self.assertTrue(isinstance(TVU_agarathi,TamilVU))
        self.assertEqual(size,63896)
        return
    def test_isword(self):
        words = u"தமிழ் நாட்டில் சங்ககாலத்திலேயே ஒட்டியாணம் போன்ற இடையணிகள் இருந்தமைக்கான சான்றுகளும் பெண்".split(" ")
        self.assertEqual(len(list(filter(self.TVU.isWord,words))),3)
        self.assertTrue(self.TVU.isWord(u"தமிழ்"))
        
if __name__ == "__main__":
    unittest.main()
