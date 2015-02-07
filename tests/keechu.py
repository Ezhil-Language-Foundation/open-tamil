# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
#  
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
# example keechu
from tamil.utf8 import get_letters

class Keechu(unittest.TestCase):
    def test_words_to_letters(self):
        k1 = u"இந்தக் குளிர்ல டெய்லி தலைக்கு குளிக்கற நல்லவங்க இருக்கறதாலதான் கோவை இப்படி சூப்பரா இருக்காம்"
        word_length = [4,4,3,4,5,6,9,2,4,4,5]
        for idx,kk in enumerate(k1.split(' ')):
            idx_len = len( get_letters(kk) )
            print('w# ',idx, idx_len )
            self.assertEqual( word_length[idx], idx_len)


if __name__ == '__main__':
    unittest.main()
