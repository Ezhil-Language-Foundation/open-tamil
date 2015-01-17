#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from tamil.txt2unicode import auto2unicode, tscii2unicode

BUF_SIZE = 100

infile = 'sample_encode_documents/tscii.sample1.txt'
outfile = 'sample_encode_documents/tscii.sample1.unicode.txt'

inf = open(infile)
outf = open(outfile, 'w')


def converte2unicode(lines):
    for line in lines:
        uni = tscii2unicode(line)
        outf.write(uni)
# end of def converte2unicode(lines, outf):

tmp_lines = inf.readlines(BUF_SIZE)
while tmp_lines:
    # converrt 100 lines at a time
    converte2unicode(tmp_lines)	
    tmp_lines = inf.readlines(BUF_SIZE)
# end of while tmp_lines:

inf.close()
outf.close()

print("converted unicode stored in file", outfile)
