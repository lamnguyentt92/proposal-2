# Idea specification (Proposal 1, ACL 2027): Who Is "con"? Dyad-Anchored Person Reference When LLM Agents Write Memories in Vietnamese

**Status (2026-11-20): CONDITIONAL GO — pilot gate first. No data collected, no experiment run, no result exists.**
**Lineage:** GPT-6 draft SCOPE-INTERVENTIONS v5 → IDEA_L1 → L1R (after the novelty attack) → L1S (after the adversarial review) → this specification (after the kill argument and the novelty drift scan).
**Target:** ACL 2027 via ACL Rolling Review — area "Discourse and Pragmatics" (alternative: "Multilingualism and Cross-Lingual NLP"); eligible for the Special Theme track. Simulated-referee outlook (judgement, same-family, provisional): Findings most likely, main track reachable only if the pilot supports C1 and C3.
**Authoring note:** this is an AI-assisted planning document. ACL/ARR requires AI use to be declared in the Responsible NLP checklist; do not paste this text into the manuscript.

## 1. Problem and motivation (with evidence)

A memory writer converts dialogue into context-free third-person records, so it must decide whom each proposition is about. English hides the step because person is lexical. In Vietnamese, kin terms (con, em, anh, chị, cháu…) serve as first-, second- and third-person forms, and inside a report they are anchored to the dyad of the *reported* speech event; the possessor of a bare kin noun is also unexpressed ("Lan bảo mẹ ốm": whose mother?).

