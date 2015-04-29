## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai
## 
from __future__ import print_function

import os

def _make_dict_with_path( srcfiles ):
    return dict( [( srcfile.split(u".txt")[0], mk_path( srcfile ) ) \
                      for srcfile in srcfiles] )

def get_data_dir():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return os.path.sep.join([dirname,u'data'])

def get_data_dictionaries( ):
    srcfiles = [u'tamilvu_dictionary_words.txt']
    return _make_dict_with_path(srcfiles)

def get_data_categories( ):
    srcfiles = [u'peyargal.txt',
                u'capitals-n-countries.txt',
                u'maligaiporul.txt',
                u'mooligaigal.txt',
                u'nagarangal.txt',
                u'palam.txt',
                u'vilangugal.txt']
    return  _make_dict_with_path(srcfiles)

DATADIR = get_data_dir()

def mk_path( srcfile ):
    return os.path.sep.join( [DATADIR, srcfile] )

CATEGORY_DATA_FILES = get_data_categories( )

DICTIONARY_DATA_FILES = get_data_dictionaries( )
