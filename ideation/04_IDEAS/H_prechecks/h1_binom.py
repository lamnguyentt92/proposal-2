# Same LP as h1_horizon.py but for the FULL-COUNT design: each scenario gets exactly n i.i.d.
# attempts and the number of successes C ~ Bin(n,p) is recorded (as in pass@k rollouts).
import numpy as np
from scipy.optimize import linprog
from scipy.stats import binom

def best_linear_binom(n, k, N, m=1500):
    j = np.arange(m)
    q = (np.cos(np.pi * j / (m - 1)) + 1) / 2
    p = 1 - q
    P = np.array([binom.pmf(np.arange(n + 1), n, pp) for pp in p])
    f = q ** k
    nv = n + 1
    c = np.zeros(nv + 2); c[nv] = 1; c[nv + 1] = 1 / np.sqrt(N)
    A1 = np.hstack([P, -np.ones((m, 1)), np.zeros((m, 1))]); b1 = f
    A2 = np.hstack([-P, -np.ones((m, 1)), np.zeros((m, 1))]); b2 = -f
    I = np.eye(nv)
    A3 = np.hstack([I, np.zeros((nv, 1)), -np.ones((nv, 1))]); b3 = np.zeros(nv)
    A4 = np.hstack([-I, np.zeros((nv, 1)), -np.ones((nv, 1))]); b4 = np.zeros(nv)
    A = np.vstack([A1, A2, A3, A4]); b = np.concatenate([b1, b2, b3, b4])
    res = linprog(c, A_ub=A, b_ub=b, bounds=[(None, None)] * nv + [(0, None), (0, None)], method="highs")
    return res.fun, res.x[nv], res.x[nv + 1]

for N in [629, 5000, 10**5]:
    print(f"\nFULL-COUNT design, N = {N}")
    print(" n    k   k/n   total_err   bias    ||phi||")
    for n in [10, 20, 50]:
        for mult in [1, 2, 3, 5, 10, 80]:
            k = int(n * mult)
            tot, e, M = best_linear_binom(n, k, N)
            print(f"{n:3d} {k:5d} {mult:5.1f}   {tot:8.4f}  {e:8.4f}  {M:8.2f}")
