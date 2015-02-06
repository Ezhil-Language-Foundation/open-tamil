# This Python file uses the following encoding: utf-8
# (C) 2015 Muthiah Annamalai
# This file is part of open-tamil project

import sys
PYTHON3 = sys.version > '3'

if PYTHON3:
    class long(int):
        pass

def num2tamilstr( number ):
    """ work till l lakh crore - i.e 1e5*1e7 = 1e12. 
        turn number into a numeral, Indian style. """
    
    if not any( filter( lambda T: isinstance( number, T), [int, long]) ) or number < 0:
        raise Exception('num2tamilstr input has to be a positive, and long or integer')
    if number > long(1e12):
        raise Exception('num2tamilstr input is too large')
    
    units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
    teens = (u'பதினொன்று', u' பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து',u'பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19    
    tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது',u'அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
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
    n_crore = long(100*n_lakh)
    
    suffix_base = { n_crore: crore, n_lakh : lakh, n_thousand : thousands}
    
    num_map = {n_crore : [one_prefix,crore[0]],
               n_lakh  : [one_prefix,lakh[0]],
               n_thousand : [one_thousand_prefix, thousands[0]],
               n_hundred : [hundreds[0]], #special
               n_ten : [units[10]],
               n_one : [units[1]]}
    
    all_bases = [n_crore, n_lakh, n_thousand, n_hundred, n_ten,n_one]
    allowed_bases = filter( lambda base: number >= base, all_bases )
    
    for n_base in allowed_bases:
        if number == n_base:
            return u" ".join(num_map[n_base])
        quotient_number = long( number/n_base )
        residue_number = number - n_base*quotient_number
        
        if n_base == n_one:
            return units[number]
        elif n_base == n_ten:
            if residue_number == 0:
                return tens[quotient_number-1]
            if number < 20:
                return teens[number-10-1]
            numeral = tens_suffix[quotient_number-2]
        elif n_base == n_hundred:
            if residue_number == 0:
                return hundreds[quotient_number-1]
            numeral = hundreds_suffix[quotient_number-1]
        else:
            if ( quotient_number == 1 ):
                if n_base == n_thousand:
                    numeral = one_thousand_prefix
                else:
                    numeral = one_prefix
            else:
                numeral = num2tamilstr( quotient_number )
        suffix = u''
        if n_base >= n_thousand:
            suffix = suffix_base[n_base][long(residue_number > 0)]
            if residue_number == 0:
                return numeral + u' ' + suffix
            numeral = numeral + u' ' + suffix
        residue_numeral = num2tamilstr( residue_number )
        return numeral+u' '+residue_numeral
    
    # number has to be zero
    return units[0]

def num2tamilstr_american( number ):
    """ work till 1000 trillion  - 1 - i.e  = 1e12*1e3 - 1. 
        turn number into a numeral, Indian style. """
    
    if not any( filter( lambda T: isinstance( number, T), [int, long]) ) or number < 0:
        raise Exception('num2tamilstr_american input has to be a positive, and long or integer')
    
    if number >= long(1e15):
        raise Exception('num2tamilstr input is too large')
    
    units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
    teens = (u'பதினொன்று', u' பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து',u'பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19    
    tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது',u'அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
    tens_suffix = (u'இருபத்தி', u'முப்பத்தி', u'நாற்பத்தி', u'ஐம்பத்தி', u'அறுபத்தி', u'எழுபத்தி', u'எண்பத்தி', u'தொன்னூற்றி') # 10+-90+    
    hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு','ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 - 900
    hundreds_suffix = (u'நூற்றி', u'இருநூற்றி', u'முன்னூற்று', u'நாநூற்று', u'ஐநூற்று', u'அறுநூற்று', u'எழுநூற்று', u'எண்ணூற்று',u'தொள்ளாயிரத்து') #100+ - 900+
    
    one_thousand_prefix = u'ஓர்'
    thousands = (u'ஆயிரம்',u'ஆயிரத்தி')
    
    one_prefix = u'ஒரு'
    mil = u'மில்லியன்'
    million = (mil,mil)
    
    bil = u'பில்லியன்'
    billion = (bil,bil)
    
    tril = u'டிரில்லியன்'
    trillion = (tril,tril)
    
    n_one = 1
    n_ten = 10
    n_hundred = 100
    n_thousand = 1000
    n_million = 1000*n_thousand
    n_billion = long(1000*n_million)
    n_trillion = long(1000*n_billion)
    
    suffix_base = { n_trillion: trillion, 
                    n_billion : billion, 
                    n_million : million, 
                    n_thousand : thousands}
    
    num_map = {n_trillion : [one_prefix,trillion[0]],
               n_billion : [one_prefix,billion[0]],
               n_million  : [one_prefix,million[0]],
               n_thousand : [one_thousand_prefix, thousands[0]],
               n_hundred : [hundreds[0]], #special
               n_ten : [units[10]],
               n_one : [units[1]]}
    
    all_bases = [n_trillion,n_billion, n_million, n_thousand, n_hundred, n_ten,n_one]
    allowed_bases = filter( lambda base: number >= base, all_bases )
    
    for n_base in allowed_bases:
        if number == n_base:
            return u" ".join(num_map[n_base])
        quotient_number = long( number/n_base )
        residue_number = number - n_base*quotient_number
        
        if n_base == n_one:
            return units[number]
        elif n_base == n_ten:
            if residue_number == 0:
                return tens[quotient_number-1]
            if number < 20:
                return teens[number-10-1]
            numeral = tens_suffix[quotient_number-2]
        elif n_base == n_hundred:
            if residue_number == 0:
                return hundreds[quotient_number-1]
            numeral = hundreds_suffix[quotient_number-1]
        else:
            if ( quotient_number == 1 ):
                if n_base == n_thousand:
                    numeral = one_thousand_prefix
                else:
                    numeral = one_prefix
            else:
                numeral = num2tamilstr( quotient_number )
        suffix = u''
        if n_base >= n_thousand:
            suffix = suffix_base[n_base][long(residue_number > 0)]
            if residue_number == 0:
                return numeral + u' ' + suffix
            numeral = numeral + u' ' + suffix
        residue_numeral = num2tamilstr_american( residue_number )
        return numeral+u' '+residue_numeral

    # number has to be zero
    return units[0]
