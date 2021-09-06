# (C) 2016 Muthiah Annamalai
# This code is part of open-tamil project

import codecs
import re
import sys

import tamil


def do():
    dst = codecs.open(sys.argv[2], "w", "utf-8")
    fname = sys.argv[1]
    with codecs.open(fname, "r", "utf-8") as fp:
        lines = fp.readlines()
    for line in lines:
        parts = re.split("\s+", line)
        tapart = []
        ta_part = list(filter(tamil.utf8.istamil_prefix, parts))
        rest_part = [x for x in parts if not tamil.utf8.istamil_prefix(x)]
        dst.write(
            "%s   %s\n" % (re.sub("\-$", " ", "-".join(rest_part)), "-".join(ta_part))
        )
    dst.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: flipline.py <file-src> <file-dest>")
        sys.exit(0)
    do()
