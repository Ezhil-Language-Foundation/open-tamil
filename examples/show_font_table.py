# This code is released to public domain.
# It is part of open-tamil project examples.
#
# Code to show fontbased encoding tables in Open-TAMIL
# Ref: https://github.com/Ezhil-Language-Foundation/open-tamil/issues/216

import sys
from pprint import pprint
import unicodedata

# requires installing fontTools
# Ref: https://fonttools.readthedocs.io
from fontTools import ttLib


def show_font_table(fontname):
    f=ttLib.TTFont(fontname)
    cmap=f.getBestCmap()
    pprint(cmap)
    for k,v in cmap.items():
        if v.startswith('uni'):
            v = chr(int(v[3:],16))
            try:
                sfx = unicodedata.name(v)
            except ValueError as e:
                sfx = None
        else:
            sfx = unicodedata.name(v[0])
        print(k,"=>",v,'|',sfx)

if len(sys.argv) < 2:
    print("usage: python3 show_font_table.py {TTF filename}")
    sys.exit(-1)
else:
    show_font_table(sys.argv[1])
