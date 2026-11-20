# IDEA_M2: The task suite as its own oracle — metamorphic state relations for label-free bounds on wrong "pass" verdicts in mobile agent benchmarks

Citation status used below: **[notes]** = identifier appears in `research_notes/.../agent_security_sota.md` or `hot_topics.md`; **[fetched]** = primary record or full text opened in this ideation session (2026-11-20); **[index]** = only the alphaXiv index record (ID, title, first lines of abstract) was seen.

- Gap addressed: **G6** (false positives among "successful" computer-use/mobile runs), with **G3** (no validity audit of mobile safety benchmarks) as the second application.

- Target venue and track: **IJCAI 2027 Main Track** (agent evaluation; cross-discipline software-testing × AI, which the call encourages; the frame problem gives the idea a classical-AI anchor). Alternative with the same content: ICML 2027, area "Evaluation", contribution type "Datasets, Evaluations and Benchmarks".

- Problem (1 paragraph): Audits of computer-use benchmarks measured wrong FAIL verdicts (15.3% across five benchmarks) and state that false positives among successes were not estimated because only failed trajectories were sampled (2607.28367 [notes]). The closest study of wrong passes hand-edits *reference* runs after reading each verifier's source and shows that AppWorld and WorkArena verifiers accept unrequested changes; its own limitations say it gives "no prevalence estimate", evaluates no model-generated runs, and needs a separate harness per benchmark; it covers no mobile benchmark (2610.09142 [fetched, full text]). Estimating how often *real agent passes* are wrong appears to need either a human label per trajectory or a hand-written closed-world specification per task, and both must be redone for every benchmark. Meanwhile AndroidWorld is reported near saturation (2602.07787 [notes]), so the remaining question about it is precisely whether the passes are real.

- Key insight (the non-obvious observation; 2–3 sentences): Tasks in a stateful benchmark constrain each other. If task T⁻¹ undoes task T, then "checker passes T" and "checker passes T⁻¹" jointly imply that the device returns to its starting state, up to a noise mask that can be *measured* from repeated scripted round-trips; a passed pair that does not return is a certified wrong or extra effect, with no human label, no per-task frame specification and no reading of verifier code. The same reasoning gives idempotence for "ensure"-type goals and commutation for independent tasks, so the suite acts as an oracle for its own checkers on agent-generated runs, which is where prevalence has to be measured.

- Approach (how the insight becomes a method/system/theory):
  1. **State observer for the Android emulator**: typed snapshot of app databases, shared preferences, content providers (contacts, calendar, messages, media), system/secure/global settings and file-tree hashes, with a typed diff. This is standard instrumentation in automated Android testing.
  2. **Measured noise mask**: run scripted gold compositions K times per relation; fields that vary across gold runs (timestamps, auto-increment IDs, recents) are masked. The mask's false-alarm rate is estimated on held-out gold runs and reported.
  3. **Four relations**: R1 round-trip (T ; T⁻¹ ⇒ state ≈ start); R2 idempotence (an "ensure X" goal run twice ⇒ the second run changes nothing); R3 commutation (T1 ; T2 ≈ T2 ; T1 for tasks on disjoint apps); R4 pre-satisfied goal (start state already satisfies T ⇒ pass with an empty diff).
  4. **Estimator**: among compositions in which the checker passed every leg, the violation rate is a *lower bound* on P(wrong or extra effect | pass), reported with exact or cluster-bootstrap intervals by task template. Two annotators adjudicate a stratified sample to attribute each violation to a leg and grade severity (user-data change vs incidental residue).
  5. **Frame-aware rescoring**: recompute agent rankings with violating passes removed and test whether verdict error is differential across agents and scaffolds.
  6. **Safety-benchmark variant (G3)**: in a mobile safety benchmark, a "safe and task completed" verdict must also satisfy "diff ⊆ gold diff of the user task"; a violation is a missed harm, the costly direction for a safety score.

- Contribution type: **new measurement/benchmark** (a measurement instrument and the first prevalence bounds; negative-result reading available if the bound is near zero).

- Claims (falsifiable, 2–4):
  - **C1 (prevalence).** On a mobile capability benchmark, the certified violation rate among checker-passed compositions has a 95% lower confidence bound above 3% for at least two of the tested agents. An upper bound below 1% for all agents is the pre-specified negative result ("frame errors exist in principle but are negligible in practice").
  - **C2 (differential error).** Violation rates differ across agents/scaffolds (mixed-effects likelihood-ratio test with task-template random effects), and frame-aware rescoring changes the order of at least one pair of agents.
  - **C3 (existence is not prevalence).** Per-template mutation scores obtained by mutating gold runs, the 2610.09142 method, correlate weakly (Spearman ρ < 0.4) with per-template violation rates observed on agent runs.
  - **C4 (instrument validity and transfer).** On scripted runs with planted unrequested writes (duplicate, extra field, unrelated delete) the relations flag at least 90%, clean held-out gold runs are flagged at most 2%, and the same four relations instantiate on one non-mobile stateful benchmark without benchmark-specific oracle code beyond a state reader.

