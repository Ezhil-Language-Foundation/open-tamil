# * coding: utf8 *
# 
# (C) 2013-2015, 2017-2019 Muthiah Annamalai <ezhillang@gmail.com>
# Library provides various encoding services for Tamil libraries

from . import utf8
from . import tscii
from . import tweetparser

from . import txt2unicode
from . import txt2ipa
from . import numeral
from . import regexp
from . import wordutils
from . import utils

VERSION = '0.96'
__all__ = ['utf8','txt2unicode','numeral','txt2unicode','txt2ipa','numeral','regexp','utils','wordutils']
