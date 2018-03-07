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

if PYTHON3:
    class long(int):
        pass

class NumeralStringLimitTests(unittest.TestCase):
    def test_case_basic(self):
        self.assertEqual(u"புள்ளி மூன்று மூன்று",tamil.numeral.num2tamilstr('0.33'))
        self.assertEqual(u"புள்ளி ஒன்பது எட்டு ஏழு ஆறு",tamil.numeral.num2tamilstr('0.9876'))
        
    def test_case_american(self):
        self.assertEqual(u"புள்ளி மூன்று மூன்று",tamil.numeral.num2tamilstr_american('0.33'))
        self.assertEqual(u"புள்ளி ஒன்பது எட்டு ஏழு ஆறு",tamil.numeral.num2tamilstr_american('0.9876'))
            
class NumeralTestAmerican(unittest.TestCase):
    def runTest(self,var,nos):
        for numerStr,num in zip(var,nos):
            print('Testing ---> ',num)
            self.assertEqual( numerStr, tamil.numeral.num2tamilstr_american( num ), num )
        return

    def test_friend_of_rama( self ):
        ramanujan = 1729
        gometra = tamil.numeral.num2tamilstr( ramanujan )
        expected = u"ஓர் ஆயிரத்தி எழுநூற்று இருபத்தி ஒன்பது"
        self.assertEqual( gometra, expected )
    
    def test_units( self ):
        units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
        self.runTest( units, range(0,11) )
        return        

    def test_basic_pulli(self):
        numerals = (u'புள்ளி ஐந்து', u'ஒன்று புள்ளி ஐந்து', u'இரண்டு புள்ளி ஐந்து', u'மூன்று புள்ளி ஐந்து', u'நான்கு புள்ளி ஐந்து', u'ஐந்து புள்ளி ஐந்து', u'ஆறு புள்ளி ஐந்து', u'ஏழு புள்ளி ஐந்து', u'எட்டு புள்ளி ஐந்து', u'ஒன்பது புள்ளி ஐந்து', u'பத்து புள்ளி ஐந்து')
        numbers = [i+0.5 for i in range(0,11)]
        self.runTest( numerals, numbers )
        return
    
    def test_teens( self ):
        teens = (u'பதினொன்று', u' பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து',u'பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19    
        self.runTest( teens, range(11,20) )
        return
        
    def test_tens ( self ):
        tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது',u'அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
        self.runTest( tens, range(10,100,10) )
        return
        
    def test_100s( self ):
        hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு',u'ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 - 900
        self.runTest( hundreds, range(100,1000,100) )
        return
        
    def test_max( self ):
        maxno = long(1e15 - 1)
        expected = u'தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது டிரில்லியன் தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது பில்லியன் தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது மில்லியன் தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது'
        self.assertEqual( tamil.numeral.num2tamilstr_american( maxno ), expected )
        return
    
    def test_numerals(self):
        var = {0:u"பூஜ்ஜியம்",
        long(1e7):u"பத்து மில்லியன்",
        long(1e9-1):u"தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது மில்லியன் தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது",
        3060:u"மூன்று ஆயிரத்தி அறுபது",
        1:u"ஒன்று",
        2:u"இரண்டு",
        3:u"மூன்று",
        5:u"ஐந்து",
        10:u"பத்து",
        11:u"பதினொன்று",
        17:u"பதினேழு",
        19:u"பத்தொன்பது",
        20:u"இருபது",
        21:u"இருபத்தி ஒன்று",
        1051:u"ஓர் ஆயிரத்தி ஐம்பத்தி ஒன்று",
        100000:u"நூறு ஆயிரம்",
        100001:u"நூறு ஆயிரத்தி ஒன்று",
        10011:u"பத்து ஆயிரத்தி பதினொன்று",
        49:u"நாற்பத்தி ஒன்பது",
        50:u"ஐம்பது",
        55:u"ஐம்பத்தி ஐந்து",
        1000001:u"ஒரு மில்லியன் ஒன்று",
        90:u"தொன்னூறு",
        99:u"தொன்னூற்றி ஒன்பது",
        100:u"நூறு",
        101:u"நூற்றி ஒன்று",
        1000:u"ஓர் ஆயிரம்",
        111:u"நூற்றி பதினொன்று",
        1000000000000:u"ஒரு டிரில்லியன்",
        1011:u"ஓர் ஆயிரத்தி பதினொன்று"}
        
        for k,actual_v in var.items():
            v = tamil.numeral.num2tamilstr_american(k)
            print('verifying => # %d'%k)
            self.assertEqual(v,actual_v,k)
        return

class NumeralTest(unittest.TestCase):
    def runTest(self,var,nos):
        for numerStr,num in zip(var,nos):
            print('Testing ---> ',num)
            self.assertEqual( numerStr, tamil.numeral.num2tamilstr( num ), num )
        return

    def test_units( self ):
        units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
        self.runTest( units, range(0,11) )
        return
        
    def test_teens( self ):
        teens = (u'பதினொன்று', u' பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து',u'பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19    
        self.runTest( teens, range(11,20) )
        return
        
    def test_tens ( self ):
        tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது',u'அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
        self.runTest( tens, range(10,100,10) )
        return
        
    def test_100s( self ):
        hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு',u'ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 - 900
        self.runTest( hundreds, range(100,1000,100) )
        return
        
    def test_max( self ):
        maxno = long(1e12 - 1 )
        expected = u'தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது கோடியே தொன்னூற்றி ஒன்பது இலட்சத்தி தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது'
        self.assertEqual( tamil.numeral.num2tamilstr( maxno ), expected )
        return
    
    def test_numerals(self):
        var = {0:u"பூஜ்ஜியம்",
        3060:u"மூன்று ஆயிரத்தி அறுபது",
        1:u"ஒன்று",
        2:u"இரண்டு",
        3:u"மூன்று",
        5:u"ஐந்து",
        10:u"பத்து",
        11:u"பதினொன்று",
        17:u"பதினேழு",
        19:u"பத்தொன்பது",
        20:u"இருபது",
        21:u"இருபத்தி ஒன்று",
        1051:u"ஓர் ஆயிரத்தி ஐம்பத்தி ஒன்று",
        100000:u"ஒரு இலட்சம்",
        100001:u"ஒரு இலட்சத்தி ஒன்று",
        10011:u"பத்து ஆயிரத்தி பதினொன்று",
        49:u"நாற்பத்தி ஒன்பது",
        50:u"ஐம்பது",
        55:u"ஐம்பத்தி ஐந்து",
        1000001:u"பத்து இலட்சத்தி ஒன்று",
        90:u"தொன்னூறு",
        99:u"தொன்னூற்றி ஒன்பது",
        100:u"நூறு",
        101:u"நூற்றி ஒன்று",
        1000:u"ஓர் ஆயிரம்",
        111:u"நூற்றி பதினொன்று",
        1000000000000:u"ஒரு இலட்சம் கோடி",
        1011:u"ஓர் ஆயிரத்தி பதினொன்று"}
        
        for k,actual_v in var.items():
            v = tamil.numeral.num2tamilstr(k)
            print('verifying => # %d'%k)
            self.assertEqual(v,actual_v,k)
        return

class NumeralNegTest(unittest.TestCase):
    def runTest(self,var,nos):
        for numerStr,num in zip(var,nos):
            print('Testing ---> ',num)
            self.assertEqual( numerStr, tamil.numeral.num2tamilstr( num ), num )
        return
    
    def test_100s( self ):
        hundreds = ( u'- நூறு', u'- இருநூறு', u'- முன்னூறு', u'- நாநூறு',u'- ஐநூறு', u'- அறுநூறு', u'- எழுநூறு', u'- எண்ணூறு', u'- தொள்ளாயிரம்') #100 - 900
        self.runTest( hundreds, range(-100,-1000,-100) )
        return

    def test_USA(self):
        ramanujan = -1729
        gometra = tamil.numeral.num2tamilstr( ramanujan )
        expected = u"- ஓர் ஆயிரத்தி எழுநூற்று இருபத்தி ஒன்பது"
        self.assertEqual( gometra, expected )
    
    def test_3LKPLUS1(self):
        x1 = 3e5 + 1
        actual = tamil.numeral.num2tamilstr( x1 )
        expected = u'மூன்று இலட்சத்தி ஒன்று'
        self.assertEqual( actual, expected )
    
    def test_PI(self):
        if PYTHON3:
            print("Python3 has different rounding")
            return
            
        pie = 3.1415
        expected = u'மூன்று புள்ளி ஒன்று நான்கு ஒன்று ஐந்து'
        actual = tamil.numeral.num2tamilstr(pie)
        actual_USA = tamil.numeral.num2tamilstr_american(pie)
        self.assertEqual(actual,expected)
        self.assertEqual(actual_USA,expected)
    
    def test_PI_million(self):
        pie = 3e6 + 0.1415
        expected = u'மூன்று மில்லியன் புள்ளி ஒன்று நான்கு ஒன்று'
        actual_USA = tamil.numeral.num2tamilstr_american(pie)
        self.assertEqual(actual_USA[0:len(expected)],expected)
    
    def test_PI_lakshalu(self):
        pie = 3e5+0.1415
        expected = u'மூன்று இலட்சம் புள்ளி ஒன்று நான்கு ஒன்று ஐந்து'
        actual_IN = tamil.numeral.num2tamilstr(pie)
        self.assertEqual(actual_IN[0:len(expected)],expected)
    
    #@unittest.skipIf( PYTHON3, "Python3 has different rounding")
    def test_INFRAC(self):
        if PYTHON3:
            print("Python3 has different rounding")
            return
        exp2 = u'ஓர் ஆயிரத்தி ஒன்று புள்ளி நான்கு ஐந்து'
        actual_IN2 = tamil.numeral.num2tamilstr(1001+0.45)
        self.assertEqual(actual_IN2,exp2)
        exp2 = u'ஓர் ஆயிரம் புள்ளி நான்கு ஐந்து'
        actual_IN2 = tamil.numeral.num2tamilstr(1000+0.45)
        self.assertEqual(actual_IN2,exp2)
        
    def test_VITHIVILAKKU(self):
        if PYTHON2_6:
            # exception API is different in Python 2.6
            return
        with self.assertRaises(Exception):
            tamil.numeral.num2tamilstr( complex(5,6) )
        with self.assertRaises(Exception):
            tamil.numeral.num2tamilstr( 'mannagatti' )

    
if __name__ == '__main__':        
    unittest.main()
