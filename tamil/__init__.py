# -*- coding: utf-8 -*-
# 
# (C) 2013 Muthiah Annamalai <ezhillang@gmail.com>
# Library provides various encoding services for Tamil libraries
# 

import utf8
import tscii

def printchar( letters ):
    for c in letters: 
        print c, "\u%04x"%ord(c)
