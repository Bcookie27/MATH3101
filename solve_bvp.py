# Finite difference Method 
# Outputs the Linear System for BVP where -u''(x) = f(x) only
import numpy as np
from scipy.sparse import diags
from math import e
import matplotlib.pyplot as plt
import scipy.special as sps  

def solve_bvp(l, f, gamma, P):
    lambx = (l/P)**2
    A = np.zeros([P-1, P-1])
    f = [f"f_{j}" for j in range(1, P)]
    u = [f"u_{i}" for i in range(1, P)]
    gamma = np.array([-1, 2.5])
    for i in range(0, P):
        A[i][i] = 2
        A[i+1][i] = -1
        A[i][i+1] = -1
    pass

x_min = float(input("X-min: "))
x_max = float(input("X-max: "))
gamma = np.array([x_min, x_max])
P = float(input("Input P: "))
x = np.linspace(x_min, x_max, P, dtype=float)
f_x = lambda x: input("Insert function: ")
solve_bvp(2, 5*e**(-x), gamma, P)