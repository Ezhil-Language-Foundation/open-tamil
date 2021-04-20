# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# (C) முத்தையா அண்ணாமலை 2013-2015
#

import codecs
from tamil import utf8


class Corpus:
    """Class defines a Corpus data file, and reading information from
    this file for only the Tamil letters. Usage would be to construct this object,
    with a filename argument, and then use next_tamil_letter() method on this object."""

    def __init__(self, filename):
        """ @filename - describe corpus to be loaded"""
        self.filename = filename
        self.handle = None

    def next_tamil_letter(self):
        """ method loads the corpus and returns one Tamil letter at a time in iterable"""
        with codecs.open(self.filename, "r", "utf-8") as handle:
            self.handle = handle
            for letter in filter(utf8.istamil,utf8.get_letters_iterable(self.handle.read())):
                yield letter
        return
