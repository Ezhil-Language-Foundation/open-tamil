## This Python file uses the following encoding: utf-8
##
## (C) 2007, 2008, 2013 Muthiah Annamalai <gnumuthu@user.sf.net>
## Licensed under GPL Version 3
## Error Correction:msathia 2013<msathia@gmail.com>

## constants
TA_ACCENT_LEN = 13 #12 + 1
TA_AYUDHA_LEN = 1
TA_UYIR_LEN = 12
TA_MEI_LEN = 18
TA_AGARAM_LEN = 18
TA_SANSKRIT_LEN = 4
TA_UYIRMEI_LEN = 216 # 18*12

# List of letters you can use
uyir_letters = [u"அ",u"ஆ",u"இ", 
	u"ஈ",u"உ",u"ஊ",u"எ",u"ஏ",u"ஐ",u"ஒ",u"ஓ",u"ஔ"]

ayudha_letter = u"ஃ"

mei_letters = [u"க்",u"ச்",u"ட்",u"த்",u"ப்",u"ற்",
	       u"ஞ்",u"ங்",u"ண்",u"ந்",u"ம்",u"ன்",
	       u"ய்",u"ர்",u"ல்",u"வ்",u"ழ்",u"ள்" ]

accent_symbols = [u"",u"ா",u"ி",u"ீ",u"ு",u"ூ",
		  u"ெ",u"ே",u"ை",u"ொ",u"ோ",u"ௌ",u"ஃ"]

agaram_letters = [u"க",u"ச",u"ட",u"த",u"ப",u"ற",
		  u"ஞ",u"ங",u"ண",u"ந",u"ம",u"ன",
		  u"ய",u"ர",u"ல",u"வ",u"ழ",u"ள"]

sanskrit_letters = [u"ஜ",u"ஷ", u"ஸ",u"ஹ"]
sanskrit_mei_letters =[u"ஜ்",u"ஷ்", u"ஸ்",u"ஹ்"]

uyirmei_letters = [
 "க"  ,"கா"  ,"கி"  ,"கீ"  ,"கு"  ,"கூ"  ,"கெ"  ,"கே"  ,"கை"  ,"கொ"  ,"கோ"  ,"கௌ"  ,
"ச"  ,"சா"  ,"சி"  ,"சீ"  ,"சு"  ,"சூ"  ,"செ"  ,"சே"  ,"சை"  ,"சொ"  ,"சோ"  ,"சௌ" , 
 "ட"  ,"டா"  ,"டி"  ,"டீ"  ,"டு"  ,"டூ"  ,"டெ"  ,"டே"  ,"டை"  ,"டொ"  ,"டோ"  ,"டௌ", 
"த"  ,"தா"  ,"தி"  ,"தீ"  ,"து"  ,"தூ"  ,"தெ"  ,"தே"  ,"தை"  ,"தொ"  ,"தோ"  ,"தௌ", 
"ப"  ,"பா"  ,"பி"  ,"பீ"  ,"பு"  ,"பூ"  ,"பெ"  ,"பே"  ,"பை"  ,"பொ"  ,"போ"  ,"பௌ" , 
"ற"  ,"றா"  ,"றி"  ,"றீ"  ,"று"  ,"றூ"  ,"றெ"  ,"றே"  ,"றை"  ,"றொ"  ,"றோ"  ,"றௌ", 
"ஞ"  ,"ஞா"  ,"ஞி"  ,"ஞீ"  ,"ஞு"  ,"ஞூ"  ,"ஞெ"  ,"ஞே"  ,"ஞை"  ,"ஞொ"  ,"ஞோ"  ,"ஞௌ"  ,
"ங"  ,"ஙா"  ,"ஙி"  ,"ஙீ"  ,"ஙு"  ,"ஙூ"  ,"ஙெ"  ,"ஙே"  ,"ஙை"  ,"ஙொ"  ,"ஙோ"  ,"ஙௌ"  ,
"ண"  ,"ணா"  ,"ணி"  ,"ணீ"  ,"ணு"  ,"ணூ"  ,"ணெ"  ,"ணே"  ,"ணை"  ,"ணொ"  ,"ணோ"  ,"ணௌ"  ,
"ந"  ,"நா"  ,"நி"  ,"நீ"  ,"நு"  ,"நூ"  ,"நெ"  ,"நே"  ,"நை"  ,"நொ"  ,"நோ"  ,"நௌ"  ,
"ம"  ,"மா"  ,"மி"  ,"மீ"  ,"மு"  ,"மூ"  ,"மெ"  ,"மே"  ,"மை"  ,"மொ"  ,"மோ"  ,"மௌ" , 
"ன"  ,"னா"  ,"னி"  ,"னீ"  ,"னு"  ,"னூ"  ,"னெ"  ,"னே"  ,"னை"  ,"னொ"  ,"னோ"  ,"னௌ", 
"ய"  ,"யா"  ,"யி"  ,"யீ"  ,"யு"  ,"யூ"  ,"யெ"  ,"யே"  ,"யை"  ,"யொ"  ,"யோ"  ,"யௌ", 
"ர"  ,"ரா"  ,"ரி"  ,"ரீ"  ,"ரு"  ,"ரூ"  ,"ரெ"  ,"ரே"  ,"ரை"  ,"ரொ"  ,"ரோ"  ,"ரௌ", 
"ல"  ,"லா"  ,"லி"  ,"லீ"  ,"லு"  ,"லூ"  ,"லெ"  ,"லே"  ,"லை"  ,"லொ"  ,"லோ"  ,"லௌ" , 
"வ"  ,"வா"  ,"வி"  ,"வீ"  ,"வு"  ,"வூ"  ,"வெ"  ,"வே"  ,"வை"  ,"வொ"  ,"வோ"  ,"வௌ" , 
"ழ"  ,"ழா"  ,"ழி"  ,"ழீ"  ,"ழு"  ,"ழூ"  ,"ழெ"  ,"ழே"  ,"ழை"  ,"ழொ"  ,"ழோ"  ,"ழௌ" , 
"ள"  ,"ளா"  ,"ளி"  ,"ளீ"  ,"ளு"  ,"ளூ"  ,"ளெ"  ,"ளே"  ,"ளை"  ,"ளொ"  ,"ளோ"  ,"ளௌ" ]

