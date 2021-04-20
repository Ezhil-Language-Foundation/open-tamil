## -*- coding: utf-8 -*-
# (C) 2015-2016 Muthiah Annamalai
#  <ezhillang@gmail.com>
#
# This function provides a list of alternatives for downstream use as suggestor in
# the Tamil spelling modules/programs

# Ref: http://norvig.com/spell-correct.html
from tamil.utf8 import (
    tamil_letters,
    get_letters,
    mei_letters,
    agaram_letters,
    sanskrit_letters,
    sanskrit_mei_letters,
    uyir_letters,
)

from pprint import pprint


def norvig_suggestor(word, alphabets=None, nedits=1, limit=float("inf")):
    if not alphabets:
        alphabets = tamil_letters
    if not type(word) is list:
        wordL = get_letters(word)
    else:
        wordL = word
    # recursive method for edit distance > 1
    if nedits > 1:
        result = []
        for nAlternate in norvig_suggestor(
            wordL, alphabets, nedits - 1, limit - len(result)
        ):
            if len(result) > limit:
                break
            result.extend(
                norvig_suggestor(nAlternate, alphabets, 1, limit - len(result))
            )
        return set(result)

    ta_splits = [
        [u"".join(wordL[: idx - 1]), u"".join(wordL[idx:])]
        for idx in range(len(wordL) + 1)
    ]
    # pprint( ta_splits )
    ta_deletes = [a + b[1:] for a, b in ta_splits if b]
    ta_transposes = [a + b[1] + b[0] + b[2:] for a, b in ta_splits if len(b) > 1]
    ta_replaces = [a + c + b[1:] for a, b in ta_splits for c in alphabets]
    ta_replaces2 = [c + b for a, b in ta_splits for c in alphabets]
    ta_inserts = [a + c + b for a, b in ta_splits for c in alphabets]
    # TODO: add a normalizing pass word words in vowel+consonant forms to eliminate dangling ligatures
    return set(ta_deletes + ta_transposes + ta_replaces + ta_replaces2 + ta_inserts)
