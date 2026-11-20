# 07_SELECTION — Selector scores (independent), 2026-11-20

**Role:** selector with no stake in any idea. **Inputs read in full:** `00_CONSTRAINTS.md`, `01_VENUES.md` (plus the calibration section of `01_VENUES_notes.md`), both `09_IDEA_SPEC_*` files, `IDEA_V1R/V1`, `IDEA_R1/S3/M1`, all ten `05_NOVELTY/` reports and all eight `06_REDTEAM/` files. No web search; every judgement below rests on those files.

**Status of this document:** a judgement on plans. No finalist has data, a pilot or a running artefact. Every review used here is same-family (provisional); no cross-family review exists yet.

## 1. How I scored

- Scale 1–5 in half-point steps. Anchors: **4** = clears the A* main-track bar on that criterion as the documents stand; **3** = borderline (Findings / weak-reject-to-borderline); **2** = below the bar; **5** = an expert referee would grant it without argument.
- "Clears an A* bar" for the overall verdict means: novelty ≥ 4 **and** venue ≥ 4 **and** no gate at *fail* **and** weighted total ≥ 4.0.
- Novelty is scored on the *verified* delta: what a novelty report actually checked for the version being judged.
- P1 and P2 are judged on the current specifications. Their reviews were written against L1R / F1R; section 5 records how far each specification answers them.
- Feasibility covers buildability and measurability only. Deadlines, staffing and workload were not used anywhere.

## 2. Score table

| Criterion | Weight | P1 (ACL) | P2 (ICML) | V1R (ACL) | R1 (ICML) |
|---|---|---|---|---|---|
| Novelty (verified delta) | 0.35 | 3.5 | 3.0 | 3.0 | 2.5 |
| Venue fit and bar | 0.25 | 3.5 | 2.5 | 3.0 | 3.0 |
| Significance to the community | 0.15 | 3.0 | 3.0 | 2.0 | 3.5 |
| Evaluation clarity | 0.10 | 3.5 | 4.0 | 2.5 | 3.0 |
| Extensibility to the journal | 0.05 | 4.0 | 3.5 | 3.0 | 3.5 |
| Technical feasibility | 0.05 | 4.0 | 3.0 | 3.5 | 3.0 |
| Ethics / legal / disclosure (5 = low risk) | 0.05 | 4.0 | 4.5 | 3.0 | 3.5 |
| **Weighted total** | 1.00 | **3.50** | **3.08** (3.075) | **2.83** (2.825) | **2.95** |

One-line basis per cell:

| Criterion | P1 | P2 | V1R | R1 |
|---|---|---|---|---|
| Novelty | Drift scan: core *novel* (kin-term resolution through the reported dyad at write time, not found in any source). But genre, design and silent commitment are precedented, and the two claims that carry the "memory" argument (C1 format gap, C3 store-level conflation) were added after the last scan | Drift scan: *incremental*; only C2 (seeded-vs-real miss rates) is clean; C1 partly anticipated (MobileJudgeBench, AgentRewardBench), C3 a replication, C4 a recombination | Hunters split (novel-narrow / incremental). Instrument unanticipated; thesis, congruence effect and attribution probe all published; parent paper already has a pronoun ablation (61 → 58%) | Both hunters *incremental*; each pillar has a neighbour from the last four weeks (2611.15835, 2610.40926, 2611.12705) plus STADS and Geer 2015. Card not revised afterwards and still claims a new method with a guarantee |
| Venue | Fit is strong (Discourse/Pragmatics, special theme, benchmark scale inside the calibrated range). Bar: the only referee prediction on record is "Findings ceiling"; main track depends on the pilot | Simulated referee fit 3/5; reads as a single-ecosystem checker audit with software-testing lineage; second benchmark *family* is optional in the spec | Fit 4, predicted ARR 2.5–3 (borderline Findings), card not redesigned after the review | Statistical evaluation method suits ICML's Evaluation area better than P2, but the bar is untested (no referee) and a stronger-theory competitor is likely in the same pool |
| Significance | Concrete audience (memory-framework designers, multilingual NLP). No evidence yet that the construction occurs when Vietnamese users talk to an assistant; one language | Tests an assumption behind ≥ 8 grader-audit papers. Prior evidence points to rare wrong passes (~1.4%); audited agents are not the leaderboard systems | Reviewer: a few points on a cue the attacker controls for free; a null says little | Documented, widely felt problem (ASR@k not comparable; 10.8% of papers state a budget). Risk that the bound is valid but too loose |
| Evaluation | Each claim has a fixed criterion and a refuting result; right strongest baseline; pilot gate. Weak points: the stop rule needs K1 (itself a conjunction) *and* K2; C0 threshold only "proposed"; no scorer-validation step; C1 interaction exposed to ceiling effects | Preregistered equivalence test with power statement, full blind audit as reference, agent-free pilot, single-condition kill criteria. Weak points: family-level miss rates depend on the seeding mix; no spike-ins for auditor recall | C2 has no sign, C4 is true by construction, C1 under-specified; under-powered at planned sizes; no kill criteria; reviewer's killer design not adopted | S3 and M1 each have a decisive held-out experiment and baselines, but two claim sets are unreconciled, species definition is open, and nothing has been red-teamed |
| Extensibility | Computational Linguistics; anchor/dyad model, second kin-term language, pro-drop contrast | JAIR/AIJ; safety, desktop/web, route synthesis. Referee doubts AIJ fit | Second language, probes; thin journal story | Sequential/anytime-valid version, memory and mobile targets |
| Feasibility | Frameworks, baselines and a local 27B model verified from code; nothing run end to end; scorer for free-text records unspecified | KVM host unconfirmed; mask viability unknown; eight screen-state templates are outside any state observer; ≥ 2 scripted routes are hard for several apps | Floor/ceiling problem on frontier models; power needs ≥ 300 natively written scenarios | Attacker code availability unchecked; sparse successes on strong defenders; cost of near-exhaustive campaigns open; no feasibility review |
| Ethics | Human participants (Study 0, raters) need an exemption determination; fictional data; no attacks | Emulator-only, synthetic data, upstream disclosure planned | Natively written injection phrasings; reduces to a gender-flip contrast; human study | Sandbox attack research, permitted by the constraints; API terms for attack traffic unchecked |

**Sensitivity.** P1's lead over P2 (0.43) survives any single half-point change, and survives a simultaneous −0.5 / +0.5 on novelty. P2 vs R1 (0.13) does **not**: one half point on novelty or venue for either reverses it. Treat P2 and R1 as tied on score; they differ in evidence (P2 has three reviews, a kill argument and a drift scan; R1 has none of these).

## 3. Gate table

