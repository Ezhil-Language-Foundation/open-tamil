# -*- coding: utf-8 -*-
# (C) 2015-2018 Muthiah Annamalai
#  
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
import tamil

class VersionTester(unittest.TestCase):
    def test_version(self):        
        self.assertEqual(tamil.VERSION,'0.7')

if __name__ == '__main__':    
    unittest.main()

