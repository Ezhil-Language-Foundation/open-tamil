#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Arulalan.T <arulalant@gmail.com>
# (C) 2015 Muthiah Annamalai
# This file is part of 'open-tamil/txt2unicode' package examples
# 

import sys
sys.path.append('../..')
from tamil.txt2unicode import tscii2unicode, unicode2tscii, unicode2auto, auto2unicode

uni_1 = u"""திருவள்ளுவர் அருளிய திருக்குறள்    """
tscii = unicode2tscii(uni_1)
if not tscii:
    # FIXME: known faliure.
    assert False, "unicode2tscii failed. You need to debug"
print(tscii,len(tscii))
tscii_sample = tscii.split(' ')[0]
tscii_from_auto = unicode2auto(uni_1, tscii_sample)
uni_2 = auto2unicode(tscii_from_auto)

f = open(u'auto_encode-result.txt', 'w')
f.write("Initial unicode : " + uni_1 + "\n\n")
f.write("From unicode to tscii : " + tscii + "\n\n")
f.write("From unicode to tscii by auto function : " + tscii_from_auto + "\n\n")
f.write("Again back to unicode from above tscii by auto function: " +  uni_2)
f.close()

assert (uni_1 == uni_2), " Both unicode are 'not' same! "
assert (tscii == tscii_from_auto), " Both tscii are 'not' same! "

print("unicode original input", uni_1)
print("from unicode2tscii", tscii)
print("from unicode2auto", tscii_from_auto)
print("back to unicode", uni_2)

print("converted unicode stored in 'auto_encode-result.txt' file")
