## -*- coding: utf-8 -*-
#(C) 2018 Muthiah Annamalai
# This file is part of Open-Tamil project
# You may use or distribute this file under terms of MIT license
## 
from __future__ import print_function
import codecs
import json

from tamil import utf8
from pprint import pprint

from solthiruthi import resources
from huffman import huffman, print_huffman_code_cwl

def build_morse_code():
    unigram = TamilUnigramStats().unigram
    v_keys = unigram.keys()
    p = [unigram[k] for k in v_keys]
    code,_ = huffman(v_keys,p)
    cwl,codelist = print_huffman_code_cwl(code,p,v_keys)
    tamilmorse = {}
    print(u"<ul>")
    descending_keys = [x for _,x in sorted(zip(unigram.values(),v_keys),reverse=True)]
    for k in descending_keys:
        v = code[k]
        v = v.replace('0','.').replace('1','-')
        tamilmorse[k] = v
        print(u"<li>%s  -&gt; <b><kbd>%s</kbd></b></li>"%(k,v))
    print(u"</ul>")
    with codecs.open("tamilmorse.json","w","utf-8") as fp:
        fp.write( json.dumps(tamilmorse) )
    return

class TamilUnigramStats:
    def __init__(self):
        self.unigram = {} # Tamil letter -> probability of occurence
        self.unigram_file = resources.mk_path("tvu_unigram.txt")
        with codecs.open(self.unigram_file,"r","utf-8") as fp:
            for L in fp.readlines():
                a,b = L.split("-")
                a=a.strip()
                b=b.strip()
                self.unigram[a]=float(b)
            normalize = 1+sum(self.unigram.values())
            for k,v in self.unigram.items():
                self.unigram[k] = v/normalize
        

if __name__ == u"__main__":
    build_morse_code()

