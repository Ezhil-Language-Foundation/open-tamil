#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../..')

from tamil.txt2ipa.ipaconvert import ipa, broad
from tamil.txt2ipa.transliteration import tam2lat


text = 'வணக்கம் தமிழகம் '


t1 = tam2lat(text)
t2 = " " + t1 + " "
t2 = ipa(t2)
t3 = broad(t2)
print "after tam2lat", t1
print "after ipa", t2
print "after broad", t3

