## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
## This module is part of solthiruthi project under open-tamil umbrella.
## This code maybe used/distributed under MIT LICENSE.

from __future__ import print_function
import abc
import codecs
import copy

from tamil import utf8

# Suffix removal algorithm
class RemoveSuffix(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        self.possible_suffixes = None
        self.replace_suffixes = {} #valid dictionary
        self.reversed_suffixes = []
    
    @abc.abstractmethod
    def setSuffixes(self):
        pass
    
    def prepareSuffixes(self):
        assert self.possible_suffixes
        # reverse the words in each letter.
        for word in self.possible_suffixes:
            self.reversed_suffixes.append( utf8.reverse_word(word) )
        return
    
    def removeSuffix(self,word):
        removed = False
        if not self.possible_suffixes:
            # init once
            self.setSuffixes()
            self.prepareSuffixes()
        word_lett = utf8.get_letters(word)
        rword_lett = copy.copy(word_lett)
        rword_lett.reverse()
        #print('rev word ->',rword_lett)
        rword = u"".join(rword_lett)
        longest_match = ""
        for itr in range(len(self.reversed_suffixes)):
            suffix = self.reversed_suffixes[itr]
            #print(itr,utf8.get_letters(suffix))
            if rword.startswith(suffix):
                if len(longest_match) <= len(suffix):
                    longest_match = suffix
                    #print('L-match-->',utf8.get_letters(longest_match))
            continue
        if len(longest_match) > 0:
            removed = True
            sfx = []
            for itr in range(len(utf8.get_letters(longest_match))):
                sfx.append( word_lett.pop() )
            word = u"".join(word_lett)
            sfx.reverse()
            sfx= u"".join(sfx)
            # rule to replace suffix
            alt_suffix = self.replace_suffixes.get(sfx,None)
            if alt_suffix:
                word = word + alt_suffix
        return word,removed

class RemoveCaseSuffix(RemoveSuffix):        
    def __init__(self):
        super(RemoveCaseSuffix,self).__init__()
    def setSuffixes(self):
        self.possible_suffixes=[u"உக்கு",u"க்கு",u"ளை",u"கள்"]

class RemovePluralSuffix(RemoveSuffix):        
    def __init__(self):
        super(RemovePluralSuffix,self).__init__()
    def setSuffixes(self):
        self.replace_suffixes = {u"ற்கள்":u"ல்",u"கள்":u"",u"ல்":u"", u"ட்கள்": u"ள்", u"ங்கள்":u"ம்"}
        self.possible_suffixes=list(self.replace_suffixes.keys())
        
def xkcd():
    obj = RemovePluralSuffix()
    expected = [u"பதிவி",u"கட்டளை",u"அவர்"]
    words_list = [u"பதிவில்",u"கட்டளைகள்",u"அவர்கள்"]
    for w,x in zip(words_list,expected):
        rval = obj.removeSuffix(w)
        assert(rval[1])
        print(utf8.get_letters(w),'->',rval[1])
        assert(rval[0] == x)
    return

if __name__ == "__main__":
    xkcd()
