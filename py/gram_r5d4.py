#!/usr/bin/python
#
# The determinant of Gram matrix for monomial basis
# Rank 5, Dimension 4
#

from itertools import permutations
from numpy import linalg as la
import numpy

n=range(4)

def dot(a,b,(xs,ys)):
    zs=[(i0,i1,i2,i3,i4) for i0 in n for i1 in n for i2 in n for i3 in n for i4 in n]
    return sum([a[z[xs[0]],z[xs[1]],z[xs[2]],z[xs[3]],z[xs[4]]]*b[z[ys[0]],z[ys[1]],z[ys[2]],z[ys[3]],z[ys[4]]] for z in zs])

def kr(i,j):
    return int(i==j)

e5=[(i0,i1,i2,i3,i4) for i0 in [0,1] for i1 in [0,1] for i2 in [0,1] for i3 in [0,1] for i4 in [0,1] ]
t32=map(lambda i: (numpy.array([int(x0==i[0] and x1==i[1] and x2==i[2] and x3==i[3] and x4==i[4]) for x0 in n for x1 in n for x2 in n for x3 in n for x4 in n]).reshape(4,4,4,4,4),[0,1,2,3,4]),e5)


axes10=map(lambda t2:[x for s in t2 for x in s],frozenset(map(lambda x:(frozenset(x[0:3]),frozenset(x[3:])),permutations(range(5)))))
e3=[(i0,i1,i2) for i0 in [0,1] for i1 in [0,1] for i2 in [0,1] ]
t80=[(a,s) for a in map(lambda i: numpy.array([int(x0==i[0] and x1==i[1] and x2==i[2])*kr(x3,x4) for x0 in n for x1 in n for x2 in n for x3 in n for x4 in n]).reshape(4,4,4,4,4),e3) for s in axes10]


axes15=map(lambda t2:[t2[0]]+[x for s in t2[1] for x in s],frozenset(map(lambda x:(x[0],frozenset([frozenset(x[1:3]),frozenset(x[3:])])),permutations(range(5)))))
t30=[(a,s) for a in map(lambda i: numpy.array([int(x0==i)*kr(x1,x2)*kr(x3,x4) for x0 in n for x1 in n for x2 in n for x3 in n for x4 in n]).reshape(4,4,4,4,4),[0,1]) for s in axes15]

t142=t32+t80+t30

m=numpy.array([dot(i[0],j[0],(i[1],j[1])) for i in t142 for j in t142],dtype=numpy.uint8).reshape(len(t142),len(t142))


print "Nb tensors","=",len(m[0])
print "Gram Det","=", la.det(m)
#print "eigenvalues","=", sorted(la.eigvals(m))
#numpy.savetxt("/tmp/monom_2.txt",m,fmt="%u")


