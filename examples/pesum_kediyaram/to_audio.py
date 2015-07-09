# -*- coding: utf8 -*-
# This file is distributed under MIT License
# 2015 Muthiah Annamalai <ezhillang@gmail.com>
#

import time
import os
import sys
import tamil
import winsound

while True:
    number = input(u'Enter a number >> ') 
    actual_fn = []
    numeral = tamil.numeral.num2tamilstr( number, actual_fn )
    for fn in actual_fn:
        winsound.PlaySound(os.path.join('data','audio','female',fn+'.wav'),winsound.SND_NOSTOP)

sys.exit(0)

numerale = u'ஓர் ஆயிரம் புள்ளி நான்கு ஐந்து'
filenames = ['one_thousand_prefix','thousands_0','pulli','units_4','units_5']
# ideally compose the audio stream and run some kind of smoothing filter
for fn in filenames:
    winsound.PlaySound(os.path.join('data','audio','female',fn+'.wav'),winsound.SND_NOSTOP) #winsound.SND_ASYNC) #
