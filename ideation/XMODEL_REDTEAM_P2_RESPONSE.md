<!-- Cross-family review, saved verbatim. Reviewer model as self-reported: OpenAI GPT-6 (no finer version exposed). Run by the author on 2026-11-20 with the prompt and attachments in ideation/xmodel_kit/. Everything below this comment is the unedited response. -->

Independent Referee Report — ICML 2027
Area: Evaluation | Contribution type: Datasets, Evaluations and Benchmarks | Review date: November 20, 2026 | Stage: Research proposal, no experiments conducted

Proposal: Are the Passes Real? A State-Level Audit of Mobile-Agent Benchmark Verdicts and a Test of Whether Verifier Mutation Scores Transfer to Real Agent Failures
Pre-execution verdict: Borderline / Weak Reject
Novelty: Incremental

Central assessment: This is a legitimate scientific evaluation question with a potentially important negative result. However, the proposal does not yet establish that its principal experiment will yield a sufficiently identifiable, informative, and generalizable result for ICML.

The proposal's strongest idea is C2: testing whether the ability of seeded faults to evade benchmark verifiers transfers to naturally occurring agent failures. This is more interesting than merely discovering defective checkers or correcting leaderboard scores.

The central problem is that C2 may measure differences in the composition of synthetic and naturally occurring failure populations rather than an informative property of verifier quality. If this distinction is not handled rigorously, the experiment could be technically correct yet scientifically unsurprising.

The submission is appropriately placed under ICML 2027's evaluation contribution type. The official guidance explicitly recognizes novel evaluation questions, auditing techniques, protocols, and scientific insights from rigorous evaluation of existing systems; a new learning algorithm is not required. 

icml.cc+1

This report evaluates the proposal's technical merits, research validity, ethics, and resource feasibility, not its schedule or the number of people conducting the study.
1. Scores
Scale: 1 = poor, 2 = below expectations, 3 = adequate/borderline, 4 = strong, 5 = exceptional. Scores assess the proposed research, not completed empirical evidence.
Criterion	Score	One-line justification
Novelty	3/5	The mode-conditional transfer test is relatively unexplored, but mutation auditing, state oracles, and verdict-error measurement have substantial precedents.
Significance	4/5	If mutation scores cannot predict real false accepts, the result could change how agent benchmarks report evaluation reliability.
Technical depth	3/5	Stateful observation, differential oracles, and clustered equivalence testing are nontrivial, but the principal statistics and testing mechanisms are established.
Soundness potential	2/5	Ground-truth completeness, failure-mode support, selection bias, and correction identifiability remain insufficiently resolved.
Evaluation design	3/5	Three benchmarks, blinded annotation, frozen operators, and held-out agents are strong choices; the proposed sampling and validation design still has important gaps.
Clarity	4/5	The scope, claims C1–C5, anticipated negative outcomes, and kill criteria are unusually explicit.
Venue fit	4/5	Strong topical alignment with ICML Evaluation and Datasets, Evaluations and Benchmarks, conditional on a generalizable methodological contribution.

Unweighted mean
3.29 / 5




The most consequential scores are soundness potential (2/5) and technical depth (3/5). Improving these would do more for acceptance than adding another benchmark.
2. Likely reasons for rejection, ranked by severity
R1 — The independent ground truth is not sufficiently established
Severity: Critical | Threatens C1, C2, C4

The proposal treats a differential comparison against scripted reference executions as the foundation of state-level truth.

But a reference execution establishes one valid way to complete a task, not the complete set of valid final states.

Two reference routes per template do not establish that every other legitimate route has been represented. Furthermore, a mask learned from varying fields cannot reliably distinguish benign variation from important unintended changes.

For example, suppose a task asks an agent to create a contact:
- Reference route A creates the contact directly.
- Reference route B imports the contact from a file.
- The agent creates the contact through a third legitimate route, which changes a different metadata field.
- The oracle flags the unfamiliar metadata as an unwanted side effect.
Conversely, if an unexpected write occurs in a field classified as variable, the mask may suppress a genuine error.

Both situations are possible without any defect in the benchmark's native checker.

The proposal's blind human audit mitigates this concern, but the two annotators still need an independent task-level specification of permitted and forbidden effects. Merely seeing a reference state and the agent's state does not necessarily establish intent.

Required change: Define a task-specific correctness contract independent of both the native checker and the reference routes. Use randomized human adjudication, including oracle-unflagged runs, to validate both false alarms and missed errors.
R2 — C2 may be an artifact of failure-distribution mismatch
Severity: Critical | Threatens the primary novelty claim

