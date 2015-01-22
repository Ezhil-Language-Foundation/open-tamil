#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

import copy, random
import tamil

from sys import version
PYTHON3 = version > '3'

# compute word intersection graph of the a wordlist
# optimized for using the symmetry in computation but not space
class WordXSec:
    @staticmethod
    def driver(wordlist):
        obj = WordXSec( wordlist )
        obj.compute()
        obj.display()
        return obj
    
    def __init__(self,wordlist):
        self.wordlist = wordlist
        # adjacency list of intersection graph
        self.xsections = {}
    
    def compute( self ):
        # compute the intersection graph into @xsections dictionary
        wordlist = self.wordlist
        """ build a dictionary of words, and their intersections """
        xsections = {}
        for i in range(len(wordlist)):
            word_i = wordlist[i]
            for j in range(len(wordlist)):
                word_j = wordlist[j]
                if i == j:
                    # force self-intersection to be 0
                    if not xsections.get(word_i,None):
                        xsections[word_i] = ['']
                    else:
                        xsections[word_i].extend([''])
                    continue
                # optimize for, i > j, info is calculated already 
                if i > j:
                    xsec_counts = xsections[word_j][i]
                else:
                    xsec_counts = tamil.utf8.word_intersection( word_i, word_j )
                if not xsections.get(word_i,None):
                    xsections[word_i] =  [xsec_counts]
                else:
                    xsections[word_i].extend( [ xsec_counts ] )
        self.xsections = xsections
    
    def display(self):
        # print adjacency list of intersection graph
        for k in self.wordlist:
            v = self.xsections[k]
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
    WordXSec.driver( wordlist )
