#!/usr/bin/python
# This Python file uses the following encoding: utf-8

# Port of Prof. Vasu Renganathan's Tamil TTS to Python
# This file is released under terms of MIT License
# (C) 2017 - Ezhil Language Foundation

import tamil
import os
import sys
import re
import time
import codecs
from pprint import pprint

_DEBUG = False


# Syllable to AF mapper
class Syllable2AF(object):
    numeral_digits = [
        "saiphar",
        "onru",
        "irandu",
        "muunru",
        "naanku",
        "ainthu",
        "aaru",
        "eezu",
        "ettu",
        "onpathu",
        "pattu",
    ]
    AudioMap = {
        ".": "stop",
        u" ": "space1",
        u" ": "space",
        u"அ": "a",
        u"ஆ": "aa",
        u"இ": "i",
        u"ஈ": "ii",
        u"உ": "u",
        u"ஊ": "uu",
        u"எ": "e",
        u"ஏ": "ee",
        u"ஐ": "ai",
        u"ஒ": "o",
        u"ஓ": "oo",
        u"ஔ": "au",
        u"ஃ": "space1",
        u"க": "ka",
        u"கா": "kaa",
        u"கி": "ki",
        u"கீ": "kii",
        u"கு": "ku",
        u"கூ": "kuu",
        u"கெ": "ke",
        u"கே": "kee",
        u"கை": "kai",
        u"கொ": "ko",
        u"கோ": "koo",
        u"கௌ": "kau",
        u"க்": "k",
        u"க்ஷ": "ksha",
        u"க்ஷா": "kshaa",
        u"க்ஷி": "kshi",
        u"க்ஷீ": "kshii",
        u"க்ஷு": "kshu",
        u"க்ஷூ": "kshuu",
        u"க்ஷெ": "kshe",
        u"க்ஷே": "kshee",
        u"க்ஷை": "kshai",
        u"க்ஷொ": "ksho",
        u"க்ஷோ": "kshoo",
        u"க்ஷௌ": "kshau",
        u"ங": "nga",
        u"ஙா": "ngaa",
        u"ஙி": "ngi",
        u"ஙீ": "ngii",
        u"ஙு": "ngu",
        u"ஙூ": "nguu",
        u"ஙெ": "nge",
        u"ஙே": "ngee",
        u"ஙை": "ngai",
        u"ஙொ": "ngo",
        u"ஙோ": "ngoo",
        u"ஙௌ": "ngau",
        u"ங்": "ng",
        u"ச": "ca",
        u"சா": "caa",
        u"சி": "ci",
        u"சீ": "cii",
        u"சு": "cu",
        u"சூ": "cuu",
        u"செ": "ce",
        u"சே": "cee",
        u"சை": "cai",
        u"சொ": "co",
        u"சோ": "coo",
        u"சௌ": "cau",
        u"ச்": "c",
        u"ஜ": "ja",
        u"ஜா": "jaa",
        u"ஜி": "ji",
        u"ஜீ": "jii",
        u"ஜு": "ju",
        u"ஜூ": "juu",
        u"ஜெ": "je",
        u"ஜே": "jee",
        u"ஜை": "jai",
        u"ஜொ": "jo",
        u"ஜோ": "joo",
        u"ஜௌ": "jau",
        u"ஜ்": "j",
        u"ஞ": "nja",
        u"ஞா": "njaa",
        u"ஞி": "nji",
        u"ஞீ": "njii",
        u"ஞு": "nju",
        u"ஞூ": "njuu",
        u"ஞெ": "nje",
        u"ஞே": "njee",
        u"ஞை": "njai",
        u"ஞொ": "njo",
        u"ஞோ": "njoo",
        u"ஞௌ": "njau",
        u"ஞ்": "nj",
        u"ட": "ta",
        u"டா": "taa",
        u"டி": "ti",
        u"டீ": "tii",
        u"டு": "tu",
        u"டூ": "tuu",
        u"டெ": "te",
        u"டே": "tee",
        u"டை": "tai",
        u"டொ": "to",
        u"டோ": "too",
        u"டௌ": "tau",
        u"ட்": "t",
        u"ண": "nnna",
        u"ணா": "nnnaa",
        u"ணி": "nnni",
        u"ணீ": "nnnii",
        u"ணு": "nnnu",
        u"ணூ": "nnnuu",
        u"ணெ": "nnne",
        u"ணே": "nnnee",
        u"ணை": "nnnai",
        u"ணொ": "nnno",
        u"ணோ": "nnnoo",
        u"ணௌ": "nnnau",
        u"ண்": "nnn",
        u"த": "tha",
        u"தா": "thaa",
        u"தி": "thi",
        u"தீ": "thii",
        u"து": "thu",
        u"தூ": "thuu",
        u"தெ": "the",
        u"தே": "thee",
        u"தை": "thai",
        u"தொ": "tho",
        u"தோ": "thoo",
        u"தௌ": "thau",
        u"த்": "th",
        u"ந": "na",
        u"நா": "naa",
        u"நி": "ni",
        u"நீ": "nii",
        u"நு": "nu",
        u"நூ": "nuu",
        u"நெ": "ne",
        u"நே": "nee",
        u"நை": "nai",
        u"நொ": "no",
        u"நோ": "noo",
        u"நௌ": "nau",
        u"ந்": "n",
        u"ன": "nna",
        u"னா": "nnaa",
        u"னி": "nni",
        u"னீ": "nnii",
        u"னு": "nnu",
        u"னூ": "nnuu",
        u"னெ": "nne",
        u"னே": "nnee",
        u"னை": "nnai",
        u"னொ": "nno",
        u"னோ": "nnoo",
        u"னௌ": "nnau",
        u"ன்": "nn",
        u"ப": "pa",
        u"பா": "paa",
        u"பி": "pi",
        u"பீ": "pii",
        u"பு": "pu",
        u"பூ": "puu",
        u"பெ": "pe",
        u"பே": "pee",
        u"பை": "pai",
        u"பொ": "po",
        u"போ": "poo",
        u"பௌ": "pau",
        u"ப்": "p",
        u"ம": "ma",
        u"மா": "maa",
        u"மி": "mi",
        u"மீ": "mii",
        u"மு": "mu",
        u"மூ": "muu",
        u"மெ": "me",
        u"மே": "mee",
        u"மை": "mai",
        u"மொ": "mo",
        u"மோ": "moo",
        u"மௌ": "mau",
        u"ம்": "m",
        u"ய": "ya",
        u"யா": "yaa",
        u"யி": "yi",
        u"யீ": "yii",
        u"யு": "yu",
        u"யூ": "yuu",
        u"யெ": "ye",
        u"யே": "yee",
        u"யை": "yai",
        u"யொ": "yo",
        u"யோ": "yoo",
        u"யௌ": "yau",
        u"ய்": "y",
        u"ர": "ra",
        u"ரா": "raa",
        u"ரி": "ri",
        u"ரீ": "rii",
        u"ரு": "ru",
        u"ரூ": "ruu",
        u"ரெ": "re",
        u"ரே": "ree",
        u"ரை": "rai",
        u"ரொ": "ro",
        u"ரோ": "roo",
        u"ரௌ": "rau",
        u"ர்": "r",
        u"ற": "rra",
        u"றா": "rraa",
        u"றி": "rri",
        u"றீ": "rrii",
        u"று": "rru",
        u"றூ": "rruu",
        u"றெ": "rre",
        u"றே": "rree",
        u"றை": "rrai",
        u"றொ": "rro",
        u"றோ": "rroo",
        u"றௌ": "rrau",
        u"ற்": "rr",
        u"ல": "la",
        u"லா": "laa",
        u"லி": "li",
        u"லீ": "lii",
        u"லு": "lu",
        u"லூ": "luu",
        u"லெ": "le",
        u"லே": "lee",
        u"லை": "lai",
        u"லொ": "lo",
        u"லோ": "loo",
        u"லௌ": "lau",
        u"ல்": "l",
        u"ள": "lla",
        u"ளா": "llaa",
        u"ளி": "lli",
        u"ளீ": "llii",
        u"ளு": "llu",
        u"ளூ": "lluu",
        u"ளெ": "lle",
        u"ளே": "llee",
        u"ளை": "llai",
        u"ளொ": "llo",
        u"ளோ": "lloo",
        u"ளௌ": "llau",
        u"ள்": "ll",
        u"ழ": "za",
        u"ழா": "zaa",
        u"ழி": "zi",
        u"ழீ": "zii",
        u"ழு": "zu",
        u"ழூ": "zuu",
        u"ழெ": "ze",
        u"ழே": "zee",
        u"ழை": "zai",
        u"ழொ": "zo",
        u"ழோ": "zoo",
        u"ழௌ": "zau",
        u"ழ்": "z",
        u"வ": "va",
        u"வா": "vaa",
        u"வி": "vi",
        u"வீ": "vii",
        u"வு": "vu",
        u"வூ": "vuu",
        u"வெ": "ve",
        u"வே": "vee",
        u"வை": "vai",
        u"வொ": "vo",
        u"வோ": "voo",
        u"வௌ": "vau",
        u"வ்": "v",
        u"ஶ": "space1",
        u"ஶா": "space1",
        u"ஶி": "space1",
        u"ஶீ": "space1",
        u"ஶு": "space1",
        u"ஶூ": "space1",
        u"ஶெ": "space1",
        u"ஶே": "space1",
        u"ஶை": "space1",
        u"ஶொ": "space1",
        u"ஶோ": "space1",
        u"ஶௌ": "space1",
        u"ஷ": "sha",
        u"ஷா": "shaa",
        u"ஷி": "shi",
        u"ஷீ": "shii",
        u"ஷு": "shu",
        u"ஷூ": "shuu",
        u"ஷெ": "she",
        u"ஷே": "shee",
        u"ஷை": "shai",
        u"ஷொ": "sho",
        u"ஷோ": "shoo",
        u"ஷௌ": "shau",
        u"ஷ்": "sh",
        u"ஸ": "sa",
        u"ஸா": "saa",
        u"ஸி": "si",
        u"ஸீ": "sii",
        u"ஸு": "su",
        u"ஸூ": "suu",
        u"ஸெ": "se",
        u"ஸே": "see",
        u"ஸை": "sai",
        u"ஸொ": "so",
        u"ஸோ": "soo",
        u"ஸௌ": "sau",
        u"ஸ்": "s",
        u"ஹ": "ha",
        u"ஹா": "haa",
        u"ஹி": "hi",
        u"ஹீ": "hii",
        u"ஹு": "hu",
        u"ஹூ": "huu",
        u"ஹெ": "he",
        u"ஹே": "hee",
        u"ஹை": "hai",
        u"ஹொ": "ho",
        u"ஹோ": "hoo",
        u"ஹௌ": "hau",
        u"ஹ்": "h",
    }

    def __init__(self):
        super(Syllable2AF, self).__init__()

    @staticmethod
    def syllable_mapper_uyir_mei(in_syllable):
        data = Syllable2AF.AudioMap.get(in_syllable, None)
        if not data:
            # convert digits
            try:
                digit = int(in_syllable)
                return Syllable2AF.numeral_digits[digit]
            except ValueError as vex:
                data = "space"  # bad literal, _, +, -, (, ) etc.

        return data


