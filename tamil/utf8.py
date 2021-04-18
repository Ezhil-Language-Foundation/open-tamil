## This Python file uses the following encoding: utf-8
##
## (C) 2007, 2008, 2013, 2015, 2016-2020 Muthiah Annamalai <ezhillang@gmail.com>
## (C) 2013 msathia <msathia@gmail.com>
##
## This file is dual licensed - originally GPL v3 from Ezhil, and
## then as part of open-tamil package in MIT license.
##
## Licensed under GPL Version 3

import abc
import operator
import re
import string
from copy import copy
from sys import version

PYTHON3 = version > "3"
assert PYTHON3, "PYTHON3 required to operate Open-Tamil library"
import functools

## constants
TA_ACCENT_LEN = 13  # 12 + 1
TA_AYUDHA_LEN = 1
TA_UYIR_LEN = 12
TA_MEI_LEN = 18
TA_AGARAM_LEN = 18
TA_SANSKRIT_LEN = 6
TA_UYIRMEI_LEN = 216
TA_GRANTHA_UYIRMEI_LEN = 24 * 12
TA_LETTERS_LEN = 247 + 6 * 12 + 22 + 4 - TA_AGARAM_LEN - 4  # 323


def to_unicode_repr(_letter):
    """helpful in situations where browser/app may recognize Unicode encoding
    in the \u0b8e type syntax but not actual unicode glyph/code-point"""
    # Python 2-3 compatible
    return "u'" + "".join(["\\u%04x" % ord(l) for l in _letter]) + "'"


def letters_to_py(_letters):
    """ return list of letters e.g. uyir_letters as a Python list """
    return "[u'" + "',u'".join(_letters) + "']"


# List of letters you can use
uyir_letters = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
vowel_a = "அ"
vowel_aa = "ஆ"
vowel_i = "இ"
vowel_ii = "ஈ"
vowel_u = "உ"
vowel_uu = "ஊ"
vowel_e = "எ"
vowel_ee = "ஏ"
vowel_ai = "ஐ"
vowel_o = "ஒ"
vowel_oo = "ஓ"
vowel_au = "ஔ"
aytham_letter = "ஃ"
ayudha_letter = aytham_letter

kuril_letters = ["அ", "இ", "உ", "எ", "ஒ"]
nedil_letters = ["ஆ", "ஈ", "ஊ", "ஏ", "ஓ", "ஐ", "ஔ"]
dipthong_letters = ["ஐ", "ஔ"]

pronoun_letters = ["அ", "இ", "உ"]
suttezhuththu = pronoun_letters

questionsuffix_letters = ["ஆ", "ஏ", "ஓ"]
vinaaezhuththu = questionsuffix_letters

vallinam_letters = ["க்", "ச்", "ட்", "த்", "ப்", "ற்"]
mellinam_letters = ["ங்", "ஞ்", "ண்", "ந்", "ம்", "ன்"]
idayinam_letters = ["ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"]

mei_letters = [
    "க்",
    "ச்",
    "ட்",
    "த்",
    "ப்",
    "ற்",
    "ஞ்",
    "ங்",
    "ண்",
    "ந்",
    "ம்",
    "ன்",
    "ய்",
    "ர்",
    "ல்",
    "வ்",
    "ழ்",
    "ள்",
]

accent_symbols = [
    "", "ா", "ி", "ீ", "ு", "ூ", "ெ", "ே", "ை", "ொ", "ோ", "ௌ", "ஃ"
]

accent_aa = accent_symbols[1]
accent_i = accent_symbols[2]
accent_u = accent_symbols[3]
accent_uu = accent_symbols[4]
accent_e = accent_symbols[5]
accent_ee = accent_symbols[6]
accent_ai = accent_symbols[7]
accent_o = accent_symbols[8]
accent_oo = accent_symbols[9]
accent_au = accent_symbols[10]

pulli_symbols = ["்"]

agaram_letters = [
    "க",
    "ச",
    "ட",
    "த",
    "ப",
    "ற",
    "ஞ",
    "ங",
    "ண",
    "ந",
    "ம",
    "ன",
    "ய",
    "ர",
    "ல",
    "வ",
    "ழ",
    "ள",
]
mayangoli_letters = ["ண", "ன", "ந", "ல", "ழ", "ள", "ர", "ற"]

consonant_ka = "க"
consonant_nga = "ங"
consonant_ca = "ச"
consonant_ja = "ஜ"
consonant_nya = "ஞ"
consonant_tta = "ட"
consonant_nna = "ண"
consonant_nnna = "ன"
consonant_ta = "த"
consonant_tha = "த"
consonant_na = "ந"
consonant_pa = "ப"
consonant_ma = "ம"
consonant_ya = "ய"
consonant_ra = "ர"
consonant_rra = "ற"
consonant_la = "ல"
consonant_lla = "ள"
consonant_llla = "ழ"
consonant_zha = "ழ"
consonant_va = "வ"

sanskrit_letters = ["ஶ", "ஜ", "ஷ", "ஸ", "ஹ", "க்ஷ"]
sanskrit_mei_letters = ["ஶ்", "ஜ்", "ஷ்", "ஸ்", "ஹ்", "க்ஷ்"]

grantha_mei_letters = copy(mei_letters)
grantha_mei_letters.extend(sanskrit_mei_letters)

grantha_agaram_letters = copy(agaram_letters)
grantha_agaram_letters.extend(sanskrit_letters)

