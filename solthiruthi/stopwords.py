## -*- coding: utf-8 -*-
## (C) 2018 Muthiah Annamalai, <ezhillang@gmail.com>

import codecs
import os
from .resources import get_data_dir


def get_stop_words():
    stop_words = []
    with codecs.open(
        os.path.join(get_data_dir(), u"TamilStopWords.txt"), "r", "utf-8"
    ) as fp:
        stop_words = list(
            filter(lambda w: len(w) > 0, map(lambda w: w.strip(), fp.readlines()))
        )
    return stop_words
