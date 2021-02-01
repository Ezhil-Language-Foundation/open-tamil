# -*- coding: utf-8 -*-
# (C) 2017 Muthiah Annamalai
# This file is part of open-tamil examples
# This code is released under public domain

# Ref API help from : https://scikit-learn.org
import numpy as np
import random
import string
import time, os

import joblib

# project modules
from .classifier_eng_vs_ta import jaffna_transliterate
from .preprocess import Feature

scaler = joblib.load( os.path.dirname(os.path.abspath(__file__)) + '/neuralnets/scaler.pkl' )
nn = joblib.load( os.path.dirname(os.path.abspath(__file__)) +'/neuralnets/nn.pkl' )

def process_word(s):
    if any([l in string.ascii_lowercase for l in s]):
        s = jaffna_transliterate(s)
        # print(u"Transliterated to %s"%s)
    # print(u"Checking in NN '%s'"%s)
    try:
        f = Feature.get(s)
        scaled_feature = scaler.transform(np.array(f.data()).reshape(1, -1))
        y = nn.predict(scaled_feature)
        # print( scaled_feature )
        # print( y )
        if y.ravel() > 0:
            return "%s என்பது தமிழ் வார்த்தையாக இருக்கலாம்" % s
        else:
            return "%s என்பது ஆங்கில வார்த்தையாக இருக்கலாம்" % s
    except Exception as ioe:
        return ioe.message
    return

if __name__ == "__main__":
    value=process_word('vanakkam')
    print(value)
    value=process_word('hello')
    print(value)
