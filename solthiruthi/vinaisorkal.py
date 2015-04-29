## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai
## 
## Ref: Dr. V.S. Rajam, http://letsgrammar.org/verbsWithClass.html
##
from __future__ import print_function

class struct(object):
    def __setattr__(self,prop,val):
        self.__dict__[prop] = val
        
    def __init__(self):
        pass
    
    @staticmethod
    def build(**kwargs):
        obj = struct()
        for k,v in kwargs.items():
            print(k,v)
            setattr(obj, k, v)
        return obj

class VerbClass:
    def __init__(self,classify,words):
        self.__dict__ = {'classification':None,'words':[]}
        self.words = words
        self.classification = classify
    def __str__(self):
        return u"Classifcation = %s with %d words "%(self.classification,len(self.words))
    
class VinaiSorkal: 
    IrregularVerbs = VerbClass('8',['a','uru','kAN','cA','tA'])
    Doublets = VerbClass('6',['kicukicu','ciTuciTu'])
    
if __name__ == "__main__":
    x=struct.build(a=1,b=3)
    print( getattr(x,'a') )
    print( x.a )
    print( x.b )
    
    print( VinaiSorkal.IrregularVerbs )
    print( VinaiSorkal.Doublets )
