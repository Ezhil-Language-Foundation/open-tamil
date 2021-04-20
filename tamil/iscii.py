# -*- coding: utf-8 -*-
#
# (C) 2015 Muthiah Annamalai
# Licensed under GPL Version 3
#

# *இஸ்கீ*
# ISCII-Tamil library provides the Tamil symbol table and mapping to Unicode
# A converter, for example, could be written based on this information.
#
# Ref: Wikipedia article on ISCII, or Tamil article இஸ்கீ

VERSION = "1"

# load ASCII 7-bit code page first
ISCII = list(map(lambda x: x < 128 and u"%c" % x or u"?", range(0, 256)))

# append ISCII tamil page on higher side

ISCII_DIRECT_LOOKUP = []

# Vowels, Consonants and Tamil numerals have bijective from ISCII into Unicode
# Sec. 1 - Vowels
ISCII[0xAB:0xB8] = [
    u"அ",
    u"ஆ",
    u"இ",
    u"ஈ",
    u"உ",
    u"ஊ",
    u"எ",
    u"ஏ",
    u"ஐ",
    u"ஒ",
    u"ஓ",
    u"ஔ",
    u"ஃ",
]
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0xAB, 0xB8))

# Sec. 2 - Consonants
ISCII[0xB8:0xCA] = [
    u"க",
    u"ங",
    u"ச",
    u"ஞ",
    u"ட",
    u"ண",
    u"த",
    u"ந",
    u"ப",
    u"ம",
    u"ய",
    u"ர",
    u"ல",
    u"வ",
    u"ழ",
    u"ள",
    u"ற",
    u"ன",
]
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0xB8, 0xCA))

# Grantha
ISCII[0x83] = u"ஜ"  # Je
ISCII[0x84] = u"\u0BB7"  # SSA - ஷ
ISCII[0x85] = u"\u0BB8"  # SA - ஸ
ISCII[0x86] = u"\u0BB9"  # HA - ஹ
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0x83, 0x87))

# Grantha/Mei forms
ISCII[0x88] = u"ஜ்"  # iJ
ISCII[0x89] = u"\u0BB7\u0BCD"  # iSS - ஷ்
ISCII[0x8A] = u"\u0BB8\u0BCD"  # iS - ஸ்
ISCII[0x8B] = u"\u0BB9\u0BCD"  # iH - ஹ்
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0x88, 0x8C))

# Sec. 3 - Tamil numerals
ISCII[0x80] = u"\u0BE6"  # Tamil digit 0 - ௦
ISCII[0x81] = u"\u0BE7"  # Tamil digit 1 - ௧
ISCII[0x8D] = u"\u0BE8"  # Tamil digit 2 - ௨
ISCII[0x8E] = u"\u0BE9"  # Tamil digit 3 - ௩
ISCII[0x8F] = u"\u0BEA"  # Tamil digit 4 - ௪
ISCII[0x90] = u"\u0BEB"  # Tamil digit 5 - ௫
ISCII[0x95] = u"\u0BEC"  # Tamil digit 6 - ௬
ISCII[0x96] = u"\u0BED"  # Tamil digit 7 - ௭
ISCII[0x97] = u"\u0BEE"  # Tamil digit 8 - ௮
ISCII[0x98] = u"\u0BEF"  # Tamil digit 9 - ௯
ISCII[0x9D] = u"\u0BF0"  # Tamil digit 10 - ௰ # Tamil people
ISCII[0x9E] = u"\u0BF1"  # Tamil digit 100 - ௱ # have a logarithmic
ISCII[0x9F] = u"\u0BF2"  # Tamil digit 1000 - ௲ # size of numerals - rich folks :-)
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0x80, 0xA0))

# Sec. 4 - in five parts for grantha, mei, ukaram, ookaram, di, and dii

# Sec. 4.1 - Grantha ligatures
ISCII[0x82] = u"\u0bb6\u0bcd\u0bb0\u0bc0"  # SRI - ஶ்ரீ
ISCII[0x87] = u"\u0b95\u0bcd\u0bb7"  # KSHA - க்ஷ
ISCII[0x8C] = u"\u0b95\u0bcd\u0bb7\u0bcd"  # KSH - க்ஷ்
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + [0x82, 0x87, 0x8C]

# Sec. 4.2 - Mei series
ISCII[0xEC:0xFE] = [
    u"க்",
    u"ங்",
    u"ச்",
    u"ஞ்",
    u"ட்",
    u"ண்",
    u"த்",
    u"ந்",
    u"ப்",
    u"ம்",
    u"ய்",
    u"ர்",
    u"ல்",
    u"வ்",
    u"ழ்",
    u"ள்",
    u"ற்",
    u"ன்",
]
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0xEC, 0xFF))

# கு ஙு சு ஞு  டு ணு து நு பு மு யு று லு வு ழு ளு னு  ரு

# Sec. 4.3 - Ukara series
ISCII[0xCC] = u"கு"
ISCII[0x99] = u"ஙு"
ISCII[0xCD] = u"சு"
ISCII[0x9A] = u"ஞு"
ISCII[0xCE:0xDC] = [
    u"டு",
    u"ணு",
    u"து",
    u"நு",
    u"பு",
    u"மு",
    u"யு",
    u"ரு",
    u"லு",
    u"வு",
    u"ழு",
    u"ளு",
    u"று",
    u"னு",
]
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0xCE, 0xDD))
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + [0xCC, 0x99, 0xCD, 0x9A]

