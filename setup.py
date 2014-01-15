#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# (C) 2013-2014 முத்தையா அண்ணாமலை 
# open-tamil project

from distutils.core import setup
from codecs import open

setup(name='Open-Tamil',
      version='0.2.2-devel',
      description='Tamil language text processing tools',
      author='Muthiah Annamalai',
      author_email='ezhillang@gmail.com',
      url='https://github.com/arcturusannamalai/open-tamil',
      packages=['tamil','transliterate','ngram'],
      license='GPLv3',
      platforms='PC,Linux,Mac',
      classifiers='Natural Language :: Tamil',
      long_description=open('README.md','r','UTF-8').read(),
      download_url='https://github.com/arcturusannamalai/open-tamil/archive/latest.zip',#pip
      )
