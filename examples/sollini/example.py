# (C) 2021 Muthiah Annamalai
# This file is part of Open-Tamil project
# You may use or distribute this file under terms of MIT license

import networkx as nx
from tamil.utf8 import get_letters
from examples.sollini.pm_bigram_sorted_042521 import freqsort_data as tamil_bigram

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
    nx.drawing.nx_pydot.write_dot(n, 'tamil_bigram.dot')

build_network()