The specification correctly recognizes that the native checkers are deterministic and that differences in family-level miss rates arise from the composition of cases.

Consider two templates belonging to one failure-mode category:
	Template A	Template B
Native checker misses failures	0%	100%
Share of seeded faults	90%	10%
Share of real failures	10%	90%

The pooled miss rates are 10% for seeded faults and 90% for real failures.

This difference does not demonstrate a new weakness of the checker. It reflects that the two populations put their weight on different templates.

The proposal already plans template reweighting and a composition-only null. Those are important safeguards, but they do not solve within-template, within-mode heterogeneity.

For example, failures labelled wrong entity can involve a wrong identifier, duplicated entity, stale reference, invalid recipient, or unsaved draft. A seeding operator may generate only one of these.

A referee will ask whether C2 measures a general property of mutation-score transfer or merely a predictable mismatch between the published operators and the agents' actual error mechanisms.

Required change: Specify the estimand separately for the observed agent-failure distribution and for the common-support, template-matched population. Report where synthetic and real failure subtypes do not overlap. Treat absent support as non-identifiable, not as evidence of non-equivalence.
R3 — The proposed audit does not automatically observe all real failures
Severity: Critical | Threatens prevalence estimation

Section 2 asserts that whole-state truth makes all real failures available as a denominator, while Section 7 proposes reviewing all oracle-flagged runs and a random sample of unflagged runs.

Those are different things.

When only sampled unflagged runs receive human adjudication, the study does not know the exact number of real failures. It can estimate it using the sampling design.

For C2, this matters because the denominator is all truly failed agent runs, not merely checker-FAIL runs or oracle-flagged runs.

The study therefore needs a two-phase, probability-weighted audit. Each included trajectory must have a known selection probability, and uncertainty must incorporate both audit sampling and template clustering.

Otherwise, failure-mode miss rates may be biased toward errors the new oracle is good at detecting.
R4 — The corrected-score validation can succeed trivially
Severity: Major | Threatens C2's practical significance

The held-out-agent criterion is a corrected success rate within two percentage points of its audited rate.

This is insufficient if the native success rate is already within two points.

For example, if the native checker reports 40%, the true rate is 39%, and the mutation-calibrated estimator reports 39.5%, the estimator meets the stated criterion. But reporting 40% without any correction also meets it.

The proposal must demonstrate improvement over the uncorrected score and a strong calibration baseline, not merely absolute accuracy within a tolerance.

A further complication is that correcting scores requires handling both error directions. Let \(T\) denote true success and \(Y\) the native verdict:
\[
\alpha=P(Y=1\mid T=0)
\]

\[
\beta=P(Y=0\mid T=1)
\]

Then, under stable and identifiable error rates,
\[
P(T=1)=
\frac{P(Y=1)-\alpha}{1-\alpha-\beta}.
\]

Seeded failure mutants primarily estimate \(\alpha\), whereas the correction also requires \(\beta\). The study needs an explicit method for estimating the latter and propagating the uncertainty of both.
R5 — Equivalence testing is likely to be underpowered in the relevant cells
Severity: Major | Threatens C2's conclusiveness

The planned design subdivides observations by benchmark, checker family, failure mode, and agent. It then uses clustered equivalence tests with multiplicity correction.

A large number of failed agent runs does not guarantee adequate information within each cell. Thousands of executions may still represent only a small number of distinct templates with relevant failure modes.

Moreover, proving equivalence within a narrow, decision-relevant margin generally requires substantially more precision than merely detecting a difference.

The proposal's K2 stopping rule handles this responsibly. Nevertheless, the scientific risk remains that most C2 cells will be either deterministic, nearly empty, or statistically inconclusive.

Required change: Power the primary tests using independent template clusters, observed mode frequencies, and plausible intracluster dependence. Fix a small number of scientifically motivated primary cells; treat others as exploratory.
R6 — The instrument is an integration of established mechanisms
Severity: Major | Threatens novelty

Gold-end-state comparison and collateral-damage detection were already part of AppWorld (ACL 2024, arXiv:2407.18901). 

arxiv.org

The supplied reports also identify mutation audits, replay-and-diff, and established noise-masking techniques.

An additional relevant study is VerifierBench (arXiv:2610.28679), which evaluates executable verifiers using 4,993 test cases covering valid alternatives and invalid solutions and employs repeatability and mutation checks. Its main subject is generated verifiers, rather than the prevalence of errors in shipped mobile checkers, so it does not anticipate C2; it does further reduce the novelty of C4 as a standalone instrumentation contribution. 

