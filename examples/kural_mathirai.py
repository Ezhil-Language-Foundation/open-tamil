#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter, OrderedDict
from pprint import pprint
from scipy.optimize import curve_fit

from kural import Thirukkural
from tamil.utf8 import get_letters, get_tamil_words, total_maaththirai


# Define model function to be used to fit to the data above:
def gauss(x, *p):
    A, mu, sigma = p
    return A * np.exp(-((x - mu) ** 2) / (2.0 * sigma ** 2))


def main():
    eq = Counter()
    eqd = {}
    kural = Thirukkural()
    for kural_no in range(1330):
        kural_words = get_tamil_words(get_letters(kural.get_kural_no(kural_no + 1).ta))
        mathirai = sum([total_maaththirai(word) for word in kural_words])
        if eq[mathirai] == 0:
            eqd[mathirai] = [kural_no + 1]
        else:
            eqd[mathirai].append(kural_no + 1)
        eq[mathirai] += 1
    eq_sorted = OrderedDict(sorted(eq.items(), key=lambda x: x))
    pprint(eq_sorted)
    pprint(eq_sorted.values())
    pprint(eqd)
    print("total = ", sum(eq.values()))
    plt.scatter(eq_sorted.keys(), eq_sorted.values())
    plt.ylabel(u"குறட்பாக்கள் எண்ணிக்கை", {"fontname": "Catamaran"})
    plt.xlabel(u"மாத்திரை அளவு", {"fontname": "Catamaran"})  # Arial Unicode MS'})

    # p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
    p0 = [75.0, 20.0, 5.0]
    coeff, var_matrix = curve_fit(
        gauss, list(eq_sorted.keys()), list(eq_sorted.values()), p0=p0
    )

    # Get the fitted curve
    hist_fit = gauss(list(eq_sorted.keys()), *coeff)
    plt.plot(
        eq_sorted.keys(),
        hist_fit,
        label="Gaussian Fitted data (mean=%g, std=%g)" % (coeff[1], coeff[2]),
    )
    plt.title(
        r"குறள் மாத்திரை வரிசை (Gauss \mu=%g, \sigma=%g)" % (coeff[1], coeff[2]),
        {"fontname": "Catamaran"},
    )

    # Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
    print("Fitted mean = ", coeff[1])
    print("Fitted standard deviation = ", coeff[2])

    plt.show()


if __name__ == "__main__":
    main()
