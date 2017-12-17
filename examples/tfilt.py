# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
#
import codecs
import sys
import tamil
from transliterate import *
import operator

def print_tamil_words( tatext ):
    taletters = tamil.utf8.get_letters(tatext)
    # raw words
    #for word in re.split(u"\s+",tatext):
    #    print(u"-> ",word)    
    # tamil words only
    frequency = {}
    for pos,word in enumerate(tamil.utf8.get_tamil_words(taletters)):
        #print(pos, word)
        frequency[word] = 1 + frequency.get(word,0)
    #for key in frequency.keys():
    #    print(u"%s : %s"%(frequency[key],key))
    # sort words by descending order of occurence
    for l in sorted(frequency.iteritems(), reverse=True, key=operator.itemgetter(1)):
        print(u"%s"%( l[0]))#,l[1]))

def demo_tamil_text_filter( url ):    
    tatext = codecs.open(url,"r","utf-8").read()
    print_tamil_words( tatext )

if __name__ == u"__main__":
    for url in sys.argv[1:]:
        demo_tamil_text_filter(url)

