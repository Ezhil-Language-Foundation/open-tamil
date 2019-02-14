# -*- coding: utf-8 -*-
# (C) 2019 Muthiah Annamalai

from opentamiltests import *
import unittest
from solthiruthi.tamil99kbd import inv_confusion_matrix as kbd_cm
from solthiruthi.qwertykbd import confusion_matrix as en_kbd_cm
from solthiruthi.typographical import generate_candidates, oridam_generate_patterns

class SolthiruthiTypographical(unittest.TestCase):
    @staticmethod
    def checkpat(word_in,check_words,ed):
        pat = oridam_generate_patterns(word_in,en_kbd_cm,ed)
        pat = [u"".join(p) for p in pat]
        #print "Total = %d"%(len(pat))
        #print "Total set = %d"%len( set(pat) )
        return (len(pat),len(set(pat)))
    
    def test_edit_distance_one(self):
        n,_ = SolthiruthiTypographical.checkpat(list('shat'),['what','shag'],1)
        self.assertEqual(n,21)

    def test_edit_distance_two(self):
        n,_ = SolthiruthiTypographical.checkpat(list('arg'),['art','arg'],2)
        self.assertEqual(n,117)

if __name__ == "__main__":
    unittest.main()
