# IDEA_S3: What the red team did not find: overlap-based lower bounds on the breakable fraction of a defended agent

Source tags for identifiers: [notes] = in the research-notes files; [read] = primary record opened in this session (alphaXiv full text); [index] = alphaXiv index record only.

- Gap addressed: G8 (application to defence evaluation serves G5).

- Target venue and track: IJCAI 2027 Main Track (compact method with validation; a cross-discipline paper joining software-reliability statistics and agent security, which the call encourages). The same paper would also fit ICML 2027 "Evaluation"; only one venue can receive it.

- Problem (1 paragraph): Defence papers report the fraction of scenarios an attacker broke within its budget, and budgets range from 10 attempts to 800 to industrial-scale training (G8). The number is a snapshot of search effort: in 2611.11861 [read] the most robust defender resists 87% of scenarios at 150 queries and 66% at 320, and resistance falls further as the attacker model gets stronger. Trained attackers also lose diversity (2611.19680 [notes]). A reader cannot tell from any of these tables how many scenarios are breakable but not yet broken, nor compare two attackers run at different budgets.

- Key insight (the non-obvious observation; 2–3 sentences): Result tables discard the overlap between independent campaigns, and the overlap is what speaks about the unseen: if separate campaigns keep breaking the same scenarios the breakable set is nearly exhausted, while many scenarios broken by exactly one campaign mean many more have been broken by none. Unseen-species estimators turn singleton and doubleton counts into a lower bound on the breakable fraction, which is the direction needed to refute a robustness claim, and rarefaction places attackers with unequal budgets on one cost axis. The closest work bounds missing mass under i.i.d. sampling from the deployment distribution (2611.15835 [read]); under an adversary there is no such distribution, so the estimand has to be the size of the breakable set, and a low discovery rate for one attacker says nothing about another.

- Approach (how the insight becomes a method/system/theory):
  1. Species are defined on the victim side and verified by environment state: a benchmark scenario (coarse) or scenario x violating tool-call signature (fine), never attacker text; this mirrors crash bucketing in fuzzing (STADS, 1803.02130 [index]; 2611.15835 cites a 2018 software-testing precedent by Böhme, which I take to be this paper, but its reference list was not checked).
  2. Sampling units are independent replicate campaigns (seed x attacker configuration) at a fixed per-scenario budget; the data are an incidence matrix of campaigns by species.
  3. Estimators: incidence-based lower bound on richness with intervals, sample coverage, and rarefaction/extrapolation curves in queries and in dollars (the estimator family is the one referenced in 2604.05057 [read]: Good 1953, Chao 1984, Efron-Thisted 1976).
  4. Assumptions stated and stressed: the lower-bound property is proved for exchangeable replicates with scenario-specific detection probabilities; simulation and real data show how it behaves when attackers share a base model (positive dependence, expected to keep the bound conservative) and when attackers learn across scenarios (non-stationary detection).
  5. Outputs: for a defence, "broken x%, at least y% breakable (95% lower bound), coverage z"; for an attacker, unique coverage at equal cost and marginal coverage given the others; a saturation diagnostic that separates "this attacker is exhausted" from "the defence is exhausted".

- Contribution type: new method

- Claims (falsifiable, 2–4):
  - C1 (validity): the lower bound computed from cheap attackers at budget B does not exceed the breakable fraction later observed by a pooled campaign at 6–10x the budget that includes a held-out stronger attacker family, in at least 90% of (target, defence) cells.
  - C2 (informativeness): across cells the bound predicts the number of newly broken scenarios at the extended budget (pre-registered rank correlation), where ASR at budget B and a fitted saturation curve do not.
  - C3 (comparison): ranking attackers by rarefied unique coverage at equal cost differs from ranking them by their reported ASR@k, and RL-trained attackers with high ASR show low unique coverage.
  - C4 (no transfer of reassurance): a small per-attacker discovery rate (missing mass under attacker A, estimated as in 2611.15835) does not bound what attacker B finds next; the overlap-based bound does.

