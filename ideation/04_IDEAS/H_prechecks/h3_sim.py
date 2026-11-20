# Pre-check for IDEA_H3: write-back memory as a reinforcement process.
# Types: A = language-specific / minority variant, B = normalised / majority variant.
# Each session: retrieve k records uniformly, reader outputs A w.p. g(j/k) (j = #A retrieved),
# writer normalises an A-output to B w.p. delta, output is written back.
import numpy as np
rng = np.random.default_rng(1)

def g_match(j, k): return j / k                        # probability matching
def g_major(j, k, s=4.0):                               # majority-amplifying (logistic in j/k)
    z = s * (2 * j / k - 1); return 1 / (1 + np.exp(-z)) if 0 < j < k else float(j == k)

def run(mode, g, k, delta, n0, x0, T, B=None, reps=2000):
    nA = np.full(reps, int(round(x0 * n0))); n = np.full(reps, n0)
    out = {}
    for t in range(1, T + 1):
        x = nA / n
        j = rng.binomial(k, x)
        pA = np.array([g(jj, k) for jj in j]) * (1 - delta)
        newA = rng.random(reps) < pA
        if mode == "append":
            nA = nA + newA; n = n + 1
        else:                                            # budgeted: overwrite a uniformly chosen record
            dieA = rng.random(reps) < x
            nA = nA + newA.astype(int) - dieA.astype(int)
        if t in (10, 100, 1000, 3000, 10000): out[t] = (np.mean(nA / n), np.mean(nA == 0), np.mean(nA == n))
    return out

n0 = 50; x0 = 0.4
print("== writer bias delta=0.05, probability-matching reader, k=5, n0=B=50, x0=0.4 ==")
a = run("append", g_match, 5, 0.05, n0, x0, 10000)
b = run("budget", g_match, 5, 0.05, n0, x0, 10000)
for t in a:
    print(f" t={t:6d} append: mean x={a[t][0]:.3f} (theory x0*((n0+t)/n0)^-delta={x0*((n0+t)/n0)**-0.05:.3f}, extinct={a[t][1]:.2f}) | "
          f"budget: mean x={b[t][0]:.3f} (theory x0*exp(-delta t/B)={x0*np.exp(-0.05*t/n0):.3f}, extinct={b[t][1]:.2f})")

print("== no writer bias (delta=0): neutral drift, matching reader ==")
a = run("append", g_match, 5, 0.0, n0, x0, 10000)
b = run("budget", g_match, 5, 0.0, n0, x0, 10000)
for t in a:
    print(f" t={t:6d} append: mean x={a[t][0]:.3f} P(extinct)={a[t][1]:.2f} P(fixed)={a[t][2]:.2f} | budget: mean x={b[t][0]:.3f} P(extinct)={b[t][1]:.2f} P(fixed)={b[t][2]:.2f}")

print("== majority-amplifying reader, delta=0 ==")
a = run("append", g_major, 5, 0.0, n0, x0, 10000)
b = run("budget", g_major, 5, 0.0, n0, x0, 10000)
for t in a:
    print(f" t={t:6d} append: mean x={a[t][0]:.3f} P(x<0.05)~ext={a[t][1]:.2f} | budget: mean x={b[t][0]:.3f} P(extinct)={b[t][1]:.2f} P(fixed)={b[t][2]:.2f}")

# Bernstein urn function f = B_k[g]: count interior fixed points for the majority reader
from scipy.stats import binom
xs = np.linspace(0, 1, 2001)
for k in (1, 3, 5, 9):
    f = sum(binom.pmf(j, k, xs) * g_major(j, k) for j in range(k + 1))
    h = f - xs; sign_changes = int(np.sum(np.sign(h[1:-1][:-1]) * np.sign(h[1:-1][1:]) < 0))
    print(f" k={k}: interior sign changes of B_k[g]-id = {sign_changes};  slope at 1/2 = {(f[1001]-f[999])/(xs[1001]-xs[999]):.2f}")
