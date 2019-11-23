## This Python file uses the following encoding: utf-8
##
## (C) 2007, 2008, 2013, 2015, 2016 Muthiah Annamalai <ezhillang@gmail.com>
## (C) 2013 msathia <msathia@gmail.com>
##
## This file is dual licensed - originally GPL v3 from Ezhil, and
## then as part of open-tamil package in MIT license.
##
## Licensed under GPL Version 3

from sys import version
from copy import copy
import re
import operator
import string
import abc
PYTHON3 = version > '3'
del version

if PYTHON3:
    import functools

## constants
TA_ACCENT_LEN = 13 #12 + 1
TA_AYUDHA_LEN = 1
TA_UYIR_LEN = 12
TA_MEI_LEN = 18
TA_AGARAM_LEN = 18
TA_SANSKRIT_LEN = 6
TA_UYIRMEI_LEN = 216
TA_GRANTHA_UYIRMEI_LEN = 24*12
TA_LETTERS_LEN = 247 + 6*12 + 22 + 4 - TA_AGARAM_LEN - 4 #323

def to_unicode_repr( _letter ):
    """ helpful in situations where browser/app may recognize Unicode encoding
        in the \u0b8e type syntax but not actual unicode glyph/code-point"""
    # Python 2-3 compatible
    return u"u'"+ u"".join( [ u"\\u%04x"%ord(l) for l in _letter ] ) + u"'"

def letters_to_py( _letters ):
        """ return list of letters e.g. uyir_letters as a Python list """
        return u"[u'"+u"',u'".join( _letters )+u"']"

# List of letters you can use
uyir_letters = [u"அ",u"ஆ",u"இ",u"ஈ",u"உ",u"ஊ",u"எ",u"ஏ",u"ஐ",u"ஒ",u"ஓ",u"ஔ"]
vowel_a  = u"அ"
vowel_aa = u"ஆ"
vowel_i  = u"இ"
vowel_ii = u"ஈ"
vowel_u  = u"உ"
vowel_uu = u"ஊ"
vowel_e  =  u"எ"
vowel_ee = u"ஏ"
vowel_ai = u"ஐ"
vowel_o  = u"ஒ"
vowel_oo = u"ஓ"
vowel_au = u"ஔ"
ayudha_letter = u"ஃ"

kuril_letters = [u"அ", u"இ", u"உ", u"எ", u"ஒ"]
nedil_letters = [u"ஆ", u"ஈ", u"ஊ", u"ஏ", u"ஓ"]

vallinam_letters = [u"க்", u"ச்", u"ட்", u"த்", u"ப்", u"ற்"]
mellinam_letters = [u"ங்", u"ஞ்", u"ண்", u"ந்", u"ம்", u"ன்"]
idayinam_letters = [u"ய்", u"ர்", u"ல்", u"வ்", u"ழ்", u"ள்"]

mei_letters = [u"க்",u"ச்",u"ட்",u"த்",u"ப்",u"ற்",
           u"ஞ்",u"ங்",u"ண்",u"ந்",u"ம்",u"ன்",
           u"ய்",u"ர்",u"ல்",u"வ்",u"ழ்",u"ள்" ]

accent_symbols = [u"",u"ா",u"ி",u"ீ",u"ு",u"ூ",
          u"ெ",u"ே",u"ை",u"ொ",u"ோ",u"ௌ",u"ஃ"]
accent_aa = accent_symbols[1]
accent_i  = accent_symbols[2]
accent_u  = accent_symbols[3]
accent_uu = accent_symbols[4]
accent_e  = accent_symbols[5]
accent_ee = accent_symbols[6]
accent_ai = accent_symbols[7]
accent_o  = accent_symbols[8]
accent_oo = accent_symbols[9]
accent_au = accent_symbols[10]

pulli_symbols = [u"்"]

agaram_letters = [u"க",u"ச",u"ட",u"த",u"ப",u"ற",
          u"ஞ",u"ங",u"ண",u"ந",u"ம",u"ன",
          u"ய",u"ர",u"ல",u"வ",u"ழ",u"ள"]
consonant_ka = u"க"
consonant_nga = u"ங"
consonant_ca = u"ச"
consonant_ja = u"ஜ"
consonant_nya = u"ஞ"
consonant_tta = u"ட"
consonant_nna = u"ண"
consonant_nnna = u"ன"
consonant_ta = u"த"
consonant_tha = u"த"
consonant_na = u"ந"
consonant_pa = u"ப"
consonant_ma = u"ம"
consonant_ya = u"ய"
consonant_ra = u"ர"
consonant_rra = u"ற"
consonant_la = u"ல"
consonant_lla = u"ள"
consonant_llla = u"ழ"
consonant_zha = u"ழ"
consonant_va = u"வ"

