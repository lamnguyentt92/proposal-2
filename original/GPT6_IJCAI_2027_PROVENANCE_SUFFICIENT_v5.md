# IJCAI 2027 — FINAL REVISED RESEARCH PROPOSAL v5

## PROVENANCE-SUFFICIENT: Decision-Sufficient Memory Abstraction under Conflicting Evidence for Long-Horizon AI Agents

**Research status:** **Exploratory hypothesis — NOT demonstrated novel; NO theorem, experiment, or dataset completed.**  
**Authoring status:** planning document prepared with AI; **not manuscript text**.  
**Meta-decision:** **PIVOT / SMALL FORMAL PILOT ONLY**.  
**Supersedes:** v4 `EPISTEMIC-COMMIT`; action guards and contingent planning are no longer proposed as headline novelty.

## 1. One-sentence scientific thesis

Study **which trust-labelled correlations and alternative support relationships an agent memory must retain during compression** so that later safety-sensitive *query–action decisions* remain equivalent to decisions made with the complete legal evidence history, under a fixed storage/query budget and explicitly assumed trust model.

**Important distinction:** Belief-state planning, information gathering, and source verification are established. The candidate new result, if any, must concern a **nontrivial decision-sufficient compression/representation** for a sharply defined class of agent-memory evidence, not simply a new name for belief-state planning.

## 2. Venue-specific research questions

**RQ1 — Sufficiency:** What task-dependent statistic of a long history `H` preserves the actions and evidence queries necessary for deciding high-impact irreversible tool effects without retaining every raw message?

**RQ2 — Complexity:** For which restricted dependency/source structures can the smallest or a bounded-approximation decision-sufficient representation be computed efficiently? Is the problem already solved by standard knowledge compilation or belief abstraction?

**RQ3 — Robustness to corrupt memories:** When one source is unreliable, can the compressed representation retain enough independent support to select informative queries without converting that source's text into permission/authority?

**Primary hypothesis (must be falsified):** A problem-specific support-correlation representation has a measurable advantage in decision-equivalence per memory bit **over classical factored belief-state and knowledge-compiled representations with the same legally available information**. Without that advantage, the paper is NO-GO.

## 3. Novelty boundary: what this paper CANNOT claim

- Not first to use sets of possible worlds / belief states, contingent sensing, active diagnosis, or risk-sensitive verification.
- Not first to track derivation lineage, detect stale plans, use trusted reference monitors or revise a memory graph.
- Not first to block malicious memory or certify revocation.
- Not a cryptographic guarantee of world truth, external transaction atomicity, data deletion, or adversarial robustness against compromised authority.
- Not a novel theorem merely because `∀w∈B, Pre(a,w)` implies a robust admissible action.