arxiv.org+1

I would not reject the proposal for using established mechanisms. ICML evaluation papers can do that. However, the resulting instrument must enable a meaningful scientific conclusion that existing techniques could not support.
R7 — Generality is narrower than the proposal suggests
Severity: Moderate to major | Threatens C1, C2, C5

AndroidWorld and MobileWorld are two benchmarks from the Android GUI family, not two independent evaluation paradigms.

AppWorld introduces a genuinely different API-based environment, but its native evaluator already checks unexpected state changes. That makes it a valuable contrast and also limits how much new instrumentation is demonstrated there.

Additionally, the proposal limits itself to open-source, controlled environments without external server-side state, while describing MobileWorld's self-hosted backends. The definition of whole state must explicitly include any relevant backend state.

Three rooted physical phones can support a controlled replication, but not a general claim about physical Android devices.

I would accept conditional generality across the studied checker designs, not across stateful agent evaluation as a whole.
R8 — The evaluation target and ethical definition of success need tightening
Severity: Moderate | Threatens interpretation

The study treats persistent unrequested changes as potential failures. However, an application can legitimately modify caches, navigation history, timestamps, or other incidental state while fulfilling a task.

A definition of success that penalizes all such writes could measure adherence to a strict frame condition rather than the benchmark's intended notion of task completion.

The protocol should distinguish task failure, harmless incidental effects, materially harmful side effects, and state changes whose permissibility is ambiguous. Results should be reported under both strict and task-relevant correctness definitions.

The proposed isolated phones and lack of personal accounts address many ethical concerns. Remaining requirements include sanitizing released state diffs, avoiding irreversible operations in evaluation environments, and coordinating disclosure of verifier defects before public exploitation.

3. Strongest missing baseline
Real-failure-calibrated transfer from source agents to a held-out agent.

The existing baseline list includes full human audit, LLM state verification, hand-written expected diffs, raw diffs, the native checker, and trajectory judges. None directly addresses the question: Does synthetic calibration offer an advantage over empirical calibration from real agent failures?

I would require a baseline with the following protocol.
Train / calibration population

Blindly audit a probability sample of real trajectories from several source agents, then estimate native-checker false-accept and false-reject rates by benchmark, template, and failure mode.


Frozen calibration

Fit a regularized hierarchical model of real-run verifier error using the source-agent data only. Freeze the calibration before examining held-out-agent outcomes.


Held-out evaluation

Predict the held-out agent's true success rate and compare it with the prediction from the published-mutant kill matrix against an independent audit.


Compare at least the following four estimators using paired data and identical held-out tasks:
Estimator	Purpose
Native pass rate	No-calibration baseline
Published-mutant calibration	Primary proposed approach
Real-failure calibration	Strongest missing competitor
Design-based stratified human audit	Accuracy and cost reference

Report absolute score error, interval coverage, ranking fidelity, calibration sample size, and total measurement cost.

Why this baseline is decisive: If a modest audit of source agents predicts held-out outcomes more accurately and cheaply than constructing and validating seeded faults, the proposed mutation-calibration approach loses much of its practical motivation.

It could still be scientifically useful to establish that mutation scores do not transfer, but the paper would then need to explain precisely when empirical calibration is preferable and when synthetic calibration remains valuable.
4. Single experiment most likely to produce a negative result
The held-out-agent mutation-transfer experiment (C2)
My prediction: The seeded-fault miss rates will not demonstrate equivalence to real-failure miss rates across both benchmark families within the proposed decision-relevant margins. Some cells will exhibit a detectable discrepancy; others will be inconclusive.

This is a scientific prediction, not an observation.

The most revealing experiment would be:
1. Freeze the published mutation operators, failure-mode taxonomy, and equivalence margins.
2. Produce seeded faults on AndroidWorld and AppWorld without observing the held-out agent's outcomes.
3. Estimate each native checker's miss rate for those faults.
4. Run a held-out agent and obtain independent, probability-weighted ground-truth labels.
5. Compare miss rates within matched templates and modes; predict the held-out agent's corrected score.
AppWorld is particularly informative because its evaluator already attempts to detect collateral damage. 

arxiv.org

The likely difficulty is that a published mutation operator may create a narrow type of side effect while real agents produce a different mixture of unsuccessful end states.

