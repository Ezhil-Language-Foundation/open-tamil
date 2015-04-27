#!/usr/bin/python

import sys
import codecs
import tamil
import json

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

def extract_words(filename):
    ht = json.load( codecs.open(filename,'r','utf-8') )
    for word in sorted(ht.keys()):
        print(word)
    return

if __name__ == u"__main__":
    for itr in range(1,25):
        filename = u"v%02d.json"%itr
        extract_words(filename)
