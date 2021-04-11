## This Python file uses the following encoding: utf-8
##
## (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
from __future__ import print_function, division
import copy
import collections
import math
import random
import re
from . import utf8


def combinations(symbols_in):
    if isinstance(symbols_in, list):
        symbols = symbols_in
    else:
        symbols = utf8.get_letters(symbols_in)

    uniq_symbols = list(set(symbols))
    N = len(uniq_symbols)
    input_zip = zip(range(0, N), uniq_symbols)
    for count in range(0, 2 ** N):
        bin_rep = bin(count)[2:]
        diff_zeros = N - len(bin_rep)
        bin_rep = "0" * diff_zeros + bin_rep
        filter_symbol = lambda idx: bin_rep[idx] == "1" and uniq_symbols[idx] or u""
        word_combo = u"".join(map(filter_symbol, range(0, N)))
        yield word_combo
    return


def __default_true(*args):
    return True


def permutations(symbols, predicate=__default_true, prefix=u""):
    if not isinstance(symbols, list):
        #        raise Exception(u'symbols என்ற உள்ளீடு iterable interface கொண்டதாக வேண்டும். அது சரம் (str) வகையாக இருந்தால் tamil.utf8.get_letters() பயன்பாட்டை முதலில் உபயொகிக்க!')
        symbols = utf8.get_letters(symbols)

    if len(symbols) == 1:
        yield symbols[0]

    for idx in range(0, len(symbols)):
        new_list = copy.copy(symbols)
        new_pfx = prefix + symbols[idx]
        if not predicate(new_pfx):
            continue
        del new_list[idx]
        for vars in permutations(new_list, predicate, new_pfx):
            yield symbols[idx] + vars
        del new_list
    return


def tamil_permutations(inword):
    if isinstance(inword, list):
        letters = inword
    else:
        letters = utf8.get_letters(inword)
    for word in permutations(letters):
        yield word
    return


def is_palindrome(*args):
    return palindrome(*args)


