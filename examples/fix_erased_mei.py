# -*- coding: utf-8 -*-
# (C) 2020, முத்து அண்ணாமலை.
# இந்த நிரல் துண்டு MIT உரிமத்தில் வெளியிடப்பட்டது
import operator
from pprint import pprint

import tamil
from solthiruthi.scoring import bigram_scores, unigram_score

chol = tamil.utf8.get_letters("கணனன")


def mean(x):
    return sum(x) / float(len(x))


def pulligal_helper(prefix, letters):
    if len(letters) == 0: return [prefix]
    letter = letters[0]
    result = []
    if letter in tamil.utf8.agaram_letters:
        result1 = pulligal_helper(prefix + letter, letters[1:])
        mei_letter = letter + tamil.utf8.pulli_symbols[0]
        result2 = pulligal_helper(prefix + mei_letter, letters[1:])
        result.extend(result1)
        result.extend(result2)
    else:
        result1 = pulligal_helper(prefix + letter, letters[1:])
        result.extend(result1)
    return result


def pulligal_branch_bound(prefix, letters, அகராதி):
    """ we restrict options if its not a prefix in dictionary """
    if len(letters) == 0: return [prefix]
    letter = letters[0]
    result = []
    prefer = அகராதி.starts_with(prefix)
    if letter in tamil.utf8.agaram_letters:
        alternate2 = prefix + mei_letter
        if அகராதி.starts_with(alternate2) or prefer:
            mei_letter = letter + tamil.utf8.pulli_symbols[0]
            result2 = pulligal_branch_bound(alternate2, letters[1:])
            result.extend(result2)
    alternate1 = prefix + letter
    if அகராதி.starts_with(alternate1) or prefer:
        result1 = pulligal_branch_bound(alternate1, letters[1:])
        result.extend(result1)
    return result


# sort in descending order
result_tpl = [("".join(sol), (unigram_score(sol))) for sol in pulligal_helper("", chol)]
result_tpl = sorted(result_tpl, key=operator.itemgetter(1), reverse=True)
pprint(result_tpl)

"""
['கணனன',
 'கணனன்',
 'கணன்ன',
 'கணன்ன்',
 'கண்னன',
 'கண்னன்',
 'கண்ன்ன',
 'கண்ன்ன்',
 'க்ணனன',
 'க்ணனன்',
 'க்ணன்ன',
 'க்ணன்ன்',
 'க்ண்னன',
 'க்ண்னன்',
 'க்ண்ன்ன',
 'க்ண்ன்ன்']

#bigram score
[('கணனன', -12.834944378986375),
 ('கணனன்', -16.834944378986375),
 ('கணன்ன', -16.44297269239452),
 ('கணன்ன்', -20.44297269239452),
 ('கண்னன', -15.995814661052302),
 ('கண்னன்', -19.9958146610523),
 ('கண்ன்ன', -19.60384297446045),
 ('கண்ன்ன்', -23.60384297446045),
 ('க்ணனன', -17.231101404525926),
 ('க்ணனன்', -21.231101404525926),
 ('க்ணன்ன', -20.83912971793407),
 ('க்ணன்ன்', -24.83912971793407),
 ('க்ண்னன', -20.39197168659185),
 ('க்ண்னன்', -24.39197168659185),
 ('க்ண்ன்ன', -24.0),
 ('க்ண்ன்ன்', -28.0)]

# unigram score
[('கணனன', -7.5531477474850535),
 ('கணனன்', -8.553147747485053),
 ('கணன்ன', -8.553147747485053),
 ('கணன்ன்', -9.553147747485053),
 ('கண்னன', -8.553147747485053),
 ('கண்னன்', -9.553147747485053),
 ('கண்ன்ன', -9.553147747485053),
 ('கண்ன்ன்', -10.553147747485053),
 ('க்ணனன', -8.553147747485053),
 ('க்ணனன்', -9.553147747485053),
 ('க்ணன்ன', -9.553147747485053),
 ('க்ணன்ன்', -10.553147747485053),
 ('க்ண்னன', -9.553147747485053),
 ('க்ண்னன்', -10.553147747485053),
 ('க்ண்ன்ன', -10.553147747485053),
 ('க்ண்ன்ன்', -11.553147747485053)]
"""
