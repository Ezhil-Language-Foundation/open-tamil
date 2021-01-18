#!python
# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2018 சுரேந்தர் இரவிச்சந்திரன்
# Copyright (C) 2019 முத்து அண்ணாமலை
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import imp

try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3

imp.reload(sys)
# sys.setdefaultencoding('utf-8')

from tamil import utf8 as tamil
import argparse
import codecs


class Text:
    """ Text object holds a file object and counts requisite stats """

    def __init__(self, content=None, lineonly=True, wordonly=True, charonly=True):
        self.content = content
        self.lineonly = lineonly
        self.wordonly = wordonly
        self.charonly = charonly
        self.letter_toll = 0
        self.line_toll = 0
        self.word_toll = 0
        self.line = ""
        if content:
            for line in content:
                self.line = line
                if self.lineonly:
                    self.count_line()
                if self.wordonly:
                    self.count_word()
                if self.charonly:
                    self.count_letter()

    def count_word(self):
        self.word_toll += len(self.line.split())

    def count_line(self):
        self.line_toll += 1

    def count_letter(self):
        self.letter_toll += len(tamil.get_letters(self.line))


def print_file_stats(filename):
    try:
        fileobj = codecs.open(filename, "r", "utf-8")
    except FileNotFoundError as e:
        print(("File {} not found".format('"' + filename + '"')))
        return
    except OSError as err:
        print(("OS error: {0}".format(err)))
        return
    file_text = Text(
        fileobj,
        lineonly=attribs["line"],
        wordonly=attribs["word"],
        charonly=attribs["char"],
    )
    fileobj.close()

    file_stats = construct_file_stats(file_text, filename)
    add_to_total_stats(file_text)
    print(file_stats)


def add_to_total_stats(txtobj):  # Text
    total_stats.line_toll += txtobj.line_toll
    total_stats.word_toll += txtobj.word_toll
    total_stats.letter_toll += txtobj.letter_toll


def construct_file_stats(textobj, name=""):  # Text
    file_stat_display = ""

    if attribs["line"]:
        file_stat_display += "{:>8}".format(textobj.line_toll)
    if attribs["word"]:
        file_stat_display += "{:>8}".format(textobj.word_toll)
    if attribs["char"]:
        file_stat_display += "{:>8}".format(textobj.letter_toll)
    # TBD: complete implementation of unique-word counting
    file_stat_display += " {}".format(name)

    return file_stat_display


parser = argparse.ArgumentParser()
parser.add_argument("-w", action="store_true", help="Count Words")
parser.add_argument("-l", action="store_true", help="Count Lines")
parser.add_argument("-c", action="store_true", help="Count Characters")
parser.add_argument("-u", action="store_true", help="Count unique words")
parser.add_argument("files", nargs=argparse.REMAINDER)
options = parser.parse_args()

# defaults
attribs = {
    "line": True,
    "word": True,
    "char": True,
    "uniq": False,
}

if options.l or options.w or options.c:
    attribs["line"] = options.l
    attribs["word"] = options.w
    attribs["char"] = options.c
    attribs["uniq"] = options.u
total_stats = Text()

if len(options.files) > 0:
    for file in options.files:
        try:
            print_file_stats(file)
        except Exception as ioe:
            print(("Cannot process file %s\n    %s" % (file, str(ioe))))
    if len(options.files) > 1:
        total = construct_file_stats(total_stats, "total")
        print(total)