uyirmei_letters = [
    "க",
    "கா",
    "கி",
    "கீ",
    "கு",
    "கூ",
    "கெ",
    "கே",
    "கை",
    "கொ",
    "கோ",
    "கௌ",
    "ச",
    "சா",
    "சி",
    "சீ",
    "சு",
    "சூ",
    "செ",
    "சே",
    "சை",
    "சொ",
    "சோ",
    "சௌ",
    "ட",
    "டா",
    "டி",
    "டீ",
    "டு",
    "டூ",
    "டெ",
    "டே",
    "டை",
    "டொ",
    "டோ",
    "டௌ",
    "த",
    "தா",
    "தி",
    "தீ",
    "து",
    "தூ",
    "தெ",
    "தே",
    "தை",
    "தொ",
    "தோ",
    "தௌ",
    "ப",
    "பா",
    "பி",
    "பீ",
    "பு",
    "பூ",
    "பெ",
    "பே",
    "பை",
    "பொ",
    "போ",
    "பௌ",
    "ற",
    "றா",
    "றி",
    "றீ",
    "று",
    "றூ",
    "றெ",
    "றே",
    "றை",
    "றொ",
    "றோ",
    "றௌ",
    "ஞ",
    "ஞா",
    "ஞி",
    "ஞீ",
    "ஞு",
    "ஞூ",
    "ஞெ",
    "ஞே",
    "ஞை",
    "ஞொ",
    "ஞோ",
    "ஞௌ",
    "ங",
    "ஙா",
    "ஙி",
    "ஙீ",
    "ஙு",
    "ஙூ",
    "ஙெ",
    "ஙே",
    "ஙை",
    "ஙொ",
    "ஙோ",
    "ஙௌ",
    "ண",
    "ணா",
    "ணி",
    "ணீ",
    "ணு",
    "ணூ",
    "ணெ",
    "ணே",
    "ணை",
    "ணொ",
    "ணோ",
    "ணௌ",
    "ந",
    "நா",
    "நி",
    "நீ",
    "நு",
    "நூ",
    "நெ",
    "நே",
    "நை",
    "நொ",
    "நோ",
    "நௌ",
    "ம",
    "மா",
    "மி",
    "மீ",
    "மு",
    "மூ",
    "மெ",
    "மே",
    "மை",
    "மொ",
    "மோ",
    "மௌ",
    "ன",
    "னா",
    "னி",
    "னீ",
    "னு",
    "னூ",
    "னெ",
    "னே",
    "னை",
    "னொ",
    "னோ",
    "னௌ",
    "ய",
    "யா",
    "யி",
    "யீ",
    "யு",
    "யூ",
    "யெ",
    "யே",
    "யை",
    "யொ",
    "யோ",
    "யௌ",
    "ர",
    "ரா",
    "ரி",
    "ரீ",
    "ரு",
    "ரூ",
    "ரெ",
    "ரே",
    "ரை",
    "ரொ",
    "ரோ",
    "ரௌ",
    "ல",
    "லா",
    "லி",
    "லீ",
    "லு",
    "லூ",
    "லெ",
    "லே",
    "லை",
    "லொ",
    "லோ",
    "லௌ",
    "வ",
    "வா",
    "வி",
    "வீ",
    "வு",
    "வூ",
    "வெ",
    "வே",
    "வை",
    "வொ",
    "வோ",
    "வௌ",
    "ழ",
    "ழா",
    "ழி",
    "ழீ",
    "ழு",
    "ழூ",
    "ழெ",
    "ழே",
    "ழை",
    "ழொ",
    "ழோ",
    "ழௌ",
    "ள",
    "ளா",
    "ளி",
    "ளீ",
    "ளு",
    "ளூ",
    "ளெ",
    "ளே",
    "ளை",
    "ளொ",
    "ளோ",
    "ளௌ",
]

tamil247 = [ayudha_letter]
tamil247.extend(uyir_letters)
tamil247.extend(mei_letters)
tamil247.extend(uyirmei_letters)

# Ref: https://en.wikipedia.org/wiki/Tamil_numerals
# tamil digits : Apart from the numerals (0-9), Tamil also has numerals for 10, 100 and 1000.
tamil_digit_1to10 = ["௦", "௧", "௨", "௩", "௪", "௫", "௬", "௭", "௮", "௯", "௰"]
tamil_digit_100 = "௱"
tamil_digit_1000 = "௲"

tamil_digits = [(num, digit)
                for num, digit in zip(range(0, 11), tamil_digit_1to10)]
tamil_digits.extend([(100, tamil_digit_100), (1000, tamil_digit_1000)])

# tamil symbols
_day = "௳"
_month = "௴"
_year = "௵"
_debit = "௶"
_credit = "௷"
_rupee = "௹"
_numeral = "௺"
_sri = "\u0bb6\u0bcd\u0bb0\u0bc0"  # SRI - ஶ்ரீ
_ksha = "\u0b95\u0bcd\u0bb7"  # KSHA - க்ஷ
_ksh = "\u0b95\u0bcd\u0bb7\u0bcd"  # KSH - க்ஷ்
_indian_rupee = "₹"
tamil_symbols = [
    _day,
    _month,
    _year,
    _debit,
    _credit,
    _rupee,
    _numeral,
    _sri,
    _ksha,
    _ksh,
    _indian_rupee,
]

