#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

import copy, random
import tamil

from sys import version
PYTHON3 = version > '3'
        
# Vertical / Horizontal Word Grids

# Put a list of words into a grid. this is purely vertical or purely horizontal style.
class WordXSec:
    @staticmethod
    def compute( wordlist ):
        """ build a dictionary of words, and their intersections """
        xsections = {}
        for i in xrange(len(wordlist)):
            word_i = wordlist[i]
            for j in xrange(len(wordlist)):
                word_j = wordlist[j]
                if i == j :
                    xsections[word_i] = xsections.get(word_i,list())
                    continue
                # optimize for, i > j, info is calculated already 
                #if i > j:
                #    xsections[word_j].extend( [ xsections[word_i][j] ] )
                xsec_counts = tamil.utf8.word_intersection( word_i, word_j )
                if not xsections.get(word_i,None):
                    xsections[word_i] =  [xsec_counts]
                else:
                    xsections[word_i].extend( [ xsec_counts ] )
        for k,v in xsections.items():
            print( ",".join( ["%d"%len(vv) for vv in v] ) )
        return

if __name__ == "__main__":
    lang = ['EN','TA'][0]
    if lang == 'EN':
        wordlist = [u'food',u'water',u'shelter',u'clothing']
        fill_letters = list(map(chr,[ord('a')+i for i in range(0,26)]))
    else:
        wordlist = [u'உப்பு', u'நாற்பண்',u'பராபரம்', u'கான்யாறு', u'ஆறு', u'சன்னியாசி', u'நெல்லி']
        fill_letters = tamil.utf8.tamil_letters
    WordXSec.compute( wordlist )
