# 07_SELECTION — Independent referee scores for the four finalists

Scored 2026-11-20 by one sceptical referee (ACL / ICML area-chair perspective), independently of any other scorer.

**Basis and limits**
- Judged from the files only (`01_VENUES.md`, the finalist specifications/cards, `05_NOVELTY/`, `06_REDTEAM/`). No web search, no experiment, no code run.
- Scores use half-point steps on the 1–5 scale. Totals are weighted sums with the fixed rubric weights.
- Probability bands and predicted review outcomes are **judgements, not measurements**. They are conditional on competent execution of the plan as written, not on favourable results.
- This is a same-model-family review, so it shares the blind spots of the earlier hunters and reviewers. Treat it as provisional until a cross-family check is done.
- The evidence is uneven. P1 and P2 went through two prior-art hunts, a drift scan, adversarial reviews and a kill argument, and were then revised. V1R had one combined review. R1 had two prior-art hunts but **no adversarial review, no feasibility check and no revision**; its merged card is a stub pointing to two unreconciled cards. R1's scores therefore carry the widest uncertainty.
- Technical feasibility ignores staffing, workload and deadlines, as the rubric requires.

## 1. Score table

| Criterion | Weight | P1 (ACL) | P2 (ICML) | V1R (ACL) | R1 (ICML) |
|---|---|---|---|---|---|
| Novelty (verified delta to closest work) | 0.35 | 3.5 | 3.0 | 3.0 | 2.5 |
| Venue fit and bar | 0.25 | 4.0 | 3.0 | 3.0 | 3.5 |
| Significance to the venue's community | 0.15 | 3.0 | 3.0 | 2.0 | 3.5 |
| Evaluation clarity | 0.10 | 3.5 | 4.0 | 2.5 | 3.5 |
| Extensibility to the journal | 0.05 | 4.0 | 3.5 | 3.0 | 4.0 |
| Technical feasibility | 0.05 | 4.0 | 3.5 | 3.0 | 3.0 |
| Ethics / legal / disclosure risk (5 = low risk) | 0.05 | 4.0 | 4.5 | 3.0 | 3.5 |
| **Weighted total** | 1.00 | **3.625** | **3.225** | **2.800** | **3.150** |

**Ranking:** P1 (3.63) > P2 (3.23) ≈ R1 (3.15) > V1R (2.80).

**Robustness.** A half-point change in one novelty score moves a total by 0.175.
- P1 first and V1R last survive any single half-point change.
- P2 versus R1 does **not**: the 0.075 gap is inside my scoring noise. P2 is ahead because it is a revised, red-teamed specification with pre-registered tests; R1 has the better natural fit to ICML and the larger upside, but the weaker verified delta and no stress test.

| | Main-track band (judgement) | Where in the band |
|---|---|---|
| P1, ACL 2027 | 10–25% | Top of the band. Main or Findings together: 25–40% or better. |
| P2, ICML 2027 | 10–25% | Lower-middle. |
| R1, ICML 2027 | 10–25% | Lower edge, and only after the card is repositioned (see notes). |
| V1R, ACL 2027 | < 10% | Findings is the realistic ceiling. |

## 2. Per-finalist notes

### P1 — "Who Is *con*?" Dyad-anchored person reference in Vietnamese memory writing (ACL 2027)

**Why these scores**
- *Novelty 3.5.* Two hunts and the drift scan found no memory benchmark with kin-term or dyad items and no Vietnamese memory-write resource. The delta to DIAL-SUMMER, AmbiCoref, Turkish indexical shift and the 2026 memory-write cluster is specific and stated. Held below 4 because:
  - the genre is established (LAPSE: minimal pairs on framework-native writers; AuthMem-Bench: paired promotion/retention metrics);
  - the silent-commitment phenomenon is known in English coreference, which the specification concedes;
  - the two claims that now carry the memory-specific story, C1 (format gap) and C3 (store-level conflation), were added **after** the last drift scan and have not been checked against prior art.
