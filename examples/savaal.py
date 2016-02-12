# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests

import tamil
import solthiruthi
from solthiruthi.dictionary import *

TVU_dict,_ = DictionaryBuilder.create(TamilVU)
word = u'சவால்’'
q=list(tamil.wordutils.combinagrams(word,TVU_dict))
print(u'|'.join(q))
