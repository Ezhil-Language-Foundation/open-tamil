# * coding: utf8 *
# 
# (C) 20132015 Muthiah Annamalai <ezhillang@gmail.com>
# Library provides various encoding services for Tamil libraries

from . import utf8
from . import tscii

from . import txt2unicode
from . import txt2ipa
from . import numeral
from . import regexp

__all__ = ['utf8','txt2unicode','num2tamilstr','txt2unicode','txt2ipa','numeral','regexp']