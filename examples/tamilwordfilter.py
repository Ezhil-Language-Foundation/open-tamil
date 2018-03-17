#!python
# -*- coding: utf-8 -*-
# (C) 2013-2018 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 
from __future__ import print_function
import sys
import codecs
from tamil.utf8 import print_tamil_words
from transliterate import *
import operator

if __name__ == u"__main__":
    if len(sys.argv) < 2:
        print(u"Usage: tamilwordfilter.py <filename-1> <filename-2> ... \n")
    for filename in sys.argv[1:]:
        with codecs.open(filename,"r","UTF-8") as fp:
            print_tamil_words( fp.read() )
