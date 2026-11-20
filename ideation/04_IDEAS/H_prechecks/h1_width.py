# Pre-check for IDEA_H1: worst-case identified-interval width for failure at budget k
# given the first n moments (depth-n data) equals 2*E_n(x^k;[0,1]) by LP duality.
# We compute E_n numerically (discrete minimax on a fine Chebyshev grid) and compare with exp(-n^2/k).
import numpy as np
from scipy.optimize import linprog
from numpy.polynomial import chebyshev as C

def En(n, k, m=3000):
    j = np.arange(m)
    t = np.cos(np.pi * j / (m - 1))          # Chebyshev extrema on [-1,1]
    x = (t + 1) / 2
    f = x ** k
    V = C.chebvander(t, n)                    # basis T_0..T_n at t
    # minimise e s.t. |f - V c| <= e
    nvar = n + 2
    c = np.zeros(nvar); c[-1] = 1
    A = np.block([[V, -np.ones((m, 1))], [-V, -np.ones((m, 1))]])
    b = np.concatenate([f, -f])
    res = linprog(c, A_ub=A, b_ub=b, bounds=[(None, None)] * (n + 1) + [(0, None)], method="highs")
    return res.x[-1]

print("n   k     2*E_n(x^k)   exp(-n^2/k)   n^2/k")
for n, k in [(10, 20), (10, 40), (10, 100), (10, 800), (16, 64), (16, 256), (16, 1000),
             (28, 800), (32, 1000), (64, 1000), (45, 2000), (20, 400), (30, 900), (40, 1600), (60,3600)]:
    e = En(n, k)
    print(f"{n:<3d} {k:<5d} {2*e:10.4e}   {np.exp(-n*n/k):10.4e}   {n*n/k:6.2f}")
