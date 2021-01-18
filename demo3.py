# -*- coding: utf-8 -*-
## (C) 2019 Muthiah Annamalai,
## This module is part of solthiruthi project under open-tamil umbrella.
## This code maybe used/distributed under MIT LICENSE.
from solthiruthi.dictionary import DictionaryBuilder, TamilVU
from solthiruthi.tamil99kbd import inv_confusion_matrix as kbd_cm
from solthiruthi.typographical import corrections

TVU,_ = DictionaryBuilder.create(TamilVU)

wl = corrections('அன்பம்',TVU,kbd_cm,ed=2)
for c in wl:
    print(("u'%s',"%c))
print(("L = %d"%len(wl)))
