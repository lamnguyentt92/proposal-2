# IDEA_T1: SeedCount — estimating how many PASS verdicts are wrong from seeded end-state faults (mobile-agent graders)

- Gap addressed: G6 (false positives/negatives in grading computer-use/mobile agents), with G3 for the safety-grader arm.

- Target venue and track: ICML 2027, topic area "Evaluation (methodology, meta-studies, replicability)", contribution type "Datasets, Evaluations and Benchmarks". (Fallback contribution type if the decisive experiment fails: "Negative Results".)

- Problem (1 paragraph):
  Mobile-agent benchmarks grade a run with a programmatic check over device state (SQLite rows, files, settings). Audits show these checks are wrong often enough to matter, but nobody can say *how many reported successes are false for a given agent*. The re-audit in 2607.28367 sampled only FAIL verdicts (15.3% wrong) and states that false positives among successes are not estimated. The evidence-bounds audit 2605.10448 did look at AndroidWorld passes, but on 41 sampled cases x 2 models it could decide only half of the records (P/F/U = 13/28/41; native score 61.0%, supported bound [15.9%, 65.9%]) because post-state is not retained, and it needs an LLM-drafted checklist plus two-researcher review per record. Mutation-style audits of graders have appeared in 2026 (see "Closest work"), but they report *mutant survival counts*, which describe a hand-written mutant set, not the leaderboard. Direct human audit of every PASS for every new agent does not scale. The missing object is an estimator of the agent-specific false-pass count with an interval, that does not require reading the passes.

- Key insight (the non-obvious observation; 2–3 sentences):
  The failures a grader *did* catch are a thinned sample of all failures, and the thinning probability per failure mode is a property of the grader alone, measurable without any agent by seeding end-state faults of that mode on the emulator. This is the fault-seeding (Mills) / Horvitz–Thompson argument from software reliability: if the grader kills a fraction d_m of seeded faults of mode m and caught n_m real failures of mode m from agent a, then about n_m * (1 - d_m) / d_m failures of that mode slipped through as PASS. Because agents differ in their failure-mode mix, the false-pass rate is agent-specific — exactly the "differential oracle error" that 2609.25173 shows analytically can invert a ranking and says is unmeasured — and it becomes computable from each agent's *failed* runs plus one agent-free kill matrix.

- Approach (how the insight becomes a method/system/theory):
  1. Reference end-states. For every task instance, a closed-loop UIAutomator gold script (resource-id selectors, explicit waits) produces the correct end-state; the native checker must pass it (known-answer control).
  2. State-level fault seeding, stratified by failure mode. Operators are derived from observed agent failures, not from the checker source: M1 wrong entity (correct action on a sibling contact/note/event), M2 partial completion (subset of required items/fields), M3 near-miss value (date +-1, AM/PM, unit, trailing text), M4 uncommitted (visible in UI, not persisted), M5 collateral change (extra delete/edit of unrelated state), M6 wrong location/app (right content, wrong folder or app), M7 null agent, M8 (safety tasks) harm realised by a route variant (other recipient, other path, other app). Each seeded fault is produced *through the app's own UI by a script* (so it is reachable), and enters the denominator only if two annotators independently judge that it violates the instruction (the analogue of the "witnessed mutant" rule in 2609.22220; equivalent mutants are quarantined).
  3. Kill matrix K[task, mode] -> survival s_{t,m} with a Beta posterior.
  4. Failure-mode labelling of each agent's grader-detected FAIL runs from the emulator state diff (LLM-assisted, human-validated on a sample; confusion matrix estimated).
  5. Estimator. FP_hat(a) = sum_{t,m} n_{a,t,m} * s_{t,m} / (1 - s_{t,m}), with partial pooling across tasks sharing a checker family; interval by task-clustered bootstrap combined with posterior draws of s. Modes with s = 1 ("blind modes") are not estimable: they are reported separately as an explicit lower-bound caveat and are the only place a direct audit is still required.
  6. Output: corrected success (and, for safety benchmarks, corrected harm) rates per agent with intervals, a test of whether the correction changes any pairwise ordering, and the kill matrix as a reusable artefact for benchmark maintainers.
  The single assumption — within a (checker family, mode) stratum a seeded fault is as detectable as an agent's real fault — is the agent-evaluation version of the "are mutants a valid substitute for real faults" question (Just et al., FSE 2014; record seen at https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014-abstract.html) and is tested directly by the decisive experiment.

- Contribution type: new measurement/benchmark (with a new estimator; a negative result if the stratified coupling assumption fails).

- Claims (falsifiable, 2–4):
  C1. On AndroidWorld and one second mobile benchmark, a non-trivial share of (task, mode) cells have s > 0, concentrated in M5 (collateral change) and M6 (wrong location). Falsified if survival is ~0 everywhere.
  C2. For each agent, the predicted false-pass count lies inside the 95% interval of a blinded two-annotator audit of a random sample of that agent's PASS runs with full emulator post-state, and its absolute error is lower than every baseline below.
  C3. False-pass rates differ between agents by more than their intervals (agent-specific oracle error), so a single pooled correction is wrong; reported together with whether any top-of-leaderboard ordering changes after correction.
  C4. For safety checkers, seeded harms reached by a route variant (M8) survive at a higher rate than canonical-route harms, i.e. missed-harm error is larger than missed-failure error.

