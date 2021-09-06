import codecs

from solthiruthi.dictionary import *
from tamil import wordutils

TVU, TVU_size = DictionaryBuilder.create(TamilVU)
ag, ag2 = wordutils.anagrams_in_dictionary(TVU)
with codecs.open("demo.txt", "w", "utf-8") as fp:
    itr = 1
    for k, c in ag:
        v = ag2[k]
        fp.write("%03d) %s\n" % (itr, " | ".join(v)))
        itr += 1
