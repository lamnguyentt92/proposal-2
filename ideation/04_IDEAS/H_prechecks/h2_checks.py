# Pre-checks for IDEA_H2.
import itertools, numpy as np
from scipy.optimize import linprog

# (A) Pairwise-overlap interface: range of the union size given all |R_i| and |R_i ∩ R_j| (LP over Venn atoms).
def union_range(n, size, pair):
    atoms = [T for r in range(1, n + 1) for T in itertools.combinations(range(n), r)]
    A, b = [], []
    for i in range(n):
        A.append([1.0 if i in T else 0.0 for T in atoms]); b.append(size)
    for i, j in itertools.combinations(range(n), 2):
        A.append([1.0 if (i in T and j in T) else 0.0 for T in atoms]); b.append(pair)
    c = np.ones(len(atoms))
    lo = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="highs")
    hi = linprog(-c, A_eq=A, b_eq=b, bounds=(0, None), method="highs")
    return lo.fun, -hi.fun

print("(A) n records, every record has `size` roots, every pair shares `pair` roots -> [min,max] distinct roots")
for n, size, pair in [(3, 2, 1), (4, 3, 1), (6, 10, 4), (8, 35, 15), (10, 126, 56), (12, 462, 210)]:
    lo, hi = union_range(n, size, pair)
    print(f"  n={n:2d} size={size:4d} pair={pair:4d}: union in [{lo:.1f}, {hi:.1f}]  ratio={hi/lo:.2f}  (n/4={n/4:.2f})")

# explicit integer witnesses for n=4: K4-edge structure (6 roots) vs core+private (9 roots)
A_ = [set() for _ in range(4)]
for r, (i, j) in enumerate(itertools.combinations(range(4), 2)):
    A_[i].add(r); A_[j].add(r)
B_ = [{0, 10 + 2 * i, 11 + 2 * i} for i in range(4)]
def profile(F): return sorted(len(s) for s in F), sorted(len(F[i] & F[j]) for i, j in itertools.combinations(range(4), 2)), len(set().union(*F))
print("  witness A:", profile(A_), " witness B:", profile(B_))

# (B) Coarsest context-invariant statistic for the decision |(R ∪ U) \ X| >= tau with |X| <= d (X = revoked roots).
def classes(k, tau, d):
    roots = range(k)
    subsets = [frozenset(s) for r in range(k + 1) for s in itertools.combinations(roots, r)]
    dels = [frozenset(s) for r in range(d + 1) for s in itertools.combinations(roots, r)]
    sig = {}
    for R in subsets:
        s = tuple(len((R | U) - X) >= tau for U in subsets for X in dels)
        sig.setdefault(s, []).append(R)
    return sig
from math import comb
print("(B) number of context-equivalence classes vs prediction 1 + sum_{j < tau+d} C(k,j)")
for k, tau, d in [(4, 1, 0), (4, 2, 0), (5, 2, 0), (5, 2, 1), (5, 3, 1), (6, 2, 2), (6, 3, 1)]:
    sig = classes(k, tau, d)
    t = tau + d
    pred = 1 + sum(comb(k, j) for j in range(min(t, k + 1)))
    ok = all((len(v) == 1 and len(v[0]) < t) or all(len(R) >= t for R in v) for v in sig.values())
    print(f"  k={k} tau={tau} d={d}: classes={len(sig)} predicted={pred} structure_ok={ok}")

# (C) bottom-(tau+d) sketches answer the threshold query exactly after any <= d revocations (random test)
rng = np.random.default_rng(0)
bad = 0
for _ in range(20000):
    k = 12; tau = int(rng.integers(1, 4)); d = int(rng.integers(0, 3)); t = tau + d
    recs = [frozenset(rng.choice(k, size=int(rng.integers(0, 7)), replace=False).tolist()) for _ in range(int(rng.integers(1, 6)))]
    X = frozenset(rng.choice(k, size=int(rng.integers(0, d + 1)), replace=False).tolist())
    truth = len(frozenset().union(*recs) - X) >= tau
    sk = [frozenset(sorted(r)[:t]) for r in recs]
    est = len(frozenset().union(*sk) - X) >= tau
    bad += truth != est
print("(C) mismatches of bottom-(tau+d) sketch vs truth in 20000 random trials:", bad)
