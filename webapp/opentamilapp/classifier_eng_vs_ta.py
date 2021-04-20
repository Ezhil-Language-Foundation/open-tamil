## This Python file uses the following encoding: utf-8
## (C) 2017 Muthiah Annamalai <ezhillang@gmail.com>
## This code is released under public domain
import codecs
from tamil import utf8
from transliterate import azhagi, jaffna, combinational, algorithm


def demo_classify():
    for l in utf8.get_letters_iterable("இதுதாண்டாபோலிசு"):
        print(("%s - %s" % (l, utf8.classify_letter(l))))


def jaffna_transliterate(eng_string):
    tamil_tx = algorithm.Iterative.transliterate(
        jaffna.Transliteration.table, eng_string
    )
    return tamil_tx


def azhagi_transliterate(eng_string):
    tamil_tx = algorithm.Iterative.transliterate(
        azhagi.Transliteration.table, eng_string
    )
    return tamil_tx


def combinational_transliterate(eng_string):
    tamil_tx = algorithm.Iterative.transliterate(
        combinational.Transliteration.table, eng_string
    )
    return tamil_tx


def operations():
    # 3 forms of Tamil transliteration for English word
    jfile = codecs.open("english_dictionary_words.jaffna", "w", "utf-8")
    cfile = codecs.open("english_dictionary_words.combinational", "w", "utf-8")
    afile = codecs.open("english_dictionary_words.azhagi", "w", "utf-8")

    with codecs.open("english_dictionary_words.txt", "r") as engf:
        for idx, w in enumerate(engf.readlines()):
            w = w.strip()
            if len(w) < 1:
                continue
            print(idx)
            jfile.write("%s\n" % jaffna_transliterate(w))
            cfile.write("%s\n" % combinational_transliterate(w))
            afile.write("%s\n" % azhagi_transliterate(w))

    jfile.close()
    cfile.close()
    afile.close()


if __name__ == "__main__":
    operations()
