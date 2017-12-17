# -*- coding: utf-8 -*-
# (C) 2017 Muthiah Annamalai
#
# This file is part of 'open-tamil' package tests
#

# setup the paths
from opentamiltests import *
import os
from spell import Speller


class SpellInterfaceTest(unittest.TestCase):
    def test_basic(self):
        filename = os.path.join("data","doc1.spell")
        sys.stdin.close()
        obj = Speller(filename,lang="ta")
        self.assertTrue(obj.in_tamil_mode())
        #self.assertEqual(obj.error_count(),14)

if __name__ == '__main__':
    unittest.main()
