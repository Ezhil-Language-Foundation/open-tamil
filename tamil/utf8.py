## This Python file uses the following encoding: utf-8
##
## (C) 2007, 2008, 2013 Muthiah Annamalai <ezhillang@gmail.com>
## Licensed under GPL Version 3
## (C) 2013 msathia <msathia@gmail.com>

## constants
TA_ACCENT_LEN = 13 #12 + 1
TA_AYUDHA_LEN = 1
TA_UYIR_LEN = 12
TA_MEI_LEN = 18
TA_AGARAM_LEN = 18
TA_SANSKRIT_LEN = 4
TA_UYIRMEI_LEN = 216 # 18*12

def  letters_to_py( _letters ):
        """ return list of letters e.g. uyir_letters as a Python list """
        return u"[u'"+u"',u'".join( _letters )+u"']"

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
u"க"  ,u"கா"  ,u"கி"  ,u"கீ"  ,u"கு"  ,u"கூ"  ,u"கெ"  ,u"கே"  ,u"கை"  ,u"கொ"  ,u"கோ"  ,u"கௌ"  ,
u"ச"  ,u"சா"  ,u"சி"  ,u"சீ"  ,u"சு"  ,u"சூ"  ,u"செ"  ,u"சே"  ,u"சை"  ,u"சொ"  ,u"சோ"  ,u"சௌ" , 
u"ட"  ,u"டா"  ,u"டி"  ,u"டீ"  ,u"டு"  ,u"டூ"  ,u"டெ"  ,u"டே"  ,u"டை"  ,u"டொ"  ,u"டோ"  ,u"டௌ", 
u"த"  ,u"தா"  ,u"தி"  ,u"தீ"  ,u"து"  ,u"தூ"  ,u"தெ"  ,u"தே"  ,u"தை"  ,u"தொ"  ,u"தோ"  ,u"தௌ", 
u"ப"  ,u"பா"  ,u"பி"  ,u"பீ"  ,u"பு"  ,u"பூ"  ,u"பெ"  ,u"பே"  ,u"பை"  ,u"பொ"  ,u"போ"  ,u"பௌ" , 
u"ற"  ,u"றா"  ,u"றி"  ,u"றீ"  ,u"று"  ,u"றூ"  ,u"றெ"  ,u"றே"  ,u"றை"  ,u"றொ"  ,u"றோ"  ,u"றௌ", 
u"ஞ"  ,u"ஞா"  ,u"ஞி"  ,u"ஞீ"  ,u"ஞு"  ,u"ஞூ"  ,u"ஞெ"  ,u"ஞே"  ,u"ஞை"  ,u"ஞொ"  ,u"ஞோ"  ,u"ஞௌ"  ,
u"ங"  ,u"ஙா"  ,u"ஙி"  ,u"ஙீ"  ,u"ஙு"  ,u"ஙூ"  ,u"ஙெ"  ,u"ஙே"  ,u"ஙை"  ,u"ஙொ"  ,u"ஙோ"  ,u"ஙௌ"  ,
u"ண"  ,u"ணா"  ,u"ணி"  ,u"ணீ"  ,u"ணு"  ,u"ணூ"  ,u"ணெ"  ,u"ணே"  ,u"ணை"  ,u"ணொ"  ,u"ணோ"  ,u"ணௌ"  ,
u"ந"  ,u"நா"  ,u"நி"  ,u"நீ"  ,u"நு"  ,u"நூ"  ,u"நெ"  ,u"நே"  ,u"நை"  ,u"நொ"  ,u"நோ"  ,u"நௌ"  ,
u"ம"  ,u"மா"  ,u"மி"  ,u"மீ"  ,u"மு"  ,u"மூ"  ,u"மெ"  ,u"மே"  ,u"மை"  ,u"மொ"  ,u"மோ"  ,u"மௌ" , 
u"ன"  ,u"னா"  ,u"னி"  ,u"னீ"  ,u"னு"  ,u"னூ"  ,u"னெ"  ,u"னே"  ,u"னை"  ,u"னொ"  ,u"னோ"  ,u"னௌ", 
u"ய"  ,u"யா"  ,u"யி"  ,u"யீ"  ,u"யு"  ,u"யூ"  ,u"யெ"  ,u"யே"  ,u"யை"  ,u"யொ"  ,u"யோ"  ,u"யௌ", 
u"ர"  ,u"ரா"  ,u"ரி"  ,u"ரீ"  ,u"ரு"  ,u"ரூ"  ,u"ரெ"  ,u"ரே"  ,u"ரை"  ,u"ரொ"  ,u"ரோ"  ,u"ரௌ", 
u"ல"  ,u"லா"  ,u"லி"  ,u"லீ"  ,u"லு"  ,u"லூ"  ,u"லெ"  ,u"லே"  ,u"லை"  ,u"லொ"  ,u"லோ"  ,u"லௌ" , 
u"வ"  ,u"வா"  ,u"வி"  ,u"வீ"  ,u"வு"  ,u"வூ"  ,u"வெ"  ,u"வே"  ,u"வை"  ,u"வொ"  ,u"வோ"  ,u"வௌ" , 
u"ழ"  ,u"ழா"  ,u"ழி"  ,u"ழீ"  ,u"ழு"  ,u"ழூ"  ,u"ழெ"  ,u"ழே"  ,u"ழை"  ,u"ழொ"  ,u"ழோ"  ,u"ழௌ" , 
u"ள"  ,u"ளா"  ,u"ளி"  ,u"ளீ"  ,u"ளு"  ,u"ளூ"  ,u"ளெ"  ,u"ளே"  ,u"ளை"  ,u"ளொ"  ,u"ளோ"  ,u"ளௌ" ]

