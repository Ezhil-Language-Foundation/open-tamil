# -*- coding: utf-8 -*-
# (C) 2016 Muthiah Annamalai
#
# This file is part of 'open-tamil' package
# It implements a data-driven spell checker for Tamil language
#
from __future__ import print_function

import argparse
import copy
import codecs
import functools
import itertools
import json
import operator
import pprint
import re
import string
import sys
import threading
import time

import tamil
from transliterate import azhagi, jaffna, combinational, algorithm
from solthiruthi.suggestions import norvig_suggestor
from solthiruthi.morphology import (
    RemoveCaseSuffix,
    RemovePluralSuffix,
    RemovePrefix,
    RemoveVerbSuffixTense,
    CaseFilter,
)
from solthiruthi.dictionary import DictionaryBuilder, TamilVU, EnglishLinux
from solthiruthi.heuristics import BadIME, AdjacentConsonants, AdjacentVowels
from ngram.Distance import Dice_coeff, edit_distance

# Make Bi-Lingual dictionary

PYTHON3 = sys.version_info[0] == 3
assert PYTHON3, "சொல்திருத்தி செயலி பைத்தான் 3-இல் மற்றுமே இயங்கும்!"

_DEBUG = False


# save 6s for the code on a old machine
class LoadDictionary(threading.Thread):
    DEBUG = False
    lock = threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self, name="LoadDictionaryInBackground")

    def run(self):
        start = time.time()
        Speller.get_dictionary()
        Speller.get_english_dictionary()
        if LoadDictionary.DEBUG:
            print("LOADED DICTIONARY in  %g (s)" % (time.time() - start))
        return


class DeletionFilter:
    @staticmethod
    def get_suggestions(letters, lexicon):
        rval = []
        L = len(letters)
        for idx, letter in enumerate(letters):
            muthal = idx == 0 and u"" or u"".join(letters[0:idx])
            meethi = idx == L and u"" or u"".join(letters[min(L - 1, idx + 2):])
            walt = muthal + meethi
            if lexicon.isWord(walt):
                rval.append(walt)
        return rval


class OttruSplit:
    """ யாரிகழ்ந்து = [ய்  + ஆரிகழ்ந்து], [யார், இகழ்ந்து] ,[யாரிக், அழ்ந்து], [யாரிகழ்ந்த்,உ]"""

    def __init__(self, word, letters):
        self.word = word
        if word != u"".join(letters):
            letters = tamil.utf8.get_letters(word)
        self.letters = letters
        self.results = list()

    def run(self, lexicon):
        self.generate_splits()
        return self.filter(lexicon)

    def generate_splits(self):
        """
        யாரிகழ்ந்து =
            [['ய்', 'ஆரிகழ்ந்து'],
             ['யார்', 'இகழ்ந்து'],
             ['யாரிக்', 'அழ்ந்து'],
             ['யாரிகழ்ந்த்', 'உ']]
        """
        L = len(self.letters) - 1
        for idx, letter in enumerate(self.letters):
            if not (letter in tamil.utf8.grantha_uyirmei_letters):
                continue
            muthal = idx == 0 and u"" or u"".join(self.letters[0:idx])
            meethi = idx == L and u"" or u"".join(self.letters[idx + 1:])
            mei, uyir = tamil.utf8.splitMeiUyir(letter)
            muthal = muthal + mei
            meethi = uyir + meethi
            self.results.append([muthal, meethi])
        return len(self.results) > 0

    def filter(self, lexicon):
        self.results = list(filter(lambda x: all(map(lexicon.isWord, x)), self.results))
        return self.results


