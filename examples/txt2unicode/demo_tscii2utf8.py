#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../..')
from tamil.txt2unicode import tscii2unicode

tscii = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """
uni = tscii2unicode(tscii)
f = open('unicode-result.txt', 'w')
f.write(uni)
f.close()

print "tscii", tscii
print "unicode", uni 
print "converted unicode stored in 'unicode-result.txt' file"