## total tamil letters in use, including sanskrit letters
tamil_letters = [
	
## /* Uyir */
 "அ","ஆ","இ", "ஈ","உ","ஊ","எ","ஏ","ஐ","ஒ","ஓ","ஔ",

##/* Ayuda Ezhuthu */
"ஃ",
	
## /* Mei */	
 "க்","ச்","ட்","த்","ப்","ற்","ஞ்","ங்","ண்","ந்","ம்","ன்","ய்","ர்","ல்","வ்","ழ்","ள்",

## /* Agaram */
"க","ச","ட","த","ப","ற","ஞ","ங","ண","ந","ம","ன","ய","ர","ல","வ","ழ","ள",
	
## /* Sanskrit (Vada Mozhi) */
"ஜ","ஷ", "ஸ","ஹ",

##/* Sanskrit (Mei) */
"ஜ்","ஷ்", "ஸ்","ஹ்",
	
## /* Uyir Mei */
 "க"  ,"கா"  ,"கி"  ,"கீ"  ,"கு"  ,"கூ"  ,"கெ"  ,"கே"  ,"கை"  ,"கொ"  ,"கோ"  ,"கௌ" 
 ,"ச"  ,"சா"  ,"சி"  ,"சீ"  ,"சு"  ,"சூ"  ,"செ"  ,"சே"  ,"சை"  ,"சொ"  ,"சோ"  ,"சௌ" 
 ,"ட"  ,"டா"  ,"டி"  ,"டீ"  ,"டு"  ,"டூ"  ,"டெ"  ,"டே"  ,"டை"  ,"டொ"  ,"டோ"  ,"டௌ" 
 ,"த"  ,"தா"  ,"தி"  ,"தீ"  ,"து"  ,"தூ"  ,"தெ"  ,"தே"  ,"தை"  ,"தொ"  ,"தோ"  ,"தௌ" 
 ,"ப"  ,"பா"  ,"பி"  ,"பீ"  ,"பு"  ,"பூ"  ,"பெ"  ,"பே"  ,"பை"  ,"பொ"  ,"போ"  ,"பௌ" 
 ,"ற"  ,"றா"  ,"றி"  ,"றீ"  ,"று"  ,"றூ"  ,"றெ"  ,"றே"  ,"றை"  ,"றொ"  ,"றோ"  ,"றௌ" 
 ,"ஞ"  ,"ஞா"  ,"ஞி"  ,"ஞீ"  ,"ஞு"  ,"ஞூ"  ,"ஞெ"  ,"ஞே"  ,"ஞை"  ,"ஞொ"  ,"ஞோ"  ,"ஞௌ" 
 ,"ங"  ,"ஙா"  ,"ஙி"  ,"ஙீ"  ,"ஙு"  ,"ஙூ"  ,"ஙெ"  ,"ஙே"  ,"ஙை"  ,"ஙொ"  ,"ஙோ"  ,"ஙௌ" 
 ,"ண"  ,"ணா"  ,"ணி"  ,"ணீ"  ,"ணு"  ,"ணூ"  ,"ணெ"  ,"ணே"  ,"ணை"  ,"ணொ"  ,"ணோ"  ,"ணௌ" 
 ,"ந"  ,"நா"  ,"நி"  ,"நீ"  ,"நு"  ,"நூ"  ,"நெ"  ,"நே"  ,"நை"  ,"நொ"  ,"நோ"  ,"நௌ" 
 ,"ம"  ,"மா"  ,"மி"  ,"மீ"  ,"மு"  ,"மூ"  ,"மெ"  ,"மே"  ,"மை"  ,"மொ"  ,"மோ"  ,"மௌ" 
 ,"ன"  ,"னா"  ,"னி"  ,"னீ"  ,"னு"  ,"னூ"  ,"னெ"  ,"னே"  ,"னை"  ,"னொ"  ,"னோ"  ,"னௌ" 
 ,"ய"  ,"யா"  ,"யி"  ,"யீ"  ,"யு"  ,"யூ"  ,"யெ"  ,"யே"  ,"யை"  ,"யொ"  ,"யோ"  ,"யௌ" 
 ,"ர"  ,"ரா"  ,"ரி"  ,"ரீ"  ,"ரு"  ,"ரூ"  ,"ரெ"  ,"ரே"  ,"ரை"  ,"ரொ"  ,"ரோ"  ,"ரௌ" 
 ,"ல"  ,"லா"  ,"லி"  ,"லீ"  ,"லு"  ,"லூ"  ,"லெ"  ,"லே"  ,"லை"  ,"லொ"  ,"லோ"  ,"லௌ" 
 ,"வ"  ,"வா"  ,"வி"  ,"வீ"  ,"வு"  ,"வூ"  ,"வெ"  ,"வே"  ,"வை"  ,"வொ"  ,"வோ"  ,"வௌ" 
 ,"ழ"  ,"ழா"  ,"ழி"  ,"ழீ"  ,"ழு"  ,"ழூ"  ,"ழெ"  ,"ழே"  ,"ழை"  ,"ழொ"  ,"ழோ"  ,"ழௌ" 
 ,"ள"  ,"ளா"  ,"ளி"  ,"ளீ"  ,"ளு"  ,"ளூ"  ,"ளெ"  ,"ளே"  ,"ளை"  ,"ளொ"  ,"ளோ"  ,"ளௌ" 
 
 ##/* Sanskrit Uyir-Mei */
  ,"ஜ"  ,"ஜா"  ,"ஜி"  ,"ஜீ"  ,"ஜு"  ,"ஜூ"  ,"ஜெ"  ,"ஜே"  ,"ஜை"  ,"ஜொ"  ,"ஜோ"  ,"ஜௌ" 
 ,"ஷ"  ,"ஷா"  ,"ஷி"  ,"ஷீ"  ,"ஷு"  ,"ஷூ"  ,"ஷெ"  ,"ஷே"  ,"ஷை"  ,"ஷொ"  ,"ஷோ"  ,"ஷௌ" 
 ,"ஸ"  ,"ஸா"  ,"ஸி"  ,"ஸீ"  ,"ஸு"  ,"ஸூ"  ,"ஸெ"  ,"ஸே"  ,"ஸை"  ,"ஸொ"  ,"ஸோ"  ,"ஸௌ" 
 ,"ஹ"  ,"ஹா"  ,"ஹி"  ,"ஹீ"  ,"ஹு"  ,"ஹூ"  ,"ஹெ"  ,"ஹே"  ,"ஹை"  ,"ஹொ"  ,"ஹோ"  ,"ஹௌ" ]

