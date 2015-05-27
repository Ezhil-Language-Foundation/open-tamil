# encoding: utf-8
# (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>

class AssertionError < RuntimeError
end

def assert &block
    raise AssertionError unless yield
end

module Tamil
    ## constants
    TA_ACCENT_LEN = 13 #12 + 1
    TA_AYUDHA_LEN = 1
    TA_UYIR_LEN = 12
    TA_MEI_LEN = 18
    TA_AGARAM_LEN = 18
    TA_SANSKRIT_LEN = 6
    TA_UYIRMEI_LEN = 216
    TA_GRANTHA_UYIRMEI_LEN = 24*12
    TA_LETTERS_LEN = 247 + 6*12 + 22 + 4 - TA_AGARAM_LEN - 4 #323

    # List of letters you can use
    @@agaram_letters = ["க","ச","ட","த","ப","ற","ஞ","ங","ண","ந","ம","ன","ய","ர","ல","வ","ழ","ள"]
    AGARAM_LETTERS = @@agaram_letters.clone
    
    @@uyir_letters = ["அ","ஆ","இ","ஈ","உ","ஊ","எ","ஏ","ஐ","ஒ","ஓ","ஔ"]
    @@ayudha_letter = "ஃ"
    
    @@kuril_letters = ["அ", "இ", "உ", "எ", "ஒ"]
    @@nedil_letters = ["ஆ", "ஈ", "ஊ", "ஏ", "ஓ"]

    @@vallinam_letters = ["க்", "ச்", "ட்", "த்", "ப்", "ற்"]
    @@mellinam_letters = ["ங்", "ஞ்", "ண்", "ந்", "ம்", "ன்"]
    @@idayinam_letters = ["ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"]

    @@mei_letters = ["க்","ச்","ட்","த்","ப்","ற்","ஞ்","ங்","ண்","ந்","ம்","ன்","ய்","ர்","ல்","வ்","ழ்","ள்" ]

    @@accent_symbols = ["","ா","ி","ீ","ு","ூ","ெ","ே","ை","ொ","ோ","ௌ","ஃ"]
    @@pulli_symbols = ["்"]

    @@sanskrit_letters = ["ஶ","ஜ","ஷ", "ஸ","ஹ","க்ஷ"]
    @@sanskrit_mei_letters =["ஶ்","ஜ்","ஷ்", "ஸ்","ஹ்","க்ஷ்"]

    @@grantha_mei_letters = @@mei_letters.clone()
    @@grantha_mei_letters.concat(@@sanskrit_mei_letters)

    @@grantha_agaram_letters = @@agaram_letters.clone()
    @@grantha_agaram_letters.concat(@@sanskrit_letters)

    @@uyirmei_letters = [ "க"  ,"கா"  ,"கி"  ,"கீ"  ,"கு"  ,"கூ"  ,"கெ"  ,"கே"  ,"கை"  ,"கொ"  ,"கோ"  ,"கௌ"  ,
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

    def Tamil.get_letters(word)
        ## Split a tamil-unicode stream into
        ## tamil characters (individuals).
        """ splits the word into a character-list of tamil/english
            characters present in the stream """ 
        ta_letters = Array.new()
        not_empty = false
        wlen = word.length()
        idx = 0
        while (idx < wlen)
            c = word[idx]
            if @@uyir_letters.include?(c) or c == @@ayudha_letter
                ta_letters.insert(-1,c)
                not_empty = true
            elsif @@grantha_agaram_letters.include?(c)
                ta_letters.insert(-1,c)
                not_empty = true
            elsif @@accent_symbols.include?(c)
                if not not_empty
                   # odd situation
                   ta_letters.insert(-1,c)
                   not_empty = true
                else
                   ta_letters[-1] += c 
                end                   
            else
                if c < "\u00FF"
                   ta_letters.insert(-1, c )
                else
                   if not_empty
                      ta_letters[-1]+= c
                   else
                      ta_letters.insert(-1,c)
                      not_empty = true
                   end
                end
            end
            idx = idx + 1
        end
        return ta_letters
    end

    ## length of the definitions
    def Tamil.accent_len( )
        return Tamil::TA_ACCENT_LEN ## 13 = 12 + 1
    end

    def Tamil.ayudha_len( )
        return Tamil::TA_AYUDHA_LEN ## 1 
    end

    def Tamil.uyir_len( )
        return Tamil::TA_UYIR_LEN ##12
    end

    def Tamil.mei_len( )
        return Tamil::TA_MEI_LEN ##18
    end

    def Tamil.agaram_len( )
        assert { @@agaram_letters.length == Tamil::TA_AGARAM_LEN }
        return Tamil::TA_AGARAM_LEN ##18
    end

    def Tamil.uyirmei_len( )
        return Tamil::TA_UYIRMEI_LEN ##216
    end

    def Tamil.tamil_len(  )
        return @@tamil_letters.length
    end

    ## access the letters
    def Tamil.uyir( idx )
        assert { ( idx >= 0 ) and  ( idx < Tamil.uyir_len() ) }
        return Tamil::uyir_letters[idx]
    end

    def Tamil.agaram( idx )
        assert {( idx >= 0) and ( idx < Tamil.agaram_len() )}
        return @@agaram_letters[idx]
    end

    def Tamil.mei( idx )
        assert {( idx >= 0 ) and ( idx < Tamil.mei_len() )}
        return @@mei_letters[idx]
    end

    def Tamil.uyirmei( idx )
        assert {( idx >= 0 ) and  ( idx < Tamil.uyirmei_len() ) }
        return @@uyirmei_letters[idx]
    end
    
end

# ## total tamil letters in use, including sanskrit letters
# tamil_letters = [
 
# ## /* Uyir */
# "அ","ஆ","இ", "ஈ","உ","ஊ","எ","ஏ","ஐ","ஒ","ஓ","ஔ",

# ##/* Ayuda Ezhuthu */
# "ஃ",
 
# ## /* Mei */    
# "க்","ச்","ட்","த்","ப்","ற்","ஞ்","ங்","ண்","ந்","ம்","ன்","ய்","ர்","ல்","வ்","ழ்","ள்",

# ## /* Agaram */
# ## "க","ச","ட","த","ப","ற","ஞ","ங","ண","ந","ம","ன","ய","ர","ல","வ","ழ","ள",
 
# ## /* Sanskrit (Vada Mozhi) */
# ## "ஜ","ஷ", "ஸ","ஹ",

# ##/* Sanskrit (Mei) */
# "ஜ்","ஷ்", "ஸ்","ஹ்",
 
# ## /* Uyir Mei */
# "க"  ,"கா"  ,"கி"  ,"கீ"  ,"கு"  ,"கூ"  ,"கெ"  ,"கே"  ,"கை"  ,"கொ"  ,"கோ"  ,"கௌ" 
# ,"ச"  ,"சா"  ,"சி"  ,"சீ"  ,"சு"  ,"சூ"  ,"செ"  ,"சே"  ,"சை"  ,"சொ"  ,"சோ"  ,"சௌ" 
# ,"ட"  ,"டா"  ,"டி"  ,"டீ"  ,"டு"  ,"டூ"  ,"டெ"  ,"டே"  ,"டை"  ,"டொ"  ,"டோ"  ,"டௌ" 
# ,"த"  ,"தா"  ,"தி"  ,"தீ"  ,"து"  ,"தூ"  ,"தெ"  ,"தே"  ,"தை"  ,"தொ"  ,"தோ"  ,"தௌ" 
# ,"ப"  ,"பா"  ,"பி"  ,"பீ"  ,"பு"  ,"பூ"  ,"பெ"  ,"பே"  ,"பை"  ,"பொ"  ,"போ"  ,"பௌ" 
# ,"ற"  ,"றா"  ,"றி"  ,"றீ"  ,"று"  ,"றூ"  ,"றெ"  ,"றே"  ,"றை"  ,"றொ"  ,"றோ"  ,"றௌ" 
# ,"ஞ"  ,"ஞா"  ,"ஞி"  ,"ஞீ"  ,"ஞு"  ,"ஞூ"  ,"ஞெ"  ,"ஞே"  ,"ஞை"  ,"ஞொ"  ,"ஞோ"  ,"ஞௌ" 
# ,"ங"  ,"ஙா"  ,"ஙி"  ,"ஙீ"  ,"ஙு"  ,"ஙூ"  ,"ஙெ"  ,"ஙே"  ,"ஙை"  ,"ஙொ"  ,"ஙோ"  ,"ஙௌ" 
# ,"ண"  ,"ணா"  ,"ணி"  ,"ணீ"  ,"ணு"  ,"ணூ"  ,"ணெ"  ,"ணே"  ,"ணை"  ,"ணொ"  ,"ணோ"  ,"ணௌ" 
# ,"ந"  ,"நா"  ,"நி"  ,"நீ"  ,"நு"  ,"நூ"  ,"நெ"  ,"நே"  ,"நை"  ,"நொ"  ,"நோ"  ,"நௌ" 
# ,"ம"  ,"மா"  ,"மி"  ,"மீ"  ,"மு"  ,"மூ"  ,"மெ"  ,"மே"  ,"மை"  ,"மொ"  ,"மோ"  ,"மௌ" 
# ,"ன"  ,"னா"  ,"னி"  ,"னீ"  ,"னு"  ,"னூ"  ,"னெ"  ,"னே"  ,"னை"  ,"னொ"  ,"னோ"  ,"னௌ" 
# ,"ய"  ,"யா"  ,"யி"  ,"யீ"  ,"யு"  ,"யூ"  ,"யெ"  ,"யே"  ,"யை"  ,"யொ"  ,"யோ"  ,"யௌ" 
# ,"ர"  ,"ரா"  ,"ரி"  ,"ரீ"  ,"ரு"  ,"ரூ"  ,"ரெ"  ,"ரே"  ,"ரை"  ,"ரொ"  ,"ரோ"  ,"ரௌ" 
# ,"ல"  ,"லா"  ,"லி"  ,"லீ"  ,"லு"  ,"லூ"  ,"லெ"  ,"லே"  ,"லை"  ,"லொ"  ,"லோ"  ,"லௌ" 
# ,"வ"  ,"வா"  ,"வி"  ,"வீ"  ,"வு"  ,"வூ"  ,"வெ"  ,"வே"  ,"வை"  ,"வொ"  ,"வோ"  ,"வௌ" 
# ,"ழ"  ,"ழா"  ,"ழி"  ,"ழீ"  ,"ழு"  ,"ழூ"  ,"ழெ"  ,"ழே"  ,"ழை"  ,"ழொ"  ,"ழோ"  ,"ழௌ" 
# ,"ள"  ,"ளா"  ,"ளி"  ,"ளீ"  ,"ளு"  ,"ளூ"  ,"ளெ"  ,"ளே"  ,"ளை"  ,"ளொ"  ,"ளோ"  ,"ளௌ" 
 
# ##/* Sanskrit Uyir-Mei */
# ,"ஶ", 	"ஶா", 	"ஶி", 	"ஶீ", "ஶு", "ஶூ", "ஶெ", "ஶே", "ஶை", "ஶொ", "ஶோ", "ஶௌ"
# ,"ஜ"  ,"ஜா"  ,"ஜி"  ,"ஜீ"  ,"ஜு"  ,"ஜூ"  ,"ஜெ"  ,"ஜே"  ,"ஜை"  ,"ஜொ"  ,"ஜோ"  ,"ஜௌ" 
# ,"ஷ"  ,"ஷா"  ,"ஷி"  ,"ஷீ"  ,"ஷு"  ,"ஷூ"  ,"ஷெ"  ,"ஷே"  ,"ஷை"  ,"ஷொ"  ,"ஷோ"  ,"ஷௌ" 
# ,"ஸ"  ,"ஸா"  ,"ஸி"  ,"ஸீ"  ,"ஸு"  ,"ஸூ"  ,"ஸெ"  ,"ஸே"  ,"ஸை"  ,"ஸொ"  ,"ஸோ"  ,"ஸௌ" 
# ,"ஹ"  ,"ஹா"  ,"ஹி"  ,"ஹீ"  ,"ஹு"  ,"ஹூ"  ,"ஹெ"  ,"ஹே"  ,"ஹை"  ,"ஹொ"  ,"ஹோ"  ,"ஹௌ"
# ,"க்ஷ"  ,"க்ஷா"  ,"க்ஷி" 	,"க்ஷீ" 	,"க்ஷு"  ,"க்ஷூ"  ,"க்ஷெ"   ,"க்ஷே" ,"க்ஷை"  ,"க்ஷொ" ,"க்ஷோ"  ,"க்ஷௌ" ]

# grantha_uyirmei_letters =  tamil_letters[tamil_letters.index("கா")-1:].clone()


# def uyirmei_constructed( mei_idx, uyir_idx):
    # """ construct uyirmei letter give mei index and uyir index """
    # idx,idy = mei_idx,uyir_idx
    # assert ( idy >= 0 and idy < uyir_len() )
    # assert ( idx >= 0 and idx < mei_len() )
    # return agaram_letters[mei_idx]+accent_symbols[uyir_idx]

# def tamil( idx ):
    # """ retrieve Tamil letter at canonical index from array utf8.tamil_letters """
    # assert ( idx >= 0 and idx < tamil_len() )
    # return tamil_letters[idx]

# # companion function to @tamil()
# def getidx(letter):
    # for itr in range(0,tamil_len()):
        # if tamil_letters[itr] == letter:
            # return itr
    # raise Exception("Cannot find letter in Tamil arichuvadi")    

# ## useful part of the API:
# def istamil_prefix( word ):
    # """ check if the given word has a tamil prefix. Returns
    # either a True/False flag """
    # for letter in tamil_letters:
        # if ( word.find(letter) == 0 ):
            # return True
    # return False

# if not PYTHON3:
    # is_tamil_unicode_predicate = lambda x: x >= unichr(2946) and x <= unichr(3066)
# else:
    # is_tamil_unicode_predicate = lambda x: x >= chr(2946) and x <= chr(3066)
# def is_tamil_unicode( sequence ):
    # # Ref: languagetool-office-extension/src/main/java/org/languagetool/openoffice/TamilDetector.java    
    # if type(sequence) is list:
        # return list(map( is_tamil_unicode_predicate, sequence ))
    # if len(sequence) > 1:
        # return list(map( is_tamil_unicode_predicate, get_letters(sequence) ))
    # return is_tamil_unicode_predicate( sequence )

# def all_tamil( word_in ):
    # """ predicate checks if all letters of the input word are Tamil letters """ 
    # if isinstance(word_in,list):
        # word = word_in
    # else:
        # word = get_letters( word_in )
    # return all( [(letter in tamil_letters) for letter in word] )

# def has_tamil( word ):
    # """check if the word has any occurance of any tamil letter """
    # # list comprehension is not necessary - we bail at earliest
    # for letters in tamil_letters:
        # if ( word.find(letters) >= 0 ):
            # return True
    # return False

# def istamil( tchar ):
    # """ check if the letter tchar is prefix of 
    # any of tamil-letter. It suggests we have a tamil identifier"""
    # if (tchar in tamil_letters):
        # return True
    # return False

# def istamil_alnum( tchar ):
    # """ check if the character is alphanumeric, or tamil.
    # This saves time from running through istamil() check. """
    # return ( tchar.isalnum( ) or istamil( tchar ) )

# def reverse_word( word ):
    # """ reverse a Tamil word according to letters not unicode-points """
    # op = get_letters( word )
    # op.reverse()
    # return "".join(op)

# ## find out if the letters like, "பொ" are written in canonical "ப + ொ"" graphemes then
# ## return True. If they are written like "ப + ெ + ா" then return False on first occurrence
# def is_normalized( text ):
    # TLEN,idx = len(text),1
    # kaal = "ா"
    # sinna_kombu, periya_kombu = "ெ", "ே"
    # kombugal = [sinna_kombu, periya_kombu]
    
    # def predicate( last_letter, prev_letter):
        # if ((last_letter == kaal) and (prev_letter in kombugal)):
            # return True
        # return False
    # if TLEN < 2:
        # return True
    # elif TLEN == 2:
        # if predicate( text[-1], text[-2] ):
            # return False
        # return True
    # a = text[0]
    # b = text[1]
    # assert idx == 1
    # while (idx < TLEN):
        # if predicate(b,a):
            # return False
        # a=b
        # idx = idx + 1
        # if idx < TLEN:
            # b=text[idx]
    # # reached end and nothing tripped us
    # return True 
    
# def _make_set(args):
    # if PYTHON3:
        # return frozenset(args)
    # return set(args)

# grantha_agaram_set = _make_set(grantha_agaram_letters)
# accent_symbol_set = _make_set(accent_symbols)
# uyir_letter_set   = _make_set(uyir_letters)


# _all_symbols = copy( accent_symbols )
# _all_symbols.extend( pulli_symbols )
# all_symbol_set = _make_set(_all_symbols)

# # same as get_letters but use as iterable
# def get_letters_iterable( word ):
    # """ splits the word into a character-list of tamil/english
    # characters present in the stream """
    # WLEN,idx = len(word),0
    
    # while (idx < WLEN):
        # c = word[idx]
        # #print(idx,hex(ord(c)),len(ta_letters))
        # if c in uyir_letter_set or c == ayudha_letter:
            # idx = idx + 1
            # yield c
        # elif c in grantha_agaram_set:
            # if idx + 1 < WLEN and word[idx+1] in all_symbol_set:
                # c2 = word[idx+1]
                # idx = idx + 2
                # yield (c + c2)
            # else:
                # idx = idx + 1
                # yield c
        # else: 
            # idx = idx + 1
            # yield c
    # raise StopIteration

# def get_words(letters,tamil_only=False):
    # return [ word for word in get_words_iterable(letters,tamil_only) ]

# def get_words_iterable( letters, tamil_only=False ):
    # """ given a list of UTF-8 letters section them into words, grouping them at spaces """
    
    # # correct algorithm for get-tamil-words
    # buf = []
    # for idx,let in enumerate(letters):
        # if not let.isspace():
            # if istamil(let) or (not tamil_only):
                # buf.append( let )
        # else:
            # if len(buf) > 0:
                # yield  "".join( buf )
                # buf = []
    # if len(buf) > 0:
        # yield "".join(buf)

# def get_tamil_words( letters ):
    # """ reverse a Tamil word according to letters, not unicode-points """
    # return [word for word in get_words_iterable( letters, tamil_only = True )]

# if PYTHON3:
    # def cmp( x, y):
        # if x == y:
            # return 0
        # if x > y:
            # return 1
        # return -1

# # answer if word_a ranks ahead of, or at same level, as word_b in a Tamil dictionary order...
# # for use with Python : if a > 0 
# def compare_words_lexicographic( word_a, word_b ):
    # """ compare words in Tamil lexicographic order """
    # # sanity check for words to be all Tamil
    # if ( not all_tamil(word_a) ) or (not all_tamil(word_b)) :
        # print("## ")
        # print(word_a)
        # print(word_b)
        # print("Both operands need to be Tamil words")
    # La = len(word_a)
    # Lb = len(word_b)
    # all_TA_letters = "".join(tamil_letters)
    # for itr in range(0,min(La,Lb)):
            # pos1 = all_TA_letters.find( word_a[itr] )
            # pos2 = all_TA_letters.find( word_b[itr] )

            # if pos1 != pos2 :
                    # #print  not( pos1 > pos2), pos1, pos2
                    # return cmp(pos1, pos2)

    # # result depends on if La is shorter than Lb, or 0 if La == Lb  i.e. cmp
    # return cmp(La,Lb)

# # return a list of ordered-pairs containing positions
# # that are common in word_a, and word_b; e.g.
# # தேடுக x தடங்கல் -> one common letter க [(2,3)]
# # சொல் x   தேடுக -> no common letters []
# def word_intersection( word_a, word_b ):
    # """ return a list of tuples where word_a, word_b intersect """
    # positions = []
    # word_a_letters = get_letters( word_a )
    # word_b_letters = get_letters( word_b )
    # for idx,wa in enumerate(word_a_letters):
        # for idy,wb in enumerate(word_b_letters):
            # if ( wa == wb ):
                # positions.append( (idx, idy) )
    # return positions

# def splitMeiUyir(uyirmei_char):    
    # """
    # This function split uyirmei compound character into mei + uyir characters
    # and returns in tuple.

    # Input : It must be unicode tamil char. 

    # Written By : Arulalan.T
    # Date : 22.09.2014

    # """
 
    # if not isinstance(uyirmei_char, PYTHON3 and str or unicode):
        # raise ValueError("Passed input letter '%s' must be unicode, \
                                # not just string" % uyirmei_char)
 
    # if uyirmei_char in mei_letters:
        # return uyirmei_char

    # if uyirmei_char in uyir_letters:
        # return uyirmei_char   
 
    # if uyirmei_char not in grantha_uyirmei_letters: 
        # raise ValueError("Passed input letter '%s' is not tamil letter" % uyirmei_char)
 
    # idx = grantha_uyirmei_letters.index(uyirmei_char)
    # uyiridx = idx % 12
    # meiidx = int((idx - uyiridx)/ 12)
    # return (grantha_mei_letters[meiidx], uyir_letters[uyiridx])
# # end of def splitMeiUyir(uyirmei_char): 

# def joinMeiUyir(mei_char, uyir_char):    
    # """
    # This function join mei character and uyir character, and retuns as 
    # compound uyirmei unicode character.
 
    # Inputs:
        # mei_char : It must be unicode tamil mei char. 
        # uyir_char : It must be unicode tamil uyir char. 
 
    # Written By : Arulalan.T
    # Date : 22.09.2014    
    # """    
    # if not isinstance(mei_char, PYTHON3 and str or unicode):
        # raise ValueError("Passed input mei character '%s' must be unicode, \
                                # not just string" % mei_char)
    # if not isinstance(uyir_char, PYTHON3 and str or unicode):
        # raise ValueError("Passed input uyir character '%s' must be unicode, \
                                # not just string" % uyir_char)
    # if mei_char not in grantha_mei_letters:
        # raise ValueError("Passed input character '%s' is not a"
                         # "tamil mei character" % mei_char)
    # if uyir_char not in uyir_letters:
        # raise ValueError("Passed input character '%s' is not a"
                         # "tamil uyir character" % uyir_char)
    # uyiridx = uyir_letters.index(uyir_char)
    # meiidx = grantha_mei_letters.index(mei_char)
    # # calculate uyirmei index 
    # uyirmeiidx = meiidx*12 + uyiridx
    # return grantha_uyirmei_letters[uyirmeiidx]

# Tamil Letters
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
# ஶ ஶா ஶி ஶீ 	ஶு 	ஶூ 	ஶெ 	ஶே 	ஶை ஶொ ஶோ ஶௌ
# ஜ ஜா ஜி ஜீ ஜு ஜூ ஜெ ஜே ஜை ஜொ ஜோ ஜௌ 
# ஷ ஷா ஷி ஷீ ஷு ஷூ ஷெ ஷே ஷை ஷொ ஷோ ஷௌ 
# ஸ ஸா ஸி ஸீ ஸு ஸூ ஸெ ஸே ஸை ஸொ ஸோ ஸௌ 
# ஹ ஹா ஹி ஹீ ஹு ஹூ ஹெ ஹே ஹை ஹொ ஹோ ஹௌ
# க்ஷ க்ஷா க்ஷி க்ஷீ க்ஷு க்ஷூ க்ஷெ க்ஷே க்ஷை க்ஷொ க்ஷோ க்ஷௌ