The result would have three possible interpretations:
Outcome	Scientific meaning
Equivalence demonstrated across both families, with improved held-out predictions	Strong evidence that mutation calibration can transfer under the tested conditions
Meaningful non-equivalence after matching templates and failure modes	Strong evidence that published synthetic operators are not representative of actual agent failures
Most cells inconclusive or lack common support	The central transfer hypothesis cannot be evaluated adequately with this design

My concern is the third outcome.

A negative result is not automatically a weak paper. ICML 2027 explicitly recognizes negative results as a contribution category. However, a failure of equivalence must be distinguished from insufficient power, and a distribution-mismatch finding must reveal something beyond the fact that different failures behave differently.

The decisive test is not whether C2 is true. It is whether the experiment can establish a useful and generalizable answer either way.

5. Boundary cases and counterexamples for every Section 5 claim
C1 — State-level prevalence
Claim: Measure wrong-PASS and wrong-FAIL prevalence and the fraction of wrong passes detectable only through state.
Boundary case	Consequence
Wrong passes are genuinely rare, and most detected errors are wrong FAILs	C1 adds limited new information about false acceptance
Every wrong pass is also identifiable from screenshots or UI trees	The principal state-only novelty is absent
A legitimate alternative route produces a persistent state outside the reference set	The oracle may falsely classify a correct execution as a failure
Important effects occur remotely, transiently, or outside monitored storage	The proposed observer cannot establish whole-environment truth
Unrequested state changes are harmless but counted as failures	Prevalence becomes dependent on an unusually strict correctness definition

Critical observation: A true state-only share of zero is not equivalent to evidence that state-level evaluation has no value. State-level measurements could still improve correctness for failures also visible in trajectories, reduce auditing costs, or expose false negatives.

However, those would be narrower contributions than the stated C1 novelty.

C1 additionally needs separate, blinded trajectory-only and state-inclusive adjudication. Otherwise, the number of failures detectable only at state level cannot be measured convincingly.
C2 — Mode-conditional transfer of published seeding recipes
Claim: Seeded-fault miss rates are equivalent to real-agent-failure miss rates within each checker family and failure mode.
Boundary case	Consequence
A failure mode contains no real agent failures	Its transfer rate is undefined
Real failures and seeded faults occupy disjoint subtypes within a broad mode	Transfer cannot be identified for the target distribution
Both populations are always rejected by the checker	Equivalence may hold trivially without demonstrating useful calibration
Both populations are always accepted	Equivalence holds, but mutation-based correction can become poorly informative about unobserved modes
A seeding recipe represents only a narrow subset of the real failure distribution	The difference reflects limited operator support rather than a universal failure of mutation testing
The held-out agent produces a different mix of failure modes	Calibration may fail even when all source-agent cells appeared equivalent

The most important boundary case is support mismatch.

If an operator never creates a particular real-agent failure mechanism, no amount of statistical reweighting can recover its miss rate without additional assumptions.

Equivalence should therefore be stated relative to a defined fault distribution and support set, rather than as an unconditional property of the verifier.

The proposal's current formulation, which says the miss rates equal one another, should be replaced by a statistically operational statement about equivalence within a preregistered tolerance.
C3 — Differential verdict error and leaderboard ordering
Claim: Verdict-error rates may differ across agents, affecting relative rankings.
Boundary case	Consequence
Agents have similar error rates	No meaningful differential mismeasurement is established
Error rates differ but the true performance gap is large	No ranking reversal occurs
Rankings reverse only between statistically indistinguishable agents	The reversal has little practical significance
Agents use different scaffolds, task mixtures, or initialization protocols	Apparent agent-specific error may actually be a configuration effect
Correction changes rankings less than random removal of an equivalent number of passes	The ordering effect is not uniquely attributable to systematic verifier defects

The last case is especially important.

The supplied drift scan identifies empirical leaderboard changes in earlier work, including Silent Instrument Errors Reorder Agent Leaderboards (arXiv:2611.04399), which I independently opened. 

arxiv.org

C3 is therefore a replication or extension to mobile stateful benchmarks, not a first demonstration that evaluator errors can change rankings.

A convincing result must report uncertainty in the pairwise corrected performance difference, not just whether the numerical order changes.
C4 — Instrument quality
Claim: The state oracle attains precision of at least 0.8, recall above an LLM state-reading verifier, and lower human cost per new agent than a full audit.
Boundary case	Consequence
Flag precision is high only because obvious failures dominate	The oracle may still miss the subtle errors central to C1
Masks suppress fields where malicious or accidental writes occur	Precision may improve at the expense of recall
A well-designed LLM verifier using the same structured state achieves equal or better recall	The claimed instrument advantage disappears
Human reviewers must resolve most flags or ambiguous changes	Operational savings may be small
Reference-route and mask construction costs dominate	Lower cost per new agent holds only after substantial reuse
The oracle flags syntactic state differences rather than task-semantic violations	Its output may not correspond to the intended correctness metric

