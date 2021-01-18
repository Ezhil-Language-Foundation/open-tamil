## -*- coding: utf-8 -*-
# (C) 2018 Muthiah Annamalai
# This file is part of Open-Tamil project
# You may use or distribute this file under terms of MIT license

import codecs
import json
import tamil
import sys
import os


# e.g. python morse_decode.py ...-. .-.---.-.-..-- ..-.--.---.-.-... --.-....
def decode(text):
    with codecs.open(
        os.path.join(os.path.dirname(__file__), "tamilmorse.json"), "r", "utf-8"
    ) as fp:
        codebook = json.loads(fp.read())
    output = []
    reverse_code = {}
    for k, v in list(codebook.items()):
        reverse_code[v] = k
    output = [reverse_code.get(chunks, "x") for chunks in text.split(" ")]
    return " ".join(output)


if __name__ == "__main__":
    print(decode(" ".join(sys.argv[1:])))
