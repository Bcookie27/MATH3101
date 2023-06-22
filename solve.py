import numpy as np
from scipy.linalg import solve
from scipy import exp

from scipy.sparse import diags
import matplotlib.pyplot as plt

def solve_bvp(L, f, gamma, P):
    # setting up system eqn
    b = np.zeros(P-1) # RHS vector
    d1 = np.full(P, 2)
    A = np.diag(d1)
    for r in range(P):
        for c in range(P):
            if c == r - 1 or c == r + 1:
                A[r, c] = -1       

    # applying boundary conditions
    A = A[]
    # solving system equation
    
    # solution to the given bvp
    gamma = np.array(gamma)
    sol = create_bvp(A, x, gamma)
    A = sol.gamma[0]
    x = sol.x
    
    return A, x

def create_bvp(A, x, gamma):# function to insert the inputted bvp by user
    dydx = np.zeros(2)  
    dydx[0] = gamma[1]
    dydx[1] = gamma[0]
    
    return dydx
    
L = 2
f = lambda x: 5*exp(-x)
gamma = [-1, 2.5]
P = 6
A, x = solve_bvp(L, f, gamma, P)
print("Solution: ", A)
print("Points:", x)
