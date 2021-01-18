# * coding: utf8 *
#
# (C) 2019 Muthiah Annamalai <ezhillang@gmail.com>
#
#  This file provides a REST API interface to Tamil spelling checker
#  written in compliance with Vaani solthiruthi protocol by Neechalkaran.
#
#  You may also use this by obtaining the correct URL and authorized APIKEY
#  from Neechalkaran.com
#

import requests
from collections import namedtuple
import re

Result = namedtuple("Result", ["Flag", "Solspan", "Userword", "Suggestions"])

# Will be revealed in due course of time.
BASEURL = "#########################################"


class SpellChecker:
    def __init__(self, apikey="XXXXX", _baseurl=None):
        self._apikey = apikey
        self._baseurl = BASEURL if not _baseurl else _baseurl

    def check_word(self, words: list, sandhi=False, translated=False):
        """HTTP Get request parameters.
        1. tamilwords -> each words need to be separated with single pipe |. sentence are separated by double pipe ||string|Required
        2. apikey -> Valid apikey|string|Required
        3. sandhi -> Default value is true. It needs to be set false, if sandhi suggestions are not required |Boolean|optional
        4. translated -> Default value is true. It needs to be set false, if foreign words do not need relevant Tamil word|Boolean|optional

        Resource Result Description
        Collection of Sol
        1. Flag -> It returns the result of the word|boolean|None.
        2. solspan -> User Words count for the suggested word. When multiple consecutive words have single suggestion, Then it will be useful.|numeric|
        3. Userword -> It returns the given word|string|None.
        4. Suggestions -> If the flag is wrong, then it gives the suggestion based on available algorithm|string|None.
        """
        if not isinstance(words, list):
            words = re.split("\s+", words)
        response = requests.get(
            self._baseurl,
            params={
                "tamilwords": u"|".join(words),
                "apikey": self._apikey,
                "sandhi": sandhi,
                "translated": translated,
            },
        )
        if not response.ok:
            raise Exception(
                u"தகவல் சேவை துண்டிக்கப்பட்டது அல்லது இணைப்பு துண்டிக்கப்பட்டது"
            )
        return [Result(**r) for r in response.json()]


if __name__ == "__main__":
    from pprint import pprint

    pprint(SpellChecker().check_word(u"வாணி என்பது ஒரு சொற்பிழைத்திருத்தி"))