- Closest work known so far (with identifiers) and the expected delta:
  - **Finding Side-Effect Loopholes in AppWorld and WorkArena Verifiers**, arXiv 2610.09142 [fetched, full text]: mutation testing of verifiers with hand-written edits to reference runs; frames the gap as postcondition vs frame condition. Delta: (i) this idea measures agent-generated passes and gives a prevalence bound with intervals; (ii) no verifier source is read and no per-task edit is written; (iii) mobile GUI state rather than API/web records; (iv) C3 tests directly whether their kind of evidence predicts prevalence. Its "one frame check for every task" is listed as future work with the open costs "fields that legitimately vary" and "several valid end states" — the measured mask and the round-trip reference address both.
  - **How Benchmarks Mis-Score Computer-Use Agents**, arXiv 2607.28367 [notes]: human re-audit of 150 FAIL trajectories. Delta: the complementary error direction, without per-trajectory human labels.
  - **Agent-Diff**, arXiv 2602.11224 [index], and **EffectMatch**, arXiv 2609.31301 [abstract fetched]: new checks that compare state changes with a hand-specified expected or approved outcome. Delta: these need a per-task expected diff; here the reference is the start state or the commuted run, so no expected diff is authored. They are the accuracy upper-bound baseline.
  - **Agentic Benchmark Checklist**, arXiv 2507.02825; **Unearned passes**, arXiv 2609.34262; **oracle failure**, arXiv 2610.16067; **executable-contract audit**, arXiv 2609.37315; **silent instrument errors**, arXiv 2611.04399 [all notes]: audits of coding, customer-service and tool benchmarks by inspection, trace review or contracts. Delta: none is label-free on agent runs, none is mobile.
  - **SANE**, arXiv 2610.28886 [abstract fetched]: metamorphic testing of *LLM judges* with perturbation recipes. Delta: programmatic state verifiers and environment-state relations, not text judges.
  - **UndoBench**, arXiv 2610.05622 [abstract fetched]: measures agents' fault recovery with paired control/fault runs; not scored by state restoration and not an audit of checkers. Delta: different object (the checker, not the agent's recovery skill).
  - Method lineage: Chen et al., "Metamorphic Testing: A Review of Challenges and Opportunities", ACM Computing Surveys 51(1), 2018 [fetched record].
  - Benchmarks to instrument: AndroidWorld 2405.14573; MobileSafetyBench 2410.17520; MobileWorldSafety 2608.17659 [all notes].

- Evaluation sketch: settings, baselines (strongest first), metrics, decisive experiment
  - **Settings.** AndroidWorld-style emulator benchmark with open-source apps; reversible task pairs, ensure-type tasks, disjoint-app pairs and pre-satisfied starts selected by a written applicability rule, with suite coverage of each relation reported. Agents: 2–3 API models under at least two scaffolds, plus 1–2 open GUI agents served locally; at least three runs per composition. Safety variant on one mobile safety benchmark. Transfer check on one API-world benchmark.
  - **Baselines, strongest first.** (1) Hand-written closed-world expected-diff checks on a task subset (Agent-Diff/EffectMatch style): the accuracy ceiling, compared on errors found per hour of specification. (2) Gold-run mutation testing as in 2610.09142. (3) A VLM/LLM trajectory judge used as a false-positive detector, the usual process-based alternative (cf. OSWorld-Pro 2609.24890 and the judge agreement F1 0.76–0.79 in 2506.14866 [notes]). (4) Raw state diff with no learned mask, to show what the mask buys.
  - **Metrics.** Violation rate among passed compositions with intervals; flag precision and recall against blind human adjudication (two annotators, agreement reported); false-alarm rate on held-out gold runs; rank changes after rescoring; cost per confirmed wrong pass for each method.
  - **Decisive experiment.** Blind adjudication of a stratified random sample of flagged and unflagged checker-passed runs. The instrument fails if flag precision is below 0.8, or if the agent-run violation rate is statistically indistinguishable from the gold-run false-alarm rate (then C1 and C2 are both unsupported and the honest paper is the negative result).

- Resources needed vs available (00_CONSTRAINTS.md):
  - Android emulators with root for state dumps: assumed from the researcher's Android-testing expertise but marked "(chưa khai báo)" in 00_CONSTRAINTS — **needs confirmation**.
  - Commercial APIs for GUI agents; 1–2 GPUs for open GUI agents of moderate size — available.
  - Annotators: adjudication of screenshots and state diffs is language-independent; two annotators — available.
  - Expertise: record-and-replay scripting, UI automation, state instrumentation, test-oracle design — this is the researcher's published area.

- Risks and unknowns:
  - **Applicability.** Reversible pairs exist for only part of a suite, so R1 results describe a selected subset; R2–R4 widen coverage but each has its own selection. Which AndroidWorld tasks form inverse pairs must be checked in the repository; I did not verify the task list in this session.
  - **Residue vs harm.** Agents leave incidental traces (search history, drafts, recents) that gold scripts do not. If most violations are benign residue, C1 holds numerically but matters little; the severity grading decides this.
  - **Composition changes the task.** The second leg starts from a non-clean state. Conditioning on both legs passing protects the bound, but attribution to a leg needs humans.
  - **Unobservable state.** Apps with server-side state cannot be snapshotted; restrict to offline/open-source apps and say so.
  - **Irreversible actions** (sent messages) fall outside R1 by definition.
  - **Crowding.** Verifier auditing is active (2610.09142 cites six ICLR 2027 submissions on verifier flaws; "Scalable Weak-to-Strong Verifier Hardening", arXiv 2610.15924 [index]); none found uses cross-task relations on agent runs, but OpenReview was not searched.
  - **Result dependence.** A near-zero violation rate is publishable only as a well-powered negative result.

- Conference core / journal extension (1 line each):
  - Conference core: the four relations, the measured mask, prevalence bounds and rescoring on one mobile benchmark, planted-fault validation, and the blind adjudication.
  - Journal extension: safety-benchmark variant at full scale, desktop and web benchmarks, automatic synthesis of inverse tasks, and the effect of frame-aware rewards on RL-trained agents (left open by 2610.09142).

- Generator perspective: empirical/measurement
