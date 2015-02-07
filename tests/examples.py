# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *

from transliterate import *


from tamil import utf8 as tamil

def demo_lib_tamil():
     """ some example modules for Tamil library """
     for c in tamil.accent_symbols:
          if c and (LINUX): print(u"%s"%c, "u%04x"%ord(c))
          
     if ( LINUX ): print(u"|".join(tamil.accent_symbols[1:]))
     
     u" ".join(["\\u%04X"%ord(c) for c in tamil.accent_symbols[1:]])     
     
     u" ".join(["%04X"%ord(c) for c in tamil.accent_symbols[1:]])
     
     u" \\u".join(["%04X"%ord(c) for c in tamil.accent_symbols[1:]])
     
     u" \\u".join(["%04X"%ord(c) for c in tamil.accent_symbols[1:]])
     
     u" ".join(["\\u%04X"%ord(c) for c in tamil.accent_symbols[1:]])

if __name__ == "__main__":
     demo_lib_tamil()
