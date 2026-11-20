<!-- Cross-family review, saved verbatim. Reviewer model as self-reported: OpenAI GPT-6 (no finer version exposed). Run by the author on 2026-11-20 with the prompt and attachments in ideation/xmodel_kit/. Everything below this comment is the unedited response. -->

# **Independent Adversarial Prior-Art Review — P2**

ICML 2027 · Evaluation · Datasets, Evaluations and Benchmarks

**Review date:** 20 November 2026\
**Specification:** *Are the Passes Real? A State-Level Audit of Mobile-Agent Benchmark Verdicts and a Test of Whether Verifier Mutation Scores Transfer to Real Agent Failures*

## **1. Scope and preliminary findings**

I reviewed the P2 proposal together with `P2_priorart_A.md`, `P2_priorart_B.md`, and `P2_drift_scan.md`. The reports describe predecessor designs as well as the current proposal, so evidence concerning abandoned fault-count estimators or metamorphic inverse-task instruments must not be mistaken for anticipation of the current claims C1–C5.

The central distinction is between three research questions:

1. **Verifier adequacy:** Can artificially constructed faulty states fool an agent benchmark's grader?
2. **Verdict validity:** How frequently does that grader incorrectly accept or reject real agent executions?
3. **Transfer validity:** Can the grader's behavior on seeded faults predict its behavior on actual agent failures, conditional on failure mode?

The first two have substantial prior art. The third is the proposed contribution that requires the most adversarial scrutiny.

Two important anticipations are already independently confirmed from primary publications:

- **AppWorld (ACL 2024)** explicitly evaluates task completion through state-based unit tests that check collateral damage. Thus, end-state verification, allowance for different successful solutions, and detection of unintended state changes are established benchmark-design techniques, not new primitives.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://aclanthology.org\&sz=32)

  ACL Anthology

- **AgentRewardBench (2025)** evaluates 1,302 real web-agent trajectories with expert annotations of success and side effects, compares official rule-based evaluators against human judgments, and documents discrepancies. Thus, measuring evaluator errors on real agent trajectories predates P2.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arxiv.org+1



The remaining investigation focuses on whether prior work already combines verifier mutation testing with real-failure measurements, especially in mobile agents and stateful benchmarks.

### **Additional high-risk overlap**

The independent search also found direct precedents for the proposed state-reading verifier baseline and oracle evaluation:

- **Interactive Reward Agent** (arXiv:2607.25904, July 2026) verifies GUI completion by inspecting post-execution system configurations, files, and application settings, rather than relying exclusively on screenshots.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arxiv.org

- **VeriCUA: Verification as Agentic Exploration for Computer-Using Agents** (arXiv:2610.40578, October 2026) combines GUI and code-based evidence gathering across computer-use environments.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arxiv.org

- **Evidence-First Agentic Verification** (arXiv:2610.17724, October 2026) evaluates its verifier on both 2,586 human-labelled criteria and a separate 13-family fault-injection suite, reporting detection and false-alarm measures. This comes especially close to P2's proposed C4 evaluation methodology, although it does not establish C2's seeded-versus-real-failure transfer hypothesis.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arxiv.org



These findings narrow the defensible novelty of C4: the contribution cannot simply be *verification using hidden environment state* or *evaluation using injected faults and human-labelled agent errors*. It must be the specific route-diverse whole-state oracle, its demonstrated advantages over existing verifiers, and its usefulness for the C2 experiment.

### **A stronger C4 anticipation than the earlier reports emphasized**

The full text of **VeriCUA** contains an explicit **online AndroidWorld verifier evaluation**, including structured-state access, repeated verifier passes, visual fallback, agreement rates, wrong-fail counts, and the effects of additional verification passes. This is not merely a desktop-verifier precedent.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org



Consequently, C4 must demonstrate an advantage over an existing **AndroidWorld environment-aware verifier**, not just over a generic LLM prompted with a state dump. The claimed advantage of a route-diverse differential oracle is still potentially distinct, but its incremental benefit needs a controlled comparison.

## **2. Searches run**

**Search date:** 20 November 2026. The review covers material discoverable up to that date, including preprints and submissions that may not yet have undergone peer review.

I searched across arXiv, ACL Anthology, ICLR proceedings, indexed ICML/NeurIPS proceedings, OpenReview, software-engineering publications, GitHub, university-hosted papers, and dissertation repositories. I used several overlapping query families rather than relying on titles containing “agent evaluation”.