## total tamil letters in use, including sanskrit letters
tamil_letters = [
    ## /* Uyir */
    "அ",
    "ஆ",
    "இ",
    "ஈ",
    "உ",
    "ஊ",
    "எ",
    "ஏ",
    "ஐ",
    "ஒ",
    "ஓ",
    "ஔ",
    ##/* Ayuda Ezhuthu */
    "ஃ",
    ## /* Mei */
    "க்",
    "ச்",
    "ட்",
    "த்",
    "ப்",
    "ற்",
    "ஞ்",
    "ங்",
    "ண்",
    "ந்",
    "ம்",
    "ன்",
    "ய்",
    "ர்",
    "ல்",
    "வ்",
    "ழ்",
    "ள்",
    ## /* Agaram */
    ## "க","ச","ட","த","ப","ற","ஞ","ங","ண","ந","ம","ன","ய","ர","ல","வ","ழ","ள",
    ## /* Sanskrit (Vada Mozhi) */
    ## "ஜ","ஷ", "ஸ","ஹ",
    ##/* Sanskrit (Mei) */
    "ஜ்",
    "ஷ்",
    "ஸ்",
    "ஹ்",
    ## /* Uyir Mei */
    "க",
    "கா",
    "கி",
    "கீ",
    "கு",
    "கூ",
    "கெ",
    "கே",
    "கை",
    "கொ",
    "கோ",
    "கௌ",
    "ச",
    "சா",
    "சி",
    "சீ",
    "சு",
    "சூ",
    "செ",
    "சே",
    "சை",
    "சொ",
    "சோ",
    "சௌ",
    "ட",
    "டா",
    "டி",
    "டீ",
    "டு",
    "டூ",
    "டெ",
    "டே",
    "டை",
    "டொ",
    "டோ",
    "டௌ",
    "த",
    "தா",
    "தி",
    "தீ",
    "து",
    "தூ",
    "தெ",
    "தே",
    "தை",
    "தொ",
    "தோ",
    "தௌ",
    "ப",
    "பா",
    "பி",
    "பீ",
    "பு",
    "பூ",
    "பெ",
    "பே",
    "பை",
    "பொ",
    "போ",
    "பௌ",
    "ற",
    "றா",
    "றி",
    "றீ",
    "று",
    "றூ",
    "றெ",
    "றே",
    "றை",
    "றொ",
    "றோ",
    "றௌ",
    "ஞ",
    "ஞா",
    "ஞி",
    "ஞீ",
    "ஞு",
    "ஞூ",
    "ஞெ",
    "ஞே",
    "ஞை",
    "ஞொ",
    "ஞோ",
    "ஞௌ",
    "ங",
    "ஙா",
    "ஙி",
    "ஙீ",
    "ஙு",
    "ஙூ",
    "ஙெ",
    "ஙே",
    "ஙை",
    "ஙொ",
    "ஙோ",
    "ஙௌ",
    "ண",
    "ணா",
    "ணி",
    "ணீ",
    "ணு",
    "ணூ",
    "ணெ",
    "ணே",
    "ணை",
    "ணொ",
    "ணோ",
    "ணௌ",
    "ந",
    "நா",
    "நி",
    "நீ",
    "நு",
    "நூ",
    "நெ",
    "நே",
    "நை",
    "நொ",
    "நோ",
    "நௌ",
    "ம",
    "மா",
    "மி",
    "மீ",
    "மு",
    "மூ",
    "மெ",
    "மே",
    "மை",
    "மொ",
    "மோ",
    "மௌ",
    "ன",
    "னா",
    "னி",
    "னீ",
    "னு",
    "னூ",
    "னெ",
    "னே",
    "னை",
    "னொ",
    "னோ",
    "னௌ",
    "ய",
    "யா",
    "யி",
    "யீ",
    "யு",
    "யூ",
    "யெ",
    "யே",
    "யை",
    "யொ",
    "யோ",
    "யௌ",
    "ர",
    "ரா",
    "ரி",
    "ரீ",
    "ரு",
    "ரூ",
    "ரெ",
    "ரே",
    "ரை",
    "ரொ",
    "ரோ",
    "ரௌ",
    "ல",
    "லா",
    "லி",
    "லீ",
    "லு",
    "லூ",
    "லெ",
    "லே",
    "லை",
    "லொ",
    "லோ",
    "லௌ",
    "வ",
    "வா",
    "வி",
    "வீ",
    "வு",
    "வூ",
    "வெ",
    "வே",
    "வை",
    "வொ",
    "வோ",
    "வௌ",
    "ழ",
    "ழா",
    "ழி",
    "ழீ",
    "ழு",
    "ழூ",
    "ழெ",
    "ழே",
    "ழை",
    "ழொ",
    "ழோ",
    "ழௌ",
    "ள",
    "ளா",
    "ளி",
    "ளீ",
    "ளு",
    "ளூ",
    "ளெ",
    "ளே",
    "ளை",
    "ளொ",
    "ளோ",
    "ளௌ"
    ##/* Sanskrit Uyir-Mei */
    ,
    "ஶ",
    "ஶா",
    "ஶி",
    "ஶீ",
    "ஶு",
    "ஶூ",
    "ஶெ",
    "ஶே",
    "ஶை",
    "ஶொ",
    "ஶோ",
    "ஶௌ",
    "ஜ",
    "ஜா",
    "ஜி",
    "ஜீ",
    "ஜு",
    "ஜூ",
    "ஜெ",
    "ஜே",
    "ஜை",
    "ஜொ",
    "ஜோ",
    "ஜௌ",
    "ஷ",
    "ஷா",
    "ஷி",
    "ஷீ",
    "ஷு",
    "ஷூ",
    "ஷெ",
    "ஷே",
    "ஷை",
    "ஷொ",
    "ஷோ",
    "ஷௌ",
    "ஸ",
    "ஸா",
    "ஸி",
    "ஸீ",
    "ஸு",
    "ஸூ",
    "ஸெ",
    "ஸே",
    "ஸை",
    "ஸொ",
    "ஸோ",
    "ஸௌ",
    "ஹ",
    "ஹா",
    "ஹி",
    "ஹீ",
    "ஹு",
    "ஹூ",
    "ஹெ",
    "ஹே",
    "ஹை",
    "ஹொ",
    "ஹோ",
    "ஹௌ",
    "க்ஷ",
    "க்ஷா",
    "க்ஷி",
    "க்ஷீ",
    "க்ஷு",
    "க்ஷூ",
    "க்ஷெ",
    "க்ஷே",
    "க்ஷை",
    "க்ஷொ",
    "க்ஷோ",
    "க்ஷௌ",
]

grantha_uyirmei_letters = copy(tamil_letters[tamil_letters.index("கா") - 1:])


## length of the definitions
def accent_len():
    return TA_ACCENT_LEN  ## 13 = 12 + 1


def ayudha_len():
    return TA_AYUDHA_LEN  ## 1


def uyir_len():
    return TA_UYIR_LEN  ##12


def mei_len():
    return TA_MEI_LEN  ##18


def agaram_len():
    return TA_AGARAM_LEN  ##18


def uyirmei_len():
    return TA_UYIRMEI_LEN  ##216


def tamil_len():
    return len(tamil_letters)


## access the letters
def uyir(idx):
    assert idx >= 0 and idx < uyir_len()
    return uyir_letters[idx]


def agaram(idx):
    assert idx >= 0 and idx < agaram_len()
    return agaram_letters[idx]


def mei(idx):
    assert idx >= 0 and idx < mei_len()
    return mei_letters[idx]


def uyirmei(idx):
    assert idx >= 0 and idx < uyirmei_len()
    return uyirmei_letters[idx]


def mei_to_agaram(in_syllable):
    if in_syllable in grantha_mei_letters:
        mei_pos = grantha_mei_letters.index(in_syllable)
        agaram_a_pos = 0
        syllable = uyirmei_constructed(mei_pos, agaram_a_pos)
        return syllable
    return in_syllable


def uyirmei_constructed(mei_idx, uyir_idx):
    """ construct uyirmei letter give mei index and uyir index """
    idx, idy = mei_idx, uyir_idx
    assert idy >= 0 and idy < uyir_len()
    assert idx >= 0 and idx < 6 + mei_len()
    return grantha_agaram_letters[mei_idx] + accent_symbols[uyir_idx]


