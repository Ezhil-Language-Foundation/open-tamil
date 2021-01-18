## -*- coding: utf-8 -*-
## (C) 2015-2017 Muthiah Annamalai,
##
from __future__ import print_function
import abc
import sys
from tamil import utf8
from pprint import pprint

PYTHON3 = sys.version[0] == "3"


def get_letters(word):
    if isinstance(word, list):
        chars = word
    else:
        chars = utf8.get_letters(word)
    return chars


class Rule:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def apply(self, word, ctx):
        """@word is just that. @ctx is a dict of NwordsPrevious, NwordsNext,
        and a list of surrounding words for as items.
        e.g. ctx = {'NPrev' : 4, 'Prev' : [w1,w2,w3,w4],'NNext':2,'Next':[w1,w2]}
        return value should be boolean (False if error found) and an optional reason as second argument
        """
        return False, None


class Sequential:
    @staticmethod
    def in_sequence(word, ref_set, ref_reason, freq_threshold=2):
        """ ignore ctx information right now. If repetition/match length >= @freq_threshold then we flag-it """
        chars = get_letters(word)
        flag = True  # no error assumed
        reason = None  # no reason
        freq_count = 0
        for char in chars:
            if char in ref_set:
                freq_count += 1
                if freq_count >= freq_threshold:
                    flag = False
                    break
                continue
            freq_count = 0  # continue loop
        if not flag:
            reason = ref_reason
        return flag, reason


class AdjacentVowels(Rule):
    """donot allow adjacent vowels in the word.
    ஆஅக்காள் (originally -> அக்காள்) will be flagged
    """

    reason = u"ஒன்றைத்தொடர்ந்துஒன்று உயிரெழுத்துக்கள் வரக்கூடாது. இது பெரும்பாலும் பிழையாக இருக்கும்."
    uyir_letters = set(utf8.uyir_letters)

    def apply(self, word, ctx=None):
        """ ignore ctx information right now """
        return Sequential.in_sequence(
            word, AdjacentVowels.uyir_letters, AdjacentVowels.reason
        )


class AdjacentConsonants(Rule):
    """donot allow adjacent consonants in the word.
    this may not be as useful as AdjacentVowels rules
    """

    reason = u"ஒன்றைத்தொடர்ந்துஒன்று மெய் எழுத்துக்கள் வரக்கூடாது. இது பெரும்பாலும் பிழையாக இருக்கும்."
    mei_letters = set(utf8.mei_letters)
    agaram_letters = set(utf8.agaram_letters)

    def __init__(self, freq=2):
        self.freq_threshold = freq

    def apply(self, word, ctx=None):
        """ ignore ctx information right now """
        flag, reason = Sequential.in_sequence(
            word,
            AdjacentConsonants.mei_letters,
            AdjacentConsonants.reason,
            self.freq_threshold,
        )
        if flag:
            flag, reason = Sequential.in_sequence(
                word,
                AdjacentConsonants.agaram_letters,
                AdjacentConsonants.reason,
                self.freq_threshold,
            )
        return flag, reason


class RepeatedLetters(Rule):
    """ donot allow more than one repetition of a letter in word """

    reason = u"ஒரே எழுத்து பல முரை (>= 2) தொடர்ச்சியாக வந்தால் அது பிழையான சொல் ஆகும்"

    def apply(self, word, ctx=None):
        """ ignore ctx information right now """
        chars = get_letters(word)
        flag = True  # no error assumed
        reason = None  # no reason
        prev_letter = None
        for char in chars:
            if prev_letter == char:
                flag = False
                break
            prev_letter = char  # continue loop
        if not flag:
            reason = RepeatedLetters.reason
        return flag, reason


class BadIME(Rule):
    """donot allow vowels with kombu, thunaikaal etc in the word.
    ஆாள் (originally intended as -> ஆள்) will be flagged
    """

    reason = u"சொல்லில் பிழை காரணம், இல்லாத தமிழ் எழுத்து.."
    uyir_letters = set(utf8.uyir_letters)

    def apply(self, word, ctx=None):
        """ ignore ctx information right now """
        chars = get_letters(word)
        flag = True  # no error assumed
        reason = None  # no reason
        prev_char = None

        for char in chars:
            rule1, rule2, rule3 = False, False, False
            # rule 1 : uyir followed by kombugal
            rule1 = (char[-1] in utf8.accent_symbols) and (char[0] in utf8.uyir_letters)
            if not rule1:
                # rule 2 : two pullis adjacent to each other
                rule2 = (
                    len(char) >= 2
                    and (char[-1] == utf8.pulli_symbols[0])
                    and (char[-2] == char[-1])
                )
                if not rule2:
                    # rule 3 : none of the accent symbols repeat
                    # exclusions to rule 3 : non-standard Unicode encoding of periya kombu / siriya kombu with thunai kaal
                    rule3 = (
                        len(char) >= 2
                        and (char[-1] in utf8.accent_symbols)
                        and (char[-2] in utf8.accent_symbols)
                        and not (char[-1] == u"ா" and char[-2] in [u"ெ", u"ே"])
                    )

            if rule1 or rule2 or rule3:
                flag = False
                reason = BadIME.reason
                break
            prev_char = char  # continue loop
        # print([flag,reason])
        return flag, reason
