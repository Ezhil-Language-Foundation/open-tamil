# This Python file uses the following encoding: utf-8
# (C) 2020 முத்து அண்ணாமலை
# This file is part of open-tamil project
import copy as _copy
from tamil.utf8 import get_letters, pulli_symbols
from tamil.utf8 import grantha_agaram_letters, grantha_mei_letters
from tamil.utf8 import uyir_letters, ayudha_letter, splitMeiUyir


# Barathi Braille வழியில் உருவான தமிழ் பிரெயில்
# Ref: https://en.wikipedia.org/wiki/Tamil_Braille
class BrailleCell:
    """
    Describe 3x2 (3-row, 2-col) Braille cell.
    positions are 1-6 from Left->Right, Top->Bot.
    """

    def __init__(self, letter, pos):
        self.letter = letter
        self.pos = _copy.copy(pos)
        self.cells = [[False, False], [False, False], [False, False]]
        assert len(pos) < 6, "6 cell positions can only be specified."
        if len(pos) > 0:
            assert (max(pos) < 7) and (min(pos) > 0), "positions are [1-6] only"
        for _pos in pos:
            x, y = (_pos - 1) % 2, (_pos - 1) // 2
            self.cells[y][x] = True
        # print(self,self.letter)

    def gethash(self):
        return "".join(["%d" % x for x in self.pos])

    def __str__(self):
        result = ""
        for i in range(3):
            for j in range(2):
                if self.cells[i][j]:
                    result += "*"
                else:
                    result += "_"
            result += "\n"
        return result


# எ.கா.
# =>வணக்கம்
# => "⠧⠼⠅⠰⠅⠍⠰"

# Ref: https://en.wikipedia.org/wiki/Tamil_Braille
# Generate Braille cells from Tamil Text
table = {}
table["அ"] = BrailleCell("அ", [1])
table["ஆ"] = BrailleCell("ஆ", [2, 4, 5])
table["இ"] = BrailleCell("இ", [2, 3])
table["ஈ"] = BrailleCell("ஈ", [4, 5])
table["உ"] = BrailleCell("உ", [1, 5, 6])
table["ஊ"] = BrailleCell("ஊ", [1, 3, 4, 6])
table["எ"] = BrailleCell("எ", [3, 6])
table["ஏ"] = BrailleCell("ஏ", [1, 4])
table["ஐ"] = BrailleCell("ஐ", [2, 5])
table["ஒ"] = BrailleCell("ஒ", [1, 2, 5, 6])
table["ஓ"] = BrailleCell("ஓ", [1, 4, 5])
table["ஔ"] = BrailleCell("ஔ", [2, 3, 6])
table["க"] = BrailleCell("க", [1, 5])
table["ங"] = BrailleCell("ங", [2, 5, 6])
table["ச"] = BrailleCell("ச", [1, 2])
table["ஜ"] = BrailleCell("ஜ", [2, 3, 4])
table["ஞ"] = BrailleCell("ஞ", [3, 4])
table["ட"] = BrailleCell("ட", [2, 3, 4, 5, 6])
table["ண"] = BrailleCell("ண", [2, 4, 5, 6])
table["த"] = BrailleCell("த", [2, 3, 4, 5])
table["ந"] = BrailleCell("ந", [1, 2, 4, 5])
table["ப"] = BrailleCell("ப", [1, 2, 3, 5])
table["ம"] = BrailleCell("ம", [1, 2, 5])
table["ய"] = BrailleCell("ய", [1, 2, 4, 5, 6])
table["ர"] = BrailleCell("ர", [1, 3, 4, 5])
table["ல"] = BrailleCell("ல", [1, 3, 5])
table["ள"] = BrailleCell("ள", [2, 4, 6])
table["வ"] = BrailleCell("வ", [1, 3, 5, 6])
table["ஶ"] = BrailleCell("ஶ", [1, 2, 6])
table["ஷ"] = BrailleCell("ஷ", [1, 2, 3, 5, 6])
table["ஸ"] = BrailleCell("ஸ", [2, 3, 5])
table["ஹ"] = BrailleCell("ஹ", [1, 3, 4])
table["க்ஷ"] = BrailleCell("க்ஷ", [1, 2, 3, 4, 5])
table["ற"] = BrailleCell("ற", [1, 2, 3, 4, 6])
table["ழ"] = BrailleCell("ழ", [1, 3, 4, 5, 6])
table["ன"] = BrailleCell("ன", [4, 6])
table["்"] = BrailleCell("்", [2])
table["ஃ"] = BrailleCell("ஃ", [6])

