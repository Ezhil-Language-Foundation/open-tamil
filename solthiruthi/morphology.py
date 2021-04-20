## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
## This module is part of solthiruthi project under open-tamil umbrella.
## This code maybe used/distributed under MIT LICENSE.

from __future__ import print_function
import abc
import codecs
import copy

from tamil import utf8


# Suffix removal algorithm
class RemoveSuffix(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.possible_suffixes = None
        self.replace_suffixes = {}  # valid dictionary
        self.reversed_suffixes = []

    @abc.abstractmethod
    def setSuffixes(self):
        pass

    @abc.abstractmethod
    def apply(self, word):
        pass

    def prepareSuffixes(self):
        assert self.possible_suffixes
        # reverse the words in each letter.
        for word in self.possible_suffixes:
            self.reversed_suffixes.append(utf8.reverse_word(word))
        return

    def removeSuffix(self, word):
        removed = False
        if not self.possible_suffixes:
            # init once
            self.setSuffixes()
            self.prepareSuffixes()
        word_lett = utf8.get_letters(word)
        rword_lett = copy.copy(word_lett)
        rword_lett.reverse()
        # print('rev word ->',rword_lett)
        rword = u"".join(rword_lett)
        longest_match = ""
        for itr in range(len(self.reversed_suffixes)):
            suffix = self.reversed_suffixes[itr]
            # print(itr,utf8.get_letters(suffix))
            if rword.startswith(suffix):
                if len(longest_match) <= len(suffix):
                    longest_match = suffix
                    # print('L-match-->',utf8.get_letters(longest_match))
            continue
        if len(longest_match) > 0:
            removed = True
            sfx = []
            for itr in range(len(utf8.get_letters(longest_match))):
                sfx.append(word_lett.pop())
            word = u"".join(word_lett)
            sfx.reverse()
            sfx = u"".join(sfx)
            # rule to replace suffix
            alt_suffix = self.replace_suffixes.get(sfx, None)
            if alt_suffix:
                word = word + alt_suffix
        return word, removed


# remove prefix using the suffix removal algorithm via reversal of word
class RemovePrefix(RemoveSuffix):
    def __init__(self):
        super(RemovePrefix, self).__init__()

    def setSuffixes(self):
        self.replace_suffixes = {
            u"மா": u"",
            u"பேர்": u"",
            u"அதி": u"",
            u"பெரிய": u"",
            u"பெரு": u"",
            u"சின்ன": u"",
            u"ஆதி": u"",
            u"சிறு": u"",
            u"அக்": u"",
            u"இக்": u"",
            u"எக்": u"",
        }
        self.possible_suffixes = [
            utf8.reverse_word(word) for word in self.replace_suffixes.keys()
        ]

    def apply(self, word):
        return self.removePrefix(word)

    def removePrefix(self, word):
        word_lett = utf8.get_letters(word)
        word_lett.reverse()
        a, b = self.removeSuffix(u"".join(word_lett))
        return [utf8.reverse_word(a), b]


class RemoveCaseSuffix(RemoveSuffix):
    def __init__(self):
        super(RemoveCaseSuffix, self).__init__()

    def apply(self, word):
        return self.removeSuffix(word)

    def setSuffixes(self):
        accusative = u"ை"
        instrumental = u"ஆல்"
        associative = u"ஓடு"
        dative = u"க்கு"
        genitive = u"இன்"
        possessive = u"உடைய"
        locative = u"இடம்"
        ablative = u"இடமிருந்து"
        self.possible_suffixes = [
            u"உக்கு",
            u"க்கு",
            u"ளை",
            u"கள்",
            accusative,
            instrumental,
            associative,
            dative,
            genitive,
            possessive,
            locative,
            ablative,
        ]
        self.replace_suffixes = dict()
        for w in self.possible_suffixes:
            self.replace_suffixes[w] = u""
        return


class RemoveHyphenatesNumberDate(RemoveCaseSuffix):
    """Done correctly (மேல்) 65536-மேல்,
    ivan paritchayil இரண்டாவது, 2-வது"""

    pass


class RemoveVerbSuffixTense(RemoveCaseSuffix):
    def __init__(self):
        super(RemoveCaseSuffix, self).__init__()
        self.tenses = {"present": u"கிற்", "past": u"த", "future": u"வ"}

    def setSuffixes(self):
        """"""
        tense_endings = [u"ஏன்", u"ஆய்", u"ஆர்", u"ஆன்", u"ஆள்", u"அது", u"ஓம்", u"அன"]
        self.possible_suffixes = tense_endings
        self.replace_suffixes = tense_endings


class RemovePluralSuffix(RemoveSuffix):
    def __init__(self):
        super(RemovePluralSuffix, self).__init__()

    def apply(self, word):
        return self.removeSuffix(word)

    def setSuffixes(self):
        self.replace_suffixes = {
            u"ற்கள்": u"ல்",
            u"கள்": u"",
            u"ல்": u"",
            u"ட்கள்": u"ள்",
            u"ங்கள்": u"ம்",
        }
        self.possible_suffixes = list(self.replace_suffixes.keys())


class RemoveNegationSuffix(RemoveCaseSuffix):
    def __init__(self):
        super(RemoveNegationSuffix, self).__init__()

    def setSuffixes(self):
        self.replace_suffixes = {u"கே": u"", u"ல்லை": u"", u"ாதே": u"", u"ாமல்": u""}
        self.possible_suffixes = list(self.replace_suffixes.keys())


class CaseFilter(object):
    def __init__(self, *filter_obj_list):
        object.__init__(self)
        self.filters = filter_obj_list

    def apply(self, word_in):
        word = [word_in, None]
        for filter_obj in self.filters:
            word = filter_obj.apply(word[0])
        return word[0]


def xkcd():
    obj = RemovePluralSuffix()
    objf = CaseFilter(obj)
    expected = [u"பதிவி", u"கட்டளை", u"அவர்", u"பள்ளி"]
    words_list = [u"பதிவில்", u"கட்டளைகள்", u"அவர்கள்", u"பள்ளிகள்"]
    for w, x in zip(words_list, expected):
        rval = obj.removeSuffix(w)
        trunc_word = objf.apply(w)
        assert trunc_word == rval[0]
        assert rval[1]
        print(utf8.get_letters(w), "->", rval[1])
        assert rval[0] == x
    return


if __name__ == "__main__":
    xkcd()
