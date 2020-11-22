## -*- coding: utf-8 -*-
## (C) 2020 Muthiah Annamalai
##
from tamil.utf8 import get_letters
from tamil.utils.santhirules import joinWords

def make_plural(peyar):
    # கூட்டுப்பெயர்களுக்கு மட்டுமே இது சேறும்.
    return joinWords(peyar, "கள்")

def make_possessive_1(peyar):
    return joinWords(peyar, "இன்")

def make_possessive_2(peyar):
    return joinWords( make_possessive_1(peyar) , "அது")

def make_possessive_3(peyar):
    return joinWords(peyar,"ற்கு")

def make_possessive_4(peyar):
    return joinWords(peyar,"ஆல்")

def make_all_variants(பெயர்):
    return [_சார்பு(பெயர்) for _சார்பு in [make_plural,make_possessive_1,make_possessive_2,\
                    make_possessive_3,make_possessive_4]]
