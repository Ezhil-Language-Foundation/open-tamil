# -*- coding: utf-8 -*-
# (C) 2016-17 Muthiah Annamalai

from opentamiltests import *
import os
import codecs
from pprint import pprint
from spell import Speller, LoadDictionary, OttruSplit, Mayangoli
from tamil import utf8

TA_SPELLER = Speller(lang=u"TA",mode="web")

class SpellTestFiles(unittest.TestCase):
    def setUp(self):
        self.speller = TA_SPELLER

    def test_file10(self):
        nwords = 31
        npass = 13
        nfail = 18
        fail_n_suggs = dict()
        obj = {'total':nwords,
        'correct_words':npass,
        'wrong_words':nfail,
        'word_suggestions':fail_n_suggs}
        filename = "data/doc10.spell"
        self._tester(filename,obj)

    def test_file1(self):
        nwords = 32
        npass = 18
        nfail = 14
        fail_n_suggs = dict()
        obj = {'total':nwords,
        'correct_words':npass,
        'wrong_words':nfail,
        'word_suggestions':fail_n_suggs}
        filename = "data/doc1.spell"
        self._tester(filename,obj)

    def test_rest(self):
        for f in [2,3,4,5,6,7,8,9,11,12]:
            self._test_simple("data/doc%d.spell"%f)

    def _test_simple(self,filename):
        with codecs.open(filename,"r","utf-8") as fp:
            data = self.speller.noninteractive_spellcheck(fp.read())
        self.assertTrue( data['total'] > 0 )
        self.assertTrue( data['wrong_words'] > 0 )
        self.assertTrue( data['correct_words'] > 0 )

    def _tester(self,filename,ref_obj):
        with codecs.open(filename,"r","utf-8") as fp:
            data = self.speller.noninteractive_spellcheck(fp.read())
        self.assertEqual(data['total'],ref_obj['total'])
        self.assertEqual(data['wrong_words'],ref_obj['wrong_words'])
        self.assertEqual(data['correct_words'],ref_obj['correct_words'])

class SpellTestTamil(unittest.TestCase):
    def setUp(self):
        self.speller =  TA_SPELLER

    def test_tamil_mode(self):
        self.assertTrue(self.speller.in_tamil_mode())

    def test_drop_letter(self):
        word,alt = u"இருபட்து",u"இருபது"
        not_ok,sugg = self.speller.check_word_and_suggest(word)
        self.assertFalse(not_ok)
        self.assertTrue(alt in sugg)

    def test_comma_numbers(self):
        alt = u"பத்து ஆயிரம்"
        not_ok,sugg = self.speller.check_word_and_suggest(u"10,000")
        self.assertFalse(not_ok)
        self.assertTrue(alt in sugg)

    def test_iyalbu_punarchi(self):
        for w in [ u"பொன்மலை", u"பொன்மாலை", u"மாமரம்"]:
            ok,alt = self.speller.check_word_and_suggest(w)
            self.assertTrue(ok)

    def test_words_split(self):
        for w in [u"உள்ளமது",u"அச்சமின்றி",u"கணிதமழகு",u"காலமானாலும்"]:#u"செயல்படு"]:
            ok,alt = self.speller.check_word_and_suggest(w)
            self.assertTrue(ok)

    def test_words_with_numeral(self):
        data = [("900",u"தொள்ளாயிரம்"),("1000001.5",u"பத்து இலட்சத்தி ஒன்று புள்ளி ஐந்து"),("-10.5",u"கழித்தல் பத்து புள்ளி ஐந்து")]
        for w,sugg in data:
            not_ok,suggs = self.speller.check_word_and_suggest(w)
            self.assertFalse(not_ok)
            self.assertTrue(sugg in suggs)


    # # 1024 512 256 எல்லாமே இரண்டின் பெருக்குகள்
    def test_numeral_input(self):
        data = [("900",u"தொள்ளாயிரம்"),("1000001.5",u"பத்து இலட்சத்தி ஒன்று புள்ளி ஐந்து"),("-10.5",u"கழித்தல் பத்து புள்ளி ஐந்து")]
        for _,words in data:
            for word in words.split(u" "):
                ok,suggs = self.speller.check_word_and_suggest(word)
                self.assertTrue(ok)

    def test_words_with_hyphen(self):
        not_ok,suggs = self.speller.check_word_and_suggest(u"வெத்து-வேட்டு")
        self.assertFalse(not_ok)
        self.assertTrue(u"வெத்து வேட்டு" in suggs)

    def test_words_with_dates(self):
        # test if all the words are in the dictionary
        for w in [u"1989-ஆம்;",u"தரம்",u"1497-இல்"]:
            ok,_ = self.speller.check_word_and_suggest(w)
            self.assertTrue( ok, w )
        return

    def test_words_with_punctuation(self):
        # test if all the words are in the dictionary
        for w in [u"சவால்!",u"மகதம்;",u"ஆரதம்,"]:#, u"பல்லவன் ;",u"பாதம்:",u"கவணம்/", u"செயல்_"]:
            ok,_ = self.speller.check_word_and_suggest(w)
            self.assertTrue( ok, w )
        return

    def test_words_in_dictionary(self):
        # test if all the words are in the dictionary
        for w in [u"சவால்",u"மகதம்",u"ஆரதம்", u"பல்லவன்",u"பாதம்",u"கவணம்", u"செயல்"]:
            ok,_ = self.speller.check_word_and_suggest(w)
            self.assertTrue( ok, w )
        return

    def test_words_in_error(self):
        # test if the words in error are flagged
        # further test if suggestion contains the right word
        debug = False
        words_and_fixes = { u"எந்திர" : u"எந்திரம்",
                            u"செயல்பட":u"செயல்"}
        for w,right_word in words_and_fixes.items():
            notok,suggs = self.speller.check_word_and_suggest( w )
            if ( debug ):
                pprint(notok)
                pprint(suggs)
            self.assertFalse( notok, w )
            self.assertTrue( right_word in suggs, u"%s -> (%s)"%(right_word,u", ".join(suggs) ))
        return

    def test_ottru_split(self):
        expect = [[u"ய்",u"ஆரிகழ்ந்து"], [u"யார்",u"இகழ்ந்து"] , [u"யாரிக்",u"அழ்ந்து"], [u"யாரிகழ்ந்த்",u"உ"]]
        word = u"யாரிகழ்ந்து"
        ottru = OttruSplit(word,tamil.utf8.get_letters(word))
        ottru.generate_splits()
        self.assertEqual(ottru.results,expect)

    def test_mayangoli_suggests_simple(self):
        alt = Mayangoli.run(u"பளம்",[u"ப",u"ள",u"ம்"])
        expect = [u"பளம்",u"பழம்",u"பலம்"]
        alt = sorted(alt)
        expect = sorted(expect)
        self.assertEqual(len(alt),len(expect))
        self.assertEqual(alt,expect)

    def test_mayangoli_suggests_notsimple(self):
        expect_l = [3,3,3*3*2*3]
        for idx,w in enumerate([u"கண்ணன்",u"அப்பளம்",u"எழுத்தாளருமான"]):
            alt = Mayangoli.run(w,tamil.utf8.get_letters(w))
            self.assertEqual(len(alt),expect_l[idx])

    def test_mayangoli_suggests_none(self):
        expect_l = 0
        w = u"குதிகால்"
        alt = Mayangoli.run(w,tamil.utf8.get_letters(w))
        self.assertEqual(len(alt),expect_l)

