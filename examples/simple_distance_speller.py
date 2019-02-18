# -*- coding: utf-8 -*-
from ngram.Distance import edit_distance

def get_min_distance_alternate( pizhai ):
    agarathi_sorkal = [u'அவிழ்',u'அவல்',u'அவள்',u'தவில்',u'தவள்']
    distances = map( lambda w: edit_distance( pizhai, w) , agarathi_sorkal )
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

pizhai_sorkal = [u'ஏவள்', u'இவல்']
for pizhai in pizhai_sorkal:
    alternate = get_min_distance_alternate( pizhai )
    print(u"%s => %s"%(pizhai,u",".join(alternate)))
