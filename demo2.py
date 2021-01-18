from pprint import pprint

import tamil
from tamilstemmer import TamilStemmer

kv = [('நாற்பத்தி ஐந்து',45),('ஓர் ஆயிரத்து எழுநூற்று இருபத்தொன்பது',1729),
('ஓர் ஆயிரத்து ஒன்று',1001)]

stemmer = TamilStemmer()
for k,v in kv:
    pprint([stemmer.stemWord(word) for word in tamil.utf8.get_words(k)])
#['நாற்பத்தி', 'ஐந்']
#['ஓர்', 'ஆயிர', 'எழுநூற்று', 'இருபத்தொன்']
#['ஓர்', 'ஆயிர', 'ஒன்று']
