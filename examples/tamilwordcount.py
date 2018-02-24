#!/usr/bin/env python3

from tamil import utf8 as tamil
import argparse


class Text:
    def __init__(self, content):
        self.content = content
        self.letter_toll = 0
        self.line_toll = 0
        self.word_toll = 0
        self.count_letter()
        self.count_line()
        self.count_word()

    def count_word(self):
        if self.__valid():
            self.word_toll = len(self.content.split())

    def count_line(self):
        if self.__valid():
            self.line_toll = len(self.content.splitlines())

    def count_letter(self):
        if self.__valid():
            self.letter_toll = len(tamil.get_letters(self.content))

    def __valid(self):
        return True


parser = argparse.ArgumentParser()
parser.add_argument('-w',action='store_true', help='Count Words')
parser.add_argument('-l',action='store_true', help='Count Lines')
parser.add_argument('-c',action='store_true', help='Count Charachters')
parser.add_argument('files', nargs=argparse.REMAINDER)
options = parser.parse_args()

sample = '''சுரேந்தர்
மிகவும் அமைதியானவர். நல்லவர்.
நேர்மையானவர்.
பண்பாளர்.'''

sample1 = Text(sample)

if options.files:
    print(options.files)
else:
    if options.c:
        print("எழுத்து எண்ணிக்கை: {0}".format(sample1.letter_toll))
    if options.l:
        print("வரி எண்ணிக்கை: {0}".format(sample1.line_toll))
    if options.w:
        print("சொல் எண்ணிக்கை: {0}".format(sample1.word_toll))