# (C) 2021 Muthiah Annamalai
# This file is part of open-tamil project
from itertools import product

from .utf8 import get_letters_elementary, shorten


def get_superposition_representation(word, raw=False):
    """
        Treat word as a Vowel + Consonant representation and compute Kronecker product:
        e.g.

        குவாண்டம் விதிகளால் உயிர்மெய்பிரித்தால்:
        அதாவது, |த> = |அ> + |த்>
        |தமிழ்> = |த> (x) |மி> (x) |ழ்>
               = |அஇ> + |அழி> + |அழ்> + |ழ ழ்> + |த் ழ்> + |திழ்> + |தி> + |திழ்>

        இதைவைத்து ஒரு சொல்தேடல் அல்கோரிதம் செய்யலாம். வேறு என்ன பண்ணலாம்?

        This follows from Quantum algebra representation of states.
        when @raw = False the letters in supersposition are not shortened.

        Note: for N-letter word we return 2^N alternates which can be time and memory
        in-efficient for large N.
    """
    alternates = [x or '' for x in get_letters_elementary(word, symmetric=True)]
    grouped = []
    for idx in range(0, len(alternates), 2):
        grouped.append([alternates[idx], alternates[idx + 1]])
    if raw:
        superpos = [u"".join(word) for word in product(*grouped)]
        return superpos
    superpos = []
    for word_ in product(*grouped):
        # remove none
        word = list(filter(lambda x: x, word_))
        superpos.append(word)
    shortened = list(map(shorten, superpos))
    return shortened
