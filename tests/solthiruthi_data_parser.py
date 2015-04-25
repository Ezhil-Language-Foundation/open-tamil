# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

# setup the paths
from opentamiltests import *
from solthiruthi.data_parser import *

class DataParserTest(unittest.TestCase):
    def test_worlists(self):
        obj = DataParser.run(["data/maligaiporul.txt",\
                              "data/vilangugal.txt"])
        r = obj.analysis()
        self.assertEqual(r['catlen'],5)
        self.assertEqual(r['total'],141)
        self.assertEqual(sorted(r['dict'].values()),sorted([62,28,31,17,3]))

if __name__ == "__main__":
    unittest.main()