def tamil(idx):
    """ retrieve Tamil letter at canonical index from array utf8.tamil_letters """
    assert idx >= 0 and idx < tamil_len()
    return tamil_letters[idx]


# companion function to @tamil()
def getidx(letter):
    for itr in range(0, tamil_len()):
        if tamil_letters[itr] == letter:
            return itr
    raise Exception("Cannot find letter in Tamil arichuvadi")


## useful part of the API:
def istamil_prefix(word):
    """check if the given @word has a tamil prefix. Returns
    either a True/False flag"""
    for letter in tamil_letters:
        if word.find(letter) == 0:
            return True
    return False


def is_tamil_unicode_value(intx: int):
    """
    Quickly check if the given parameter @intx belongs to Tamil Unicode block.
    :param intx:
    :return: True if parameter is in the Tamil Unicode block.
    """
    return (intx >= (2946) and intx <= (3066))


def is_tamil_unicode_codept(x: str):
    """
    Check quickly if the given parameter @x (character) belongs to Tamil Unicode block.
    :param x:
    :return:
    """
    intx = ord(x)
    return is_tamil_unicode_value(intx)


def is_tamil_unicode_predicate(x: str):
    """
    Predicate to work on string @x which is not processed by get_letters() to estimate if it is a Tamil string.
    :param x: text string
    :return: True or False based on @x being Tamil letters exclusively.
    """
    if not is_tamil_unicode_codept(x[0]):
        return False
    return (len(x) > 1 and is_tamil_unicode_predicate(x[1:])) or True


def is_tamil_unicode(sequence):
    # Ref: languagetool-office-extension/src/main/java/org/languagetool/openoffice/TamilDetector.java
    if isinstance(sequence,list):
        return list(map(is_tamil_unicode_predicate, sequence))
    if len(sequence) > 1:
        return list(map(is_tamil_unicode_predicate, get_letters(sequence)))
    return is_tamil_unicode_predicate(sequence)


def has_english(word_in):
    """
    :param word_in: input word was string or list sequence
    :return: return True if word_in has any English letters in the string
    """
    return (not all_tamil(word_in) and len(word_in) > 0
            and any([l in word_in for l in string.ascii_letters]))


def all_tamil(word_in):
    """
    Predicate function
    :param word_in:
    :return:  predicate checks if all letters of the input @word_in are Tamil letters
    """
    if isinstance(word_in, list):
        word = word_in
    else:
        word = get_letters(word_in)
    return all([(letter in tamil_letters) for letter in word])


def has_tamil(word):
    """
    :param word: Input text string
    :return: True if the word has any occurance of any tamil letter """
    # list comprehension is not necessary - we bail at earliest
    for letters in tamil_letters:
        if word.find(letters) >= 0:
            return True
    return False


def istamil(tchar):
    """
    :param tchar: input parameter character
    :return: True if the letter tchar is prefix of
    any of tamil-letter. It suggests we have a tamil identifier"""
    if tchar in tamil_letters:
        return True
    return False


def istamil_alnum(tchar):
    """check if the character is alphanumeric, or tamil.
    This saves time from running through istamil() check."""
    return tchar.isalnum() or istamil(tchar)


def reverse_word(word):
    """ reverse a Tamil word according to letters not unicode-points """
    op = get_letters(word)
    op.reverse()
    return "".join(op)


def is_normalized(text):
    """
    find out if the letters like, "பொ" are written in canonical "ப + ொ"" graphemes then
    return True. If they are written like "ப + ெ + ா" then return False on first occurrence

    :param text: text
    :return: True if letters of word are in canonical representation
    """
    TLEN, idx = len(text), 1
    kaal = "ா"
    Laa = "ள"
    sinna_kombu, periya_kombu = "ெ", "ே"
    kombugal = [sinna_kombu, periya_kombu]

    # predicate measures if the normalization is violated
    def predicate(last_letter, prev_letter):
        if (kaal == last_letter) and (prev_letter in kombugal):
            return True
        if (Laa == last_letter) and (prev_letter == sinna_kombu):
            return True
        return False

    if TLEN < 2:
        return True
    elif TLEN == 2:
        if predicate(text[-1], text[-2]):
            return False
        return True
    idx = TLEN
    a = text[idx - 2]
    b = text[idx - 1]
    while idx >= 0:
        if predicate(b, a):
            return False
        b = a
        idx = idx - 1
        if idx >= 0:
            a = text[idx]
    return True


def _make_set(args):
    return frozenset(args)


grantha_agaram_set = _make_set(grantha_agaram_letters)
accent_symbol_set = _make_set(accent_symbols)
uyir_letter_set = _make_set(uyir_letters)

_GLL = set()
_GLL.update(uyir_letter_set)
_GLL.add(ayudha_letter)
_GLL.update(grantha_agaram_set)
## Split a tamil-unicode stream into
## tamil characters (individuals).
from functools import lru_cache


def copy_lru_decorator(f):
    @lru_cache(16192)
    def f_lru(*args, **kwargs):
        return f(*args, **kwargs)

    def f_copy_lru(*args, **kwargs):
        y = f_lru(*args, **kwargs)
        return copy(y)

    return f_copy_lru


# @copy_lru_decorator
def get_letters(word):
    """Splits the @word into a character-list of tamil/english
    characters present in the stream. This routine provides a robust tokenizer
    for Tamil unicode letters."""
    ta_letters = list()
    not_empty = False
    for c in word:
        if c in _GLL:
            ta_letters.append(c)
            not_empty = True
            continue

        if c in accent_symbol_set:
            if not not_empty:
                # odd situation
                ta_letters.append(c)
                not_empty = True
            else:
                ta_letters[-1] += c
            continue

        cval = ord(c)
        if cval < 256 or not (is_tamil_unicode_value(cval)):
            ta_letters.append(c)
            continue

        if not_empty:
            ta_letters[-1] += c
        else:
            ta_letters.append(c)
            not_empty = True

    return ta_letters


_all_symbols = copy(accent_symbols)
_all_symbols.extend(pulli_symbols)
all_symbol_set = _make_set(_all_symbols)


def get_letters_length(word):
    """ @word என்ற சொல் என்பதன் எழுத்துக்கள் நீளம்."""
    return len(get_letters(word))


