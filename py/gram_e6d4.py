#!/usr/bin/python
#
# The determinant of Gram matrix for the basis of Kronecker deltas
# Number of detas 3, Dimension 4
#

from itertools import permutations
from numpy import linalg as la
import numpy

axes=map(lambda s3:[x for s2 in s3 for x in s2],frozenset(map(lambda x:frozenset([frozenset(x[0:2]),frozenset(x[2:4]),frozenset(x[4:])]),permutations(range(6)))))

def kr(i,j):
    return int(i==j)

def kr3(x0,x1,x2,x3,x4,x5):
    return kr(x0,x1)*kr(x2,x3)*kr(x4,x5)

def dot(a,b,(xs,ys)):
    zs=[(i0,i1,i2,i3,i4,i5) for i0 in n for i1 in n for i2 in n for i3 in n for i4 in n for i5 in n]
    return sum([a[z[xs[0]],z[xs[1]],z[xs[2]],z[xs[3]],z[xs[4]],z[xs[5]]]*b[z[ys[0]],z[ys[1]],z[ys[2]],z[ys[3]],z[ys[4]],z[ys[5]]] for z in zs])

n=range(4)
a=numpy.array([kr3(x0,x1,x2,x3,x4,x5) for x0 in n for x1 in n for x2 in n for x3 in n for x4 in n for x5 in n]).reshape(4,4,4,4,4,4)

m=numpy.array([dot(a,a,(i,j)) for i in axes for j in axes]).reshape(len(axes),len(axes))

print "Nb tensors","=",len(m[0])
print "Gram Det","=", la.det(m)
#print "eigenvalues","=", sorted(la.eigvals(m))
#numpy.savetxt("/tmp/monom_0.txt",m,fmt="%u")


