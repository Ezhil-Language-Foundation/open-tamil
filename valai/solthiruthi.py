# * coding: utf8 *
#
# (C) 2019 Muthiah Annamalai <ezhillang@gmail.com>
#
#  This file provides a REST API interface to Tamil spelling checker
#  written in compliance
#

import requests
from collections import namedtuple
import re

Result = namedtuple("Result", ["word", "alternatives"])

BASEURL = "http://tamilpesu.us:7000/spellchecker"
from pprint import pprint


class SpellChecker:
    def __init__(self, apikey="XXXXX", _baseurl=None):
        self._apikey = apikey
        self._baseurl = BASEURL if not _baseurl else _baseurl

    def check_word(self, words: list, lang_code="ta_IN"):
        """HTTP POST request parameters.
        1. lang  : language code - ta_IN is only supported now.
        2. text  : string formed by words separated by '\n' character
        """
        if not isinstance(words, list):
            words = re.split("\s+", words)
        response = requests.post(
            self._baseurl, data={"text": u"\n".join(words), "lang": lang_code}
        )
        if not response.ok:
            raise Exception(
                u"தகவல் சேவை துண்டிக்கப்பட்டது அல்லது இணைப்பு துண்டிக்கப்பட்டது"
            )
        result_words = response.json()["words"]
        results = []
        for word, alternates in result_words.items():
            results.append(Result(word=word, alternatives=alternates))
        return results


if __name__ == "__main__":
    pprint(SpellChecker().check_word(u"வாணி என்பது ஒரு"))