# make this number go to 247+
if _DEBUG:
    print(
        "filled = %d/%d"
        % (
            len(list(filter(len, Syllable2AF.AudioMap.values()))),
            len(Syllable2AF.AudioMap.values()),
        )
    )


# text to be output as audio
class SubjectText(object):
    def __init__(self, text):
        super(SubjectText, self).__init__()
        self.text = text
        self.filename = "<text>"
        self.syllables = []
        self.audiomapping = ["space", "space1"]  # ambient start

        self._map_to_syllables()
        self._build_audio_mapping()
        self._soften_stops()

    def reset(self):
        while len(self.audiomapping) > 0:
            self.audiomapping.pop()

    def _map_to_syllables(self):
        tamil_or_spc = lambda x: tamil.utf8.istamil(x) or x in [
            " ",
            "\r",
            "\n",
            ".",
            ",",
            ";",
            "?",
            "!",
        ]
        self.syllables = filter(tamil_or_spc, tamil.utf8.get_letters(self.text))

    def _build_audio_mapping(self):
        REPEAT_SPACE = 2
        for syllable in self.syllables:
            # syll = AudioMap.get(syllable,"space")
            # syll = syll != '' and syll or "space"
            syll = Syllable2AF.syllable_mapper_uyir_mei(syllable)
            self.audiomapping.append(syll)
            if syll in ["space1", "space"]:
                for i in range(0, REPEAT_SPACE):
                    self.audiomapping.append(syll)

    # port of 'soften stops' subroutine from Prof. Vasu's code.
    # soften intervocalic and after nasal stop consonants
    def _soften_stops(self):
        for pos in range(1, len(self.audiomapping)):
            curr_s = self.audiomapping[pos]
            prev_s = self.audiomapping[pos - 1]
            next_s = (
                    (pos < len(self.audiomapping) - 1)
                    and self.audiomapping[pos + 1]
                    or None
            )
            if curr_s.startswith("k"):
                if prev_s.startswith("ng"):
                    curr_s = "ng" + curr_s[1:]
                elif curr_s != "k" and prev_s != "k" and prev_s != "space":
                    curr_s = "h" + curr_s[1:]
            elif curr_s.startswith("c"):
                if prev_s == "nj":
                    curr_s = "j" + curr_s[1:]
                elif curr_s != "c" and prev_s != "c" and prev_s != "space":
                    curr_s = "s" + curr_s[1:]
            elif curr_s.startswith("th"):
                if prev_s in ["n", "u"] or (
                        curr_s != "th" and prev_s != "th" and prev_s != "space"
                ):
                    if _DEBUG:
                        curr_old = curr_s
                    curr_s = "dh" + curr_s[2:]
                    if _DEBUG:
                        print(
                            "Softening %s%s -> %s%s"
                            % (prev_s, curr_old, prev_s, curr_s)
                        )
                elif next_s and next_s.find("space") >= 0:
                    curr_s = "dh" + curr_s[2:]
            elif curr_s.startswith("t"):
                if prev_s == "nnn" or (
                        curr_s != "t" and prev_s != "space" and prev_s != "t"
                ):
                    curr_s = "d" + curr_s[1:]
            elif curr_s.startswith("p"):
                if prev_s == "m" or (
                        curr_s != "p" and prev_s != "p" and prev_s != "space"
                ):
                    curr_s = "b" + curr_s[1:]
            self.audiomapping[pos] = curr_s

    def get_audiofile_order(self):
        # ['va','na','ka','m']
        if _DEBUG:
            pprint(self.audiomapping)
        return self.audiomapping


