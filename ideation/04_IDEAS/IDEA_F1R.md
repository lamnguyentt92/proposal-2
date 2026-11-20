# IDEA_F1R: Passed, but did it? Certified lower bounds and audited estimates of wrong PASS verdicts in mobile-agent benchmarks

Revision of IDEA_F1 (= IDEA_T1 + IDEA_M2) after the Stage 5 novelty attack (one permitted return to Stage 4). Both
prior-art reports (`05_NOVELTY/IDEA_F1_priorart_A.md`, `_B.md`) rated the merged idea **incremental**: the seeded-fault
estimator is Mills / Lincoln–Petersen / Rogan–Gladen and agent-free state seeding with kill rates already exists; the
cross-task metamorphic instrument on agent-generated runs is the part neither hunter found. This card re-centres on that
part and demotes seeding to a tested assumption.

- Gap addressed: G6 (+ G3).

- Target venue and track: ICML 2027, area "Evaluation", contribution type "Datasets, Evaluations and Benchmarks" (fallback "Negative Results").

- Problem (1 paragraph): Mobile-agent benchmarks grade a run with a programmatic check over device state. AndroidWorld is reported near saturation (arXiv:2602.07787), so the open question is whether the passes are real. The audit of computer-use scoring in arXiv:2607.28367 sampled only FAIL verdicts and says false positives among successes were not estimated; arXiv:2605.10448 looked at AndroidWorld passes but could decide only half of 41 sampled records because post-state is not retained. A 2026 cluster mutates *reference* runs to show verifiers accept unrequested changes (arXiv:2610.09142; Sun, Research Square rs-10665114; arXiv:2609.22220) but reports existence (kill rates), not prevalence on agent runs, and covers no mobile benchmark. Coding-agent audits (SWE-Bench+, UTBoost, SWE-ABS, TestJack) get prevalence only by re-grading every pass with a stronger oracle. What is missing is a way to measure, on real agent runs and without labelling each pass, how often a PASS is wrong.

- Key insight (the non-obvious observation; 2–3 sentences): A stateful benchmark's **task suite is redundant**: some tasks undo others, some are idempotent, some commute. So "the checker passed both legs" has a checkable consequence in device state — after T then T⁻¹ the device must be back at its start, up to a noise mask that can be *measured* with scripted round-trips. A passed composition that violates the relation is a **certificate** that at least one verdict is wrong or that an unrequested effect occurred, obtained on agent-generated runs with no human label, no per-task expected diff and no reading of verifier code. This gives prevalence where mutation audits give only existence, and it supplies the missing ground truth to test — rather than assume — whether seeded faults are a valid stand-in for real agent failures.

- Approach:
  1. **State observer** for the Android emulator: typed snapshot of app databases, shared preferences, content providers, settings and file-tree hashes, with typed diff (standard Android-testing instrumentation).
  2. **Fixed-policy controls** (from IDEA_T2): closed-loop scripted reference policies run K times per task and per composition. They give (a) the noise mask and its false-alarm rate on held-out gold runs, (b) checker specificity on known-correct end states, (c) harness flakiness with the policy held fixed.
  3. **Cross-task relations on agent runs**: R1 round-trip (T ; T⁻¹ ⇒ state ≈ start), R2 idempotence (an "ensure X" goal run twice changes nothing the second time), R3 commutation (tasks on disjoint apps). R4 pre-satisfied goal is kept only as a cited replication control (anticipated by OpenReview i7FGehiANA). Coverage of each relation over the suite is reported by a written applicability rule.
  4. **Certified lower bound**: among compositions in which the checker passed every leg, the masked-violation rate lower-bounds P(wrong or extra effect | pass); exact / task-clustered intervals; two annotators attribute each violation to a leg and grade severity (user-data change vs benign residue).
  5. **Seeded-fault calibration as a tested hypothesis**: end-state faults stratified by failure mode (wrong entity, partial completion, near-miss value, uncommitted, collateral change, wrong location) are produced through the app UI by script and validated by two annotators. They measure checker sensitivity per (checker family, mode). A two-sided Rogan–Gladen-style correction (sensitivity from seeds, specificity from step 2) gives a *predicted* false-pass count per agent. Because programmatic checkers are deterministic, sensitivity is estimated at checker-family level across parameterised instances; cells with sensitivity 0 ("blind modes") are reported as non-estimable.
  6. **Blind audit as arbiter**: a stratified random sample of checker-passed runs with retained post-state is adjudicated by two annotators blind to all instruments.

- Contribution type: new measurement instrument + first prevalence measurements on a mobile benchmark + a preregistered test of the seeded-fault assumption for agent graders.

- Claims (falsifiable):
  - **C1 (prevalence).** On a mobile capability benchmark the certified violation rate among checker-passed compositions has a 95% lower confidence bound above 3% for at least two agents. Pre-specified negative result: upper bound below 1% for all agents.
  - **C2 (differential error).** Violation rates differ across agents/scaffolds (mixed-effects test with task-template random effects) and rescoring without violating passes changes the order of at least one pair.
  - **C3 (existence is not prevalence).** Per-template kill rates from gold-run mutation (the arXiv:2610.09142 / Sun method) correlate weakly (Spearman ρ < 0.4) with per-template violation rates on agent runs.
  - **C4 (coupling test).** The seed-calibrated prediction of each agent's false-pass count falls inside the 95% interval of the blind audit. Either outcome is reportable: success licenses cheap per-agent correction; failure is direct evidence that seeded faults do not represent agent failures in this setting.
  - Instrument validity is a precondition, not a claim: planted unrequested writes flagged ≥ 90%, held-out gold runs flagged ≤ 2%.

