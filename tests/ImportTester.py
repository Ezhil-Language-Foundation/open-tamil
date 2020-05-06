# -*- coding: utf-8 -*-
# (C) 2015-2017, 2020 Muthiah Annamalai
#
# This file is part of 'open-tamil' package tests
#

# setup the paths
from opentamiltests import *

class ImportTester(unittest.TestCase):
    def test_import_tester(self):
        import tamil; import ngram; import transliterate

    def test_import_num2tamilstr(self):
        from tamil.numeral import num2tamilstr, num2tamilstr_american
        for key in ['num2tamilstr','num2tamilstr_american']:
            assert locals()[key]

    def test_kural(self):
        from kural import Kural, Thirukkural
        kk = Thirukkural()
        self.assertTrue( kk )
        self.assertTrue( u"ஆதி"  in kk.db[0].ta)
        self.assertTrue(u"பகவன்" in kk.db[0].ta)

if __name__ == '__main__':
    unittest.main()
