#!python
# -*- coding: utf-8 -*-
# (C) 2013-2019 Muthiah Annamalai
#
# This file is part of 'open-tamil' package tests
#

import sys
import imp

try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3

imp.reload(sys)
# sys.setdefaultencoding('utf-8')

import codecs
from tamil.utf8 import print_tamil_words
from transliterate import *
import operator

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tamilwordfilter.py <filename-1> <filename-2> ... \n")
    for filename in sys.argv[1:]:
        with codecs.open(filename, "r", "UTF-8") as fp:
            for line in fp:  # SO:6475328 - read file line by line
                print_tamil_words(line)