class SpellBadIMETest(unittest.TestCase):
    def setUp(self):
        self.speller = TA_SPELLER

    def test_invalid_word_det(self):
        not_a_word = u"ஆாள்"
        self.assertFalse( self.speller.check_word_and_suggest(not_a_word)[0] )

    def test_invalid_word3(self):
        not_a_word = u"தூூக்"
        self.assertFalse( self.speller.check_word_and_suggest(not_a_word)[0] )
        not_a_word = u"ஏூூளா"
        self.assertFalse( self.speller.check_word_and_suggest(not_a_word)[0] )

    def test_valid_word_det(self):
        for word in [u"ஆள்",u"ஏனை",u"எந்திரம்",u"செயல்"]:
            self.assertTrue( self.speller.check_word_and_suggest(word)[0] )
        return

    @unittest.skip("ignore")
    def test_all_valid(self):
        data,DEBUG = [],False
        with codecs.open("data/project_madurai_utf8.txt","r","utf-8") as f:
            data = filter(lambda x: len(x)>2, f.readlines())
        obj = BadIME()
        for idx,line in enumerate(data):
            for col,word in enumerate( re.split(u'\s+',line) ):
                if DEBUG:
                    print(idx,col)
                    print(utf8.get_letters(word))
                self.assertEqual(obj.apply(word),(True,None))
            pass
        pass

    def test_invalid_pulli_seq(self):
        not_a_word = u"ஆள்்ஆ"
        class List:
            def __init__(self):
                self.L = list()
            def append(self,obj):
                self.L.append(obj)
        errmsgs = List()
        self.assertFalse( self.speller.check_word_and_suggest(not_a_word,errmsgs)[0] )
        self.assertEqual(errmsgs.L,[u"TypographicalError"])

    def test_drop_letter(self):
        word,alt = u"இருபட்து",u"இருபது"
        not_ok,sugg = self.speller.check_word_and_suggest(word)
        self.assertFalse(not_ok)
        self.assertTrue(alt in sugg)

if __name__ == "__main__":
    unittest.main()
