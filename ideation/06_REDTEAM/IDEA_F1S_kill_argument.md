# Kill argument for IDEA_F1S (same-family reviewer, provisional; 2026-11-20)

**Reject: the one claim that makes this more than a benchmark audit cannot fail informatively.**

C2 ("existence does not predict prevalence") is the paper's only general result, and it is vacuous on three counts.

1. **Nobody holds the refuted hypothesis.** Per the prior-art reports, arXiv:2610.09142 says its counts give no prevalence estimate, and arXiv:2609.22220 restricts itself to comparative and existence claims. C2 confirms a disclaimer.
2. **A low correlation is built into the estimand.** By the idea's own insight, a wrong pass needs a blind spot and an agent failure landing in it. The per-template wrong-pass rate therefore tracks how often agents fail on that template, which kill rates never measure. Task difficulty alone can produce ρ < 0.4.
3. **The data cannot discriminate.** At the planned ≈1,000 pooled passes and a 3% rate, roughly 30 wrong passes are spread over 116+ templates. Most per-template rates will be zero, which attenuates ρ whatever the truth. Precision is planned for C1 only; the 0.4 threshold has no power analysis.

Without C2, what remains is a gold-state differential re-grade of AndroidWorld: the SWE-bench recipe (PatchDiff, SWE-ABS) plus Agent-Diff-style state diffs, with rank changes under re-grading already established elsewhere. The idea's own referee scored ICML fit 3/5.

The fair test, P(pass | real agent failure, failure mode) against the kill rate for that mode, is not what is proposed.

Word count: 224 (memo body, `wc -w`; excludes the title line and this line).
