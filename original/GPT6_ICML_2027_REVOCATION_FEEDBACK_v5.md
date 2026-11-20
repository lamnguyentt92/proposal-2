# ICML 2027 — FINAL REVISED RESEARCH PROPOSAL v5

## REVOCATION-FEEDBACK: Learnability of Budgeted Agent Memory under Policy-Induced Feedback Censoring and Irreversible State Loss

**Research status:** **MATHEMATICAL IDEA ONLY; no theorem proved, no code or measurements completed.**  
**Meta-decision:** **HOLD — FORMAL NOVELTY GATE FIRST.**  
**Supersedes:** v4 `REVSHIFT-POM` as a proposed distinctive contribution.  
**ICML contribution type, if validated:** **Theory** or **General**; alternatively a substantial negative-results/evaluation contribution if *genuinely informative*, not as a fallback label.

## 1. Positioning / single scientific question

How does **irreversible, permission-mandated state removal** alter what an online memory-management policy can learn when the removal also prevents observing a memory item's future utility, and the task distribution and permission state may later change?

The novelty hypothesis is **not** that memory has a budget, not that eligibility changes, not that feedback is delayed, and not that privacy constraints exist. Each is established. What may be worth ICML is a **precisely characterized learnability boundary** at the intersection of (i) *path-dependent memory state*, (ii) *authorized-only observations*, and (iii) *later costly or impossible lawful reacquisition*. A formal reduction to known bandit/caching formulations is the null hypothesis and must be tested first.

## 2. Research questions and measurable targets

**RQ1 — Model equivalence:** Can `REVOCATION-FEEDBACK` be reduced to sleeping bandits/online caching with an enlarged memory-state space without losing the problem's information constraints? If yes, what remains truly new?

**RQ2 — Identifiability:** Which additional legally observable signals are necessary for adaptive allocation policies to learn demand after revoked items are removed, without estimating utility from the prohibited contents?

**RQ3 — Algorithmic value:** Under a bounded-variation task process, explicitly priced authorized reacquisition and a finite memory budget, can a feasible policy achieve a nontrivial performance guarantee against a **reachable, nonanticipating comparator** with identical observations?

**H0 (strong null):** `MemPrice + policy mask + change detector + delayed-feedback learner` (or a sleeping-bandit/online caching method with state augmentation) matches the candidate at equal legal information, budget, computation and reacquisition cost.

**H1 (conditional):** there exists a rigorously specified environment family or restricted structural condition where a distinct algorithm/theorem is required and matters quantitatively.

## 3. Prior-work confrontation and novelty restrictions

