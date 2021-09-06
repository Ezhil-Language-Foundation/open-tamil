# -*- coding: utf-8 -*-
# This file is part of Open-Tamil package unittests
# (C) 2021 Muthu Annamalai

import unittest

# setup the paths
from opentamiltests import *
from tamil.quantum import get_superposition_representation


class QuantumTests(unittest.TestCase):
    def test_alternates_1(self):
        alternates = get_superposition_representation('தமிழ்')
        self.assertEqual(len(alternates),8)
        self.assertEqual(alternates,['த்ம்ழ்', 'த்ம்', 'திழ்', 'தி', 'மழ்', 'ம', 'அழி', 'அஇ'])

    def test_alternates_2(self):
        alternates = get_superposition_representation('கரோனா')
        self.assertEqual(len(alternates),8)

    def test_alternates_3(self):
        alternates = get_superposition_representation('தடுப்பூசி',raw=True)
        self.assertEqual(len(alternates),32)

if __name__ == "__main__":
    unittest.main()
