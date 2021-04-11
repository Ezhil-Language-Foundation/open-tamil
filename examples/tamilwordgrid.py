#!python
# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

import sys
import imp

try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3

# imp.reload(sys)
# sys.setdefaultencoding('utf-8')

import copy, random
import tamil
import re
import codecs
from math import sqrt

PYTHON3 = sys.version > "3"


# Vertical / Horizontal Word Grids
class Solver:
    def __init__(self, wordgrid):
        self.wordgrid = wordgrid

    def place(self):
        # dynamic programming algorithm
        # calculate the available positions to place the word
        # place 1 word then solve same problem of placing n-1 words on modified grid
        # if next steps of placing the n-1 words fails, we need to cleanup the current placement
        # if unable to place the word, return false
        self.wordgrid.precompute()


# Put a list of words into a grid. this is purely vertical or purely horizontal style.
class WordGrid:
    @staticmethod
    def sorter(a, b):
        if len(a) > len(b):
            return 1
        if len(a) == len(b):
            return 0
        return -1

    @staticmethod
    def compute(words, fill_letters, outputfile=None):
        drv = WordGrid(words, fill_letters)
        drv.precompute()
        drv.clear_placements()
        drv.generate()
        drv.display(outputfile)
        print(drv.grid_size)
        print(drv.grid)
        return

    def __init__(self, words, letters):
        self.words = copy.copy(words)
        self.words_letters = [tamil.utf8.get_letters(word_i) for word_i in words]
        self.fill_letters = letters
        self.max_word_len = 0
        self.grid_size = 0
        self.grid = list()
        pass

    def __del__(self):
        del self.words
        del self.grid

    def display(self, output):
        if not output:
            output = sys.stdout

        output.write(
            '<html><meta charset="UTF-8" />\n<head><title>word grids</title></head>\n<body>\n'
        )
        output.write(
            """<style>
        table {
    border-collapse: collapse;
}
tr:nth-child(even){background-color: #f2f2f2}
table, th, td {
    border: 1px solid black;
}
td {
width : 40px;
height: 40px;
text-align : center;
}
</style>"""
        )
        output.write("<div><ol>\n")
        for w in self.words:
            lw = len(tamil.utf8.get_letters(w))
            output.write("<li>%s | %d</li>\n" % (w, lw))
        output.write("</ol></div>\n")
        output.write("<table>\n")
        for row_idx in range(len(self.grid)):
            row_data = " ".join(
                "<td>%s</td>" % self.grid[row_idx][col_idx][0]
                for col_idx in range(len(self.grid[row_idx]))
            )
            output.write("<tr>%s</tr>\n" % row_data)
        output.write("</table>\n")
        # occupancy
        output.write("<hr/>\n")
        output.write("<table>\n")
        for row_idx in range(len(self.grid)):
            row_data = " ".join(
                "<td>%s</td>" % (self.grid[row_idx][col_idx][1] and "X" or "\u25A0")
                for col_idx in range(len(self.grid[row_idx]))
            )
            output.write("<tr>%s</tr>\n" % row_data)
        output.write("</table>\n")
        # style=\"border: 1px solid black;\"
        output.write("</body></html>\n")
        return

        output.write("<= P =>")
        for row_idx in range(len(self.grid)):
            row_data = " ".join(
                str(self.grid[row_idx][col_idx][1])[0]
                for col_idx in range(len(self.grid[row_idx]))
            )
            output.write(row_data)
        return

    def precompute(self):
        # grid rows = no of words
        # grid size = no of columns
        self.max_word_len = int(
            (max(list([len(tamil.utf8.get_letters(x)) for x in self.words])))
        )
        self.grid_size = 3 + int(self.max_word_len)
        # sort words in order
        if PYTHON3:
            self.words = sorted(self.words, key=len)
        else:
            self.words.sort(cmp=WordGrid.sorter)
        # prepare a random grid of dim [#words x #max-word-length]
        # len(self.words)
        for itr_r in range(self.grid_size):
            self.grid.append(
                [
                    [random.choice(self.fill_letters), False]
                    for i in range(self.grid_size)
                ]
            )
        return

    def clear_placements(self):
        # grid rows = no of words
        # grid size = no of columns
        # prepare a random grid of dim [#words x #max-word-length]
        for idx in range(0, self.grid_size):
            for idy in range(0, self.grid_size):
                self.grid[idx][idy][1] = False
                self.grid[idx][idy][0] = random.choice(self.fill_letters)
        return

    # return if x,y position in the grid is empty or filled
    def is_empty(self, x, y):
        return self.grid[x][y][1]
        return None

    def generate_vertical(self):
        self.generate_horizontal()
        # transpose the array.
        grid_new = list()
        for itr in range(len(self.grid[0])):
            grid_new.append(list(range(len(self.grid))))
        for itr_r in range(self.grid_size):
            for itr_c in range(len(self.grid[0])):
                grid_new[itr_c][itr_r] = self.grid[itr_r][itr_c]
        self.grid = grid_new
        return

        return None

    def generate_horizontal(self):
        for idx, word_i in enumerate(self.words):
            letters_i = self.words_letters[idx]
            L = len(letters_i)
            excess = self.grid_size - L
            start_pos = random.choice(list(range(excess)))
            for idy, letter in enumerate(letters_i):
                self.grid[idx][start_pos + idy] = [letter, True]
            pass
        return

        return None

    def place_letter(self, letter, x, y):
        self.grid[x][y][0] = letter
        self.grid[x][y][1] = True
        return

    def is_unsafe(self, letter, x, y):
        # print("%d x %d "%(x,y))
        try:
            if self.grid[x][y][1]:  # already placed
                # it is unsafe if the grid contains different letter
                return self.grid[x][y][0] != letter
        except IndexError as ie:
            return True  # indeed unsafe
        return False

    def place_word(self, word, dir, pos):
        return self.can_place_in_direction(word, dir, pos, doplace=True)

    def can_place_in_direction(self, word, dir, pos, doplace=False):
        L = len(word)
        itr = 1
        XMAX = len(self.words)
        YMAX = self.grid_size
        x, y = pos
        if doplace:
            self.place_letter(word[0], x, y)
        if dir == "|":
            while itr < L:
                y = y + 1
                if not (y < YMAX):
                    return False
                if self.is_unsafe(word[itr], x, y):
                    return False
                if doplace:
                    self.place_letter(word[itr], x, y)
                itr = itr + 1
            return True
        elif dir == "-":
            while itr < L:
                x = x + 1
                if not (x < XMAX):
                    return False
                if self.is_unsafe(word[itr], x, y):
                    return False
                if doplace:
                    self.place_letter(word[itr], x, y)
                itr = itr + 1
            return True
        elif dir == "\\":
            while itr < L:
                y = y + 1
                x = x + 1
                if not (x < XMAX or y < YMAX):
                    return False
                if self.is_unsafe(word[itr], x, y):
                    return False
                if doplace:
                    self.place_letter(word[itr], x, y)
                itr = itr + 1
            return True
        elif dir == "//":
            while itr < L:
                y = y - 1
                x = x - 1
                if x < 0 or y < 0:
                    return False
                if self.is_unsafe(word[itr], x, y):
                    return False
                if doplace:
                    self.place_letter(word[itr], x, y)
                itr = itr + 1
            return True
        return False

    def can_place_word(self, word):
        dir = None
        pos = None
        directions = ["\\", "/", "-", "|"]
        seed_sites = list()
        for idx in range(0, self.grid_size):
            for idy in range(0, self.grid_size):
                # can't use this position as a seed
                if self.grid[idx][idy][1]:
                    continue
                seed_sites.append([idx, idy])

        for itr in range(0, len(seed_sites)):
            pos = random.choice(seed_sites)
            for dir in directions:
                if self.can_place_in_direction(word, dir, pos):
                    return pos, dir
        return None, None

    def generate_randomized_placement(self):
        words_to_place = len(self.words_letters)
        while words_to_place > 0:
            word = self.words_letters[words_to_place - 1]
            directions = ["|", "-", "\\", "/"]
            pos, dir = self.can_place_word(word)
            if not pos:
                print(("Cannot place the word # %d" % words_to_place))
                return False
            self.place_word(word, dir, pos)
            words_to_place -= 1
        return True

    def generate_randomized(self):
        # try shuffling the grid a thousand times
        for i in range(0, 100000):
            self.clear_placements()
            if self.generate_randomized_placement():
                print(("Found solution during attempt %d" % i))
                return
        print("Cannot find solution after several attempts")
        return

    def generate(self):
        # self.generate_horizontal()
        self.generate_randomized()