A 0.8 precision threshold is not enough by itself.

The instrument should be assessed by its effect on estimating true pass rates, including bias and interval coverage, as well as classification precision and recall.

For costs, report the break-even number of evaluated agents, including the initial cost of reference-route construction and maintenance.
C5 — Not an emulator artifact
Claim: Emulator-learned masks preserve comparable false-alarm rates and seeded-fault detection on rooted physical Android phones.
Boundary case	Consequence
Device firmware or API version changes the observed state schema	Mask transfer may fail despite identical task semantics
Differences arise from timestamps, caches, or hardware-specific metadata	False-alarm differences need not represent failures of task verification
The three phones share a common platform configuration	Apparent replication may not establish wider device robustness
Root privileges alter application behavior	The physical-device arm may not reflect ordinary user-device execution
Masks work for seeded faults but miss naturally occurring phone-specific failures	C5 validates only the tested synthetic fault distribution

C5 is a sensible supporting experiment, but I would not credit it as a major independent contribution unless it demonstrates transfer on a genuinely meaningful change in the environment.

It should remain a limited robustness claim.

6. Kill argument
Approximately 200 words | One committed argument for rejection

The paper's principal weakness is that its proposed ground truth is not sufficiently independent of the instrument used to construct it. The authors claim to measure the rate at which benchmark verifiers accept incorrect agent executions, but they establish correctness by comparing agent end states with a small collection of scripted reference executions and masking observed variation. This procedure does not characterize the full set of states that legitimately satisfy a natural-language task. A correct agent may produce a state not represented by the reference routes, while an incorrect agent may alter fields that the mask has learned to ignore.

The subsequent human audit does not automatically resolve this problem. If adjudicators use the same state differences to identify violations, they may inherit the instrument's assumptions. Moreover, auditing every flagged run but sampling unflagged runs requires careful probability weighting to avoid verification bias. Without an independent correctness specification and a demonstrated ability to detect errors missed by the oracle, the resulting wrong-pass rates are not reliably identified.

This undermines the proposed mutation-transfer test itself, because its real-failure denominator is constructed from potentially incomplete or misclassified ground truth. Consequently, even statistically significant differences between seeded and real failures could reflect measurement error. The paper would therefore lack a sufficiently trustworthy empirical foundation for its central claim.

7. What would make this a clear accept?
I would move from Weak Reject to Accept, potentially Strong Accept, if the eventual paper demonstrated the following results.
A. Establish independent ground truth
A task-level correctness specification should distinguish required changes, forbidden changes, tolerated incidental effects, and ambiguous behavior.

The adjudication sample should be drawn with known inclusion probabilities, include oracle-unflagged executions, and use independent human labels. The released artifact should contain enough evidence to reproduce the prevalence estimates and characterize adjudicator disagreement.
B. Resolve C2 with adequately powered, preregistered tests
I would require evidence for the same transfer estimand on AndroidWorld/MobileWorld and AppWorld, with uncertainty accounting for clustering, multiplicity, and support mismatch.

Both a positive and a negative result can be valuable:
- A positive result would demonstrate that frozen published mutation operators predict real-failure miss rates within meaningful tolerances and generalize to an unseen agent.
- A negative result would demonstrate a systematic, explainable failure of mutation-score transfer, surviving template matching, failure-mode refinement, and comparison against a composition-only null.
What would not suffice is a large collection of inconclusive tests accompanied by anecdotal examples of faulty checkers.
C. Demonstrate practical predictive value
The proposed method should beat the native score and a real-run calibration baseline on held-out agents, with uncertainty.

For a positive-transfer paper, a useful result would be a meaningful reduction in corrected-score error and acceptable confidence-interval coverage on both benchmark families.

For a negative-transfer paper, I would expect a demonstrably better alternative or a defensible rule describing when mutation calibration is reliable and when it should not be used.
D. Establish what state-level instrumentation uniquely contributes
A convincing C1/C4 result would contain real, independently confirmed wrong-PASS cases that trajectory-only review misses, alongside sufficient evidence that the oracle detects them consistently.

The comparison must use strong trajectory and state-reading baselines on the same cases.

