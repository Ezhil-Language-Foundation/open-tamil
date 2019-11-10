# -*- coding: utf-8 -*-
# (C) 2016-17 Muthiah Annamalai

from opentamiltests import *
import os
import codecs
from pprint import pprint
from spell import Speller, LoadDictionary, OttruSplit, Mayangoli
from valai import solthiruthi as tamilpesu
from valai import vaani

class TamilpesuTest(unittest.TestCase):
        def test_basic(self):
              tp = tamilpesu.SpellChecker()
              options = tp.check_word(u'வாணி என்பது ஒரு')
              self.assertEqual( len(options), 1)
              self.assertGreaterEqual( len(options[0].alternatives), 2 )

if __name__ == "__main__":
    unittest.main()