# same as get_letters but use as iterable
def get_letters_iterable(word):
    """splits the word into a character-list of tamil/english
    characters present in the stream"""
    WLEN, idx = len(word), 0

    while idx < WLEN:
        c = word[idx]
        if c in uyir_letter_set or c == ayudha_letter:
            idx = idx + 1
            yield c
        elif c in grantha_agaram_set:
            if idx + 1 < WLEN and word[idx + 1] in all_symbol_set:
                c2 = word[idx + 1]
                idx = idx + 2
                yield (c + c2)
            else:
                idx = idx + 1
                yield c
        else:
            idx = idx + 1
            yield c
    return


grantha_uyirmei_splits = {}
for _uyir_idx in range(0, 12):
    for _mei_idx, _mei in enumerate(grantha_mei_letters):
        _uyirmei = uyirmei_constructed(_mei_idx, _uyir_idx)
        grantha_uyirmei_splits[_uyirmei] = [_mei, uyir_letters[_uyir_idx]]


def join_letters_elementary(elements):
    """
    @elements ['க்','ஆ'] input will return 'கா' - this function is complementary of splitMeiUyir(...)
    :param elements: even element list of size >= 2  of vowel or consonants.
    :return: join elementary list of vowel-consonant into conjugates;
    """
    assert len(elements) % 2 == 0, u"input has to be an even numbered list"
    return "".join([
        joinMeiUyir(elements[i], elements[i + 1])
        for i in range(0, len(elements), 2)
    ])


def get_letters_elementary_iterable(word, symmetric=False):
    """
    Generator based @get_letters_elementary function
    :param word: Tamil word
    :param symmetric: boolean
    :return: yield the letter in word
    """
    for letter in get_letters_iterable(word):
        letter_parts = grantha_uyirmei_splits.get(letter, None)
        if letter_parts:
            yield letter_parts[0]
            yield letter_parts[1]
        else:
            if letter in grantha_mei_letters:
                yield letter
                if symmetric:
                    yield None
            else:
                if symmetric:
                    yield None
                yield letter
    return


def get_letters_elementary(word, symmetric=False):
    """
    Get letters elementary function to return @word as Vowel-Consonant splits.
    e.g. ['காகம்' -> 'க்','ஆ','க்','அ','ம்',None] (None is present when @symmetric=True]
    :param word: Tamil word
    :param symmetric: make result list of even number.
    :return: list of V-C splits of @word
    """
    rval = []
    for letter in get_letters(word):
        letter_parts = grantha_uyirmei_splits.get(letter, None)
        if letter_parts:
            rval.append(letter_parts[0])
            rval.append(letter_parts[1])
        else:
            if letter in grantha_mei_letters:
                rval.append(letter)
                if symmetric:
                    rval.append(None)
            else:
                if symmetric:
                    rval.append(None)
                rval.append(letter)
    return rval


def get_words(letters, tamil_only=False):
    """
    Return words in the letter stream.
    :param letters: letters as list or generator
    :param tamil_only: filter for Tamil only words
    :return: list of words
    """
    return [word for word in get_words_iterable(letters, tamil_only)]


def get_words_iterable(letters, tamil_only=False):
    """ given a list of UTF-8 letters section them into words, grouping them at spaces; return
        words in the letter stream; this function operates as generator
    :param letters: letters as list or generator
    :param tamil_only: filter for Tamil only words
    :return: list of words as generator
    """
    # correct algorithm for get-tamil-words
    buf = []
    for idx, let in enumerate(letters):
        if not let.isspace():
            if istamil(let) or (not tamil_only):
                buf.append(let)
        else:
            if len(buf) > 0:
                yield "".join(buf)
                buf = []
    if len(buf) > 0:
        yield "".join(buf)


def get_tamil_words(letters):
    """
    Return Tamil words in the letter stream.
    :param letters: letters as list or generator
    :return: list of words
    """
    if not isinstance(letters, list):
        raise Exception(
            "metehod needs to be used with list generated from 'tamil.utf8.get_letters(...)'"
        )
    return [word for word in get_words_iterable(letters, tamil_only=True)]


def cmp(x, y):
    if x == y:
        return 0
    if x > y:
        return 1
    return -1


# answer if word_a ranks ahead of, or at same level, as word_b in a Tamil dictionary order...
# for use with Python : if a > 0
def compare_words_lexicographic(word_a, word_b):
    """ compare words in Tamil lexicographic order """
    # sanity check for words to be all Tamil
    word_a_in = get_letters(word_a)
    word_b_in = get_letters(word_b)
    if (not all_tamil(word_a_in)) or (not all_tamil(word_b_in)):
        return cmp(word_a_in, word_b_in)
    La = len(word_a_in)
    Lb = len(word_b_in)
    for itr in range(0, min(La, Lb)):
        pos1 = tamil_letters.index(word_a_in[itr])
        pos2 = tamil_letters.index(word_b_in[itr])

        if pos1 != pos2:
            return cmp(pos1, pos2)

    # result depends on if La is shorter than Lb, or 0 if La == Lb  i.e. cmp
    return cmp(La, Lb)


# return a list of ordered-pairs containing positions
# that are common in word_a, and word_b; e.g.
# தேடுக x தடங்கல் -> one common letter க [(2,3)]
# சொல் x   தேடுக -> no common letters []
def word_intersection(word_a, word_b):
    """ return a list of tuples where word_a, word_b intersect """
    positions = []
    word_a_letters = get_letters(word_a)
    word_b_letters = get_letters(word_b)
    for idx, wa in enumerate(word_a_letters):
        for idy, wb in enumerate(word_b_letters):
            if wa == wb:
                positions.append((idx, idy))
    return positions


def unicode_normalize(cplxchar):
    """
    Normalize complex Vowel-Consonant conjugate Tamil letter into a Unicode normalized format;
    e.g. 'க்'+'ஓ' என்பது 'கோ' என்று எழுதுவதே சரியான குறியீடு. 'க்'+'ஏ' = கே + கால் சேர்ப்பதும் யூனிக்கோடில்
    அனுமதிபெற்றாலும் அது சரியானதல்ல; அவ்வகை குறிமுறைகளை சீர்செய்வதே இந்த நிரல்துண்டு.
    :param cplxchar:
    :return:
    """
    Laa = "ள"
    kaal = "ா"
    sinna_kombu_a = "ெ"
    periya_kombu_aa = "ே"
    sinna_kombu_o = "ொ"
    periya_kombu_oo = "ோ"
    kombu_ak = "ௌ"

    lcplx = len(cplxchar)
    if lcplx >= 3 and cplxchar[-1] == Laa:
        if cplxchar[-2] == sinna_kombu_a:
            return cplxchar[:-2] + kombu_ak
    if lcplx >= 2 and cplxchar[-1] == kaal:
        if cplxchar[-2] == sinna_kombu_a:
            return cplxchar[:-2] + sinna_kombu_o
        if cplxchar[-2] == periya_kombu_aa:
            return cplxchar[:-2] + periya_kombu_oo
    # no-op
    return cplxchar


