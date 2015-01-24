# This Python file uses the following encoding: utf-8
# (C) 2015 Muthiah Annamalai
# This file is part of open-tamil project

from __future__ import division, print_function
import math
import sys
PYTHON3 = sys.version > '3'

if PYTHON3:
        class long: int

def num2tamilstr( number ):
    """ work till l lakh crore - i.e 1e5*1e7 = 1e12. 
        turn number into a numeral, Indian style. """
    
    if not any( filter( lambda T: isinstance( number, T), [int, long]) ) or number < 0:
        raise Exception('num2tamilstr input has to be a positive, and long or integer')
    
    if number > 1e12:
        raise Exception('num2tamilstr input is too large')
    
    units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
    teens = (u'பதினொன்று', u' பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து','பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19    
    tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது','அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
    tens_suffix = (u'இருபத்தி', u'முப்பத்தி', u'நாற்பத்தி', u'ஐம்பத்தி', u'அறுபத்தி', u'எழுபத்தி', u'எண்பத்தி', u'தொன்னூற்றி') # 10+-90+    
    hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு','ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 - 900
    hundreds_suffix = (u'நூற்றி', u'இருநூற்றி', u'முன்னூற்று', u'நாநூற்று', u'ஐநூற்று', u'அறுநூற்று', u'எழுநூற்று', u'எண்ணூற்று',u'தொள்ளாயிரத்து') #100+ - 900+
    
    one_thousand_prefix = u'ஓர்'
    thousands = (u'ஆயிரம்',u'ஆயிரத்தி')
    
    one_prefix = u'ஒரு' 
    lakh = (u'இலட்சம்',u'இலட்சத்தி')
    crore = (u'கோடி',u'கோடியே')
    
    n_one = 1
    n_ten = 10
    n_hundred = 100
    n_thousand = 1000
    n_lakh = 100*n_thousand
    n_crore = 1e2*n_lakh
    
    suffix_base = { n_crore: crore, n_lakh : lakh, n_thousand : thousands}
    
    num_map = {n_crore : [one_prefix,crore[0]],
               n_lakh  : [one_prefix,lakh[0]],
               n_thousand : [one_thousand_prefix, thousands[0]],
               n_hundred : [hundreds[1]], #special
               n_ten : [units[10]],
               n_one : [units[1]]}
    
    all_bases = [n_crore, n_lakh, n_thousand, n_hundred, n_ten,n_one]
    allowed_bases = filter( lambda base: number >= base, all_bases )
    
    for n_base in allowed_bases:
        if number == n_base:
            return u" ".join(num_map[n_base])
        
        quotient_number = int(math.floor( number/n_base ))
        residue_number = int(number % n_base)
        
        if n_base == n_one:
            return units[number]
        elif n_base == n_ten:
            if residue_number == 0:
                return tens[quotient_number-1]
            if number < 20:
                return teens[number-10-1]
            numeral = tens_suffix[quotient_number-2]
        elif n_base == n_hundred:
            numeral = hundreds_suffix[quotient_number-1]
        else:
            numeral = num2tamilstr( quotient_number )
        suffix = u''
        if n_base >= n_thousand:
            suffix = suffix_base[n_base][int(residue_number > 0)]
            if residue_number == 0:
                return numeral + u' ' + suffix
        numeral = numeral + u' ' + suffix
        residue_numeral = num2tamilstr( residue_number )
        return numeral+u' '+residue_numeral
    
    # number has to be zero
    return units[0]