# tamil symbols
_day = u"௳"
_month = u"௴"
_year = u"௵"
_debit = u"௶"
_credit = u"௷"
_rupee = u"௹"
_numeral = u"௺"
_sri = u"\u0bb6\u0bcd\u0bb0\u0bc0" #SRI - ஶ்ரீ
_ksha = u"\u0b95\u0bcd\u0bb7" #KSHA - க்ஷ
_ksh = u"\u0b95\u0bcd\u0bb7\u0bcd" #KSH - க்ஷ்

tamil_symbols = [_day, _month, _year, _debit, _credit, _rupee, _numeral, _sri, _ksha, _ksh]

## total tamil letters in use, including sanskrit letters
tamil_letters = [
	
## /* Uyir */
u"அ",u"ஆ",u"இ", u"ஈ",u"உ",u"ஊ",u"எ",u"ஏ",u"ஐ",u"ஒ",u"ஓ",u"ஔ",

##/* Ayuda Ezhuthu */
u"ஃ",
	
## /* Mei */	
u"க்",u"ச்",u"ட்",u"த்",u"ப்",u"ற்",u"ஞ்",u"ங்",u"ண்",u"ந்",u"ம்",u"ன்",u"ய்",u"ர்",u"ல்",u"வ்",u"ழ்",u"ள்",

## /* Agaram */
u"க",u"ச",u"ட",u"த",u"ப",u"ற",u"ஞ",u"ங",u"ண",u"ந",u"ம",u"ன",u"ய",u"ர",u"ல",u"வ",u"ழ",u"ள",
	
## /* Sanskrit (Vada Mozhi) */
u"ஜ",u"ஷ", u"ஸ",u"ஹ",

##/* Sanskrit (Mei) */
u"ஜ்",u"ஷ்", u"ஸ்",u"ஹ்",
	
## /* Uyir Mei */
u"க"  ,u"கா"  ,u"கி"  ,u"கீ"  ,u"கு"  ,u"கூ"  ,u"கெ"  ,u"கே"  ,u"கை"  ,u"கொ"  ,u"கோ"  ,u"கௌ" 
 ,u"ச"  ,u"சா"  ,u"சி"  ,u"சீ"  ,u"சு"  ,u"சூ"  ,u"செ"  ,u"சே"  ,u"சை"  ,u"சொ"  ,u"சோ"  ,u"சௌ" 
 ,u"ட"  ,u"டா"  ,u"டி"  ,u"டீ"  ,u"டு"  ,u"டூ"  ,u"டெ"  ,u"டே"  ,u"டை"  ,u"டொ"  ,u"டோ"  ,u"டௌ" 
 ,u"த"  ,u"தா"  ,u"தி"  ,u"தீ"  ,u"து"  ,u"தூ"  ,u"தெ"  ,u"தே"  ,u"தை"  ,u"தொ"  ,u"தோ"  ,u"தௌ" 
 ,u"ப"  ,u"பா"  ,u"பி"  ,u"பீ"  ,u"பு"  ,u"பூ"  ,u"பெ"  ,u"பே"  ,u"பை"  ,u"பொ"  ,u"போ"  ,u"பௌ" 
 ,u"ற"  ,u"றா"  ,u"றி"  ,u"றீ"  ,u"று"  ,u"றூ"  ,u"றெ"  ,u"றே"  ,u"றை"  ,u"றொ"  ,u"றோ"  ,u"றௌ" 
 ,u"ஞ"  ,u"ஞா"  ,u"ஞி"  ,u"ஞீ"  ,u"ஞு"  ,u"ஞூ"  ,u"ஞெ"  ,u"ஞே"  ,u"ஞை"  ,u"ஞொ"  ,u"ஞோ"  ,u"ஞௌ" 
 ,u"ங"  ,u"ஙா"  ,u"ஙி"  ,u"ஙீ"  ,u"ஙு"  ,u"ஙூ"  ,u"ஙெ"  ,u"ஙே"  ,u"ஙை"  ,u"ஙொ"  ,u"ஙோ"  ,u"ஙௌ" 
 ,u"ண"  ,u"ணா"  ,u"ணி"  ,u"ணீ"  ,u"ணு"  ,u"ணூ"  ,u"ணெ"  ,u"ணே"  ,u"ணை"  ,u"ணொ"  ,u"ணோ"  ,u"ணௌ" 
 ,u"ந"  ,u"நா"  ,u"நி"  ,u"நீ"  ,u"நு"  ,u"நூ"  ,u"நெ"  ,u"நே"  ,u"நை"  ,u"நொ"  ,u"நோ"  ,u"நௌ" 
 ,u"ம"  ,u"மா"  ,u"மி"  ,u"மீ"  ,u"மு"  ,u"மூ"  ,u"மெ"  ,u"மே"  ,u"மை"  ,u"மொ"  ,u"மோ"  ,u"மௌ" 
 ,u"ன"  ,u"னா"  ,u"னி"  ,u"னீ"  ,u"னு"  ,u"னூ"  ,u"னெ"  ,u"னே"  ,u"னை"  ,u"னொ"  ,u"னோ"  ,u"னௌ" 
 ,u"ய"  ,u"யா"  ,u"யி"  ,u"யீ"  ,u"யு"  ,u"யூ"  ,u"யெ"  ,u"யே"  ,u"யை"  ,u"யொ"  ,u"யோ"  ,u"யௌ" 
 ,u"ர"  ,u"ரா"  ,u"ரி"  ,u"ரீ"  ,u"ரு"  ,u"ரூ"  ,u"ரெ"  ,u"ரே"  ,u"ரை"  ,u"ரொ"  ,u"ரோ"  ,u"ரௌ" 
 ,u"ல"  ,u"லா"  ,u"லி"  ,u"லீ"  ,u"லு"  ,u"லூ"  ,u"லெ"  ,u"லே"  ,u"லை"  ,u"லொ"  ,u"லோ"  ,u"லௌ" 
 ,u"வ"  ,u"வா"  ,u"வி"  ,u"வீ"  ,u"வு"  ,u"வூ"  ,u"வெ"  ,u"வே"  ,u"வை"  ,u"வொ"  ,u"வோ"  ,u"வௌ" 
 ,u"ழ"  ,u"ழா"  ,u"ழி"  ,u"ழீ"  ,u"ழு"  ,u"ழூ"  ,u"ழெ"  ,u"ழே"  ,u"ழை"  ,u"ழொ"  ,u"ழோ"  ,u"ழௌ" 
 ,u"ள"  ,u"ளா"  ,u"ளி"  ,u"ளீ"  ,u"ளு"  ,u"ளூ"  ,u"ளெ"  ,u"ளே"  ,u"ளை"  ,u"ளொ"  ,u"ளோ"  ,u"ளௌ" 
 
 ##/* Sanskrit Uyir-Mei */
  ,u"ஜ"  ,u"ஜா"  ,u"ஜி"  ,u"ஜீ"  ,u"ஜு"  ,u"ஜூ"  ,u"ஜெ"  ,u"ஜே"  ,u"ஜை"  ,u"ஜொ"  ,u"ஜோ"  ,u"ஜௌ" 
 ,u"ஷ"  ,u"ஷா"  ,u"ஷி"  ,u"ஷீ"  ,u"ஷு"  ,u"ஷூ"  ,u"ஷெ"  ,u"ஷே"  ,u"ஷை"  ,u"ஷொ"  ,u"ஷோ"  ,u"ஷௌ" 
 ,u"ஸ"  ,u"ஸா"  ,u"ஸி"  ,u"ஸீ"  ,u"ஸு"  ,u"ஸூ"  ,u"ஸெ"  ,u"ஸே"  ,u"ஸை"  ,u"ஸொ"  ,u"ஸோ"  ,u"ஸௌ" 
 ,u"ஹ"  ,u"ஹா"  ,u"ஹி"  ,u"ஹீ"  ,u"ஹு"  ,u"ஹூ"  ,u"ஹெ"  ,u"ஹே"  ,u"ஹை"  ,u"ஹொ"  ,u"ஹோ"  ,u"ஹௌ" ]

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