sanskrit_letters = [u"ஶ",u"ஜ",u"ஷ", u"ஸ",u"ஹ",u"க்ஷ"]
sanskrit_mei_letters =[u"ஶ்",u"ஜ்",u"ஷ்", u"ஸ்",u"ஹ்",u"க்ஷ்"]

grantha_mei_letters = copy(mei_letters)
grantha_mei_letters.extend(sanskrit_mei_letters)

grantha_agaram_letters = copy(agaram_letters)
grantha_agaram_letters.extend(sanskrit_letters)

uyirmei_letters = [
u"க"  ,u"கா"  ,u"கி"  ,u"கீ"  ,u"கு"  ,u"கூ"  ,u"கெ"  ,u"கே"  ,u"கை"  ,u"கொ"  ,u"கோ"  ,u"கௌ"  ,
u"ச"  ,u"சா"  ,u"சி"  ,u"சீ"  ,u"சு"  ,u"சூ"  ,u"செ"  ,u"சே"  ,u"சை"  ,u"சொ"  ,u"சோ"  ,u"சௌ" ,
u"ட"  ,u"டா"  ,u"டி"  ,u"டீ"  ,u"டு"  ,u"டூ"  ,u"டெ"  ,u"டே"  ,u"டை"  ,u"டொ"  ,u"டோ"  ,u"டௌ",
u"த"  ,u"தா"  ,u"தி"  ,u"தீ"  ,u"து"  ,u"தூ"  ,u"தெ"  ,u"தே"  ,u"தை"  ,u"தொ"  ,u"தோ"  ,u"தௌ",
u"ப"  ,u"பா"  ,u"பி"  ,u"பீ"  ,u"பு"  ,u"பூ"  ,u"பெ"  ,u"பே"  ,u"பை"  ,u"பொ"  ,u"போ"  ,u"பௌ" ,
u"ற"  ,u"றா"  ,u"றி"  ,u"றீ"  ,u"று"  ,u"றூ"  ,u"றெ"  ,u"றே"  ,u"றை"  ,u"றொ"  ,u"றோ"  ,u"றௌ",
u"ஞ"  ,u"ஞா"  ,u"ஞி"  ,u"ஞீ"  ,u"ஞு"  ,u"ஞூ"  ,u"ஞெ"  ,u"ஞே"  ,u"ஞை"  ,u"ஞொ"  ,u"ஞோ"  ,u"ஞௌ"  ,
u"ங"  ,u"ஙா"  ,u"ஙி"  ,u"ஙீ"  ,u"ஙு"  ,u"ஙூ"  ,u"ஙெ"  ,u"ஙே"  ,u"ஙை"  ,u"ஙொ"  ,u"ஙோ"  ,u"ஙௌ"  ,
u"ண"  ,u"ணா"  ,u"ணி"  ,u"ணீ"  ,u"ணு"  ,u"ணூ"  ,u"ணெ"  ,u"ணே"  ,u"ணை"  ,u"ணொ"  ,u"ணோ"  ,u"ணௌ"  ,
u"ந"  ,u"நா"  ,u"நி"  ,u"நீ"  ,u"நு"  ,u"நூ"  ,u"நெ"  ,u"நே"  ,u"நை"  ,u"நொ"  ,u"நோ"  ,u"நௌ"  ,
u"ம"  ,u"மா"  ,u"மி"  ,u"மீ"  ,u"மு"  ,u"மூ"  ,u"மெ"  ,u"மே"  ,u"மை"  ,u"மொ"  ,u"மோ"  ,u"மௌ" ,
u"ன"  ,u"னா"  ,u"னி"  ,u"னீ"  ,u"னு"  ,u"னூ"  ,u"னெ"  ,u"னே"  ,u"னை"  ,u"னொ"  ,u"னோ"  ,u"னௌ",
u"ய"  ,u"யா"  ,u"யி"  ,u"யீ"  ,u"யு"  ,u"யூ"  ,u"யெ"  ,u"யே"  ,u"யை"  ,u"யொ"  ,u"யோ"  ,u"யௌ",
u"ர"  ,u"ரா"  ,u"ரி"  ,u"ரீ"  ,u"ரு"  ,u"ரூ"  ,u"ரெ"  ,u"ரே"  ,u"ரை"  ,u"ரொ"  ,u"ரோ"  ,u"ரௌ",
u"ல"  ,u"லா"  ,u"லி"  ,u"லீ"  ,u"லு"  ,u"லூ"  ,u"லெ"  ,u"லே"  ,u"லை"  ,u"லொ"  ,u"லோ"  ,u"லௌ" ,
u"வ"  ,u"வா"  ,u"வி"  ,u"வீ"  ,u"வு"  ,u"வூ"  ,u"வெ"  ,u"வே"  ,u"வை"  ,u"வொ"  ,u"வோ"  ,u"வௌ" ,
u"ழ"  ,u"ழா"  ,u"ழி"  ,u"ழீ"  ,u"ழு"  ,u"ழூ"  ,u"ழெ"  ,u"ழே"  ,u"ழை"  ,u"ழொ"  ,u"ழோ"  ,u"ழௌ" ,
u"ள"  ,u"ளா"  ,u"ளி"  ,u"ளீ"  ,u"ளு"  ,u"ளூ"  ,u"ளெ"  ,u"ளே"  ,u"ளை"  ,u"ளொ"  ,u"ளோ"  ,u"ளௌ" ]

