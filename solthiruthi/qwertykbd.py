## -*- coding: utf-8 -*-
## (C) 2019 Muthiah Annamalai,
## This module is part of solthiruthi project under open-tamil umbrella.
## This code maybe used/distributed under MIT LICENSE.

# qwerty keyboard
confusion_matrix = {
    # row 1
    "q": ["w", "s", "a"],
    "w": ["q", "e", "d", "s", "a"],
    "e": ["r", "f", "d", "s", "w"],
    "r": ["e", "d", "f", "g", "t"],
    "t": ["y", "h", "g", "f", "r"],
    "y": ["u", "j", "h", "g", "t"],
    "u": ["i", "k", "j", "h", "y"],
    "i": ["o", "l", "k", "j", "u"],
    "o": ["p", "l", "k", "i"],
    "p": ["o", "l"],
    # row 2
    "a": ["q", "w", "s", "z"],
    "s": ["a", "w", "e", "d", "x", "z"],
    "d": ["e", "r", "f", "c", "x", "s"],
    "f": ["r", "t", "g", "v", "c", "d"],
    "g": ["t", "y", "h", "b", "v", "f", "r"],
    "h": ["y", "u", "j", "n", "b", "g"],
    "j": ["u", "i", "k", "m", "n", "h"],
    "k": ["i", "o", "l", "m", "j"],
    "l": ["j", "i", "o"],
    # row 3
    "z": ["a", "s", "x"],
    "x": ["z", "s", "d", "c"],
    "c": ["x", "d", "f", "v"],
    "v": ["c", "f", "g", "b"],
    "b": ["v", "g", "h", "n"],
    "n": ["b", "h", "j", "m"],
    "m": ["n", "j", "k"],
}
