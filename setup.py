#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# (C) 2013-2015 முத்தையா அண்ணாமலை 
# open-tamil project

from distutils.core import setup
from codecs import open

setup(name='Open-Tamil',
      version='0.4',
      description='Tamil language text processing tools for Python v2, v3',
      author='M. Annamalai, T. Arulalan, T. Shrinivasan',
      author_email='ezhillang@gmail.com',
      url='https://github.com/arcturusannamalai/open-tamil',
      packages=['tamil','transliterate','ngram','tamil.txt2ipa','tamil.txt2unicode','tamil.utils'],
      license='GPLv3',
      platforms='PC,Linux,Mac',
      classifiers=['Natural Language :: Tamil',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4'],
      long_description=open('README.md','r','UTF-8').read(),
      download_url='https://github.com/arcturusannamalai/open-tamil/archive/master.zip',#pip
      )