tamil247 = [ ayudha_letter ]
tamil247.extend( uyir_letters )
tamil247.extend( mei_letters )
tamil247.extend( uyirmei_letters )

# Ref: https://en.wikipedia.org/wiki/Tamil_numerals
# tamil digits : Apart from the numerals (0-9), Tamil also has numerals for 10, 100 and 1000.
tamil_digit_1to10 = [u"௦", u"௧", u"௨",u"௩",u"௪",u"௫",u"௬",u"௭",u"௮",u"௯",u"௰"]
tamil_digit_100 = u"௱"
tamil_digit_1000 = u"௲"

tamil_digits = [(num,digit) for num,digit in zip(range(0,11),tamil_digit_1to10)]
tamil_digits.extend( [(100,tamil_digit_100),(1000,tamil_digit_1000)] )

# tamil symbols
_day = u"௳"
_month = u"௴"
_year = u"௵"
_debit = u"௶"
_credit = u"௷"
_rupee = u"௹"
_numeral = u"௺"
_sri = u"\u0bb6\u0bcd\u0bb0\u0bc0" #SRI - ஶ்ரீ
_ksha = u"\u0b95\u0bcd\u0bb7" #KSHA - க்ஷ
_ksh = u"\u0b95\u0bcd\u0bb7\u0bcd" #KSH - க்ஷ்
_indian_rupee = u"₹"
tamil_symbols = [_day, _month, _year, _debit, _credit, _rupee, _numeral, _sri, _ksha, _ksh,_indian_rupee]

