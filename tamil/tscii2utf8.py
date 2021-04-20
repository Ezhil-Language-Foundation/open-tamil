#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai

from sys import argv, exit, version
import tamil
import codecs

PYTHON3 = version[0] > "2"


def usage():
    return u"tscii2utf8.py <filename-1> <filename-2> ... "


if __name__ == u"__main__":
    if not argv[1:]:
        print(usage())
        exit(-1)

    for fname in argv[1:]:
        try:
            with codecs.open(fname, "r", "utf-8") as fileHandle:
                output = tamil.tscii.convert_to_unicode(fileHandle.read())
                if PYTHON3:
                    print(output)
                else:
                    print(output.encode("utf-8"))
        except Exception as fileOrConvException:
            print(
                u"tscii2utf8 error - file %s could not be processed due to - %s"
                % (fname, str(fileOrConvException))
            )
