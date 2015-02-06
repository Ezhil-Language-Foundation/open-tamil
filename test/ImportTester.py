# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
#  
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

class ImportTester(unittest.TestCase):
    def test_import_tester(self):
        import tamil; import ngram; import transliterate

if __name__ == '__main__':    
    unittest.main()
