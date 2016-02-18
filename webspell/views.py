## -*- coding: utf-8 -*-
## (C) 2016 Muthiah Annamalai,

from webspell import app
import json
import codecs

from flask import request, render
from spell import Speller, LoadDictionary

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

#/spell?word=%E0%AE%B5%E0%AE%B0%E0%AF%81%E0%AE%95&lang=ta
# 
@app.route('/spell',methods=['GET'])
def spell():
    if u'word' in request.args:
        word = request.args['word']
        if "lang" in request.args:
            lang = request.args["lang"]
        
        ok,suggs = Speller(lang=lang,mode="web").REST_interface(word)
        if ok:
            return "<B style='color:green;'>OK!</B>"
        return "<B style='color:red;'>Not OK!</B>"+suggs
    return 'spell check with ?word=$word&lang=en'

@app.route('/spellchecker',methods=['GET','POST'])
def spellchecker():
    if request.method == 'POST':
        method = request.form['method']
        lang = request.form['lang']
        text = request.form['text']
        return "None!"
    else:
        return "Spell Checker!"
