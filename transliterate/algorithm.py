## -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
#
# Implementation of transliteration algorithm flavors
# and later used in TamilKaruvi (2007) by your's truly.
#
import tamil

def reverse_transliteration_table(table_in):
    """
        transliteration table from Tamil -> English.
    """
    table_out = {}
    keys = table_in.keys()
    keys = sorted(keys)
    keys.reverse()
    for k in keys:
        v = table_in[k]
        table_out[v] = k
    return table_out


class Tamil2English:
    """
        Transliterate Class from Tamil -> English.
    """
    @staticmethod
    def transliterate(table,tamil_str):
        letters = tamil.utf8.get_letters(tamil_str)
        ta2en_map = reverse_transliteration_table(table)
        eng_transliterated = u"".join([ta2en_map.get(tl,tl) for tl in letters])
        return eng_transliterated

class Direct:
    @staticmethod
    def transliterate(table,tamil_str):
        letters = tamil.utf8.get_letters(tamil_str)
        transliterated = u"".join([table.get(tl, tl) for tl in letters])
        #for tl in letters: print(tl,"->",table.get(tl,tl))
        return transliterated

class BlindIterative:
    """
    BlindIterative Algorithm from TamilKaruvi - less than optimal -
     -details-

     While text remains:
       Lookup the English part in anywhere in the string position
       If present:
          Lookup the Corresponding Tamil Part & Append it to the string.
       Else:
             Continue
    """
    @staticmethod
    def transliterate(table,english_str):
        """ @table - has to be one of Jaffna or Azhagi etc.
            @english_str - """
        out_str = english_str

        # for consistent results we need to work on sorted keys
        eng_parts = list(table.keys())
        eng_parts.sort()
        eng_parts.reverse()

        for eng_part in eng_parts:
            tamil_equiv = table.get(eng_part,eng_part)
            parts = out_str.split( eng_part )
            out_str = tamil_equiv.join( parts )

        return out_str

# Basically english_str can be transliterated to many possible Tamil words
# First condition is all english letters need to be used.
# Secondly all generated Tamil words from the englist_str will have to be
# scored by their bigram score.
# Return the highest scoring string
class Greedy:
    def __init__(self,table,lexicon=None):
        self.table = table
        self.options = []
        self.scores = [0.0]
        self.lexicon = lexicon
        self.full_search = False

    def score(self):
        max_idx = 0
        for idx,op in enumerate(self.options):
            prev = ''
            n_ending_uyir = 0
            n_consequetive_mei = 0
            for letter in tamil.utf8.get_letters_iterable(op):
                if (letter in tamil.utf8.mei_letters) and (prev in tamil.utf8.mei_letters ):
                    n_consequetive_mei += 1
                prev = letter
            if prev in tamil.utf8.uyir_letters:
                n_ending_uyir = 1
            w_score = len(op) - 2*n_consequetive_mei - 2*n_ending_uyir
            if w_score > self.scores[max_idx]:
                max_idx = idx
            self.scores.append( w_score )
        return max_idx

    #check if level=0 and letter is mei, then return False
    #all other cases return True
    def skip_mei(self,level,letter):
        if level > 0:
            return True
        return not( letter in tamil.utf8.mei_letters)

    def generate(self,input_str,partial='',level=0):
        if len(input_str) == 0:
            self.options.append(partial)
            return
        if level >= 1 and len(partial) == 0:
            return
        if isinstance(input_str,list):
            english_str = input_str
        else:
            english_str = tamil.utf8.get_letters(input_str)
        for itr,s in enumerate(english_str):
            curr = s
            if itr < len(english_str)-1:
                nxt = english_str[itr+1]
            else:
                nxt = ''

            w1 = self.table.get(curr,None)
            if w1: self.skip_mei(level,w1) and self.generate(english_str[itr+1:],partial+w1,level+1)

            w2 = self.table.get(curr.upper()+nxt,None)
            if w2: self.skip_mei(level,w2) and self.generate(english_str[itr+2:],partial+w2,level+1)

            #w2 = self.table.get(prev+curr,None)
            #if w2: self.generate(english_str[itr+1:],partial+w2)
            w3 = self.table.get(curr+nxt,None)
            if w3: self.skip_mei(level,w3) and self.generate(english_str[itr+2:],partial+w3,level+1)

            #w4 = self.table.get(curr.upper()+nxt.upper(),None)
            #if w4: self.skip_mei(level,w4) and self.generate(english_str[itr+2:],partial+w4,level+1)

            #w4 = self.table.get(prev+curr+nxt,None)
            #if w4: self.generate(english_str[itr+2:],partial+w4)
            prev = curr
            if ( not self.full_search ):
                break

        return

    def pick_dictionary_words(self):
        if not hasattr(self.lexicon,'isWord'):
            return
        self.options = list(filter(self.lexicon.isWord,self.options))

    def run(self,english_str,full_search=False):
        self.full_search = full_search
        self.generate(english_str)
        self.pick_dictionary_words()
        idx = self.score()
        if len(self.options) < 1:
            return english_str
        best = self.options[idx]
        self.options = set(self.options)
        return best

    @staticmethod
    def transliterate(table,english_str,lexicon=None,full_search=False):
        g = Greedy(table,lexicon)
        return g.run(english_str,full_search=full_search),g

