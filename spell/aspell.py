## -*- coding: utf-8 -*-
## (C) 2021 Muthiah Annamalai

import subprocess
import re

class ASpell:
    """
        run GNU Aspell or ispell via pipe.
        Ref: http://aspell.net/man-html/Through-A-Pipe.html
    """
    PIPE_CMD=re.split('\s+',"aspell -l ta -a --suggest")
    def __init__(self,command=PIPE_CMD):
        self.command = command
        self.text = ""
        self.result = {}

    def spellcheck(self,text,timeout=60):
        self.text = text
        pipe = subprocess.Popen(self.command,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        output,_ = pipe.communicate(bytes(text,'utf-8'),timeout)
        ASpell.parse_result(self.result,output.decode('utf-8'))
        return self.result

    @staticmethod
    def parse_result(result,output):
        #Syntax of ASpell pipe
        #OK: *
        #Suggestions: & original count offset: miss, miss, …
        #None:  # original offset
        for line in re.split('\n+',output):
            if not line.startswith('&'): continue
            word,suggestions = line.split(':')
            word = word.replace('&','').strip().split(' ')[0]
            suggestions = [word.strip() for word in suggestions.split(',')]
            result[word] = suggestions
        return result
