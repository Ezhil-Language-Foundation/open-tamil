from django.shortcuts import render
from django.http import HttpResponse
import tamil
import codecs
import sys
import copy
import math
import re
from tamil.utf8 import get_letters
from tamil import wordutils, utf8
from spell import Speller, LoadDictionary
from solthiruthi.datastore import TamilTrie, DTrie, Queue
from solthiruthi.Ezhimai import *
from solthiruthi.resources import DICTIONARY_DATA_FILES
from solthiruthi.data_parser import *
from solthiruthi.dictionary import *
from solthiruthi.datastore import DTrie
from transliterate import azhagi, jaffna, combinational, algorithm
from ngram.Corpus import Corpus
from ngram import LetterModels
from ngram.LetterModels import *
from ngram.WordModels import *
from tamil.txt2unicode import *
import tamil.utf8 as utf8
def index(request):
    return render(request,'first.html',{})
def vaypaadu(request):
    return render(request,'vaypaadu.html',{})
def trans(request):
     return render(request,'translite.html',{})
def uni(request):
     return render(request,'unicode.html',{})
def keechu(request):
     return render(request,'keechu.html',{})
def spl(request):
     return render(request,'spell.html',{})
def rev(request):
     return render(request,'reverse.html',{})
def num(request):
     return render(request,'number.html',{})
def anag(request):
     return render(request,'anagram.html',{})
def unig(request):
     return render(request,'unigram.html',{})
def ngra(request):
     return render(request,'ngram.html',{})
def numstr(request,num):
    typ=request.GET.get("type")
    if num.find(".")==-1:
       num=int(num)
    else:
       num=float(num)
    if typ=='IN':
       out=tamil.numeral.num2tamilstr( num )
    else:
        out=tamil.numeral.num2tamilstr_american(num)
    data = { "result" : out}
    json_string = json.dumps(data,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response
def unicod(request,tsci):
    cod=request.GET.get("cod")
    if cod =='t2u':
       out=tamil.tscii.convert_to_unicode(tsci)
    elif cod=='u2t':  
         temp=tsci.decode('utf-8')
         out=unicode2tscii(temp)
    data = { "result" : out}
    json_string = json.dumps(data,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response
def keech(request,k1):
    dic={}
    for idx,kk in enumerate(k1.split(' ')):
            idx_len = len( get_letters(kk) )
            #print('w# ',idx, idx_len )
            dic[idx]=idx_len
    json_string = json.dumps(dic,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response
def translite(request,tan):
    tamil_tx=algorithm.Iterative.transliterate(azhagi.Transliteration.table,tan)
    data = { "result" : tamil_tx}
    json_string = json.dumps(data,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response
def spell_check(request,k1):
    speller =  Speller(lang=u"TA",mode="web")
    notok,suggs = speller.check_word_and_suggest( k1 )
    json_string = json.dumps(suggs,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response
def test_ngram(request,ng):
    obj = DTrie()
    prev_letter = u''
            # per-line processor - remove spaces
    for char in u"".join(re.split('\s+',ng)).lower():
        if prev_letter.isalpha() and char.isalpha():
           bigram = u"".join([prev_letter,char])
           obj.add(bigram)
                # update previous
        prev_letter = char
    actual = obj.getAllWordsAndCount()
    json_string = json.dumps(actual,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response
def anagram(request,word):
    AllTrueDictionary = wordutils.DictionaryWithPredicate(lambda x: True)
    TVU,TVU_size = DictionaryBuilder.create(TamilVU)
    length = len(utf8.get_letters(word))
    actual =list(wordutils.anagrams(word,TVU))
    json_string = json.dumps(actual,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response 
def test_basic(request,word):
    n=request.GET.get("n")
    t=get_ngram_groups( word, int(n))
    json_string = json.dumps(t,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response  
def revers(request,word):
    t=tamil.utf8.reverse_word(word)
    json_string = json.dumps(t,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response
