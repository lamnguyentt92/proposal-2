# IDEA_M1: Red-teaming as species discovery — comparing attackers and certifying defenders by missing mass instead of ASR@k

Citation status used below: **[notes]** = identifier appears in `research_notes/.../agent_security_sota.md` or `hot_topics.md`; **[fetched]** = primary record or full text opened in this ideation session (2026-11-20); **[index]** = only the alphaXiv index record (ID, title, first lines of abstract) was seen.

- Gap addressed: **G8** (budget-normalised comparison of automated red-teamers). Secondary: G3 (ASR without intervals or a common estimand), G5 (what "evaluated adaptively" should mean for a defence).

- Target venue and track: **ICML 2027**, topic area "Evaluation (methodology, meta-studies, replicability)", contribution type **"Datasets, Evaluations and Benchmarks"** (an evaluation-methodology paper: no new attack, no new defence). If the decisive experiment fails, the same study is a "Negative Results" submission ("unseen-species estimators do not transfer from fuzzing to LLM red-teaming, and here is why"), provided the why is established.

- Problem (1 paragraph): Automated agent red-teamers are reported at budgets that cannot be compared: ASR@10 (2609.33628 [notes]), ASR@800 (2610.41998 [notes]), "up to 10 attempts" (2608.30207 [notes]), and RL compute at the scale of a post-training run (2607.26115 [notes]). Transfer results conflict (2606.10525 vs 2609.33628 [notes]), and co-trained attackers lose diversity while their success rate keeps rising (2611.19680 [notes, abstract fetched]: retention 0.61–0.63 after 12 rounds on 26 behaviours). A meta-analysis of 259 agentic-security papers finds that 10.8% state an attack budget and argues that ASR is a family of metrics, but it stops at a reporting checklist and runs no attack (2609.25173 [fetched, full text]). ASR@k depends on the budget, on the scenario mix, and on when the campaign stopped, so two questions have no budget-independent answer today: "which attacker is stronger?" and "how much undiscovered risk is left in this defender after this campaign?".

- Key insight (the non-obvious observation; 2–3 sentences): A red-teaming campaign is a sampling process over an unknown set of vulnerability classes, which is the unseen-species problem. The quantity that does not depend on where the campaign stopped is the *discovery probability* (missing mass): the chance that the next attack query exposes a class not yet seen, which Good–Turing-type estimators recover from the number of classes seen exactly once. Fuzzing adopted this framing and, crucially, worked out the correction for *adaptive search bias* (the sampler concentrates on what already worked), which is exactly the property of RL and evolutionary attackers that makes ASR@k curves misleading; agent red-teaming has not imported either piece.

- Approach (how the insight becomes a method/system/theory):
  1. **Species definition at three granularities**, all computed on every successful attack: (a) *effect signature* = scenario × canonicalised environment-state change that realises the attacker goal × carrier field of the payload (fully automatic in an executable environment); (b) *strategy class* = label from a fixed taxonomy, assigned by an LLM and validated against two human annotators with reported agreement; (c) *patch-equivalence* = two successful attacks are the same class if a minimal mitigation derived from one (e.g. adding it as a negative demonstration to the defender) blocks the other, computed on a subsample to check that (a) and (b) are not arbitrary.
  2. **Campaign log as an incidence stream**: query index, cost in target-model queries and in USD, success flag, species under each definition.
  3. **Estimator suite**: sample coverage (1 − singletons/n), lower-bound richness estimators, rarefaction/extrapolation curves with bootstrap intervals, and the adaptive-bias-aware estimators introduced for greybox fuzzing. For defenders where no success is found, report the upper bound on discovery probability instead of "ASR = 0".
  4. **Coverage-standardised comparison**: attackers are compared at equal estimated coverage rather than equal budget; defenders are reported with a residual discovery probability after a pooled campaign.
  5. **Validation ladder**: open-weight defenders on local GPUs, where queries are cheap enough to run campaigns close to exhaustion and obtain a pseudo ground truth for richness; then API defenders at small budgets, where only the estimators are available.

- Contribution type: **new measurement/benchmark** (measurement instrument plus a validation study; negative-result fallback).

- Claims (falsifiable, 2–4):
  - **C1 (predictive validity).** Estimators fitted on the first half of a campaign's budget predict the number of new classes found in the second half within their 95% intervals for at least 4 of 5 attacker families, and the bias-aware estimators have lower error than plain Good–Turing and than a Beta-binomial best-of-N extrapolation.
  - **C2 (rank disagreement).** Ordering attackers by ASR@k and by coverage-standardised richness gives Kendall τ ≤ 0.5, and RL-trained attackers rank higher by ASR than by richness.
  - **C3 (external validity; the decisive claim).** Across at least 8 defender configurations, a defender's residual discovery probability after a pooled automated campaign predicts its failure rate against a held-out attacker family and a held-out human-written attack set better than pooled ASR does (higher Spearman correlation, paired bootstrap).
  - **C4 (transfer is partly a sampling artefact).** Raw attack-class overlap between two defenders rises with budget, and an unseen-shared-species correction applied at small budget predicts the large-budget overlap; if so, part of the 2606.10525-vs-2609.33628 disagreement is under-sampling rather than a property of the models.