# Ref: http://www.acharya.gen.in:8080/disabilities/br_tut.php#tabular
# ஆங்கில் பிரெயில் எழுத்துக்களும் தமிழ் உயிரெழுத்துக்களுடன்
# ஒன்றாகவே குறியிடப்பட்டுள்ளன.
table["a"] = table["அ"]
table["e"] = table["ஏ"]
table["i"] = table["இ"]
table["o"] = table["ஓ"]
table["u"] = table["உ"]
# ஆங்கில மெய்/consonant களுக்கு மற்ற தனிப்பட்ட
# குறியீடுகள் உள்ளன.
table["b"] = BrailleCell("b", [1, 3])
table["c"] = BrailleCell("c", [1, 2])  # sa
table["d"] = BrailleCell("d", [1, 2, 4])
table["f"] = BrailleCell("f", [1, 2, 3])
table["g"] = BrailleCell("g", [1, 2, 3, 4])
table["h"] = BrailleCell("h", [1, 3, 4])  # ha
table["j"] = BrailleCell("j", [2, 3, 4])  # ja
table["k"] = BrailleCell("k", [1, 5])  # ka
table["l"] = BrailleCell("l", [1, 3, 5])  # la
table["m"] = BrailleCell("m", [1, 2, 5])  # ma
table["n"] = BrailleCell("n", [1, 2, 4, 5])  # Na
table["p"] = BrailleCell("p", [1, 2, 3, 5])  # pa
table["q"] = BrailleCell("q", [1, 2, 3, 4, 5])  # ksha
table["r"] = BrailleCell("r", [1, 3, 4, 5])  # chinna R
table["s"] = BrailleCell("s", [2, 3, 5])  # ஸ
table["t"] = BrailleCell("t", [2, 3, 4, 5])  # த
table["v"] = BrailleCell("v", [1, 3, 5, 6])  # வ
table["w"] = BrailleCell("w", [2, 3, 4, 6])
table["x"] = BrailleCell("x", [1, 2, 5, 6])  # ஒ
table["y"] = BrailleCell("y", [1, 2, 4, 5, 6])  # ய
table["z"] = BrailleCell("z", [1, 4, 5, 6])

table[","] = BrailleCell(",", [3])
table[";"] = BrailleCell(";", [3, 5])
table[":"] = BrailleCell(":", [3, 4])
table["."] = BrailleCell(".", [3, 4, 6])
table["!"] = BrailleCell("!", [3, 4, 5])
table["("] = BrailleCell("(", [3, 4, 5, 6])
table[")"] = BrailleCell(")", [3, 4, 5, 6])
table["'"] = BrailleCell("'", [3, 5, 6])
table['"'] = BrailleCell('"', [4, 5, 6])
table[" "] = BrailleCell(" ", [])
assert len(table) == 74, "Barathi Braille for Tamil is strictly 74  entries."


def map_to_braille(tamil_string):
    result = []
    for letter in get_letters(tamil_string):
        if letter in grantha_mei_letters:
            pos = grantha_mei_letters.index(letter)
            agaram = grantha_agaram_letters[pos]
            result.append(table[agaram])
            result.append(table[pulli_symbols[0]])
        elif letter in uyir_letters or letter == ayudha_letter:
            result.append(table[letter])
        else:
            lMei, lUyir = splitMeiUyir(letter)
            pos = grantha_mei_letters.index(lMei)
            agaram = grantha_agaram_letters[pos]
            result.append(table[agaram])
            if lUyir != "அ":
                result.append(table[lUyir])
    return result