The paper should also demonstrate that the mask does not create a substantial false-negative problem by hiding meaningful writes.
E. Release a reproducible evaluation artifact
The artifact should include pinned benchmark commits, task-level correctness contracts, reference executions, mutation operators, sampling probabilities, annotation protocols, evaluator versions, and analysis scripts.

For the physical-device arm, provide device/API configurations and evidence that benchmark initialization and restoration work correctly.

These requirements concern experimental validity and reproducibility rather than the resources or time needed to conduct the research.

If C2 is convincingly resolved across both benchmark families and the state-level truth is independently validated, I would regard the work as a genuine methodological contribution to ML evaluation rather than benchmark maintenance.

8. Acceptance probability for ICML 2027
10–25%
Judgment conditional on competent execution of the current specification

This is an expert acceptance-probability band, not an empirical probability estimate.

My reasoning is as follows.

The topic is well aligned with ICML 2027, and the central scientific question is worth asking. The proposal also has unusually explicit failure criteria and does not depend on a leaderboard inversion or any predetermined positive finding.

However, the most likely substantial obstacles are structural, not implementation-related: an independently trustworthy correctness oracle, adequate failure-mode support, and a result that distinguishes informative mutation-transfer behavior from ordinary population-composition effects.

Even if the system is implemented competently and the experiments run as planned, those obstacles could leave a technically sound paper with insufficient novelty or generality.

I would raise the band to 25–40% if the authors independently establish state-level correctness and the C2 pilot produces adequately populated, interpretable cells in both families. I would regard above 40% as defensible only with a strong completed result that substantially changes how the community should use verifier mutation scores.
Prior-art verification and confidence
I read all five supplied documents. The two earlier prior-art reports address a predecessor, F1; the drift scan addresses F1S, which is much closer to the submitted specification. I therefore used the older reports principally for methodological precedents and the drift scan for the current novelty boundary.

The following distinguishes papers independently opened in this review from work known only through the supplied reports or search results.
Paper / identifier	Opened in this review?	Relevant implication
AgentRewardBench — arXiv:2504.08942	Yes, full HTML text	Already measures real-run rule-based evaluator errors and analyzes agent-ranking discrepancies.  arxiv.org
MobileJudgeBench — arXiv:2608.11434	Yes, HTML text; figure inset not independently verified	Contains human-annotated mobile trajectories, including AndroidWorld, reducing C1's novelty.  arxiv.org
AppWorld — arXiv:2407.18901	Yes, primary abstract	State-based unit tests and collateral-damage checks are established benchmark design elements.  arxiv.org
VerifierBench — arXiv:2610.28679	Yes, full HTML text	Tests valid alternatives, invalid solutions, and mutation-based verifier reliability; additional close context for C4.  arxiv.org
Silent Instrument Errors Reorder Agent Leaderboards — arXiv:2611.04399	Yes, full HTML text	Demonstrates concrete leaderboard measurement errors and corrected orderings.  arxiv.org
Finding Side-Effect Loopholes in Verifiable Rewards — arXiv:2610.09142	No full paper opened; author-hosted public description located	Direct predecessor for mutation auditing of shipped agent verifiers.  openadapt.ai
Red-Teaming the Grader — OpenReview zh33pqlBjf	No; supplied drift scan only	Audit-driven regrading of real agent runs, but no verified independent prevalence study in the material reviewed
Ranking-inversion analysis — arXiv:2609.25173	No; supplied reports only	Previously derives analytical inversion conditions; not independent proof of C3's empirical result
Just et al., FSE 2014, Are Mutants a Valid Substitute for Real Faults in Software Testing? — DOI: 10.1145/2635868.2635929	No; supplied reports only	Foundational precedent for questioning the transferability of mutation-testing results

The latter items should not be interpreted as independently full-text verified in this review. I also cannot certify that no additional November 2026 preprint anticipates C2; this was a referee review, not an exhaustive new prior-art search.
Final decision
Weak Reject at the proposal stage, with a credible path to Accept.

The most important change is not to add models, phones, or benchmarks. It is to strengthen the identifiability and external validity of C2, beginning with independent ground truth and a rigorous test of whether frozen synthetic fault operators predict errors on real held-out agent executions.

If that experiment yields a decisive finding, the proposal could make a meaningful contribution to ICML's evaluation methodology literature, even if the principal hypothesis is rejected.

Model used: OpenAI GPT-6. A more granular internal model version or build identifier is not available to me, so I cannot truthfully provide a finer version number.