## total tamil letters in use, including sanskrit letters
tamil_letters = [

## /* Uyir */
u"அ",u"ஆ",u"இ", u"ஈ",u"உ",u"ஊ",u"எ",u"ஏ",u"ஐ",u"ஒ",u"ஓ",u"ஔ",

##/* Ayuda Ezhuthu */
u"ஃ",

## /* Mei */
u"க்",u"ச்",u"ட்",u"த்",u"ப்",u"ற்",u"ஞ்",u"ங்",u"ண்",u"ந்",u"ம்",u"ன்",u"ய்",u"ர்",u"ல்",u"வ்",u"ழ்",u"ள்",

## /* Agaram */
## u"க",u"ச",u"ட",u"த",u"ப",u"ற",u"ஞ",u"ங",u"ண",u"ந",u"ம",u"ன",u"ய",u"ர",u"ல",u"வ",u"ழ",u"ள",

## /* Sanskrit (Vada Mozhi) */
## u"ஜ",u"ஷ", u"ஸ",u"ஹ",

##/* Sanskrit (Mei) */
u"ஜ்",u"ஷ்", u"ஸ்",u"ஹ்",

## /* Uyir Mei */
u"க"  ,u"கா"  ,u"கி"  ,u"கீ"  ,u"கு"  ,u"கூ"  ,u"கெ"  ,u"கே"  ,u"கை"  ,u"கொ"  ,u"கோ"  ,u"கௌ"
,u"ச"  ,u"சா"  ,u"சி"  ,u"சீ"  ,u"சு"  ,u"சூ"  ,u"செ"  ,u"சே"  ,u"சை"  ,u"சொ"  ,u"சோ"  ,u"சௌ"
,u"ட"  ,u"டா"  ,u"டி"  ,u"டீ"  ,u"டு"  ,u"டூ"  ,u"டெ"  ,u"டே"  ,u"டை"  ,u"டொ"  ,u"டோ"  ,u"டௌ"
,u"த"  ,u"தா"  ,u"தி"  ,u"தீ"  ,u"து"  ,u"தூ"  ,u"தெ"  ,u"தே"  ,u"தை"  ,u"தொ"  ,u"தோ"  ,u"தௌ"
,u"ப"  ,u"பா"  ,u"பி"  ,u"பீ"  ,u"பு"  ,u"பூ"  ,u"பெ"  ,u"பே"  ,u"பை"  ,u"பொ"  ,u"போ"  ,u"பௌ"
,u"ற"  ,u"றா"  ,u"றி"  ,u"றீ"  ,u"று"  ,u"றூ"  ,u"றெ"  ,u"றே"  ,u"றை"  ,u"றொ"  ,u"றோ"  ,u"றௌ"
,u"ஞ"  ,u"ஞா"  ,u"ஞி"  ,u"ஞீ"  ,u"ஞு"  ,u"ஞூ"  ,u"ஞெ"  ,u"ஞே"  ,u"ஞை"  ,u"ஞொ"  ,u"ஞோ"  ,u"ஞௌ"
,u"ங"  ,u"ஙா"  ,u"ஙி"  ,u"ஙீ"  ,u"ஙு"  ,u"ஙூ"  ,u"ஙெ"  ,u"ஙே"  ,u"ஙை"  ,u"ஙொ"  ,u"ஙோ"  ,u"ஙௌ"
,u"ண"  ,u"ணா"  ,u"ணி"  ,u"ணீ"  ,u"ணு"  ,u"ணூ"  ,u"ணெ"  ,u"ணே"  ,u"ணை"  ,u"ணொ"  ,u"ணோ"  ,u"ணௌ"
,u"ந"  ,u"நா"  ,u"நி"  ,u"நீ"  ,u"நு"  ,u"நூ"  ,u"நெ"  ,u"நே"  ,u"நை"  ,u"நொ"  ,u"நோ"  ,u"நௌ"
,u"ம"  ,u"மா"  ,u"மி"  ,u"மீ"  ,u"மு"  ,u"மூ"  ,u"மெ"  ,u"மே"  ,u"மை"  ,u"மொ"  ,u"மோ"  ,u"மௌ"
,u"ன"  ,u"னா"  ,u"னி"  ,u"னீ"  ,u"னு"  ,u"னூ"  ,u"னெ"  ,u"னே"  ,u"னை"  ,u"னொ"  ,u"னோ"  ,u"னௌ"
,u"ய"  ,u"யா"  ,u"யி"  ,u"யீ"  ,u"யு"  ,u"யூ"  ,u"யெ"  ,u"யே"  ,u"யை"  ,u"யொ"  ,u"யோ"  ,u"யௌ"
,u"ர"  ,u"ரா"  ,u"ரி"  ,u"ரீ"  ,u"ரு"  ,u"ரூ"  ,u"ரெ"  ,u"ரே"  ,u"ரை"  ,u"ரொ"  ,u"ரோ"  ,u"ரௌ"
,u"ல"  ,u"லா"  ,u"லி"  ,u"லீ"  ,u"லு"  ,u"லூ"  ,u"லெ"  ,u"லே"  ,u"லை"  ,u"லொ"  ,u"லோ"  ,u"லௌ"
,u"வ"  ,u"வா"  ,u"வி"  ,u"வீ"  ,u"வு"  ,u"வூ"  ,u"வெ"  ,u"வே"  ,u"வை"  ,u"வொ"  ,u"வோ"  ,u"வௌ"
,u"ழ"  ,u"ழா"  ,u"ழி"  ,u"ழீ"  ,u"ழு"  ,u"ழூ"  ,u"ழெ"  ,u"ழே"  ,u"ழை"  ,u"ழொ"  ,u"ழோ"  ,u"ழௌ"
,u"ள"  ,u"ளா"  ,u"ளி"  ,u"ளீ"  ,u"ளு"  ,u"ளூ"  ,u"ளெ"  ,u"ளே"  ,u"ளை"  ,u"ளொ"  ,u"ளோ"  ,u"ளௌ"

##/* Sanskrit Uyir-Mei */
,u"ஶ", 	u"ஶா", 	u"ஶி", 	u"ஶீ", u"ஶு", u"ஶூ", u"ஶெ", u"ஶே", u"ஶை", u"ஶொ", u"ஶோ", u"ஶௌ"
,u"ஜ"  ,u"ஜா"  ,u"ஜி"  ,u"ஜீ"  ,u"ஜு"  ,u"ஜூ"  ,u"ஜெ"  ,u"ஜே"  ,u"ஜை"  ,u"ஜொ"  ,u"ஜோ"  ,u"ஜௌ"
,u"ஷ"  ,u"ஷா"  ,u"ஷி"  ,u"ஷீ"  ,u"ஷு"  ,u"ஷூ"  ,u"ஷெ"  ,u"ஷே"  ,u"ஷை"  ,u"ஷொ"  ,u"ஷோ"  ,u"ஷௌ"
,u"ஸ"  ,u"ஸா"  ,u"ஸி"  ,u"ஸீ"  ,u"ஸு"  ,u"ஸூ"  ,u"ஸெ"  ,u"ஸே"  ,u"ஸை"  ,u"ஸொ"  ,u"ஸோ"  ,u"ஸௌ"
,u"ஹ"  ,u"ஹா"  ,u"ஹி"  ,u"ஹீ"  ,u"ஹு"  ,u"ஹூ"  ,u"ஹெ"  ,u"ஹே"  ,u"ஹை"  ,u"ஹொ"  ,u"ஹோ"  ,u"ஹௌ"
,u"க்ஷ"  ,u"க்ஷா"  ,u"க்ஷி" 	,u"க்ஷீ" 	,u"க்ஷு"  ,u"க்ஷூ"  ,u"க்ஷெ"   ,u"க்ஷே" ,u"க்ஷை"  ,u"க்ஷொ" ,u"க்ஷோ"  ,u"க்ஷௌ" ]

