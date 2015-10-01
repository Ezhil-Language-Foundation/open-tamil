# -*- coding: utf8 -*-
# This file is distributed under MIT License
# 2015 Muthiah Annamalai <ezhillang@gmail.com>
#

import time
import os
import sys
import tamil
import winsound
import wave
    
def concat_audio_files(infiles,outfile):
    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for itr in range(len(infiles)):
        output.writeframes(data[itr][1])
    output.close()
    return

def say_number_in_tamil(number,voice_gender='female'):
    if number < 0:
        raise Exception("Negative numbers are not supported")
    
    # 1) Generate the numeral for number
    actual_fn = []
    numeral = tamil.numeral.num2tamilstr( number, actual_fn )
    
    # 2) Find the relevant audio file
    infiles = []
    for fn in actual_fn:
        infiles.append( os.path.join('data','audio',voice_gender,fn+'.wav') )
    
    # 3) Generate a single audio file
    outfile = "audio_"+str(number).replace(".","_")+".wav"
    concat_audio_files(infiles,outfile)
    
    # 4) Play this newly created audio file
    winsound.PlaySound(outfile,winsound.SND_NOSTOP)
    return

while True:
    number = input(u'Enter a number >> ') 
    say_number_in_tamil( number )

sys.exit(0)

# numerale = u'ஓர் ஆயிரம் புள்ளி நான்கு ஐந்து'
# filenames = ['one_thousand_prefix','thousands_0','pulli','units_4','units_5']
# # ideally compose the audio stream and run some kind of smoothing filter
# for fn in filenames:
    # winsound.PlaySound(os.path.join('data','audio','female',fn+'.wav'),winsound.SND_NOSTOP) #winsound.SND_ASYNC)
