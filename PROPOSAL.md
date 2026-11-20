# Idea specification (Proposal 2, ICML 2027): Are the Passes Real? A State-Level Audit of Mobile-Agent Benchmark Verdicts and a Test of Whether Verifier Mutation Scores Transfer to Real Agent Failures

**Status (2026-11-20): CONDITIONAL GO — agent-free pilot gate first. Nothing built, no experiment run, no result exists.**
**Lineage:** new idea (replaces the GPT-6 drafts PROVENANCE-SUFFICIENT and REVOCATION-FEEDBACK, both dropped) → IDEA_T1 + IDEA_M2 → F1 → F1R (after the novelty attack) → F1S (after the adversarial review) → this specification (after the kill argument and the novelty drift scan).
**Author decisions recorded 2026-11-20:** (1) this proposal is confirmed as one of the two final proposals; (2) ICML 2027 stays the target and **AppWorld is added as a required benchmark** to support a generality claim; (3) testbed confirmed — a computer for the Android emulator and **three rooted physical Android phones (Magisk)**.
**Venue honesty:** novelty verdict *incremental with one open core*; the simulated ICML referee scored venue fit 3/5. ICML 2027 (area "Evaluation", type "Datasets, Evaluations and Benchmarks" or "Negative Results") is the named target; NeurIPS Evaluations & Datasets and ISSTA/ICSE remain the fallback if kill criterion K2 fires.
**Authoring note:** AI-assisted planning document. ICML 2027 requires an AI Disclosure Statement covering ideation, literature synthesis and experiment planning; declare this document.

## 1. Problem and motivation (with evidence)

Mobile-agent benchmarks grade a run with a programmatic check over device state. What is known about verdict errors:

- **Existence, not prevalence.** A 2026 wave audits verifiers by mutating reference runs or injecting state faults and reporting kill rates: arXiv:2610.09142 (AppWorld/WorkArena), Sun (Research Square rs-10665114), arXiv:2609.22220, and six ICLR 2027 submissions on verifier flaws. Their authors restrict themselves to existence claims.
- **Trajectory-level prevalence exists, state-level does not.** MobileJudgeBench (arXiv:2608.11434) scores AndroidWorld's checker against human labels on 205 trajectories (52 tasks): precision 98.6, recall 87.2 — roughly 1.4% of passes wrong and 13% of real successes rejected — but labels come from screenshots and UI trees, so unrequested changes to device state are invisible, and it is a by-product without intervals. AgentRewardBench (arXiv:2504.08942) reports rule-based evaluator precision 83.8 / recall 55.9 on web agents and a rank swap. arXiv:2605.10448 could decide only half of its 82 AndroidWorld records because post-state was not retained. arXiv:2607.28367 audited FAIL verdicts only and no mobile benchmark.
- **Blind spots are real.** Reading AndroidWorld's code (commit 55ddaf5): 46 of 116 checkers test only a postcondition, none looks outside its own table, directory or key, and free text passes at a 0.9 similarity threshold; MobileWorld's history shows a checker that returned success for a wrong recipient (fixed 2026-07-02) and at least five other verifier fixes in 2026.
- **Nobody has tested the link.** No source found relates verifier mutation scores to audited wrong passes of real agents; "Red-Teaming the Grader" (OpenReview zh33pqlBjf) re-grades stored final states (412 passes become failures) but gives no human audit and no per-mode comparison.

## 2. Key insight

A wrong pass needs a verifier blind spot **and** a real agent failure that lands in it. The right question is therefore mode-conditional: *within a failure mode, does the verifier miss real agent failures as often as it misses seeded ones?* This is the mutants-versus-real-faults question of software testing (Just et al., FSE 2014), never asked for agent graders. It is testable on stateful benchmarks because **whole-state ground truth is obtainable without labelling each run**: a scripted reference run from the same initial state gives a gold end state, and the one obstacle — legitimate variation across correct routes and nondeterministic fields — can be measured by executing several distinct correct routes. With state-level truth, *all real failures* (hundreds per agent, not the few dozen wrong passes) become the denominator, which is what makes the test powered.

## 3. Scope

