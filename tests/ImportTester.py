# -*- coding: utf-8 -*-
# (C) 2015-2017, 2020 Muthiah Annamalai
#
# This file is part of 'open-tamil' package tests
#

# setup the paths
import time

import tamil
from kural import Kural, Thirukkural
from opentamiltests import *
from tamil.date import DateUtils


class ImportTester(unittest.TestCase):
    def test_import_tester(self):
        import tamil;
        import ngram;
        import transliterate
        self.assertTrue(True)

    def test_import_num2tamilstr(self):
        from tamil.numeral import num2tamilstr, num2tamilstr_american
        for key in ['num2tamilstr', 'num2tamilstr_american']:
            self.assertTrue(locals()[key])


class MiscTestMay2020(unittest.TestCase):
    def test_date_counts(self):
        from tamil.date import TamilLunarMonths, TamilSeasonsMonths
        self.assertEqual(len(TamilLunarMonths), 12)
        self.assertEqual(sum([d for _, d in TamilLunarMonths]), 359)
        self.assertEqual(sum([len(v) for _, v in TamilSeasonsMonths.items()]), 12)

    def test_date_fmt(self):
        self.assertTrue(DateUtils.get_time(time.localtime()))

    def test_kural(self):
        kk = Thirukkural()
        self.assertTrue(kk)
        self.assertTrue(u"ஆதி" in kk.db[0].ta)
        self.assertTrue(u"பகவன்" in kk.db[0].ta)

    def test_kural_iter(self):
        """
        நாஞ்சில் அவர்கள் எழுதியதாவது:
        https://nanjilnadan.com/2020/04/09/%e0%ae%95%e0%af%8a%e0%ae%9f%e0%af%81%e0%ae%aa%e0%af%8d%e0%ae%aa%e0%ae%be%e0%ae%b0%e0%af%8d%e0%ae%87%e0%ae%b2%e0%ae%be%e0%ae%a9%e0%af%81%e0%ae%ae%e0%af%8d/

        ̀எடுத்துக்காட்டுக்கு, புழுதி என்ற சொல் 1037வது குறளில் கையாளப்பட்டுள்ளது.
        பழம் என்ற சொல் 1120 வது குறளில் உண்டு.
        முலை என்ற சொல் 402 மற்றும் 1087 வது குறள்களில்.
        அனிச்சம் எனும் சொல் 90வது, 1111வது, 1115 வது, 1120 வது திருக் குறள்களில் உண்டு.̀
        """
        நாஞ்சில் = {'அனிச்ச': [90, 1111, 1115, 1120], 'புழுதி': [1037], 'பழம்': [1120], 'முலை': [402, 1087]}
        for சொல், இடம் in நாஞ்சில்.items():
            கண்ட_இடம் = Thirukkural.occurrence(சொல்)
            self.assertEqual(கண்ட_இடம், இடம்)


if __name__ == '__main__':
    unittest.main()
