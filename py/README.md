# Python tools



* circulant.py computes the determinant of circulant matrix

$ ./circulant.py 

Circulant matrix:

[4, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

.......

[2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 4]

Eigenvalues:

(24+0j)

........

(3.47814760073-4.54927053629j)

Det= (28473336+6.89178705215e-08j)


* gram_rMdN.py computes the determinant of Gram matrix for the monomial basis

N - dimension of the vector space

M - rank of the momonials


* gram_eMd4.py computes the determinant of Gram matrix for the Kronecker's basis

M = 2 * (number of Kronecker's deltas)

Warning: gram_e8d4.py is very slow.