# Sec. 4.4 - Ookara Series
# ஙூ ஞூ
# கூ சூ டூ ணூ தூ நூ பூ மூ யூ ரூ லூ வூ ழூ ளூ றூ னூ
ISCII[0x9B] = u"ஙூ"
ISCII[0x9C] = u"ஞூ"
ISCII[0xDC:0xEC] = [
    u"கூ",
    u"சூ",
    u"டூ",
    u"ணூ",
    u"தூ",
    u"நூ",
    u"பூ",
    u"மூ",
    u"யூ",
    u"ரூ",
    u"லூ",
    u"வூ",
    u"ழூ",
    u"ளூ",
    u"றூ",
    u"னூ",
]
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0xDC, 0xED))
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + [0x9B, 0x9C]

# Sec. 4.5 - Ligature symbols de, dee - unlike Dexter
ISCII[0xCA] = u"டி"
ISCII[0xCB] = u"டீ"
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + [0xCA, 0xCB]

# Sec. 5 - ligature glyph symbols for compound uyirmei encoding

# Sec. 5.1 - post modifiers
ISCII[0xA1] = u"ா"  # u"\u0BBE" - Aa
ISCII[0xA2] = u"ி"  # u"\u0BBF" - E
ISCII[0xA3] = u"ீ"  # u"\u0BC0" - I
ISCII[0xA4] = u"ு"  # u"\u0BC1" - u
ISCII[0xA5] = u"ூ"  # u"\u0BC2" - Oo
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0xA1, 0xA6))

# Sec. 5.2 - pre modifiers
ISCII[0xA6] = u"ெ"  # u"\u0BC6"
ISCII[0xA7] = u"ே"  # u"\u0BC7"
ISCII[0xA8] = u"ை"  # u"\u0BC8"

# Sec. 5.3 - two part modifiers - conversion rules
# 0xA6 + consonant_ISCII + 0xA1 -> consonant_Unicode + ொ #\u0BCA
# 0xA7 + consonant_ISCII + 0xA1 -> consonant_Unicode + ோ #\u0BCB
# 0xA6 + consonant_ISCII + 0xAA -> consonant_Unicode + ௌ #\u0BCC

ISCII[0xAA] = u"ௌ"  # its not exactly this symbol - but a composite mapping
ISCII_POST_MODIFIER = [0xAA, 0xA1]

ISCII_PRE_MODIFIER = [0xA6, 0xA7, 0xA8]

# Sec. 6 -  five other non-Tamil specific characters
ISCII[0x91] = u"\u2018"  # left single quote
ISCII[0x92] = u"\u2019"  # right single quote
ISCII[0x93] = u"\u201C"  # left single quote
ISCII[0x94] = u"\u201D"  # right single quot
ISCII[0xA9] = u"\u00A9"  # Copyright Sign

ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + list(range(0x92, 0x95)) + [0xA9]

# Sec. 7 - Backwards incompatibility
# vowel was moved from position 0xAD in ISCII 1.6 -> ISCII 1.7
ISCII[0xFE] = u"இ"
ISCII_DIRECT_LOOKUP = ISCII_DIRECT_LOOKUP + [0xFE]


# debugging utility
def print_table():
    print(u"<table>")
    for i in range(0, 16):
        print(
            u"<tr>"
            + u" ".join(
                [u"<td>%s</td>" % ISCII[p] for p in range(i * 16, (i + 1) * 16)]
            )
            + u"</tr>"
        )
    print(u"</table>")


## List based code uses as a look-ahead with 3-tokens before you decide to throw
## or convert the tokens into Unicode
def convert_to_unicode(tscii_input):
    """convert a byte-ASCII encoded string into equivalent Unicode string
    in the UTF-8 notation."""
    output = list()
    prev = None
    prev2x = None
    # need a look ahead of 2 tokens atleast
    for char in tscii_input:
        ## print "%2x"%ord(char) # debugging
        if ord(char) < 128:
            # base-ASCII copy to output
            output.append(char)
            prev = None
            prev2x = None

        elif ord(char) in ISCII_DIRECT_LOOKUP:
            if prev in ISCII_PRE_MODIFIER:
                curr_char = [ISCII[ord(char)], ISCII[prev]]
            else:
                # we are direct lookup char
                curr_char = [ISCII[ord(char)]]
                char = None

            output.extend(curr_char)

        elif ord(char) in ISCII_POST_MODIFIER:

            if (prev in ISCII_DIRECT_LOOKUP) and (prev2x in ISCII_PRE_MODIFIER):
                if len(output) >= 2:
                    del output[-1]  # we are reducing this token to something new
                    del output[-2]
                elif len(output) == 1:
                    del output[-1]
                else:
                    # nothing to delete here..
                    pass
                output.extend([ISCII[prev], ISCII[prev2x]])
            else:
                print("Warning: malformed ISCII encoded file; skipping characters")

            prev = None
            char = None
        else:
            # pass - must be one of the pre/post modifiers
            pass

        prev2x = prev
        if char:
            prev = ord(char)
    return u"".join(output)