def palindrome(symbols_in):
    if isinstance(symbols_in, list):
        symbols = symbols_in
    else:
        symbols = utf8.get_letters(symbols_in)
    N = len(symbols)
    for fw in range(0, N // 2):
        rev = N - 1 - fw
        if symbols[fw] != symbols[rev]:
            return False
    return True


def all_plaindromes(dictionary):
    if not callable(getattr(dictionary, "isWord", [])):
        raise Exception(
            "@dictionary என்ற உள்ளீட்டில் isWord என்ற செயல்பாட்டு கூறு கிடையாது. இது விதிவிலக்கான நிலை"
        )
    if not callable(getattr(dictionary, "getAllWords", [])):
        raise Exception(
            "@dictionary என்ற உள்ளீட்டில் getAllWords என்ற செயல்பாட்டு கூறு கிடையாது. இது விதிவிலக்கான நிலை"
        )

    for word in dictionary.getAllWords():
        if is_palindrome(word):
            yield word
    return


def anagrams(word, dictionary, permutations=tamil_permutations):
    if not callable(getattr(dictionary, "isWord", [])):
        raise Exception(
            "@dictionary என்ற உள்ளீட்டில் isWord என்ற செயல்பாட்டு கூறு கிடையாது. இது விதிவிலக்கான நிலை"
        )
    for anagram in permutations(word):
        if dictionary.isWord(anagram):
            yield anagram
    return


def is_anagram(wordA, wordB):
    return sorted(wordA) == sorted(wordB)


def anagrams_in_dictionary(dictionary):
    if not all(
            [
                callable(getattr(dictionary, "isWord", [])),
                callable(getattr(dictionary, "getAllWordsIterable", [])),
            ]
    ):
        raise Exception("dictionary object has insufficient methods")
    anagrams = dict()
    try:
        anagrams_by_len = collections.Counter()
    except AttributeError:
        anagrams_by_len = dict()

    for in_word in dictionary.getAllWordsIterable():
        word = utf8.get_letters(in_word)
        sword = u"".join(sorted(word))
        try:
            equivs = anagrams[sword]
        except KeyError as ke:
            equivs = list()
            anagrams_by_len[sword] = 0
        equivs.append(in_word)
        anagrams[sword] = equivs
        anagrams_by_len[sword] += 1
    items_to_del = copy.deepcopy(filter(lambda a: a[1] == 1, anagrams_by_len.items()))
    for itm, counts in items_to_del:
        del anagrams[itm]
        del anagrams_by_len[itm]
    del items_to_del

    itr = 0
    from operator import itemgetter

    rval_anagram_count = sorted(anagrams_by_len.items(), key=itemgetter(1))
    for k, v in rval_anagram_count:
        itr = itr + 1
        # print(u"%d/ items #%d"%(itr,v))
    # print(u"%d anagrams found"%itr)
    return rval_anagram_count, anagrams


# combinations filtered by dictionary - yields all possible sub-words of a word.
# e.g. 'bat' -> 'tab', 'bat', 'at', etc.
def combinagrams(word, dictionary, limit=float("inf")):
    count = 0
    for word_part in combinations(word):
        for valid_word in anagrams(word_part, dictionary, tamil_permutations):
            count = count + 1
            if count > limit:
                return
            yield valid_word
    return


# permutations of a word filtered by dictionary - yields all possible sub-words of a word.
# e.g. 'bullpen' -> 'pen' 'bull', 'ben' 'pull', 'pub' 'nell', 'nell' 'pub' .etc.
def permutagrams(word, dictionary):
    matches = dict()
    for perm_word in permutations(word):
        if perm_word in matches:
            continue
        matches[perm_word] = list()
        actual_splits = word_split(perm_word, dictionary)
        if len(actual_splits) > 0:
            matches[perm_word].append(actual_splits)
            yield actual_splits
    del matches
    return


def rhymes_with(inword, reverse_dictionary):
    if not all(
            [
                callable(getattr(reverse_dictionary, "isWord", [])),
                callable(getattr(reverse_dictionary, "getWordsEndingWith", [])),
            ]
    ):
        raise Exception("reverse dictionary object has insufficient methods")
    rhyming = list()
    if isinstance(inword, list):
        letters = inword
    else:
        letters = utf8.get_letters(inword)

    MAX = len(letters) * 2
    while len(rhyming) < MAX and len(letters) > 0:
        partial_word = u"".join(letters)
        matches = list(reverse_dictionary.getWordsEndingWith(partial_word))
        # print "%d -> %d"%(len(letters),len(matches))
        rhyming.extend(matches)
        del letters[0]

    # rhyming = list(set(rhyming))
    return set(rhyming[0: min(len(rhyming) - 1, MAX)])


def greedy_split(inword, dictionary):
    if not all(
            [
                callable(getattr(dictionary, "isWord", [])),
                callable(getattr(dictionary, "hasWordsStartingWith", [])),
            ]
    ):
        raise Exception("dictionary object has insufficient methods")

    if isinstance(inword, list):
        letters = inword
    else:
        letters = utf8.get_letters(inword)
    solution = list()

    longest_idx = 0
    prev_idx = 0
    idx = 0
    possible = True
    while possible:
        idx = prev_idx
        prev_word = u""
        while idx < len(letters):
            # print("%d -> %d"%(idx,prev_idx))
            word = u"".join(letters[prev_idx: idx + 1])
            if dictionary.hasWordsStartingWith(word):
                if dictionary.isWord(word):
                    prev_word = word
                    # print("word => %s"%word)
                    longest_idx = idx + 1
                elif word == inword:
                    possible = False
                    break
            else:
                # print "prev_ word"
                # pprint(prev_word)
                # pprint(solution)
                # pprint(idx)
                if len(prev_word) == 0:
                    possible = False
                    break

            idx = idx + 1

        prev_idx = longest_idx

        # print(" \t --> word %s|%s|%d"%(prev_word,str(possible),prev_idx))
        solution.append(prev_word)
        do_brk = len(prev_word) == 0
        if (prev_idx) >= len(letters) or do_brk:
            possible = not do_brk
            break

    # print(u"//".join(solution))
    if possible:
        return solution

    return list()


def word_split(inword, dictionary):
    if not callable(getattr(dictionary, "isWord", [])):
        raise Exception("dictionary object has insufficient methods")

    if isinstance(inword, list):
        letters = inword
    else:
        letters = utf8.get_letters(inword)

    solutions = list()

    idx = 0
    while idx < len(letters) - 1:
        # print idx
        prev_word = u"".join(letters[0: idx + 1])
        next_word = u"".join(letters[idx + 1:])
        temp_sol = list()
        # print prev_word,next_word
        sol1 = greedy_split(prev_word, dictionary)
        if len(sol1) > 0:
            sol2 = greedy_split(next_word, dictionary)
            if len(sol2) > 0:
                tmpsol = list()
                tmpsol.extend(sol1)
                tmpsol.extend(sol2)
                if not (tmpsol in solutions):
                    solutions.append(tmpsol)
                # try cross product of s1, and s2 computed recursively!
                s1 = word_split(prev_word, dictionary)
                s2 = word_split(next_word, dictionary)
                for sols in s1:
                    for sols2 in s2:
                        l = list()
                        l.extend(sols)
                        l.extend(sols2)
                        if not (l in solutions):
                            solutions.append(l)
        idx = idx + 1

    return solutions


def minnal(word_list, use_grantham=False):
    L = list(map(utf8.get_letters, word_list))
    allL = list()
    # For words like: 'கன்னன்' we need both the 'ன்' to come out in grid.
    for l in L:
        stat = {}
        wordl = []
        # for i,j in zip(l,range(0,len(l)))] )
        for i in l:
            stat[i] = stat.get(i, 0) + 1
        for i in l:
            wordl.append(i + str(stat[i]))
            stat[i] -= 1
        allL.extend(wordl)
    allL = list(set(allL))
    allL = [re.sub("\d+", "", l) for l in allL]
    L = utf8.tamil_sorted(allL)
    Sq = int(math.ceil(math.sqrt(len(L))) ** 2)
    random_inserts = Sq - len(L)
    L.extend(
        [
            random.choice(utf8.tamil247 if not use_grantham else utf8.tamil_letters)
            for i in range(0, random_inserts)
        ]
    )
    random.shuffle(L)
    i = 0
    Lside = int(math.sqrt(len(L)))
    textgrid = []
    text = u""
    while i < len(L):
        text = text + (u",".join(L[i: i + Lside])) + u"\n"
        textgrid.append(L[i: i + Lside])
        i = i + Lside
    return textgrid, text


# dummy dictionary interface for use with anagrams
DictionaryWithPredicate = collections.namedtuple("DictionaryWithPredicate", ["isWord"])


# Utility class
class DictionaryFixedWordList(object):
    def __init__(self, wlist):
        self.wlist = wlist
        object.__init__(self)

    def isWord(self, word):
        return word in self.wlist

    def hasWordsStartingWith(self, pfx):
        return any([w.startswith(pfx) for w in self.wlist])
