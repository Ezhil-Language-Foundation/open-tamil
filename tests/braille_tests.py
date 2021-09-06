# -*- coding: utf-8 -*-
# This file is part of Open-Tamil package unittests
# (C) 2018 Muthu Annamalai

import string

import tabraille
# setup the paths
from opentamiltests import *


class BrailleTests(unittest.TestCase):
    def test_braille(self):
        self.assertEqual(len(tabraille.table), 74, "74 elements expected in table")

    def test_atoz(self):
        for letter in string.ascii_lowercase:
            self.assertTrue(tabraille.table[letter])

    def test_braille_mapping(self):
        expected = [
            tabraille.table["ந"],
            tabraille.table["ஆ"],
            tabraille.table["ன"],
            tabraille.table["்"],
        ]
        self.assertListEqual(tabraille.map_to_braille("நான்"), expected)

    def test_braille_mapping2(self):
        word = "கப்பல்"
        letters = ["க", "ப", "்", "ப", "ல", "்"]
        expected = [tabraille.table[l] for l in letters]
        self.assertEqual(tabraille.map_to_braille(word), expected)


if __name__ == "__main__":
    unittest.main()