grantha_uyirmei_letters = copy( tamil_letters[tamil_letters.index(u"கா")-1:] )

## length of the definitions
def accent_len( ):
    return TA_ACCENT_LEN ## 13 = 12 + 1

def ayudha_len( ):
    return TA_AYUDHA_LEN ## 1

def uyir_len( ):
    return TA_UYIR_LEN ##12

def mei_len( ):
    return TA_MEI_LEN ##18

def agaram_len( ):
    return TA_AGARAM_LEN ##18

def uyirmei_len( ):
    return TA_UYIRMEI_LEN ##216

def tamil_len(  ):
    return len(tamil_letters)

## access the letters
def uyir( idx ):
    assert ( idx >= 0 and idx < uyir_len() )
    return uyir_letters[idx]

def agaram( idx ):
    assert ( idx >= 0 and idx < agaram_len() )
    return agaram_letters[idx]

def mei( idx ):
    assert ( idx >= 0 and idx < mei_len() )
    return mei_letters[idx]

def uyirmei( idx ):
    assert( idx >= 0 and idx < uyirmei_len() )
    return uyirmei_letters[idx]

def mei_to_agaram(in_syllable):
    if in_syllable in grantha_mei_letters:
        mei_pos = grantha_mei_letters.index(in_syllable)
        agaram_a_pos = 0
        syllable = uyirmei_constructed(mei_pos,agaram_a_pos)
        return syllable
    return in_syllable

def uyirmei_constructed( mei_idx, uyir_idx):
    """ construct uyirmei letter give mei index and uyir index """
    idx,idy = mei_idx,uyir_idx
    assert ( idy >= 0 and idy < uyir_len() )
    assert ( idx >= 0 and idx < 6+mei_len() )
    return grantha_agaram_letters[mei_idx]+accent_symbols[uyir_idx]

def tamil( idx ):
    """ retrieve Tamil letter at canonical index from array utf8.tamil_letters """
    assert ( idx >= 0 and idx < tamil_len() )
    return tamil_letters[idx]

# companion function to @tamil()
def getidx(letter):
    for itr in range(0,tamil_len()):
        if tamil_letters[itr] == letter:
            return itr
    raise Exception("Cannot find letter in Tamil arichuvadi")

## useful part of the API:
def istamil_prefix( word ):
    """ check if the given word has a tamil prefix. Returns
    either a True/False flag """
    for letter in tamil_letters:
        if ( word.find(letter) == 0 ):
            return True
    return False

if not PYTHON3:
    is_tamil_unicode_predicate = lambda x: x >= unichr(2946) and x <= unichr(3066)
else:
    is_tamil_unicode_predicate = lambda x: x >= chr(2946) and x <= chr(3066)
def is_tamil_unicode( sequence ):
    # Ref: languagetool-office-extension/src/main/java/org/languagetool/openoffice/TamilDetector.java
    if type(sequence) is list:
        return list(map( is_tamil_unicode_predicate, sequence ))
    if len(sequence) > 1:
        return list(map( is_tamil_unicode_predicate, get_letters(sequence) ))
    return is_tamil_unicode_predicate( sequence )

def has_english( word_in ):
    """ return True if word_in has any English letters in the string"""
    return not all_tamil(word_in) and len(word_in) > 0 and any([l in word_in for l in string.ascii_letters])

