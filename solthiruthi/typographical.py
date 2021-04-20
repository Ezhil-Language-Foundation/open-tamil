## -*- coding: utf-8 -*-
## (C) 2019 Muthiah Annamalai
## This module is part of solthiruthi project under open-tamil umbrella.
## This code maybe used/distributed under MIT LICENSE.

# This file implements an algorithm to eliminate any typographical
# errors from keyboard model, for an input word containing perhaps
# only a typographical errors.
#

# e.g. Input with 1 typographical error maybe:
# பழரதம் when used intended to type பழரசம் in the Tamil 99 keyboard
#
from tamil.utf8 import get_letters_elementary, pulli_symbols
from .dictionary import Dictionary
import copy


# explore all edit distances - i.e. len(word_in) or only upto value in ed.
# we can restrict the edit distance search to any value from [1-N]
def oridam_generate_patterns(word_in, cm, ed=1, level=0, pos=0, candidates=None):
    """ ed = 1 by default, pos - internal variable for algorithm """
    alternates = cm.get(word_in[pos], [])
    if not candidates:
        candidates = []
    assert ed <= len(
        word_in
    ), "edit distance has to be comparable to word size [ins/del not explored]"
    if (pos > len(word_in)) or ed == 0:
        return candidates
    pfx = ""
    sfx = ""
    curr_candidates = []
    for p in range(0, pos):
        pfx = pfx + word_in[p]
    for p in range(pos + 1, len(word_in)):
        sfx = sfx + word_in[p]
    for alt in alternates:
        word_alt = pfx + alt + sfx
        if not (word_alt in candidates):
            candidates.append(word_alt)
            curr_candidates.append(word_alt)
    for n_pos in range(pos, len(word_in)):
        # already what we have ' candidates ' of this round are edit-distance 1
        for word in curr_candidates:
            oridam_generate_patterns(word, cm, ed - 1, level + 1, n_pos, candidates)
    if level == 0:
        # candidates.append(word_in)
        for n_pos in range(pos, len(word_in)):
            oridam_generate_patterns(word_in, cm, ed, level + 1, n_pos, candidates)
    return candidates


def corrections(word_in, dictionary, keyboard_cm, ed=2):
    """
    @input: word_in - input word
         dictionary - dictionary/lexicon
         keyboard_cm - confusion matrix for keyboard in question
    """
    assert isinstance(dictionary, Dictionary)
    candidates = oridam_generate_patterns(word_in, keyboard_cm, ed)
    # TBD: score candidates by n-gram probability of language model occurrence
    # etc. or edit distance from source word etc.
    return list(filter(dictionary.isWord, candidates))
