# IDEA_L1R: Whose fact is it? Dyad-anchored person reference and scope composition at memory-write time (Vietnamese–English)

Revision of IDEA_L1 after the Stage 5 novelty attack (one permitted return to Stage 4). Both prior-art reports
(`05_NOVELTY/IDEA_L1_priorart_A.md`, `_B.md`) rated IDEA_L1 **incremental**: the speech-report framing, single-operator
laundering, the minimal-pair genre for memory writers and keep-the-frame records are all published. This card keeps only
what neither hunter found and replaces the key insight. It evolves the GPT-6 draft SCOPE-INTERVENTIONS v5.

- Gap addressed: G1 (primary), G12 (through the English-pivot result).

- Target venue and track: ACL 2027 via ARR — "Discourse and Pragmatics" (first choice) or "Multilingualism and Cross-Lingual NLP"; eligible for the Special Theme (homogenization) through claim C1b. Contribution types: data resource + model analysis.

- Problem (1 paragraph): A memory writer turns dialogue into context-free third-person records ("User is quitting her job"). To do that it must decide the *holder* of every proposition. English makes this look like a solved sub-step because person is lexical (I / you / she). In Vietnamese it is not: kin terms (chị, anh, em, con, cô…) serve as first-, second- and third-person forms, and which person a token denotes is fixed by the speaker–addressee dyad established earlier in the discourse; embedded subjects are freely null and quotation is not obligatorily marked. Memory writers, however, extract turn- or chunk-locally, emit third-person records, and are prompted (and largely trained) in English person categories. The information that decides the holder therefore often lies outside the unit the writer sees. No published memory benchmark can detect the resulting error: every one found is English or Chinese–English/Russian, and all 2026 write-error studies (FACTWASH, LAPSE, AuthMem-Bench, Manufactured Confidence, AgentMemGate) vary one English operator at a time with cue-readable gold.

- Key insight (the non-obvious observation; 2–3 sentences): Holder resolution in Vietnamese is **discourse-state-dependent, not string-dependent**: the same reported sentence has a different gold holder under a different, earlier-established xưng–hô frame, so a *string-identical target turn* yields a minimal pair with opposite gold records. This turns an informal worry ("memory tools are worse in Vietnamese") into a sharp architectural prediction: holder error should be a step function of whether the frame-setting turn falls inside the writer's extraction window, should persist under "cautious" prompts (which can only drop the fact, not re-anchor it) and should not be repaired by translate-to-English-then-extract, because translation must commit to I/you/she before the writer runs. The same logic generalises beyond person: whether the reporting frame may be dropped depends on operator class and scope order, so cue-matched twins with opposite gold decisions separate real composition from cue-keyed caution in both languages.

- Approach (how the insight becomes a method/system/theory):
  1. **Gold frame per scored proposition** (human-annotated): ⟨holder, polarity, condition, source chain, anchor span, user-commitment ∈ {committed-p, committed-not-p, attributed-only, conditional-only, none, genuinely-ambiguous}⟩; the write decision follows from the tuple by a fixed rule table. Ambiguous items are kept and scored by admissible-set matching.
  2. **Layer D — dyad items (Vietnamese only, natively authored).** (a) *Frame-flip pairs*: target turn held constant, e.g. "Lan bảo chị nên nghỉ việc để đi học tiếp."; context A establishes the user as *em* with Lan senior, context B establishes the user as *chị* with Lan junior. (b) *Distance manipulation*: the frame-setting turn is placed 1, k, or > window turns before the target, crossing each framework's documented extraction window. (c) *Null subject under report* ("Mẹ bảo về quê ăn Tết."), (d) attitude triple *biết / nghĩ / tưởng*, (e) negation without *không* ("Em có nghỉ việc đâu"). Every Vietnamese judgment is confirmed by ≥2 native annotators before it enters the gold; regional variants recorded.
  3. **Layer T — cue-matched scope twins (EN and VI, natively authored in each language, not translated).** A family = an asserted base turn + single-operator variants + a *license twin* and a *block twin* with the same cue inventory and opposite gold write decision ("Lan doesn't know I quit" vs "Lan doesn't think I quit"), at depth 2 and 3. Operators: REPORT/QUOTE × self/other, COND, NEG, ATT (factive / non-factive / counter-factive), TEMPORAL.
  4. **Held-out composition split**: few-shot exemplars and any tuned extractor see all single operators and a fixed subset of pairs; test uses unseen pairs and all triples; whole families held out.
  5. **Constructive probe — dyad register**: a minimal writer-side change that carries the current xưng–hô frame (speaker self-term, addressee term, named third parties with their terms) as explicit state into every extraction call. Tests whether the locality account is right (it should close the distance effect and leave twin errors untouched).

- Contribution type: new measurement/benchmark (primary) + mechanism finding (window locality) + small diagnostic method (dyad register).

