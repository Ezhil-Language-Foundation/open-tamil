#!python
# -*- coding: utf-8 -*-
# (C) 2013-2018 Muthiah Annamalai
import sys
import imp

try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3

imp.reload(sys)
# sys.setdefaultencoding('utf-8')

from sys import argv, exit
import tamil
import sys
import codecs


def usage():
    return "tamiltscii2utf8.py <source-file> <destination-file> "


if __name__ == "__main__":
    if not argv[1:]:
        print((usage()))
        exit(-1)

    try:
        source_file = argv[1]
        destination_file = argv[2]
        with open(source_file, "rb") as fileHandle:
            print(("working on " + source_file + "\n"))
            output = tamil.tscii.convert_to_unicode(fileHandle.read())
            # print( output )
            fi = codecs.open(destination_file, "w", "UTF-8")
            fi.write(output.encode("utf-8"))
            fi.close()
        print(
            ("TSCII to UTF8 conversion completed. Check the file " + destination_file)
        )
    except Exception as fileOrConvException:
        print(
            (
                    "tamiltscii2utf8 error - file %s could not be processed due to - %s"
                    % (source_file, str(fileOrConvException))
            )
        )