def gen_grid():
    if len(sys.argv) < 2:
        lang = ["EN", "TA"][1]
        if lang == "EN":
            wordlist = ["food", "water", "shelter", "clothing"]
            fill_letters = list(map(chr, [ord("a") + i for i in range(0, 26)]))
        else:
            wordlist = [
                "உப்பு",
                "நாற்பண்",
                "பராபரம்",
                "கான்யாறு",
                "ஆறு",
                "சன்னியாசி",
                "நெல்லி",
            ]
            fill_letters = (
                    tamil.utf8.uyir_letters
                    + tamil.utf8.mei_letters
                    + tamil.utf8.agaram_letters
            )
        WordGrid.compute(wordlist, fill_letters)
    else:
        data = codecs.open(sys.argv[1], "r", "utf-8").readlines()
        wordlist = [line.split("-")[0].strip() for line in data]
        wordlist = [re.sub("\s+", "", x).strip() for x in wordlist]
        wordlist = [w for w in wordlist if w.find("#") == -1]
        fill_letters = tamil.utf8.get_letters("".join(wordlist))
        if tamil.utf8.all_tamil(wordlist[0]):
            fill_letters += tamil.utf8.uyir_letters + tamil.utf8.agaram_letters
        else:
            wordlist = [word.upper() for word in wordlist]
            fill_letters += [chr(i).upper() for i in range(97, 97 + 26)]
        # from pprint import pprint
        # pprint(wordlist)
        with codecs.open("output.html", "w", "utf-8") as fp:
            WordGrid.compute(wordlist, fill_letters, fp)
    return


if __name__ == "__main__":
    gen_grid()