def all_tamil( word_in ):
    """ predicate checks if all letters of the input word are Tamil letters """
    if isinstance(word_in,list):
        word = word_in
    else:
        word = get_letters( word_in )
    return all( [(letter in tamil_letters) for letter in word] )

def has_tamil( word ):
    """check if the word has any occurance of any tamil letter """
    # list comprehension is not necessary - we bail at earliest
    for letters in tamil_letters:
        if ( word.find(letters) >= 0 ):
            return True
    return False

def istamil( tchar ):
    """ check if the letter tchar is prefix of
    any of tamil-letter. It suggests we have a tamil identifier"""
    if (tchar in tamil_letters):
        return True
    return False

def istamil_alnum( tchar ):
    """ check if the character is alphanumeric, or tamil.
    This saves time from running through istamil() check. """
    return ( tchar.isalnum( ) or istamil( tchar ) )

def reverse_word( word ):
    """ reverse a Tamil word according to letters not unicode-points """
    op = get_letters( word )
    op.reverse()
    return u"".join(op)

## find out if the letters like, "பொ" are written in canonical "ப + ொ"" graphemes then
## return True. If they are written like "ப + ெ + ா" then return False on first occurrence
def is_normalized( text ):
    #print(text[0],text[1],text[2],text[-1],text[-2])
    TLEN,idx = len(text),1
    kaal = u"ா"
    Laa = u"ள"
    sinna_kombu, periya_kombu = u"ெ", u"ே"
    kombugal = [sinna_kombu, periya_kombu]

    # predicate measures if the normalization is violated
    def predicate( last_letter, prev_letter):
        if ((kaal == last_letter) and (prev_letter in kombugal)):
            return True
        if ((Laa == last_letter) and (prev_letter == sinna_kombu)):
            return True
        return False
    if TLEN < 2:
        return True
    elif TLEN == 2:
        if predicate( text[-1], text[-2] ):
            return False
        return True
    idx = TLEN
    a = text[idx-2]
    b = text[idx-1]
    while (idx >= 0):
        if predicate(b,a):
            return False
        b=a
        idx = idx - 1
        if idx >= 0:
            a=text[idx]
    return True

def _make_set(args):
    if PYTHON3:
        return frozenset(args)
    return set(args)

grantha_agaram_set = _make_set(grantha_agaram_letters)
accent_symbol_set = _make_set(accent_symbols)
uyir_letter_set   = _make_set(uyir_letters)

## Split a tamil-unicode stream into
## tamil characters (individuals).
def get_letters( word ):
    """ splits the word into a character-list of tamil/english
    characters present in the stream """
    ta_letters = list()
    not_empty = False
    WLEN,idx = len(word),0
    while (idx < WLEN):
        c = word[idx]
        #print(idx,hex(ord(c)),len(ta_letters))
        if c in uyir_letter_set or c == ayudha_letter:
            ta_letters.append(c)
            not_empty = True
        elif c in grantha_agaram_set:
            ta_letters.append(c)
            not_empty = True
        elif c in accent_symbol_set:
            if not not_empty:
                # odd situation
                ta_letters.append(c)
                not_empty = True
            else:
                #print("Merge/accent")
                ta_letters[-1] += c
        else:
            if ord(c) < 256 or not (is_tamil_unicode(c)):
                ta_letters.append( c )
            else:
                if not_empty:
                    #print("Merge/??")
                    ta_letters[-1]+= c
                else:
                    ta_letters.append(c)
                    not_empty = True
        idx = idx + 1
    return ta_letters


_all_symbols = copy( accent_symbols )
_all_symbols.extend( pulli_symbols )
all_symbol_set = _make_set(_all_symbols)

# same as get_letters but use as iterable
def get_letters_iterable( word ):
    """ splits the word into a character-list of tamil/english
    characters present in the stream """
    WLEN,idx = len(word),0

    while (idx < WLEN):
        c = word[idx]
        #print(idx,hex(ord(c)),len(ta_letters))
        if c in uyir_letter_set or c == ayudha_letter:
            idx = idx + 1
            yield c
        elif c in grantha_agaram_set:
            if idx + 1 < WLEN and word[idx+1] in all_symbol_set:
                c2 = word[idx+1]
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
for _uyir_idx in range(0,12):
    for _mei_idx, _mei in enumerate(grantha_mei_letters):
        _uyirmei = uyirmei_constructed( _mei_idx, _uyir_idx )
        grantha_uyirmei_splits[_uyirmei] = [_mei,uyir_letters[_uyir_idx]]

