# -*- coding: utf-8 -*-
# 
# (C) 2013 Muthiah Annamalai
# Licensed under GPL Version 3
# 

# 
# TSCII library provides the TSCII v1.7 symbol table and mapping to Unicode
# A converter, for example, could be written based on this information.
# 
# Ref: M. Nedumaran, "Text conversion from TSCII 1.7 to Unicode," (2007).

# load ASCII 7-bit code page first
TSCII = map( lambda x:  x < 128 and u"%c"%x or u"?" , range(0,256))

# append TSCII tamil page on higher side

# Vowels, Consonants and Tamil numerals have bijective from TSCII into Unicode 
# Sec. 1 - Vowels
TSCII[0xAB:0xB8] = [u"அ",u"ஆ",u"இ",u"ஈ",u"உ",u"ஊ",u"எ",u"ஏ",u"ஐ",u"ஒ",u"ஓ",u"ஔ",u"ஃ"]

# Sec. 2 - Consonants
TSCII[0xB8:0xCA] = [u"க",u"ங",u"ச",u"ஞ",u"ட",u"ண",u"த",u"ந",
                    u"ப",u"ம",u"ய",u"ர",u"ல",u"வ",u"ழ",u"ள",
                    u"ற",u"ன",]

# Grantha 
TSCII[0x84] = u"\u0BB7" # SSA - ஷ
TSCII[0x85] = u"\u0BB8" # SA - ஸ
TSCII[0x86] = u"\u0BB9" # HA - ஹ

# Sec. 3 - Tamil numerals
TSCII[0x80] = u"\u0BE6" # Tamil digit 0 - ௦
TSCII[0x81] = u"\u0BE7" # Tamil digit 1 - ௧
TSCII[0x8D] = u"\u0BE8" # Tamil digit 2 - ௨
TSCII[0x8E] = u"\u0BE9" # Tamil digit 3 - ௩
TSCII[0x8F] = u"\u0BEA" # Tamil digit 4 - ௪
TSCII[0x90] = u"\u0BEB" # Tamil digit 5 - ௫
TSCII[0x95] = u"\u0BEC" # Tamil digit 6 - ௬
TSCII[0x96] = u"\u0BED" # Tamil digit 7 - ௭
TSCII[0x97] = u"\u0BEE" # Tamil digit 8 - ௮
TSCII[0x98] = u"\u0BEF" # Tamil digit 9 - ௯ 
TSCII[0x9D] = u"\u0BF0" # Tamil digit 10 - ௰ # Tamil people 
TSCII[0x9E] = u"\u0BF1" # Tamil digit 100 - ௱ # have a logarithmic 
TSCII[0x9F] = u"\u0BF2" # Tamil digit 1000 - ௲ # size of numerals - rich folks :-)

# Sec. 4 - in five parts for grantha, mei, ukaram, ookaram, di, and dii

# Sec. 4.1 - Grantha ligatures
TSCII[0x82] = u"\u0bb6\u0bcd\u0bb0\u0bc0" #SRI - ஶ்ரீ
TSCII[0x87] = u"\u0b95\u0bcd\u0bb7" #KSHA - க்ஷ
TSCII[0x8C] = u"\u0b95\u0bcd\u0bb7\u0bcd" #KSH - க்ஷ்

# Sec. 4.2 - Mei series
TSCII[0xEC:0xFE] = [u"க்",u"ங்",u"ச்",u"ஞ்",u"ட்",u"ண்",u"த்",u"ந்",
                    u"ப்",u"ம்",u"ய்",u"ர்",u"ல்",u"வ்",u"ழ்",u"ள்",
                    u"ற்",u"ன்"]

# கு ஙு சு ஞு  டு ணு து நு பு மு யு று லு வு ழு ளு னு  ரு

# Sec. 4.3 - Ukara series
TSCII[0xCC] = u"கு"
TSCII[0x99] = u"ஙு"
TSCII[0xCD] = u"சு"
TSCII[0x9A] = u"ஞு"
TSCII[0xCE:0xDC] = [u"டு", u"ணு", u"து", u"நு", u"பு", u"மு", u"யு",u"ரு", u"லு", u"வு", u"ழு", u"ளு", u"று", u"னு"]

# Sec. 4.4 - Ookara Series
# ஙூ ஞூ 
# கூ சூ டூ ணூ தூ நூ பூ மூ யூ ரூ லூ வூ ழூ ளூ றூ னூ
TSCII[0x9B] = u"ஙூ"
TSCII[0x9C] = u"ஞூ"
TSCII[0xDC:0xEC] = [u"கூ", u"சூ",u"டூ",u"ணூ",u"தூ",u"நூ",u"பூ",u"மூ",u"யூ",u"ரூ", u"லூ", u"வூ",u"ழூ",u"ளூ",u"றூ",u"னூ"]

# Sec. 4.5 - Ligature symbols de, dee - unlike Dexter
TSCII[0xCA] = u"டி"
TSCII[0xCB] = u"டீ"

# Sec. 5 - ligature glyph symbols for compound uyirmei encoding

# Sec. 5.1 - post modifiers
TSCII[0xA1] = u"ா" # u"\u0BBE" - Aa
TSCII[0xA2] = u"ி" #u"\u0BBF" - E
TSCII[0xA3] = u"ீ" #u"\u0BC0" - I
TSCII[0xA4] = u"ு" #u"\u0BC1" - u
TSCII[0xA5] = u"ூ" #u"\u0BC2" - Oo

# Sec. 5.2 - pre modifiers
TSCII[0xA6] = u"ெ" #u"\u0BC6" 
TSCII[0xA7] = u"ே" #u"\u0BC7" 
TSCII[0xA8] = u"ை" #u"\u0BC8"

# Sec. 5.3 - two part modifiers - conversion rules
# 0xA6 + consonant_TSCII + 0xA1 -> consonant_Unicode + ொ #\u0BCA
# 0xA7 + consonant_TSCII + 0xA1 -> consonant_Unicode + ோ #\u0BCB
# 0xA6 + consonant_TSCII + 0xAA -> consonant_Unicode + ௌ #\u0BCC

TSCII[0xAA] = u"ௌ"

# Sec. 6 -  five other non-Tamil specific characters
TSCII[0x91] = u"\u2018" #left single quote
TSCII[0x92] = u"\u2019" #right single quote
TSCII[0x93] = u"\u201C" #left single quote
TSCII[0x94] = u"\u201D" #right single quot
TSCII[0xA9] = u"\u00A9" #Copyright Sign

# Sec. 7 - Backwards incompatibility
# vowel was moved from position 0xAD in TSCII 1.6 -> TSCII 1.7
TSCII[0xFE] = u"இ"

# debugging utility
def print_table():
    print "<table>"
    for i in range(0,16):
        print u"<tr>"+u" ".join([u"<td>%s</td>"%TSCII[p] for p in range(i*16,(i+1)*16)])+u"</tr>"
    print "</table>"
