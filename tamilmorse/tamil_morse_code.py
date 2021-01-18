## -*- coding: utf-8 -*-
# (C) 2018 Muthiah Annamalai
# This file is part of Open-Tamil project
# You may use or distribute this file under terms of MIT license
##
from __future__ import print_function
import codecs
import json

from solthiruthi import resources
from .huffman import huffman, print_huffman_code_cwl


def TVU_morse_code():
    # unigram data from Project Madurai
    unigram = TamilUnigramStats().unigram
    build_morse_code(unigram)


def Madurai_morse_code():
    # unigram data from Project Madurai
    unigram = MaduraiUnigramStats().unigram
    build_morse_code(unigram)


def build_morse_code(unigram):
    v_keys = unigram.keys()
    p = [unigram[k] for k in v_keys]
    code, _ = huffman(v_keys, p)
    cwl, codelist = print_huffman_code_cwl(code, p, v_keys)
    tamilmorse = {}
    print(u"<ul>")
    descending_keys = [
        x for _, x in sorted(zip(unigram.values(), v_keys), reverse=True)
    ]
    for k in descending_keys:
        v = code[k]
        v = v.replace("0", ".").replace("1", "-")
        tamilmorse[k] = v
        print(u"<li>%s  -&gt; <b><kbd>%s</kbd></b></li>" % (k, v))
    print(u"</ul>")
    with codecs.open("tamilmorse.json", "w", "utf-8") as fp:
        fp.write(json.dumps(tamilmorse))
    return


class UnigramStats:
    def __init__(self, filename):
        self.unigram = {}  # Tamil letter -> probability of occurence
        self.unigram_file = resources.mk_path(filename)
        with codecs.open(self.unigram_file, "r", "utf-8") as fp:
            for L in fp.readlines():
                a, b = L.split("-")
                a = a.strip()
                b = b.strip()
                self.unigram[a] = float(b)
            normalize = 1 + sum(self.unigram.values())
            for k, v in self.unigram.items():
                self.unigram[k] = v / normalize


class TamilUnigramStats(UnigramStats):
    def __init__(self):
        UnigramStats.__init__(self, "tvu_unigram.txt")


class MaduraiUnigramStats(UnigramStats):
    def __init__(self):
        UnigramStats.__init__(self, "madurai_unigram.txt")


if __name__ == u"__main__":
    Madurai_morse_code()
