# This Python file uses the following encoding: utf-8
# (C) 2020 Muthiah Annamalai
# This file is part of open-tamil project
import string
from tamil.utf8 import get_letters
from tamil.numeral import num2tamilstr


def normalize_numeral_text(text_tokens):
    """
    Input @text_tokens = ["இரு","நண்பர்கள்","௹","100","கொடுத்து","உணவு","உண்டனர்."]
                                                                                      ^   - எண் 100 என்பது சொல்வடிவில் நூறு என்று
    வெளியிடப்படும்.
    """
    rval = []
    for word in text_tokens:
        if (word[0] in string.digits) or word[0] == "-":
            try:
                val = num2tamilstr(word)
                rval.append(val)
            except Exception as e:
                rval.append(word)
        else:
            rval.append(word)
    return rval


def normalize_punctuation_text(text_tokens):
    """
    Input @text_tokens = ["இரு","நண்பர்கள்","௹","100","கொடுத்து","உணவு","உண்டனர்."]
                                                                             ^ ரூபாய் என்று மாற்றி வெளியிடப்படும்.
    """
    special_char_map = {
        "!": "ஆச்சரியக்குறி",
        "!=": "சமன்பாடு இல்லை",
        ",": "துணைக்குறி",
        "#": "எண்",
        "$": "டாலர்",
        "™": "முத்திரை",
        "©": "பதிப்புரிமை",
        "௹": "ரூபாய்",
        "₹": "ரூபாய்",
        "£": "பவுண்டு",
        "%": "சதவிகிதம்",
        "&": "மற்றும்",
        "*": "நட்சத்திரக்குறி",
        "(": "அடைப்புகுக்குறி தொடக்கம்",
        ")": "அடைப்புகுக்குறி முடிவு",
        "[": "அடைப்புகுக்குறி தொடக்கம்",
        "]": "அடைப்புகுக்குறி முடிவு",
        "{": "அடைப்புகுக்குறி தொடக்கம்",
        "}": "அடைப்புகுக்குறி முடிவு",
        "+": "கூட்டல்குறி",
        "-": "கழித்தல்குறி",
        "x": "பெருக்கல்குறி",
        "/": "வகுத்தல்குறி",
        "=": "சமன்பாடுக்குறி",
        ":": "புள்ளி",
        '"': "மேற்கோள்குறி",
        "'": "மேற்கோள்குறி",
        ";": "அரைப்புள்ளி",
        ".": "முற்றுப்புள்ளி",
        "?": "கேள்விக்குறி",
    }
    rval = []
    for char in text_tokens:
        rval.append(special_char_map.get(char, char))
    return rval