- Closest work known so far (with identifiers) and the expected delta:
  - **STADS: Software Testing as Species Discovery**, arXiv 1803.02130 [fetched record], and **Estimating Residual Risk in Greybox Fuzzing**, Böhme, Liyanage, Wüstholz, ESEC/FSE 2021 [fetched conference page]: the source framing and the adaptive-bias estimators. Delta: no natural "coverage element" exists for LLM attacks, so the species definition and its validation (patch-equivalence) are new; the sampler is an LLM policy, not a mutation fuzzer.
  - **SABER**, arXiv 2601.22636 [abstract fetched]: Beta model of per-prompt success to extrapolate ASR@N under best-of-N resampling of jailbreaks. Delta: it extrapolates a success *rate* for i.i.d. resampling of one attack; it does not estimate how many distinct vulnerabilities remain, does not handle adaptive attackers, and is not agentic. It is the strongest statistical baseline for C1.
  - **Survival analysis of time-to-jailbreak**, arXiv 2605.12869 [abstract fetched]: three chat models, preliminary. Delta: time-to-first-success per prompt, no class structure, no residual-risk estimate.
  - **Attack Diversity Retention**, arXiv 2611.19680 [notes, abstract fetched]: diversity relative to an untrained attacker. Delta: a relative spread metric with no extrapolation and no link to defender risk.
  - **Attack Success Rate Is Not a Number**, arXiv 2609.25173 [fetched]: identifies budget and adaptivity as free parameters; analytical only, "no empirical ranking inversion" reported by its own limitations section. Delta: this idea supplies the estimand and the empirical inversion test.
  - Harnesses to build on, not competitors: AgentDojo 2406.13352, AgentDyn 2602.03117, AutoDojo 2606.15057, MetaPI 2611.10026 [all notes].

- Evaluation sketch: settings, baselines (strongest first), metrics, decisive experiment
  - **Settings.** Environments: AgentDojo and AgentDyn through an existing adaptive harness. Attackers (at least five families with different search bias): static templates, tree/iterative black-box refinement as in 2606.10525, MCTS fuzzing (AgentVigil 2505.05849), RL (PISmith 2603.13026, code released per notes), evolutionary/principle-library (2608.30207 or 2603.22341). Defenders: open-weight models of two sizes with and without a prompt-level defence, a detector filter, a tool-policy defence (Progent 2504.11703) and an adversarially fine-tuned open model (Meta-SecAlign 2507.02735); plus 2–3 API models at small budget.
  - **Baselines, strongest first.** (1) Budget-matched ASR@k curves in target queries and in USD — the referee's default "just match the budgets" answer; C2 and C3 must beat it. (2) SABER-style Beta extrapolation (2601.22636). (3) Time-to-first-success survival curves (2605.12869). (4) Diversity retention (2611.19680) and embedding-dispersion diversity.
  - **Metrics.** Interval coverage and relative error of second-half predictions (C1); Kendall τ between rankings (C2); Spearman correlation with held-out attacker success, with paired bootstrap over defenders (C3); predicted vs realised overlap (C4); sensitivity of every result to the three species definitions.
  - **Decisive experiment.** C3. Hold out one automated attacker family and one human-written set; compute residual discovery probability and pooled ASR from the remaining attackers only; test which one predicts held-out failure across defenders. Negative outcomes that would sink the claim: no gain over budget-matched ASR, or intervals in C1 that fail to cover for adaptive attackers.

- Resources needed vs available (00_CONSTRAINTS.md):
  - Commercial APIs: attacker LLMs and 2–3 API defenders at small budgets — available.
  - 1–2 GPUs: serving open-weight defenders for near-exhaustive campaigns and LoRA-scale RL attacker training — available at mid-size model scale; frontier-scale self-play (2607.26115) is neither needed nor attempted.
  - Annotators: two annotators for strategy-class labels (English attack text; language skills sufficient) — available.
  - Software-testing expertise: the fuzzing estimators and campaign instrumentation come from the researcher's own field — available.
  - Not needed: Android testbed, white-box access to closed models.

- Risks and unknowns:
  - **Species definition.** If results flip between definitions (a), (b), (c), the instrument is not well defined; the sensitivity analysis could become the main (negative) finding.
  - **Sparse successes on frontier defenders.** 2611.11861 [notes] reports the only open reproducible adaptive attacker broke 2 of 80 AgentDojo scenarios; with near-zero discoveries the method yields only an upper bound, so the informative results will come from open and mid-tier defenders.
  - **Estimator assumptions.** LLM attackers with cross-run memory are more strongly adaptive than fuzzers; the fuzzing corrections may not hold. Unknown until C1 is run.
  - **Open-ended class space.** Richness estimates are lower bounds; the paper must not present them as totals.
  - **Attacker refusals.** Safety-tuned attacker models refuse (2606.10525 [notes]); attacker model choice may confound family comparisons.
  - **Novelty check still owed.** Two index searches found no unseen-species treatment of LLM red-teaming; OpenReview submissions were not searched.

- Conference core / journal extension (1 line each):
  - Conference core: species definitions, estimator suite, and C1–C3 on one text tool-calling environment family with five attacker families.
  - Journal extension: adaptive-bias analysis specific to LLM attackers, C4 at scale, GUI/mobile and memory-persistent targets, and a stopping rule for defence certification.

- Generator perspective: empirical/measurement
