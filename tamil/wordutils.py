## This Python file uses the following encoding: utf-8
##
## (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
import copy
from . import utf8

def permutations(symbols):
    if len(symbols) == 1:
        yield symbols[0]
    
    for idx in range(0,len(symbols)):
        new_list = copy.copy(symbols)
        del new_list[idx]
        for vars in permutations(new_list):
            yield symbols[idx]  + vars
        del new_list

def anagrams(word,dictionary):
    letters = utf8.get_letters(word)
    for anagram in permutations(letters):
        if dictionary.isWord(anagram):
            yield anagram
