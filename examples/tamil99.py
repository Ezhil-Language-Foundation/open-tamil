#!/usr/bin/python

import sys
import codecs
from pprint import pprint

arg = sys.argv[1]
fp = codecs.open(arg,"r","utf-8")
data = fp.readlines()
fp.close()

# nearest neighbors
nn = {}

data = filter(lambda l: len(l.strip()) > 0,data)
order = []
for d in data:
    a,b=d.split('-')
    order.append(a.strip())
    values = b.strip().split(' ')
    nn[a.strip()]=values

print '{'
#for k,v in nn.items():
for i in order:
    k,v = i,nn[i]
    vv = ",".join([ "u'%s'"%vi   for vi in v])
    print """u'%s' : [%s], """%(k,vv)
print '}'

fwd_confusion_matrix = nn
confusion_matrix = {}
for k,v in fwd_confusion_matrix.items():
    for vv in v:
        if not confusion_matrix.get(vv,None):
            confusion_matrix[vv]=set()
        confusion_matrix[vv].add(k)

nn = confusion_matrix
print '{'
#for k,v in nn.items():
for i in order:
    k,v = i,nn[i]
    v=list(v)
    vv = ",".join([ "u'%s'"%vi   for vi in v])
    print """u'%s' : [%s], """%(k,vv)
print '}'