class Mayangoli:
    varisai = [
        [u"ல்", u"ழ்", u"ள்"],
        [u"ர்", u"ற்"],
        [u"ந்", u"ன்", u"ண்"],
        [u"ங்", u"ஞ்"],
    ]  # வரிசை.

    def __init__(self, word, letters):
        self.word = word
        if word != u"".join(letters):
            letters = tamil.utf8.get_letters(word)
        self.letters = letters
        self.matches_and_positions = []
        self.alternates = []
        self.pos_classes = []

    @staticmethod
    def run(word, letters):
        obj = Mayangoli(word, letters)
        obj.find_letter_positions()
        if len(obj.matches_and_positions) == 0:
            return []
        obj.find_correspondents()
        obj.generate_word_alternates()
        return obj.alternates

    def find_letter_positions(self):
        for idx, letter in enumerate(self.letters):
            p = tamil.utf8.splitMeiUyir(letter)
            if len(p) == 1:
                continue
            mei, uyir = p
            for r in range(0, len(Mayangoli.varisai)):
                for c in range(0, len(Mayangoli.varisai[r])):
                    if mei == Mayangoli.varisai[r][c]:
                        self.matches_and_positions.append((idx, r, c))
        return len(self.matches_and_positions) > 0

    def find_correspondents(self):
        for pos, r, c in self.matches_and_positions:
            src_letter = self.letters[pos]
            _, src_uyir = tamil.utf8.splitMeiUyir(src_letter)
            alt_letters = list()
            for alternate_mei in Mayangoli.varisai[r]:
                alt_letters.append(tamil.utf8.joinMeiUyir(alternate_mei, src_uyir))
            self.pos_classes.append(alt_letters)
        return True

    def _generate_combinations(self):
        return itertools.product(*self.pos_classes)

    def generate_word_alternates(self):
        # find matches in Mayangoli classes
        # if there are no Mayangoli matches then we return []
        # for each match we find the class and find corresponding uyirmei alternates
        # generate the combinations of these alternates in the said word positions
        # caller will filter the new word alternates (returned)
        # based on substituting these correspondents
        for position_sub in self._generate_combinations():
            alt_letters = copy.copy(self.letters)
            if _DEBUG:
                pprint.pprint(position_sub)
            idx = 0
            for pos, r, c in self.matches_and_positions:
                alt_letters[pos] = position_sub[idx]
                idx += 1
            word_alt = u"".join(alt_letters)
            self.alternates.append(word_alt)
        return True


class Typographical:
    @staticmethod
    def checkFormErrors(word, errmsg=None):
        r1 = BadIME()
        r2 = AdjacentConsonants()
        r2.freq_threshold = 4
        r3 = AdjacentVowels()
        item0 = operator.itemgetter(0)
        if errmsg and r1.apply(word)[0]:
            errmsg.append(u"BadIME")
            print("Bad IME")
        return any(list(map(lambda obj: not item0(obj.apply(word)), [r1, r2, r3])))