def join_letters_elementary(elements):
    assert len(elements)%2 == 0, u'input has to be an even numbered list'
    return u"".join([joinMeiUyir(elements[i],elements[i+1]) for i in range(0,len(elements),2)])

def get_letters_elementary_iterable(word,symmetric=False):
    for letter in get_letters_iterable(word):
        letter_parts = grantha_uyirmei_splits.get(letter,None)
        if letter_parts:
            yield letter_parts[0]
            yield letter_parts[1]
        else:
            if letter in grantha_mei_letters:
                yield letter
                if symmetry: yield None
            else:
                if symmetry: yield None
                yield letter
    return

def get_letters_elementary(word,symmetric=False):
    rval = []
    for letter in get_letters(word):
        letter_parts = grantha_uyirmei_splits.get(letter,None)
        if letter_parts:
            rval.append( letter_parts[0] )
            rval.append( letter_parts[1] )
        else:
            if letter in grantha_mei_letters:
                rval.append( letter )
                if symmetric: rval.append(None)
            else:
                if symmetric: rval.append(None)
                rval.append( letter )
    return rval

def get_words(letters,tamil_only=False):
    return [ word for word in get_words_iterable(letters,tamil_only) ]

def get_words_iterable( letters, tamil_only=False ):
    """ given a list of UTF-8 letters section them into words, grouping them at spaces """

    # correct algorithm for get-tamil-words
    buf = []
    for idx,let in enumerate(letters):
        if not let.isspace():
            if istamil(let) or (not tamil_only):
                buf.append( let )
        else:
            if len(buf) > 0:
                yield  u"".join( buf )
                buf = []
    if len(buf) > 0:
        yield u"".join(buf)

def get_tamil_words( letters ):
    """ reverse a Tamil word according to letters, not unicode-points """
    if not isinstance(letters,list):
        raise Exception("metehod needs to be used with list generated from 'tamil.utf8.get_letters(...)'")
    return [word for word in get_words_iterable( letters, tamil_only = True )]

if PYTHON3:
    def cmp( x, y):
        if x == y:
            return 0
        if x > y:
            return 1
        return -1

# answer if word_a ranks ahead of, or at same level, as word_b in a Tamil dictionary order...
# for use with Python : if a > 0
def compare_words_lexicographic( word_a, word_b ):
    """ compare words in Tamil lexicographic order """
    # sanity check for words to be all Tamil
    if ( not all_tamil(word_a) ) or (not all_tamil(word_b)) :
        #print("## ")
        #print(word_a)
        #print(word_b)
        #print("Both operands need to be Tamil words")
        pass
    La = len(word_a)
    Lb = len(word_b)
    all_TA_letters = u"".join(tamil_letters)
    for itr in range(0,min(La,Lb)):
            pos1 = all_TA_letters.find( word_a[itr] )
            pos2 = all_TA_letters.find( word_b[itr] )

            if pos1 != pos2 :
                    #print  not( pos1 > pos2), pos1, pos2
                    return cmp(pos1, pos2)

    # result depends on if La is shorter than Lb, or 0 if La == Lb  i.e. cmp
    return cmp(La,Lb)

# return a list of ordered-pairs containing positions
# that are common in word_a, and word_b; e.g.
# தேடுக x தடங்கல் -> one common letter க [(2,3)]
# சொல் x   தேடுக -> no common letters []
def word_intersection( word_a, word_b ):
    """ return a list of tuples where word_a, word_b intersect """
    positions = []
    word_a_letters = get_letters( word_a )
    word_b_letters = get_letters( word_b )
    for idx,wa in enumerate(word_a_letters):
        for idy,wb in enumerate(word_b_letters):
            if ( wa == wb ):
                positions.append( (idx, idy) )
    return positions

def unicode_normalize(cplxchar):
    Laa = u"ள"
    kaal = u"ா"
    sinna_kombu_a = u"ெ"
    periya_kombu_aa = u"ே"
    sinna_kombu_o = u"ொ"
    periya_kombu_oo = u"ோ"
    kombu_ak = u"ௌ"

    lcplx = len(cplxchar)
    if lcplx>=3 and cplxchar[-1] == Laa:
        if cplxchar[-2] == sinna_kombu_a:
            return ( cplxchar[:-2] + kombu_ak )
    if lcplx >= 2 and cplxchar[-1] == kaal:
        if cplxchar[-2] == sinna_kombu_a:
            return ( cplxchar[:-2]+sinna_kombu_o )
        if cplxchar[-2] == periya_kombu_aa:
            return ( cplxchar[:-2]+periya_kombu_oo )
    # no-op
    return cplxchar