# driver class
class ConcatennativeTTS(object):
    TARGETDIR = os.path.join(os.path.split(__file__)[0], "tamilsound")
    FMT = "mp3"

    def __init__(self, text, outputfile):
        super(ConcatennativeTTS, self).__init__()
        self.outputfile = outputfile
        self.subject_text = SubjectText(text)

    def run(self):
        self._mergeaudio()  # write to outputfile

    def _mergeaudio(self):
        full_syllable_files = [
            os.path.join(
                ConcatennativeTTS.TARGETDIR, syllable_file + "." + ConcatennativeTTS.FMT
            )
            for syllable_file in self.subject_text.get_audiofile_order()
        ]
        missing = []
        with open(self.outputfile, "wb") as out_fp:
            for f in full_syllable_files:
                try:
                    with open(f, "rb") as in_fp:
                        out_fp.write(in_fp.read())
                except IOError as ioe:
                    if _DEBUG:
                        missing.append(os.path.basename(f).split(".")[0])
                    print(
                        'Warning: cannot synthesize syllable "%s" with error \n\t[%s]'
                        % (os.path.basename(f).split(".")[0], str(ioe))
                    )
        if _DEBUG and len(missing) >= 1:
            pprint(set(missing))
        return


if __name__ == u"__main__":
    if len(sys.argv) < 3:
        print("Usage: ")
        print("driver.py $AUDIO_OUTPUTFILENAME $TAMIL_TEXTFILENAME")
        sys.exit(-1)

    filename_in = sys.argv[2]
    outputfile = sys.argv[1]
    start = time.time()
    with codecs.open(filename_in, "r", "UTF-8") as fp:
        data = fp.read()
        tts = ConcatennativeTTS(data, outputfile)
        tts.run()
    lapsed = time.time() - start
    print(u"Tamil speech output to %s in %g(s)" % (outputfile, lapsed))
    sys.exit(0)