Closest technical confrontation: [Rintanen (IJCAI 2005)](https://ijcai.org/proceedings/2005/128), [Bonet & Geffner (IJCAI 2011)](https://ijcai.org/proceedings/2011/324), [Causal Belief Decomposition (IJCAI 2013)](https://ijcai.org/proceedings/2013/336), [Fadnis & Rintanen, Generalized 3-Valued Belief States](https://research.aalto.fi/en/publications/generalized-3-valued-belief-states-in-conformant-planning/), [ATR](https://arxiv.org/abs/2609.08015), [PlanFence](https://arxiv.org/abs/2609.03340), [AMV-Guard](https://arxiv.org/abs/2610.31446). Review proofs and implementations of these sources before claiming any reduction, complexity result, or advantage.

## 4. Motivating *illustrative* counterfactual pair

Consider a fictional supply-order agent. A trusted source `S1` states `item is eligible for replacement`. A lower-trust imported summary `S2` claims `the customer approved destination change`. A second independent signed record `S3` may or may not corroborate `S2`. An externally checked policy `A` allows only actions that meet both authorization and factual preconditions.

Two histories can share the **same bag of atomic memory facts and marginal confidence scores** while differing in whether `S1` and `S3` are independent support or copies of the same upstream record. If the agent compresses away the dependency relation, it may choose the wrong trusted query (or overstate confidence). A compact summary that retains the actual source-dependency relation may support a better plan.

**Hard reviewer challenge:** classical belief-state planners and probabilistic graphical models can represent dependence. Thus the example is **not evidence of novelty**. The experiment must compare at *equal storage budget* to sound classical relational/factor representations, and demonstrate a precise structural or computational advantage—not just beat a bag-of-facts ablation.

## 5. Formal candidate (not a proved result)

Let a history be `H=(E,Γ,A,τ)` where `E` is source-labelled observations, `Γ` is a set of compatibility/dependence constraints, `A` is an authenticated external authorization reference, and `τ` is a time model. A memory abstraction `M=σ(H)` contains at most `B` bits/tokens under a declared encoding. A later task `d` has a family of actions `Act(d)` and allowed trusted queries `Q(d)` with cost `c(q)`.

A full-history planning problem induces an *information state* `b(H,d)` and a feasible set of contingent query/action policies `Π(H,d,K)` under total query cost `K`. The compressed-history problem yields `Π(M,d,K)`. Define `V*(H,d,K)` from an explicit legitimate-progress utility and constraints; define `V*(M,d,K)` analogously with **exactly the same observation model**. The candidate `ε`-sufficiency criterion is:

```
For all tasks d in D and query budgets K in Kset:
  |V*(H,d,K) - V*(σ(H),d,K)| <= ε
  AND the abstraction does not permit an unsafe commit excluded by H,
  under the stated soundness assumptions.
```

The precise quantifier over `D`, tolerance/utility, abstraction semantics, handling of source corruption, and whether full history contains inadmissible raw data **must be fixed before any theorem**. It is possible that an exact belief-state representation is already the minimal sufficient statistic; this is a required null model. If `σ(H)` silently has access to external trusted queries unavailable to baseline, the evaluation is invalid.

**Proposed result targets — currently unproved:**

- T1: characterize conditions where naive factorized marginal compression loses a relevant correlation; *this elementary counterexample is an ablation justification, not a headline theorem*.
- T2: prove an original bound/algorithm for a narrow evidence graph class (e.g., bounded incidence-treewidth with a constrained query family) and compare directly to compiled belief representations. If a known algorithm matches, T2 is not original.
- T3: derive an explicit cost/decision-equivalence guarantee for an approximate representation under **stated, checkable** assumptions, or report its impossibility with a genuinely informative separation.

## 6. Candidate algorithm, only if T2/T3 survives the literature audit

1. **Typed evidence extraction:** attach source identity, time, signed/unsigned provenance and relation links to memory items. LLM extraction is evaluated as a separate noisy front-end and never grants authority.
2. **Support structure:** represent independent, dependent and mutually incompatible support as a compact constraint graph / circuit; never infer independence from superficial text similarity.
3. **Task-indexed abstraction:** retain only source relations required for a declared set of action preconditions and allowed query outcomes; preserve conservative uncertainty.
4. **Decision checker:** use a conventional contingent planner over the resulting information state; external reference monitor handles authorization and factual checks supported by target API.
5. **Verification allocator:** select safe source queries under a fixed cost budget. The allocator is **not** a novel claim unless differentiated from active sensing/VOI.
6. **Audit and fallback:** on unsupported evidence, missing source provenance, or an unverified precondition, defer irreversible commit; log abstention and missed legitimate work.

Do not claim worst-case safety unless the stored uncertainty set covers the true state and commit-time checking is atomic for every required predicate. In non-atomic real tools, report risk empirically without a guarantee.

## 7. Pilot benchmark: decision-equivalent memory abstraction

**Status:** proposed, not built. **Unit:** one finite evidence-dependency graph with exact possible worlds, source reliability assumptions, available queries, external authorization, and a later action-precondition set.

**Pilot design:** 20 manually specified families, each with (a) a version that changes only source dependence, (b) source-signature conflicts, (c) irrelevant edits, (d) false provenance, (e) conflicting parallel supports, (f) query failure/delay. Start with 2–6 Boolean latent variables permitting exhaustive enumeration; only scale after a proof-level gap is found. Prepare an independent set of natural-language renderings to test the extraction front-end separately.

**Baselines (all same allowed inputs and memory budget):** `bag-of-facts`, full-record retrieval with query cost accounted for, exact belief-state planner, classical factored belief abstraction, knowledge-compiled constraints, ATR+AMV+monitor, and oracle full-state (diagnostic only). A fixed `always query` and `always abstain` reference highlights cost/trivial safety. The strongest main comparator is **classical factor/compiled representation + contingent planner + trusted authority**, not an impoverished vector-store summary.

**Primary metrics:** decision equivalence over legal actions/queries; memory bits/tokens; authorized completion under fixed safety cap; false irreversible commits; source queries and time.  
**Secondary:** false abstentions, plan quality, extraction/provenance errors, world-coverage violation, sensitivity to query reliability, worst-case memory-growth under graph width.  
**Ablations:** remove correlation links; remove source labels; replace precise constraints with marginal confidence; vary budget; vary graph width; remove trusted monitor **only in closed simulator for illustration**; break soundness assumptions.

**Statistics:** exact enumeration where possible; for larger instances repeated independent graph families, not just repeated prompts. Pareto curves storage–decision error–query cost with paired confidence intervals. Do not aggregate unsupported tool-execution safety into a single positive rate.

## 8. Threat model, security & privacy

**Adversary:** supplies untrusted memory summaries, altered tool text, or copied-source evidence; cannot forge trusted signatures, modify the authority ledger, bypass effect guard, or corrupt every trusted data origin. **Defender:** can reject, verify or request trusted evidence. **Privacy:** minimization of retained material is a potential ancillary benefit, not proved DP or lawful deletion. No real payment operations or sensitive account data should be used in pilot.

**Failure assumptions:** false authority labels, unmodelled true worlds, policy races or non-atomic external actions can invalidate safety. Explicitly publish those failure cases; avoid 100% security claims.

## 9. Hard go/no-go tests

**GO only if all of the following become true:** (i) full-text literature audit shows a specific unsolved representation class; (ii) a **nontrivial** formal result is derived/proved or a striking reproducible negative-result distinction exists; (iii) strongest classical alternative at equal budget cannot match the result; (iv) gains survive different graph families.

**NO-GO** if source correlations are fully captured by standard factor/compiled belief methods under equivalent resources, if the result is a reformulation of planning with sensing, if only poor LLM parsing produces a gap, or if safe execution is solely due to the reference monitor.

## 10. Practical work plan and venue requirements

- **By 27 Nov 2026 (proposed):** reconstruct 20 exact cases; read belief-abstraction/knowledge-compilation sources; formalize sufficiency and decision cost.
- **By 6 Dec:** reproduce exact planner and two compact classical baselines; search for a strict structural limitation.
- **By 15 Dec:** mathematical go/no-go decision; if no original result, stop IJCAI manuscript preparation.
- **Only if GO:** produce reproducible simulator, tested bounds and independent scenario-family evaluation.

**IJCAI 2027 Main Track:** abstract deadline **4 Jan 2027**, full paper **11 Jan 2027**, maximum **7 content pages + 2 reference pages** ([official CFP](https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/)). **Important authorship restriction:** LLMs may polish author-written text but must not generate new submission content; this document is research ideation and **must not be copied into the manuscript**. Authors should independently derive and write any final paper and seek official clarification where appropriate.

## 11. Final scientific appraisal

**Priority:** #2 for exploratory work, but **NO-GO as a committed IJCAI paper at present**. Its only defensible prospect is a genuinely novel **decision-sufficient, source-correlated memory abstraction with formal or exceptionally strong algorithmic evidence**, distinct from classical contingent planning. The v5 revision makes that possible test explicit and preserves a principled stop condition.
