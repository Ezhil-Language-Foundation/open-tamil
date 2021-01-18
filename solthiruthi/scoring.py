## -*- coding: utf-8 -*-
## (C) 2017 Muthiah Annamalai,
##
from __future__ import print_function
import codecs
import math
import operator
import os
import sys

from tamil import utf8
from pprint import pprint

from . import resources

PYTHON3 = sys.version[0] == "3"
if PYTHON3:
    from functools import reduce


class NGStats:
    def __init__(self):
        self.unigram_file = resources.mk_path("tvu_unigram.txt")
        self.bigram_file = resources.mk_path("tvu_bigram.txt")
        self.default = (1e-1, 1e-4)
        self.bigram = dict()
        self.unigram = dict()
        self.load()

    def load(self):
        with codecs.open(self.bigram_file, "r", "utf-8") as fp:
            for L in fp.readlines():
                a, b = L.split("-")
                a = a.strip()
                b = b.strip()
                self.bigram[a] = float(b)
            normalize = 1 + sum(self.bigram.values())
            for k, v in self.bigram.items():
                self.bigram[k] = v / normalize

        with codecs.open(self.unigram_file, "r", "utf-8") as fp:
            for L in fp.readlines():
                a, b = L.split("-")
                a = a.strip()
                b = b.strip()
                self.unigram[a] = float(b)
            normalize = 1 + sum(self.unigram.values())
            for k, v in self.unigram.items():
                self.unigram[k] = v / normalize
            # pprint(self.unigram)
            # pprint(sum(self.unigram.values()))

    def _ngram_scorer(self, letters, dictionary, default):
        res = list()
        for letter in letters:
            res.append(dictionary.get(letter, default))
        return res

    def unigram_score(self, letters):
        return self._ngram_scorer(letters, self.unigram, self.default[0])

    def bigram_score(self, letters):
        return self._ngram_scorer(letters, self.bigram, self.default[1])


ngstats = NGStats()


def unigram_score(letters):
    return math.log10(reduce(operator.mul, ngstats.unigram_score(letters), 1.0))


def bigram_scores(letters):
    g1_letters = list()
    g2_letters = list()
    L = len(letters)

    # (1,2,3, ... ) sequence is grouped (1, 2 3, 4 5, ...)
    L = len(letters)
    g1_letters.append(letters[0])
    for idx, l in enumerate(letters[min(L - 1, 1) :]):
        if idx == 0:
            l_prev = l
            continue
        curr = u"".join([l_prev, l])
        g1_letters.append(curr)
        l_prev = l

    # (1,2,3, ... ) sequence is grouped (1 2, 3 4, ... )
    for idx, l in enumerate(letters):
        if idx == 0:
            l_prev = l
            continue
        curr = u"".join([l_prev, l])
        g2_letters.append(curr)
        l_prev = l
    if len(g2_letters) == 0:
        g2_letters.append(letters[0])
    # pprint(letters)
    # pprint(g1_letters)
    # pprint(g2_letters)
    s1 = reduce(operator.mul, ngstats.bigram_score(g1_letters), 1.0)
    s2 = reduce(operator.mul, ngstats.bigram_score(g2_letters), 1.0)
    return list(map(math.log10, [s1, s2]))


if __name__ == u"__main__":
    #  a ab abc 123456789
    input_words = u"டைட்டானிக் படத்தில் ஜேக் மற்றும் ரோஸ் தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
    for word in input_words:
        pprint(word)
        letters = utf8.get_letters(word)
        pprint(bigram_scores(letters))
        pprint(unigram_score(letters))