The following are representative **queries actually run**; variants substituted *checker*, *grader*, *reward function*, *test oracle*, *judge*, *fault injection*, and *mutation testing*.

```

"MobileJudgeBench" AndroidWorld rule based precision recall
"Finding Side-Effect Loopholes in AppWorld and WorkArena Verifiers"
"Mutation Testing of Task-Scoped State Oracles"
"Measuring the Checker" mutation analysis benchmark oracles
agent verifier mutation score transfer real failures
"seeded faults" "real failures" agent benchmark
"synthetic faults" "real failures" grader
"mutation score" "agent" "false positives" benchmark
agent benchmark verifier fault injection real agent failures
AndroidWorld checker false pass wrong pass audit
MobileWorld verifier scoring wrong recipient
AppWorld collateral damage duplicate write verifier
site:openreview.net "side-effect omissions" evaluator rankings
site:openreview.net verifier flaws agent benchmark 2026
site:proceedings.mlr.press agent verifier mutation benchmark
site:aclanthology.org agent verifier state audit 2026
site:arxiv.org/abs/2611 agent evaluator mutations real failures
agent benchmark regrading leaderboard rank reversal
agentic benchmark "fault injection" "real agent"
software testing mutants substitute real faults Just 2014
"state field coverage" oracle quality mutation score
Android GUI alternative routes state oracle noise snapshots
AndroidWorld physical devices emulator grader comparison
thesis dissertation mutation scores synthetic faults oracle
site:github.com android_world verifier issue
site:github.com mobileworld scoring fixes

```

I also searched the literature under older terminology: *test-oracle problem*, *oracle deficiency*, *state-based assertions*, *mutation–real-fault coupling*, *metamorphic testing*, *differential testing*, *frame conditions*, *collateral state changes*, and *measurement validity*.

These searches uncovered two particularly important records not given comparable emphasis in the earlier reports: a paper that already performs **fault-injection auditing plus real-agent regrading with rank changes**, and a paper that evaluates **an environment-aware verifier directly on AndroidWorld**.

Verification levels below mean:

- **Full text:** the paper's primary manuscript or author-hosted full text was opened and inspected.
- **Abstract:** the primary publisher, proceedings, or author record was opened, but the complete manuscript was not verified.
- **Not independently verified:** the record appeared in searches or supplied reports, but its primary source could not be opened.

## **3. Closest works and exact remaining delta**

### **3.1 Direct threats to the proposed contributions**

**1. Finding Side-Effect Loopholes in AppWorld and WorkArena Verifiers**

**Identifier:** [arXiv:2610.09142v3](https://arxiv.org/abs/2610.09142?utm_source=chatgpt.com)\
**Verification:** Full text; version dated 16 November 2026.

**What it already does:** Constructs controlled invalid edits to known-correct executions and checks whether official benchmark evaluators reject them. It demonstrates duplicate-write acceptance in AppWorld across six tasks from two templates, and wrong-field acceptance in all 36 valid WorkArena edited runs. Its paper also describes a small archive of earlier agent runs, but does not use those to establish population-level error rates.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.cnoctave.top\&sz=32)

arxiv.cnoctave.top



**Exact delta:** P2 proposes measuring *actual agent-failure-conditioned miss rates* and comparing them with the miss rates of those published mutants.

**Does the delta matter?** **Yes, substantially for C2.** But mutation recipes, controlled invalid-state construction, independent wrong-effect checks, and proof of verifier loopholes are already anticipated. P2 must not claim these techniques as original.

**Adversarial finding:** The published mutants are selected to expose particular loopholes. Their ability to transfer to the distribution of natural agent failures is precisely the untested assumption. That supports the importance of C2, but also creates a significant selection-bias problem.

**2. Benchmarking LLM Judges for Mobile Agent Evaluation — MobileJudgeBench**