- Closest work known so far and the delta — see the two prior-art reports for verification levels:
  - arXiv:2610.09142 (AppWorld/WorkArena verifier loopholes) — hand-written edits to reference runs; no prevalence, no agent runs, no mobile; names a whole-state frame check as future work.
  - Sun, Research Square rs-10665114 (DOI 10.21203/rs.3.rs-10665114/v1) — agent-free, class-stratified state-fault injection on τ²-Bench/ToolSandbox/AppWorld, 100/110 rejected. **Covers the seeding step**; no conversion to real false passes, no mobile.
  - arXiv:2609.22220 (ICLR 2027 submission Hdwn4xkEHp) — kill matrix with witnessed denominator; restricts itself to existence claims.
  - OpenReview 7XacL5fqyu (ARR Aug 2026) — metamorphic contracts on a single recorded state, exposing false *failures*; not cross-task, not agent runs.
  - OpenReview i7FGehiANA (ARR Oct 2026) — pre-satisfied-goal inflation → anticipates R4.
  - OpenReview RWjv2Zg0Wa (16.8% of verifiers pass a no-op), 8PIpkkfZ84, GWFSBzaPNd, zGz2CHm7x2, VXFTF9Je8S, 0ad4aBnjoQ; SABench arXiv:2610.34167; AgentRelBench (OpenReview eQH5SQYour) — neighbouring verifier/state-diff audits; none uses cross-task relations on agent runs.
  - Thor (Adamsen, Mezzetti, Møller, ISSTA 2015), Genie (arXiv:2008.03585), DLD (arXiv:2010.05584) — neutral/inverse event sequences as label-free oracles for **apps**; here the relation is pointed at agent runs to expose the **benchmark checker**. Must be cited as the method lineage.
  - Rogan–Gladen-style corrections already ported to LLM/agent grading: arXiv:2606.10315, 2511.21140, 2601.05420. Mills error seeding (1972; primary report not obtained — cite via Duran & Wiorkowski, IEEE TSE 1981, DOI 10.1109/tse.1981.230821). **The estimator algebra is not claimed.**
  - Validity of seeded faults: Just et al., FSE 2014; Knight & Ammann 1985; AUDIT (OpenReview fpeLFP6JEE) — the evidence a referee will use against step 5; C4 is the direct test.
  - Prevalence by re-grading (coding agents): SWE-Bench+ arXiv:2410.06992, UTBoost 2506.09289, SWE-ABS 2603.00520, TestJack 2610.10619, arXiv:2609.34262. Baseline family "why not build a stronger checker".
  - arXiv:2605.10448 (AndroidWorld evidence bounds), arXiv:2607.28367 (FAIL-only audit; two figures for wrong FAIL verdicts, 15.3% and 10.7%, were reported by different readers of this paper — re-check which slice each refers to), arXiv:2609.25173 (analytic ranking inversion under differential oracle error).
  - Not found by either hunter: cross-task relations on agent-generated runs to bound wrong passes; either instrument on a mobile benchmark; validation of seeded-fault calibration against a blind audit of passes. OpenReview was searchable only via its search endpoint; scoop risk is rated high by both hunters.

- Evaluation sketch:
  - Settings: AndroidWorld (arXiv:2405.14573) plus one second mobile benchmark; safety variant on MobileSafetyBench (arXiv:2410.17520) or MobileWorldSafety (arXiv:2608.17659) where "safe and completed" must also satisfy diff ⊆ gold diff; one non-mobile stateful benchmark for a transfer check. Agents: 2–3 API models under ≥ 2 scaffolds + 1–2 open GUI agents on local GPUs; ≥ 3 runs per composition; weaker agents included so failures are not too rare.
  - Baselines, strongest first: (1) state-reading LLM verifier re-grading every pass over retained post-state; (2) hand-written expected-diff checks on a task subset (Agent-Diff arXiv:2602.11224 / EffectMatch arXiv:2609.31301 style); (3) gold-run mutation score; (4) prediction-powered correction from a small audited subset; (5) pooled, unstratified Rogan–Gladen; (6) raw diff without the measured mask.
  - Metrics: violation rate among passed compositions with intervals; flag precision/recall against blind adjudication; false-alarm rate on gold runs; rank changes after rescoring; absolute error and coverage of the seed-calibrated prediction; human minutes and API cost per newly evaluated agent.
  - Decisive experiment (run early on ~15 task pairs): blind adjudication of flagged vs unflagged checker-passed runs. The instrument fails if flag precision < 0.8 or if the agent-run violation rate is indistinguishable from the gold-run false-alarm rate.

- Resources needed vs available: Android emulators with root/adb/SQLite access and UIAutomator scripting (researcher's published area; emulator availability still to be confirmed in 00_CONSTRAINTS); commercial APIs; 1–2 GPUs for open GUI agents; two annotators (language-independent task). No model training.

- Risks and unknowns: (1) applicability — reversible pairs cover part of a suite; which AndroidWorld tasks form inverse pairs has not been checked in the repository; (2) most violations may be benign residue — severity grading decides whether C1 matters; (3) deterministic checkers may make seeded sensitivity 0/1 per cell, leaving C4 uninformative; (4) scoop risk: arXiv:2610.09142 publicly names the gap and six ICLR 2027 submissions work on verifier flaws; (5) "audit paper" perception at ICML — the instrument-plus-validation framing is the defence; (6) near-zero violation rate is publishable only as a well-powered negative result.

- Conference core / journal extension:
  - Core: relations R1–R3 with measured mask, prevalence bounds and rescoring on one mobile benchmark, coupling test C4, blind audit.
  - Extension (JAIR / AIJ): safety benchmarks at full scale, desktop and web benchmarks, automatic synthesis of inverse tasks, estimator theory under mode misclassification, checker repair from surviving faults.

- Generator perspective: software-testing transfer + measurement, revised by the coordinator after Stage 5.
