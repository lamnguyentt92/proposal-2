# Pre-check for IDEA_H1: achievable worst-case error of the best LINEAR estimator of
# m_k = E[(1-p)^k] (failure-to-break at budget k) from N scenarios, each attacked with
# i.i.d. attempts until first success or depth n (data: T ^ n).  Estimator = mean of phi(T^n).
# Worst-case error bound minimised: sup_q |E_q phi - q^k| + ||phi||_inf / sqrt(N)   (LP).
import numpy as np
from scipy.optimize import linprog

def best_linear(n, k, N, m=1500):
    j = np.arange(m)
    q = (np.cos(np.pi * j / (m - 1)) + 1) / 2          # grid on [0,1], q = 1-p
    p = 1 - q
    # outcomes t=1..n (success at t): prob p q^{t-1};  outcome n+1 (censored): q^n
    P = np.zeros((m, n + 1))
    for t in range(1, n + 1):
        P[:, t - 1] = p * q ** (t - 1)
    P[:, n] = q ** n
    f = q ** k
    nv = n + 1
    # variables: phi (n+1), e, M
    c = np.zeros(nv + 2); c[nv] = 1; c[nv + 1] = 1 / np.sqrt(N)
    A1 = np.hstack([P, -np.ones((m, 1)), np.zeros((m, 1))]); b1 = f
    A2 = np.hstack([-P, -np.ones((m, 1)), np.zeros((m, 1))]); b2 = -f
    I = np.eye(nv)
    A3 = np.hstack([I, np.zeros((nv, 1)), -np.ones((nv, 1))]); b3 = np.zeros(nv)
    A4 = np.hstack([-I, np.zeros((nv, 1)), -np.ones((nv, 1))]); b4 = np.zeros(nv)
    A = np.vstack([A1, A2, A3, A4]); b = np.concatenate([b1, b2, b3, b4])
    res = linprog(c, A_ub=A, b_ub=b, bounds=[(None, None)] * nv + [(0, None), (0, None)], method="highs")
    return res.fun, res.x[nv], res.x[nv + 1]

for N in [80, 629, 5000, 10**5, 10**7]:
    print(f"\nN = {N} scenarios (log N = {np.log(N):.1f})")
    print(" n    k   k/n   total_err   bias    ||phi||")
    for n in [10, 20, 50]:
        for mult in [1, 1.5, 2, 3, 5, 10, 80]:
            k = int(n * mult)
            tot, e, M = best_linear(n, k, N)
            print(f"{n:3d} {k:5d} {mult:5.1f}   {tot:8.4f}  {e:8.4f}  {M:8.2f}")
