#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../..')

from tamil.txt2ipa import txt2ipa

text = 'வணக்கம் தமிழகம் '


print "input unicode text", text
print "after ipa", txt2ipa(text, broad=False)
print "after broad", txt2ipa(text) # by default broad is enabled 

