#!python
# -*- coding: utf-8 -*-
# (C) 2013-2018 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

import tamil
import sys
from transliterate import *
from tamil.utf8 import print_tamil_words
try:
    import bs4 #requires beautiful soup 4
except ImportError as ie:
    # work with BS3
    try:
        import BeautifulSoup
    except ImportError as ie2:
        print("Module BeautifulSoup required for successful execution; please install module via pip.\n")
        sys.exit(-1)
    class bs4:
        BeautifulSoup = BeautifulSoup.BeautifulSoup

from urllib2 import urlopen
import operator

def url_tamil_text_filter( url ):
    tapage = bs4.BeautifulSoup(urlopen(url))
    tatext = tapage.body.text
    print_tamil_words( tatext )

if __name__ == u"__main__":
    if len(sys.argv) < 2:
        print(u"Usage: tamilurlfilter.py <url-1> <url-2> ...\n")
    for url in sys.argv[1:]:
        url_tamil_text_filter(url)