| Verified work | Covered contribution | V5 must establish beyond it |
|---|---|---|
| [MemPrice, arXiv:2610.24955](https://arxiv.org/abs/2610.24955) | Online memory allocation/pricing, hard budget, irreversible compression, trajectory-sensitive comparator | New consequence of **permission-induced observation constraints**, not pricing/budget alone |
| [OSL-MR, arXiv:2606.10616](https://arxiv.org/abs/2606.10616) | Online-observable learning, delayed miss/reacquisition and staleness costs | Not a re-label of learning from permitted features |
| [MemCredit, arXiv:2611.15600](https://arxiv.org/abs/2611.15600) | Context-dependent memory utility under intervention-derived supervision | No 'first decision credit' claim; do not import inaccessible test-time counterfactuals |
| [Emamjomeh-Zadeh et al., PMLR 132 (2021)](https://proceedings.mlr.press/v132/emamjomeh-zadeh21a.html) | Online learning with changing feasible action sets | Masked actions not novel |
| [SP-Mem, arXiv:2608.16551](https://arxiv.org/abs/2608.16551) | Consent-controlled privacy tiers and retrieval | Enforcement architecture not ML novelty |
| **Partial monitoring, online caching, switching-cost bandits** | Missing/delayed rewards and path-dependent control | Full-theory audit still required before any originality claim |

The new paper **must not** claim certified differential privacy, certified erasure from pretrained weights, universal no-regret, or avoidance of consent/privacy laws solely through a simulator.

## 4. Exact formal model (candidate, not previously proved)

At step `t`, task context `x_t` arrives. Let `I` be a finite item set with item representations/levels `l`, sizes `s_{i,l}`, and current state `m_t` (`absent`, `eligible raw`, `eligible compressed`, `revoked/erased`, `reacquisition pending`, etc.). A trusted authorization process sets `g_t(i, purpose)∈{0,1}`. Allowed actions `a_t∈F(m_t,g_t,B)` obey a hard budget `B` and cannot read/retain prohibited content.

The environment draws task regime `z_t` and reward `r_t`, but the learner sees only the filtration of **legally allowed observations**:

```
F_t = sigma( permitted task metadata, trusted permission events,
             allowed memory representations, executed allowed actions,
             realized permitted rewards, authorized reacquisition outcomes )
```

The learner's action `a_t` must be `F_t`-measurable. If permission revoked for `i`, its content and prohibited item-dependent features are removed from modelled accessible state. A new consent event may authorize a **fresh acquisition** with stated delay and cost; it does not restore a forbidden shadow cache. No reward of an unexecuted illegal use is revealed to the learner.

Let state dynamics `m_{t+1}=T(m_t,a_t,g_t,ξ_t)` model irreversible deletion/recompression and permitted reacquisition; `ξ_t` is exogenous randomness. Define per-round legal utility:

```
u_t = r_t(legal task completion, a_t, m_t)
      - c_retrieval(a_t) - c_reacquisition(a_t) - c_compute(a_t)
```

The proposed primary comparison is to a **reachable same-information policy class** `Π_F`: nonanticipating, policy-compliant policies acting under the same filtration, action spaces, storage state transitions and budgets. Because memory trajectories differ, define the coupling of exogenous tasks/permission events across policies explicitly and **state the regret/comparator before proving bounds**. A clairvoyant hindsight trajectory may appear **only as an unattainable diagnostic**.

### Critical impossibility caveat

A 'two hidden worlds with the same observations' proof only establishes an elementary identifiability barrier if the environments differ in rewards for actions the learner cannot ever legally execute. That alone is not interesting: if an action is illegal, its counterfactual reward is irrelevant to legal policy quality. To be scientifically meaningful, the indistinguishable worlds must lead to *different future permitted* decisions or reacquisition costs **without granting access to revoked information**. Constructing such a pair and proving a substantive separation is a necessary novelty gate.

## 5. Proposed theoretical package — conditional targets

**T1: A nontrivial separation or reduction result.** Analyze a minimal class with two memories, two regimes, one revocation/regrant transition, and costly reacquisition. First attempt a reduction to ordinary stateful sleeping-bandit/online caching. If the reduction preserves the filtration and comparator, report the equivalence, not an invented novel theorem.

**T2: Learnability condition.** Specify exactly which allowed proxy observations (`task category`, `public aggregate demand`, `authorized requery`) permit identification of future *legal* memory value under shifts. Compare impossibility with a well-defined class where observation coverage/variation budgets are bounded. Any conditions should be practically testable, not an oracle.

**T3: A positive algorithm / bound.** Only after T1/T2 survive theory audit, derive a viable state-aware online learner, e.g. constrained optimistic estimate with explicit state transitions and safe decision filters. Its bound must be compared term-by-term with known sleeping-bandit, switching-cost, partial-monitoring and caching rates; do not promise a specific `O(√T)` formula without proof.

**T4: An empirical failure mode if theory novelty fails.** A reusable negative result may show common agent-memory evaluations rank an infeasible oracle highest by illegally using deleted contents. This is a different **evaluation paper** and would require concrete, broadly generalizable evidence and verified originality. Do not rebrand an incremental algorithm as a negative result to make the deadline.

## 6. Candidate algorithm architecture (not implemented)

- **Authorization monitor (hard rule, not ML novelty):** provides `g_t`, rejects prohibited reads/writes, deletes agent-controlled state within declared scope, and logs revocation/regrant events.
- **Allowed observation handler:** records only lawful task outcomes and permitted summary statistics; distinguishes `missing reward because unselected`, `unavailable action due to policy`, and `item lost irreversibly`.
- **State-aware estimator:** predicts future *authorized* utility for representations and re-acquisition requests, with uncertainty; never trains on revoked raw contents after revocation without a valid retention basis.
- **Policy optimizer:** chooses valid compression, retention, retrieval, and authorised reacquisition under `B`, accounting for future recoverability and delay in a nonanticipating manner.
- **Shift handler:** models task shifts separately from permission shifts; uses only non-sensitive, permitted covariates for detection.
- **Audit:** every online feature and gradient input is included in a permission-parity report; rejected access attempts are counted, but do not imply DP or certified unlearning.

If this reduces in code and analysis to an existing constrained bandit with trivial masking and an enlarged state, explicitly document that and stop the ICML method track.

## 7. Benchmark and experimental protocol

### Stage 0: analytical testbed

One toy world with `|I|=2–4`, binary demand regimes, exact legal-state transition, one revocation/regrant, delayed authorized re-acquisition. Enumerate all possible legal histories, verify each baseline's permitted observation filtration, and compare exact dynamic programming under the **specified** comparator. Include cases where later regrant never happens; deleted-value future rewards should be irrelevant there.

### Stage 1: simulated regimes

Factorial variations: task shift (none/abrupt/gradual), permission shift (none/revoke/regrant), censoring (none/eligible-only), recoverability (impossible/costly/cheap), reacquisition delay, correlation among items, memory budget, permitted proxy informativeness. Randomize exogenous sequences and hold identical sequences across methods; keep independent regime-generator holdouts. Begin with low-cardinality models before LLM workloads.

### Stage 2: agent integration (only after formal GO)

Connect to synthetic long-memory tasks and optional [LongMemEval](https://arxiv.org/abs/2410.10813) / agent workloads with **simulated, clearly labeled** permission events, preserving the same external monitor for all systems. Do not claim that benchmark-synthetic consent constitutes legal authorization in a deployed system.

### Required baselines

1. Recency/LFU/importance with identical permission monitor.
2. MemPrice; MemPrice + mask; MemPrice + mask + change detector; **MemPrice + mask + delay-aware learner**.
3. OSL-MR under observability parity.
4. State-augmented sleeping-bandit/switching-cost caching with available-action sets and legal reacquisition.
5. Always-reacquire-when-authorized; never-store (privacy-utility reference).
6. Full-information clairvoyant oracle **only as a diagnostic upper bound, never the main regret comparator**.

Report exact implementation/version and missing features of reproduced methods; do not imply reproductions are official without testing them.

### Metrics and controls

**Primary:** normalized authorized utility relative to a declared reachable comparator under *the same legal inputs*, and state-transition-aware learning loss or regret where mathematically defined.  
**Secondary:** hard budget violations, illegal access attempts, legal reacquisition count/delay/cost, dynamic adaptation lag, observed feedback rate, allowed context tokens, storage/compute cost, canary exposure from modelled stores, Pareto utility–cost plots.  
**Stats:** paired seeds and exogenous event sequences; cluster 95% CIs by regime-generator family; report no-shift, task-only, policy-only, joint-shift separately; include negative controls where every item is always eligible or no revocation occurs.

### Ablations

No revocation, reversible compression, zero reacquisition delay, complete feedback, no legal proxy, perfect allowed proxy, no shift detector, no stateful future-cost estimate, equal-budget comparison without special access. An intentional *permission-violating* agent may be used only as a labelled attack/leakage stress reference in a **fully synthetic** sandbox, not a competitive baseline.

## 8. Threat model and privacy limitations

**Trusted components:** authorization ledger, simulator time, legal-use monitor. **Attacker/environment:** user events change permission, tasks shift; optional adversary injects noisy memory/task text but cannot forge ledger events. **Revocation semantics:** local removal from declared agent-controlled stores; not deletion from LLM parameters, provider logs, file backups or other unmodelled surfaces. **Prohibited:** reconstruct revoked raw data from embeddings, or using hidden private ground truth to choose online actions. Track provenance of all learned state.

Privacy claims must remain narrow: compliant online choices *within a model*, not regulation compliance or differential privacy. Authorization shifts may be adversarial or stochastic, but assumptions must be fixed per theorem/test.

## 9. Hard go/no-go and deadline plan

**Mathematical GO:** an independently checked statement is both correct and genuinely not subsumed by known sleeping-bandit/caching/partial-monitoring results; there is a fair algorithmic test showing why it matters.  
**NO-GO:** same reduction + known bound suffices, inaccessible rewards sneak into policies, a theorem relies on clairvoyance, data privacy claims outstrip scope, or baseline gains vanish under matched access.

**Proposed checkpoints:** by **27 Nov 2026** finalize filtration and reduction attempt; by **6 Dec** solve minimum toy model + executable composed baseline; by **15 Dec** formal go/no-go; **only then** scale.  
**ICML 2027:** abstract **14 Jan 2027**, full **22 Jan 2027**, 8 pages body with unrestricted references/appendices ([official CFP](https://icml.cc/Conferences/2027/CallForPapers)). The venue requires a **substantive AI Disclosure Statement**, explicitly including AI-supported ideation, literature synthesis, experimental planning, code/analysis if applicable ([policy](https://icml.cc/Conferences/2027/UseOfGenerativeAIByAuthors)). These AI-assisted planning documents must be accurately accounted for if materially used.

## 10. Final scientific appraisal

**Priority #3; HOLD.** The useful deliverable is a rigorous *question* and falsification strategy. No original regret bound, lower bound, or performance improvement exists yet. The best next action is an independent theory reading/proof exercise, **not** a large agent-memory training pipeline. If the model reduces to known online learning with constrained actions, stop or publish an accurately framed methodological replication/negative result at a suitable venue.
