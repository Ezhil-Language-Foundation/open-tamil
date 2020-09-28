## -*- coding: utf-8 -*-
# (C) 2020 முத்து அண்ணாமலை
# https://en.wikipedia.org/wiki/ITRANS
from tamil.utf8 import uyirmei_letters, uyir_letters,  splitMeiUyir
from collections import OrderedDict
_uyir = (("அ","a"),
    ("ஆ",("aa","A")),
    ("இ","i"),
    ("ஈ",("ee","I")),
     ("உ","u"),
     ("ஊ",("oo","U")),
    ("எ","e"),
    ("ஏ",("ae", "E")),
    ("ஐ","ai"),
    ("ஒ","o"),
    ("ஓ",("oa","O")),
    ("ஔ","au"))
_aytham = (("ஃ",("H","Ahh")),)
_mei = (("க்",("k", "kh", "g", "c")),
("ங்","nG"),
("ச்","ch"),
("ஜ்","j"),
("ஞ்","nY"),
("ட்",("d","t")),
("ண்","nN"),
("த்",("dh","dt")),
("ந்","N"),
("ன்","n"),
("ப்",("b","bh","p")),
("ம்","m"),
("ய்","y"),
("ர்","r"),
("ற்","R"),
("ல்","l"),
("ள்","L"),
("ழ்",("z","zh")),
("வ்",("v","w")),
("ஷ்","sh"),
("ஸ்","s"),
("ஹ்","h"),
("ஃப்","f"))

class Transliteration:
    """
    ITRANS encoding formats.
    """
    table = OrderedDict()#{}

def _options(_ref,_sym):
    _v = []
    for _k,_v in _ref:
        if _k == _sym: break
    return _v

for ta_map in [_uyir,_mei,_aytham]:
    for obj in ta_map:
        ta,en=obj[0],obj[1]
        if not isinstance(en,(list,tuple)):
            en = list(en)
        for e in en:
            Transliteration.table[e] = ta

# mix of consonants and compound - uyirmei - letters
for vc in uyirmei_letters:
    c,v = splitMeiUyir(vc)
    for vo in _options(_uyir,v):
        for co in _options(_mei,c):
            if not Transliteration.table.get(co+vo,None):
                Transliteration.table[co+vo] = vc
            elif False:#elif not vc in Transliteration.table.values():
                #print("clobbered ",co+vo,Transliteration.table[co+vo],vc)
                Transliteration.table[co+vo]=vc

#from pprint import pprint
#pprint(Transliteration.table)
#print(len(Transliteration.table))