Evidence that this is unaddressed:
- Every memory-write error study found (2025–Nov 2026) is English, Chinese–English or Russian and varies English operators: FACTWASH (arXiv:2608.03372), LAPSE (arXiv:2609.36457), AuthMem-Bench (arXiv:2608.01679), Manufactured Confidence (arXiv:2606.29279), AgentMemGate (arXiv:2610.07707), DerivAudit (arXiv:2609.36130), HaluMem (arXiv:2511.03506). None has person anchoring.
- Open-source writers are English-designed: Mem0's extraction prompt tells the writer to replace pronouns with names or "User"; Graphiti's summary prompt tells it to state facts directly without reporting verbs; Graphiti's fuzzy name normalisation keeps only `[a-z0-9' ]` (public in getzep/graphiti PRs #1357 and #1850, which describe a missed fast path — the false-merge consequence for Vietnamese names is unreported).
- Two independent prior-art hunts, one referee and one drift scan found no memory benchmark with kin-term or dyad items, no Vietnamese memory-write resource, and no empirical source on how Vietnamese users address an assistant.
- Agents/tool-use titles at ACL rose from 142 to 366 in a year while multilingual/low-resource titles stayed flat (54 → 52; third-party title classification), and ACL 2027's special theme names lower-resource languages.

## 2. Key insight

Writing a third-person record from Vietnamese requires **dyad-anchored resolution of relational person terms**: a kin term must be mapped to a person through the dyad (and possessor) of the speech event it belongs to. A memory system turns this from a comprehension difficulty into a *persistent, compounding* error in three memory-specific ways:

1. **The record format forces a commitment.** A standalone record or graph edge has no slot for "unresolved"; a reader answering a question can hedge, a writer cannot.
2. **Consolidation conflates anchors.** Deduplicating entity mentions by surface form merges "mẹ" (the user's mother) with "mẹ" (Lan's mother), and — with ASCII-only normalisation — distinct names that differ in a diacritic.
3. **The surface form is discarded.** After the write, the kin term and its dyad are gone, so the error cannot be repaired at read time and propagates to later sessions.

These predict where prompt localisation helps (the resolution step) and where it cannot (schema and consolidation) — knowledge a memory designer does not get from an English benchmark or from a comprehension probe.

## 3. Scope

- **Setting:** text dialogue between one user and an assistant with a long-term memory writer; fictional personas; Vietnamese with English and explicit-name Vietnamese controls.
- **Systems:** open-source memory frameworks with inspectable writes — Mem0 OSS (10-message extraction context) and Graphiti (3-episode context), LangMem with a fixed caller-supplied context; extractor-only conditions. Versions and commits pinned.
- **Assumptions (each stated in the paper):** A1 gold is a distribution over readings from native raters, not a single label; A2 elicited conversations approximate, but are not, spontaneous use; A3 conclusions concern the tested framework versions and backbones.
- **Out of scope:** consent/permission ledgers; hedging and single-operator scope in English (covered by the 2026 cluster); attacks; legal compliance; any claim about real users' private data.

## 4. Contributions

1. **Study 0 (first measurement):** how Vietnamese speakers refer to themselves, the assistant and third parties when talking to an assistant; frequency of kin terms inside reports and of reported dyads that differ from the user–assistant dyad. → C0
2. **Resource:** a natively authored Vietnamese memory-write benchmark with span-anchored frames and graded gold (rater reading distributions with "cannot tell"), natural + diagnostic layers, matched explicit-name and English controls. → C1, C2
3. **Mechanism analysis at three levels:** resolution step (information-matched), record format (write vs comprehension), store (consolidation and later-session consequences). → C1–C3
4. **Design implications tested, not asserted:** localised dyad instruction, a record schema with anchored relational references and an "unresolved" slot, anchor-aware and diacritic-safe deduplication — which error component each removes. → C3, C4

## 5. Claims and how each will be established

| ID | Claim (exact scope) | Evidence type | Success criterion fixed in advance | Refuting result |
|---|---|---|---|---|
| C0 | In elicited Vietnamese user–assistant conversations about family/work, kin terms inside reports are not marginal | Measurement (Study 0) | Rate with interval reported; threshold fixed now: ≥ 5% of turns that mention a third party | Rate below threshold → K3 |
| C1 | **Format gap.** Same backbone, same input: person-assignment error in written memory records exceeds the error of a direct comprehension probe ("who does *con* refer to?"), and this gap is larger on kin-term items than on explicit-name and English controls | Experiment | Item-level mixed model; gap difference with family-clustered 95% CI excluding 0 | Gap on kin-term items not larger than on controls |
| C2 | **Divergence from native readers.** With identical input, writers put more probability mass on readings chosen by < 10% of raters than raters do among themselves; on items where ≥ 50% of raters say "cannot tell", framework-native writers still file the fact under one person in > 50% of cases | Experiment + human distribution | Divergence above rater-to-rater divergence for framework-native writers and for the strongest extractor | Strongest extractor within rater-to-rater divergence (the restriction to framework-native writers is then a secondary result only) |
| C3 | **Store-level conflation is not fixed by prompt localisation.** In end-to-end runs, the rate at which distinct persons are merged or a fact is stored under the wrong person is higher for kin-term dialogues than for controls; a Vietnamese dyad-resolution instruction lowers record-level errors but leaves consolidation-level conflation, which the schema/dedup changes remove | Experiment (ablation over three interventions) | Each intervention's effect on each error component with CIs | The one-line prompt patch removes both components |
| C4 | **The English pivot relocates errors.** Document-level translate-then-extract changes the error mix (fewer unresolved kin terms, more wrong-person assignments) without lowering the total below direct Vietnamese extraction | Experiment | Total wrong-or-unresolved rate, paired by item | Translation closes the gap to controls |
| C5 | **Persistence (supporting claim, not a headline).** A wrong-person record produces wrong-person answers in a later session at a higher rate than the full-dialogue reader does, and replacing the native record by the oracle record removes the difference | Experiment (native record vs oracle record vs full-dialogue reader, later question fixed) | Paired difference with CI | No difference between native and oracle record → the write error has no downstream consequence in this harness |

Commitments added after the atomised kill argument (`06_REDTEAM/KILL_ATOMS_P1.md`):
- **C1 is an extraction-format effect unless shown otherwise.** A non-memory condition (one-shot third-person summary of the same turn) is run beside the memory writers; what the store adds beyond a summary is read from C3 and C5 only.
- **Difficulty-matched control.** Besides explicit-name and English controls, C1 and C2 use non-kin items of comparable probe error (ambiguous third-person reference and nested reports with names). C1 is also reported conditional on the same backbone answering the comprehension probe correctly. Model link (logit) and a ceiling check are fixed before collection.
- **C1 and C2 are reported with the Vietnamese dyad instruction applied** as well as without it, on at least three backbones named before the pilot (two commercial, one local).
- **C2 fallback is secondary.** If the strongest extractor is within rater-to-rater divergence, the restriction of C2 to framework-native writers is reported as a secondary result and cannot be the headline.
- **C3, added outcome.** If the dyad instruction does not lower record-level error either, the failure is attributed to the backbone and the paper concedes the comprehension framing for that component.
- **C4 consequence.** If translation closes the gap, C4 is dropped as a claim and translation is reported as a mitigation.
- **Thresholds fixed now, before any data:** C0 threshold = 5% of turns that mention a third party; "above controls" = lower bound of the 95% CI of the difference above 0 and a point estimate of at least 5 percentage points.

The silent-commitment *phenomenon* (C2, second half) is not claimed as new: AmbiCoref (2023.findings-eacl.75), Correct-Detect (2025.emnlp-main.1527) and "It Depends" (2025.uncertainlp-main.20) show it for English coreference. What is claimed is its measurement in memory writing with a retention cost.

## 6. Positioning: closest works and delta

| Work | What it does | Delta |
|---|---|---|
| DIAL-SUMMER, arXiv:2602.08149 | Error taxonomy for summaries of human–assistant dialogue; names first/second → third-person conversion errors (speaker misattribution, viewpoint distortion in 20.8% of summaries) | English only, speakers are "Human"/"Assistant", no third parties inside reports, categorical labels, summaries not memory stores. We claim only the part English cannot show |
| AmbiCoref (2023.findings-eacl.75); Correct-Detect (2025.emnlp-main.1527) | Ambiguous-pronoun minimal pairs with human uncertainty; disambiguate-vs-detect trade-off | English third-person pronouns, no kin terms, no dyad, no records. Design ancestors of the diagnostic layer |
| Vietnamese person coreference, arXiv:2504.19606 | 266 first-person news narratives, GPT-3.5/4 scored on gold mentions | No dialogue, no report/dyad analysis, no memory. Used as a sanity-check set |
| WMT 2026, 2026.wmt-main.16 | EN–VI translation judged with dyadic profiles and role reversal | Generation-side, 30 items, no person resolution. Protocol precedent; motivates C4 |
| Chinese zero pronouns arXiv:2605.31056; Turkish indexical shift arXiv:2406.05569 | Person reference under report, comprehension/translation | Not memory; C1 (format gap) is the test that separates us from a comprehension probe |
| FACTWASH, LAPSE, AuthMem-Bench, Manufactured Confidence, AgentMemGate, "Whose Memory Is It?" (arXiv:2610.09008), DerivAudit, HaluMem, MemAlign/ConMem (arXiv:2610.33432), PASB (arXiv:2607.10526), TimlMemBench (2026.findings-emnlp.507) | English/Chinese memory-write errors by stance, hedge, source, aspect | None tests person anchoring. Their framing ("a write drops who said it") is cited, not claimed |
| "Same Conversation, Different Languages" (OpenReview iJZKvQGoDj); MemBubble arXiv:2610.25127 | Multilingual memory | No Vietnamese, no kin-term reference |
| Decontextualization: Choi et al. arXiv:2102.05169; abstention variant arXiv:2301.09044 | Make a sentence stand alone | English; supplies the strongest baseline |
| Hlava Cor, arXiv:2606.25383 | Distributional coreference gold (Czech) | Precedent for graded gold; not memory |

Verification levels for each item are recorded in `05_NOVELTY/`. Novelty verdicts: predecessor L1 — *incremental* (two hunters); redesigned core — *novel* (drift scan). All reviews are same-family (provisional); see §13.

## 7. Evaluation plan

**Research questions.** RQ1 Does the construction occur in user–assistant talk? RQ2 With identical input, do writers resolve relational person terms as native speakers do? RQ3 Does writing cost accuracy beyond comprehension? RQ4 What does consolidation add, and which design change removes which error?

**Data.**
- *Study 0:* native speakers from more than one region converse with an assistant on scripted open scenarios with fictional personas; consent, compensation, ethics-exemption determination.
- *Natural layer:* ~600–800 elicited turns with span-anchored frames ⟨about-whom, possessor/anchor, source chain, commitment, anchor span⟩, two trained native annotators + third-person adjudication.
- *Diagnostic layer:* ~300 authored families × 2–4 variants: reported-dyad anchoring; self- vs other-reference of the reported speaker; bare kin noun with ambiguous possessor; null subject under *bảo/nói/dặn*; frame-flip pairs; names differing in a diacritic.
- *Controls:* explicit-name Vietnamese; English counterparts validated by a native English speaker.
- *Graded gold:* ≥ 8 native raters per diagnostic item, shown exactly the context a writer receives, "cannot tell" allowed.

**Conditions.** (i) comprehension probe; (ii) single extraction call with each framework's logged context; (iii) end-to-end multi-session runs; (iv) later-session question with native vs oracle record (consequence measure).

**Baselines, strongest first.** (1) contextualise-then-extract with abstention on a frontier reasoning model, given exactly each framework's context; (2) structured extractor with an explicit Vietnamese dyad-resolution instruction; (3) document-level translate-then-extract; (4) hedge-preserving prompt of Manufactured Confidence, verbatim; (5) framework-native writers; (6) full-dialogue reader. Interventions for C3: localised prompt; schema with anchored relational reference + unresolved slot; anchor-aware, diacritic-safe dedup.

**Metrics.** Three-way person score (correct / wrong / kin term left unresolved); error types (kin-noun literalisation, dyad capture, possessor error, silent commitment); licensed-fact retention; divergence from rater distribution; store-level person-merge rate; later-answer wrong-person rate.

**Statistics.** Unit = item nested in family; mixed models with family and rater random effects; family-clustered bootstrap CIs; agreement per field (κ/α; MASI-based α for admissible sets; unitizing α for spans); multiplicity control across C1–C4; sample sizes fixed from pilot variance before full collection.

**Killer experiment (run first, on the pilot):** 60 diagnostic families + 40 elicited turns; strongest extractor vs 8 raters (C2) and write-vs-comprehension (C1); one end-to-end run per framework with and without the localised prompt (C3).

## 8. Theory plan

No theorem. A small explicit model is required by the journal referee and helps the conference paper: a record is licensed iff every relational person term is resolved to an entity through ⟨anchor event, dyad, possessor⟩; define the three error types as failures of that mapping. Boundary cases to state: stranger dyads (tôi/mình–bạn) where no self/addressee flip can arise; operator-fixed assistant personas; regional variants.

## 9. Artifact plan

Benchmark (frames, rater distributions, annotation manual, disagreement cases), scoring scripts, logged prompts/contexts per framework version, intervention patches. Licences: data CC BY 4.0; code Apache-2.0/MIT-compatible with the frameworks. No personal data: fictional personas only. Report framework defects (e.g. Vietnamese false merges) upstream before publication.

## 10. Risks, mitigations, pivot and kill criteria

| Risk | Mitigation |
|---|---|
| Frontier extractors match native raters | Pilot gate; C1 and C3 must then carry the paper, otherwise K1 applies |
| Phenomenon rare in elicited talk | Study 0 first; threshold fixed in advance |
| Low agreement on perspective items | Graded gold instead of filtering; report per-field agreement |
| Vietnamese readings in this document are unverified | Every example confirmed by native speakers before use; regional raters |
| One language | Second kin-term/honorific language in the journal version |
| Scoop (memory-write benchmarks appear monthly) | The Vietnamese core needs native authoring; re-run the novelty scan before submission |

**Kill criteria (no repositioning; thresholds as fixed in §5):**
- **K1 — memory does no work.** On the pilot, the format gap on kin-term items is not above controls (C1 null) **and** end-to-end person conflation is not above controls (C3 null). The memory paper stops, whatever C2 shows: what would remain is a single-language comprehension probe, which is a different and smaller paper and not this proposal.
- **K2 — the fix is one line.** The localised dyad instruction removes both record-level and consolidation-level error. The paper stops; the instruction is contributed upstream to the frameworks.
- **K3 — it does not occur.** Study 0 rate below 5% of turns that mention a third party. No main-track resource paper and no claim of practical relevance; the diagnostic items may be released as data without a paper claim.
- Pilot decisions use at least three end-to-end runs per framework and condition.

## 11. Resources and timeline

Available: commercial APIs; 1–2 GPUs (local 27B-class model, to be validated on the pilot); two trained native annotators. To obtain: third native speaker for adjudication; rater pool and Study 0 participants; native-English validator. API cost: low thousands of USD if frontier models are kept for extractor baselines (auditor's estimate, to be re-measured).

Milestones: pilot gate (K1–K3) → Study 0 + annotation manual → full collection → experiments → writing → two internal review rounds. First cycle of interest: ARR 4 Jan 2027 (ACL 2027); if the pilot gate or collection is not complete, the next ARR cycles (EMNLP 2027) — timing does not change the idea.

## 12. Conference core vs journal extension

- **Conference core (8 pages):** Study 0, benchmark with graded gold, C1–C4, Graphiti diacritics check.
- **Journal extension (Computational Linguistics accepts substantially extended conference papers; TACL does not):** explicit anchor/dyad model, full annotation manual and disagreement analysis, a second kin-term or honorific language plus a pro-drop contrast language, VI–EN code-switching, larger downstream study. New title and abstract; cite the conference paper.

## 13. Red-team issues that Process 2 must address

Atomised kill argument (`06_REDTEAM/KILL_ATOMS_P1.md`; status before the commitments in §5 and §10 were added: 1 answered in design, 4 partly answered, 1 unresolved). Nothing has been run, so "answered" means the design holds a test that can prove the objection right.

| # | Issue | Status after this revision | What closes it |
|---|---|---|---|
| 1 | Memory does no explanatory work | Tests exist (C1 with non-memory condition, C3, C5); K1 stops the paper if C1 and C3 are both null | Pilot results |
| 2 | Kin-term items are simply harder | Difficulty-matched control and conditional analysis committed | Gap survives against matched controls |
| 3 | If the localised prompt works, the paper is a prompt patch | K2 | C3 result on ≥ 3 runs per framework |
| 4 | If it fails, it is a comprehension result in a wrapper | Comprehension probe in the design; C1/C2 reported with the instruction applied; concession rule in §5 | Record error not tracking probe error |
| 5 | Downstream read-out is not new | Demoted to supporting claim C5 with a refuting result | — |
| 6 | No outcome counts against the submission | K1–K3 rewritten as stops; thresholds fixed in §5 | — |

Further standing issues:
7. **Not yet scanned for novelty as now specified:** the write-vs-comprehension gap (C1) and entity conflation of relational terms in memory stores (C3). The drift scan covered the L1S claims. arXiv:2610.10265 (same-name entity confusion in memory; listed by a hunter, not examined) must be read against C3.
8. **Scorer validity:** an LLM scorer for Vietnamese free-text records must be validated on ~300 human-scored records before use.
9. **Controls a referee asked for:** a Chinese null-subject control; dialect and no-diacritic input conditions.
10. **Naturalness:** Study 0 is the only evidence; elicitation is not spontaneous use.
11. **Vietnamese readings in this document are unverified** until confirmed by native speakers.
12. **Process gaps:** the devil's-advocate review of the L1R version did not run (launch failure); its role was covered by the referee review, the kill argument and its atomisation. All reviews are same-family (provisional): run `XMODEL_NOVELTY_P1_PROMPT.md` and `XMODEL_REDTEAM_P1_PROMPT.md` in another model family, or record a waiver.
13. **Search limits:** Google Scholar, Semantic Scholar, non-public ARR submissions and Vietnamese-language venues were not searchable; re-scan before submission.
