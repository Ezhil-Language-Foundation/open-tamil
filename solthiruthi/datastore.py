## -*- coding: utf-8 -*-
## (C) 2015-2019 Muthiah Annamalai,
##
from __future__ import print_function
import abc
import sys
import codecs
import pickle
from tamil import utf8
from pprint import pprint

PYTHON3 = sys.version[0] == "3"


class Queue(list):
    ExceptionMsg = u"Queue does not support list method %s"

    # implement a FIFO structure based on a list
    def __init__(self):
        super(Queue, self).__init__()

    def insert(self, obj):
        super(Queue, self).insert(0, obj)

    def peek(self):
        """ look at next imminent item """
        return self[0]

    def isempty(self):
        return self.__len__() == 0

    def __getitem__(self, pos):
        LEN = self.__len__()
        if pos != 0 and pos != -1 and pos != (LEN - 1):
            raise Exception(
                Queue.ExceptionMsg % u"index" + u" as invoked @ pos= %d" % pos
            )
        if pos == -1:
            pos = LEN - 1
        return super(Queue, self).__getitem__(LEN - 1 - pos)

    def reverse(self):
        raise Exception(Queue.ExceptionMsg % "reverse")

    def __getslice__(self):
        raise Exception(Queue.ExceptionMsg % "__getslice__")

    def remove(self):
        raise Exception(Queue.ExceptionMsg % "remove")

    def sort(self):
        raise Exception(Queue.ExceptionMsg % "sort")

    def append(self, obj):
        raise Exception(Queue.ExceptionMsg % "append")


class Trie(utf8.CacheGetLettersMixin):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super(Trie, self).__init__()

    # concrete implementation for cached mixin
    def get_letters_impl(self, word):
        return self.is_english and [l for l in word] or utf8.get_letters(word)

    @abc.abstractmethod
    def add(self, word):
        return

    @abc.abstractmethod
    def isWord(self, word, ret_ref_trie=False):
        """ return a boolean as first output, and second output will be the reference trie """
        return

    @abc.abstractmethod
    def getAllWords(self):
        return

    @abc.abstractmethod
    def getAllWordsPrefix(self, prefix):
        return

    @abc.abstractmethod
    def hasWordPrefix(self, prefix):
        return

    @abc.abstractmethod
    def getAllWordsIterable(self):
        for word in self.getAllWords():
            yield word
        return

    @staticmethod
    def mk_empty_trie(alpha_len):
        return [[False, None] for i in range(alpha_len)]

    def loadWordFile(self, filename):
        # words will be loaded from the file into the Trie structure
        with codecs.open(filename, "r", "utf-8") as fp:
            # 2-3 compatible
            for word in fp.readlines():
                self.add(word.strip())
        return

    @staticmethod
    def serializeToFile(obj, filename):
        with open(filename, u"wb") as fp:
            pickle.dump(obj, fp)
        return True

    @staticmethod
    def deserializeFromFile(filename):
        obj = None
        with open(filename, u"rb") as fp:
            obj = pickle.load(fp)
        return obj


class Node:
    def __init__(self):
        # super(Node,self).__init__()
        self.__dict__ = {"alphabets": {}, "is_word": {}, "count": {}}

    def __str__(self):
        return str(self.__dict__)


