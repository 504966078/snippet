#!/usr/bin/python
#
# We calculate the determinant of a circulant matrix
#

import cmath


def show(row):
    NR=len(row)
    def value(n):
        return reduce(lambda x,y:
                      x+y,
                      map(lambda i: row[i]*cmath.exp((2 * cmath.pi * 1j * n * i )/NR),range(NR)))

    print "Circulant matrix:"
    for n in range(NR): print map(lambda i: row[(i-n)], range(NR))
    print

    print "Eigenvalues:"
    for n in range(NR): print value(n)
    print

    print "Det=",reduce(lambda x,y : x*y, map(lambda n: value(n),range(NR)))
    print

show([4,2,2,2,2,2,2,1,1,1,1,1,1,1,1])
#show([4,2,2,2,1,1,2,1,1,1,1,2,1,1,2])
