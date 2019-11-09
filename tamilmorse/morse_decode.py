## -*- coding: utf-8 -*-
#(C) 2018 Muthiah Annamalai
# This file is part of Open-Tamil project
# You may use or distribute this file under terms of MIT license

import codecs
import json
import tamil
import sys
import os

CURRDIR = os.path.dirname(os.path.realpath(__file__))
#e.g. python morse_decode.py ...-. .-.---.-.-..-- ..-.--.---.-.-... --.-....
def decode(text):
    with codecs.open(os.path.join(CURRDIR,'data',"madurai_tamilmorse.json"),"r","utf-8") as fp:
        codebook = json.loads(fp.read())
    output = []
    reverse_code = {}
    for k,v in codebook.items():
        reverse_code[v] = k
    #print(">%s<"%text)
    output = [reverse_code.get(chunks,"x") for chunks in text.split(" ")]
    #print(u" ".join(output))
    return u" ".join(output)

if __name__ == u"__main__":
    decode(" ".join(sys.argv[1:]))
