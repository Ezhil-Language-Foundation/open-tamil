## -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# Implementation of transliteration algorithm flavors
# and later used in TamilKaruvi (2007) by your's truly.
# 

# BlindIterative Algorithm from TamilKaruvi - less than optimal -
class BlindIterative:
    
    @staticmethod
    def transliterate(table,english_str):
        """ @table - has to be one of Jaffna or Azhagi etc.
            @english_str - """
# 
# -details-
# 
# While text remains:
#   Lookup the English part in anywhere in the string position
#   If present:
#   	  Lookup the Corresponding Tamil Part & Append it to the string.
#   Else: 
#         Continue
# 
        out_str = english_str

        # for consistent results we need to work on sorted keys
        eng_parts = list(table.keys())
        eng_parts.sort()
        eng_parts.reverse()
        
        for eng_part in eng_parts:
            tamil_equiv = table[eng_part]
            parts = out_str.split( eng_part )
            out_str = tamil_equiv.join( parts )
        
        return out_str

# Azhagi has a many-to-one mapping - using a Tamil language model and Baye's conditional probabilities
# to break the tie when two or more Tamil letters have the same English syllable. Currently 
# this predictive transliterator is not available in this package. Also such an algorithm could be
# used with any table.
# 
# challenge use a probabilistic model on Tamil language to score the next letter,
# instead of using the longest/earliest match
# http://www.mazhalaigal.com/tamil/learn/keys.php
class Predictive:
    @staticmethod
    def transliterate(table,english_str):
        raise Exception("Not Implemented!")
        pass

# Sequential Iterative Algorithm modified from TamilKaruvi
class Iterative:
    
    @staticmethod
    def transliterate(table,english_str):
        """ @table - has to be one of Jaffna or Azhagi etc.
            @english_str - """
# 
# -details-
# 
# While text remains:
#   Lookup the First-Matching-Longest-English part
#   If present:
#   	  Lookup the Corresponding Tamil Part & Append it.
#   Else: 
#         Continue
# 
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
                    curr_prefix_lower = curr_prefix[0].lower() + curr_prefix[1:]
                
                ## print curr_prefix
                iters = iters - 1
                if ( curr_prefix in eng_parts ):
                    out_str = out_str + table[curr_prefix]
                    pos = pos + len( curr_prefix)
                    success = True
                    break;
                elif ( curr_prefix_lower in eng_parts ):
                    out_str = out_str + table[curr_prefix_lower]
                    pos = pos + len( curr_prefix_lower )
                    success = True
                    break;
                
            # replacement was a success
            if ( success ):
                continue
            
            # too-bad we didn't find a replacement - just copy char to output
            ## print "concatennate the unmatched =>",english_str[pos],"<="
            if ord(english_str[pos]) < 128:
                rep_char = english_str[pos]
            else:
                rep_char = "?"
            out_str = out_str + rep_char
            
            pos = pos + 1
        
        return out_str
