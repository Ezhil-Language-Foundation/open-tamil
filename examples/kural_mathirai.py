#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8
from kural import Thirukkural
from tamil.utf8 import get_letters, get_tamil_words, total_maaththirai
from collections import Counter, OrderedDict
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib

def main():
    eq = Counter()
    eqd = {}
    kural = Thirukkural()
    for kural_no in range(1330):
        kural_words = get_tamil_words(get_letters(kural.get_kural_no(kural_no+1).ta))
        mathirai = sum([total_maaththirai(word) for word in kural_words])
        if eq[mathirai] == 0:
                eqd[mathirai] = [kural_no+1]
        else:
            eqd[mathirai].append(kural_no+1)
        eq[mathirai] += 1
    eq_sorted=OrderedDict(sorted(eq.items(),key=lambda x: x))
    pprint(eq_sorted)
    pprint(eq_sorted.values())
    pprint(eqd)
    print("total = ",sum(eq.values()))
    plt.scatter(eq_sorted.keys(),eq_sorted.values())
    plt.title(u'குறள் மாத்திரை வரிசை',{'fontname':'Catamaran'})
    plt.ylabel(u'குறட்பாக்கள் எண்ணிக்கை',{'fontname':'Catamaran'})
    plt.xlabel(u'மாத்திரை அளவு',{'fontname':'Catamaran'}) #Arial Unicode MS'})
    plt.show()

if __name__ == "__main__":
    main()