def all_tamil( word ):
        return all( [(letter in tamil_letters) for letter in word] )

def has_tamil( word ):
        """check if the word has any occurance of any tamil letter """
        # list comprehension is not necessary - we bail at earliest
        for letters in tamil_letters:
                if ( word.find(letters) >= 0 ):
                        return True
        return False

def istamil ( tchar ):
        """ check if the letter tchar is prefix of 
        any of tamil-letter. It suggests we have a tamil identifier"""
        if (tchar in tamil_letters):
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
	prev = u''#word = unicode(word) #.encode('utf-8')
	#word=word.decode('utf-8')
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
                # assertion is somewhat heavy handed here
				print(u"Warning: #unknown/expected state - continuing tamil letter tokenizing. Copy unknown character to string output")
                                ta_letters.append( c )
	if prev != u'': #if prev is not null it is $c
		ta_letters.append( prev )
#print ta_letters
#print u"".join(ta_letters)
	return ta_letters

# same as get_letters but use as iterable
def get_letters_iterable( word ):
	""" splits the word into a character-list of tamil/english
	characters present in the stream """
	prev = u''
	ta_letters = []
	for c in word:
		if c in uyir_letters or c == ayudha_letter:
			yield (prev+c)
			prev = u''
		elif c in agaram_letters or c in sanskrit_letters:
			if prev != u'':
				yield (prev)
			prev = c
		elif c in accent_symbols:
			yield (prev+c)
			prev = u''
		else:
			if prev != u'':
				yield (prev+c)
				prev = u''
			elif ord(c) < 256:
				# plain-old ascii
				yield ( c )
			else:
                # assertion is somewhat heavy handed here
				print(u"Warning: #unknown/expected state - continuing tamil letter tokenizing. Copy unknown character to string output")
                                yield c
	if prev != u'': #if prev is not null it is $c
		yield prev