| Gate | P1 (ACL) | P2 (ICML) | V1R (ACL) | R1 (ICML) |
|---|---|---|---|---|
| G1 venue fit | **Conditional** — fit and scale match calibration, but the spec no longer names the ARR area (L1S named Discourse and Pragmatics) and main track rests on the pilot | **Conditional** — venue, area and type named; fit 3/5; calibrated ICML papers are methods and multi-setting benchmarks, not one-ecosystem audits | **Conditional** — track named, fit good, predicted Findings | **Conditional** — ICML Evaluation named, but S3 targets IJCAI and M1 ICML; no referee calibration |
| G2 novelty | **Conditional** — no anticipation of the dyad core in two hunts and a drift scan; delta written; C1 and C3 as now specified are unscanned | **Conditional** — no anticipation of C2; delta written; the rest is incremental, so the delta's weight sits on one claim | **Conditional** — instrument unanticipated; delta narrow and partly pre-empted by the parent paper's pronoun row | **Conditional** — application unclaimed, but the written delta is out of date and overclaims |
| G3 significance | **Conditional** — community concrete; natural occurrence unmeasured (Study 0 pending, elicited only) | **Conditional** — community concrete; expected headline is "passes are mostly right" | **Fail** — no rational attacker produces the incongruent condition; frequency of a stable dyad unknown | **Pass** — concrete community and a documented measurement problem |
| G4 feasibility | **Pass** — components verified from code and licences; open items are scorer validation and an end-to-end check of the Graphiti merge | **Conditional** — testbed unconfirmed; K1 (mask) undecided; observer cannot see screen-state verdicts | **Conditional** — usable dynamic range only on mid-tier models | **Conditional** — no feasibility review; attacker code and campaign cost unverified |
| G5 falsifiability | **Pass** — refuting result per claim, strongest baseline named, pilot can fail; stop rule is lenient | **Pass** — preregistered test, strong baselines, agent-free gate; seed-mix dependence must be stated | **Fail** as written — two of four claims cannot fail; no kill criteria; strongest baseline (person-less directive) absent | **Conditional** — decisive experiments exist in the component cards, never merged or reviewed |
| G6 integrity | **Pass** — no overlap with the author's other work under review; fictional data; disclosure route clear | **Pass** — no overlap with other work under review; synthetic emulator data; ICML AI Disclosure Statement planned | **Conditional** — shares its linguistic resource and its venue slot with P1; injection data is dual-use | **Conditional** — no content conflict, but the project rule "Stage 6 runs for every finalist" is unmet |
| **Tally** | 3 pass, 3 conditional | 2 pass, 4 conditional | 4 conditional, 2 fail | 1 pass, 5 conditional |

No finalist passes all six gates outright.

## 4. Ranking

**1. P1 — 3.50.** The only finalist whose core a novelty report calls novel, with strong venue fit and a design that now answers most of its review. What holds it at 3.5 is that the novel part is narrow (one language) and that the memory-specific claims meant to defeat the kill argument are unproven and unscanned. Significance has no evidence behind it until Study 0 exists.

**2. P2 — 3.08.** The best-specified evaluation of the four and the lowest ethics risk, with one clean open claim. It ranks second on evidence, not on margin: novelty is incremental by its own drift scan and ICML fit is the weakest venue score in the table.

**3. R1 — 2.95.** The most ICML-shaped problem and the highest significance score, but an unrevised stub: two component cards with different venues and claim sets, a delta the hunters contradicted, and no red-team review. Its score is the least certain of the four and it cannot be selected until Stage 6 has run.

**4. V1R — 2.83.** A clean instrument aimed at a small effect. It fails two gates as written, its reviewer's redesign has not been applied, and it competes with P1 for the same linguistic resource and the same venue.

## 5. How far the current specifications answer the earlier reviews

**P1 vs the L1R reviews and the L1S kill argument**

| Review point | Answered in the spec? |
|---|---|
| Central result true by construction | Yes — information-matched design; raters see exactly the writer's context |
| No evidence the frames occur | In design only — Study 0, threshold to be fixed; still elicited, not observed |
| Categorical gold on graded phenomena | Yes — ≥ 8 raters, "cannot tell", distributional gold; factivity items dropped |
| Two papers in one | Yes — English operator twins removed |
| Strongest baselines | Mostly — contextualise-then-extract with abstention, one-line patch, context-matched translation, English controls. Missing: Chinese null-subject control, dialect / no-diacritic input conditions |
| "Memory does no explanatory work" | In design only — C1 (write vs comprehension) and C3 (consolidation). Both can fail; neither has been checked for prior work |
| "Both outcomes of the localised prompt sink the paper" | Partly — C3 predicts a residue the prompt cannot remove; if the prompt removes both components the paper is a patch |
| Every refutation pre-converted into a repositioning | Partly — "no repositioning" is declared, but C2's refuting result still narrows the claim to native writers, and the stop rule needs three things to fail |
| Three-way outcome and validated scorer | Half — the three-way score is there; scorer validation against humans is not |

**P2 vs the F1R reviews and the F1S kill argument**

