# This Python file uses the following encoding: utf-8
# (C) 2015-2018 Muthiah Annamalai
# This file is part of open-tamil project

import sys
import math
PYTHON3 = sys.version > '3'

if PYTHON3:
    unicode = str
    class long(int):
        pass

def num2tamilstr( *args ):
    """ work till one lakh crore - i.e 1e5*1e7 = 1e12.
        turn number into a numeral, Indian style. Fractions upto 1e-30"""
    number = args[0]
    if len(args) < 2:
        filenames = []
    else:
        filenames = args[1]
    if len(args) ==3:
        tensSpecial = args[2]
    else:
        tensSpecial='BASIC'
    if not any( filter( lambda T: isinstance( number, T), [str,unicode,int, long, float]) ) or isinstance(number,complex):
        raise Exception('num2tamilstr input has to be a long or integer or float')
    if float(number) > long(1e12):
        raise Exception('num2tamilstr input is too large')
    if float(number) < 0:
        return u"- "+num2tamilstr( -number )

    units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
    units_suffix = (u'பூஜ்ஜியம்', u'தொன்று', u'திரண்டு', u'மூன்று', u'நான்கு', u'தைந்து', u'தாறு', u'தேழு', u'தெட்டு', u'தொன்பது', u'பத்து') # 0-10
    units_suffix_nine = (u'பூஜ்ஜியம்', u'றொன்று', u'றிரண்டு', u'மூன்று', u'நான்கு', u'றைந்து', u'றாறு', u'றேழு', u'றெட்டு', u'றொன்பது', u'பத்து') # 0-10
    tween = [1.0,2.0,5.0,6.0,7.0,8.0,9.0]
    teens = (u'பதினொன்று', u'பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து',u'பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19
    tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது',u'அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
    tens_full_prefix = (u'இருபத்து', u'முப்பத்து', u'நாற்பத்து', u'ஐம்பத்து', u'அறுபத்து', u'எழுபத்து', u'எண்பத்து', u'தொன்னூற்று') # 10+-90+
    tens_prefix = (u'இருபத்', u'முப்பத்', u'நாற்பத்', u'ஐம்பத்', u'அறுபத்', u'எழுபத்', u'எண்பத்', u'தொன்னூற்') # 10+-90+
    hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு',u'ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 - 900
    hundreds_suffix = (u'நூற்றி', u'இருநூற்று', u'முன்னூற்று', u'நாநூற்று', u'ஐநூற்று', u'அறுநூற்று', u'எழுநூற்று', u'எண்ணூற்று',u'தொள்ளாயிரத்து') #100+ - 900+

    one_thousand_prefix = u'ஓர்'
    thousands = (u'ஆயிரம்',u'ஆயிரத்து')

    one_prefix = u'ஒரு'
    lakh = (u'இலட்சம்',u'இலட்சத்து')
    crore = (u'கோடி',u'கோடியே')

    pulli = u'புள்ளி'
    n_one = 1.0
    n_ten = 10.0
    n_hundred = 100.0
    n_thousand = 1000.0
    n_lakh = 100.0*n_thousand
    n_crore = (100.0*n_lakh)
    # handle fractional parts
    if float(number) > 0.0 and float(number) < 1.0:
        rval = []
        rval.append(pulli)
        filenames.append( 'pulli' )
        number_str = str(number).replace('0.','')
        for digit in number_str:
            filenames.append( "units_%d"%int(digit))
            rval.append( units[int(digit)] )
        return u' '.join(rval)

    if isinstance(number,str) or isinstance(number,unicode):
        result = u""
        number = number.strip()
        assert(len(args) == 1)
        assert(len(number) > 0)
        is_negative = number[0] == "-"
        if  is_negative:
            number = number[1:]
        frac_part = u""
        if number.find(".") >= 0:
            rat_part,frac_part = number.split(".")
            frac_part = num2tamilstr(u"0."+frac_part)
        else:
            rat_part = number
        if len(rat_part) > 0:
            result = num2tamilstr(float(rat_part))
        result = result +u" "+ frac_part
        return is_negative and "-" + result.strip() or result.strip()

    suffix_base = { n_crore: crore, n_lakh : lakh, n_thousand : thousands}
    suffix_file_map = {n_crore: "crore", n_lakh : "lakh", n_thousand : "thousands"}

    file_map = {n_crore :["one_prefix","crore_0"],
                n_lakh : ["one_prefix","lakh_0"],
                n_thousand :  ["one_thousand_prefix", "thousands_0"],
               n_hundred : ["hundreds_0"], #special
               n_ten : ["units_10"],
               n_one : ["units_1"]}

    num_map = {n_crore : [one_prefix,crore[0]],
               n_lakh  : [one_prefix,lakh[0]],
               n_thousand : [one_thousand_prefix, thousands[0]],
               n_hundred : [hundreds[0]], #special
               n_ten : [units[10]],
               n_one : [units[1]]}

    all_bases = [n_crore, n_lakh, n_thousand, n_hundred, n_ten,n_one]
    allowed_bases = list(filter( lambda base: number >= base, all_bases ))
    if len(allowed_bases) >= 1:
        n_base = allowed_bases[0]
        if number == n_base:
            if tensSpecial=='BASIC':
                filenames.extend(file_map[n_base])
                return u" ".join(num_map[n_base])
            elif tensSpecial=='NINES':
                filenames.extend(file_map[n_base])
                return units_suffix_nine[long(number%10)]
            else:
                filenames.extend(file_map[n_base])
                return units_suffix[long(number%10)]
        quotient_number = long( number/n_base )
        residue_number = number - n_base*quotient_number
        #print number, n_base, quotient_number, residue_number, tensSpecial
        if n_base == n_one:
            if isinstance(number,float):
                int_part = long(number%10)
                frac = number - float(int_part)
                filenames.append("units_%d"%int_part)
                if abs(frac) > 1e-30:
                    if tensSpecial=='BASIC':
                        return units[int_part]+u' ' + num2tamilstr(frac,filenames)
                    elif tensSpecial=='NINES':
                        return units_suffix_nine[int_part]+u' ' + num2tamilstr(frac,filenames)
                    else:
                        return units_suffix[int_part]+u' ' + num2tamilstr(frac,filenames)

                else:
                    if tensSpecial=='BASIC':
                        return units[int_part]
                    elif tensSpecial=='NINES':
                        return units_suffix_nine[int_part]
                    else:
                        return units_suffix[int_part]
            else:
                if tensSpecial=='BASIC':
                    filenames.append("units_%d"%number)
                    return units[number]
                elif tensSpecial=='NINES':
                    filenames.append("units_%d"%number)
                    return units_suffix_nine[number]
                else:
                    filenames.append("units_%d"%number)
                    return units_suffix[number]

        elif n_base == n_ten:
            if residue_number < 1.0:
                filenames.append("tens_%d"%(quotient_number-1))
                if residue_number == 0.0:
                    return tens[quotient_number-1]
                #else: //seems not reachable.
                #    numeral = tens[quotient_number-1]
            elif number < 20:
                filenames.append("teens_%d"%(number-10))
                residue_number = math.fmod(number,1)
                teen_number = int(math.floor(number - 10))
                if residue_number > 1e-30:
                    return teens[teen_number-1] +u' ' + num2tamilstr(residue_number,filenames)
                else:
                    return teens[teen_number-1]+u' '
            if residue_number < 1.0:
                filenames.append( "tens_%d"%(quotient_number-1) )
                numeral = tens[quotient_number-1]+u' '
            else:
                if residue_number in tween:
                    filenames.append( "tens_prefix_%d"%(quotient_number-2) )
                    numeral = tens_prefix[quotient_number-2]
                    tensSpecial='SPECIAL'
                    if (quotient_number==9):
                        tensSpecial = 'NINES'
                else:
                    filenames.append( "tens_prefix_%d"%(quotient_number-2) )
                    numeral = tens_full_prefix[quotient_number-2]+u' '
        elif n_base == n_hundred:
            if residue_number == 0:
                filenames.append("hundreds_%d"%(quotient_number-1))
                return hundreds[quotient_number-1]+u' '
            if residue_number < 1.0:
                filenames.append( "hundreds_%d"%(quotient_number-1) )
                numeral = hundreds[quotient_number-1]+u' '
            else:
                filenames.append("hundreds_suffix_%d"%(quotient_number-1))
                numeral = hundreds_suffix[quotient_number-1]+u' '
        else:
            if ( quotient_number == 1 ):
                if n_base == n_thousand:
                    filenames.append("one_thousand_prefix")
                    numeral = one_thousand_prefix
                else:
                    filenames.append("one_prefix")
                    numeral = one_prefix
            else:
                numeral = num2tamilstr( quotient_number, filenames )
        if n_base >= n_thousand:
            suffix = suffix_base[n_base][long(residue_number >= 1)]
            suffix_filename = "%s_%d"%(suffix_file_map[n_base],long(residue_number >= 1))
            if residue_number == 0:
                filenames.append(suffix_filename)
                return numeral + u' ' + suffix+u' '
            filenames.append(suffix_filename)
            numeral = numeral + u' ' + suffix+u' '
        residue_numeral = num2tamilstr( residue_number, filenames, tensSpecial)
        #return numeral+u' '+residue_numeral
        return numeral+residue_numeral
    # number has to be zero
    filenames.append("units_0")
    return units[0]

def num2tamilstr_american( *args ):
    number = args[0]
    """ work till 1000 trillion  - 1 - i.e  = 1e12*1e3 - 1.
        turn number into a numeral, American style. Fractions upto 1e-30. """

    if not any( filter( lambda T: isinstance( number, T), [int, str, unicode, long, float]) ) or isinstance(number,complex):
        raise Exception('num2tamilstr_american input has to be long or integer')
    if float(number) >= long(1e15):
        raise Exception('num2tamilstr input is too large')
    if float(number) < 0:
        return u"- "+num2tamilstr_american( -float(number) )

    units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
    hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு',u'ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 - 900

    one_thousand_prefix = u'ஓர்'
    thousands = (u'ஆயிரம்',u'ஆயிரத்து')

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
    allowed_bases = list(filter( lambda base: float(number) >= base, all_bases ))

    # handle fractional parts
    if float(number) > 0.0 and float(number) <= 1000.0:
        return num2tamilstr(number)

    if isinstance(number,str) or isinstance(number,unicode):
        result = u""
        number = number.strip()
        assert(len(args) == 1)
        assert(len(number) > 0)
        is_negative = number[0] == "-"
        if  is_negative:
            number = number[1:]
        frac_part = u""
        if number.find(".") >= 0:
            rat_part,frac_part = number.split(".")
            frac_part = num2tamilstr_american(u"0."+frac_part)
        else:
            rat_part = number
        if len(rat_part) > 0:
            result = num2tamilstr_american(float(rat_part))
        result = result +u" "+ frac_part
        return result.strip()

    if len(allowed_bases) >= 1:
        n_base = allowed_bases[0]
        if number == n_base:
            return u" ".join(num_map[n_base])
        quotient_number = long( number/n_base )
        residue_number = number - n_base*quotient_number

        if n_base < n_thousand:
            raise Exception("This can never happen")
        else:
            if ( quotient_number == 1 ):
                if n_base == n_thousand:
                    numeral = one_thousand_prefix+u' '
                else:
                    numeral = one_prefix+u' '
            else:
                numeral = num2tamilstr( quotient_number )
        if n_base >= n_thousand:
            suffix = suffix_base[n_base][long(residue_number >= 1)]
            if residue_number == 0:
                return numeral + u' ' + suffix
            numeral = numeral + u' ' + suffix
        residue_numeral = num2tamilstr_american( residue_number )
        return numeral+u' '+residue_numeral

    # number has to be zero
    return units[0]
