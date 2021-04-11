#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################################
# (C) 2014 Arulalan.T <arulalant@gmail.com>                                  #
#                                                                            #
# Written By : Arulalan.T <arulalant@gmail.com>                              #
# Date : 02.08.2014                                                          #
#                                                                            #
# This file is part of oepn-tamil/txt2ipa                                    #
#                                                                            #
# txt2ipa is free software: you can redistribute it and/or                   #
# modify it under the terms of the GNU General Public License as published by#
# the Free Software Foundation, either version 3 of the License, or (at your #
# option) any later version. This program is distributed in the hope that it #
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty#
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General#
# Public License for more details. You should have received a copy of the GNU#
# General Public License along with this program. If not, see                #
# <http://www.gnu.org/licenses/>.                                            #
#                                                                            #
##############################################################################

import re


# Convert Tamil text into romanized encoding using transliteratoin.php before apply any
# of the functions below


def ipa(text):  # Generates narrow transcription of Tamil texts

    text = " " + text + " "
    #    text = """ %s """ % text

    # Move Punctuations
    repl = lambda m: " " + m.group(1) + " "
    text = re.sub('([\\,\\\,\.\!\?"\'"\(\)])', repl, text)
    # text = re.sub("/(?<=[\w])([\\,\.\!\?\"\'\"\(\)])/",repl,text)
    # text = re.sub("/([\\,\.\!\?\"\'\"\(\)])(?=[\w])/",repl,text)

    # The comments below refer to the implementation of transcription rules as described in the
    # book - Panniru Thirumurai Olipeyarppu by Punal K Murugaiyan

    # Dipthongs

    text = text.replace("ai", "ay")  # 5.3.3.1 ii Palatal Approximant ... # ai

    text = text.replace("au", "av")  # au - dipthong replacement

    # Grantha

    text = text.replace("j", "ʤ")
    text = text.replace("h", "ɦ")
    text = text.replace("S", "ʂ")
    text = text.replace("srI", "ʂrI")

    # Mey

    # Vallinam

    # pa

    text = re.sub(
        r"(?<=[aAiIuUeEoO])p(?=[aAiIuUeEoO])", "β", text
    )  # 5.3.1.6 iii Voiced Bilabial Fricative
    text = re.sub(r"(?<=[yrlvZL])p", "β", text)  # 5.3.1.6 iii

    text = re.sub(r"(?<=[GJnVmN])p", "b", text)  # 5.3.1.6 ii voiced bilabial plosive

    # 5.3.1.6 i no replacement

    # ta

    text = re.sub(
        r"(?<=[aAiIuUeEoOyrlvZL])t(?=[aAiIuUeEoO])", "ð", text
    )  # 5.3.1.5 iii Voiced dental Fricative

    text = re.sub(r"(?<=[nV])t", "d̪", text)  # 5.3.1.5 ii Voiced dental plosive

    text = re.sub(r"t", "t̪", text)  # 5.3.1.5 i Voiceless dental plosive

    # Ra

    text = text.replace("XX", "t̺t̺ʳ")  # 5.3.1.4 ii & ii find correct name

    text = re.sub(r"(?<=V)X", "d̺ʳ", text)  # 5.3.1.4 iii

    # 5.3.1.4 iv & v implemented in idaiyinam section

    # Ta

    text = re.sub(
        r"(?<=[aAiIuUeEoO])T(?=[aAiIuUeEoO])", "ɽ", text
    )  # 5.3.1.3 iii Retroflex Flap

    text = re.sub(r"(?<=[N])T", "ɖ", text)  # 5.3.1.3 ii Voiced Retroflex Plosive | VT ?

    text = text.replace("T", "ʈ")  # 5.3.1.3 i Voiceless Retroflex Plosive

    # ca

    text = re.sub(
        r"(?<=[aAiIuUeEoOl])c(?=[aAiIuUeEoO])", "s", text
    )  # 5.3.1.2 iii voiceless alveolar fricatives

    repl = lambda m: m.group(1) + "s"
    text = re.sub(r"(\s)c", repl, text)  # 5.3.1.2 iii

    text = re.sub(r"(V)c", repl, text)

    text = re.sub(
        r"(?<=[J])c", "ʤ", text
    )  # 5.3.1.2 ii Voiced Post Alveolar affricate - Symbol Changed : d͡ʒ

    text = re.sub(
        r"c", "ʧ", text
    )  # 5.3.1.2 i Voicless Post Alveolar Affrivate - Symbol Changed : t͡ʃ

    # ka

    text = re.sub(r"Gk(?=[iI])", "ŋʲgʲ", text)  # 5.3.2.1 ii Palatized Velar Nasal

    text = text.replace("Gk", "ŋg")  # 5.3.2.1 Velar Nasal

    text = re.sub(
        r"(?<=[aAiIuUeEoO])k(?=[iI])", "ç", text
    )  # 5.3.1.1 viii voiceless palatal fricative

    # yrZlLv assumed above. Missing in definiation : eykiya -> eyçiya  aarkiya -> aarçiya....

    text = re.sub(
        r"(?<=r)k(?=[aAuUeEoO])", "ɣ", text
    )  # 5.3.1.1 Vii Voiced Velar Fricative

    text = re.sub(
        r"(?<=[aAiIuUeEoO])k(?=[aAuUeEoO])", "x", text
    )  # 5.3.1.1 vi Voicless Velar Fricative

    text = re.sub(r"(?<=[ylvZL])k(?=[aAuUeEoO])", "x", text)  # above

    text = re.sub(r"ykk", "jcc", text)  # 5.3.1.1 v voiceless palatal plosive

    text = re.sub(r"jkk", "jcc", text)  # above

    text = re.sub(
        r"(?<=[rylvZLGVNaAiIuUeEoO])k(?=[iI])", "gʲ", text
    )  # 5.3.1.1 iv Voiced Palatized Velar Plosive

    text = re.sub(
        r"(?<=[NVmn])k(?=[aAuUeEoO])", "g", text
    )  # 5.3.1.1 iii voiced velar plosive

    text = re.sub(r"(?<=k)k(?=[iI])", "kʲ", text)  # 5.3.1.1 ii Voiceless velar plosive

    # 5.3.1.1 i no relacement #

    # Idaiyinam

    text = text.replace("Z", "ɻ")  # 5.3.3.6  Retroflex Approximant

    text = re.sub(
        r"(?<=[aAiIuUeEoO])L(?=[aAiIuUeEoO])", "ɭʼ", text
    )  # 5.3.3.5 i Lateral Approximant - Ejective

    text = text.replace("L", "ɭ")  # 5.3.3.5 ii Lateral Approximant

    # 5.3.3.4 no change

    text = re.sub(
        r"(?<=[aAiIuUeEoO])[rX](?=[aAiIuUeEoO])", "ɾ", text
    )  # 5.3.3.3 i Alveolar Tap

    # 5.3.3.3 ii - pure consonant r - no replacement

    text = re.sub(r"X(?!=[aAiIuUeEoO])", "r", text)  # 5.3.3.3 ii Trill

    text = re.sub(
        r"(?<=[aAiIuUeEoO])v(?=[aAiIuUeEoO])", "ʋ", text
    )  # 5.3.3.2 ii labio-dental approximant
    text = re.sub(
        r"(\s)v(?=[aAiIuUeEoO])", lambda m: m.group(1) + "ʋ", text
    )  # 5.3.3.2 ii
    text = text.replace(
        "vv", "ʊ̯ʋ"
    )  # 5.3.3.2 i near-close near-back rounded vowel - part of a dipthong
    text = text.replace("v", "ʋ")

    text = re.sub(
        r"yy", "jɪ̯", text
    )  # 5.3.3.1 i near-close near-front unrounded vowel - part of a dipthong
    text = re.sub(
        r"y", "ɪ̯", text
    )  # 5.3.3.1 i near-close near-front unrounded vowel - part of a dipthong

    # Mellinam

    # 5.3.2.6 no replacement

    text = re.sub(
        r"[Vn]", "n̺", text
    )  # 5.3.2.4 Alveolar Nasal (Check Actual name in Wikipedia)

    text = text.replace("n̺d̪", "n̪d̪")  # 5.3.2.5 Dental Nasal

    text = re.sub(
        r"(?<=[aAiIuUeEoO])N(?=[aAiIuUeEoO])", "ɳʼ", text
    )  # 5.3.2.3 ii Retroflex Nasal Ejective

    text = text.replace("N", "ɳ")  # 5.3.2.3 Retroflex Nasal

    text = text.replace("J", "ɲ")  # 5.3.2.3 Palatal Nasal

    text = re.sub(r"GG(?=[iI])", "ŋʲŋʲ", text)  # Assumed based on above

    text = text.replace("GG", "ŋŋ")  # Assumed based on above

    text = text.replace("G", "ŋ")  # Assumed based on above

    # Uyir

    # Seperate Pure Vowel Combinations

    text = re.sub(
        r"([aAiIuUeEoO])([aAiIuUeEoO])", lambda m: m.group(1) + "_" + m.group(2), text
    )

    # return text

    # Long O

    text = re.sub(r"o(\s)", lambda m: "o·" + m.group(1), text)  # 5.2.5.2 v

    text = re.sub(r"(\s)o(?!·)", lambda m: m.group(1) + "ʷoː", text)  # 5.2.5.2 iii
    text = re.sub(r"_o(?!·)", "ʷoː", text)  # 5.2.5.2 iii - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·])o(?![ː·])", "oː", text)  # 5.2.5.2 i

    # Short o

    text = re.sub(r"(\s)O(?!·)", lambda m: m.group(1) + "ʷo̞", text)  # 5.2.5.1 iii
    text = re.sub(r"_O(?!·)", "ʷo̞", text)  # 5.2.5.1 iii - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·̞])O(?![ː·])", "o̞", text)  # 5.2.5.1 i

    # Adding extra symbol for Retroflex Consonants

    retroflex = ["ɽ", "ɖ", "ʈ", "ɳ", "ɭ", "ɻ"]

    for rf in retroflex:
        text = re.sub("/̞(?=" + rf + ")", "̞˞", text)

    # Long e

    text = re.sub(r"e(\s)", lambda m: "e·" + m.group(1), text)  # 5.2.4.2 v

    text = re.sub(r"(\s)e(?!·)", lambda m: m.group(1) + "ʲeː", text)  # 5.2.4.2 iii
    text = re.sub(r"_e(?!·)", "ʲeː", text)  # 5.2.4.2 iii - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·̞])e(?![ː·])", "eː", text)  # 5.2.5.2 i

    # short e

    text = re.sub(r"(\s)E(?!·)", lambda m: m.group(1) + "ʲɛ̝", text)  # 5.2.4.1 iii
    text = re.sub(r"_E(?!·)", "ʲɛ̝", text)  # 5.2.4.1 iii - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·̞̝])E(?![ː·])", "ɛ̝", text)  # 5.2.5.4 i

    # Adding extra symbol for Retroflex Consonants

    for rf in retroflex:
        text = re.sub("/̝(?=" + rf + ")", "̝˞", text)

    # short u

    text = re.sub(
        r"(?<!u)(\S)(?<![bʋpmβ])u", lambda m: m.group(1) + "ɨ", text
    )  # 5.2.3.1 v

    text = re.sub(r"(\s)u(?!·)", lambda m: m.group(1) + "ʷʊ", text)  # 5.2.3.1 iii

    text = re.sub(r"_u(?!·)", "ʷʊ", text)  # 5.2.3.1 iii - puththi_Ottum

    text = re.sub(
        r"(?<!u\S)([bʋpmβ])u", lambda m: m.group(1) + "ʉ̩", text
    )  # 5.2.3.1  Vii

    text = re.sub(r"([bʋpβm])u", lambda m: m.group(1) + "ʉ̩", text)  # 5.2.3.1  Vii

    text = re.sub(r"(?<![bʋpβm])u(\s)", lambda m: "ɨ" + m.group(1), text)  # 5.2.3.1 v

    repl = lambda m: m.group(1) + m.group(2) + "ʊ"

    text = re.sub(r"(\s)(\S)(ɨ|ʉ̩)", repl, text)  # 5.2.5.2 i

    text = re.sub(r"(U)(\S{1,2})ɨ", repl, text)  # 5.2.5.2 i

    text = re.sub(r"(ʊ)(\S{1,2})ɨ", repl, text)

    text = re.sub(r"(ʊ)(\S{1,2})ʉ̩", repl, text)

    text = re.sub(r"(?<![bʋβpm])ʊ(\s)", lambda m: "ɨ" + m.group(1), text)  # 5.2.3.1 v

    text = re.sub(r"(?<=[bʋβpm])ʊ(\s)", lambda m: "ʉ̩" + m.group(1), text)

    for rf in retroflex:
        text = re.sub(r"ʊ(?=" + rf + ")", "ʊ˞", text)

    for rf in retroflex:
        text = re.sub(r"ʉ̩(?=" + rf + ")", "ʉ̩˞", text)

    for rf in retroflex:
        text = re.sub(r"ɨ(?=" + rf + ")", "ɨ˞", text)

    #

    text = re.sub(r"\S(<=!u)\Su", "ɨ", text)  # 5.2.3.1 v

    # Long u

    text = re.sub(r"U(\s)", lambda m: "u·" + m.group(1), text)  # 5.2.3.2 v

    text = re.sub(r"(\s)U(?!·)", lambda m: m.group(1) + "ʷuː", text)  # 5.2.3.2 iii
    text = re.sub(r"_U(?!·)", "ʷuː", text)  # 5.2.3.2 iii - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·̞̝])U(?![ː·])", "uː", text)  # 5.2.3.2 i

    # short i

    text = re.sub(r"i(\s)", lambda m: "ɪ·" + m.group(1), text)  # 5.2.2.1 iii

    text = re.sub(r"(\s)i(?!·)", lambda m: m.group(1) + "ʲɪ", text)  # 5.2.4.2 iii
    text = re.sub(r"_i(?!·)", "ʲɪ", text)  # 5.2.4.2 iii - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·̞̝])i(?![ː·])", "ɪ", text)  # 5.2.5.2 i

    for rf in retroflex:
        text = re.sub(r"ɪ(?=" + rf + ")", "ɪ˞", text)

    # Long i

    text = re.sub(r"I(\s)", lambda m: "i·" + m.group(1), text)  # 5.2.2.2 v

    text = re.sub(r"(\s)I(?!·)", lambda m: m.group(1) + "ʲiː", text)  # 5.2.2.2 iii
    text = re.sub(r"_I(?!·)", "ʲiː", text)  # 5.2.2.2 iii - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·̞̝])I(?![ː·])", "iː", text)  # 5.2.2.2 i

    # Long A

    text = re.sub(r"(\s)A(?!·)", lambda m: m.group(1) + "ˀɑː", text)  # 5.2.1.2 iii
    text = re.sub(r"_A(?!·)", "ˀɑː", text)  # 5.2.1.2 iii - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·̞̝])A(?![ː·])", "ɑː", text)  # 5.2.1.2 i

    # short a

    # Transcription of Abbreviation Ignored

    text = re.sub(r"(\s)a(?!·)", lambda m: m.group(1) + "ˀʌ", text)  # 5.2.1.1 vi
    text = re.sub(r"_a(?!·)", "ˀʌ", text)  # 5.2.1.1 vi - puththi_Ottum

    text = re.sub(r"(?<![aAiIuUeEoOː·̞̝])a(?![ː·])", "ʌ", text)  # 5.2.1.1 i

    text = re.sub(r"ʌ(\s)", lambda m: "ə" + m.group(1), text)  # 5.2.1.1 iii

    for rf in retroflex:
        text = re.sub(r"ʌ(?=" + rf + ")", "ʌ˞", text)

    # Aytham

    text = text.replace("K", "x")
    text = text.replace("xt̪", "xð")
    text = text.replace("xk", "xx")

    # Adding extra symbol for Retroflex Consonants Common of U & O

    # Regex won't accept (?=[Multiple Unicode Chars]) so separating each charcter

    for rf in retroflex:
        text = re.sub(r"ː(?=" + rf + ")", "˞ː", text)

    # Fixing kaaZBbu kaLaip kaLaippu bugs

    text = text.replace("βp", "pp")
    text = text.replace("β ", "p ")
    text = re.sub(
        r"ʧ([ \n])s", lambda m: "ʧ" + m.group(1) + "ʧ", text
    )  # ac samayam -> ac camayam \\ Check with Newlines ac \n samayam

    # New IPA Convensions

    text = text.replace("ː", "ː")
    text = text.replace("·", "ˑ")  #
    text = text.replace("ʧ", "tʃ")
    text = text.replace("ʤ", "dʒ")

    # ɨɭ (i- + Refelex -> <u> <Retroflex>

    text = text.lstrip()

    return text


