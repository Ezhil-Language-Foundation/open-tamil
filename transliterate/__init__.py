# (C) 2013-2015 Muthiah Annamalai
from . import UOM
from . import azhagi
from . import combinational
from . import itrans
from . import jaffna
from . import ISO
from .algorithm import Iterative, Greedy, Tamil2English, reverse_transliteration_table

#Transliteration module
iterative_transliterate = Iterative.transliterate
