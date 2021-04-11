# -*- coding: utf-8 -*-
# This file is part of open-tamil ngrams package
# (C) முத்தையா அண்ணாமலை 2013-2015,2017
#
# N-gram language model for Tamil letters

import tamil
import copy
from .Corpus import Corpus
import codecs
import operator


class Letters:
    def __init__(self, filename):
        self.letter = dict()
        self.letter.update(
            zip(tamil.utf8.tamil_letters, map(lambda x: 0, tamil.utf8.tamil_letters))
        )
        self.corpus = Corpus(filename)

    def __del__(self):
        try:
            del self.corpus
        except Exception:
            pass

    def __unicode__(self):
        op = u""
        for lett, freq in self.letter.items():
            op = op + u"%s => %d\n" % (lett, freq)
        print(max(self.letter.values()))
        return op

    def update_file(self, filename):
        self.corpus = Corpus(filename)

    def save(self, filename):
        raise Exception("Not implemented")


class Unigram(Letters):
    def __init__(self, filename):
        Letters.__init__(self, filename)

    def frequency_model(self):
        """ build a letter frequency model for Tamil letters from a corpus """
        # use a generator in corpus
        for next_letter in self.corpus.next_tamil_letter():
            # update frequency from corpus
            self.letter[next_letter] = self.letter[next_letter] + 1

    def save(self, filename):
        with codecs.open(filename, "w", "utf-8") as fp:
            for k, v in sorted(
                    self.letter.items(), key=operator.itemgetter(1), reverse=True
            ):
                if v == 0:
                    continue
                fp.write(u"%s - %d\n" % (k, v))
        return True


class Bigram(Unigram):
    def __init__(self, filename):
        Unigram.__init__(self, filename)
        self.letter2 = dict()
        for k in tamil.utf8.tamil_letters:
            self.letter2[k] = copy.copy(self.letter)

    def language_model(self, verbose=True):
        """ builds a Tamil bigram letter model """
        # use a generator in corpus
        prev = None
        for next_letter in self.corpus.next_tamil_letter():
            # update frequency from corpus
            if prev:
                self.letter2[prev][next_letter] += 1
                if verbose:
                    print(prev)
                    print(next_letter)
                    print(self.letter2[prev][next_letter])
            prev = next_letter  # update always
        return

    def save(self, filename):
        with codecs.open(filename, "w", "utf-8") as fp:
            d = {}
            for k, v in self.letter2.items():
                for k2, v2 in v.items():
                    if v2 == 0:
                        continue
                    d[k + k2] = v2
            for k, v in sorted(d.items(), key=operator.itemgetter(1), reverse=True):
                fp.write(u"%s - %d\n" % (k, v))
        return True


class Trigram(Unigram):
    def __init__(self, filename):
        Unigram.__init__(self, filename)
        self.letter3 = dict()

    def language_model(self, verbose=True):
        """ builds a Tamil bigram letter model """
        # use a generator in corpus
        p2 = None
        p1 = None
        for next_letter in self.corpus.next_tamil_letter():
            # update frequency from corpus
            if p2:
                trig = p2 + p1 + next_letter
                self.letter3[trig] = 1 + self.letter3.get(trig, 0)
            p2 = p1
            p1 = next_letter  # update always
        return

    def save(self, filename):
        with codecs.open(filename, "w", "utf-8") as fp:
            for k, v in sorted(
                    self.letter3.items(), key=operator.itemgetter(1), reverse=True
            ):
                if v == 0:
                    continue
                fp.write(u"%s - %d\n" % (k, v))
        return True
