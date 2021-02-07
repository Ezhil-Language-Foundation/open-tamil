from tamil.txt2unicode import *
from transliterate import ISO, algorithm
import tamil

def unicode_converter(tsci, cod):
    out = ""
    if cod == "t2u":
        out = tamil.tscii.convert_to_unicode(tsci)
    elif cod == "u2t":
        temp = str(tsci)
        out = unicode2tscii(temp)
    elif cod == "an2u":
        temp = str(tsci)
        out = encode2unicode.anjal2unicode(temp)
    elif cod == "bam2u":
        temp = str(tsci)
        out = encode2unicode.bamini2unicode(temp)
    elif cod == "boom2u":
        temp = str(tsci)
        out = encode2unicode.boomi2unicode(temp)
    elif cod == "karan2u":
        temp = str(tsci)
        out = encode2unicode.dinakaran2unicode(temp)
    elif cod == "thanthy2u":
        temp = str(tsci)
        out = encode2unicode.dinathanthy2unicode(temp)
    elif cod == "kavi2u":
        temp = str(tsci)
        out = encode2unicode.kavipriya2unicode(temp)
    elif cod == "mura2u":
        temp = str(tsci)
        out = encode2unicode.murasoli2unicode(temp)
    elif cod == "mylai2u":
        temp = str(tsci)
        out = encode2unicode.mylai2unicode(temp)
    elif cod == "nakk2u":
        temp = str(tsci)
        out = encode2unicode.nakkeeran2unicode(temp)
    elif cod == "roman2u":
        temp = str(tsci)
        out = encode2unicode.roman2unicode(temp)
    elif cod == "tab2u":
        temp = str(tsci)
        out = encode2unicode.tab2unicode(temp)
    elif cod == "tam2u":
        temp = str(tsci)
        out = encode2unicode.tam2unicode(temp)
    elif cod == "indoweb2u":
        temp = str(tsci)
        out = encode2unicode.indoweb2unicode(temp)
    elif cod == "koeln2u":
        temp = str(tsci)
        out = encode2unicode.koeln2unicode(temp)
    elif cod == "libi2u":
        temp = str(tsci)
        out = encode2unicode.libi2unicode(temp)
    elif cod == "oldvikatan2u":
        temp = str(tsci)
        out = encode2unicode.oldvikatan2unicode(temp)
    elif cod == "webulagam2u":
        temp = str(tsci)
        out = encode2unicode.webulagam2unicode(temp)
    elif cod == "auto2u":
        temp = str(tsci)
        result = []
        out = encode2unicode.auto2unicode(temp, result)
        out += "<BR/><B>Encoding={0}</B><BR/>".format(result)
    elif cod == "dinamani2u":
        temp = str(tsci)
        out = encode2unicode.dinamani2unicode(temp)
    elif cod == "pallavar2u":
        temp = str(tsci)
        out = encode2unicode.pallavar2unicode(temp)
    elif cod == "diacritic2u":
        temp = str(tsci)
        out = encode2unicode.diacritic2unicode(temp)
    elif cod == "shreelipi2u":
        temp = str(tsci)
        out = encode2unicode.shreelipi2unicode(temp)
    elif cod == "softview2u":
        temp = str(tsci)
        out = encode2unicode.softview2unicode(temp)
    elif cod == "tace2u":
        temp = str(tsci)
        out = encode2unicode.tace2unicode(temp)
    elif cod == "vanavil2u":
        temp = str(tsci)
        out = encode2unicode.vanavil2unicode(temp)
    elif cod == "indica2u":
        temp = str(tsci)
        out = encode2unicode.indica2unicode(temp)
    elif cod == "anu2u":
        temp = str(tsci)
        out = encode2unicode.anu2unicode(temp)
    elif cod == "shreelipiavid2u":
        temp = str(tsci)
        out = encode2unicode.shreelipiavid2unicode(temp)
    elif cod == "unicode2anjal":
        temp = str(tsci)
        out = unicode2encode.unicode2anjal(temp)
    elif cod == "unicode2bamini":
        temp = str(tsci)
        out = unicode2encode.unicode2bamini(temp)
    elif cod == "unicode2boomi":
        temp = str(tsci)
        out = unicode2encode.unicode2boomi(temp)
    elif cod == "unicode2dinakaran":
        temp = str(tsci)
        out = unicode2encode.unicode2dinakaran(temp)
    elif cod == "unicode2dinathanthy":
        temp = str(tsci)
        out = unicode2encode.unicode2dinathanthy(temp)
    elif cod == "unicode2kavipriya":
        temp = str(tsci)
        out = unicode2encode.unicode2kavipriya(temp)
    elif cod == "unicode2murasoli":
        temp = str(tsci)
        out = unicode2encode.unicode2murasoli(temp)
    elif cod == "unicode2mylai":
        temp = str(tsci)
        out = unicode2encode.unicode2mylai(temp)
    elif cod == "unicode2nakkeeran":
        temp = str(tsci)
        out = unicode2encode.unicode2nakkeeran(temp)
    elif cod == "unicode2roman":
        temp = str(tsci)
        out = unicode2encode.unicode2roman(temp)
    elif cod == "unicode2tab":
        temp = str(tsci)
        out = unicode2encode.unicode2tab(temp)
    elif cod == "unicode2tam":
        temp = str(tsci)
        out = encode2unicode.unicode2tam(temp)
    elif cod == "unicode2indoweb":
        temp = str(tsci)
        out = unicode2encode.unicode2indoweb(temp)
    elif cod == "unicode2koeln":
        temp = str(tsci)
        out = unicode2encode.unicode2koeln(temp)
    elif cod == "unicode2libi":
        temp = str(tsci)
        out = unicode2encode.unicode2libi(temp)
    elif cod == "unicode2oldvikatan":
        temp = str(tsci)
        out = unicode2encode.unicode2oldvikatan(temp)
    elif cod == "unicode2webulagam":
        temp = str(tsci)
        out = unicode2encode.unicode2webulagam(temp)
    elif cod == "unicode2dinamani":
        temp = str(tsci)
        out = unicode2encode.unicode2dinamani(temp)
    elif cod == "unicode2pallavar":
        temp = str(tsci)
        out = unicode2encode.unicode2pallavar(temp)
    elif cod == "unicode2diacritic":
        temp = str(tsci)
        out = unicode2encode.unicode2diacritic(temp)
    elif cod == "unicode2shreelipi":
        temp = str(tsci)
        out = unicode2encode.unicode2shreelipi(temp)
    elif cod == "unicode2softview":
        temp = str(tsci)
        out = unicode2encode.unicode2softview(temp)
    elif cod == "unicode2tace":
        temp = str(tsci)
        out = unicode2encode.unicode2tace(temp)
    elif cod == "unicode2vanavil":
        temp = str(tsci)
        out = unicode2encode.unicode2vanavil(temp)
    elif cod == "unicode2indica":
        temp = str(tsci)
        out = unicode2encode.unicode2indica(temp)
    elif cod == "unicode2anu":
        temp = str(tsci)
        out = unicode2encode.unicode2anu(temp)
    elif cod == "unicode2shreelipiavid":
        temp = str(tsci)
        out = unicode2encode.unicode2shreelipiavid(temp)
    elif cod=="ISO2unicode":
        temp = str(tsci)
        ISO_table = ISO.Transliteration.table
        top,result = algorithm.Greedy.transliterate(ISO_table,temp)
        #print(result.options)
        out = list(result.options)[0]
        #TODO/alternative option.
        #out = algorithm.Direct.transliterate(ISO_table,temp)
        #join uyir mei.
    elif cod=="unicode2ISO":
        temp = str(tsci)
        ISO_table = ISO.ReverseTransliteration.table
        out = algorithm.Direct.transliterate(ISO_table,temp)
    data = {"result": out}
    return data
