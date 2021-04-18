#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (C) 2013-2021 முத்து அண்ணாமலை மற்றும் ஓப்பன் தமிழ் பங்களிப்பாளர்கள்
# open-tamil project

from codecs import open

from setuptools import setup

long_description = open("README.rst", "r", "UTF-8").read()

setup(
    name="Open-Tamil",
    version="1.0",
    description="Tamil language text processing tools for Python v3",
    author="M. Annamalai, T. Arulalan, and other contributors",
    author_email="ezhillang@gmail.com",
    long_description=long_description,
    url="https://github.com/Ezhil-Language-Foundation/open-tamil",
    packages=[
        "tamil",
        "transliterate",
        "ngram",
        "tamil.txt2ipa",
        "tamil.txt2unicode",
        "tamil.utils",
        "solthiruthi",
        "spell",
        "tamilstemmer",
        "tamilmorse",
        "tamilsandhi",
        "valai",
        "kural",
        "tamiltts",
        "tabraille",
    ],
    package_dir={
        "solthiruthi": "solthiruthi",
        "tamilmorse": "tamilmorse",
        "tamilsandhi": "tamil-sandhi-checker/tamilsandhi",
    },
    package_data={
        "solthiruthi": ["data/*.txt"],
        "tamilmorse": ["data/*.json"],
        "tamilsandhi": ["all-tamil-nouns.txt"],
    },
    license="MIT",
    scripts=[
        "examples/tamilwordcount.py",
        "examples/tamilwordfilter.py",
        "examples/tamilurlfilter.py",
        "examples/tamilphonetic.py",
        "examples/tamiltscii2utf8.py",
        "examples/tamilwordgrid.py",
        "examples/tamilspell.py",
        "examples/solpattiyal.py",
    ],
    platforms="PC,Linux,Mac",
    classifiers=[
        "Natural Language :: Tamil",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
    download_url="https://github.com/Ezhil-Language-Foundation/open-tamil/archive/master.zip",
)
