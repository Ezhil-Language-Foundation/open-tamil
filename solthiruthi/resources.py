## -*- coding: utf-8 -*-
## This file is part of Open-Tamil project.
## (C) 2015,2020 Muthiah Annamalai
##
from __future__ import print_function

import os


def _make_dict_with_path(srcfiles):
    return dict([(srcfile.split(u".txt")[0], mk_path(srcfile)) for srcfile in srcfiles])


def get_data_dir():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return os.path.sep.join([dirname, u"data"])


def get_data_dictionaries():
    srcfiles = {
        "tamilvu": "tamilvu_dictionary_words.txt",
        "projmad": "proj-madurai-040415.txt",
        "wikipedia": "wikipedia_full_text_032915.txt",
        "english": "english_dictionary_words.txt",
        "parallel": "parallel_dictionary.txt",
        "vatamozhi": "monierwilliams_dictionary_words.txt",
    }
    for k, v in srcfiles.items():
        srcfiles[k] = mk_path(v)
    return srcfiles


def get_data_categories():
    # add new elements to end
    srcfiles = [
        "peyargal.txt",
        "capitals-n-countries.txt",
        "maligaiporul.txt",
        "mooligaigal.txt",
        "nagarangal.txt",
        "palam.txt",
        "vilangugal.txt",
        "TamilStopWords.txt",
    ]
    return _make_dict_with_path(srcfiles)


DATADIR = get_data_dir()


def mk_path(srcfile):
    return os.path.sep.join([DATADIR, srcfile])


CATEGORY_DATA_FILES = get_data_categories()

DICTIONARY_DATA_FILES = get_data_dictionaries()