def splitMeiUyir(uyirmei_char):
    """
    This function split uyirmei compound character into mei + uyir characters
    and returns in tuple.

    Input : It must be unicode tamil char.

    Written By : Arulalan.T
    Date : 22.09.2014

    """

    if not isinstance(uyirmei_char, PYTHON3 and str or unicode):
        raise ValueError("Passed input letter '%s' must be unicode, \
                                not just string" % uyirmei_char)

    if uyirmei_char in mei_letters or uyirmei_char in uyir_letters or uyirmei_char in ayudha_letter:
        return uyirmei_char

    if uyirmei_char not in grantha_uyirmei_letters:
        if not is_normalized( uyirmei_char ):
            norm_char = unicode_normalize(uyirmei_char)
            rval = splitMeiUyir( norm_char )
            return rval
        raise ValueError("Passed input letter '%s' is not tamil letter" % uyirmei_char)

    idx = grantha_uyirmei_letters.index(uyirmei_char)
    uyiridx = idx % 12
    meiidx = int((idx - uyiridx)/ 12)
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
    if not mei_char: return uyir_char
    if not uyir_char: return mei_char

    if not isinstance(mei_char, PYTHON3 and str or unicode):
        raise ValueError(u"Passed input mei character '%s' must be unicode, not just string" % mei_char)
    if not isinstance(uyir_char, PYTHON3 and str or unicode) and uyir_char != None:
        raise ValueError(u"Passed input uyir character '%s' must be unicode, not just string" % uyir_char)
    if mei_char not in grantha_mei_letters:
        raise ValueError(u"Passed input character '%s' is not a tamil mei character" % mei_char)
    if uyir_char not in uyir_letters:
        raise ValueError(u"Passed input character '%s' is not a tamil uyir character" % uyir_char)
    if uyir_char:
        uyiridx = uyir_letters.index(uyir_char)
    else:
        return mei_char
    meiidx = grantha_mei_letters.index(mei_char)
    # calculate uyirmei index
    uyirmeiidx = meiidx*12 + uyiridx
    return grantha_uyirmei_letters[uyirmeiidx]

def classify_letter(letter):
    if not isinstance(letter, PYTHON3 and str or unicode):
        raise TypeError("Input'%s' must be unicode, not just string" % letter)
    kinds = [u'kuril',u'nedil',u'ayudham',u'vallinam',u'mellinam',u'idayinam',u'uyirmei',u'tamil_or_grantham']
    if letter in uyir_letters:
        if letter in kuril_letters:
            return u'kuril'
        elif letter in nedil_letters:
            return u'nedil'
        elif letter == ayudha_letter:
            return 'ayudham'
    if letter in mei_letters:
        if letter in mellinam_letters:
            return 'mellinam'
        elif letter in vallinam_letters:
            return 'vallinam'
        elif letter in idayinam_letters:
            return 'idayinam'
    if letter in uyirmei_letters:
        return 'uyirmei'
    if letter in tamil_letters:
        return 'tamil_or_grantham'
    if letter.isalpha():
        return 'english'
    elif letter.isdigit():
        return 'digit'
    raise ValueError("Unknown letter '%s' neither Tamil nor English or number"%letter)

def print_tamil_words( tatext, use_frequencies = False ):
    taletters = get_letters(tatext)
    #for word in re.split(u"\s+",tatext):
    #    print(u"-> ",word)
    # tamil words only
    frequency = {}
    for pos,word in enumerate(get_tamil_words(taletters)):
        frequency[word] = 1 + frequency.get(word,0)
    #for key in frequency.keys():
    #    print(u"%s : %s"%(frequency[key],key))
    # sort words by descending order of occurence
    for l in sorted(frequency.iteritems(), key=operator.itemgetter(1)):
        if use_frequencies:
            print(u"%d -> %s"%(l[1],l[0]))
        else:
            print(u"%s"%l[0])

def tamil_sorted(list_data):
    if PYTHON3:
        asorted = sorted(list_data,key=functools.cmp_to_key(compare_words_lexicographic))
    else:
        asorted = sorted(list_data,cmp=compare_words_lexicographic)
    return asorted

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
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        self._cache = {}

    @abc.abstractmethod
    def get_letters_impl(self,word):
        raise NotImplementedError()

    def get_letters(self,word):
        """
        This is a cached implementation of get_letters.
        @word - can be a Tamil/English word (letter sequence)
        @return - list of letters in @word and cache for future use.
        """
        rval = self._cache.get(word,None)
        if not rval:
            rval = self.get_letters_impl(word)
            self._cache[word] = rval
        return rval
