# This code is part of Open-Tamil project.
# இந்த நிரல் பொது உரிமத்தின் கீழ் வழங்கப்படுகிறது.
#
# Parse word list from Monier Williams Sanskrit Dictionary due to
# Prof. Prem Pahlajrai, and  IITS - Cologne Digital Sanskrit Lexicon
# University of Cologne (Universität zu Köln)
# Ref: http://faculty.washington.edu/prem/mw/mw.html

from bs4 import BeautifulSoup
from glob import glob
import re


def proc_file(htmlfile):
    bullet3 = chr(8921)  # '⋙'
    bullet2 = chr(8811)  # '≫'
    with open(htmlfile, "r") as fp:
        dom = BeautifulSoup(fp, features="html.parser")
    tag = "dt"
    print(htmlfile)
    for wordTag in dom.findAll(tag):
        word = re.sub("|".join([bullet2, bullet3]), "", wordTag.text)
        word = re.sub("\d+", "", word)
        word = re.sub("\s+", "", word)
        print("\t", word)
    return


if __name__ == "__main__":
    # Vowels (14)
    # a	ā	i	ī	u	ū
    # ṛ	ṝ	ḷ	ḹ
    # e	ai	o	au
    # Consonants (non-vowels = 25+4+4 = 33)
    # k	kh	g	gh	ṅ
    # c	ch	j	jh	ñ
    # ṭ	ṭh	ḍ	ḍh	ṇ
    # t	th	d	dh	n
    # p	ph	b	bh	m
    # Semi-Vowels
    # y	r	l	v
    # Sibilants & Aspirate
    # ś	ṣ	s	h
    for _html_file in glob("*.html"):
        proc_file(_html_file)
