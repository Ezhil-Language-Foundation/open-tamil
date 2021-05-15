# -*- coding: utf-8 -*-
# This file is part of Open-Tamil package unittests
# (C) 2021 Muthu Annamalai

# setup the paths
from opentamiltests import *
import unittest
from tamil.quantum import get_superposition_representation

class QuantumTests(unittest.TestCase):
    def test_alternates(self):
        alternates = get_superposition_representation('தமிழ்')
        print(alternates)
        self.assertEqual(len(alternates),8)
        self.assertEqual(alternates,['த்ம்ழ்', 'த்ம்', 'திழ்', 'தி', 'மழ்', 'ம', 'அழி', 'அஇ'])

if __name__ == "__main__":
    unittest.main()