- **Setting:** stateful agent benchmarks with programmatic state checkers — Android GUI benchmarks on the emulator and one API-world benchmark; unmodified runs from the shipped initial state; open-source apps without server-side state.
- **Benchmarks (three, two families):**
  - *Android GUI family:* AndroidWorld (116 templates; Apache-2.0) and MobileWorld (public, self-hosted backends, per-task snapshots).
  - *API-world family (required):* AppWorld (Trivedi et al., ACL 2024, DOI 10.18653/v1/2024.acl-long.850; 9 apps, 457 APIs, 750 tasks). No emulator is needed. Its evaluator uses state-based unit tests that also check for unexpected changes ("collateral damage"), and arXiv:2610.09142 published verifier mutants for it with code (`OpenAdaptAI/side-effect-loopholes`). The feasibility audit read that AppWorld ships reference solutions; confirm at the pinned commit.
  - Why this family matters for the argument: 46 of AndroidWorld's 116 checkers test a postcondition only and none looks outside its own table, directory or key, whereas AppWorld's evaluator tests for collateral damage by design. The pair gives a contrast in checker design, and on AppWorld the C2 test can use **published mutants unmodified**, with no porting choices of ours.
  - Commits pinned for all three.
- **Devices:** main runs on the emulator (the benchmarks' supported configuration). The three rooted phones are used for a **real-device replication arm** on a stratified subset of AndroidWorld templates (see §7); they are factory-reset test devices with no personal accounts, SIM or personal data.
- **Assumptions:** A1 two annotators with retained state and screenshots can adjudicate correctness; A2 scripted reference routes are correct (known-answer control: the native checker must pass them); A3 conclusions hold for the audited commits, agents and scaffolds.
- **Out of scope:** safety benchmarks and missed-harm analysis (journal extension); confidentiality harms that leave no state trace; proprietary leaderboard agents that cannot be rerun; any modification of benchmark tasks for the main results.

## 4. Contributions

1. **Instrument:** a whole-state differential oracle for Android agent benchmarks with a *route-diverse measured mask*; read-only tasks need no gold (any persistent change is a flag). → C4
2. **Measurement:** first state-level, two-direction verdict-error rates for mobile-agent benchmarks, with intervals, including the share of wrong passes invisible to trajectory-level review. → C1
3. **Test of a methodological assumption:** mode-conditional transfer of seeded-fault miss rates to real agent failures. → C2
4. **Generality across checker designs and platforms:** the same measurements on an API-world benchmark whose evaluator checks collateral damage by design, and a real-device replication of the Android results. → C1, C2, C5
5. **Leaderboard consequence:** agent-specific verdict error and its effect on orderings (replication outside coding of results known for SWE-bench-style re-grading). → C3

## 5. Claims and how each will be established

| ID | Claim (exact scope) | Evidence type | Success criterion fixed in advance | Refuting result |
|---|---|---|---|---|
| C1 | **State-level prevalence.** Wrong-PASS and wrong-FAIL rates per agent on the audited commits, and the share of wrong passes detectable only at state level (unrequested changes not visible in screenshots/UI trees) | Measurement + blind audit | Rates with template-clustered 95% CIs; achievable precision stated before collection; the state-only share is the quantity that goes beyond MobileJudgeBench | State-only share indistinguishable from 0 → state-level audit adds nothing over trajectory review |
| C2 | **Mode-conditional transfer of published seeding recipes.** For each checker family × failure mode, the native checker's miss rate on real agent failures equals its miss rate on seeded faults of that mode, where the seeded faults follow fault operators frozen before any agent run (Android: the published operators of arXiv:2610.09142 and Sun's six fault classes, ported to Android state; AppWorld: the published mutants of arXiv:2610.09142, used unmodified) | Experiment (preregistered equivalence test) | Equivalence margin fixed in advance **from the tolerable bias of a corrected score** (the largest miss-rate gap that keeps a corrected pass rate within 2 percentage points); minimum cell size counted in distinct templates; power for equivalence and for difference from pilot variance with templates as clusters | **Holds** → kill matrices can correct a new agent's score without a new audit, checked on one agent held out from all design decisions (criterion: corrected pass rate within 2 points of the audited rate). **Fails** → size and direction of the bias of published seeding recipes. **Inconclusive** in more than half of the cells → no general claim → K2 |
| C3 | **Differential verdict error.** Wrong-pass and wrong-fail rates differ across agents/scaffolds; the paper reports whether correction changes any pairwise ordering | Experiment | Mixed model with template random effects; ordering changes reported with uncertainty. A null is the expected outcome under arXiv:2609.25173's "demanding condition" and is reported as such | — (reported either way; not a headline claim) |
| C4 | **Instrument quality.** The oracle's flags reach precision ≥ 0.8 against the blind audit, with recall above an LLM state-reading verifier, at lower human cost per new agent than a full audit | Experiment | Precision/recall with CIs; minutes and API cost per agent | Precision < 0.8 or recall not above the LLM verifier → instrument contribution fails |
| C5 | **Not an emulator artefact (supporting claim, not a headline).** On a stratified subset of AndroidWorld templates run on rooted physical phones, the mask learned on the emulator keeps a comparable false-alarm rate on correct reference runs, and the oracle flags the same seeded faults | Experiment (replication on 3 devices) | False-alarm rate on device within a pre-fixed distance of the emulator rate; seeded-fault detection agreement reported per template | Mask does not transfer (device-specific state swamps it) → results are stated for the emulator configuration only |

