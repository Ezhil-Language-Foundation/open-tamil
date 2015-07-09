# (C) 2013 Muthiah Annamalai
# 
# This file is part of Ezhil Language project
# 
# path manipulation magic sets up the current development verison of ezhil
# as the library from the "ezhil-lang/tests/unit" path.

import sys, os

open_tamil_path = (os.sep).join(os.getcwd().split(os.sep)[:-1])
print(open_tamil_path) # library
sys.path.insert(0,open_tamil_path)

PYTHON2_7 = (sys.version[0:3] == '2.7')
PYTHON2_6 = (sys.version[0:3] == '2.6')
PYTHON3 = sys.version > '3'
WINDOWS = (sys.platform.find('win') != -1)
LINUX = not WINDOWS

import tamil

import transliterate

import ngram

import unittest

import solthiruthi

# 2-3 straddle
try:
    from test import test_support
except ImportError as ex:
    from test import support as test_support