- Closest work known so far (with identifiers) and the expected delta:
  Prior-art check run in this session (queries: "mutation testing agent benchmark grader", "oracle problem agent evaluation", "fault seeding / capture-recapture false passes"): mutation of graders is NOT new in 2026; the estimator and the mobile setting are what I did not find.
  - 2610.09142 "Finding Side-Effect Loopholes in AppWorld and WorkArena Verifiers" [abstract read]: hand-written edits to correct runs, designed from the verifier source; all confirmed false positives were unrequested changes. Delta: no mobile, mutants not derived from agent failures, no translation of survival into a false-pass count.
  - "Red-Teaming the Grader: Mutation-Validated Constraint Checking for Tool-Agent Benchmarks", NeurIPS 2026 workshop "Who Verifies the Agents?" (https://neurips.cc/virtual/2026/172887, OpenReview zh33pqlBjf) [page read]: mutation probes on reference solutions of the author's own 800-scenario benchmark; states "No single component is new". Delta: self-hardening of one benchmark, no estimator.
  - 2609.22220 "Measuring the Checker: Mutation Analysis for GPU-Kernel Benchmark Oracles" [read]: witnessed denominator, official check misses 16.9% of 7,384 witnessed faults; realism probe of only 60 problems. Delta: different domain; does not predict real false accepts on a leaderboard.
  - 2605.10448 "Can Agent Benchmarks Support Their Scores?" [read]: three-state evidence labels and partial-identification bounds on five benchmarks including AndroidWorld. Delta: needs per-record LLM+human review and retained artefacts; gives wide bounds, not a point estimate; no agent-free component.
  - 2607.28367 (FAIL-only audit; names the missing false-positive estimate), 2609.34262 (LLM judges over 3,810 passing coding trajectories), 2609.25173 (analytic ranking-inversion condition under differential oracle error, no measurement), 2610.16067 (fault injection *into the oracle* of tau-bench to validate an audit suite), 2609.00038 (fault injection into trajectories to test LLM judges; paired discrimination), 2611.02624 and OS-Sentinel 2510.24411 [arXiv record seen in search listing] (state-reading harm judges), 2507.02825 (checklist).
  - Not opened, listing only: TestJack 2610.10619, PartHackBench 2609.29578, BenchGuard 2604.24955 (abstract read: LLM cross-verification, no mutation), "AUDIT: Validating LLM Judges Through Controlled Error Injection" (NeurIPS 2026 workshop page read; does not estimate real-world judge error from injections).
  - Source-status note: the Mills error-seeding model was confirmed only through secondary pages in this session (no primary record fetched); locate and read the original before citing it in a manuscript.
  Expected delta in one line: first method that turns seeded-fault detection into an agent-specific, interval-valued estimate of false passes, validated against a human audit, and first application to Android device-state success and safety checkers.

- Evaluation sketch: settings, baselines (strongest first), metrics, decisive experiment
  Settings: AndroidWorld 2405.14573 (116 templates, device-state checkers); a safety arm on MobileSafetyBench 2410.17520 or MobileWorldSafety 2608.17659 (rule check then LLM judge); optionally AndroidLab 2410.24024. 4–6 agents spanning strength: frontier API models in a standard scaffold plus open GUI models on the local GPUs, 3 seeds each.
  Baselines: (B1) direct audit of every PASS by a state-reading LLM verifier over retained post-state (the 2611.02624 / 2605.10448 style) — the "why not just audit?" baseline; (B2) prediction-powered correction: small human-audited subset + LLM-judge labels on the rest; (B3) Rogan–Gladen correction with one pooled survival rate (unstratified mutation score); (B4) raw mutation score as in 2610.09142.
  Metrics: absolute error and interval coverage of predicted false-pass count against the human audit; change in pairwise orderings (Kendall tau) after correction; human minutes and API cost per newly evaluated agent.
  Decisive experiment (preregistered): freeze the kill matrix and the estimator, predict the false-pass count per agent, then run the blinded audit of ~300 PASS runs per agent with emulator snapshots. If predictions fall outside the audit interval for most agents, the stratified coupling assumption is false for agent graders and the method is refuted.

- Resources needed vs available (00_CONSTRAINTS.md):
  Needed: Android emulator farm on CPU with snapshot/adb/SQLite access, gold UIAutomator scripts, seeded-fault scripts; API budget for roughly 116 tasks x 3 seeds x 5 agents plus LLM-assisted labelling; 1–2 GPUs for open GUI agents; two independent annotators for mutant validity and the PASS audit. Available: emulator and automated-testing expertise (published), commercial APIs + 1–2 GPUs, >=2 annotators fluent in English (the audit is language-independent). No model training. Emulator availability is marked "(chưa khai báo)" in the constraints and must be confirmed.

- Risks and unknowns:
  1. Near-saturated benchmarks yield few detected failures, so n_{a,t,m} is small and intervals wide; mitigation: include weaker agents, harder parameter seeds, a second benchmark.
  2. Blind modes (s = 1) may carry most of the false passes; then the estimator is only a lower bound and the contribution shifts toward the kill matrix.
  3. Failure-mode labelling error propagates; needs the confusion-matrix correction.
  4. The coupling assumption may fail (seeded faults easier or harder to detect than real ones).
  5. Scoop risk is real: at least four 2026 preprints mutate graders; adding an estimator is a natural next step for any of them.
  6. "Audit paper" perception at ICML; the estimator-plus-validation framing is the defence.
  7. I did not search GitHub issue trackers of the benchmarks or OpenReview submissions under review.

- Conference core / journal extension (1 line each):
  Core: estimator + kill matrices for AndroidWorld and one mobile safety benchmark + preregistered human-audit validation.
  Extension: desktop/web benchmarks, estimator theory under mode misclassification and dependence, automatic checker repair synthesised from surviving faults (JAIR/AIJ).

- Generator perspective: cross-domain transfer (software testing)
