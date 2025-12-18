

# -*- coding: utf-8 -*-
## (C) 2025 Hariharan Umapathi,
from opentamiltests import *
from tamilnlpweb.tamil_nlp_web_api import TamilNLPWeb



class TamilNLPWebTest(unittest.TestCase):
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        self.api = TamilNLPWeb()
        self.assertFalse(self.base_url != None)

    def test_suffix(self):
        wordlist = [u"மலைகள்", u"பாடுதல்", u"ஓடினான்"]
        expected = [u"மலை", u"பாடு", u"ஓடி"]
        stems = [self.ta_stemmer.stemWord(word) for word in wordlist]
        self.assertSequenceEqual(stems, expected)


if __name__ == "__main__":
    unittest.main()
