## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai
## 
from __future__ import print_function

import abc

class ISpeller(object):
    __metaclass__ = abc.ABCMeta    

    @abc.abstractmethod
    def process_word(self,word):
        raise Exception("ISpeller : method should return word, and if it was in error or not")

    def get_return_obj(self,word):
        return {'word':word,'is_error':False,'alternatives':None}
