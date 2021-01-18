#!/usr/bin/python
# (C) 2015-2106 - Muthiah Annamalai
# parse data files for Tamil proper nouns
from __future__ import print_function
import codecs
import sys
import json
import tamil
import re
import pprint


class WordList:
    # data structure for a WordList containing only one category
    def __init__(self, cat):
        self.category = cat
        self.words = []

    def add(self, word):
        self.words.append(word.strip())


class DataParser:
    def __init__(self, files):
        self.categories = []
        self.files = files

    def process(self):
        for filename in self.files:
            self.parse_data(filename)
        for cat in self.categories:
            cat.words = set(cat.words)  # unique elements only
        return

    @staticmethod
    def run(args):
        # print(u">> starting data processing for files <<")
        # print(u"|".join(args))
        obj = DataParser(args)
        obj.process()
        return obj

    def parse_data(self, filename):
        cat = None
        # print(u">> file %s"%filename)
        with codecs.open(filename, "r", "utf-8") as fp:
            for line in fp.readlines():
                if line.startswith(">>"):
                    if cat:
                        self.categories.append(cat)
                        cat = None
                    newcat = line.replace(">>", "").strip()
                    cat = WordList(cat=newcat)
                elif line.startswith("#"):
                    continue
                elif cat:
                    word = u"".join(re.split("\s+", line)[1:])
                    if len(word) > 0:
                        cat.add(word)
                    else:
                        # odd looking line - we'll keep it anyway
                        cat.add(line.strip())
        if cat:
            self.categories.append(cat)
        return

    def analysis(self):
        r = {"catlen": 0, "total": 0, "dict": {}}
        r["catlen"] = len(self.categories)
        word_count = []
        for cat in self.categories:
            cat_wlen = len(cat.words)
            r["dict"][cat.category] = list(cat.words)
            word_count.append(cat_wlen)
        r["total"] = sum(word_count)
        return r

    def __unicode__(self):
        "print the statistics of the wordlist etc"
        rep = u"# categories = %d" % len(self.categories)
        word_count = []
        for cat in self.categories:
            cat_wlen = len(cat.words)
            rep += u" %s -> %d\n" % (cat.category, cat_wlen)
            word_count.append(cat_wlen)
        rep += "Total words -> %d \n" % sum(word_count)
        return rep


if __name__ == u"__main__":
    if len(sys.argv) < 2:
        print(u"usage: python data_parser.py <filename1> ... <filenamen>")
        print(
            u"       this command shows categories of words and their frequencies in document(s);"
        )
        sys.exit(-1)
    obj = DataParser.run(sys.argv[1:])
    r = obj.analysis()
    # if you wanted to save the results to JSON
    with codecs.open("ref.json", "w", "utf-8") as fp:
        # pprint.pprint( json.dumps(r), fp )
        fp.write(json.dumps(r))

    print(u"cat %d / total words %d" % (r["catlen"], r["total"]))
