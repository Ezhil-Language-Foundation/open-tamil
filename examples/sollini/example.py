# (C) 2021 Muthiah Annamalai
# This file is part of Open-Tamil project
# You may use or distribute this file under terms of MIT license

import networkx as nx
import random
from tamil.utf8 import get_letters
from examples.sollini.pm_bigram_sorted_042521 import freqsort_data as tamil_bigram
from examples.sollini.pm_unigram_sorted_050621 import freqsort_data as tamil_unigram

# Plan
# 1. Build bi-gram trellis
# 2. Run Viterbi algorithm
def build_network():
    n = nx.DiGraph()
    for rec in tamil_bigram:
        ab,weight=rec[0],rec[1]
        a,b=get_letters(ab)
        n.add_edge(a,b,weight=weight)
    print( n.number_of_nodes(), n.number_of_edges())
    #pos = nx.drawing.nx_pydot.graphviz_layout(n, prog='dot')
    #edge_labels = {(n1, n2): d['label'] for n1, n2, d in n.edges(data=True)}
    #nx.draw_networkx_edge_labels(n, pos, edge_labels=edge_labels)
    #nx.drawing.nx_pydot.write_dot(n, 'tamil_bigram.dot')
    return n

def print_word(network,length):
    word = []
    uni_letters = []
    uni_prob = []
    big_letters = []
    big_prob = []
    big = {}
    for l,p in tamil_unigram:
        uni_prob.append(p)
        uni_letters.append(l)
    for l,p in tamil_bigram:
        big_letters.append(l)
        big_prob.append(p)
        big[l] = p
    word.append( random.choices(population=uni_letters,weights=uni_prob,k=1)[0] )
    length -= 1
    while length > 0:
        startswith_letters = list(filter( lambda x: x.startswith( word[-1]) ,big_letters))
        startswith_prob = [big[l] for l in startswith_letters]
        big_choice = random.choices(population=startswith_letters,weights=startswith_prob,k=1)[0]
        word.append( get_letters(big_choice)[-1] )
        length -= 1
    w = "|".join(word)
    print(w)
    return w

network = build_network()
for i in range(100):
    print_word(network,random.randint(1,10))
