#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) 2013-2018 Muthiah Annamalai
#
# This file is part of 'open-tamil' package tests
#

import sys
import imp
import ssl

try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3

# imp.reload(sys)
# sys.setdefaultencoding('utf-8')

import tamil
from transliterate import *
from tamil.utf8 import print_tamil_words

USE_BS4 = False
try:
    import bs4  # requires beautiful soup 4

    USE_BS4 = True
except ImportError as ie:
    # work with BS3
    try:
        import BeautifulSoup
    except ImportError as ie2:
        print(
            "Module BeautifulSoup required for successful execution; please install module via pip.\n"
        )
        sys.exit(-1)


    class bs4:
        BeautifulSoup = BeautifulSoup.BeautifulSoup

from urllib.request import urlopen
import operator

# support HTTPS default contexts
ssl._create_default_https_context = ssl._create_unverified_context


def url_tamil_text_filter(url):
    if USE_BS4:
        tapage = bs4.BeautifulSoup(urlopen(url), "html.parser")
    else:
        tapage = bs4.BeautifulSoup(urlopen(url))
    # tatext = tapage.body.text
    # Ref: SO 1936466
    tatext = tapage.findAll(text=True)
    tatext = [
        x
        for x in tatext
        if not (
                x.parent.name in ["style", "script", "head", "title", "meta", "[document]"]
        )
    ]
    tatext = " ".join([txt.strip() for txt in tatext])
    print_tamil_words(tatext)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tamilurlfilter.py <url-1> <url-2> ...\n")
    for url in sys.argv[1:]:
        url_tamil_text_filter(url)