## some assertions, languages dont change fast.
assert ( TA_ACCENT_LEN == len(accent_symbols) )
assert ( TA_AYUDHA_LEN == 1 )
assert ( TA_UYIR_LEN == len( uyir_letters ) )
assert ( TA_MEI_LEN == len( mei_letters ) )
assert ( TA_AGARAM_LEN == len( agaram_letters ) )
assert ( TA_SANSKRIT_LEN == len( sanskrit_letters )) 
assert ( TA_UYIRMEI_LEN == len( uyirmei_letters ) )

## length of the definitions
def accent_len( ):
        return TA_ACCENT_LEN ## 13 = 12 + 1

def ayudha_len( ):
        return TA_AYUDHA_LEN ## 1 

def uyir_len( ):
        return TA_UYIR_LEN ##12

def mei_len( ):
        return TA_MEI_LEN ##18

def agaram_len( ):
        return TA_AGARAM_LEN ##18

def uyirmei_len( ):
        return TA_UYIRMEI_LEN ##216

def tamil_len(  ):
        return len(tamil_letters)

## access the letters
def uyir( idx ):
        assert ( idx >= 0 and idx < uyir_len() )
        return uyir_letters[idx]

def agaram( idx ):
       assert ( idx >= 0 and idx < agaram_len() )
       return agaram_letters[idx]