Cross-family reading of C1 and C2 (fixed before data): C1 is reported per benchmark with the checker-design contrast (postcondition-only vs collateral-damage-checking) as a planned comparison; C2 is tested separately in each family, and a general claim is made only if it is conclusive in both. If the two families disagree, the paper reports the disagreement as the result.

Not claimed: the oracle idea in general (goal-state comparison and collateral-damage checks exist in τ-bench and AppWorld since 2024; replay-and-diff in OpenReview kuSAqpyELw; masks learned from repeated known-good runs in Diffy, 2015); that rankings change after grader correction (OpenReview 8PIpkkfZ84, arXiv:2611.04399, arXiv:2611.13541, AgentRewardBench); the Mills / Rogan–Gladen estimator algebra.

What C2 does and does not test (answer to the referee's determinism objection): programmatic checkers are deterministic, so within one template a seeded fault and a real failure with the same end state get the same verdict. A family-level miss rate is therefore a mixture over templates and sub-modes, and a difference between seeded and real miss rates measures **how representative a seeding recipe's fault mix is of what agents actually do** — which is the property that decides whether a kill rate says anything about a leaderboard. To keep this from being an artefact of our own choices: operators are taken from published audits and frozen before agent runs; seeded miss rates are reweighted to the template mix of the real failures in each cell (and a template-matched analysis is reported); a composition-only null shows how much non-equivalence the mix alone produces; mode labels are assigned blind to the native verdict, with agreement reported per mode.

## 6. Positioning: closest works and delta

| Work | What it does | Delta |
|---|---|---|
| MobileJudgeBench, arXiv:2608.11434 | AndroidWorld checker vs human labels on 205 trajectories (52 tasks, 4 agents) | Screenshot/UI-tree labels miss state damage; by-product without intervals; 52/116 templates. We add state-level truth, both directions with CIs, all templates |
| AgentRewardBench, arXiv:2504.08942 | Rule-based evaluators vs experts on 1,302 web trajectories; rank swap | Web, trajectory review, no retained state, no predictor |
| arXiv:2610.09142; Sun rs-10665114; arXiv:2609.22220; OpenReview RWjv2Zg0Wa, GWFSBzaPNd, zGz2CHm7x2, VXFTF9Je8S, 0ad4aBnjoQ | Verifier audits by mutation / fault injection | Existence only. They supply the predictor that C2 tests |
| "Red-Teaming the Grader", OpenReview zh33pqlBjf | Mutation audit carried to re-grading stored final states (412 passes → failures) | One domain, no human audit, no per-mode comparison of seeded vs real miss rates |
| arXiv:2605.10448 | Partial-identification bounds on AndroidWorld scores | Half the records undecidable without post-state; we retain whole state |
| arXiv:2607.28367 | Human audit of FAIL verdicts (15.3% wrong = 10.7% evaluator false negatives + 4.7% broken tasks); no mobile | Both directions, mobile |
| OpenReview kuSAqpyELw; Agent-Diff arXiv:2602.11224; EffectMatch arXiv:2609.31301; SABench arXiv:2610.34167; AgentRelBench (OpenReview eQH5SQYour) | Replay/diff and expected-diff checks; unauthorised writes in tool agents | Not mobile GUI state; hand-specified diffs or single route; no route-diverse measured mask; no coupling test |
| Just et al., FSE 2014; Knight & Ammann 1985; coding-side coupling arXiv:2607.22880, 2609.09315, 2606.16062 | Mutants vs real faults | Precedent and method for C2; never done for agent graders |
| SWE-Bench+ arXiv:2410.06992, UTBoost 2506.09289, SWE-ABS 2603.00520, TestJack 2610.10619 | Prevalence by stronger-oracle re-grading in coding | Other domain; no coupling test |
| arXiv:2609.25173 | Analytic ranking-inversion condition; ran no agents | C3 is its empirical check on mobile |
| Thor (ISSTA 2015), Genie arXiv:2008.03585, DLD arXiv:2010.05584 | Android state oracles for apps | Method lineage for the observer and mask |

Verification levels are recorded in `ideation/05_NOVELTY/`. Novelty verdicts: predecessor F1 — *incremental* (two hunters); redesigned idea — *incremental; C2 clean in every source searched* (drift scan). All reviews are same-family (provisional); see §13.

## 7. Evaluation plan

**Research questions.** RQ1 How often are PASS and FAIL verdicts wrong at state level, and how much of it is invisible to trajectory review? RQ2 Do seeded-fault miss rates transfer to real agent failures within a mode? RQ3 Is verdict error agent-specific enough to matter for orderings? RQ4 How good and how cheap is the oracle?

**Pipeline.**
1. *State observer:* typed snapshot/diff of benchmark-app SQLite databases, SMS/contacts providers, shared storage, settings; taken before and after every run.
2. *Reference routes:* for each template, UIAutomator scripts along ≥ 2 distinct correct routes, each repeated; native checker must pass them.
3. *Mask:* fields varying across correct runs; false-alarm rate on held-out correct routes; recall on planted unrequested writes.
4. *Agent runs:* M3A and T3A with one strong and one inexpensive API model; 1–2 open 8B-class GUI agents on local GPUs; ≥ 3 seeds; weaker agents included on purpose so failures are plentiful. One agent is designated in advance as held out: it is used only for the final check of C2.
5. *Ground truth:* oracle flags + blind adjudication by two annotators of all flagged runs and a random sample of unflagged passes and fails (state, screenshots); each real failure labelled with a failure mode (wrong entity, partial completion, near-miss value, uncommitted, collateral change, wrong location, null).
6. *Seeded faults (frozen before step 4):* end-state faults following published operators, produced through the app UI by script, validated by two annotators; kill matrix per checker family × mode. Auditor recall is checked with spike-ins (known wrong runs inserted blind into the audit queue).

7. *AppWorld arm:* agents are code-writing API agents (ReAct-style and one stronger scaffold) on commercial and local models, ≥ 3 seeds; state = the app databases before and after each run; gold end states from the shipped reference solutions (a set where several end states are valid); ground truth by the same oracle-plus-blind-audit procedure; seeded faults = the published mutants. AppWorld's own collateral-damage check is a baseline as well as the object under audit.
8. *Real-device arm:* 10–15 AndroidWorld templates stratified by checker style, on the three rooted phones. Known obstacle to resolve in the pilot: AndroidWorld obtains root with `adb root`, which production builds rooted with Magisk normally do not offer, so state reads have to go through `su -c` (harness adaptation). The benchmark's emulator-specific setup steps (clock reset, app-snapshot restore, APK set for API 33) must be checked on each device model before any result is used.

**Baselines, strongest first.** (1) full blind human audit (truth and cost reference); (2) LLM state-reading verifier over retained post-state; (3) hand-written expected-diff checks on a subset; (4) raw diff without the measured mask; (5) native checker; (6) trajectory-level judge as in MobileJudgeBench.

**Statistics.** Unit = run nested in template; intervals clustered by template; C2 as a two one-sided equivalence test per cell with pooled calibration, margin and minimum cell size preregistered; power stated before collection (a 3% rate needs ≈ 1,000 passes for a 2.0–4.3% interval; C2 uses all real failures, expected in the hundreds per agent for weaker agents); multiplicity control across cells; audit agreement (κ) reported.

**Killer experiments (run early).** (a) *Agent-free:* on ~15 templates, learn the mask on one correct route and measure false alarms on other correct routes. (b) *Small agent pilot:* one inexpensive agent on ~30 templates; count real failures per mode to check that C2 cells can be populated.

## 8. Theory plan

A short identification statement, not a theorem paper: define verdict error in both directions relative to state-level truth; state what a whole-state oracle with a route-diverse mask identifies (wrong outcomes and unrequested persistent changes) and what it cannot (effects with no state trace; correct end states outside the gold set); define the mode-conditional transfer hypothesis and the bias of a score corrected with seeded-fault rates when it fails. Boundary cases: deterministic checkers give 0/1 miss rates per (template, mode) — comparison is made at checker-family level; modes with no real failures are non-estimable and reported as such.

## 9. Artifact plan

State observer, reference-route scripts, masks, kill matrices, audited verdict labels, analysis code (Apache-2.0, matching AndroidWorld). Release scripts and diffs, not AVD images or APKs. Checker defects reported upstream before publication; pinned commits documented.

## 10. Risks, mitigations, pivot and kill criteria

| Risk | Mitigation |
|---|---|
| Route-dependent benign residue swamps the mask | Agent-free pilot (a) decides; route-diverse gold; severity grading |
| Wrong passes rare | C1's headline quantity is the state-only share and both directions; C2 uses all failures |
| C2 cells sparse | Pilot (b); weaker agents; pooling by checker family; preregistered minimum cell size |
| Scripting two routes for many templates | Stratify templates by checker style; start with the 46 postcondition-only templates |
| Scoop (verifier auditing is active; arXiv:2610.09142 names a whole-state frame check as future work) | Novelty re-scan at each milestone; the coupling test and mobile state truth are the protected parts |
| "Maintenance paper" perception at ICML | Lead with C2 as a general methodological test across two benchmark families (Android GUI and AppWorld) |
| AppWorld's evaluator already checks collateral damage, so wrong passes may be very rare there | That contrast is a planned result (C1); C2 uses real failures, which are plentiful on AppWorld |
| Real-device arm does not run (root model, API level, device-specific state) | It is a supporting arm; the main results do not depend on it; drop it and state the emulator-only scope |

**Kill criteria (no repositioning):**
- **K1** — mask false-alarm rate on held-out correct routes stays above 10% for most pilot templates → the oracle is not viable → stop.
- **K2** — fixed **before** pilot (b): the list of checker families, a minimum cell size counted in distinct templates with at least one real failure of the mode, and the number of cells that must reach it on each benchmark. The rule applies per family (Android, AppWorld). If pilot (b) misses it in both families, or if in the final analysis more than half of the cells are inconclusive in both, there is no general claim → not an ICML submission (step down to NeurIPS Evaluations & Datasets, an SE venue or a workshop — author's decision).
- **K2b** — if C2 is conclusive in one family only, the paper claims that family only and says so in the title and abstract; the author then decides whether ICML is still the right venue.
- **K3** — a paper appears that tests transfer of seeded-fault miss rates to real agent failures with a human audit → return to adversarial review.

## 11. Resources and timeline

Testbed (confirmed by the author on 2026-11-20): a computer for the Android emulator and three rooted physical Android phones (Magisk). To verify on that computer before pilot (a): hardware virtualisation is available to the emulator (on Linux, `/dev/kvm` exists; an arm64 Mac runs a native arm64 AVD). The emulator needs no GPU. AppWorld needs no emulator. Other resources: commercial APIs (a few hundred to a few thousand USD for the Android runs depending on models — auditor's estimate, to be re-measured in the pilot; AppWorld runs add API cost that has not been estimated); 1–2 GPUs for open GUI agents and local models; two annotators (language-independent task). The cloud workspace used for this ideation cannot run the Android emulator.

Milestones: pilot (a) on the emulator → observer + first reference routes → AppWorld set-up and reproduction of the published mutant results → **preregistration of C2 (operators, families, margin, minimum cell size, held-out agent)** → pilot (b) in both families → real-device feasibility check → full runs → audit → analysis → writing → two internal review rounds. First cycle of interest: ICML 2027 (abstract 14 Jan, paper 22 Jan 2027); if the gates are not passed in time, NeurIPS 2027 — timing does not change the idea.

## 12. Conference core vs journal extension

- **Conference core (8 pages + appendix):** oracle with route-diverse mask, C1–C4 on AndroidWorld, MobileWorld and AppWorld, blind audit, preregistered C2, real-device replication (C5) in the appendix.
- **Journal extension (JAIR or AIJ; both accept substantially extended conference papers — quartile to be checked in JCR):** safety benchmarks (missed-harm direction), desktop/web benchmarks, automatic synthesis of reference routes, identification analysis in full, checker repair from surviving faults. New title and abstract; cite the conference paper.

## 13. Red-team issues that Process 2 must address

Atomised kill argument (`ideation/06_REDTEAM/KILL_ATOMS_P2.md`; status before the commitments in §5, §7 and §10 were added: 1 answered, 4 partly answered, 1 unresolved). Nothing has been run.

| # | Issue | Status after this revision | What closes it |
|---|---|---|---|
| 1 | C2 refutes a hypothesis nobody holds | Reframed as representativeness of published seeding recipes with a usable "holds" branch and a held-out-agent check | Cite concrete uses of kill rates as a verifier-quality score; held-out result |
| 2 | Low association is built into the estimand | Estimand is now the miss rate given a real failure within a mode; reweighting, template-matched analysis and composition-only null committed | Those analyses |
| 3 | Data too sparse | Denominator = all real failures; minimum cell size fixed before pilot (b); K2 | Pilot (b) |
| 4 | No power analysis for C2 | **Still open:** margin rule and cell-size rule are stated, the numbers are not computed | A written power analysis before pilot (b), including the inconclusive outcome |
| 5 | Without C2 it is a known re-grading recipe | Conceded in "Not claimed"; K2 now also applies to the final analysis | — |
| 6 | The fair test is not the one proposed | Adopted (mode-conditional test) | — |

Further standing issues:
7. **Determinism / seeding-recipe objection** (second scorer): answered by the paragraph in §5; a referee may still judge C2 to be a property of the recipe rather than of mutation audits — the paper must say so itself.
8. **Venue fit 3/5.** The author decided on 2026-11-20 to keep ICML and add AppWorld as a required second family; the scorers' view that NeurIPS Evaluations & Datasets is the more likely home stands as a recorded risk, and K2/K2b define when to step down.
9. **Controls a scorer asked for:** random-pass-removal control for C3; named LLM-verifier baselines.
10. **Testbed:** confirmed by the author (emulator computer + three Magisk-rooted phones); virtualisation support on the computer and the `adb root` vs `su -c` adaptation on the phones are still to be checked.
11. **Gold diff dominates relations; composed runs are a different population** — accepted; both removed from the core.
12. **Process gaps:** all reviews are same-family (provisional): run `ideation/XMODEL_NOVELTY_P2_PROMPT.md` and `ideation/XMODEL_REDTEAM_P2_PROMPT.md` in another model family, or record a waiver. The redesigned C2 has had one drift scan (clean) but no two-hunter attack.
13. **Search limits:** GitHub issue bodies, Semantic Scholar citation graphs, OpenReview PDFs and non-public submissions were not searchable; re-scan before submission.
14. **Additions not yet attacked:** the AppWorld arm and the real-device arm were added after the last novelty scan and review. Check in particular whether AppWorld-specific audits beyond arXiv:2610.09142 already report wrong-pass prevalence on agent runs, and include both arms in the cross-family review.
