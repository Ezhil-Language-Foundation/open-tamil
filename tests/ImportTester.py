# -*- coding: utf-8 -*-
# (C) 2015-2017 Muthiah Annamalai
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
        
if __name__ == '__main__':    
    unittest.main()
