# -*- coding: utf-8 -*-
from ngram.Distance import edit_distance

def get_min_distance_alternate( pizhai ):
    agarathi_sorkal = ['அவிழ்','அவல்','அவள்','தவில்','தவள்']
    distances = [edit_distance( pizhai, w) for w in agarathi_sorkal]
    print(distances)
    m = min(distances)
    idx = -1
    matches = []
    while True:
        old_idx = idx
        try:
            idx = distances.index(m,1+old_idx,len(distances))
        except ValueError:
            break
        matches.append( agarathi_sorkal[idx] )
    return matches

pizhai_sorkal = ['ஏவள்', 'இவல்']
for pizhai in pizhai_sorkal:
    alternate = get_min_distance_alternate( pizhai )
    print(("%s => %s"%(pizhai,",".join(alternate))))
