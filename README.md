open-tamil [![Build Status](https://travis-ci.org/arcturusannamalai/open-tamil.png)](https://travis-ci.org/arcturusannamalai/open-tamil) [![Documentation Status](https://readthedocs.org/projects/open-tamil/badge/)](http://open-tamil.readthedocs.org/en/latest/) [![Coverage Status](https://coveralls.io/repos/arcturusannamalai/open-tamil/badge.svg)](https://coveralls.io/r/arcturusannamalai/open-tamil)
==========

Open Source Tamil Tools and Tamil Library for Python 2, 3
திற மூல தமிழ் கருவிகள்

Software ( மென்பொருள் )
=====================
Python  Packages ( பைதான் தொகுப்புகள்  )
===================================
'tamil' என்ற பைத்தன் தொகுப்பை வழங்குகிரோம்

#tamil
open-tamil provides Python package 'tamil' with ability to,

1. map unicode code-points to Tamil letters - basic but important parsing - in a routine called get_letters from a Tamil word
   '''tamil.utf8.get_letters''' and '''tamil.utf8.get_letters_iterable''' API return the Tamil letters from the unicode points of a normalized unicode string.
   These routines are written with efficiency in mind, and tested for accuracy.
   
2. work with vowels (uyir) and consonants (mei), compound, uyir-mei letters
3. reverse letters in Tamil word
4. numeral - convert a given number (integer) into a numeral in Indian or American based system.
   e.g. following call will return the string
        >> '''tamil.numeral.num2tamilstr_american( long(1e7) )'''  
        u"பத்து மில்லியன்",

#txt2unicode
Tamil Text Encode to Unicode Converter and vice versa.
If you Don't you know what your Tamil text encoding, don't worry; the '''tamil.txt2unicode.auto2unicode''' function will find it and convert to unicode for you. 
யுனிகோட் மாற்றி மற்றும் மாறாகவும் தமிழ் உரை குறியாக்கம்.
நீங்கள் என்ன உங்கள் தமிழ் உரை குறியீட்டு தெரியாது என்றால், கவலைப்பட வேண்டாம்; '' 'tamil.txt2unicode.auto2unicode' '' செயல்பாடு அது கண்டுபிடிக்கும் & நீங்கள் யுனிகோட் மாற்ற வேண்டும்.

Right now, it supports with 25 Tamil encodes. Read more details about [txt2unicode](tamil/txt2unicode/README.md) and [limitation](examples/txt2unicode/encodes_chars/README.md) of `auto2unicode` and `unicode2auto`
இப்போது, அது 25 தமிழ் குறியாக்கம் கொண்ட ஆதரிக்கிறது. 'auto2unicode' மற்றும் 'unicode2auto' என்ற [txt2unicode] (தமிழ் / txt2unicode / README.md) மற்றும் [குறைபாடு] (உதாரணங்கள் / txt2unicode / encodes_chars / README.md) பற்றி மேலும் விவரங்களை படிக்க

#txt2ipa
Tamil Unicode Text to International Phonetic Alphabet (IPA) converter 
Read more details about [txt2ipa](tamil/txt2ipa/README.md)
சர்வதேச (ஐபிஏ) மாற்றி, தமிழ் யுனிகோட் உரை; பற்றி மேலும் விவரங்களை படிக்க (தமிழ் / txt2ipa / README.md) 

#transliterate
the python package `transliterate` provides for commonly used transliteration
phonetic schemes like,

1. Azhagi - phonetic maps for all Tamil letters - many -> one supporting multiple form inputs
2. Jaffna Library - phonetic maps for all Tamil letters - one->one
3. Combinational layout - based on phonetic mapping of vowel+consonant

where you can supply English text, which phonetically encodes Tamil, and then receive Unicode encoded, in a best-effort algorithm for the longest phonetic match.

`transliterate` தொகுப்பு பொதுவாக பயன்படுத்தப்படும் ஒலிபெயர்ப்பு வழங்குகிறது; மூன்று வகையானவை
1. அழகி - தமிழ் கடிதங்கள் ஒலிப்பு வரைபடங்கள் - பல -> ஒரு ஆதரவு பல வடிவம் உள்ளீடுகள்
2. யாழ்ப்பாண நூலகம் - தமிழ் கடிதங்கள் ஒலிப்பு வரைபடங்கள் - ஒன்று> ஒரு
3. பலதரப்பட்ட அமைப்பு - உயிர் + மெய் உச்சரிப்பு மேப்பிங் அடிப்படையில் 

*C-tamil*
the package under C-tamil provides some of the same functionality as Python 'tamil' but in ISO-C for C/C++ use.
* சி தமிழ் *
பைதான் 'தமிழ்' தொகுப்பு கீழ்  சிலதும் ஐஎஸ்ஓ 'சி தமிழ்'  சி / சி++ பயன்படுத்த கிடைக்கும்.

#Onscreen Keyboard
Open-tamil provides the keyboard layout in the file `keyboard/tamil.js` for they jQuery UI plugin.
'tamil.js' விசைப்பலகை அமைப்பை வழங்குகிறது. 

#Language Models (மாதிரிகள்)
Basic support for letter unigram, bigram models using UTF-8 based corpora are supported in the package 'ngram/'
which supports unigram model at the moment. More complex language models are expected to be developed soon.
எழுத்து unigram அடிப்படை ஆதரவு, bigram மாதிரிகள், UTF-8 அடிப்படையில் சொற்கிடங்கின் பயன்படுத்தி தொகுப்பு ஆதரவு 'Ngram /'
எந்த நேரத்தில் மாதிரி unigram ஆதரிக்கிறது. மிகவும் நுணுக்கமான மொழி மாதிரிகள் விரைவில் அபிவிருத்தி செய்யப்படும் என எதிர்பார்க்கப்படுகிறது.

Installation
==========
Installation from Python Package Index is also recommended, following the commands,
```
$ pip install open-tamil
```

Examples (உதாரணங்கள்)
===================
Open-Tamil is a set of Python libraries which can help your application - web, system software, GUI on desktop etc. support Tamil text processing, inputs etc.

Open-Tamil is still a basic collection of tools - its not complete yet. We have keyboard layouts, converters to change old encoding to UTF-8, N-gram language models, transliterators etc.

Examples for using Python Open-Tamil are found in https://github.com/arcturusannamalai/open-tamil/tree/master/test

உள்ளீடுகள் முதலியன டெஸ்க்டாப் வலை அமைப்பு மென்பொருள், வரைகலை ஆதரவு தமிழ் உரை செயலாக்க - ஓபன் தமிழ் பைதான் உங்கள் விண்ணப்பத்தை உதவும் தொகுப்பு. திறந்த தமிழ் இன்னும் கருவிகள் ஒரு அடிப்படை தொகுப்பு ஆகும் - அதன் இன்னமும் முடிவடையவில்லை. நாம், UTF-8, என்-கிராம் மொழி மாதிரிகள், transliterators முதலியன பழைய முறையை மாற்ற விசைப்பலகை அமைப்பு, மாற்றிகள் வேண்டும். பைதான் ஓபன் தமிழ் பயன்படுத்தி உதாரணங்கள் https://github.com/arcturusannamalai/open-tamil/tree/master/test காணப்படுகின்றன

Goals
=====
Goal of this package is to collect and develop open-source licensed Tamil tools, in one location that provide the following,

1. Unicode standard tools for Tamil - provide various tools for Tamil Unicode development. Currently 25 encodes are supported, read about it [here](tamil/txt2unicode/README.md) 
2. Access Unicode Tamil letters, vowels and consonants.
3. Breakdown Tamil glyphs and unicode code-points into Tamil letter representations - collation
4. Tools for navigating a corpus of data, build word frequency, prediction tables etc.
5. Conversion from various encodings. e.g. TSCII to Unicode etc. We hope eventually to converts between the other major Tamil encodings like TAB, TAM, Bamini (*insert-your-favortie-font-encoding*) into Tamil Unicode encoding.
6. Support all of above in Python 2.6.x, 2.7.x as well as in Python3.

While most of tools in this package will be in Python 2.6. or later, we are open to other open-source language source code contributions.

Contributing to Open-Tamil
==========================
1. Please add your code, and unit tests under MIT, GNU GPL or ASF licenses.
2. Update your code into modules, add unit tests following the Python flake8, pylint standards
3. Please do not mix TABS and SPACES. Use 4-space for Tabs. Use 
4. Make sure your module installed as part of pip package
5. Ensure your code works for Python 2 and 3.

About (பற்றி)
==========
Tamil is classical language primarily spoken in South India.
தமிழ் முதன்மையாக தென் இந்தியாவில் பேசப்படும் பாரம்பரிய மொழி ஆகும்.
