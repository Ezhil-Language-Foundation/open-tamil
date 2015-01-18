# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

import tamil
from transliterate import *
try:
    import bs4 #requires beautiful soup 4
except ImportError as ie:
    # work with BS3
    import BeautifulSoup
    class bs4:
        BeautifulSoup = BeautifulSoup.BeautifulSoup
from urllib2 import urlopen
import operator

def print_tamil_words( tatext ):
    taletters = tamil.utf8.get_letters(tatext)
    
    # raw words
    #for word in re.split(u"\s+",tatext):
    #    print(u"-> ",word)
    
    # tamil words only
    frequency = {}
    for pos,word in enumerate(tamil.utf8.get_tamil_words(taletters)):
        print(pos, word)
        frequency[word] = 1 + frequency.get(word,0)
    
    #for key in frequency.keys():
    #    print(u"%s : %s"%(frequency[key],key))
    
    # sort words by descending order of occurence
    for l in sorted(frequency.iteritems(), key=operator.itemgetter(1)):
        print( l[0],':',l[1])
    

def demo_tamil_text_filter( ):
    url = u"http://tamil.thehindu.com/opinion/columns/%E0%AE%89%E0%AE%9F%E0%AE%A9%E0%AF%87-%E0%AE%89%E0%AE%9F%E0%AE%A9%E0%AF%87-%E0%AE%8E%E0%AE%B4%E0%AF%81%E0%AE%A4%E0%AE%BF%E0%AE%A9%E0%AE%BE%E0%AE%B2%E0%AF%8D-%E0%AE%9A%E0%AF%86%E0%AE%AF%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%AA%E0%AF%8D-%E0%AE%AA%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AE%BF%E0%AE%95%E0%AF%88-%E0%AE%AA%E0%AF%8B%E0%AE%B2-%E0%AE%86%E0%AE%95%E0%AE%BF%E0%AE%B5%E0%AE%BF%E0%AE%9F%E0%AF%81%E0%AE%AE%E0%AF%8D-%E0%AE%85%E0%AE%9A%E0%AF%8B%E0%AE%95%E0%AE%AE%E0%AE%BF%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AE%A9%E0%AF%8D-%E0%AE%A8%E0%AF%87%E0%AE%B0%E0%AF%8D%E0%AE%95%E0%AE%BE%E0%AE%A3%E0%AE%B2%E0%AF%8D/article5615711.ece"
    url = u"http://ta.wikipedia.org"
    tapage = bs4.BeautifulSoup(urlopen(url))
    tatext = tapage.body.text
    print_tamil_words( tatext )

if __name__ == u"__main__":
    demo_tamil_text_filter()
