## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai
##
from __future__ import print_function

import codecs
import os
import sys
from tamil import utf8
from pprint import pprint
from . import WordSpeller
from . import resources

PYTHON3 = sys.version > "3"


class PattiyalThiruthi(WordSpeller.ISpeller):
    def __init__(self, option):
        """ spell checker based on whitelist agarathi """
        if option != "std":
            raise Exception(u"unknown dictionary specified %s" % option)
        self.agarathi = PattiyalThiruthi.loadWordFile(
            resources.DICTIONARY_DATA_FILES[u"tamilvu"]
        )

    def process_word(self, word):
        # {'word':word,'is_error':False,'alternatives':None}
        rval = self.get_return_obj(word)
        if not (word in self.agarathi):
            rval["is_error"] = True
        # we don't provide alternatives %rval['alternatives']
        return rval

    @staticmethod
    def loadWordFile(filename):
        # words will be loaded from the file into the Trie structure
        with codecs.open(filename, "r", "utf-8") as fp:
            data = map(lambda word: word.strip(), fp.readlines())
        if PYTHON3:
            return frozenset(data)
        return set(data)


if __name__ == "__main__":
    obj = PattiyalThiruthi("std")
    from pprint import pprint

    in_words = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
    pprint(map(obj.process_word, in_words))
