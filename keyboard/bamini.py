## -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai

from .layout import Layout

class Bamini( Layout ):
    def load_layout(self):
        self.keymap[u'`'] = u"ஹ|`"
        self.keymap[u'1'] = u"1|!"

