#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import tamil
import codecs
import sys
import copy
import math
import re
import cgi
import json
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
import tamil.utf8 as utf8
from tamilsandhi.sandhi_checker import check_sandhi
from .tamilwordgrid import generate_tamil_word_grid
from .webuni import unicode_converter
import random

#try:
import tamilmorse
#except ImportError as ioe:
#   print("tamilmorse library not imported")
#   pass

PYTHON26 = sys.version.find('2.6') >= 0
if not PYTHON26:
   from classifier import process_word

try: 
   from tamiltts import ConcatennativeTTS
except Exception as ioe:
   pass

if sys.version_info[0]<3:
   reload(sys)
   sys.setdefaultencoding('utf8')
def index(request):
    return render(request,'first.html',{"PYTHON26":PYTHON26})
def vaypaadu(request):
    return render(request,'vaypaadu.html',{"PYTHON26":PYTHON26})
def trans(request):
     return render(request,'translite.html',{"PYTHON26":PYTHON26})
def uni(request):
     return render(request,'unicode.html',{"PYTHON26":PYTHON26})
def keechu(request):
     return render(request,'keechu.html',{"PYTHON26":PYTHON26})
def spl(request):
     return render(request,'spell.html',{"PYTHON26":PYTHON26})
def rev(request):
     return render(request,'reverse.html',{"PYTHON26":PYTHON26})
def morse_code(request):
     return render(request,'morse.html',{"PYTHON26":PYTHON26})
def num(request):
     return render(request,'number.html',{"PYTHON26":PYTHON26})
def anag(request):
     return render(request,'anagram.html',{"PYTHON26":PYTHON26})
def unig(request):
     return render(request,'unigram.html',{"PYTHON26":PYTHON26})
def ngra(request):
     return render(request,'ngram.html',{"PYTHON26":PYTHON26})
def sandhi_check(request):
     return render(request,'sandhi_check.html',{"PYTHON26":PYTHON26})

if not PYTHON26:
   def get_classify(request):
      return render(request,'classifier.html',{"PYTHON26":PYTHON26})

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
    data=unicode_converter(tsci,cod)
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
@csrf_exempt
def call_sandhi_check(request):
    k1= cgi.escape(request.POST.get('tamiltext',u'அங்குக் கண்டான் அந்த பையன் எத்தனை பழங்கள் '))
    print(k1)
    dic={}
    temp=u""
    dic['old']=k1
    text,res=check_sandhi(k1)
    for i,j in enumerate(k1.split()):
       try:
          if j!=text[i]:
             text[i]="<span class='highlight'>"+text[i]+"</span>"
       except IndexError:
              pass
    dic['new']=u" ".join(text)
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

def morse(request,direction="encode",word=""):
   if direction.lower().find("encode") >= 0:
      fn = tamilmorse.encode
   else:
      fn = tamilmorse.decode
   json_string = json.dumps( fn(word), ensure_ascii = False )
   print json_string
   response = HttpResponse( json_string, content_type="application/json; charset=utf-8" )
   return response

#TBD:
#def sorttamil(request):

#TBD:
#def synthesize_number(request):

#TBD:
#def kalsee_on_web(request):

def tts_demo(request):
   if request.method == "GET":
      return render(request,"tts_demo.html",{'solution':u'','PYTHON26':PYTHON26})
   assert( request.method == "POST" )
   words = request.POST.get("words",u"")
   mp3path = os.path.join('static',u"audio_%d.mp3"%random.randint(0,1000000))
   static_path = os.path.join(os.path.split(__file__)[0],mp3path)
   tts = ConcatennativeTTS(words,static_path)
   tts.run()
   return render(request,"tts_demo.html",{'solution':mp3path,'PYTHON26':PYTHON26})

def xword(request):
   if request.method == "GET":
      return render(request,'xword.html',{'solution':u'','PYTHON26':PYTHON26})
   assert( request.method == "POST" )
   words = request.POST.get("words",[])
   wordlist = filter(len,[ w.strip() for w in re.split(u"\n+",words) ])
   grid,sol = generate_tamil_word_grid(wordlist)
   return render(request,'xword.html',{'solution':grid,'wordlist':wordlist,'PYTHON26':PYTHON26})

def summarizer(request):
   if request.method == "GET":
      return render(request,'summarizer.html',{'text_input':u'','PYTHON26':PYTHON26})
   assert( request.method == "POST" )
   text_input = request.POST.get("text_input",u"")
   
   # Create a SummaryTool object
   st = tamil.utils.SummaryTool()
   
   # Build the sentences dictionary
   sentences_dic = st.get_sentences_ranks(text_input)
   title = u"தமிழ் பேசு.us:"
   # Build the summary with the sentences dictionary
   text_summary = st.get_summary(title, text_input, sentences_dic)
   in_w = len(tamil.utf8.get_words(text_input))
   out_w = len(tamil.utf8.get_words(text_summary))
   text_comments = u"உள்ளீடு அளவு: %d சொற்கள், வெளியீடு அளவு: %d சொற்கள். சுருக்கம் %3.3g.\n"%(in_w,out_w,in_w/(1.0*out_w))
   return render(request,u'summarizer.html',{'text_input':text_input,"text_summary":text_summary,"text_comments":text_comments,'PYTHON26':PYTHON26})
def classify_word(request):
    word=request.GET.get('tamiltext')
    result=process_word(word)
    data = { "result" : result}
    json_string = json.dumps(data,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string,content_type="application/json; charset=utf-8" )
    return response

