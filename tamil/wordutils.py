## This Python file uses the following encoding: utf-8
##
## (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
import copy
import collections
from . import utf8

def permutations(symbols):
    if not isinstance(symbols,list):
        raise Exception(u'symbols என்ற உள்ளீடு iterable interface கொண்டதாக வேண்டும். அது சரம் (str) வகையாக இருந்தால் tamil.utf8.get_letters() பயன்பாட்டை முதலில் உபயொகிக்க!')
    
    if len(symbols) == 1:
        yield symbols[0]
    
    for idx in range(0,len(symbols)):
        new_list = copy.copy(symbols)
        del new_list[idx]
        for vars in permutations(new_list):
            yield symbols[idx]  + vars
        del new_list
    raise StopIteration

def tamil_permutations(inword):
    letters = utf8.get_letters(inword)
    for word in permutations( letters ):
        yield word
    raise StopIteration

def anagrams(word,dictionary):
    letters = utf8.get_letters(word)
    for anagram in permutations(letters):
        if dictionary.isWord(anagram):
            yield anagram
    raise StopIteration
