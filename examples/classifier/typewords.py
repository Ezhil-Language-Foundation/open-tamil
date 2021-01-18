## This Python file uses the following encoding: utf-8
import codecs
import tamil
import sys
from pprint import pprint


def safe_splitMeiUyir(arg):
    try:
        # when uyir letters are passed to splitMeiUyir function it will throw an IndexError
        rval = tamil.utf8.splitMeiUyir(arg)
        if len(rval) == 1:
            return (rval, u"")
        return rval
    except IndexError as idxerr:
        pass
    except ValueError as valerr:
        # non tamil letters cannot be split - e.g. '26வது'
        pass
    return (u"", u"")


class FilterDictionary:
    def __init__(self, matchtype="ANY"):
        # show all words containing only given letter series
        self.fn = u"tamilvu_dictionary_words.txt"
        self.db = []
        self.type = matchtype.lower()
        self.criteria_options = {}
        with codecs.open(self.fn, "r", "utf-8") as fp:
            self.db = map(lambda l: l.strip(), fp.readlines())

    @staticmethod
    def getUyirMeiSeries(ref_letter):
        # if we give 'கை' get full series 'க்','க','கா', ... 'கௌ'
        mei, uyir = safe_splitMeiUyir(ref_letter)
        if uyir in [u"", u" "]:
            return [mei]
        pulli = tamil.utf8.pulli_symbols[0]
        mei = mei[0]  # agaram
        series = [mei + pulli]
        for sym in tamil.utf8.accent_symbols[:-1]:
            series.append(mei + sym)
        return series

    def is_in_sequence(self, letter):
        for ol in self.criteria_options.keys():
            if letter in self.criteria_options[ol]:
                return True
        return False

    def rebuild_criteria(self, criteria):
        Cl = list(set(tamil.utf8.get_letters(criteria)))
        self.criteria_options = {}  # reset
        for cl in Cl:
            self.criteria_options[cl] = FilterDictionary.getUyirMeiSeries(cl)
        return

    def select(self, criteria):
        choices = []  # result
        self.rebuild_criteria(criteria)
        for w in self.db:
            Ll = tamil.utf8.get_letters(w)
            count = 0
            for l in Ll:
                if not self.is_in_sequence(l):
                    break
                count = count + 1
            if count == len(Ll):
                if self.type == "any":
                    choices.append(w)
                elif self.type == "all":
                    # scoreboard
                    rmatches = {x: False for x in self.criteria_options.keys()}
                    for letter in Ll:
                        for ol in self.criteria_options.keys():
                            if letter in self.criteria_options[ol]:
                                rmatches[ol] = rmatches[ol] or True
                    if all(rmatches.values()):
                        choices.append(w)
                else:
                    raise Exception("Incorrect type")
        return choices


while True:
    choices = raw_input(u">> ").decode("UTF-8")  # u"அக"
    matchtype = len(sys.argv) > 1 and sys.argv[1] or "all"
    options = FilterDictionary(matchtype).select(choices)
    for w in options:
        print(u"%s" % w)
    continue
