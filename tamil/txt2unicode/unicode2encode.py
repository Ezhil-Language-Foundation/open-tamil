#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
# (C) 2014 Arulalan.T <arulalant@gmail.com>                                  #
#                                                                            #
# Author : Arulalan.T <arulalant@gmail.com>                                  #
# Date : 04.08.2014                                                          #
#                                                                            #
# This file is part of open-tamil/txt2uni                                    #
#                                                                            #
# txt2unicode is free software: you can redistribute it and/or               #
# modify it under the terms of the GNU General Public License as published by#
# the Free Software Foundation, either version 3 of the License, or (at your #
# option) any later version. This program is distributed in the hope that it #
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty#
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General#
# Public License for more details. You should have received a copy of the GNU#
# General Public License along with this program. If not, see                #
# <http://www.gnu.org/licenses/>.                                            #
#                                                                            #
##############################################################################

from .encode2utf8 import (
    anjal2utf8,
    bamini2utf8,
    boomi2utf8,
    dinakaran2utf8,
    dinamani2utf8,
    dinathanthy2utf8,
    kavipriya2utf8,
    murasoli2utf8,
    mylai2utf8,
    nakkeeran2utf8,
    roman2utf8,
    tab2utf8,
    tam2utf8,
    tscii2utf8,
    pallavar2utf8,
    indoweb2utf8,
    koeln2utf8,
    libi2utf8,
    oldvikatan2utf8,
    webulagam2utf8,
    diacritic2utf8,
    shreelipi2utf8,
    softview2utf8,
    tace2utf8,
    vanavil2utf8,
    indica2utf8,
    anu2utf8,
    shreelipiavid2utf8,
)

from .encode2unicode import _all_encodes_, _get_unique_ch, _get_unique_common_encodes

__all__ = [
    "unicode2anjal",
    "unicode2bamini",
    "unicode2boomi",
    "unicode2dinakaran",
    "unicode2dinathanthy",
    "unicode2kavipriya",
    "unicode2murasoli",
    "unicode2mylai",
    "unicode2nakkeeran",
    "unicode2roman",
    "unicode2tab",
    "unicode2tam",
    "unicode2tscii",
    "unicode2indoweb",
    "unicode2koeln",
    "unicode2libi",
    "unicode2oldvikatan",
    "unicode2webulagam",
    "unicode2auto",
    "unicode2dinamani",
    "unicode2pallavar",
    "unicode2diacritic",
    "unicode2shreelipi",
    "unicode2softview",
    "unicode2tace",
    "unicode2vanavil",
    "unicode2indica",
    "unicode2anu",
    "unicode2shreelipiavid",
]


def unicode2encode(text, charmap):
    """
    charmap : dictionary which has both encode as key, unicode as value
    """
    if isinstance(text, (list, tuple)):
        unitxt = ""
        for line in text:
            for val, key in charmap.items():
                if key in line:
                    line = line.replace(key, val)
                # end of if val in text:
            unitxt += line
        # end of for line in text:
        return unitxt
    elif isinstance(text, str):
        for val, key in charmap.items():
            if key in text:
                text = text.replace(key, val)
        return text


def unicode2anjal(text):
    return unicode2encode(text, anjal2utf8)


def unicode2bamini(text):
    return unicode2encode(text, bamini2utf8)


def unicode2boomi(text):
    return unicode2encode(text, boomi2utf8)


def unicode2dinakaran(text):
    return unicode2encode(text, dinakaran2utf8)


def unicode2dinamani(text):
    return unicode2encode(text, dinamani2utf8)


def unicode2dinathanthy(text):
    return unicode2encode(text, dinathanthy2utf8)


def unicode2kavipriya(text):
    return unicode2encode(text, kavipriya2utf8)


def unicode2murasoli(text):
    return unicode2encode(text, murasoli2utf8)


def unicode2mylai(text):
    return unicode2encode(text, mylai2utf8)


def unicode2nakkeeran(text):
    return unicode2encode(text, nakkeeran2utf8)


def unicode2roman(text):
    return unicode2encode(text, roman2utf8)


def unicode2tab(text):
    return unicode2encode(text, tab2utf8)


def unicode2tam(text):
    return unicode2encode(text, tam2utf8)


def unicode2tscii(text):
    return unicode2encode(text, tscii2utf8)


def unicode2pallavar(text):
    return unicode2encode(text, pallavar2utf8)


def unicode2indoweb(text):
    return unicode2encode(text, indoweb2utf8)


def unicode2koeln(text):
    return unicode2encode(text, koeln2utf8)


def unicode2libi(text):
    return unicode2encode(text, libi2utf8)


def unicode2oldvikatan(text):
    return unicode2encode(text, oldvikatan2utf8)


def unicode2webulagam(text):
    return unicode2encode(text, webulagam2utf8)


def unicode2diacritic(text):
    return unicode2encode(text, diacritic2utf8)


def unicode2shreelipi(text):
    return unicode2encode(text, shreelipi2utf8)


def unicode2softview(text):
    return unicode2encode(text, softview2utf8)


def unicode2tace(text):
    return unicode2encode(text, tace2utf8)


def unicode2vanavil(text):
    return unicode2encode(text, vanavil2utf8)


def unicode2indica(text):
    return unicode2encode(text, indica2utf8)


def unicode2anu(text):
    return unicode2encode(text, anu2utf8)


def unicode2shreelipiavid(text):
    return unicode2encode(text, shreelipiavid2utf8)


def unicode2auto(unicode_text, encode_text):
    """
    This function will convert unicode (first argument) text into other
    encodes by auto find the encode (from available encodes) by using sample
    encode text in second argument of this function.

    unicode_text : Pass unicode string which has to convert into other encode.
    encode_text : Pass sample encode string to identify suitable encode for it.

    This function tries to identify encode in available encodings.
    If it finds, then it will convert unicode_text into encode string.

    Author : Arulalan.T

    08.08.2014

    """

    _all_unique_encodes_, _all_common_encodes_ = _get_unique_common_encodes()
    # get unique word which falls under any one of available encodes from
    # user passed text lines
    unique_chars = _get_unique_ch(encode_text, _all_common_encodes_)
    # count common encode chars
    clen = len(_all_common_encodes_)
    msg = "Sorry, couldn't find encode :-(\n"
    msg += "Need more words to find unique encode out side of %d " % clen
    msg += "common compound characters"
    if not unique_chars:
        print(msg)
        return ""
    # end of if not unique_chars:

    for encode_name, encode_keys in _all_unique_encodes_:
        if not len(encode_keys):
            continue
        for ch in encode_keys:
            # check either encode char is presnent in word
            if ch in unique_chars:
                # found encode
                print(("Found encode : ", encode_name))
                encode = _all_encodes_[encode_name]
                return unicode2encode(unicode_text, encode)
            # end of if ch in unique_chars:
        # end of ifor ch in encode_keys:
    else:
        print(msg)
        return ""
    # end of for encode in _all_unique_encodes_:

# end of def auto2unicode(text):
