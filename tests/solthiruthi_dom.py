# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

from opentamiltests import *
from solthiruthi.dom import WordEntity, Document

import os

from tamil import utf8

class DOMTest(unittest.TestCase):
    def test_entity(self):
        word = u"nuthin"
        q = WordEntity(word,row=5,col=6)
        self.assertEqual(q.word,word)
        self.assertEqual(q.letters,utf8.get_letters(u"nuthin"))
        self.assertEqual((q.row, q.col),(5,6))
        self.assertTrue(q.isWord())

class DocTest(unittest.TestCase):
    def test_mkdoc(self):
       d = Document(os.path.join(os.getcwd(),"data","richmond.txt"))
       self.assertTrue(isinstance(d,Document))

if __name__ == "__main__":
    unittest.main()
