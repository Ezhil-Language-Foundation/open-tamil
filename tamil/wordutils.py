## This Python file uses the following encoding: utf-8
##
## (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
import copy
import collections
from . import utf8

def combinations(symbols_in):
    if isinstance(symbols_in,list):
        symbols = symbols_in
    else:
        symbols = utf8.get_letters(symbols_in)
    
    uniq_symbols = list(set(symbols))
    N = len(uniq_symbols)
    input_zip = zip(range(0,N),uniq_symbols)
    for count in range(0,2**N):
        bin_rep = bin(count)[2:]
        diff_zeros = N - len(bin_rep)
        bin_rep = '0'*diff_zeros + bin_rep
        filter_symbol = lambda idx: bin_rep[idx] == '1' and uniq_symbols[idx] or u''
        word_combo = u''.join( map(filter_symbol, range(0,N)) )
        yield word_combo
    raise StopIteration

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
    if isinstance(inword,list):
        letters = inword
    else:
        letters = utf8.get_letters(inword)
    for word in permutations( letters ):
        yield word
    raise StopIteration

def palindrome(symbols_in):
    if isinstance(symbols_in,list):
        symbols = symbols_in
    else:
        symbols = utf8.get_letters(symbols_in)
    N = len(symbols)
    for fw in range(0,N):
        rev = N-1 - fw
        if symbols[fw] != symbols[rev]:
            return False
    return True
    
def anagrams(word,dictionary,permutations=tamil_permutations):
    if not callable( getattr(dictionary,'isWord',[]) ):
        raise Exception("@dictionary என்ற உள்ளீட்டில் isWord என்ற செயல்பாட்டு கூறு கிடையாது. இது விதிவிலக்கான நிலை")
    for anagram in permutations(word):
        if dictionary.isWord(anagram):
            yield anagram
    raise StopIteration

# combinations filtered by dictionary - yields all possible sub-words of a word.
# e.g. 'bat' -> 'tab', 'bat', 'at', etc.
def combinagrams(word,dictionary):
    for word_part in combinations(word):
        for valid_word in anagrams(word_part,dictionary,tamil_permutations):
            yield valid_word
    raise StopIteration

# dummy dictionary interface for use with anagrams
DictionaryWithPredicate = collections.namedtuple('DictionaryWithPredicate',['isWord'])