def splitMeiUyir(uyirmei_char):
    """
    This function split uyirmei compound character into mei + uyir characters
    and returns in tuple.

    Input : It must be unicode tamil char, V=vowel, C=char, VC=compound VC.
    Output: (mei,uyir) if it is VC, otherwise return input if it is V, or C.
    Written By : Arulalan.T
    Date : 22.09.2014

    """

    if not isinstance(uyirmei_char, str):
        raise ValueError("Passed input letter '%s' must be unicode, \
                                not just string" % uyirmei_char)

    if (uyirmei_char in mei_letters or uyirmei_char in uyir_letters
            or uyirmei_char in ayudha_letter):
        return uyirmei_char

    if uyirmei_char not in grantha_uyirmei_letters:
        if not is_normalized(uyirmei_char):
            norm_char = unicode_normalize(uyirmei_char)
            rval = splitMeiUyir(norm_char)
            return rval
        raise ValueError("Passed input letter '%s' is not tamil letter" %
                         uyirmei_char)

    idx = grantha_uyirmei_letters.index(uyirmei_char)
    uyiridx = idx % 12
    meiidx = int((idx - uyiridx) / 12)
    return (grantha_mei_letters[meiidx], uyir_letters[uyiridx])


# end of def splitMeiUyir(uyirmei_char):


def joinMeiUyir(mei_char, uyir_char):
    """
    This function join mei character and uyir character, and retuns as
    compound uyirmei unicode character.

    Inputs:
        mei_char : It must be unicode tamil mei char.
        uyir_char : It must be unicode tamil uyir char.

    Written By : Arulalan.T
    Date : 22.09.2014
    """
    if not mei_char:
        return uyir_char
    if not uyir_char:
        return mei_char

    if not isinstance(mei_char, str):
        raise ValueError(
            "Passed input mei character '%s' must be unicode, not just string"
            % mei_char)
    if not isinstance(uyir_char, str) and uyir_char != None:
        raise ValueError(
            "Passed input uyir character '%s' must be unicode, not just string"
            % uyir_char)
    if mei_char not in grantha_mei_letters:
        raise ValueError(
            "Passed input character '%s' is not a tamil mei character" %
            mei_char)
    if uyir_char not in uyir_letters:
        raise ValueError(
            "Passed input character '%s' is not a tamil uyir character" %
            uyir_char)
    if uyir_char:
        uyiridx = uyir_letters.index(uyir_char)
    else:
        return mei_char
    meiidx = grantha_mei_letters.index(mei_char)
    # calculate uyirmei index
    uyirmeiidx = meiidx * 12 + uyiridx
    return grantha_uyirmei_letters[uyirmeiidx]


def classify_letter(letter):
    """
    Report if Tamil letter is kuril, nedil, aytham, vallinam, mellinam, idayinam, uyirmei or grantham letters.
    :param letter: Tamil letter
    :return: class of letter as string.
    """
    if not isinstance(letter, str):
        raise TypeError("Input'%s' must be unicode, not just string" % letter)
    kinds = [
        u"kuril",
        u"nedil",
        u"ayudham",
        u"vallinam",
        u"mellinam",
        u"idayinam",
        u"uyirmei",
        u"tamil_or_grantham",
    ]
    if letter in uyir_letters:
        if letter in kuril_letters:
            return u"kuril"
        elif letter in nedil_letters:
            return u"nedil"
        elif letter == ayudha_letter:
            return "ayudham"
    if letter in mei_letters:
        if letter in mellinam_letters:
            return "mellinam"
        elif letter in vallinam_letters:
            return "vallinam"
        elif letter in idayinam_letters:
            return "idayinam"
    if letter in uyirmei_letters:
        return "uyirmei"
    if letter in tamil_letters:
        return "tamil_or_grantham"
    if letter.isalpha():
        return "english"
    elif letter.isdigit():
        return "digit"
    raise ValueError(
        "Unknown letter '%s' neither Tamil nor English or number" % letter)


def print_tamil_words(tatext, use_frequencies=True):
    """
    Print tamil text word frequencies
    :param tatext: text as string
    :param use_frequencies: default True
    :return: print data to terminal as side-effect.
    """
    taletters = get_letters(tatext)
    # tamil words only
    frequency = {}
    for pos, word in enumerate(get_tamil_words(taletters)):
        frequency[word] = 1 + frequency.get(word, 0)
    # sort words by descending order of occurence
    for l in sorted(frequency.items(), key=operator.itemgetter(1)):
        if use_frequencies:
            print("%d -> %s" % (l[1], l[0]))
        else:
            print("%s" % l[0])
    return

compare_lexicograph_key = functools.cmp_to_key(compare_words_lexicographic)


def tamil_sorted(list_data, key=compare_lexicograph_key):
    """
    Sort list of Tamil strings in lexicographic order
    :param list_data: list of Tamil strings
    :param key: default to compare by Tamil dictionary (lexicographic) order
    :return: sorted string.
    """
    asorted = sorted(list_data, key=key)
    return asorted


def hex2unicode(ip_data, offset=3):
    """
    எ.கா. 'b9abc1b95bbeba4bbebb0baebcd' =
               'சுகாதாரம்'
    எ.கா. 'b95' = அ
    """
    result = []
    for s in re.split("\\-|/", ip_data):
        result.append("".join(
            [chr(int(s[i:i + offset], 16)) for i in range(0, len(s), offset)]))
    return result


def unicode2hex(ip_data, offset=3):
    """
     hex2unicode என்பதன் நேர்மாறான சார்பு
    எ.கா.  'சுகாதாரம்' ->  'b9abc1b95bbeba4bbebb0baebcd'
    எ.கா. 'அ' -> 'b95'
    """
    result = []
    for letter in get_letters_iterable(ip_data):
        if is_tamil_unicode(letter):
            for _letter in letter:
                result.append(("%{0}x".format(offset)) % ord(_letter))
        else:
            result.append(letter)
    return "".join(result)


