#!python
# -*- coding: utf-8 -*-
#
# This file is distributed under MIT License or default open-tamil license.
# (C) 2013-2015 Muthiah Annamalai
#
# This file is part of 'open-tamil' examples
# It can be used to identify patterns in a Tamil text files;
# e.g. it has been used to identify patterns in Tamil Wikipedia
# articles.
#

import tamil
import sys
import codecs
from transliterate import *
import re

from functools import cmp_to_key
import operator

PYTHON3 = sys.version[0] > "2"
if not PYTHON3:
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout)


# use generators for better memory footprint -- 04/04/15
class WordFrequency(object):
    # get words
    @staticmethod
    def get_tamil_words_iterable(letters):
        """ given a list of UTF-8 letters section them into words, grouping them at spaces """
        # punctuations = u'-,+,/,*,>,<,_,],[,{,},(,)'.split(',')+[',']
        # isspace_or_tamil = lambda x:  not x in punctuations  and tamil.utf8.istamil(x)

        # correct algorithm for get-tamil-words
        buf = []
        for idx, let in enumerate(letters):
            if tamil.utf8.istamil(let):
                buf.append(let)
            else:
                if len(buf) > 0:
                    yield "".join(buf)
                    buf = []
        if len(buf) > 0:
            yield "".join(buf)

    # sentinel
    def __init__(self, tatext=""):
        object.__init__(self)
        self.frequency = {}

    # process data
    def process(self, new_text):
        for taline in new_text.split("\n"):
            self.tamil_words_process(taline)
        return

    # finalize
    def display(self):
        self.print_tamil_words()
        return

    # processor / core
    def tamil_words_process(self, taline):
        taletters = tamil.utf8.get_letters_iterable(taline)
        # raw words
        # for word in re.split(u"\s+",tatext):
        #    print(u"-> ",word)
        # tamil words only
        for pos, word in enumerate(WordFrequency.get_tamil_words_iterable(taletters)):
            if len(word) < 1:
                continue
            self.frequency[word] = 1 + self.frequency.get(word, 0)
        return

    # closer/results
    def print_tamil_words(self):
        # sort words by descending order of occurence
        print("# unique words = %d" % (len(self.frequency)))
        for l in sorted(list(self.frequency.items()), key=operator.itemgetter(1)):
            print(l[0], ":", l[1])
        print("#" * 80)
        print("# sorted in Tamil order")
        for l in sorted(
                list(self.frequency.keys()),
                key=cmp_to_key(tamil.utf8.compare_words_lexicographic),
        ):
            print(l, ":", self.frequency[l])
        return


# driver
def demo_tamil_text_filter(file_urls):
    # url = u"../tawiki-20150316-all-titles"
    if not type(file_urls) is list:
        file_urls = [file_urls]
    obj = WordFrequency()
    for filepath in file_urls:
        try:
            tatext = codecs.open(filepath, "r", "utf-8").read()
            obj.process(tatext)
        except Exception as e:
            sys.stderr.write(
                "Skipping the file :"
                + filepath
                + " due to exception\n\t\t "
                + str(e)
                + "\n"
            )
    obj.display()
    return obj


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python solpattiyal.py <filename>")
        print(
            "       this command shows list of unique words in Tamil and their frequencies in document(s);"
        )
        print("       it also relists the words in the sorted order")
        sys.exit(-1)
    demo_tamil_text_filter(sys.argv[1:])
