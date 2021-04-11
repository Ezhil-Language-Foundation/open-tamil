## -*- coding: utf-8 -*-
## (C) 2021 Muthiah Annamalai

import subprocess
import re

try:
    from tamilsandhi import check_sandhi

    SKIP_SANDHI_CHECKER = False
except ModuleNotFoundError:
    SKIP_SANDHI_CHECKER = True
NL = re.compile('\n+')
SPC = re.compile('\s+')


class ASpell:
    """
        run GNU Aspell or ispell via pipe.
        Ref: http://aspell.net/man-html/Through-A-Pipe.html
    """
    PIPE_CMD = re.split('\s+', "aspell -l ta --encoding UTF-8 -a --suggest")

    def __init__(self, command=PIPE_CMD):
        self.command = command
        self.text = ""
        self.result = {}

    def spellcheck(self, text, timeout=60):
        self.text = text
        pipe = subprocess.Popen(self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, _ = pipe.communicate(bytes(text, 'utf-8'), timeout)
        ASpell.parse_result(self.result, output.decode('utf-8'))

        if SKIP_SANDHI_CHECKER:
            return self.result

        prev_word = ''
        for line in re.split(NL, text):
            for word in re.split(SPC, line):
                if prev_word != '':
                    if prev_word not in self.result:
                        # if a word is in error we don't/can't do a sandhi-check
                        sandhi_result, _ = check_sandhi([prev_word, word])
                        if sandhi_result[0] != prev_word:
                            self.result[prev_word] = [sandhi_result[0], prev_word]
                if word.endswith('.'):
                    prev_word = ''
                else:
                    prev_word = word

        return self.result

    @staticmethod
    def parse_result(result, output):
        # Syntax of ASpell pipe
        # OK: *
        # Suggestions: & original count offset: miss, miss, …
        # None:  # original offset
        for line in re.split('\n+', output):
            if not line.startswith('&'): continue
            word, suggestions = line.split(':')
            word = word.replace('&', '').strip().split(' ')[0]
            suggestions = [word.strip() for word in suggestions.split(',')]
            result[word] = suggestions
        return result