# Azhagi has a many-to-one mapping - using a Tamil language model and Baye's conditional probabilities
# to break the tie when two or more Tamil letters have the same English syllable. Currently
# this predictive transliterator is not available in this package. Also such an algorithm could be
# used with any table.
#
# challenge use a probabilistic model on Tamil language to score the next letter,
# instead of using the longest/earliest match
# http://www.mazhalaigal.com/tamil/learn/keys.php
class Predictive:
    """
    This is work in progress. Currently disabled.
    """
    @staticmethod
    def transliterate(table,english_str):
        raise Exception("Not Implemented!")
        pass

class Iterative:
    """
    Sequential Iterative Algorithm modified from TamilKaruvi
     -details-
     While text remains:
       Lookup the First-Matching-Longest-English part
       If present:
          Lookup the Corresponding Tamil Part & Append it.
       Else:
          Continue
    """
    @staticmethod
    def transliterate(table,english_str):
        """ @table - has to be one of Jaffna or Azhagi etc.
            @english_str - """
        out_str = english_str

        # for consistent results we need to work on sorted keys
        eng_parts = list(table.keys())
        eng_parts.sort()
        eng_parts.reverse()

        MAX_ITERS_BEFORE_YOU_DROP_LETTER = max(list(map(len,eng_parts)))

        remaining = len(english_str)
        out_str = ''
        pos = 0
        while pos < remaining:

            # try to find the longest prefix in input from L->R in greedy fashion
            iters = MAX_ITERS_BEFORE_YOU_DROP_LETTER
            success = False

            while iters >= 0:
                curr_prefix = english_str[pos:min(pos+iters-1,remaining)]
                curr_prefix_lower = None
                if ( len(curr_prefix) >= 2 ):
                    if isinstance(curr_prefix,list):
                        curr_prefix_lower = curr_prefix[0].lower() + "".join(curr_prefix[1:])
                    else:
                        curr_prefix_lower = curr_prefix[0].lower() + curr_prefix[1:]

                ## print curr_prefix
                iters = iters - 1
                if ( curr_prefix in eng_parts ):
                    out_str = out_str + table[curr_prefix]
                    pos = pos + len( curr_prefix)
                    success = True
                    break
                elif ( curr_prefix_lower in eng_parts ):
                    out_str = out_str + table[curr_prefix_lower]
                    pos = pos + len( curr_prefix_lower )
                    success = True
                    break

            # replacement was a success
            if ( success ):
                continue

            # copy input to output if transliteration fails or Tamil inputs found
            if len(english_str[pos]) == 1 and ord(english_str[pos]) < 128:
                rep_char = english_str[pos]
            else:
                rep_char = english_str[pos] #copy-string to output - maybe Tamil letter also.
            out_str = out_str + rep_char

            pos = pos + 1

        return out_str
