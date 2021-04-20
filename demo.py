# -*- coding: utf-8 -*-
## (C) 2019 Muthiah Annamalai,
## This module is part of solthiruthi project under open-tamil umbrella.
## This code maybe used/distributed under MIT LICENSE.
from solthiruthi.dictionary import DictionaryBuilder, TamilVU
from solthiruthi.qwertykbd import confusion_matrix as en_kbd_cm
from solthiruthi.tamil99kbd import inv_confusion_matrix as kbd_cm
from solthiruthi.typographical import oridam_generate_patterns, corrections

TVU, _ = DictionaryBuilder.create(TamilVU)


def checkpat(word_in, check_words, kbd=en_kbd_cm):
    pat = oridam_generate_patterns(word_in, kbd, ed=len(word_in))
    pat = ["".join(p) for p in pat]
    print("Total = %d" % (len(pat)))
    print("Total set = %d" % len(set(pat)))
    for word in check_words:
        print('%s ->' % word, word in pat)
    for p in pat:
        print(p)


# checkpat(list('arg'),['art','arg'])
# checkpat(get_letters(u'பவளம்'),[u'பவகல்',u'கவளம்'],kbd_cm)
# checkpat(get_letters(u'அன்பம்'),[u'இன்பம்'],kbd_cm)
wl = corrections('அன்பம்', TVU, kbd_cm, ed=2)
for c in wl:
    print(("u'%s'," % c))
print(("L = %d" % len(wl)))
