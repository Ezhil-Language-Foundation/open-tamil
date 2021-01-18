# -*- coding: utf-8 -*-
# (C) 2014 Arulalan.T <arulalant@gmail.com>
# This file is part of open-tamil package

try:
    # python 2.7 defaults comes with collections module
    from collections import OrderedDict
except Exception as e:
    try:
        # In python 2.2 to 2.6, user need to install ordereddict via pip
        from ordereddict import OrderedDict
    except Exception as e:
        OrderedDict = dict
