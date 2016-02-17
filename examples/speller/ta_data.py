# -*- coding: utf-8 -*-
# (C) 2016 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package
# We generate unigram and bi-gram statistics for Tamil texts
# 
import tamil
from ngram.LetterModels import Unigram
import codecs
import pprint
import copy
import operator
from functools import cmp_to_key
import sys

def print_tamil_words_by_frequency(frequency,fp=None):
        # sort words by descending order of occurence
        if not fp:
            fp = sys.stdout
        fp.write(u"# unique words = %d\n"%(len(frequency)))
        fp.write(u"# sorted in Frequency order\n")
        fp.write(u"freqsort_data = [\n")
        for k,v in sorted(frequency.items(), key=operator.itemgetter(1),reverse=True):
            fp.write( u"[u'%s',%g],\n"%(k,v))
        fp.write("]\n")
        fp.write(u"#"*80+u"\n")
        fp.write(u"# sorted in Tamil order\n")
        fp.write(u"alphasort_data = [\n")
        for l in sorted(frequency.keys(), key=cmp_to_key(tamil.utf8.compare_words_lexicographic)):
            k,v=l,frequency[l]
            fp.write( u"[u'%s',%g],\n"%(k,v))
        fp.write("]\n")
        return

def get_prob(data):
    # adjust for non-zero probability of all symbols
    delta = 1e9
    data2 = copy.copy(data)
    s = 0.0
    nzeros = 0
    for k,v in data2.items():
       s += float(v)
       if ( v == 0 ):
           nzeros += 1
       elif  v < delta: #and not zero
           delta = v
    # delta has lowest frequency
    delta = float(delta)/2.0
    
    if nzeros > 0:
        s = s + delta*nzeros
    print(u"n-zeros = %d,%g"%(nzeros,delta/s))
    for k,v in data2.items():
        if data2[k] == 0:
            data2[k] = delta
        data2[k] = float(data2[k])/s
    # fudge adjust so probabilities sum to 1.0
    eps = abs(sum( [ v for k,v in data2.items()] ) - 1.0)
    data2[k] = data2[k]-eps
    return data2

def proc_stats(data=None,filename="dummy.txt"):
    with codecs.open(filename,"w","utf-8") as fp:
        data_as_prob = get_prob(data)
        print_tamil_words_by_frequency( data_as_prob, fp )
    return

def get_stats():
    obj = Unigram("out-tamil-words.txt")
    obj.frequency_model()
    with codecs.open("ta_data_freq.txt","w","utf-8") as fp:
        pprint.pprint( obj.letter, stream=fp)    
    proc_stats(obj.letter,u"ta_data_freq2.txt")
    return

class BigramHash(Unigram):
    def __init__(self,filename):
        Unigram.__init__(self,filename)
        self.bigram = dict()
        
    def frequency_model( self ):
        """ build a letter frequency model for Tamil letters from a corpus """
        prev_letter = None
        # use a generator in corpus
        prev_letter = list(self.corpus.next_tamil_letter())[0]
        for next_letter in self.corpus.next_tamil_letter():
            # update frequency from corpus
            key = prev_letter+next_letter
            val = self.bigram.get(key,None)
            prev_letter = next_letter
            if not val:
                self.bigram[key] = 0
            self.bigram[key] += 1
        
        return

def proc_stats2(data):
    proc_stats(get_prob( data ),"ta_data_bigram_sorted.txt")

def get_stats2():
    obj = BigramHash("out-tamil-words.txt")
    obj.frequency_model()
    with codecs.open("ta_data_bigram_freq.txt","w","utf-8") as fp:
        pprint.pprint( obj.bigram, stream=fp )    
    proc_stats2(obj.bigram)
    return

if __name__ == u"__main__":
    #proc_stats()
    get_stats2()
