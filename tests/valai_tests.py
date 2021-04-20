# -*- coding: utf-8 -*-
# (C) 2016-17 Muthiah Annamalai

from opentamiltests import *
import os
import codecs
from pprint import pprint
from spell import Speller, LoadDictionary, OttruSplit, Mayangoli, ASpell
from valai import solthiruthi as tamilpesu
from valai import vaani

CURRDIR = os.path.dirname(os.path.abspath(__file__))


class TamilpesuTest(unittest.TestCase):
    def test_basic(self):
        tp = tamilpesu.SpellChecker()
        try:
            options = tp.check_word(u"வாணி என்பது ஒரு")
        except Exception as e:
            return
        self.assertEqual(len(options), 1)
        self.assertGreaterEqual(len(options[0].alternatives), 2)

    def test_aspell_parse_fmt(self):
        results = {}
        with codecs.open(os.path.join(CURRDIR, "data", "aspell.out"), "r", "utf-8") as fp:
            data = fp.read()
        ASpell.parse_result(results, data)
        self.assertEqual(len(results), 15)
        self.assertTrue("செய்வது" in results)
        self.assertEqual(len(results["செய்வது"]), 19)
        miss = ["செய்து", "செய்தி", "நெய்து", "பெய்து", "செய்", "ஆய்வு", "உய்வு", "எய்து", "ஓய்வு", "சத்து", "செய்ய",
                "யுவதி", "தேய்வு", "தொய்வு", "பெய்வி", "வாய்வு", "வயது", "யாது", "தயவு"]
        self.assertListEqual(results["செய்வது"], miss)


if __name__ == "__main__":
    unittest.main()
