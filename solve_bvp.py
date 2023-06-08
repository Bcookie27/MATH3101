# Finite difference Method 
# Outputs the Linear System for BVP where -u''(x) = f(x) only

import numpy as np
from scipy.sparse import diags
from math import e
def solve_bvp(l, f, gamma, P):
    lambx = (l/P)**2
    # ab = ([[0]*(P-2)])*(P-2)
    u = np.arange(P-1)
    f_1 = list(map(f, range(0, P-1)))
    A = np.zeros((P+1, P+1))
    A[0, 0] = 1
    A[P, P] = 1
    for i in range(0, P):
        A[i][i] = 2
        A[i+1][i] = -1
        A[i][i+1] = -1
    # specifies U and x vector
    