- Claims (falsifiable):
  - **C1 (dyad anchoring).** On frame-flip pairs, the same-holder rate (assigning one holder to both members, always wrong for one) exceeds 50% for framework-native writers and stays above the human disagreement rate for the strongest structured extractor. **C1b:** translate-to-English-then-extract does not reduce it. Refuted if the best extractor reaches the human floor.
  - **C2 (locality, not comprehension).** For a fixed backbone, holder accuracy drops when the frame-setting turn moves outside the writer's extraction window, while a full-dialogue reader with the same backbone stays flat; the dyad register removes most of the drop. Refuted if there is no window effect.
  - **C3 (caution is not composition).** Cue-keyed policies (a FACTWASH-style lexicon gate; AgentMemGate's cautious extractor; a hedge-preserving prompt) show a trade-off on cue-matched twins: paired twin accuracy falls ≥ 20 points below their single-operator accuracy. Refuted if any reaches paired accuracy within 5 points of single-operator accuracy.
  - **C4 (composition).** Accuracy on held-out operator combinations is lower than on seen combinations of equal depth by more than the family-clustered 95% interval.

- Closest work known so far (with identifiers) and the expected delta — see the two prior-art reports for verification levels:
  - FACTWASH, arXiv:2608.03372 — cue-lexicon checks for five stances; single operators; names reported-speech scope as future work. **Baseline**, the cue-based policy the twins are built to break.
  - LAPSE, arXiv:2609.36457 — aspect minimal pairs on mem0/Graphiti/Letta; write decision never flips within a pair; English.
  - AuthMem-Bench, arXiv:2608.01679 — paired histories incl. third-party report → user fact; different channel (tool/e-mail), cues not matched, no nesting; English.
  - Manufactured Confidence, arXiv:2606.29279 — hearsay becomes flat fact in mem0/LangMem/Zep; its hedge-preserving prompt is weak contrary evidence to C3 and must be a baseline.
  - AgentMemGate, arXiv:2610.07707 — §6.2 already concedes protection "tracks wording"; C3 quantifies and generalises it rather than discovering it.
  - "Whose Memory Is It?", arXiv:2610.09008; CASK (OpenReview jXE0A1Pv0T) — discourse-ownership framing; **the framing is theirs, not claimed here**; they name nested scopes as future work.
  - WMT 2026, ACL Anthology 2026.wmt-main.16 — EN–VI translation with dyadic profiles and role reversal (20/20 → 4/20). Precedent for the annotation protocol; suggests MT picks a default dyad, which motivates C1b.
  - Chinese zero pronouns, arXiv:2605.31056 (Anthology 2026.findings-emnlp.654); Turkish indexical shift, arXiv:2406.05569; English indexicals 2025.findings-acl.1203 — linguistic neighbours outside memory.
  - DerivAudit 2609.36130, HaluMem 2511.03506, MemAlign/ConMem 2610.33432, PASB 2607.10526, TimlMemBench 2026.findings-emnlp.507, "Same Conversation, Different Languages" (OpenReview iJZKvQGoDj; EN/ES/HI/ZH, no Vietnamese) — positioning.
  - Keep-the-frame records (OLLIE D12-1048, MinIE, Eywa 2605.30771, DISCERN 2611.15729): **not claimed**; the earlier "lazy disquotation" claim is dropped.
  - Industry evidence (read on GitHub by hunter B): Graphiti's summary prompt instructs the writer to state facts directly and avoid reporting verbs; Mem0's prompts have no rule for third parties, reported speech, conditionals or negation.
  - Not found by either hunter: frame-flip/dyad items in any memory benchmark; any Vietnamese memory-writing benchmark; cue-matched opposite-gold twins; factive/non-factive/counter-factive verbs at write time; ≥2-operator nesting with held-out combinations. OpenReview was searchable only through its search endpoint; non-public ARR submissions are invisible.

- Evaluation sketch:
  - Size: Layer D ≈ 300 families × (2 frames × 3 distances) + ≈ 150 families for (c)–(e); Layer T ≈ 250 families per language × 5–6 variants. Target ≈ 4,500–5,500 scored propositions; all double-annotated by native speakers, third-person adjudication blind to model output; κ per field and per layer; naturalness rating per item.
  - Systems (15–20 configurations): native writers of 3–4 frameworks (Mem0, Graphiti/Zep, Letta, LangMem) × 2–3 backbones (commercial + one open model on local GPU) + extractor-only conditions.
  - Baselines, strongest first: (1) structured extractor on a frontier reasoning model that must output source chain, operator stack, anchor and holder before deciding; (2) the same with the dyad register; (3) FACTWASH-style gate; (4) AgentMemGate cautious extractor; (5) hedge-preserving prompt; (6) translate-to-English-then-(1); (7) full-dialogue reader (comprehension reference); (8) naive extract–store.
  - Metrics: same-holder rate on frame-flip pairs; holder accuracy by frame distance; paired twin accuracy; false unconditional promotion and licensed-fact retention; seen-vs-held-out gap; family-clustered bootstrap intervals. Secondary: effect on later answers with native vs oracle record.
  - Decisive experiment (run first, on a 60-family pilot): baseline (1) on frame-flip pairs with the frame outside the window, and on held-out cue-matched twins. If it sits at the human floor on both, the insight is dead for frontier extractors and the paper reduces to framework-level findings plus a negative result.

- Resources needed vs available: commercial APIs; one open model on 1–2 GPUs; ≥ 2 native Vietnamese annotators fluent in English (available). Natural English authoring would benefit from one near-native checker (to confirm). No user data: all dialogues fictional.

- Risks and unknowns: (1) annotation agreement on perspective items (TWIST reports low raw κ on comparable contrasts) — mitigated by the ambiguous class, not by filtering; (2) frontier models may solve English twins, shifting weight to Layer D; (3) Vietnamese judgments in this card are the generator's readings and need native confirmation; (4) scoop risk on Layer T is high (FACTWASH author and the LAPSE/SEAM lab are each one step away); Layer D is the protected part; (5) frameworks' extraction windows must be read from their code, not assumed.

- Conference core / journal extension:
  - Core: Layer D + Layer T, claims C1–C4, dyad-register probe.
  - Extension (Computational Linguistics accepts extended conference papers): annotation manual and disagreement analysis, a third language with obligatory social deixis (e.g. Korean/Japanese/Thai), VI–EN code-switched dialogues, downstream answer study.

- Generator perspective: linguistics/pragmatics, revised by the coordinator after Stage 5.
