# IDEA_T2: Whose variance? Zero-decision-variance reference policies separate harness flakiness from agent inconsistency

- Gap addressed: G3 (validity of agent benchmark numbers, absence of variance reporting on mobile benchmarks), touching G6 (wrong FAIL verdicts).

- Target venue and track: IJCAI 2027 Main Track (no topic list; 7 pages + 2 pages references; a compact "new problem + method + measurement" paper). If the result is negative it fits ICML 2027 "Evaluation" with contribution type "Negative Results" instead.

- Problem (1 paragraph):
  Repeated-run metrics (pass^k, run-to-run standard deviation, reliability coefficients) are becoming the standard reading of agent benchmarks: 2602.07150 on SWE-bench Verified, 2604.17849 on OSWorld, 2610.00651 across 22 benchmarks. All of them read run-to-run disagreement as a property of the agent or its scaffold. On an emulated phone that reading is unsafe: a correct decision can still be graded FAIL because the screenshot was taken before the UI settled, an input event was dropped under host load, state leaked from the previous task, or the checker read state mid-write. The AndroidWorld paper (2405.14573, ICLR 2025) itself reports variation at a fixed seed and attributes it to model non-determinism, with no control that holds the policy fixed; its interface exposes an optional wait-to-stabilise heuristic. 2602.07787 calls AndroidWorld near-saturated at pass^3 = 94.0% — whether the missing 6 points belong to the agent or to the harness is currently undecidable. For safety benchmarks the same defect is worse: an injected element that had not rendered when the observation was taken is scored "safe".

- Key insight (the non-obvious observation; 2–3 sentences):
  Software testing defines a flaky test as one whose verdict changes while the code is held fixed; agent benchmarks never hold the "code" (the policy) fixed, so harness flakiness is unidentifiable and is silently booked as agent inconsistency. A closed-loop scripted reference policy has zero decision variance yet is exposed to the same emulator, observation protocol, reset logic and checker, so its failure rate isolates the harness term and its pass^k is a noise ceiling on the pass^k any agent can be measured to have. Once the harness term is isolated, the classic flaky-test root causes (async wait, order dependence, time; Luo et al. 2014 as cited in 2610.16067) and their known remedies transfer directly.

