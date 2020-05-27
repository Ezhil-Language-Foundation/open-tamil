# -*- coding: utf-8 -*-
# This file is part of Open-Tamil package unittests
# (C) 2018 Muthu Annamalai

# setup the paths
from opentamiltests import *
import unittest
from tamiltts.vasikka import *
import sys

class TTSTests(unittest.TestCase):
    def test_basename(self):
        available = [syllable+".mp3" for _,syllable in Syllable2AF.AudioMap.items()]
        available.extend([f+'.mp3' for f in Syllable2AF.numeral_digits] )
        files = os.listdir( ConcatennativeTTS.TARGETDIR )
        for f in files:
            f2 = os.path.basename(f)
            if f2.startswith('.git'): continue
            if not ( f2 in available):
                raise Exception("File %s is not in syllable list"%f2)
        return

    def test_run(self):
        data = u" ".join( [letter for letter,_ in Syllable2AF.AudioMap.items()] )
        tts = ConcatennativeTTS(data,"alphabets.mp3")
        #tts.run()

    def test_ctor(self):
        testcase = {}
        a,b = u"தமிழை  விட   பழையது   மனிதனின்   பேச்சு   மொழி!","test_oldest.mp3"
        testcase[b]=a
        a,b = u"சாலா முத்து உன்னை நேசிக்கிறான்!","test_helloworld.mp3"
        testcase[b]=a
        a,b = u" ".join( str(i) for i in range(0,10) )+".","test_digits.mp3"
        testcase[b]=a
        a,b = u"1-(800) 356-9377.","test_1_800_flowers.mp3"
        testcase[b]=a
        a,b = u"வணக்கம்.",'test_vanakkam.mp3'
        testcase[b]=a
        a,b = u"எழில் உங்களை அழைக்கிறது.","test_ezhilwelcome.mp3"
        testcase[b]=a
        a,b = u" ".join(tamil.utf8.uyir_letters)+".","test_uyir.mp3"
        testcase[b]=a
        a,b = u"ரகசியம்.","test_ragasiyam.mp3"
        testcase[b]=a
        N = len(testcase)
        failed = []
        for outputfile,data in testcase.items():
            try:
                tts = ConcatennativeTTS(data,outputfile)
                #tts.run()
            except Exception as iex:
                print(str(iex))
                raise Exception(iex)
                failed.append(outputfile)
        if len(failed) == 0:
            print("OK")
        else:
            print("FAIL: %d tests failed out of %d"%( len(failed), N))
            print("\n".join(failed))
        self.assertEqual(failed,[])
        return

if __name__ == "__main__":
    unittest.main()
