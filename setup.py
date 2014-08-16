#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# (C) 2013-2014 முத்தையா அண்ணாமலை 
# open-tamil project

from distutils.core import setup
from codecs import open

setup(name='Open-Tamil',
      version='0.3',
      description='Tamil language text processing tools',
      author='M. Annamalai, T. Arulalan,',
      author_email='ezhillang@gmail.com',
      url='https://github.com/arcturusannamalai/open-tamil',
      packages=['tamil','transliterate','ngram','tamil.txt2ipa','tamil.txt2unicode'],
      license='GPLv3',
      platforms='PC,Linux,Mac',
      classifiers='Natural Language :: Tamil',
      long_description=open('README.md','r','UTF-8').read(),
      download_url='https://github.com/arcturusannamalai/open-tamil/archive/master.zip',#pip
      )

