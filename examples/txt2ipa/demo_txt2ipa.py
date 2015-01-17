#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Arulalan.T <arulalant@gmail.com>
# 
# This file is part of 'open-tamil/txt2ipa' package examples
# 

import sys
sys.path.append('../..')

from tamil.txt2ipa import txt2ipa

# FIXME : demo does not work OK
assert False, "demo failed"
text = u'வணக்கம் தமிழகம் '


print(u"input unicode text", text)
print("after ipa", txt2ipa(text, broad=False))
print("after broad", txt2ipa(text)) # by default broad is enabled 