# Tamil Letters
# அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ ஃ
# க் ச் ட் த் ப் ற் ஞ் ங் ண் ந் ம் ன் ய் ர் ல் வ் ழ் ள் ஜ் ஷ் ஸ் ஹ்
# க ச ட த ப ற ஞ ங ண ந ம ன ய ர ல வ ழ ள ஜ ஷ ஸ ஹ
# க கா கி கீ கு கூ கெ கே கை  கௌ
# ச சா சி சீ சு சூ செ சே சை சொ சோ சௌ
# ட டா டி டீ டு டூ டெ டே டை டொ டோ டௌ
# த தா தி தீ து தூ தெ தே தை தொ தோ தௌ
# ப பா பி பீ பு பூ பெ பே பை பொ போ பௌ
# ற றா றி றீ று றூ றெ றே றை றொ றோ றௌ
# ஞ ஞா ஞி ஞீ ஞு ஞூ ஞெ ஞே ஞை ஞொ ஞோ ஞௌ
# ங ஙா ஙி ஙீ ஙு ஙூ ஙெ ஙே ஙை ஙொ ஙோ ஙௌ
# ண ணா ணி ணீ ணு ணூ ணெ ணே ணை ணொ ணோ ணௌ
# ந நா நி நீ நு நூ நெ நே நை நொ நோ நௌ
# ம மா மி மீ மு மூ மெ மே மை மொ மோ மௌ
# ன னா னி னீ னு னூ னெ னே னை னொ னோ னௌ
# ய யா யி யீ யு யூ யெ யே யை யொ யோ யௌ
# ர ரா ரி ரீ ரு ரூ ரெ ரே ரை ரொ ரோ ரௌ
# ல லா லி லீ லு லூ லெ லே லை லொ லோ லௌ
# வ வா வி வீ வு வூ வெ வே வை வொ வோ வௌ
# ழ ழா ழி ழீ ழு ழூ ழெ ழே ழை ழொ ழோ ழௌ
# ள ளா ளி ளீ ளு ளூ ளெ ளே ளை ளொ ளோ ளௌ
# ஶ ஶா ஶி ஶீ 	ஶு 	ஶூ 	ஶெ 	ஶே 	ஶை ஶொ ஶோ ஶௌ
# ஜ ஜா ஜி ஜீ ஜு ஜூ ஜெ ஜே ஜை ஜொ ஜோ ஜௌ
# ஷ ஷா ஷி ஷீ ஷு ஷூ ஷெ ஷே ஷை ஷொ ஷோ ஷௌ
# ஸ ஸா ஸி ஸீ ஸு ஸூ ஸெ ஸே ஸை ஸொ ஸோ ஸௌ
# ஹ ஹா ஹி ஹீ ஹு ஹூ ஹெ ஹே ஹை ஹொ ஹோ ஹௌ
# க்ஷ க்ஷா க்ஷி க்ஷீ க்ஷு க்ஷூ க்ஷெ க்ஷே க்ஷை க்ஷொ க்ஷோ க்ஷௌ


