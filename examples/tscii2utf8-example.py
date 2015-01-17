#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai

from sys import argv, exit
import tamil
import sys



def usage():
    return u"tscii2utf8.py <source-file> <destination-file> "

if __name__ == u"__main__":
    if not argv[1:]:
        print( usage() )
        exit(-1)

    try:	
	    source_file = argv[1]
	    destination_file = argv[2]	
            with open(source_file) as fileHandle:
                print("working on " + source_file + "\n")
                
                output = tamil.tscii.convert_to_unicode( fileHandle.read() )
		print( output )
                fi = open(destination_file,"w")
                fi.write(output.encode('utf-8'))
                fi.close()
		print("TSCII to UTF8 conversion completed. Check the file " + destination_file)

    except Exception as fileOrConvException:
            print(u"tscii2utf8 error - file %s could not be processed due to - %s"%(fname,str(fileOrConvException)))
