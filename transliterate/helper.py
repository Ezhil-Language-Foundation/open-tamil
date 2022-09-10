# (C) 2022 எழில் மொழி அறக்கட்டளை
# இந்த நிரல் ஓப்பன்-தமிழ் திரட்டின் ஒரு பகுதி.
# தமிழ் மொழி ஒலிவழி எழுத்துவடிவமைப்பு சென்னை பல்கலைக்கழகத்தின் தரபத்தில் வருவது.
# நிரலாசிரியர் - முத்து அண்ணாமலை

from transliterate.algorithm import reverse_transliteration_table, Iterative
from transliterate.ISO import ReverseTransliteration

def convert_ISO15919_to_unicode(roman_text):
    """ Tamil ISO 15919 standard is often used to convert Tamil text to romanized text.
    This specially the case in many cataloguing systems. Example:
    https://catalog.hathitrust.org/Record/6133883. Generaly Tamil public is not
    familiar with this standard.

    This routine can take the ISO 15919 romanized text and convert it into Tamil unicode text.

    usage: convert_ISO15919_to_unicode('cāmi. citamparaṉār nūṟ kaḷañciyam')
    should return Tamil text in Unicode: 'சாமி. சிதம்பரனார் நூற் களஞ்சியம்'
    """
    rev_table = reverse_transliteration_table(ReverseTransliteration.table)
    tamil_str = Iterative.transliterate(rev_table, roman_text)
    return tamil_str
