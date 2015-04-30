#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# This file is part of open-tamil project, distributed as an example
from __future__ import print_function
import tamil

import codecs
import operator
import sys
import re

LINUX = not hasattr(sys,'getwindowsversion')
PYTHON3 = sys.version > '3'

# compute word intersection graph of the a wordlist
# optimized for using the symmetry in computation but not space
class WordlistFilter:
    def __init__(self,file):
        self.file = codecs.open(file,'r','utf-8')
        self.fout = codecs.open('out.txt','w','utf-8')
        self.tatext = self.file.readlines()
        self.frequency = {}
        for line in self.tatext:
            line = line.strip()
            self.print_tamil_words( line )
        
        
    def print_tamil_words( self, line ):
        tatext = re.sub(u'\s+',u' ',line)
        if len(tatext) < 1:
            return
        taletters = tamil.utf8.get_letters(tatext)
        taletters = filter( lambda x: tamil.utf8.istamil(x) or x.isspace(), taletters )
        frequency = self.frequency
        word = u"".join(taletters)
        if len(word) < 1:
            return
        frequency[word] = 1 + frequency.get(word,0)
        print(1+frequency[word],  LINUX and word or "<WINDOWS_DONT-PRINT_ThAmIl>")
        self.frequency = frequency
    
    def __del__(self):
        for l in sorted(self.frequency.items(), key=operator.itemgetter(1)):
            if l:
                self.fout.write( "%s:%d\n"%(l[0],l[1]))
        print('total number of unique words = %d'%len(self.frequency))
        self.fout.close()
        self.file.close()

if __name__ == '__main__':
    file = 'richmond.txt'
    z = WordlistFilter( len(sys.argv) > 1 and sys.argv[1] or file  )
    try:
        z.print_tamil_words()
    except Exception as e:
        pass
    del z
