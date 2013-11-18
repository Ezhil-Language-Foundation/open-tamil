# -*- coding: utf-8 -*-
# 
# (C) 2013 Muthiah Annamalai <ezhillang@gmail.com>
# Library provides various encoding services for Tamil libraries
# 

from . import utf8
from . import tscii

def printchar( letters ):
    for c in letters: 
        print(c, u"\\u%04x"%ord(c))

P = lambda x: u" ".join(x)
