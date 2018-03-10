# -*- coding: utf-8 -*-
# (C) 2017 Muthiah Annamalai
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

class Letters(unittest.TestCase):
    def test_issue132(self):
        x=u"வரு'க"
        y=tamil.utf8.get_letters(x)
        y_eq = [u'\u0bb5', u'\u0bb0\u0bc1', u"'", u'\u0b95']
        self.assertEqual(y,y_eq)
        for a in [u"ரிஷ’",u"ரஸ“மா" , u"ரஹ“மான்"]:
            b=tamil.utf8.get_letters(a)
            b_eq = []
            #self.assertEqual(b,b_eq)
        

    def test_digit_letters(self):
        from operator import itemgetter
        first = itemgetter(0)
        numbers = list(map(first,tamil.utf8.tamil_digits))
        self.assertEqual(sum(numbers), 1155)
        self.assertTrue( numbers,[0,1,2,3,4,5,6,7,8,9,10,100,1000])        
    def test_uyir_mei_split(self):
        ak = utf8.splitMeiUyir(u"ஃ")
        self.assertEqual(ak,u"ஃ")
        il = utf8.splitMeiUyir(u"ல்")
        self.assertEqual(il,u"ல்")
        il,ee = utf8.splitMeiUyir(u"லி")
        self.assertEqual((il,ee),(u"ல்",u"இ"))

    def test_classifier(self):
        expected = []
        expected.extend(['english']*3)
        expected.extend(['digit']*4)
        expected.extend(['kuril','nedil','uyirmei','vallinam','uyirmei'])
        data = list(map(utf8.classify_letter,utf8.get_letters(u"abc1230அஆரெட்டை")))
        self.assertEqual(data,expected)

    def demo(self):
        for l in utf8.get_letters_iterable(u"இதுதாண்டாபோலிசு"):
            print("%s - %s"%(l,utf8.classify_letter(l)))
        
    def test_classified_except(self):
        with self.assertRaises(ValueError) as ve:
            utf8.classify_letter(u'.')

if __name__ == '__main__':
    unittest.main()
