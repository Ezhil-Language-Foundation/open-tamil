## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
##
from __future__ import print_function
import abc
import codecs
import re

from tamil import utf8

from .datastore import Queue


# DOM for documents
class Position:
    __metaclass__ = abc.ABCMeta

    def __init__(self, row, col):
        self.row = row
        self.col = col


class Entity(Position):
    __metaclass__ = abc.ABCMeta

    def __init__(self, word, flagged=False, **kwargs):
        super(Entity, self).__init__(**kwargs)
        self.flagged = flagged
        self.word = word
        self.letters = utf8.get_letters(word)

    def isFlagged(self):
        return self.flagged

    @abc.abstractmethod
    def isWord(self):
        pass

    def getLetters(self):
        return self.letters


class WordEntity(Entity):
    def __init__(self, word, **kwargs):
        super(WordEntity, self).__init__(word=word, **kwargs)

    def isWord(self):
        return True


class NonEntity(Entity, Position):
    def __init__(self, word, **kwargs):
        super(NonEntity, self).__init__(word=word, **kwargs)

    def isWord(self):
        return False


class Document(Queue):
    "open contents of a file on load"

    def __init__(self, filename):
        self.filename = filename
        with codecs.open(filename, "r", "utf-8") as fileobj:
            self.text = fileobj.readlines()
        super(Document, self).__init__()

    def tokenize(self):
        spc = re.compile("[\ \t\r]+")
        idx = 1
        LEN = len(self.text)
        prev = None
        for row, line in enumerate(self.text):
            re.search()  # looks useful
        if self.isempty():
            raise Exception("Empty File: Cannot be tokenized")