- Approach (how the insight becomes a method/system/theory):
  Three controls, each holding more of the policy fixed than current practice:
  - R1 "ideal-sync" gold script: UIAutomator selectors with wait-for-element. Failures = environment + reset + checker flakiness.
  - R2 "harness-sync" gold script: the same decisions, but each action is computed from the observation the harness actually returns under its default wait policy (stale tree -> mis-tap). R2 minus R1 = async-wait flakiness caused by the observation protocol.
  - R3 cached agent: a real agent whose LLM responses are cached and keyed by observation hash (accessibility-tree agents), so any divergence between two runs originates in the harness.
  Protocol: (i) rerun each control many times per task; (ii) Shaker-style stress (CPU throttling, parallel emulators, animation scale) to expose load dependence (Shaker is evaluated for Python projects in 2609.25528 [listing only]); (iii) iDFlakies-style order permutations to find polluter–victim task pairs (iDFlakies, ICST 2019; record seen at https://par.nsf.gov/biblio/10101224); (iv) root-cause each reference failure into the flaky taxonomy.
  Ceiling: with h_t the per-run probability that the harness does not spoil a correct execution of task t, observed success q_t <= p_t * h_t, hence observed pass^k <= mean_t h_t^k =: C_k, and p_t is recoverable as q_t / h_t under a stated independence assumption, which is checked by open-loop replay of each agent's own successful traces.
  Fix: replace fixed sleeps by idle synchronisation (window-stable accessibility events / frame statistics), restore a snapshot between tasks, make checkers read after quiescence; re-measure.

- Contribution type: new problem (harness-attributable flakiness as an unidentified term in agent reliability metrics) + new method + new measurement.

- Claims (falsifiable, 2–4):
  C1. Under default settings on a standard host, reference policies R1/R2 fail in more than 1% of runs and at least 5% of tasks have h_t < 0.95 on at least one of two mobile benchmarks. Falsified if the harness is clean.
  C2. The reference failure rate rises monotonically with host load, and a cached agent (R3) moves by more than the gap between adjacent public leaderboard entries when only load changes — i.e. scores from different hosts are not comparable.
  C3. Each studied benchmark contains at least one polluter–victim task pair: the verdict of a reference script depends on which task ran before it.
  C4. Idle synchronisation plus snapshot restore removes at least 80% of reference-policy failures and raises real agents' pass^k more than their pass@1.

- Closest work known so far (with identifiers) and the expected delta:
  Prior-art check run in this session (queries: "flaky agent benchmark", "nondeterminism replay AndroidWorld", "noise ceiling pass^k scripted policy"): variance of agentic evaluation is well studied; holding the policy fixed inside a GUI/emulator harness was not found.
  - 2602.07150 "On Randomness in Agentic Evals" [read]: 60,000 SWE-bench Verified trajectories; names tool execution/timing as a possible source but measures only total variance. Delta: no decomposition.
  - 2604.17849 "On the Reliability of Computer Use Agents" [abstract]: OSWorld repeated runs; sources named are execution stochasticity, task ambiguity, agent variability. Delta: no fixed-policy control.
  - "The Instrument Moves: Unrecorded Serving Changes in Agent Benchmarks", NeurIPS 2026 workshop (https://neurips.cc/virtual/2026/173007, OpenReview QEyFDDTHxp) [page read]: pins every exposed control of a mobile-agent benchmark, finds temperature-0 non-determinism and an unannounced endpoint shift; two single-run scores need about an eight-point gap. Delta: isolates the *serving* side; the emulator/observation/reset side is untouched.
  - 2610.16067 [read]: treats the harness as system under test; invariant INV-3 (verdict independent of scoring order) and a non-restoring reward function on tau-bench (94.3% -> 65.5%). Delta: text tool benchmark, oracle integrity only, no timing or load, no ceiling.
  - 2611.11216 "Replay Fidelity ... AppWorld" [read]: hidden RNG state under fixed-code replay. Delta: replay eligibility for debugging, not score attribution.
  - 2610.00651 (reliability depends on whether the claim is about a system or a model), 2608.07775 AndroidReality (deliberate perturbations to test agents — the opposite direction), 2610.19900 GraceBench [read] (agent-side execution stability on physical devices), 2609.20625 Chronicle [listing only].
  Expected delta in one line: first identification of the harness-attributable share of run-to-run disagreement in mobile-agent benchmarks, with a measurable ceiling on pass^k and a tested remedy.

- Evaluation sketch: settings, baselines (strongest first), metrics, decisive experiment
  Settings: AndroidWorld 2405.14573; a second capability benchmark (AndroidLab 2410.24024 or MobileWorld 2512.19432 [listing only]); the injection subset of MobileSafetyBench 2410.17520 to show the effect on ASR. 3 load levels x >= 30 runs per reference script; 3–4 real agents at temperature 0 with 10 runs.
  Baselines: (B1) variance-component / reliability analysis from k reruns as in 2610.00651 — the strongest existing tool, which cannot name the source; (B2) current practice: fixed seed, temperature 0, k reruns (2602.07150); (B3) stress injection applied to agents without any reference policy.
  Metrics: h_t and C_k with task-clustered intervals; harness share of total variance (law of total variance using R3); number of polluter–victim pairs; failures removed by the fix; rank stability across hosts (Kendall tau).
  Decisive experiment: all reference scripts x 30 runs x 3 loads under the unmodified harness, plus order permutations. If the failure rate stays below 0.5% at every load and no polluter is found, harness flakiness is immaterial and C1–C3 are refuted.

- Resources needed vs available (00_CONSTRAINTS.md):
  Needed: CPU machines running several emulators, gold UIAutomator scripts for every task, load-injection tooling, modest API budget (cached agent runs are cheap), optional GPU for one open GUI model. Available: this is the researcher's published area (automated Android app testing, automated evaluation frameworks); APIs and 1–2 GPUs suffice. Annotators are not required. Emulator availability to be confirmed.

- Risks and unknowns:
  1. The harness may simply be clean (AndroidWorld fixes the clock and has per-task setup/teardown); then only a short negative result remains.
  2. Screenshot-based agents cannot be cached exactly (pixel noise), so R3 is limited to accessibility-tree agents.
  3. The ceiling relies on the reference path being spoiled as often as the agent's path; agents are slower and take other routes, so the bound is approximate.
  4. Reviewers may see engineering rather than AI; needs the identifiability framing and the ceiling result up front.
  5. Seven pages is tight for two benchmarks plus a fix.
  6. Gold scripts are shared infrastructure with IDEA_T1; the two papers must not reuse claims or results.

- Conference core / journal extension (1 line each):
  Core: three controls, the pass^k ceiling, root-cause taxonomy and the fix on two mobile benchmarks.
  Extension: desktop/web harnesses, formal identifiability conditions for variance attribution, a maintained de-flaked harness with a cross-host longitudinal study.

- Generator perspective: cross-domain transfer (software testing)
