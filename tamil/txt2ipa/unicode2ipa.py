#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
# (C) 2014 Arulalan.T <arulalant@gmail.com>                                  #
# Date : 02.08.2014                                                          #
#                                                                            #
# This file is part of open-tamil/txt2ipa                                    #
#                                                                            #
# txt2ipa is free software: you can redistribute it and/or                   #
# modify it under the terms of the GNU General Public License as published by#
# the Free Software Foundation, either version 3 of the License, or (at your #
# option) any later version. This program is distributed in the hope that it #
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty#
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General#
# Public License for more details. You should have received a copy of the GNU#
# General Public License along with this program. If not, see                #
# <http://www.gnu.org/licenses/>.                                            #
#                                                                            #
##############################################################################

from .transliteration import tam2lat
from .ipaconvert import ipa
from .ipaconvert import broad as broad_ipa


def txt2ipa(text, broad=True):
    lat = tam2lat(text)
    lat = " " + lat + " "
    ipa_text = ipa(lat)

    # make memory free
    del lat

    if broad:
        ipa_text = broad_ipa(ipa_text)

    return ipa_text

# end of def txt2ipa(text, broad=True):
