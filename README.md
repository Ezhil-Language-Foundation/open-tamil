open-tamil [![Build Status](https://travis-ci.org/arcturusannamalai/open-tamil.png)](https://travis-ci.org/arcturusannamalai/open-tamil)
==========

Open Source Tamil Tools

Software
========

#tamil
open-tamil rovides Python package 'tamil' with ability to,

1. map unicode code-points to Tamil letters - basic but important parsing - in a routine called get_letters from a Tamil word
2. work with vowels (uyir) and consonants (mei), compound, uyir-mei letters
3. reverse letters in Tamil word

#transliterate
the python package 'transliterate' provides for commonly used transliteration
phonetic schemes like,

1. Azhagi - phonetic maps for all Tamil letters - many -> one supporting multiple form inputs
2. Jaffna Library - phonetic maps for all Tamil letters - one->one
3. Combinational layout - based on phonetic mapping of vowel+consonant

where you can supply English text, which phonetically encodes Tamil, and then receive Unicode encoded, in a best-effort algorithm for the longest phonetic match.
*C-tamil*
the package under C-tamil provides some of the same functionality as Python 'tamil' but in ISO-C for C/C++ use.

#Onscreen Keyboard
Open-tamil provides the keyboard layout in the file 'keyboard/tamil.js' for they jQuery UI plugin.

#Language Models
Basic support for letter unigram, bigram models using UTF-8 based corpora are supported in the package 'ngram/'
which supports unigram model at the moment. More complex language models are expected to be developed soon.

Examples
========
Open-Tamil is a set of Python libraries which can help your application - web, system software, GUI on desktop etc. support Tamil text processing, inputs etc.

Open-Tamil is still a basic collection of tools - its not complete yet. We have keyboard layouts, converters to change old encoding to UTF-8, N-gram language models, transliterators etc.

Examples for using Python Open-Tamil are found in https://github.com/arcturusannamalai/open-tamil/tree/master/test

Goals
=====
Goal of this package is to collect and develop open-source licensed Tamil tools, in one location that provide the following,

1. Unicode standard tools for Tamil - provide various tools for Tamil Unicode development. Currently TSCII, UTF8 encoding tables are provided. TAB, TAM, and other layouts are planned to be addded.
2. Access Unicode Tamil letters, vowels and consonants.
3. Breakdown Tamil glyphs and unicode code-points into Tamil letter representations - collation
4. Tools for navigating a corpus of data, build word frequency, prediction tables etc.
5. Conversion from various encodings. e.g. TSCII to Unicode etc. We hope eventually to converts between the other major Tamil encodings like TAB, TAM, Bamini (*insert-your-favortie-font-encoding*) into Tamil Unicode encoding.

While most of tools in this package will be in Python 2.6. or later, I am open to other open-source language source code contributions.

About
=====
Tamil is classical language primarily spoken in South India.