**Identifier:** [arXiv:2608.11434](https://arxiv.org/abs/2608.11434?utm_source=chatgpt.com)\
**Verification:** Full manuscript.

**What it already does:** Collects 931 human-annotated trajectories across six mobile benchmarks. Its AndroidWorld subset contains **205 trajectories over 52 tasks**. It reports the built-in rule-based checker's accuracy, precision, and recall as **94.6%, 98.6%, and 87.2%**, respectively, against human annotations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://sex8x8.com\&sz=32)

sex8x8.com



**Exact delta:** P2 uses persistent device/backend state, rather than trajectory-visible evidence alone, to identify unrequested effects; it also proposes a larger, template-clustered, two-direction audit.

**Does the delta matter?** **Yes, but conditionally.** C1 cannot be presented as the first mobile-agent benchmark grader-error measurement. It can claim incremental measurement value only if persistent-state access reveals errors that trajectory review systematically misses.

**Important statistical correction:** The 98.6% precision implies approximately 1.4% of checker-predicted successes are false under this study's annotation standard. It does **not** mean 1.4% of every AndroidWorld execution is a false pass. That denominator distinction must remain explicit.

**3. AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories**

**Identifier:** [arXiv:2504.08942](https://arxiv.org/abs/2504.08942?utm_source=chatgpt.com)\
**Verification:** Full text.

**What it already does:** Audits 1,302 real web-agent trajectories against expert labels, including success and side-effect criteria. The official rule-based evaluators obtain **83.8% precision** and **55.9% recall**, and the paper compares agent success estimates under human versus automatic evaluation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org+2



**Exact delta:** Mobile benchmarks, persistent-state-only failures, and seeded-versus-real failure-mode transfer.

**Does the delta matter?** **Yes for C2; moderate for C1.** The fundamental measurement of false accepts and false rejects on real agent runs is already published, as is the issue that regrading affects comparisons.

A correction to the earlier reports: AgentRewardBench's annotators could consult additional environmental evidence when screenshots were insufficient. The defensible distinction is **absence of a published systematic whole-state differential audit**, not an assertion that the annotators could never inspect the environment.

**4. When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark**

**Identifier:** [arXiv:2610.16067](https://arxiv.org/abs/2610.16067?utm_source=chatgpt.com)\
**Verification:** Full text.

**What it already does:** Designs an oracle-integrity suite, injects **seven evaluator defect classes**, identifies a state-mutating reward-function defect, and replays **4,320 archived real agent episodes**. In the authors' particular post-session scoring configuration, the corrected aggregate success measure falls from **94.3% to 65.5%**. Corrections differ by agent, and the leading point-estimate ordering changes. The paper supplies task-clustered intervals.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org



**Exact delta:** It does not compare native-grader miss probabilities on matched seeded faults and naturally occurring agent failures by failure mode. Nor does it supply P2's Android state-only prevalence estimate.

**Does the delta matter?** **Very strongly for C3, moderately for C2.** This is an especially important anticipation the proposal should cite.

The paper carefully qualifies the discovered defect: the benchmark's own agent consumes a correctly computed reward before a later state mutation. Its major wrong-score result concerns the authors' separate post-session scoring path. P2 must preserve that distinction instead of characterizing the work as proof that all official benchmark scores were corrupted.

**Referee implication:** Fault injection, state replay, agent-dependent score correction, and even ranking changes with clustered confidence intervals are no longer an unoccupied combination. C2's **direct transfer test**, not the other components, must be the principal contribution.

**5. Evidence-First Agentic Verification (Sauron)**

**Identifier:** [arXiv:2610.17724](https://arxiv.org/abs/2610.17724?utm_source=chatgpt.com)\
**Verification:** Full text.

**What it already does:** Assesses verification against **2,586 human-labelled criteria**, a paired **13-family fault-injection suite**, and a separate benchmark of genuine agent errors. Its injected-fault experiment reports **97% detection** and **2% false alarms on clean controls**.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org



**Exact delta:** P2 compares the *same benchmark's native checker* on matched failure modes across artificial mutations and natural agent failures, and proposes an Android whole-state differential oracle.

**Does the delta matter?** **Yes for C2, less for C4.** Sauron already demonstrates that injected faults and naturally occurring errors can both be used to assess an agent verifier. Therefore, P2's novelty is not simply collecting both kinds of failures. It is the **explicit, mode-conditioned equivalence or non-equivalence test of their detection probabilities**.

**6. VeriCUA: Verification as Agentic Exploration for Computer-Using Agents**

**Identifier:** [arXiv:2610.40578](https://arxiv.org/abs/2610.40578?utm_source=chatgpt.com)\
**Verification:** Full text, including AndroidWorld appendix.

**What it already does:** Investigates environment-aware computer-use verification with access to GUI and structured evidence. Crucially, it includes **online AndroidWorld evaluations**, varying verifier passes and visual fallback while recording false positives and wrong-fail counts.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org



**Exact delta:** P2's explicitly constructed *route-diverse, masked persistent-state differential oracle*, as opposed to exploratory evidence gathering.

**Does the delta matter?** **Only if convincingly demonstrated.** VeriCUA is a direct AndroidWorld evaluation baseline. P2's generic “LLM state-reading verifier” baseline, by itself, is too weak a comparison.

**7. AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents**

**Identifier:** [DOI:10.18653/v1/2024.acl-long.850](https://doi.org/10.18653/v1/2024.acl-long.850?utm_source=chatgpt.com)\
**Verification:** ACL Anthology primary record and abstract.

**What it already does:** Uses state-based unit tests to evaluate API-agent task success, including collateral effects from unintended changes.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aclanthology.org\&sz=32)

ACL Anthology



**Exact delta:** Systematically auditing the evaluator rather than treating it as ground truth; specifically, relating its mutant miss rate to actual agent errors.

**Does the delta matter?** **Yes for C2.** However, AppWorld already embodies the principle of checking more than task-goal completion. The proposal's state-frame design must therefore be positioned as an audit of imperfect implementations, not the invention of collateral-damage-aware grading.

### **3.2 Foundational and less direct anticipations**

**8. Are Mutants a Valid Substitute for Real Faults in Software Testing?**

**Identifier:** [FSE 2014, author record](https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014-abstract.html?utm_source=chatgpt.com)\
**Verification:** Author-hosted abstract.

**What it already does:** Empirically studies whether mutation testing stands in for real software defects, establishing the precise methodological question that motivates C2.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://homes.cs.washington.edu\&sz=32)

homes.cs.washington.edu



**Exact delta:** Its objects are programs, defects and tests—not agent benchmarks, graders, and execution-end-state errors.

**Does the delta matter?** **Yes for application specificity, no for the conceptual hypothesis.** The phrase “does mutation testing predict real failure detection?” is not novel. P2's novelty can only lie in what it establishes specifically about interactive-agent evaluators.

**9. SWE-Mutation: Can LLMs Generate Reliable Test Suites in Software**

**Identifier:** [ACL Findings 2026](https://aclanthology.org/2026.findings-acl.1976/?utm_source=chatgpt.com)\
**Verification:** Full paper.

**What it already does:** Constructs **2,636 mutants** across Python and multilingual software-engineering benchmark instances and evaluates how well agent-generated test suites reject realistic incorrect programs. It explicitly discusses the risk that artificial mutants are unrepresentative of real faults.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aclanthology.org\&sz=32)

aclanthology.org



**Exact delta:** Mutation realism for native agent benchmark verdicts rather than testing coding-agent-produced tests.

**Does the delta matter?** **Moderately.** It strengthens the expectation that P2 include severity- and realism-matched mutation baselines, rather than relying solely on coarse fault-class labels.

**10. State Field Coverage: A Metric for Oracle Quality**

**Identifier:** [Author-hosted ASE 2025 manuscript](https://nmaguirre.github.io/assets/pdf/ase2025a.pdf?utm_source=chatgpt.com)\
**Verification:** Full paper.

**What it already does:** Measures which parts of program state an oracle inspects and correlates that coverage with fault-detection ability measured through mutation analysis. Its evaluation includes 273 representation invariants and 249,027 assertions.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://nmaguirre.github.io\&sz=32)

nmaguirre.github.io



**Exact delta:** P2 measures *observed wrong verdicts on real agent-generated end states*, not merely state-field access or correlation with mutation score.

**Does the delta matter?** **Yes as a methodological baseline.** It provides a plausible lower-cost alternative: static checker-state coverage may predict the same weaknesses as P2's more expensive injected mutants. A referee could reasonably request this comparison.

**11. ROUTE: Roads Not Taken in UI Testing**

**Identifier:** [DOI:10.1145/3571851](https://doi.org/10.1145/3571851?utm_source=chatgpt.com), ACM TOSEM 2023\
**Verification:** Full text.

**What it already does:** Augments Android UI tests by exploring alternate interaction sequences, using snapshots to restore app execution states and addressing dynamic UI content.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://seal.ics.uci.edu\&sz=32)

seal.ics.uci.edu



**Exact delta:** ROUTE's test-oracle states primarily represent GUI widget hierarchies, whereas P2 seeks allowable variation in typed persistent database, storage, provider, and settings diffs across legitimate routes.

**Does the delta matter?** **Moderately.** Alternate-route testing and snapshot-backed reproducibility are established. P2 must precisely define the additional representational and statistical benefit of its persistent-state mask.

**12. Do Multi-Agents Dream of Electric Screens? Achieving 100% on AndroidWorld Through Task Decomposition**

**Identifier:** [arXiv:2602.07787v2](https://arxiv.org/abs/2602.07787?utm_source=chatgpt.com), updated 16 November 2026\
**Verification:** Full text.

**What it already does:** Evaluates AndroidWorld across cloud emulators, stock emulators, and **real Pixel 7 phones**, reporting benchmark results and agent reliability statistics.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://borowiecki.dev\&sz=32)

borowiecki.dev



**Exact delta:** P2 aims to transfer and validate an **identical masked state-differential verifier** between emulator and rooted physical devices, not merely execute an AndroidWorld agent on both.

**Does the delta matter?** **A little for C5.** Physical-device AndroidWorld experiments already exist; P2's exact verifier-replication protocol appears more specific, but is not a major stand-alone novelty claim.

**13. MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive and MCP-Augmented Environments**

**Identifier:** [ACL 2026, paper 278](https://aclanthology.org/2026.acl-long.278/?utm_source=chatgpt.com)\
**Verification:** Full text.

**What it already does:** Specifies 201 mobile tasks and four success-checking modes: database verification, storage inspection, textual matching, and application callbacks. It includes a rooted emulator and self-hosted application services.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aclanthology.org\&sz=32)

aclanthology.org



**Exact delta:** An external, whole-state correctness audit that inspects effects not necessarily covered by the task's existing checker.

**Does the delta matter?** **Yes for implementation validity, less for novelty.** Any whole-state audit must cover the self-hosted backend databases and callbacks, not just Android files accessible through root.

## **4. Claim-by-claim status — Section 5**

| Claim                                                   | Status as of 20 Nov 2026 | Adversarial assessment                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **C1 — State-level prevalence**                         | **Partly anticipated**   | Both-direction grader-error measurements already exist for AndroidWorld (MobileJudgeBench) and real web-agent tasks (AgentRewardBench). The potentially new quantity is **the proportion of wrong passes only visible in persistent state**, with credible clustered intervals. No independently verified primary record establishes that exact quantity across P2's three benchmarks.                                                                                           |
| **C2 — Mode-conditional seeded-to-real transfer**       | **Not found**            | This is the strongest remaining gap. Mutation miss rates and real-agent grader errors have both been studied; Sauron even assesses a verifier using separate injected and real-error suites. However, I did **not** verify a prior paper directly testing equivalence between **native-checker miss probabilities on frozen mutants and genuine agent failures within matched modes**, followed by held-out-agent score calibration. “Not found” is not proof of global novelty. |
| **C3 — Differential verdict error and ranking changes** | **Partly anticipated**   | AgentRewardBench already compares evaluations across agents, and arXiv:2610.16067 shows agent-dependent correction, uncertainty, and reordered rankings. The specific mixed-effects analysis for AndroidWorld/MobileWorld/AppWorld remains an application extension, not a novel general phenomenon.                                                                                                                                                                             |
| **C4 — Route-diverse masked oracle quality and cost**   | **Partly anticipated**   | AppWorld's state checks, VeriCUA's AndroidWorld verifier, Interactive Reward Agent's post-state checking, Sauron's evidence-based verification, and older Android UI-testing work cover much of the technique space. A mask learned from **multiple valid routes** and validated against held-out valid routes may be distinct; its advantage over strong existing methods is not established.                                                                                   |
| **C5 — Real-device replication**                        | **Partly anticipated**   | AndroidWorld evaluation on physical phones is published. I did not verify an existing result applying P2's proposed persistent-state masks and seeded-fault checks identically across emulator and three rooted devices. That residual distinction is real but primarily a reproducibility contribution.                                                                                                                                                                         |

### **The most dangerous boundary cases for C2**

There are three reasons a reviewer could reject the central experiment even if it is carefully implemented.

**First, matching fault modes does not guarantee matching fault distributions.** A published *wrong entity* mutation may affect a convenient, easily checked record, whereas real-agent *wrong entity* failures may affect subtler records or different APIs. Equal class labels alone do not make the comparison scientifically interpretable. P2 needs matching on checker template, affected state field, severity, action scope, and possibly execution history.

**Second, selection is endogenous.** Real-agent failures are not random draws from a seeded operator family. Models preferentially fail at confusing interfaces, ambiguous instructions and fragile multistep tasks. A positive or negative equivalence result could reflect different task mixtures rather than a fundamental property of verifier mutation testing. Template weighting and within-template matching are more important than increasing the number of agent seeds.

**Third, the proposed score-correction benefit risks circularity.** If computing a corrected success rate for a new agent still requires auditing its failures to determine their modes and frequencies, the claimed reduction in audit cost is weaker than it sounds. P2 must specify exactly what information is required at deployment to turn its published mutation kill matrix into a corrected score. The held-out-agent evaluation should include that complete information-acquisition cost.

For C1 and C4 there is a separate validity concern: **a reference end state is not necessarily the set of all legitimate end states**. Two valid routes do not prove that all other valid routes' differences are benign or malicious. Likewise, a read-only task can legitimately change caches, history or logs. Without task-specific permission semantics, a whole-state difference may be an audit flag rather than evidence of a wrong benchmark verdict.

## **5. Verdict**

Independent prior-art verdict

# **Incremental**

**The complete P2 concept is not shown to be anticipated by the primary sources I could verify. However, most of its individual components, and several of its proposed results, have already appeared.**

My reasoning is:

- **C1 has a narrow residual novelty claim**, not a broad one. Real trajectory grader errors are already quantified; the new question is their *persistent-state-only component*.
- **C3 is substantially preempted** by prior real-agent regrading studies, including one with fault-injection integrity tests, corrected rank ordering, and clustered confidence intervals.
- **C4 combines established verification ideas** and faces a directly relevant AndroidWorld environment-aware baseline.
- **C5 offers useful replication**, but physical AndroidWorld evaluation itself is not new.
- **C2 remains the single strongest distinct scientific question**: whether the behavior of a benchmark verifier on seeded invalid states predicts its behavior on naturally occurring, matched failures.

Accordingly, **“novel” would overstate the current contribution**, while **“anticipated” would overstate what these independently verified records actually establish**.

For an ICML 2027 *Datasets, Evaluations and Benchmarks* submission, the decisive experiment is C2. A positive finding must demonstrate transferable, practically useful calibration on a genuinely held-out agent. A negative finding must establish a reproducible and statistically well-supported failure of transfer—not merely a mismatch caused by arbitrary mutation choice or sparse categories.

I would regard the research direction as **conditional go** only while the following requirements remain feasible: a well-powered C2 test, transparent task/mode matching, independently adjudicated persistent-state truth, and an evaluated advantage over VeriCUA or another strong environment-aware verifier. If C2 becomes inconclusive and C1's state-only share is negligible, the residual contribution is predominantly benchmark maintenance.

The most important related-work correction is to position the paper as:

> A test of the external validity of verifier mutation scores, supported by a persistent-state audit of mobile-agent benchmarks.

It should **not** be positioned as the first audit of agent benchmark verdicts, the first state-based agent verifier, or the first demonstration that grader errors can reorder agents.

## **6. What I could not search or independently verify**

**OpenReview submissions under review.** I searched indexed titles and forum identifiers, including records described in the supplied reports as “Red-Teaming the Grader,” “The Grader Is an Intervention,” and verifier-flaw studies from ICLR 2027. Direct primary-record retrieval and comprehensive venue enumeration were blocked or incomplete. I therefore do **not** count those descriptions as independent verification, even where the reports claim abstract-level access. Any of those submissions could materially narrow C2.

**Sun's state-oracle mutation paper.** The supplied reports identify Research Square `rs-10665114`, DOI `10.21203/rs.3.rs-10665114/v1`, as one of the three nearest predecessors. I independently searched for it and attempted the publisher and DOI pages, but could not open the primary record. Its reported mutation protocol is consistent with citations in the verified Abrich manuscript, but I cannot certify its own full methodology or exact scope. Consequently, this prior-art gap remains open.

**Other primary-record gaps.** I could not reliably open the full original record for the GPU-kernel mutation-analysis paper `arXiv:2609.22220`; several OpenReview PDFs and submission records; some direct GitHub issue bodies, commits and repositories; or comprehensive citation graphs. I also did not conduct an exhaustive thesis-catalog search, patent-family search, non-English literature review, or every paper in the 2026 NeurIPS, ICML and ACL workshops.

**Evidence limitations.** Several full manuscripts were inspected through accessible author-hosted PDFs, PDF text extraction, or arXiv HTML. Where the source was a PDF, screenshots were attempted; some screenshot endpoints failed even though extracted full text could be read. Claims above distinguish those materials from publisher abstracts and unverified search hits.

**Meaning of a negative search result:** I did not find a verified C2 anticipation in the examined sources. I cannot rule out an unindexed preprint, a newly posted OpenReview submission, private code or an inaccessible publication. This is especially relevant because verifier auditing is currently an active research area.

**Model:** OpenAI GPT-6. A more granular internal version or build identifier is not exposed to me.