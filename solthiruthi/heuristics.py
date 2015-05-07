## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
## 
from __future__ import print_function
import abc
import sys
from tamil import utf8
from pprint import pprint

PYTHON3 = (sys.version[0] == '3')

class Rule:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def apply( self, word, ctx ):
        """ @word is just that. @ctx is a dict of NwordsPrevious, NwordsNext,
            and a list of surrounding words for as items. 
            e.g. ctx = {'NPrev' : 4, 'Prev' : [w1,w2,w3,w4],'NNext':2,'Next':[w1,w2]}
            return value should be boolean (False if error found) and an optional reason as second argument
        """
        return False,None    

class AdjacentVowels(Rule):
    """ donot allow adjacent vowels in the word.
        ஆஅக்காள் (originally -> அக்காள்) will be flagged
    """
    reason = u"ஒன்றைத்தொடர்ந்துஒன்று உயிரெழுத்துக்கள் வரக்கூடாது. இது பெரும்பாலும் பிழையாக இருக்கும்."
    uyir_letters = set(utf8.uyir_letters)
    
    def apply(self, word, ctx=None):
        """ ignore ctx information right now """
        chars = utf8.get_letters(word)
        flag = True #no error assumed
        reason = None #no reason
        prev_uyir = False
        for char in chars:
            if char in AdjacentVowels.uyir_letters:
                if prev_uyir:
                    flag = False
                    break
                prev_uyir = True
                continue
            prev_uyir = False # continue loop        
        if not flag:
            reason = AdjacentVowels.reason
        return flag,reason