- Closest work known so far (with identifiers) and the expected delta:
  - 2611.15835 [read] (MIT/Stanford, 11 Nov 2026): anytime-valid upper bound on the probability of an unseen failure mode, i.i.d. inputs from the deployment distribution (with a known-shift extension), coding-agent traces, no adversary. Delta: adversarial search, a richness estimand identified from cross-campaign overlap, budget-normalised attacker comparison. This is the paper a referee will cite first.
  - 2604.05057 [read]: Good-Turing "blind-spot mass" for deployment coverage of classifiers. 1803.02130 [index]: testing as species discovery. Delta: neither concerns red teaming or defences.
  - 2611.11861 [read]: resistance at 150 vs. 320 queries and across attacker strengths, no extrapolation. 2606.15057 [notes] (AutoDojo) and 2611.10026 [notes] (MetaPI): common harnesses. 2611.19680 [notes]: diversity loss. 2606.10525 vs. 2609.33628 [notes]: conflicting transfer results. 2610.22754 [read]: probability mass of harmful continuations per prompt, white-box and chat-level. 2605.12869 and 2606.00801 [index]: survival analysis of repeated jailbreaks; quality-diversity search.
  - Delta in one line: the first estimator of what a red-team campaign left undiscovered, with a held-out test of whether the estimate was right.

- Evaluation sketch: settings, baselines (strongest first), metrics, decisive experiment
  - Settings: AgentDojo (2406.13352), AgentDyn (2602.03117) and AutoDojo suites [notes]; targets are open-weight models served on 1–2 GPUs, including adversarially fine-tuned open weights (Meta-SecAlign, 2507.02735 [notes]), plus two or three low-cost API models; defences span prompt-level, detector and system-level where code exists (Progent 2504.11703, DRIFT 2506.12104 [notes]); attacker families: fixed templates, LLM-refinement, fuzzing (AgentVigil 2505.05849), RL attackers with released code (PISmith 2603.13026, curriculum RL 2609.33628), one family held out. Code availability is as stated in abstracts and was not checked.
  - Baselines: (1) per-attacker missing-mass bound of 2611.15835 applied to attack attempts; (2) parametric saturation-curve extrapolation of ASR@k; (3) union ASR at budget B, which implicitly sets the undiscovered fraction to zero; (4) best single attacker at maximum budget.
  - Metrics: coverage of the bound, relative gap to the later-observed breakable fraction, prediction error for new discoveries, cost per unique species.
  - Decisive experiment: freeze all estimates at budget B, then run the extended pooled campaign with the held-out family. The idea fails if the bound is violated in many cells (dependence reverses its direction) or is too loose to distinguish defences.

- Resources needed vs available (00_CONSTRAINTS.md): commercial APIs and 1–2 GPUs are sufficient because targets are mid-sized open models and attackers are black-box; no human annotation is needed since outcomes are state-verified; the statistical framing comes from automated software testing, the researcher's field. The open quantity is API spend for replicate campaigns, controlled by subsampling scenarios.

- Risks and unknowns: scenarios that no available attacker family can break are invisible to any overlap estimate, so the bound is relative to the attacker pool; learning attackers violate the closed-population assumption; on frontier targets successes may be so rare that the bound is wide; species granularity changes the numbers and must be fixed in advance; the authors of 2611.15835 are well placed to extend their method to adversaries; IJCAI permits LLM use for polishing only, so text from this AI-assisted card must not be copied into a submission.

- Conference core / journal extension (1 line each):
  - Core: estimator, assumptions and lower-bound result, held-out validation on prompt-injection defences, attacker comparison at equal cost.
  - Extension (JAIR/AIJ): memory defences on a dynamic memory benchmark (Trojan Hippo, 2605.01970 [notes]) and mobile agents (MobileProbe, 2611.16693 [notes]), sequential anytime-valid versions, and treatment of adaptive attackers.

- Generator perspective: adversarial/security
