## -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai

# class borrowed from Ezhil language library
class Keymap(dict):
    """ dictionary structure with a set like mathematical structure.
        that way when you insert functions for keymap library, we don't trample on each other
        by accidentally overwriting stuff"""
    def __init__(self):
        dict.__init__(self)
    def __setitem__(self,key,val):
        if ( self.has_key(key) ):
            raise KeyError(u"Dictionary is getting clobbered; key "+key+" already present")
        dict.__setitem__(self,key,val)

# map to onscreen kbd
class Layout:
    """ pure virtual class - that implements the keyboard layout information """
    def __init__(self):
        self.keymap = Keymap()
        self.js_callback = u"keyPress"
        self.load_layout()

    def load_layout(self):
        raise Exception("load_layout method not implemented")
    
    def to_javascript(self):
        for k,vv in self.keymap.items():
                for pos,v in enumerate(vv.split(u"|")):                    
                    if ( len(v) >= 4 and v == u"PIPE" ):
                            v = u"|"
                    print(u"<input type=\"button\" id=\"btn_kw_%s_%d\" value=\"%s\" onClick=\"appendText('%s');\" />"%(k,pos,v,v))
        print("/* -------------------------------- */")
        return

