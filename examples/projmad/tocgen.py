# -*- coding: utf-8 -*-
# (C) 2016 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package examples
# We find the TOC for Project-Madurai tags
# e.g.
# <tr>
#		<td >31</td>
#		<td >திருவருட்பா /அகவல்</td>
#		<td >இராமலிங்க அடிகள்</td>
#		<td ></td>
#		<td ><a href="/pm_etexts/pdf/pm0031.pdf">pm0031.pdf</a><br/> </td>
#		<td ><a href="/pm_etexts/utf8/pmuni0031.html">pmuni0031.html</a><br/> </td>
#		<td ><a href="/pm_etexts/kindlepdf/pmkindle0031.pdf">pmkindle0031.pdf</a><br/> </td>
#	</tr>

import tamil
import codecs
import sys
import collections
import BeautifulSoup
import json

if BeautifulSoup.__version__.find("3.") != 0:
    print("Error: this program requires BeautifulSoup v3.x.x series (e.g. 3.2.1)")
    sys.exit(-1)

MaduraiBook = collections.namedtuple('MaduraiBook',\
['title','author','genre','url_pdf','url_html'])

url = u"http://projectmadurai.org/pmworks.html"

try:
    page =  codecs.open('pmworks.html','r','utf-8')
except Exception as ioe:
    print(u"Cannot find file: pmworks.html; please download the file from %s"%url)

booklist = []
bookcoll = []
bsobj = BeautifulSoup.BeautifulSoup( page )
book_tags = list(bsobj('tr'))
nbooks_appx = len(book_tags)
print(u"Number of TR tags =>",nbooks_appx)

genre_set = set()
author_set = set()

# Sanity check
assert( nbooks_appx >= 550 ) # We expected atleast 550 books or more
for pos,book_tag in enumerate(book_tags):
    try:
        td_tags=  book_tag('td')
    except Exception as ie:
        td_tags = []
    if len(td_tags) < 7:
        print("Skipping tag @ %d"%pos)
        continue
    # skip first tag - its enumeration
    b_title = td_tags[1].string
    b_author = td_tags[2].string
    b_genre = td_tags[3].string
    if not b_author:
        b_author = u"Unknown"
    if not b_genre:
        b_genre = u"Uncategorized"
    b_url_pdf = {}
    for anchor in td_tags[4]('a'):
        if anchor.string:
            b_url_pdf[anchor.string] = anchor['href'] 
    b_url_html = {}
    for anchor in td_tags[5]('a'):
        if anchor.string: 
            b_url_html[anchor.string] = anchor['href'] 
    
    book = MaduraiBook( b_title, b_author, b_genre, b_url_pdf, b_url_html )
    bookcoll.append(book)
    booklist.append(book.__dict__)

for book in bookcoll:
    if len(book.author) > 0: author_set.add(book.author)
    if len(book.genre) > 0: genre_set.add(book.genre)

print("N books actual =>",len(booklist))
with codecs.open("projmad.json","w","utf-8") as fp:
    fp.write( json.dumps(booklist) )
    
with codecs.open("projmad_authors_n_genre.json","w","utf-8") as fp:
    fp.write( json.dumps( {'authors':list(author_set),'genre':list(genre_set)} ))