class DTrie(Trie):
    """trie where number of alphabets at each nodes grows with time;
    implementation uses a dictionary; it contains an attribute count for frequency of letter.
    """

    def __init__(self):
        super(DTrie, self).__init__()
        self.trie = Node()  # root node
        self.is_english = False

    @staticmethod
    def buildEnglishTrie(nalpha=26):
        obj = DTrie()
        obj.is_english = True
        return obj

    def hasWordPrefix(self, wrd_prefix):
        return self.isWordAndTrie(wrd_prefix, prefix=True)

    def isWord(self, word, ret_ref_trie=False):
        rval, ref_trie = self.isWordAndTrie(word)
        if ret_ref_trie:
            return rval, ref_trie
        return rval

    def isWordAndTrie(self, word, prefix=False):
        ref_trie = self.trie
        letters = self.get_letters(word)
        wLen = len(letters)
        rval = False
        is_prefix = False
        prev_trie = None
        for idx, letter in enumerate(letters):
            # print(str(ref_trie))
            rval = ref_trie.is_word.get(letter, False)
            prev_trie = ref_trie
            ref_trie = ref_trie.alphabets.get(letter, None)
            if not ref_trie:
                break

        if prefix:
            if idx < (len(letters) - 1):
                return False
            elif not ref_trie:
                return False
            return True

        return rval, prev_trie

    def getWordCount(self, word):
        isWord, ref_trie = self.isWord(word, ret_ref_trie=True)
        if not isWord:
            raise Exception(u"Word does not exist in Trie")
        # pprint(str(ref_trie))
        letters = self.get_letters(word)
        return ref_trie.count[letters[-1]]

    def add(self, word):
        ref_trie = self.trie
        letters = self.get_letters(word)
        wLen = len(letters)
        prev_trie = None
        assert wLen >= 1
        for idx, letter in enumerate(letters):
            value = ref_trie.alphabets.get(letter, None)
            prev_trie = ref_trie
            if not value:
                ref_trie.alphabets[letter] = Node()
                ref_trie.is_word[letter] = False
                ref_trie.count[letter] = 0
                ref_trie = ref_trie.alphabets[letter]
            else:
                ref_trie = value
        # print(str(prev_trie))
        last_trie = prev_trie
        last_trie.is_word[letter] = True
        last_trie.count[letter] += 1
        return

    def getAllWordsAndCount(self):
        # less efficient method but quick-n-dirty
        d = dict()
        for word in self.getAllWordsIterable():
            count = self.getWordCount(word)
            d.update({word: count})
        return d

    def getAllWords(self):
        # list all words in the trie structure in DFS fashion
        all_words = []
        self.getAllWordsHelper(self.trie, prefix=[], all_words=all_words)
        return all_words

    def getAllWordsPrefix(self, prefix):
        all_words = []
        val, curr_trie = self.isWord(prefix, ret_ref_trie=True)
        prefix_letters = self.get_letters(prefix)
        ref_trie = curr_trie.alphabets.get(prefix_letters[-1], curr_trie)
        # print(ref_trie.__str__())
        # ignore val
        if val:
            all_words.append(prefix)
        self.getAllWordsHelper(ref_trie, prefix_letters, all_words=all_words)
        return all_words

    def getAllWordsHelper(self, ref_trie, prefix, all_words):
        for letter in sorted(ref_trie.alphabets.keys()):
            prefix.append(letter)
            if ref_trie.is_word[letter]:
                all_words.append(u"".join(prefix))
            if ref_trie.alphabets[letter]:
                # DFS
                self.getAllWordsHelper(ref_trie.alphabets[letter], prefix, all_words)
            prefix.pop()
        return

    def getAllWordsIterable(self):
        return self.getAllWordsIterableHelper(self.trie, [])

    def getAllWordsIterableHelper(self, ref_trie, prefix):
        for letter in sorted(ref_trie.alphabets.keys()):
            prefix.append(letter)
            if ref_trie.is_word[letter]:
                yield u"".join(prefix)
            if ref_trie.alphabets[letter]:
                # DFS
                for word in self.getAllWordsIterableHelper(
                    ref_trie.alphabets[letter], prefix
                ):
                    yield word
            prefix.pop()
        return


# reverse trie : add words in reverse fashion for 'endswith' interface
class RTrie(DTrie):
    def __init__(self, is_tamil=False):
        DTrie.__init__(self)
        self.is_tamil = is_tamil

    def reverse(self, word):
        if self.is_tamil:
            rev_word = utf8.reverse_word(word)
        else:
            rev_word = word[::-1]
        return rev_word

    def add(self, word):
        rev_word = self.reverse(word)
        DTrie.add(self, rev_word)

    def getAllWordsIterable(self):
        # internal storage is in reverse order, but we insert/retrieve for
        # user via regular word order.
        for word in DTrie.getAllWordsIterable(self):
            yield self.reverse(word)
        return

    def getAllWordsPrefix(self, pfx):
        for word_pfx in DTrie.getAllWordsPrefix(self, self.reverse(pfx)):
            yield self.reverse(word_pfx)
        return

    def getWordsEndingWith(self, sfx):
        for word_sfx in self.getAllWordsPrefix(sfx):
            yield word_sfx
        return


