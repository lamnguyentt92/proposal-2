# IDEA_F1S: Do verifier audits predict wrong passes? Prevalence of false PASS verdicts in mobile-agent benchmarks, measured with a whole-state differential oracle

Redesign of IDEA_F1R after the Stage 6 adversarial review (`06_REDTEAM/IDEA_F1R_review_referee.md`,
`IDEA_F1R_review_devil.md`, `IDEA_F1R_review_feasibility.md`). Review findings applied:
- the cross-task metamorphic instrument is **dominated** by a direct diff against a scripted gold end state, which the design already builds → the gold differential becomes the primary instrument; relations are kept only where they add something (read-only tasks; tasks with several valid end states);
- AndroidWorld has natural inverses for only 25 of 116 templates, 14 of them already integrity-checked; `initialize_task` wipes app state, so composed tasks need a modified harness → composition is no longer required for the main result;
- the "lower bound on single-task passes" did not hold for composed runs → the estimand is now a property of **ordinary benchmark runs**;
- the seeded-fault Rogan–Gladen estimator is incoherent for deterministic checkers → dropped as an estimator; seeded faults are kept as (i) the predictor under test and (ii) a recall measurement for the oracle;
- one benchmark with an app-testing lineage reads as a maintenance paper → a general, falsifiable question and a second benchmark family are added.

- Gap addressed: G6 (+ G3).