# end of def ipa(text):

# Converts a narrow transcription to a broad transcription


def broad(text):
    # Remove Palatalization,
    # text = text.replace("ʲ","ʷ",)  Labialization & Glottalization
    # text = text.replace("ʷ","")
    text = text.replace("˞", "")  # Remove Retroflexion of Vowels
    text = text.replace("ʼ", "")  # Remove ejectives
    # Remove vowel position
    text = text.replace("̝", "")
    text = text.replace("̞", "")
    text = text.replace("̩", "")
    text = text.replace("ˀ", "")

    text = text.replace("ɨ", "ʉ")

    # Replacing narrow transcriptions of Consonants

    text = text.replace("ɣ", "g")  # Voiced Velar Fricative to Voiced Velar Plosive
    text = text.replace(
        "β", "b"
    )  # Voiced Bilabial Fricative to Voiced Bilabial Plosive
    text = text.replace(
        "ç", "x"
    )  # Voiceless Palatal Fricative to Voiceless Velar Fricative
    text = text.replace(
        "ʊ̯", "ʋ"
    )  # Non-syllabic near-close near-back rounder vowel to Labio-velar approximant
    text = text.replace("ð", "d̪")  # Voiced Dental Fricative to Voiced dental plosive
    text = text.replace("ɽ", "ɖ")  # Retroflex flap to Voiced Retroflex plosive
    text = text.replace(
        "c", "k"
    )  # Voiceless palatal plosive to Voiceless velar plosive
    text = text.replace("n̺", "n")

    text = text.replace("x", "g")

    text = text.replace("ŋʲ", "ŋ")
    text = text.replace("gʲ", "g")
    text = text.replace("kʲ", "k")

    text = text.replace("ɪ̯", "j")

    text = text.replace("ʌ", "ə")

    return text

# end of def broad(text):
