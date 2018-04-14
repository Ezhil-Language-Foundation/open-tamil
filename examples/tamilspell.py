#!python
# -*- coding: utf-8 -*-
#(C) 2016-2018 Muthiah Annamalai
import sys
try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3


reload(sys)
sys.setdefaultencoding('utf-8')

#This file is part of open-tamil package
import spell

if __name__ == u"__main__":
    spell.main()
