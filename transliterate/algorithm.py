## -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# Implementation of transliteration algorithm flavors
# and later used in TamilKaruvi (2007) by your's truly.
# 

# Iterative Algorithm from TamilKaruvi - less than optimal -
class Iterative:
    
    @staticmethod
    def transliterate(table,english_str):
        """ @table - has to be one of Jaffna or Azhagi etc.
            @english_str - """
# 
# -details-
# 
# While text remains:
#   Lookup the English part 
#   If present:
#   	  Lookup the Corresponding Tamil Part & Append it.
#	  Free the memory.
#   Else: 
#         Continue
# 
        out_str = english_str

        # for consistent results we need to work on sorted keys
        eng_parts = table.keys()
        eng_parts.sort()
        eng_parts.reverse()
        
        for eng_part in eng_parts:
            tamil_equiv = table[eng_part].decode('utf-8')
            parts = out_str.split( eng_part )
            out_str = tamil_equiv.join( parts )
        
        return out_str
