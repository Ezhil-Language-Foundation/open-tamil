# -*- coding: utf-8 -*-
#
# (C) முத்தையா அண்ணாமலை 2015
#
# N-gram language model for Tamil words

import tamil


def get_ngram_groups(word, n=1):
    # makes no sense - but can happen

    letters = tamil.utf8.get_letters(word)
    L = len(letters)
    if n >= L:
        return [word]

    if n == 1:
        return letters

    result = []
    for i in range(0, L - n + 1):
        result.append(u"".join(letters[i: min(i + n, L)]))
    return result