- *Venue fit 4.* Discourse and Pragmatics or LLM Agents for NLP; natively authored lower-resource data matches ACL's stated interests. Planned size (about 600–800 natural turns, about 300 families × 2–4 variants, ≥ 8 raters) sits at the lower end of the calibration range in `01_VENUES.md`.
- *Significance 3.* Useful to designers of memory systems for kin-term languages; a single language and an elicited corpus limit the reach.
- *Evaluation 3.5.* Claims have pre-fixed criteria and refuting results, the strongest baseline is named (contextualise-then-extract with abstention on a frontier model, given the framework's own context), and the pilot gate can fail. Deductions:
  - the C0 threshold (≥ 5% of third-party turns) is self-chosen, and family/work scenarios can inflate it;
  - C1 compares two response formats (free-text record against a direct probe), so part of any gap can be a scoring artefact; no validated scorer for Vietnamese records is specified, although the feasibility review asked for one;
  - the second half of C3 ("the schema/dedup changes remove conflation") is close to true by construction;
  - the kill rule needs K1 **and** K2 to fire, which leaves wide room to continue.
- *Feasibility 4, ethics 4.* Frameworks run locally and are pinned; native annotators exist; fictional personas. Study 0 is human-subjects work and needs a documented exemption or approval.

**How far the specification answers the earlier reviews**
- Answered: the tautology charge (information-matched raters, logged contexts), categorical gold (rater distributions with "cannot tell"), "two papers in one" (English twin layer dropped), missing baselines, the harm measure (later-session wrong-person answers), Letta and LangMem window problems, the Graphiti wording.
- Partly answered: naturalness (Study 0 is elicited, not observed); the translation claim (C4 is now narrower but still two-part); "every refutation becomes a repositioning" (K3 still converts to a short paper, and C2's refutation still narrows to native writers).
- Not answered: a control that separates "kin-term person shift" from "anaphora across a context boundary" (a Chinese null-subject set or an English out-of-window pronoun set); a second kin-term language is deferred to the journal.
- The kill argument ("memory does no explanatory work") is answered in design only. It stays open until C1 and C3 are shown on the pilot.

**Predicted review outcome**
- *Experiments as hoped* (Study 0 above threshold; format gap larger on kin-term items; strongest extractor diverges from raters; the prompt patch leaves store-level conflation): ARR overall around 3–3.5 with one reviewer asking "why one language" and one asking "is this a coreference paper". Findings is the most likely result; main track is reachable if a reviewer champions the store-level result.
- *Experiments negative* (frontier extractor within rater-to-rater divergence, one-line Vietnamese instruction closes the gap): the kill criteria apply. If submitted anyway, reject from main; at best a short or Findings paper recording that English-designed frameworks need a localised prompt.

**Single weakest point.** Everything that makes this a memory paper rather than a one-language deixis probe rests on C1 and C3, which are the newest, least scrutinised claims. If a one-line Vietnamese dyad instruction removes both error components, the contribution reduces to a prompt patch; if it removes neither, a referee can assign the failure to the backbone's Vietnamese comprehension.

**Main-track probability band (judgement):** 10–25%, top of the band.

### P2 — "Are the Passes Real?" State-level audit of mobile-agent verdicts and a mutation-transfer test (ICML 2027)

**Why these scores**
- *Novelty 3.* Both hunters and the drift scan say incremental with one open core: no source relates verifier mutation scores to audited real agent failures. Everything around it is published or under review (MobileJudgeBench and AgentRewardBench for both-direction verdict error; τ-bench, AppWorld and OpenReview kuSAqpyELw for gold-state and replay diffs; three records for ordering changes after grader repair). The mode-conditional form of C2 was written after the drift scan and has not been re-scanned. Scoop risk is high.
- *Venue fit 3.* ICML 2027 has an Evaluation area and matching contribution types, but the project's own simulated referee scored fit 3/5 and I agree. "Two benchmark families" is two Android suites; the API-world transfer check is "if resources allow". An ICML reviewer will ask what holds beyond Android.
- *Significance 3.* Matters to mobile-agent benchmark users and to the 2026 verifier-audit wave. The most likely C1 outcome, on existing evidence, is "wrong passes are rare, wrong fails are not", which is a modest headline.
- *Evaluation 4.* The best-specified plan of the four: pre-registered equivalence test with a margin, a power statement, strong baselines (blind human audit, LLM state-reading verifier), and two early experiments that can stop the project (mask false alarms; sparse cells). Held below 4.5 because of the construct problem under "weakest point", and because C3 has no refuting result.
- *Feasibility 3.5.* All parts are obtainable and the researcher's Android-testing background fits. The emulator testbed is unconfirmed, the mask may not reach the false-alarm target on agent-like routes, and AndroidWorld's 116 templates cap what clustered intervals can show.
- *Ethics 4.5.* Emulator-only, synthetic data, upstream disclosure planned.

**How far the specification answers the earlier reviews**
- Answered: composed runs (dropped; only unmodified runs), the dominating gold-differential baseline (now the instrument), inconsistent thresholds, the per-template correlation that the kill argument called vacuous (replaced by the test that argument itself proposed), the missing sample of FAIL verdicts.
- Partly answered: mask validity (measured on held-out scripted routes, not on adjudicated-clean agent or human runs); the audit (flag-stratified sample rather than a census, with no spike-ins to measure annotator recall); "wrong pass" against the benchmark's own task text (goal-not-achieved and unrequested side effect are still reported together).
- Not answered: the determinism objection to seeded-fault calibration; venue fit; the three-family generality the referee asked for.

**Predicted review outcome**
- *Experiments as hoped* (mask works; a non-trivial state-only share; C2 cells populated and a clear direction): passes the area-chair first round; final scores borderline to weak accept. Acceptance depends on whether reviewers credit C2 as a general methodological result. It would be received more comfortably at a datasets-and-evaluations track or a software-testing venue.
- *Experiments negative* (state-only share near zero, about 1% wrong passes, sparse or trivially 0/1 cells): K2 withdraws the ICML plan. If submitted as a negative result, weak reject: "one benchmark family's verdicts are mostly fine" is not of general interest.

**Single weakest point.** C2's construct validity. The checkers are deterministic, so within a fine cell a seeded state and a real failure of the same kind receive the same verdict by construction. Any difference in miss rates at checker-family level then reflects how the authors mixed seeds and how coarse the failure-mode taxonomy is, not a property of mutation audits. The specification acknowledges 0/1 cells and moves the comparison to family level, which is exactly where the result becomes a function of the seeding recipe. The "holds" branch also still needs failure-mode labels for each new agent, which weakens the claimed saving.

**Main-track probability band (judgement):** 10–25%, lower-middle.

### V1R — Vietnamese person reference and force marking as a test of role confusion in indirect prompt injection (ACL 2027)

**Why these scores**
- *Novelty 3.* The instrument (dyad and force minimal pairs inside injected content, with a human baseline) was not found. The thesis it tests, the language-congruence effect, the identity-mismatch asymmetry and the attribution probe are all published. The parent paper already has a pronoun ablation row with an effect of about 3 points.
- *Venue fit 3.* The topic suits ACL, but the project's own review predicts ARR 2.5–3 and I see no reason to move it.
- *Significance 2.* An attacker avoids the incongruent condition at no cost: a directive with no person reference matches every frame. A positive result is a few points on a spoofable cue; a null says little.
- *Evaluation 2.5.* C2 has no predicted direction, C4 is true by construction, "exceeds the English control" is unspecified, and the stated item counts cannot detect an effect of the expected size. No pilot gate is on the card; the review supplies one.
- *Feasibility 3.* Buildable, but frontier models sit at the floor and weak models near the ceiling, so the usable measurement range is narrow.
- *Ethics 3.* Sandbox and harmless goals are planned. Remaining risks: a validated set of Vietnamese injection phrasings, a register-matched contrast that reduces to a speaker-gender flip, and a human-subjects study.

**Predicted review outcome**
- *Experiments as hoped:* Findings if the crossed byte-identical design and a real human study are added; main track unlikely.
- *Experiments negative:* reject; a null on one feature in one language is workshop material.

**Single weakest point.** The quantity measured is not the one that matters for security. Under any realistic threat model the attacker sends the best variant, which makes the dyad factor vanish; after register matching the contrast narrows to a gender flip with an expected effect near 3 points.

**Main-track probability band (judgement):** < 10%.

### R1 — Red teaming as unseen-species sampling (ICML 2027)

**Why these scores**
- *Novelty 2.5.* Both hunters say incremental, and their findings contradict the card's "new method (+ statistical guarantee)" line:
  - missing mass for AI-agent testing with anytime-valid theory is arXiv:2611.15835 (nine days old; desk-rejected at ICLR 2027, so a likely ICML 2027 competitor);
  - rarefaction to compare jailbreak attackers is CoFiBreak (arXiv:2610.40926);
  - the overlap lower bound under positive dependence is arXiv:2611.12705 and classical capture–recapture;
  - the overlap insight was proposed for penetration tests by Geer in 2015; the framing is STADS (2018).
  What is unclaimed is the application to red-team logs and the held-out-attacker validation. The card has not been revised to say so.
- *Venue fit 3.5.* The best natural fit to ICML's Evaluation area of the four, and the problem (ASR@k is not comparable across budgets) is recognised. The bar is the difficulty: without new theory the paper is a validation study of textbook estimators, set beside a competitor that has theory. `00_CONSTRAINTS.md` says no theory specialist should be assumed.
- *Significance 3.5.* A budget-independent statement of what a campaign left undiscovered would be used by defence papers. Discounted because the bound is relative to the attacker pool, and the evidence the hunters found on few, uneven finders suggests it may be valid but too loose with about five attacker families.
- *Evaluation 3.5.* Decisive experiments exist and can fail (freeze estimates, then run a larger pooled campaign with a held-out attacker family). Deductions: the two source cards carry two claim sets and three species definitions that have not been merged; the validity test (bound not exceeded later) is passed by any sufficiently conservative bound, so informativeness carries the weight; the "truth" is itself only a larger lower bound.
- *Feasibility 3.* Not reviewed. Attacker code availability is taken from abstracts; API spend for replicate campaigns is an open quantity; near-exhaustive campaigns on open-weight targets are plausible on 1–2 GPUs.
- *Ethics 3.5.* Existing attacks in sandboxes, no human subjects in the core; running attack campaigns against commercial APIs needs a terms-of-use check.

**Predicted review outcome**
- *Experiments as hoped* (bound valid and predictive on held-out attackers; rankings by coverage differ from ASR@k): borderline to weak accept if framed as a validation study with the prior art cited in full; reviewers who know STADS or arXiv:2611.15835 will call it a port.
- *Experiments negative* (bound loose, or invalid under learning attackers): a Negative Results submission is possible only if the reason is established; otherwise weak reject.

**Single weakest point.** The method is borrowed whole, and the one estimand that is new (breakable fraction from campaign overlap) is defined relative to the attacker pool, so it cannot support the claim readers want (how much risk remains against an attacker not in the pool). The idea has also had no adversarial review, so further weaknesses are likely undiscovered.

**Main-track probability band (judgement):** 10–25%, lower edge, conditional on repositioning.

## 3. Summary for the selector

- **ACL slot:** P1 is clearly ahead of V1R (3.63 against 2.80). The two share a linguistic resource; V1R adds little that P1 does not already offer.
- **ICML slot:** P2 (3.23) and R1 (3.15) are not separable at this resolution. P2 is the safer, better-specified study with a lower ceiling and a venue-fit problem. R1 fits the venue better and has more upside but has an unrevised card, thinner verified novelty and a direct theory-backed competitor. An adversarial review and a feasibility check of R1 would be needed before the two can be compared on equal evidence.
- Checks that would most change these scores:
  1. P1: a novelty re-scan of C1 and C3, and the pilot result on the one-line prompt patch.
  2. P2: the agent-free mask pilot, and a written answer to the seeding-recipe objection to C2.
  3. R1: a revised card that drops the "new method/guarantee" claim, plus a pilot on whether the bound is informative with five attacker families.
