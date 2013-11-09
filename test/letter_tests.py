# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

import tamil.utf8 as utf8

class Letters(unittest.TestCase):
    def test_uyirmei(self):     
        print utf8.uyirmei(2) 
        assert( utf8.uyirmei(2)  == "கி" )
    
if __name__ == '__main__':    
    test_support.run_unittest(Letters)

