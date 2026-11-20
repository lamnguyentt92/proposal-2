# IDEA_L1S: Who is "con"? Dyad-anchored person reference at memory-write time in Vietnamese

Redesign of IDEA_L1R after the Stage 6 adversarial review (`06_REDTEAM/IDEA_L1R_review_referee.md`,
`IDEA_L1R_review_feasibility.md`). It evolves the GPT-6 draft SCOPE-INTERVENTIONS v5 (reported-speech attribution at
memory-write time, Vietnamese person reference, human gold) and applies these review findings:
- the "frame outside the extraction window" result was true by construction → replaced by an **information-matched** comparison of native speakers and memory writers;
- no evidence that the tested frames occur in real user–assistant dialogue → an **elicitation study** is added and the naturally frequent construction (kin terms inside reports of family/work talk) becomes the core;
- categorical gold on graded phenomena → **graded gold** from several native raters with a "cannot tell" option;
- two benchmarks in one paper → the English cue-matched scope twins are removed (kept in the idea registry as a separate paper);
- only Mem0 and Graphiti have a bounded extraction context; Letta's Python server was retired → system list fixed accordingly.

- Gap addressed: G1 (primary), G12 (through the English-pivot and ASCII-normalisation findings).

- Target venue and track: ACL 2027 via ARR — "Discourse and Pragmatics" (first choice), alternative "Multilingualism and Cross-Lingual NLP"; eligible for the Special Theme "Homogenization and knowledge collapse in LLMs". Contribution types: data resource + model analysis.

- Problem (1 paragraph): A memory writer turns dialogue into context-free third-person records, so it must decide whom each proposition is about and who vouches for it. English hides this step because person is lexical (I / you / she). Vietnamese does not: kin terms (con, em, anh, chị, cháu, cô…) serve as first-, second- and third-person forms, and inside a report they are anchored to the dyad of the *reported* speech event. In "Mẹ bảo con về quê ăn Tết" the token *con* denotes the user (the child in the mother–child dyad); in "Chị Lan bảo chị mệt" the second *chị* most naturally denotes Lan herself; in "Anh Nam bảo anh sắp chuyển vào Sài Gòn" native speakers may disagree. Such sentences are how people ordinarily tell an assistant about family and work. The prompts of open-source memory writers are English and describe the step in English terms (Mem0 instructs the writer to replace pronouns with names or "User"); Graphiti's name deduplication strips non-ASCII letters, so distinct Vietnamese names can collapse (read from code, to be confirmed by execution). Every published memory-write benchmark found is English, Chinese–English or Russian, and none tests person anchoring.

- Key insight (the non-obvious observation; 2–3 sentences): Producing a third-person memory record from Vietnamese requires **dyad-anchored deixis resolution**: mapping a kin term to a person through the dyad of the speech event it belongs to. English makes the step invisible, so English-designed writers have no instruction for it — which predicts three specific, countable errors *even when all the needed information is in the writer's input*: **kin-noun literalisation** (the fact is filed under "User's child"/"the older sister"), **dyad capture** (the term is resolved in the wrong dyad, e.g. to the user–assistant pair), and **silent commitment** (the writer files the fact under one person where native speakers say "cannot tell"). Because the comparison is information-matched, a difference between writers and native speakers cannot be explained by missing context.

- Approach:
  1. **Study 0 — does it occur? (elicitation).** Native Vietnamese speakers converse freely with an assistant about scripted but open scenarios involving fictional family and workplace personas (no private data). Measured: how users refer to themselves and the assistant, how often kin terms occur inside reports, and how often the reported dyad differs from the user–assistant dyad. The elicited turns seed the benchmark.
  2. **Benchmark.** (a) *Natural layer*: elicited turns, lightly edited, with span-anchored gold frames ⟨about-whom, source chain, commitment, anchor span⟩ by two trained native annotators plus adjudication. (b) *Diagnostic layer*: authored minimal pairs — reported-dyad anchoring (con/em/cháu inside reports), self- vs other-reference of the reported speaker (chị Lan bảo chị… / …em…), frame-flip pairs, null subject under *bảo/nói/dặn*. (c) *Controls*: the same content with explicit names (Vietnamese) and English counterparts where person is lexical.
  3. **Graded gold on the diagnostic layer**: several native raters per item (target ≥ 8), who see exactly the context a given writer receives and may answer "cannot tell"; the gold is the reading distribution, not a single label.
  4. **Information-matched protocol**: every LLM call of each writer is logged; the human raters and the writer are compared on the same input. Records are scored three-way: correct person / wrong person / kin term left unresolved, plus the error taxonomy above.
  5. **Systems**: Mem0 OSS (10-message extraction context) and Graphiti (3-episode context), LangMem with a fixed caller-supplied context, each with one commercial and one local backbone; extractor-only conditions.
  6. **Downstream read-out (secondary)**: a later-session question whose correct answer depends on the person assignment, with native vs oracle record — the memory-state intervention retained from SCOPE-INTERVENTIONS, reported as a consequence measure, not claimed as a novel design.

- Contribution type: new measurement/benchmark + mechanism finding; the first natively authored Vietnamese memory-write resource with graded human gold.