class Speller(object):
    TVU_dict = None
    ENL_dict = None
    punctuation = string.punctuation + "()[]{}"

    def __init__(self, filename=None, lang="ta", mode="non-web"):
        object.__init__(self)
        self.lang = lang.lower()
        self.filename = filename
        self.user_dict = set()
        self.case_filter = CaseFilter(
            RemovePluralSuffix(),
            RemoveVerbSuffixTense(),
            RemoveCaseSuffix(),
            RemovePrefix(),
        )
        if not self.in_tamil_mode():
            self.alphabets = [a for a in string.ascii_lowercase]
        else:
            self.alphabets = None

        if mode == "web":
            return

        if not self.filename:
            self.interactive()
        else:
            self.spellcheck(self.filename)

    def in_tamil_mode(self):
        return self.lang != u"en"

    @staticmethod
    def get_dictionary():
        LoadDictionary.lock.acquire()
        if not Speller.TVU_dict:
            Speller.TVU_dict, _ = DictionaryBuilder.create(TamilVU)
        LoadDictionary.lock.release()
        return Speller.TVU_dict

    @staticmethod
    def get_english_dictionary():
        LoadDictionary.lock.acquire()
        if not Speller.ENL_dict:
            Speller.ENL_dict, _ = DictionaryBuilder.create(EnglishLinux)
        LoadDictionary.lock.release()
        return Speller.ENL_dict

    def language(self):
        if self.in_tamil_mode():
            return "tamil"
        return "english"

    def checklang(self, word):
        if self.in_tamil_mode():
            return tamil.utf8.all_tamil(word)
        for w in word.lower():
            if not (w in string.ascii_lowercase):
                return False
        return True

    # full-text interface driver for unittest @ Dec 10, 2017
    def noninteractive_spellcheck(self, text):
        nwords = 0
        npass = 0
        nfail = 0
        fail_n_suggs = dict()
        for word in re.split("\s+", text):
            if len(word) < 1:
                continue
            nwords += 1
            result, suggs = self.REST_interface(word)
            nfail += int(not result)
            npass += int(result)
            if not result:
                fail_n_suggs[word] = suggs
        obj = {
            "total": nwords,
            "correct_words": npass,
            "wrong_words": nfail,
            "word_suggestions": fail_n_suggs,
        }
        return obj

    # Ref: https://www.tinymce.com/docs/plugins/spellchecker/
    def REST_interface(self, word):
        # returns JSON data in TinyMCE format
        ok, suggs = self.check_word_and_suggest(word)
        if _DEBUG:
            print("REST => %d" % ok)
            pprint.pprint(suggs)
        if ok:
            return ok, {}
        return ok, suggs

    @staticmethod
    def dice_comparison(ref_word, word):
        """ use this class method for SORTED"""
        val = Dice_coeff(ref_word, word)
        if val == 1:
            return 0
        return (2 * (val - 0.5) > 0) and 1 or -1

    def suggestion_policy(self, word, suggs):
        # pick suggestions that are only +/- 2 letter length different
        filter_suggs = []
        tamil_length = lambda w: len(tamil.utf8.get_letters(w))
        ref_wl = tamil_length(word)
        accept_min_max = [max(ref_wl - 2, 1), ref_wl + 1]
        filter_suggs = filter(
            lambda w: tamil_length(w) >= accept_min_max[0]
                      and len(w) <= accept_min_max[1],
            suggs,
        )
        # sort the suggestions by Dice coefficient
        filter_suggs = set(filter_suggs)
        if len(filter_suggs) == 0:
            # guess!
            filter_suggs = suggs
            filter_suggs = list(tamil.utf8.tamil_sorted(filter_suggs))
            filter_suggs[min(10, len(filter_suggs) - 1):] = []
            return filter_suggs
        _compare_fn = lambda wA, wB: (edit_distance(wA, word) < edit_distance(wB, word))
        filter_suggs = list(
            tamil.utf8.tamil_sorted(filter_suggs, key=functools.cmp_to_key(_compare_fn))
        )
        return filter_suggs

    # கட

    def str_suggestions(self, word):
        if self.in_tamil_mode():
            return u'சொல் "%s" மாற்றங்கள்' % word
        return u'SUGGESTIONS for "%s"' % word

    def mayangoli_suggestions(self, word, letters):
        alternates = Mayangoli.run(word, letters)
        alternates = filter(lambda w: w != word, alternates)
        if _DEBUG:
            for idx, w in enumerate(alternates):
                pprint.pprint(["Myangoli", idx, w])
        return copy.copy(alternates)

    def interactive(self):
        try:
            while True:
                word = input(u">> ")
                word = re.sub(u"\s+", "", word)

                # skip empty words
                if len(word) < 1:
                    continue

                if not self.checklang(word):
                    print(u'EXCEPTION "%s" is not a %s Word' % (word, self.language()))
                    continue
                ok, suggs = self.check_word_and_suggest(word)
                suggs = self.suggestion_policy(word, suggs)
                if not ok:
                    words_per_row = 4
                    option_str = u", ".join(
                        [
                            u"(%d) %s" % (itr, wrd)
                            + ((itr > 0 and itr % words_per_row == 0) and u"\n" or u"")
                            for itr, wrd in enumerate(suggs)
                        ]
                    )
                    print(u"%s\n\t %s" % (self.str_suggestions(word), option_str))
                else:
                    print(self.in_tamil_mode() and u"சரி" or u"OK")
        except KeyboardInterrupt as ke:
            pass
        except EOFError as eof:
            pass
        finally:
            print(self.in_tamil_mode() and u"\nவணக்கம்!" or "\nBYE!")
        return

    def spellcheck(self, filename):
        new_document = []
        lines = []
        with codecs.open(filename, u"r", u"utf-8") as data:
            lines = data.readlines()
        for line in lines:
            words = tamil.utf8.get_words(tamil.utf8.get_letters(line))
            for word in words:
                # FIXME : handle punctuation
                # word = filter( tamil.utf8.is_tamil_unicode_predicate, word )
                ok, suggs = self.check_word_and_suggest(word)
                suggs = list(suggs)
                if not ok:
                    option = suggs[0]
                    # take user input.
                    # FIXME: User options to include DONTREPLACE/KEEP, DELETE WORD, etc.
                    option_str = u", ".join(
                        [u"(%d) %s" % (itr, wrd) for itr, wrd in enumerate(suggs)]
                    )
                    if self.in_tamil_mode():
                        print(u'வரி "%s"' % line.strip())
                        print(
                            u"'%s' சொல்லை கொண்டு\n\t சொல்லை '%s' மாற்றிடு\n"
                            % (option_str, word)
                        )
                    else:
                        print(u'Line, "%s"' % line.strip())
                        print(u" Replace word %s with\n\t => %s\n" % (word, option_str))
                    try:
                        if self.in_tamil_mode():
                            choice_str = "விருப்பம் [-1 புறக்கணி, 0-%d மாற்றவும்]:"
                        else:
                            choice_str = u"option [-1 ignore, 0-%d replace]: "
                        choice = input(choice_str % (len(suggs) - 1))
                        choice = int(choice)
                        if choice == -1:
                            if self.in_tamil_mode():
                                print(u"வார்த்தை மாறாத இருந்தது")
                            else:
                                print(u"Not replacing word")

                            option = word
                            self.user_dict.add(word)
                        else:
                            option = suggs[choice]
                    except Exception as ie:
                        print(str(ie))
                    if self.in_tamil_mode():
                        replace_msg = u"வார்த்தை %s -> %s இதற்காக மாற்றவும்\n"
                    else:
                        replace_msg = u" replacing word %s -> %s\n"
                    print(replace_msg % (word, option))
                    new_document.append(str(option))
                else:
                    new_document.append(word)
            new_document.append(u"\n")
        if self.in_tamil_mode():
            print(u"*********** ஆவணத்தில் உள்ள பிழைகளை திருத்திய பின் *********")
        else:
            print(u"*********** cleaned up document **********")
        print(u" ".join(new_document))

    def get_lang_dictionary(self):
        if not self.in_tamil_mode():
            return Speller.get_english_dictionary()
        return Speller.get_dictionary()

    def isWord(self, word):
        # Plain old dictionary checks
        LANG_dict = self.get_lang_dictionary()
        is_dict_word = LANG_dict.isWord(word)
        in_user_dict = word in self.user_dict or is_dict_word
        return in_user_dict

    def add_numeral_words(self, lexicon):
        if not self.in_tamil_mode():
            return

        units = (
            u"பூஜ்ஜியம்",
            u"ஒன்று",
            u"இரண்டு",
            u"மூன்று",
            u"நான்கு",
            u"ஐந்து",
            u"ஆறு",
            u"ஏழு",
            u"எட்டு",
            u"ஒன்பது",
            u"பத்து",
        )  # 0-10
        teens = (
            u"பதினொன்று",
            u" பனிரண்டு",
            u"பதிமூன்று",
            u"பதினான்கு",
            u"பதினைந்து",
            u"பதினாறு",
            u"பதினேழு",
            u"பதினெட்டு",
            u"பத்தொன்பது",
        )  # 11-19
        tens = (
            u"பத்து",
            u"இருபது",
            u"முப்பது",
            u"நாற்பது",
            u"ஐம்பது",
            u"அறுபது",
            u"எழுபது",
            u"எண்பது",
            u"தொன்னூறு",
        )  # 10-90
        tens_suffix = (
            u"இருபத்து",
            u"முப்பத்து",
            u"நாற்பத்து",
            u"ஐம்பத்து",
            u"அறுபத்து",
            u"எழுபத்து",
            u"எண்பத்து",
            u"தொன்னூத்து",
        )  # 10+-90+
        hundreds = (
            u"நூறு",
            u"இருநூறு",
            u"முந்நூறு",
            u"நாநூறு",
            u"ஐநூறு",
            u"அறுநூறு",
            u"எழுநூறு",
            u"எண்ணூறு",
            u"தொள்ளாயிரம்",
        )  # 100 - 900
        hundreds_suffix = (
            u"நூற்றி",
            u"இருநூற்றி",
            u"முந்நூற்று",
            u"நாநூற்று",
            u"ஐநூற்று",
            u"அறுநூற்று",
            u"எழுநூற்று",
            u"எண்ணூற்று",
            u"தொள்ளாயிரத்து",
        )  # 100+ - 900+
        one_thousand_prefix = (u"ஓர்",)
        thousands = (u"ஆயிரம்", u"ஆயிரத்தி")

        one_prefix = (u"ஒரு",)
        lakh = (u"இலட்சம்", u"இலட்சத்து")
        crore = (u"கோடி", u"கோடியே")

        mil = (u"மில்லியன்",)
        bil = (u"பில்லியன்",)
        tril = (u"டிரில்லியன்",)

        if lexicon.isWord(tril[0]):
            return

        numerals = list()
        for wordset in [
            units,
            tens,
            teens,
            tens_suffix,
            hundreds,
            hundreds_suffix,
            one_thousand_prefix,
            thousands,
            one_prefix,
            lakh,
            crore,
            mil,
            bil,
            tril,
        ]:
            numerals.extend(wordset)
        # with codecs.open("numerals.json","w","utf-8") as fp:
        #    fp.write(json.dumps(numerals))
        for word in numerals:
            lexicon.add(word)

    @staticmethod
    def scrub_ws(word):
        return re.sub(u"[\s{}()\[\]]+", u"", word)

    def check_word_and_suggest(self, word, errmsg=None):
        word = word.strip()
        # skip known punctuation at end of line
        while len(word) >= 1 and any(map(word.endswith, Speller.punctuation)):
            word = word[:-1]
        while len(word) >= 1 and any(map(word.startswith, string.whitespace)):
            word = word[1:]

        # is number then we propose a numeral
        if self.in_tamil_mode():
            numword = word.replace(u",", u"")
            if re.match(u"[+|-]*[\d]+", numword):
                try:
                    num = float(numword)
                    posnum = num
                    if num < 0:
                        posnum = -1 * num
                    numeral_form = tamil.numeral.num2tamilstr(posnum)
                    if num < 0:
                        numeral_form = u"கழித்தல் " + numeral_form
                    return (False, [numeral_form])
                except Exception as ioe:
                    pass

            # dates are okay
            if any(map(word.endswith, [u"-இல்", u"-ஆம்", u"-இலிருந்து", u"-வரை"])):
                if re.search("^\d+", word):
                    return (True, [word])  # word is okay

            # check if words are transliterated
            if any(
                    filter(
                        lambda x: x in string.ascii_letters, tamil.utf8.get_letters(word)
                    )
            ):
                # letter-sequence only
                en_word = Speller.scrub_ws(word)
                EN_Lexicon = Speller.get_english_dictionary()
                if EN_Lexicon.isWord(en_word):
                    return (
                        False,
                        [""],
                    )  # English word - nosub- yet until we have parallel dictionaries or translation. TBD.

                # is english letter
                ta = algorithm.Iterative.transliterate(
                    jaffna.Transliteration.table, en_word
                )
                # TBD: potential for having ANN to tell if english text is pure English word
                # or a romanized Tamil word. Output of classifier can be useful here.
                return (False, [ta])

            # check if it matches Tamil numeral and has close match.
            # propose suggestions from that list.
            # TBD

        # hyphens are not okay
        if word.find(u"-") >= 0:
            return (False, [word.replace(u"-", u" ")])  # re.sub(u"^w"," ",word))
        # replace other spurious ()[] punctuations by concatenation
        # word = u"".join(filter(lambda l: not( l in Speller.punctuation), tamil.utf8.get_letters(word)))
        orig_word = u"%s" % word

        # remove digits
        word = re.sub(u"\d+", u"", word)
        letters = tamil.utf8.get_letters(word)
        TVU_dict = self.get_lang_dictionary()
        self.add_numeral_words(TVU_dict)

        # Check if this 'word' is any common kind of error
        if Typographical.checkFormErrors(word, errmsg):
            if errmsg:
                errmsg.append("TypographicalError")

        if not self.checklang(word):
            print("Word is not in desired language!")
            return (False, [u""])

        if len(word) < 1:
            print("Word is too small")
            return (False, [u""])

        # plain old dictionary + user dictionary check
        if self.isWord(word):
            return (True, word)

        # Remove case and redo the dictionary + user check
        word_nocase = self.case_filter.apply(word)
        if self.isWord(word_nocase):
            return (True, word_nocase)
        else:
            word = word_nocase

        # Consider splitting the word and see if it has 2 sub-words
        # e.g. செயல்பட => செயல் + பட
        alt = tamil.wordutils.greedy_split(word, TVU_dict)
        greedy_results = list()
        if len(alt) >= 1:
            greedy_results = [u" ".join(alt), u"-".join(alt)]
            greedy_results.extend(alt)
            # return (False, greedy_results )

        # if there are no other suggestions than deletion filter, we return
        # in presence of other suggestions we can just return suggestions
        suggs = DeletionFilter.get_suggestions(letters, TVU_dict)
        if len(suggs) > 0:
            if len(greedy_results) == 0:
                return (False, suggs)
            else:
                greedy_results.extend(suggs)

        # ottru splitting for Tamil language mode
        ottru_options = []
        if self.in_tamil_mode():
            # discover words like யாரிகழ்ந்து are accepted.
            ottru = OttruSplit(word, letters)
            ottru.run(TVU_dict)
            if len(ottru.results) > 0:
                return (True, word)
            ottru_options = ottru.results

        # TODO: Noun Declension - ticket-

        # suggestions at edit distance 1
        norvig_suggests1 = list(
            filter(
                TVU_dict.isWord, norvig_suggestor(word, self.alphabets, 1, limit=100)
            )
        )
        norvig_suggests2 = list(
            filter(
                TVU_dict.isWord, norvig_suggestor(word, self.alphabets, 2, limit=100)
            )
        )
        combinagram_suggests = list(
            tamil.wordutils.combinagrams(word, TVU_dict, limit=25)
        )
        pfx_options = TVU_dict.getWordsStartingWith(u"".join(letters[:-1]))
        # FIXME: score  the options
        options = greedy_results
        options.extend(ottru_options)
        options.extend(norvig_suggests1)
        options.extend(norvig_suggests2)
        options.extend(combinagram_suggests)
        options.extend(pfx_options)

        # filter the options against a dictionary!
        options = filter(TVU_dict.isWord, options)
        options = list(options)

        if self.in_tamil_mode():
            options.extend(self.mayangoli_suggestions(orig_word, letters))

        # sort the options
        if not self.in_tamil_mode():
            options.sort()
        else:
            options = list(tamil.utf8.tamil_sorted(options))

        # remove replacements with single-letter words
        WL = len(tamil.utf8.get_letters(word))
        if WL > 3:
            options = filter(lambda x: len(tamil.utf8.get_letters(x)) > 2, options)

        # remove dupes in list
        options2 = []
        prev = None
        for val in options:
            if val.strip() != prev:
                options2.append(val.strip())
            prev = val.strip()
        del options
        if _DEBUG:
            print("@deduplication")
            pprint.pprint(options2)

        # score by Dice or Edit-Distance coefficients
        options_score = [0.0 for i in range(len(options2))]
        for itr, sugg_word in enumerate(options2):
            # options_score[itr] = Dice_coeff( word, sugg_word )
            options_score[itr] = (
                    (len(word) - edit_distance(word, sugg_word))
                    / (1.0 * len(orig_word))
                    * Dice_coeff(word, sugg_word)
                    / 3.0
            )  # dice coeff is weighted down
        options = zip(options2, options_score)

        # limit options by score
        options = list(sorted(options, key=operator.itemgetter(1), reverse=True))
        options = [word_pair[0] for word_pair in options]
        # L = 40
        # limit to first top -L=20 only which is good enough
        # options = options[0:min(len(options),L)]
        if _DEBUG:
            pprint.pprint("@after scoring/sorting")
            pprint.pprint(options)

        # eliminate single letter options
        options = filter(lambda x: not (x in tamil.utf8.tamil_letters), options)

        # Due to suggestion policy we may have words which are found in error but we dont have
        # replacements for them!

        # TBD: options should not have the 'word'!
        return (False, options)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(u"files", nargs="*", default=[])
    parser.add_argument(
        u"-debug",
        action=u"store_true",
        default=False,
        help=u"enable debugging information on screen",
    )
    parser.add_argument(
        u"-l",
        u"--lang",
        default=u"TA",
        choices=(u"TA", u"EN"),
        help=u"option to specify English or Tamil (default) language",
    )
    parser.add_argument(
        u"-i",
        u"--interactive",
        help=u"use the interactive mode",
        default=False,
        action=u"store_true",
    )
    args = parser.parse_args()

    if not args.interactive and len(args.files) < 1:
        parser.print_help()
        sys.exit(0)
    LoadDictionary().start()

    if args.interactive:
        lang = args.lang.lower()
        Speller(filename=None, lang=lang)
        sys.exit(0)
    else:
        for file_name in args.files:
            Speller(file_name, lang="ta")


if __name__ == u"__main__":
    main()
# TBD: dieties, divinity, language, people, places, personalities to be added.
# TBD: colors, cities, places, countries, currencies to be added.
# TBD: proper nouns common names etc.
# Find bugs in TinyMCE where spell module does not highlight all the mentioned words.
# TBD: Rank options by scoring bigram models
# TBD: Insertion errors are not searched.
