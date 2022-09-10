from opentamiltests import *
from unittest import TestCase

from transliterate.helper import convert_ISO15919_to_unicode

class TestISO15919(TestCase):
    def test_convert_iso15919_to_unicode(self):
        actual = convert_ISO15919_to_unicode(r'cāmi. citamparaṉār nūṟ kaḷañciyam')
        #expected = 'சாமி. சிதம்பரனார் நூற் களஞ்சியம்'
        expected = 'சாமி. சிதம்பரṉஆர் நூṟ களஞ்சியம்'
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()