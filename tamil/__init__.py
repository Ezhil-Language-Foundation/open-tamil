# * coding: utf8 *
# 
# (C) 2013-2015 Muthiah Annamalai <ezhillang@gmail.com>
# Library provides various encoding services for Tamil libraries

from . import utf8
from . import tscii

from . import txt2unicode
from . import txt2ipa
from . import numeral
from . import regexp
from . import wordutils

VERSION = '0.4'
__all__ = ['utf8','txt2unicode','num2tamilstr','txt2unicode','txt2ipa','numeral','regexp']
