
import copy
import pdb

class Tree:
    def __init__(self,val,prob):
        self.value = val
        self.prob = prob
        self.left = None
        self.right = None

    @staticmethod
    def make(leftTree,rightTree):
        t = Tree('%s%s'%(leftTree.prob,rightTree.prob),
                 leftTree.prob+rightTree.prob)
        if leftTree.prob >= rightTree.prob:
            leftTree,rightTree = rightTree,leftTree
        t.left = leftTree
        t.right = rightTree
        return t

def huffman_reduce(treelist):
    if len(treelist) < 2:
        return
    
    if len(treelist) == 2:
        v = Tree.make(treelist[0],treelist[1])
        treelist.pop()
        treelist.pop()
        treelist.append(v)
        return
    #print(len(treelist))
    #print(treelist)
    # find least two nodes in the treelist
    pvalues = [t.prob for t in treelist]
    idx0 = pvalues.index(min(pvalues))
    #print len(treelist)
    #print idx0
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
    #if not sym:
    #    sym = 0
    #    pfx = '0'
    #else:
    if level > 0:
        pfx = pfx+'%d'%sym
    if tree.left:
        huffman_get_codes(codes,tree.left,1-sym,pfx,level+1)
    if tree.right:
        huffman_get_codes(codes,tree.right,sym,pfx,level+1)
    return

def huffman( v, p ):
    assert sum(p) == 1.0
    tree = {}
    treelist = [Tree(vv,pp) for vv,pp in zip(v,p)]
    while len(treelist) > 1:
        huffman_reduce(treelist)
    assert len(treelist) == 1
    codes = {}
    huffman_get_codes(codes,treelist[0],0,'')
    return codes,treelist[0]

def main():
    p = [0.4, 0.35, 0.2, 0.05]
    v = ['a','b','c','d']
    ##p = [0.1,0.15,0.30,0.16,0.29]
    p = [0.125 for i in range(0,8)]
    v = ['a','b','c','d','e','f','g','h']
    code,_ = huffman(v,p)
    #return code,_
    cwl = 0.0
    for k,_v in list(code.items()):
        print(("%s -> %s"%(k,_v)))
        cwl += p[v.index(k)]*len(_v)
    print("cwl = %g"%cwl)
# Ref: https://www2.cs.duke.edu/csed/poop/huff/info/
main()