- Target venue and track: ICML 2027, area "Evaluation", contribution type "Datasets, Evaluations and Benchmarks" (or "Negative Results", depending on the outcome). The Stage 6 referee rated venue fit 3/5: if the author prefers a venue where audit-style instruments are core, NeurIPS Evaluations & Datasets or ISSTA/ICSE are the step-down options (author's decision).

- Problem (1 paragraph): A 2026 wave of papers audits agent-benchmark verifiers by mutating reference runs or injecting state faults and reporting how many the verifier misses (arXiv:2610.09142; Sun, Research Square rs-10665114; arXiv:2609.22220; six ICLR 2027 submissions on verifier flaws). These are **existence** results. Whether verifier weakness translates into wrong passes on real agent runs — **prevalence** — is unmeasured outside coding benchmarks, where it is obtained by re-grading every pass with a stronger oracle (SWE-Bench+, UTBoost, SWE-ABS, TestJack). For mobile benchmarks nothing is known: arXiv:2607.28367 audited only FAIL verdicts and included no mobile benchmark; arXiv:2605.10448 could decide only half of its 82 AndroidWorld records because post-state was not retained. Reading the AndroidWorld code shows 46 of 116 checkers test only a postcondition, none looks outside its own table, directory or key, and free text passes at a 0.9 similarity threshold — so wrong passes are possible; AndroidWorld is also reported near saturation (arXiv:2602.07787), so what remains to learn from it is whether the passes are real.

- Key insight (the non-obvious observation; 2–3 sentences): A wrong pass needs two things to coincide: a verifier blind spot **and** an agent failure that lands in it. Mutation audits measure only the first, so their kill rates need not predict prevalence — the agent-benchmark version of the "are mutants a valid substitute for real faults" question, which nobody has tested for agent graders. Prevalence itself is cheaply measurable on stateful benchmarks, because a scripted reference run from the same initial state yields a whole-state gold end state; the only real obstacle is legitimate variation (different correct routes, nondeterministic fields), and that can be *measured* by running several distinct correct routes rather than assumed away.

- Approach:
  1. **State observer** for the emulator: typed snapshot and diff of benchmark-app databases, content providers (SMS, contacts), shared storage and settings, taken on unmodified benchmark runs from the shipped initial state.
  2. **Route-diverse gold and measured mask**: for each task, scripted reference solutions along at least two distinct correct UI routes, each repeated; fields that differ across correct runs form the mask. The mask's false-alarm rate is estimated on held-out correct routes; planted unrequested writes give the oracle's recall.
  3. **Whole-state differential oracle**: an agent run that the native checker passes is flagged when its masked end state differs from every gold end state. Read-only tasks need no gold: any persistent change in a passed information-retrieval run is a flag. Tasks with several valid end states are handled by the gold set or, where that is infeasible, by a scripted inverse applied after the agent's run.
  4. **Blind audit**: two annotators, blind to the oracle, adjudicate all flagged passes and a random sample of unflagged passes with retained post-state and screenshots, grading severity (wrong outcome / unrequested change to user data / benign residue). The same is done for a sample of FAIL verdicts, giving both error directions.
  5. **Predictors under test**: per-template verifier weakness measured the way the 2026 audits measure it — kill rate on seeded end-state faults stratified by failure mode, and checker style (postcondition-only vs integrity-checked).
  6. **Second benchmark family**: MobileWorld (public, self-hosted backends, per-task snapshots) and, if resources allow, one API-world benchmark with public mutants (AppWorld, code of arXiv:2610.09142) to test whether the conclusions transfer.

- Contribution type: new measurement (first prevalence estimates of wrong passes and wrong fails on mobile-agent benchmarks) + a preregistered test of whether verifier-audit scores predict them + a reusable oracle.

- Claims (falsifiable):
  - **C1 (prevalence, both directions).** The audited rate of wrong PASS verdicts and of wrong FAIL verdicts per agent, with template-clustered intervals. Pre-specified readings: an upper bound below 1% for all agents is the negative result "verifier flaws are immaterial for this leaderboard"; a lower bound above 3% for at least two agents is the positive result.
  - **C2 (existence does not predict prevalence).** Per-template seeded-fault kill rates and checker style explain little of the per-template wrong-pass rate on agent runs (preregistered: rank correlation below 0.4 with its interval reported; the alternative, a strong correlation, validates the mutation-audit methodology). Either outcome is a finding about a method used by at least four 2026 papers.
  - **C3 (differential oracle error).** Wrong-pass rates differ across agents and scaffolds (mixed model with template random effects); the paper reports whether correcting them changes any pairwise ordering — the empirical test of the inversion condition derived analytically in arXiv:2609.25173, which ran no agents.
  - **C4 (cost).** The differential oracle reaches the recall of a full blind audit of passes at a fraction of the human minutes per newly evaluated agent, and beats an LLM state-reading verifier on precision.

- Closest work and delta (verification levels are in the prior-art reports):
  - arXiv:2610.09142; Sun, Research Square rs-10665114 (DOI 10.21203/rs.3.rs-10665114/v1); arXiv:2609.22220; OpenReview RWjv2Zg0Wa, 8PIpkkfZ84, GWFSBzaPNd, zGz2CHm7x2, VXFTF9Je8S, 0ad4aBnjoQ — verifier audits by mutation/fault injection: existence, not prevalence; no mobile. **They supply the predictor C2 tests.**
  - arXiv:2605.10448 — partial-identification bounds for AndroidWorld from 41 tasks × 2 models, half undecidable without post-state. Delta: retained whole state makes records decidable; point estimates with intervals; all templates.
  - arXiv:2607.28367 — FAIL-only human audit (15.3% wrong FAIL verdicts = 10.7% evaluator false negatives + 4.7% broken tasks), no mobile benchmark. Delta: both directions, mobile.
  - Coding-agent re-grading: SWE-Bench+ arXiv:2410.06992, UTBoost 2506.09289, SWE-ABS 2603.00520, TestJack 2610.10619, arXiv:2609.34262 — prevalence by a stronger oracle in another domain; none tests whether mutation scores predict it.
  - State-diff checks with hand-written expected diffs: Agent-Diff arXiv:2602.11224, EffectMatch arXiv:2609.31301; SABench arXiv:2610.34167 (12.8% of goal-satisfied runs make unauthorised writes, tool agents); AgentRelBench (OpenReview eQH5SQYour). Delta: gold comes from scripted runs with a measured route-diverse mask rather than per-task hand specifications; mobile GUI state; validated by blind audit.
  - Just et al., FSE 2014 (mutants vs real faults); Knight & Ammann 1985 — the software-testing precedent for C2. Thor (ISSTA 2015), Genie, DLD — Android state oracles for apps (method lineage).
  - arXiv:2609.25173 — analytic ranking inversion under differential oracle error; no measurement.
  - Not found by two hunters and one referee: prevalence of wrong passes on any mobile benchmark; any test of mutation-score → prevalence coupling for agent graders. Both hunters rate scoop risk high (arXiv:2610.09142 names a whole-state frame check as future work).

- Evaluation sketch:
  - Pilot gate (agent-free, run first): learn the mask on one correct route and measure false alarms on other correct routes for ~15 templates. If correct routes cannot be told apart from wrong outcomes after masking, the oracle is not viable.
  - Settings: AndroidWorld (116 templates, shipped initial state) and MobileWorld; agents M3A and T3A with one strong and one inexpensive API model, plus 1–2 open 8B-class GUI agents on local GPUs; ≥ 3 seeds; weaker agents included so that failures are not too rare.
  - Baselines, strongest first: (1) full blind human audit of passes (ground truth and cost reference); (2) LLM state-reading verifier over the retained post-state; (3) hand-written expected-diff checks on a subset (Agent-Diff style); (4) raw diff without the measured mask; (5) native checker.
  - Statistics: intervals clustered by template; an audit interval of about 2.0–4.3% at a 3% rate needs ≈ 1,000 passes, so passes are pooled across agents and benchmarks and the achievable precision is stated before data collection; C2 reported with its interval rather than as a threshold test alone.
  - Decisive experiment: precision and recall of oracle flags against the blind audit. Below 0.8 precision, or recall indistinguishable from the LLM verifier, the instrument contribution fails and only the audit numbers remain.

- Resources needed vs available: an x86 Linux host with KVM (or arm64 Mac) for the emulator — **to be confirmed by the author**; no GPU needed for the emulator; commercial APIs (order of a few hundred to a few thousand USD depending on models, to be re-measured in the pilot); 1–2 GPUs for open GUI agents; two annotators. UIAutomator scripting of reference routes is the researcher's published area. AndroidWorld ships no reference solutions.

- Risks and unknowns: (1) wrong passes may be rare (negative-result reading must be adequately powered); (2) route-dependent benign residue may swamp the mask; (3) scripting two routes for many templates is the main engineering cost — the template set can be stratified by checker style; (4) scoop risk is high; (5) venue fit at ICML is moderate; (6) checker defects found must be reported upstream before publication.

- Conference core / journal extension:
  - Core: differential oracle with route-diverse mask, C1–C4 on AndroidWorld + one more benchmark, blind audit.
  - Extension (JAIR / AIJ): safety benchmarks (missed-harm direction), desktop and web benchmarks, automatic synthesis of reference routes, an identification analysis of what whole-state oracles can and cannot certify, checker repair.

- Generator perspective: software-testing transfer + measurement; redesigned by the coordinator after Stage 6.
