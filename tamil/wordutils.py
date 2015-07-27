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

def is_palindrome(*args):
    return palindrome(*args)
    
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

def is_anagram(wordA,wordB):
    return sorted(wordA)== sorted(wordB) 

def anagrams_in_dictionary(dictionary):
    if not all ([callable( getattr(dictionary,'isWord',[])),callable( getattr(dictionary,'getAllWordsIterable',[]))]):
        raise Exception("dictionary object has insufficient methods")
    anagrams = dict()
    anagrams_by_len = collections.Counter()
    for in_word in dictionary.getAllWordsIterable():
        word = utf8.get_letters(in_word)
        sword = u''.join(sorted(word))
        try:
            equivs = anagrams[sword]
        except KeyError as ke:
            equivs = list() 
        equivs.append( in_word )
        anagrams[sword] = equivs
        anagrams_by_len[sword] += 1
    items_to_del = filter(lambda a: a[1] == 1,anagrams_by_len.items())
    for itm,counts in items_to_del:
        del anagrams[itm]
        del anagrams_by_len[itm]
    
    itr = 0
    from operator import itemgetter
    rval_anagram_count = sorted(anagrams_by_len.items(),key=itemgetter(1))
    for k,v in rval_anagram_count:
        itr = itr +  1
        print("%d/ items #%d"%(itr,v))
    
    return rval_anagram_count,anagrams

# combinations filtered by dictionary - yields all possible sub-words of a word.
# e.g. 'bat' -> 'tab', 'bat', 'at', etc.
def combinagrams(word,dictionary):
    for word_part in combinations(word):
        for valid_word in anagrams(word_part,dictionary,tamil_permutations):
            yield valid_word
    raise StopIteration

# dummy dictionary interface for use with anagrams
DictionaryWithPredicate = collections.namedtuple('DictionaryWithPredicate',['isWord'])
