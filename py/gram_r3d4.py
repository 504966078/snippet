#!/usr/bin/python
#
# The determinant of Gram matrix for monomial basis
# Rank 3, Dimension 4
#

from itertools import permutations
from numpy import linalg as la
import numpy

n=range(4)

def dot(a,b,(xs,ys)):
    zs=[(i0,i1,i2) for i0 in n for i1 in n for i2 in n]
    return sum([a[z[xs[0]],z[xs[1]],z[xs[2]]]*b[z[ys[0]],z[ys[1]],z[ys[2]]] for z in zs])

def kr(i,j):
    return int(i==j)

e3=[(i0,i1,i2) for i0 in [0,1] for i1 in [0,1] for i2 in [0,1]]
t8=map(lambda i: (numpy.array([int(x0==i[0] and x1==i[1] and x2==i[2]) for x0 in n for x1 in n for x2 in n]).reshape(4,4,4),[0,1,2]),e3)

axes3=map(lambda t2:[t2[0]]+[x for x in t2[1]],frozenset(map(lambda x:(x[0],frozenset(x[1:])),permutations(range(3)))))
t6=[(a,s) for a in map(lambda i: numpy.array([int(x0==i)*kr(x1,x2) for x0 in n for x1 in n for x2 in n]).reshape(4,4,4),[0,1]) for s in axes3]

t14=t8+t6

m=numpy.array([dot(i[0],j[0],(i[1],j[1])) for i in t14 for j in t14],dtype=numpy.uint8).reshape(len(t14),len(t14))


print "Nb tensors","=",len(m[0])
print "Gram Det","=", la.det(m)
#print "eigenvalues","=", sorted(la.eigvals(m))
#numpy.savetxt("/tmp/monom_3.txt",m,fmt="%u")