class TamilTrie(Trie):
    "Store a list of words into the Trie data structure"

    @staticmethod
    def buildEnglishTrie(nalpha=26):
        # utility method
        to_eng = lambda x: chr(x + ord("a"))
        eng_idx = lambda x: ord(x.lower()) - ord("a")
        obj = TamilTrie(eng_idx, to_eng, nalpha)
        obj.is_english = True
        return obj

    def __init__(
        self,
        get_idx=utf8.getidx,
        invert_idx=utf8.tamil,
        alphabet_len=utf8.TA_LETTERS_LEN,
    ):
        super(Trie, self).__init__()
        self.L = alphabet_len
        self.trie = Trie.mk_empty_trie(self.L)
        self.word_limits = Trie.mk_empty_trie(self.L)
        self.getidx = get_idx
        self.invertidx = invert_idx
        self.is_english = False

    def getAllWords(self):
        # list all words in the trie structure in DFS fashion
        all_words = []
        self.getAllWordsHelper(
            self.trie, self.word_limits, prefix=[], all_words=all_words
        )
        return all_words

    def getAllWordsHelper(self, ref_trie, ref_word_limits, prefix, all_words):
        for letter_pos in range(0, len(ref_trie)):
            if ref_trie[letter_pos][0]:
                letter = self.invertidx(letter_pos)
                prefix.append(letter)
                if ref_word_limits[letter_pos][0]:
                    all_words.append(u"".join(prefix))
                if ref_trie[letter_pos][1]:
                    # DFS
                    self.getAllWordsHelper(
                        ref_trie[letter_pos][1],
                        ref_word_limits[letter_pos][1],
                        prefix,
                        all_words,
                    )
                prefix.pop()
        return

    def getAllWordsIterable(self):
        for word in self.getAllWords():
            yield word
        return

    def getAllWordsPrefix(self, prefix):
        raise Exception("NOT IMPLEMENTED RIGHT")
        all_words = []
        val, ref_trie, ref_word_limits = self.isWord(prefix, ret_ref_trie=True)
        # ignore val
        if val:
            all_words.append(prefix)
        prefix_letters = self.get_letters(prefix)
        self.getAllWordsHelper(ref_trie, ref_word_limits, prefix_letters, all_words)
        return all_words

    def hasWordPrefix(self, prefix):
        raise Exception("not implemented | X")

    def isWord(self, word, ret_ref_trie=False):
        # see if @word is present in the current Trie; return True or False
        letters = self.get_letters(word)
        wLen = len(letters)
        ref_trie = self.trie
        ref_word_limits = self.word_limits
        for itr, letter in enumerate(letters):
            idx = self.getidx(letter)
            # print(idx, letter)
            if itr == (wLen - 1):
                break
            if not ref_trie[idx][1]:
                return False  # this branch of Trie did not exist
            ref_trie = ref_trie[idx][1]
            ref_word_limits = ref_word_limits[idx][1]

        if ret_ref_trie:
            return ref_word_limits[idx][0], ref_trie, ref_word_limits
        return ref_word_limits[idx][0]

    def add(self, word):
        # trie data structure is built here
        # print("*"*30,"adding","*"*30)
        letters = self.get_letters(word)
        wLen = len(letters)
        ref_trie = self.trie
        ref_word_limits = self.word_limits
        for itr, letter in enumerate(letters):
            try:
                idx = self.getidx(letter)
            except Exception as exp:
                continue
            # print(idx, itr)
            ref_trie[idx][0] = True
            if itr == (wLen - 1):
                break
            if not ref_trie[idx][1]:
                ref_trie[idx][1] = Trie.mk_empty_trie(self.L)
                ref_word_limits[idx][1] = Trie.mk_empty_trie(self.L)
            ref_trie = ref_trie[idx][1]
            ref_word_limits = ref_word_limits[idx][1]
        ref_word_limits[idx][0] = True
        # pprint( self.trie )
        # pprint( self.word_limits )


def do_stuff():
    obj = DTrie()  # TamilTrie.buildEnglishTrie()
    # pprint( obj.trie )
    [obj.add(w) for w in ["apple", "apple", "amma", "appa", "love", "strangeness"]]
    all_words = [
        "apple",
        "amma",
        "appa",
        "love",
        "strangeness",
        "purple",
        "yellow",
        "tail",
        "tuna",
        "maki",
        "ammama",
    ]
    print("###### dostuff ################################")
    # print( obj.trie )
    for w in all_words:
        ret = obj.isWord(w, True)
        print(w, str(ret[0]), str(ret[1]))
    pprint(obj.trie)
    pprint(obj.getAllWords())
    pprint(obj.getWordCount("apple"))

    obj = DTrie()
    for i in range(3):
        obj.add("a")
    for j in range(4):
        obj.add("b")
    print(obj.trie.__str__())

    return obj


def do_load():
    " 4 GB program - very inefficient "
    obj = DTrie()  # TamilTrie()
    obj.loadWordFile("data/tamilvu_dictionary_words.txt")
    print(len(obj.getAllWords()))


if __name__ == u"__main__":
    do_stuff2()
