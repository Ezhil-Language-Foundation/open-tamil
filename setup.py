#!/usr/bin/env python

from distutils.core import setup
from codecs import open

setup(name='Open Tamil',
      version='0.1-dev',
      description='Tamil language text processing tools',
      author='Muthiah Annamalai',
      author_email='ezhillang@gmail.com',
      url='https://github.com/arcturusannamalai/open-tamil',
      packages=['tamil'],
      license='GPLv3',
      platforms='PC,Linux,Mac',
      classifiers='Natural Language :: Tamil',
      long_description=open('README.md','r','UTF-8').read(),
      download_url='https://github.com/arcturusannamalai/open-tamil/archive/latest.zip',#pip
      )

