# -*- coding: utf-8 -*-
#
# (C) முத்தையா அண்ணாமலை 2013-2015
#
# N-gram language model for Tamil letters
# This module contains edit_distance, similarity scoring modules.

import tamil


def edit_distance(wordA, wordB):
    """ " Implements Daegmar-Levenshtein edit distance algorithm to find distance between words
    @wordA, and @wordB:
    Ref: https://en.wikipedia.org/wiki/Edit_distance
    Ref: https://en.wikipedia.org/wiki/Levenshtein_distance"""
    if not isinstance(wordA,list):
        lettersA = tamil.utf8.get_letters(wordA)
    else:
        lettersA = wordA

    if not isinstance(wordB,list):
        lettersB = tamil.utf8.get_letters(wordB)
    else:
        lettersB = wordB
    n_A = len(lettersA)
    n_B = len(lettersB)
    dist_AB = [[0 for i in range(0, n_B + 1)] for i in range(0, (n_A + 1))]
    # Target prefix reached by insertion
    for j in range(1, n_B + 1):
        dist_AB[0][j] = j
    for i in range(1, n_A + 1):
        dist_AB[i][0] = i
    for j in range(1, n_B + 1):
        for i in range(1, n_A + 1):
            if lettersA[i - 1] == lettersB[j - 1]:
                new_dist = dist_AB[i - 1][j - 1]
            else:
                new_dist = min(
                    [
                        dist_AB[i - 1][j] + 1,
                        dist_AB[i][j - 1] + 1,
                        dist_AB[i - 1][j - 1] + 1,
                    ]
                )  # del, ins, or sub
            dist_AB[i][j] = new_dist
    return dist_AB[-1][-1]


def Jaccard_coeff(*args):
    """
    # Jaccard coeff - similarity score for two words @wordA, @wordB
    # https://en.wikipedia.org/wiki/Jaccard_index
    """
    return 1.0 - Dice_coeff(*args)


def Dice_coeff(wordA, wordB):
    """
    # Calculate edit-distance - Implements the Dice coefficent
    # Ref: https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient
    # distance should be between 0 - 1.0. can be used as a similarity match
    """
    if not type(wordA) is list:
        lettersA = tamil.utf8.get_letters(wordA)
    else:
        lettersA = wordA

    if not type(wordB) is list:
        lettersB = tamil.utf8.get_letters(wordB)
    else:
        lettersB = wordB
    n_A = len(lettersA)
    n_B = len(lettersB)
    # OK only if unique - set(lettersA).intersection(set(lettersB))
    n_AB = len(list(filter(lambda cmnL: cmnL in lettersB, lettersA)))
    return (2.0 * n_AB) / (n_A + n_B)
