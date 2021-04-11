# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# Licensed under GPL Version 3

import re
from . import utf8


# predicate
def is_containing_seq(start, end, seq):
    return (start in seq) and (end in seq)


# expand
def expand_sequence(start, end, seq):
    start_idx = seq.index(start)
    end_idx = seq.index(end)
    assert start_idx >= 0 and end_idx >= 0
    start_idx, end_idx = min(start_idx, end_idx), max(start_idx, end_idx)
    return u",".join(seq[start_idx: end_idx + 1])


def expand_tamil(start, end):
    """expand uyir or mei-letter range etc.
    i.e. அ-ஔ  gets converted to அ,ஆ,இ,ஈ,உ,ஊ,எ,ஏ,ஐ,ஒ,ஓ,ஔ etc.
    """
    # few sequences
    for seq in [
        utf8.uyir_letters,
        utf8.grantha_mei_letters,
        utf8.grantha_agaram_letters,
    ]:
        if is_containing_seq(start, end, seq):
            return expand_sequence(start, end, seq)
    # all Tamil letters
    seq = utf8.grantha_uyirmei_letters
    if is_containing_seq(start, end, seq):
        return expand_sequence(start, end, seq)

    raise Exception("Cannot understand sequence [%s-%s]" % (start, end))


def make_pattern(patt, flags=0):
    """
    returns a compile regular expression object
    """
    # print('input',len(patt))
    patt_letters = utf8.get_letters(patt)
    patt_out = list()
    idx = 0
    # print('output',len(patt_letters))
    patt = [None, None]
    prev = None
    LEN_PATT = len(patt_letters)
    while idx < LEN_PATT:
        if utf8.istamil(patt_letters[idx]) and (
                prev == "-" or ((idx + 1) < LEN_PATT and patt_letters[idx + 1] == u"-")
        ):
            if (idx + 1) < LEN_PATT and patt_letters[idx + 1] == u"-":
                patt[0] = patt_letters[idx]
                idx = idx + 2
                prev = "-"
            elif prev == "-":
                patt[1] = patt_letters[idx]
                patt_out.extend(expand_tamil(patt[0], patt[1]))
                idx = idx + 1
                prev = patt_letters[idx]
            continue
        patt_out.extend(patt_letters[idx])
        prev = patt_letters[idx]
        idx = idx + 1
    opattern = u"".join(patt_out)
    compile_regexp = re.compile(opattern, flags)
    return (compile_regexp, opattern)


def search(patt, inputstr):
    custom_patt = make_pattern(patt)
    return (re.search(custom_patt, inputstr), custom_patt)


def match(patt, inputstr):
    custom_patt = make_pattern(patt)[0]
    return (re.match(custom_patt, inputstr), custom_patt)