- Claims (falsifiable):
  - **C1 (information-matched divergence).** With the same input, writers' person assignments diverge from the native-speaker reading distribution more on kin-term items than on the explicit-name Vietnamese controls and the English counterparts (item-level mixed model; divergence = probability mass on readings that fewer than 10% of raters chose). Refuted if the strongest structured extractor is within rater-to-rater divergence on kin-term items.
  - **C2 (silent commitment).** On items where at least half of the raters answer "cannot tell", framework-native writers file the fact under a specific person in more than half of the cases; an abstention-enabled extractor lowers this only by also dropping facts raters agree on (measured as licensed-fact retention). Refuted if abstention removes silent commitment at no retention cost.
  - **C3 (the pivot relocates errors).** Document-level translate-to-English-then-extract changes the error mix (fewer unresolved kin terms, more wrong-person assignments) without lowering the total wrong-or-unresolved rate below direct Vietnamese extraction. Refuted if translation closes the gap to the controls.
  - **C4 (it occurs).** In the elicited conversations, kin terms inside reports occur at a rate that makes the phenomenon non-marginal (descriptive, reported with intervals; threshold fixed before collection). A rare phenomenon turns the paper into a diagnostic study and is reported as such.

- Closest work and delta (verification levels are in the prior-art reports):
  - WMT 2026, ACL Anthology 2026.wmt-main.16 — EN–VI translation judged with dyadic profiles and role reversal. Generation-side appropriateness on 30 items; no reported speech, no person resolution, no memory. Protocol precedent.
  - Chinese zero pronouns, arXiv:2605.31056 (2026.findings-emnlp.654); Turkish indexical shift, arXiv:2406.05569; English indexicals, 2025.findings-acl.1203 — person reference under report outside memory.
  - Decontextualization (Choi et al., arXiv:2102.05169) — the closest formulation of "make a sentence stand alone"; English, no open-class person terms. **The baseline family a referee will demand: contextualise-then-extract with abstention.**
  - Memory-write errors in English: FACTWASH arXiv:2608.03372; LAPSE arXiv:2609.36457; AuthMem-Bench arXiv:2608.01679; Manufactured Confidence arXiv:2606.29279; AgentMemGate arXiv:2610.07707; "Whose Memory Is It?" arXiv:2610.09008; DerivAudit arXiv:2609.36130; HaluMem arXiv:2511.03506; MemAlign/ConMem arXiv:2610.33432 (15 attribution-confusion cases); PASB arXiv:2607.10526; TimlMemBench 2026.findings-emnlp.507. None has person anchoring or Vietnamese. Their framing (a write drops who said it) is **not claimed**.
  - Multilingual memory: "Same Conversation, Different Languages" (OpenReview iJZKvQGoDj; EN/ES/HI/ZH); MemBubble arXiv:2610.25127. No Vietnamese, no kin-term reference.
  - Vietnamese person reference: Luong (1990), John Benjamins; Lê Viết Dũng (2013) on address between humans. Graded factivity (Degen & Tonhauser) motivates distributional gold.
  - Not found by two hunters and one referee: any memory benchmark with dyad/kin-term items; any Vietnamese memory-write benchmark; any empirical source on how Vietnamese users address an assistant.

- Evaluation sketch:
  - Pilot gate (run first): 60 diagnostic families + 40 elicited turns; the strongest structured extractor with the full context, scored against 8 raters. If it is within rater-to-rater divergence, C1 is dead for frontier extractors and the paper is repositioned on framework-native writers and Study 0.
  - Full size: natural layer ≈ 600–800 turns; diagnostic layer ≈ 300 families × 2–4 variants; controls matched 1:1. Roughly 3,000–4,000 scored propositions.
  - Baselines, strongest first: (1) contextualise-then-extract with abstention on a frontier reasoning model, given exactly each framework's context; (2) structured extractor with an explicit dyad-resolution instruction in Vietnamese; (3) document-level translate-then-extract; (4) hedge-preserving prompt (Manufactured Confidence, verbatim); (5) framework-native writers; (6) full-dialogue reader (comprehension reference).
  - Metrics: three-way person score; error-type rates; silent-commitment rate; licensed-fact retention; divergence from the rater distribution; inter-rater statistics per field (κ/α; MASI-based α for admissible sets); later-answer wrong-person rate. Item- and family-clustered intervals.
  - Engineering check: run Graphiti on dialogues with Vietnamese names that differ only in diacritics and report whether distinct people are merged.

- Resources needed vs available: commercial APIs; one local model on 1–2 GPUs (e.g. a SEA-LION or Qwen 27B-class model — to be validated on the pilot); two trained native annotators (available). **Additional resources to obtain:** a third native speaker for adjudication, a pool of native raters for graded gold and participants for Study 0 (consent, compensation, ethics-exemption determination), and a native-English validator for the English controls.

- Risks and unknowns: (1) frontier extractors may match the raters (pilot gate); (2) the phenomenon may be rare in elicited talk (C4); (3) elicitation with scripted scenarios may not reflect spontaneous use — state this limit; (4) regional variation (bảo/biểu, kin-term defaults) needs raters from more than one region; (5) one language: a referee may ask for a second kin-term or honorific language — planned for the journal version; (6) all Vietnamese readings in this card must be confirmed by native speakers before use.

- Conference core / journal extension:
  - Core: Study 0, the benchmark with graded gold, C1–C3, the Graphiti diacritics check.
  - Extension (Computational Linguistics): an explicit model of anchor and dyad, annotation manual and disagreement analysis, a second kin-term/honorific language and a pro-drop contrast language, VI–EN code-switching.

- Generator perspective: linguistics/pragmatics; redesigned by the coordinator after Stage 6.
