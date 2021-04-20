# * coding: utf8 *
#
# (C) 2020 Muthiah Annamalai <ezhillang@gmail.com>
#
# Uses the IIT-Bombay service on the web.
#

import json
import requests
from urllib.parse import quote
from functools import lru_cache


@lru_cache(1024, str)
def en2ta(text):
    """translate from English to Tamil"""
    return IITB_translator("en", "ta", text)


@lru_cache(1024, str)
def ta2en(text):
    """translate from Tamil to English"""
    return IITB_translator("ta", "en", text)


def IITB_translator(src_lang, dest_lang, _text):
    text = quote(_text)
    URLFMT = "http://www.cfilt.iitb.ac.in/indicnlpweb/indicnlpws/translate/{0}/{1}/{2}/"
    url = URLFMT.format(src_lang.lower(), dest_lang.lower(), text)
    response = requests.get(url)
    return response.json()[dest_lang.lower()]


if __name__ == "__main__":
    print(ta2en("கவிதை மிக அழகாக இருக்கிறது"))
    print(en2ta("world is not flat"))
