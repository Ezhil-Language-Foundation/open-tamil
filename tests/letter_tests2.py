# -*- coding: utf-8 -*-
# (C) 2017 Muthiah Annamalai
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

class Letters(unittest.TestCase):
    def test_uyir_mei_split(self):
        ak = utf8.splitMeiUyir(u"ஃ")
        self.assertEqual(ak,u"ஃ")
        il = utf8.splitMeiUyir(u"ல்")
        self.assertEqual(il,u"ல்")
        il,ee = utf8.splitMeiUyir(u"லி")
        self.assertEqual((il,ee),(u"ல்",u"இ"))

    def test_classifier(self):
        expected = []
        expected.extend(['english']*3)
        expected.extend(['digit']*4)
        expected.extend(['kuril','nedil','uyirmei','vallinam','uyirmei'])
        data = list(map(utf8.classify_letter,utf8.get_letters(u"abc1230அஆரெட்டை")))
        self.assertEqual(data,expected)
    
    def test_classified_except(self):
        with self.assertRaises(ValueError) as ve:
            utf8.classify_letter(u'.')

if __name__ == '__main__':
    unittest.main()
