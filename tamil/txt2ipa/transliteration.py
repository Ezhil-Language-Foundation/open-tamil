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

import re


# Convert Tamil unicode to intermediate romanized encoding


def tam2lat(text):
    tameng = {
        "அ": "_a",
        "ஆ": "_A",
        "இ": "_i",
        "ஈ": "_I",
        "உ": "_u",
        "ஊ": "_U",
        "எ": "_E",
        "ஏ": "_e",
        "ஐ": "_Y",
        "ஒ": "_O",
        "ஓ": "_o",
        "ஔ": "_W",
        "க": "k",
        "ங": "G",
        "ச": "c",
        "ஜ": "j",
        "ஞ": "J",
        "ட": "T",
        "ண": "N",
        "த": "t",
        "ந": "n",
        "ன": "V",
        "ப": "p",
        "ம": "m",
        "ய": "y",
        "ர": "r",
        "ற": "X",
        "ல": "l",
        "ள": "L",
        "ழ": "Z",
        "வ": "v",
        "ஶ": "F",
        "ஷ": "S",
        "ஸ": "s",
        "ஹ": "h",
        "ா": "A",
        "ி": "i",
        "ீ": "I",
        "ு": "u",
        "ூ": "U",
        "ெ": "E",
        "ே": "e",
        "ை": "Y",
        "ொ": "O",
        "ோ": "o",
        "ௌ": "W",
        "்": "F",
        "ஃ": "K",
    }

    for key, value in tameng.items():
        text = text.replace(key, value)

    text = re.sub("([kGcJTNtnpmyrlvZLXVjSsh])F", lambda m: "_" + m.group(1), text)

    text = re.sub(
        "(?<!_)([kGcJTNtnpmyrlvZLXVjSsh])(?![aAiIuUeEoOYW])",
        lambda m: m.group(1) + "a",
        text,
    )

    text = re.sub(
        "(_[kGcJTNtnpmyrlvZLXVjSsh])(_[aAiIuUeEoOYW])",
        lambda m: m.group(1) + "_" + m.group(2),
        text,
    )

    text = text.replace("_", "")
    text = text.replace("Y", "ai")
    text = text.replace("W", "au")

    return text

# end of def tam2lat(text):