| Review point | Answered in the spec? |
|---|---|
| Gold diff dominates the relations | Yes — relations dropped, gold-differential oracle is the instrument |
| Composed runs are not the shipped benchmark | Yes — unmodified runs only |
| Mask learned on one route | Yes — route-diverse mask, agent-free pilot, K1 |
| "C2 is vacuous" (nobody holds it, low correlation built in, no power) | Largely — replaced by the mode-conditional test the kill argument itself called fair, over all real failures, with an equivalence margin. Residual: with deterministic checkers the family-level miss rate is a mixture, so the result depends on the seeded mix |
| Audit validity | Partly — two blind annotators and κ; no spike-ins to measure auditor recall |
| Thresholds inconsistent, under-powered | Mostly — power stated; AndroidWorld alone cannot supply ~1,000 independent passes per agent, so pooling carries the estimate |
| Venue fit 3/5 | Not resolved — acknowledged; the second benchmark family (AppWorld) remains "if resources allow" |
| C3 controls expected by referees | No — random-pass-removal control and held-out check not in the spec |
| LLM verifier baseline | Partly — present, but the published forms the drift scan says it must beat (VeriCUA, IRA) are not named |

## 6. Overall assessment

**No finalist clears an A\* bar as the documents stand.** The best total is 3.50 against a threshold of 4.0, no finalist reaches 4 on novelty or on venue, and none passes all six gates.

**P1 comes closest.** It would clear the bar if all of the following became true:
1. On the pilot, the format gap on kin-term items exceeds the controls (C1), or the strongest extractor falls outside rater-to-rater divergence (C2).
2. In end-to-end runs on pinned Mem0 and Graphiti, person conflation survives the one-line localised prompt (C3). Today the Graphiti merge rests on helper-level arithmetic, not a framework run.
3. Study 0 exceeds a threshold fixed beforehand, in more than one region.
4. A novelty scan covers what was added last — write-vs-comprehension gaps and entity conflation in memory stores (arXiv:2610.10265 on same-name confusion and the Zep dedupe changelog were seen but not examined for this) — and Vietnamese-language venues; plus the cross-family review.
5. Native speakers confirm the example readings, which the spec itself marks as unverified.

With 1–3 in hand I would re-score novelty, venue and significance at 4, which gives a total of 3.95 — at the threshold, not comfortably above it. If 1 and 2 both fail, the kill argument stands and what remains is a single-language comprehension probe.

**P2 does not clear ICML and is unlikely to on design changes alone.** Its ceiling is set by an incremental novelty verdict and a fit of 3/5. It becomes a credible ICML submission only if pilot (a) passes, C2 cells fill on both mobile benchmarks, an API-level family is made mandatory rather than optional, and the transfer result is clear in one direction across families.

**Step-down venues (the author decides):**
- **P2: yes, put the step-down in front of the author now.** The spec's own referee names NeurIPS Evaluations & Datasets as the natural home and ISSTA/ICSE as venues that value the oracle-assessment lineage. I would present these as the expected home and ICML as the stretch, not the reverse.
- **P1: no step-down needed yet.** ARR already yields main or Findings from one submission, and the K3 route (diagnostic short paper) is defined. Revisit after the pilot.
- **R1 and V1R:** not ready to be offered to any venue. R1 needs a revised card and its Stage 6 review; V1R needs the reviewer's byte-identical crossed design and a person-less attack arm.

**For the second slot,** P2 and R1 are tied on score. P2 is the defensible choice today only because it has been attacked and repaired; R1 has not been tested at all. If the author wants a paper with better odds at ICML specifically, the cheaper next step is to revise and red-team R1, not to assume P2 will fit.

## 7. Defects found in the record

- Both specifications cite `KILL_ATOMS_P1/P2.md` and `XMODEL_*_PROMPT.md`; none of these files exists in the ideation folder.
- The P1 specification dropped the ARR area and contribution type that L1S named.
- The P1 novelty verdict ("novel core") was issued for L1S, whose C1–C4 differ from the specification's C0–C4.
- R1 has no revised card (no R1R), no merged claim set and no Stage 6 review, against the constraint that every finalist is reviewed.
