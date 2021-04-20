# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from solthiruthi.dictionary import *
from tamil import wordutils, utf8
from ngram import edit_distance
import math
from pprint import pprint

TVU, TVU_size = DictionaryBuilder.create(TamilVU)
word2, parts2 = "ஒருதலைகாதல்", ["ஒருதலை", "காதல்"]
actual2 = wordutils.word_split(word2, TVU)
pprint(actual2)

TVU, TVU_size = DictionaryBuilder.create(EnglishLinux)
TVU.add("erin")
word2, parts2 = "motherinlaw", ["ஒருதலை", "காதல்"]
word3 = None
while True:
    if not word3:
        word3 = "bullpen"
    for w in wordutils.permutagrams(word3, TVU):
        print((">>>> %s" % w))
    word3 = input("enter a word>> ")
