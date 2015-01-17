#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Arulalan.T <arulalant@gmail.com>
# 
# This file is part of 'open-tamil/txt2unicode' package examples
# 

import sys
sys.path.append('../..')
from tamil.txt2unicode import auto2unicode

# note that atleast one compound characters in below tscii variable string
# falls under tscii.unique.chars.txt characters.

# for other encodes user need to look at encodes_chars directory files and
# identify atleast one unique compound characters & incert in input text. 
# so that auto2unicode can identiy encode for you ! 

tscii = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

uni = auto2unicode(tscii)
f = open('unicode-result.txt', 'w')
f.write(uni)
f.close()

print("tscii", tscii)
print("unicode", uni)
print("converted unicode stored in 'unicode-result.txt' file\n\n")

# demo for common compound characters
common = """ù£tPùP\[tI
è£n\[nwh ùSô ªþ£ ùaô """
print("common", common)
uni = auto2unicode(common)
