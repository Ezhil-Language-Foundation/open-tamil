## -*- coding: utf-8 -*-
## (C) 2016 Muthiah Annamalai,

from webspell import app
import json
import codecs

from flask import request, render_template, redirect, url_for
from spell import Speller, LoadDictionary

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

#/spell?word=%E0%AE%B5%E0%AE%B0%E0%AF%81%E0%AE%95&lang=ta
# 
@app.route('/spell',methods=['GET','POST'])
def spell():
    if request.method == "GET":
        return render_template("spell.html",solution=False)
    
    if request.method != "POST":
        return "<B>404! Error</B>"
        
    if u'word' in request.form:
        word = request.form['word']
        if not word:
            return "Enter word!"
        lang="TA"
        if "lang" in request.form:
            lang = request.form["lang"]
        
        ok,suggs = Speller(lang=lang,mode="web").REST_interface(word)
        if ok:
            HTML = "<B style='color:green;'>OK!</B>"
        else:
            data_suggs = json.loads(suggs)
            data_suggs2 = u"<br/>\n".join( [u"<option>%d %s</option>"%(itr+1,s_word) for itr,s_word in enumerate( data_suggs.values()[0])])
            HTML = "<B style='color:red;'>Not OK!</B><br /><select>"+data_suggs2+"\n</select><br/>"
        return render_template("spell.html",solution=True,HTML=HTML,word=word)
    return redirect(url_for('spell'))
    
def spell_get_only():
    if u'word' in request.args:
        word = request.args['word']
        if not word:
            return "Enter word!"
        lang="TA"
        if "lang" in request.args:
            lang = request.args["lang"]
        
        ok,suggs = Speller(lang=lang,mode="web").REST_interface(word)
        if ok:
            return "<B style='color:green;'>OK!</B>"
        data_suggs = json.loads(suggs)
        data_suggs2 = u"<br/>\n".join( [u"%d %s"%(itr+1,s_word) for itr,s_word in enumerate( data_suggs.values()[0])])
        return "<B style='color:red;'>Not OK!</B><br />"+data_suggs2+"\n<br/>"+suggs
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
