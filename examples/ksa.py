#!/bin/env python3
from codecs import open
from tamil import utf8
import re

with open('kuttistory.txt','r','utf-8') as fp:
    data = fp.readlines()

class Stats:
    __fields__ = ('total_words','tamil_words')
stats = Stats()
stats.total_words=0.0
stats.tamil_words=0.0

for line in data:
    all_words = re.split('\s+',line.strip())
    ta_words = list(utf8.get_tamil_words(utf8.get_letters(line)))
    print((all_words,len(ta_words)))
    stats.tamil_words += len( ta_words )
    stats.total_words += len(all_words)
#tamil fraction
taf = float(stats.tamil_words)/stats.total_words
print(('English = {0}%, Tamil = {1}%'.format(100.0*(1-taf),100.0*(taf))))
