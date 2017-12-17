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

if __name__ == '__main__':
    unittest.main()
