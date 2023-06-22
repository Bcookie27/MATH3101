# Central Finite Difference method that takes in any input
import numpy as np
from scipy.linalg import solve
from scipy import exp

def solver(L, f, gamma, P):
    t = np.full(P, 2)
    A = np.diag(t)
    for r in range(P+1):
        for c in range(P+1):
            if r != P and (c == r - 1 or c == r + 1):
                A[r-1, c-1] = -1
            if r == c:
                if r == P:
                    A[r-1, c-1] = 1
                elif r == 0:
                    A[r, c] = 1
    print(A)
    x = np.linspace(0, L, int(L/P)) # denotes u that we r trying to find
    
    
L = 2
f = lambda x: 5*exp(-x)
gamma = [-1, 2.5]
P = 6
A, x = solver(L, f, gamma, P)
print("Solution: ", A)
print("Points:", x)
