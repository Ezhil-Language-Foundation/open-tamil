# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

import codecs

# setup the paths
from opentamiltests import *
import tamil
from ngram.Corpus import Corpus
from ngram import LetterModels

import tamil.utf8 as utf8

class Letters(unittest.TestCase):
    def test_data_op(self):
        dat = '\x97\xC8\xA2\xD7\xC3\xA2'
        output = tamil.tscii.convert_to_unicode( dat )
        if ( LINUX ):
            print(output)
    
    def test_project_MADURAI(self):
        fname = "data/project_madurai_tscii.txt"
        fexact = "data/project_madurai_utf8.txt"
    
        # expected 
        with codecs.open( fexact , 'r', 'utf-8') as fileHandle:
            exact = fileHandle.read()            
        
        # convert 
        with codecs.open(fname,'r','utf-8') as fileHandle:
            output = tamil.tscii.convert_to_unicode( fileHandle.read() )
            
        if ( LINUX ):
            print(len( output))
            print(len( exact ))

        ta_parts = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
        wlen_expected = [5, 5, 3, 2, 4, 2, 3, 2, 3, 8, 2, 5]
        wlen = map( lambda x: len( tamil.utf8.get_letters( x) ), ta_parts)
        if PYTHON3:
            wlen = list(wlen)
        if ( LINUX ): 
            print(wlen)
            print(wlen_expected)
        self.assertEqual( wlen, wlen_expected )

if __name__ == "__main__":
    unittest.main()