#print ta_letters
#print u"".join(ta_letters)
        raise StopIteration

def get_words( letters, tamil_only=False ):
        """ given a list of UTF-8 letters section them into words, grouping them at spaces """
        import re
        if ( tamil_only ):
                opstr = u"".join(filter( lambda x: x.isspace() or istamil(x),
                                         letters ))
        else:
                opstr = u"".join(letters)

        # debug helpers
        #for parts in re.split('\s+',opstr):
        #        print parts   
        return re.split('\s+',opstr)

def get_tamil_words( letters ):
        tamil_only = True
        return get_words( letters, tamil_only )

# answer if word_a ranks ahead of, or at same level, as word_b in a Tamil dictionary order...
# for use with Python : if a > 0 
def compare_words_lexicographic( word_a, word_b ):
        # sanity check for words to be all Tamil
        if ( not all_tamil(word_a) ) or (not all_tamil(word_b)) :
            print("## ")
            print word_a
            print word_b
            print("Both operands need to be Tamil words")
        La = len(word_a)
        Lb = len(word_b)
        all_TA_letters = u"".join(tamil_letters)
        for itr in range(0,min(La,Lb)):
                pos1 =   all_TA_letters.find( word_a[itr] )
                pos2 =   all_TA_letters.find( word_b[itr] )
                
                if pos1 != pos2 :
                        #print  not( pos1 > pos2), pos1, pos2
                        return cmp(pos1, pos2)
                
        if La == Lb:                
                # both words are equal
                return 0
        
        # else result depends on if La is shorter than Lb
        return cmp(La,Lb)

# அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ ஃ 
# க் ச் ட் த் ப் ற் ஞ் ங் ண் ந் ம் ன் ய் ர் ல் வ் ழ் ள் ஜ் ஷ் ஸ் ஹ் 
# க ச ட த ப ற ஞ ங ண ந ம ன ய ர ல வ ழ ள ஜ ஷ ஸ ஹ 
# க கா கி கீ கு கூ கெ கே கை  கௌ 
# ச சா சி சீ சு சூ செ சே சை சொ சோ சௌ 
# ட டா டி டீ டு டூ டெ டே டை டொ டோ டௌ 
# த தா தி தீ து தூ தெ தே தை தொ தோ தௌ 
# ப பா பி பீ பு பூ பெ பே பை பொ போ பௌ 
# ற றா றி றீ று றூ றெ றே றை றொ றோ றௌ 
# ஞ ஞா ஞி ஞீ ஞு ஞூ ஞெ ஞே ஞை ஞொ ஞோ ஞௌ 
# ங ஙா ஙி ஙீ ஙு ஙூ ஙெ ஙே ஙை ஙொ ஙோ ஙௌ 
# ண ணா ணி ணீ ணு ணூ ணெ ணே ணை ணொ ணோ ணௌ 
# ந நா நி நீ நு நூ நெ நே நை நொ நோ நௌ 
# ம மா மி மீ மு மூ மெ மே மை மொ மோ மௌ 
# ன னா னி னீ னு னூ னெ னே னை னொ னோ னௌ 
# ய யா யி யீ யு யூ யெ யே யை யொ யோ யௌ 
# ர ரா ரி ரீ ரு ரூ ரெ ரே ரை ரொ ரோ ரௌ 
# ல லா லி லீ லு லூ லெ லே லை லொ லோ லௌ 
# வ வா வி வீ வு வூ வெ வே வை வொ வோ வௌ 
# ழ ழா ழி ழீ ழு ழூ ழெ ழே ழை ழொ ழோ ழௌ
# ள ளா ளி ளீ ளு ளூ ளெ ளே ளை ளொ ளோ ளௌ 
# ஜ ஜா ஜி ஜீ ஜு ஜூ ஜெ ஜே ஜை ஜொ ஜோ ஜௌ 
# ஷ ஷா ஷி ஷீ ஷு ஷூ ஷெ ஷே ஷை ஷொ ஷோ ஷௌ 
# ஸ ஸா ஸி ஸீ ஸு ஸூ ஸெ ஸே ஸை ஸொ ஸோ ஸௌ 
# ஹ ஹா ஹி ஹீ ஹு ஹூ ஹெ ஹே ஹை ஹொ ஹோ ஹௌ