def mei( idx ):
       assert ( idx >= 0 and idx < mei_len() )
       return mei_letters[idx]

def uyirmei( idx ):
       assert( idx >= 0 and idx < uyirmei_len() )
       return uyirmei_letters[idx]

def uyirmei_constructed( mei_idx, uyir_idx):
       idx,idy = mei_idx,uyir_idx
       assert ( idy >= 0 and idy < uyir_len() )
       assert ( idx >= 0 and idx < mei_len() )
       return agaram_letters[mei_idx]+accent_symbols[uyir_idx]

def tamil( idx ):
        assert ( idx >= 0 and idx < tamil_len() )
        return tamil_letters[idx]

## useful part of the API:
def istamil_prefix( word ):
        """ check if the given word has a tamil prefix. Returns
        either a True/False flag """
        if ( word.isalpha() ): return False
        for letters in tamil_letters:
                if ( word.find(letters) == 0 ):
                        return True
        return False

def has_tamil( word ):
        """check if the word has any occurance of any tamil letter """
        for letters in tamil_letters:
                if ( word.find(letters) >= 0 ):
                        return True
        return False

def istamil ( tchar ):
        """ check if the letter tchar is prefix of 
        any of tamil-letter. It suggests we have a tamil identifier"""
        if ( tchar.isalpha() ): return False
        for letters in tamil_letters:
                if ( letters.find( tchar ) == 0 ):
                        return True
        return False

def istamil_alnum( tchar ):
        """ check if the character is alphanumeric, or tamil.
        This saves time from running through istamil() check. """
        return ( tchar.isalnum( ) or tchar.istamil( ) )

## reverse a Tamil word according to letters not unicode-points
def reverse_word( word ):
	op = get_letters( word )
	op.reverse()
	return u"".join(op)

## Split a tamil-unicode stream into
## tamil characters (individuals).
def get_letters( word ):
        """ splits the word into a character-list of tamil/english
        characters present in the stream """
            #word = unicode(word) #.encode('utf-8')
        prev = u''
        word=word.decode('utf-8')
	ta_letters = []
        for c in word:
		if c in uyir_letters or c == ayudha_letter:
			ta_letters.append(prev+c)
			prev = u''
		elif c in agaram_letters or c in sanskrit_letters:
			if prev != u'':
				ta_letters.append(prev)
			prev = c
		elif c in accent_symbols:
			ta_letters.append(prev+c)
			prev = u''
		else:
			if prev != u'':
				ta_letters.append(prev+c)
				prev = u''
			elif ord(c) < 256:
				# plain-old ascii
				ta_letters.append( c )
			else:
				assert False #unknown/expected state
	if prev != u'': #if prev is not null it is $c
		ta_letters.append( prev )
#print ta_letters
#print u"".join(ta_letters)
	return ta_letters