class CacheGetLettersMixin:
    """
    Private cache for get_letters.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_letters_impl(self, word):
        raise NotImplementedError()

    @copy_lru_decorator
    def get_letters(self, word):
        """
        This is a cached implementation of get_letters.
        @word - can be a Tamil/English word (letter sequence)
        @return - list of letters in @word and cache for future use.
        """
        return self.get_letters_impl(word)


"""
மாத்திரை கணித்தல்
date: 10/06/2020
Written By: Parathan
"""

vantrodar_ugaram = ["கு", "சு", "டு", "து", "பு", "று"]  # வன்றொடர் உகரம்

uyir_mei_kuril = [
    "க",
    "கி",
    "கு",
    "கெ",
    "கொ",
    "கௌ",
    "ச",
    "சி",
    "சு",
    "செ",
    "சொ",
    "சௌ",
    "ட",
    "டி",
    "டு",
    "டெ",
    "டொ",
    "டௌ",
    "த",
    "தி",
    "து",
    "தெ",
    "தொ",
    "தௌ",
    "ப",
    "பி",
    "பு",
    "பெ",
    "பொ",
    "பௌ",
    "ற",
    "றி",
    "று",
    "றெ",
    "றொ",
    "றௌ",
    "ஞ",
    "ஞி",
    "ஞு",
    "ஞெ",
    "ஞொ",
    "ஞௌ",
    "ங",
    "ஙி",
    "ஙு",
    "ஙெ",
    "ஙொ",
    "ஙௌ",
    "ண",
    "ணி",
    "ணு",
    "ணெ",
    "ணொ",
    "ணௌ",
    "ந",
    "நி",
    "நு",
    "நெ",
    "நொ",
    "நௌ",
    "ம",
    "மி",
    "மு",
    "மெ",
    "மொ",
    "மௌ",
    "ன",
    "னி",
    "னு",
    "னெ",
    "னொ",
    "னௌ",
    "ய",
    "யி",
    "யு",
    "யெ",
    "யொ",
    "யௌ",
    "ர",
    "ரி",
    "ரு",
    "ரெ",
    "ரொ",
    "ரௌ",
    "ல",
    "லி",
    "லு",
    "லெ",
    "லொ",
    "லௌ",
    "வ",
    "வி",
    "வு",
    "வெ",
    "வொ",
    "வௌ",
    "ழ",
    "ழி",
    "ழு",
    "ழெ",
    "ழொ",
    "ழௌ",
    "ள",
    "ளி",
    "ளு",
    "ளெ",
    "ளொ",
    "ளௌ",
]

uyir_mei_nedil = [
    "கா",
    "கீ",
    "கூ",
    "கே",
    "கோ",
    "சா",
    "சீ",
    "சூ",
    "சே",
    "சோ",
    "டா",
    "டீ",
    "டூ",
    "டே",
    "டோ",
    "தா",
    "தீ",
    "தூ",
    "தே",
    "தோ",
    "பா",
    "பீ",
    "பூ",
    "பே",
    "போ",
    "றா",
    "றீ",
    "றூ",
    "றே",
    "றோ",
    "ஞா",
    "ஞீ",
    "ஞூ",
    "ஞே",
    "ஞோ",
    "ஙா",
    "ஙீ",
    "ஙூ",
    "ஙே",
    "ஙோ",
    "ணா",
    "ணீ",
    "ணூ",
    "ணே",
    "ணோ",
    "நா",
    "நீ",
    "நூ",
    "நே",
    "நோ",
    "மா",
    "மீ",
    "மூ",
    "மே",
    "மோ",
    "னா",
    "னீ",
    "னூ",
    "னே",
    "னோ",
    "யா",
    "யீ",
    "யூ",
    "யே",
    "யோ",
    "ரா",
    "ரீ",
    "ரூ",
    "ரே",
    "ரோ",
    "லா",
    "லீ",
    "லூ",
    "லே",
    "லோ",
    "வா",
    "வீ",
    "வூ",
    "வே",
    "வோ",
    "ழா",
    "ழீ",
    "ழூ",
    "ழே",
    "ழோ",
    "ளா",
    "ளீ",
    "ளூ",
    "ளே",
    "ளோ",
]


def calculate_uyir_nedil_kuril_maathirai(word):
    """
    Calculate maathirai helper routine.
    :param word: kuril, nedil, uyirmei letter
    :return: mathirai
    """
    if word in uyir_mei_kuril:
        return 1
    elif word in uyir_mei_nedil:
        return 2
    elif word in nedil_letters:
        return 2
    elif word in kuril_letters:
        return 1
    elif word in mei_letters:
        return 0.5
    return 0.0  # எழுத்து வடமொழியாக இருப்பின்.. 0.0


def calculate_maththirai(letters):
    """மாத்திரை கணித்தல்: ஒரு தமிழ் சொல்லின் @letters மாத்திரை அளவை கணிக்கும்.

    விதிகள்:
    நெடில் எழுத்துக்கள் ஒலிக்கும் கால அளவு 2 மாத்திரை.
    குறில் எழுத்துக்கள் ஒலிக்கும் கால அளவு 1 மாத்திரை.
    மெய் எழுத்துக்கள் ஒலிக்கும் கால அளவு 1/2 மாத்திரை.
    ஆய்த எழுத்தை ஒலிக்க ஆகும் கால அளவு 1/2 மாத்திரை.
    மகரக் குறுக்கம் "ன்", "ண்" ஐ தொடர்ந்து வரும் "ம்" ஆனது தன அரை மாத்திரையில் இருந்து கால் மாத்திரையாய் ஒலிக்கும்
    ஒளகாரக் குறுக்கம் சொல்லின் ஆரம்பத்தில் வரும் ஒள, மெள, வௌ என்பன 1 மாத்திரையில் ஒலித்தல்

    """

    ikaram = [
        "கி",
        "சி",
        "டி",
        "தி",
        "பி",
        "றி",
        "ஞி",
        "ஙி",
        "ணி",
        "நி",
        "மி",
        "னி",
        "யி",
        "ரி",
        "லி",
        "வி",
        "ழி",
        "ளி",
    ]

    aikaaram = [
        "கை",
        "சை",
        "டை",
        "தை",
        "பை",
        "றை",
        "ஞை",
        "ஙை",
        "ணை",
        "நை",
        "மை",
        "னை",
        "யை",
        "ரை",
        "லை",
        "வை",
        "ழை",
        "ளை",
    ]

    yakaram = [
        "ய", "யா", "யி", "யீ", "யு", "யூ", "யெ", "யே", "யை", "யொ", "யோ", "யௌ"
    ]

    single_word = get_letters(letters)

    maaththiraivarisai = []

    # maaththiraivarisai_word = []

    for index, eluthu in enumerate(single_word):

        # maaththiraivarisai_word.append(eluthu)
        # print(maaththiraivarisai_word)

        # குற்றியலுகரம்
        if eluthu in vantrodar_ugaram:

            if index == 0:
                maaththiraivarisai.append(1)
            elif index == 1:
                if (single_word[0] not in uyir_mei_kuril
                        and single_word[0] not in kuril_letters):
                    maaththiraivarisai.append(0.5)
                else:
                    maaththiraivarisai.append(1)

            else:
                maaththiraivarisai.append(0.5)

        # குற்றியலிகரம்
        elif eluthu in ikaram:

            checkNext = False

            try:
                checkNext = single_word[index + 1] in yakaram
            except:
                checkNext = False

            if checkNext:
                maaththiraivarisai.append(0.5)
            else:
                maaththiraivarisai.append(1)

        # ஔகாரக் குறுக்கம்
        elif eluthu == "ஔ" or eluthu == "மௌ" or eluthu == "வெள":
            if (single_word[0] == "ஔ" or single_word[0] == "மௌ"
                    or single_word[0] == "வெள"):
                maaththiraivarisai.append(1)

        # ஐகாரக்குறுக்கம்
        elif eluthu == "ஐ":
            if single_word[0] == "ஐ":
                maaththiraivarisai.append(1.5)

        elif eluthu in aikaaram:
            if single_word[0] in aikaaram:
                maaththiraivarisai.append(1.5)
            else:
                maaththiraivarisai.append(1)
        # ஆய்தம்
        elif eluthu == "ஃ":
            if single_word[-1] == "ஃ":
                maaththiraivarisai.append(0.5)
            else:
                maaththiraivarisai.append(0.25)

        # மகரக் குறுக்கம்
        elif eluthu == "ம்":

            checkMagaram = False

            try:
                checkMagaram = (single_word[index - 1] == "ண்"
                                or single_word[index - 1] == "ன்")
            except:
                checkMagaram = False

            if checkMagaram:
                maaththiraivarisai.append(0.25)
            else:
                maaththiraivarisai.append(0.5)

        else:
            maaththiraivarisai.append(
                calculate_uyir_nedil_kuril_maathirai(eluthu))

    print(maaththiraivarisai)
    return sum(maaththiraivarisai)


def total_maaththirai(letters):
    """
    ஒரு சொல் அதன் எழுத்துக்களின் @letters  என்பதன் மாத்திரைகளை தனித்தனியே
    கணிக்கிட்டு முழுமையாக அதன் சொல்-அளவான முழு மாத்திரை அளவை வெளியிடுகிறது.
    """

    txt_string = letters.split(sep=" ")

    total_maaththiraivarisai = []

    if len(txt_string) > 1:

        for word in txt_string:
            total_maaththiraivarisai.append(calculate_maththirai(word))

    else:
        total_maaththiraivarisai.append(calculate_maththirai(letters))

    return sum(total_maaththiraivarisai)
