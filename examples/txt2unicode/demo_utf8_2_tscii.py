#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Arulalan.T <arulalant@gmail.com>
# (C) 2015 Muthiah Annamalai
# This file is part of 'open-tamil/txt2unicode' package examples
# 

import sys
sys.path.append('../..')
from tamil.txt2unicode import tscii2unicode, unicode2tscii

tscii = """¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû  """
uni_1 = tscii2unicode(tscii)
tscii_from_uni = unicode2tscii(uni_1)
uni_2 = tscii2unicode(tscii_from_uni)

f = open('encode-result.txt', 'w')
f.write("Initial tscii : " + tscii + "\n\n")
f.write("From tscii to unicode : " + uni_1 + "\n\n")
f.write("From unicode to tscii : " + tscii_from_uni + "\n\n")
f.write("Again back to unicode from above tscii : " +  uni_2)
f.close()

assert (uni_1 == uni_2), " Both unicode are 'not' same! "
assert (tscii == tscii_from_uni), " Both tscii are 'not' same! "

print("tscii original input", tscii)
print("from tscii2unicode", uni_1)
print("from unicode2tscii", tscii_from_uni)
print("back to unicode", uni_2)

print("converted unicode stored in 'encode-result.txt' file")
