#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santhirules import joinWords

a = u'என்ன'
b = u'என்ன'
w = joinWords(a, b).encode('utf8')
print w

A = a.encode('utf8')
B = b.encode('utf8')

f = open('out1.txt', 'a')
f.write(A + ' + ' + B + ' = ' + w+'\n')
f.close()
