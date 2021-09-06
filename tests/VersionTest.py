# -*- coding: utf-8 -*-
# (C) 2015-2018,2020 Muthiah Annamalai
#
# This file is part of 'open-tamil' package tests
#

import tamil
# setup the paths
from opentamiltests import *


class VersionTester(unittest.TestCase):
    def test_version(self):
        self.assertEqual(tamil.VERSION, "1.1")


if __name__ == "__main__":
    unittest.main()
