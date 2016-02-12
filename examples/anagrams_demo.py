import codecs
from tamil import wordutils
from solthiruthi.dictionary import *

TVU,TVU_size = DictionaryBuilder.create(TamilVU)
ag,ag2 = wordutils.anagrams_in_dictionary(TVU)
with codecs.open(u'demo.txt','w','utf-8') as fp:
    itr = 1
    for k,c in ag:
        v = ag2[k]
        fp.write(u'%03d) %s\n'%(itr,u' | '.join(v)))
        itr += 1
