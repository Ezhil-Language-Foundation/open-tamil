# (C) 2016 Muthiah Annamalai
# This code is part of open-tamil project

import sys
import re
import codecs
import tamil

def do():
    dst = codecs.open(sys.argv[2],"w","utf-8")
    fname = sys.argv[1]
    with codecs.open(fname,"r","utf-8") as fp:
        lines =fp.readlines()
    for line in lines:
        parts = re.split('\s+',line)
        tapart = []
        ta_part = filter( tamil.utf8.istamil_prefix, parts )
        rest_part = filter( lambda x:  not tamil.utf8.istamil_prefix(x), parts )
        dst.write(u"%s   %s\n"%(re.sub(u"\-$",u" ",u"-".join(rest_part)),u"-".join(ta_part)))
    dst.close()

if __name__ == u"__main__":
    if len(sys.argv) < 3:
        print("Usage: flipline.py <file-src> <file-dest>")
        sys.exit(0)
    do()
