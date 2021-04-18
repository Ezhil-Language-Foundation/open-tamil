#(C) 2018 Muthiah Annamalai
# This file is part of Open-Tamil project
# You may use or distribute this file under terms of MIT license

class Tree:
    """
    Implement binary Huffman codes
    Ref: https://www2.cs.duke.edu/csed/poop/huff/info/
    """
    def __init__(self,val,prob):
        self.value = val
        self.prob = prob
        self.left = None
        self.right = None

    @staticmethod
    def make(leftTree,rightTree):
        """ Utility make function."""
        t = Tree('%s%s'%(leftTree.prob,rightTree.prob),
                 leftTree.prob+rightTree.prob)
        if leftTree.prob >= rightTree.prob:
            leftTree,rightTree = rightTree,leftTree
        t.left = leftTree
        t.right = rightTree
        return t

def huffman_reduce(treelist):
    """ Intermediate steps in Huffman code. """
    if len(treelist) < 2:
        return

    if len(treelist) == 2:
        v = Tree.make(treelist[0],treelist[1])
        treelist.pop()
        treelist.pop()
        treelist.append(v)
        return
    # find least two nodes in the treelist
    pvalues = [t.prob for t in treelist]
    idx0 = pvalues.index(min(pvalues))
    tree0 = treelist[idx0]
    del treelist[idx0]

    pvalues = [t.prob for t in treelist]
    idx1 = pvalues.index(min(pvalues))
    tree1 = treelist[idx1]
    del treelist[idx1]

    treejoin = Tree.make(tree0,tree1)
    treelist.append(treejoin)
    return

def huffman_get_codes(codes,tree,sym=None,pfx='',level=0):
    if (not tree.left) and (not tree.right):
        #codes are made at leaf nodes only
        codes[tree.value] = pfx + '%d'%sym
        return
    if level > 0:
        pfx = pfx+'%d'%sym
    if tree.left:
        huffman_get_codes(codes,tree.left,1-sym,pfx,level+1)
    if tree.right:
        huffman_get_codes(codes,tree.right,sym,pfx,level+1)
    return

def huffman( v, p ):
    """ v - list of symbols. p - list of corresponding probabilities for symbol """
    assert sum(p) >= 0.99,"Sum of p = %g"%sum(p)
    treelist = [Tree(vv,pp) for vv,pp in zip(v,p)]
    while len(treelist) > 1:
        huffman_reduce(treelist)
    assert len(treelist) == 1
    codes = {}
    huffman_get_codes(codes,treelist[0],0,'')
    return codes,treelist[0]

def print_huffman_code_cwl(code,p,v):
    """ code - code dictionary with symbol -> code map, p, v is probability map """
    cwl = 0.0
    for k,_v in code.items():
        print(u"%s -> %s"%(k,_v))
        cwl += p[v.index(k)]*len(_v)
    print(u"cwl = %g"%cwl)
    return cwl,code.values()

#examples
def __demo__():
    ##p = [0.1,0.15,0.30,0.16,0.29]
    p = [0.125 for i in range(0,8)]
    v = ['a','b','c','d','e','f','g','h']
    code,_ = huffman(v,p)
    cwl,codelist = print_huffman_code_cwl(code,p,v)
    assert( cwl == 3 )

    p = [0.4, 0.35, 0.2, 0.05]
    v = ['a','b','c','d']
    code,_ = huffman(v,p)
    cwl,codelist = print_huffman_code_cwl(code,p,v)
    assert( cwl == 1.85 )

if __name__ == u"__main__":
    __demo__()
