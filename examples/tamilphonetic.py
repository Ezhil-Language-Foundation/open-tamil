#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai

from sys import argv, exit, stdin
from cmd import Cmd

import codecs, sys
#sys.stdin = codecs.getreader('utf-8')(sys.stdin)
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from transliterate import *

def usage():
    return u"tamilphonetic.py [[-stdin] [<filename-1>] [<filename-2>] ...] "

class CmdTransliterate( Cmd ):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = u"azhagi>> "
        self.phonetic_table = azhagi.Transliteration.table        

    def do_EOF(self,line):
        print("\n")
        return True
    
    def default(self,line):
        if ( line == "exit" ):
            exit(0)
        print( iterative_transliterate(self.phonetic_table,line) )
        return

if __name__ == u"__main__":
    if not argv[1:]:
        CmdTransliterate().cmdloop()
    
    for fname in argv[1:]:
        try:
            if fname == u"-stdin":
                CmdTransliterate().cmdloop()
                exit(0)
            with open(fname) as fileHandle:
                phonetic_table = azhagi.Transliteration.table
                output = iterative_transliterate( phonetic_table, fileHandle.read() )
                print( output )
        except Exception as fileOrConvException:
            print(u"tamilphonetic.py error - file %s could not be processed due to - %s"%(fname,str(fileOrConvException)))
            raise fileOrConvException
