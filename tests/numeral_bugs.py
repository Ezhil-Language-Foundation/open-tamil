# -*- coding: utf-8 -*-
# (C) 2013-2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
import tamil.utf8 as utf8 
from tamil.tscii import TSCII
import codecs
import random
import os

class NumeralStressTest(unittest.TestCase):
    def setUp(self):
        random.seed(os.urandom(5))
    
    def test_rnd(self):
        for kitr in range(0,1000):
            k = random.randint(0,1e6)
            fns = []
            print('verifying => no %g '%k)
            v = tamil.numeral.num2tamilstr(k,fns)
            #print('int/file -> /  @ %g -> %s'%(k,u"-".join(fns)))
            
        return

    def test_float_rnd(self):
        for kitr in range(0,1000):
            k = float(random.randint(0,1e6))/5.55
            fns = []
            print('float/verifying => no %10g '%k)
            v = tamil.numeral.num2tamilstr(k,fns)
            #print('float/file -> %g ->  @ %s'%(k,u"-".join(fns)))            
        return
        
class NumeralBugsTest(unittest.TestCase):
    def runTest(self,var,nos):
        for numerStr,num in zip(var,nos):
            print('Testing ---> ',num)
            self.assertEqual( numerStr, tamil.numeral.num2tamilstr( num ), num )
        return
    
    def test_numerals(self):
        var = {0.5:u"புள்ளி ஐந்து", #பூஜ்ஜியம்
        3060.5:u"மூன்று ஆயிரத்தி அறுபது புள்ளி ஐந்து",
        1.5:u"ஒன்று புள்ளி ஐந்து",
        2.5:u"இரண்டு புள்ளி ஐந்து",
        3.5:u"மூன்று புள்ளி ஐந்து",
        5.5:u"ஐந்து புள்ளி ஐந்து",
        10.5:u"பத்து புள்ளி ஐந்து",
        11.5:u"பதினொன்று புள்ளி ஐந்து",
        17.5:u"பதினேழு புள்ளி ஐந்து",
        19.5:u"பத்தொன்பது புள்ளி ஐந்து",
        20.5:u"இருபது புள்ளி ஐந்து",
        21.5:u"இருபத்தி ஒன்று புள்ளி ஐந்து",
        1051.5:u"ஓர் ஆயிரத்தி ஐம்பத்தி ஒன்று புள்ளி ஐந்து",
        100000.5:u"ஒரு இலட்சம் புள்ளி ஐந்து",
        100001.5:u"ஒரு இலட்சத்தி ஒன்று புள்ளி ஐந்து",
        10011.5:u"பத்து ஆயிரத்தி பதினொன்று புள்ளி ஐந்து",
        49.5:u"நாற்பத்தி ஒன்பது புள்ளி ஐந்து",
        50.5:u"ஐம்பது புள்ளி ஐந்து",
        55.5:u"ஐம்பத்தி ஐந்து புள்ளி ஐந்து",
        1000001.5:u"பத்து இலட்சத்தி ஒன்று புள்ளி ஐந்து",
        90.5:u"தொன்னூறு புள்ளி ஐந்து",
        99.5:u"தொன்னூற்றி ஒன்பது புள்ளி ஐந்து",
        100.5:u"நூறு புள்ளி ஐந்து",
        101.5:u"நூற்றி ஒன்று புள்ளி ஐந்து",
        1000.5:u"ஓர் ஆயிரம் புள்ளி ஐந்து",
        111.5:u"நூற்றி பதினொன்று புள்ளி ஐந்து",
        100000.5:u"ஒரு இலட்சம் புள்ளி ஐந்து",
        1011.5:u"ஓர் ஆயிரத்தி பதினொன்று புள்ளி ஐந்து"}
        
        for k,actual_v in var.items():
            fns = []
            v = tamil.numeral.num2tamilstr(k,fns)
            print('verifying => # %g /  @ %s'%(k,u"-".join(fns)))
            self.assertEqual(v,actual_v,k)
        return
            
    def test_float_USA(self):
        # used to convert with actual numeral + suffix "பூஜ்ஜியம்"
        aspen = int('1234')
        swayambu_int = tamil.numeral.num2tamilstr( aspen )
        expected = u"ஓர் ஆயிரத்தி இருநூற்றி முப்பத்தி நான்கு"
        self.assertEqual( swayambu_int, expected )

        # used to convert with actual numeral + suffix "பூஜ்ஜியம்"
        aspen_float = float('1234')
        swayambu = tamil.numeral.num2tamilstr( aspen_float )
        expected = u"ஓர் ஆயிரத்தி இருநூற்றி முப்பத்தி நான்கு"
        self.assertEqual( swayambu, swayambu_int )
    
if __name__ == '__main__':        
    unittest.main()
