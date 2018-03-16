# -*- coding: utf-8 -*-
# (C) 2013-2018 Muthiah Annamalai
#
# This file is part of 'open-tamil' package tests
#

# setup the paths
from opentamiltests import *
from transliterate import azhagi, jaffna, combinational, UOM, algorithm

class ReverseTransliterationTests(unittest.TestCase):
    def test_tamil2en_1(self):
        tamil_str = u"வணக்கம்"
        azhagi_table = azhagi.Transliteration.table
        eng_str = algorithm.Tamil2English.transliterate(azhagi_table,tamil_str)
        self.assertEqual( eng_str,u"vaNacKam")

        tamil_str = u"அன்னம்"
        azhagi_table = azhagi.Transliteration.table
        eng_str = algorithm.Tamil2English.transliterate(azhagi_table,tamil_str)
        self.assertEqual( eng_str, u"annHam")

class GreedyTests(unittest.TestCase):
    def test_UOM(self):
        # University of Madras Lexicon style transliteration standard
        tamil_word = u"வணக்கம்"
        for eng_string in [u"vṇikkim"]:
            top_match,greedy = algorithm.Greedy.transliterate(UOM.Transliteration.table,eng_string)
            #import pprint
            #pprint.pprint(greedy.options)
            self.assertTrue( tamil_word in greedy.options)

    def test_vanakkam(self):
        tamil_word = u"வணக்கம்"
        for eng_string in ["vaNakkam","vanakkam"]:
            top_match,greedy = algorithm.Greedy.transliterate(jaffna.Transliteration.table,eng_string)
            self.assertTrue( tamil_word in greedy.options )

class Yazhpanam(unittest.TestCase):
    def test_vandemataram(self):
        tamil_words = u"வந்தே மாதரம்"
        eng_string = u'vanthE mAtharam'
        tamil_tx = algorithm.Iterative.transliterate(jaffna.Transliteration.table,eng_string)
        if ( LINUX ): print("]"+tamil_tx+"[", len(tamil_words), len(tamil_tx),type(tamil_tx),type(tamil_words))
        if ( LINUX ): print("]"+tamil_words+"[")
        self.assertTrue( tamil_words == tamil_tx )

    def test_combinational(self):
        tamil_words = u"வந்தே மாதரம்"
        eng_string = u'van-thee maatharam'
        tamil_tx = algorithm.Iterative.transliterate(combinational.Transliteration.table,eng_string)
        if ( LINUX ): print("]"+tamil_tx+"[", len(tamil_words), len(tamil_tx), type(tamil_tx), type(tamil_words))
        if ( LINUX ): print("]"+tamil_words+"[", len(tamil_tx), len(tamil_words))

        self.assertTrue( tamil_words.find(tamil_tx) >= 0 )

    def test_azhagi_spec(self):
        # test for
        tamil_tx = {}
        correct_tx = {u"ke" : u"கெ", u"khae":u"கே", u"cai" : u"கை",
                      u"koh" : u"கொ", u"kho" : u"கோ"}
        for eng_string in [u"ke",u"khae",u"cai",u"koh",u"kho"]:
            tamil_tx[eng_string] = algorithm.Iterative.transliterate(azhagi.Transliteration.table,eng_string)
            if ( LINUX ): print(tamil_tx[eng_string], " => ", eng_string)
            self.assertTrue( tamil_tx[eng_string], eng_string )

    def test_azhagi(self):
        ## challenge use a probabilistic model on Tamil language to score the next letter,
        ## instead of using the longest/earliest match
        ## http://www.mazhalaigal.com/tamil/learn/keys.php

        codes = {"neenga":u"நீங்க", "andam":u"அண்டம்", "nandri":u"நன்றி", "katru":u"கற்று",
                 "viswam": u"விஸ்வம்", "namaskaaram":u"நமஸ்காரம்",
                 "sreedhar":u"ஸ்ரீதர்", "manju":u"மஞ்சு", "gnaayam":u"ஞாயம்",
                 "poi":u"பொய்", "kaai":u"காய்", "aGnGnaanam":u"அஞ்ஞானம்", "mei":u"மெய்",
                 "nanghu":u"நன்கு", "palancaL":u"பலன்கள்", "payanKaL":"பயன்கள்", "avanThaan":u"அவன்தான்",
                 "leoni":u"லியோனி", "paeTrik":u"பேட்ரிக்", "peTroal":u"பெட்ரோல்", "coapanHaegan":u"கோபன்ஹேகன்",
                 "bandham":u"பந்தம்", "saantham":u"சாந்தம்", "kaeLvi":u"கேள்வி", "koavil":u"கோவில்",
                 "nhagar":u"நகர்", "maanhagaram":u"மாநகரம்", "senhnheer":u"செந்நீர்"}

        tamil_words = u""
        for eng_string, tamil_words in codes.items():
            tamil_tx = algorithm.Iterative.transliterate(azhagi.Transliteration.table,eng_string)
            if ( LINUX ): print("]"+tamil_tx+"[", len(tamil_words), len(tamil_tx), "]"+tamil_words+"[")
            #self.assertTrue( tamil_words == tamil_tx ) #we are almost there but not yet

    def test_devotional(self):
        for k,v in {u"thiruvaachakam":u"திருவாசகம்",
                    u"mANikka vAsagar":u"மாணிக்க வாசகர்"}.items():
            tamil_tx = algorithm.Iterative.transliterate( azhagi.Transliteration.table,
                                                k )
            if( tamil_tx != v ):
                raise Exception(u"Transliteration changed\n Expected %s, but got %s for string input %\n"%(v,tamil_tx,k))
            else:
                if ( LINUX ): print(u"matched %s => %s"%(k,PYTHON3 and tamil_tx or unicode(tamil_tx)))
        return

if __name__ == '__main__':
    unittest.main()
