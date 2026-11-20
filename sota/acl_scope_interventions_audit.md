# ACL 2027 proposal "SCOPE-INTERVENTIONS" — citation audit and adversarial prior-art search

Scope of this note: proposal file `/home/claude/research/agent-memory-2027/75d2a237-06_ACL_2027_SCOPE_INTERVENTIONS_FINAL_v5.md`, audited on 2026-11-20.

Access-path disclosure (applies to every finding below):
- `WebFetch` refused the arXiv abs URLs and three of the four ACL Anthology URLs because an approval prompt went unanswered. I did not retry those calls. arXiv records were read through the alphaXiv paper tools instead; the three Anthology landing pages and two Anthology PDFs were read through the alphaXiv page/PDF reader. One Anthology page (`2026.findings-emnlp.1289`) and the ACL 2027 CFP were read with `WebFetch`.
- For arXiv:2607.10526 and arXiv:2608.16551 alphaXiv returned an AI-generated structured report, not the raw PDF text. Title, authors and numbers for those two come from that report (SP-Mem's title, date and affiliation were also confirmed by an alphaXiv search listing). Treat exact figures for those two as "secondary until the PDF is opened".
- Items marked "abstract-level only" were seen only as a search listing (title + first lines of abstract); they are leads, not verified content.

## 1. Citation audit: does each cited work exist at the given identifier and match the proposal's description?

### Takeaway
All seven cited works exist at the stated identifiers and broadly match the proposal's one-line descriptions; none is fabricated. The EMNLP 2026 Anthology volumes are published (site build dated 19 Nov 2026). The weaknesses are omissions and slightly generous "delta" wording, not fake references.

### Cited Findings

| # | Proposal's label and identifier | Verdict | What is really there |
|---|---|---|---|
| 1 | "Gated Memory", arXiv:2610.11270 | EXISTS + MATCH | "Gated Memory: Admission-Controlled Memory Formation for Conversational AI"; Preeti Saraswat, Divya Neelagiri, Ajay Manoj (Samsung Research America); v1 stamped 8 Oct 2026. A method paper, not a benchmark. |
| 2 | "Persistent Sycophancy / PASB", arXiv:2607.10526 | EXISTS + MATCH | "Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents"; Mao et al. (City University of Hong Kong, ByteDance, Yale, Fudan, Dalian University of Technology, Hong Kong Baptist University). |
| 3 | "TimlMemBench", aclanthology 2026.findings-emnlp.507 | EXISTS + MATCH | "TimlMemBench: A Diagnostic Benchmark for Governed Use of Long-Term Memory in Dialogue Agents"; Fangxing Zhou, Yifei Sun, Jiachen Li, Jinyu Xu, Yuhan Wang, Ruixin Li, Qing Xie; Findings of EMNLP 2026, pp. 10624–10638. |
| 4 | "LOCOMO-CONV", aclanthology 2026.findings-emnlp.1289 | EXISTS + MATCH | "When Users Don't Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents"; Wen-Yu Chang, Yun-Nung Chen (National Taiwan University); Findings of EMNLP 2026, pp. 27273–27293. |
| 5 | "OP-Bench", aclanthology 2026.emnlp-main.1168 | EXISTS + MATCH | "OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents"; Yulin Hu, Zimo Long, Jiahe Guo, Xingyu Sui, Xing Fu, Weixiang Zhao, Yanyan Zhao, Bing Qin (Harbin Institute of Technology); EMNLP 2026 main, pp. 26770–26827. Also on arXiv as 2601.13722. |
| 6 | "BELIEFMEM", aclanthology 2026.findings-emnlp.576 | EXISTS + MATCH (it is a memory system, not a benchmark) | "BELIEFMEM: Belief-Revising Memory for Conversational LLM Agents"; Felix Meng, Junda Wu, Julian McAuley; Findings of EMNLP 2026, pp. 12152–12166. |
| 7 | "SP-Mem", arXiv:2608.16551 | EXISTS + MATCH | "What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents"; Wenjie Wang, Wenhe Si, Xinyue Xu, Yue Xu (ShanghaiTech University); listed as published 2026-08-17. |
| 8 | ACL 2027 CFP, https://2027.aclweb.org/calls/main/ | EXISTS + MATCH on the facts the proposal uses | ARR deadline 4 Jan 2027, AoE; 8-page long / 4-page short; dual submission prohibited. |

Per-item evidence:

- Gated Memory places an admission gate ahead of extraction, labels each fact as directly stated or inferred, attaches a condition-of-applicability scope and a four-class entity scope (USER_PII / INTERNAL / EXTERNAL / GENERIC) that governs enrichment. Its only evaluation is LoCoMo-10 (1,540 questions) on a mem0 baseline with an 8B open model: 50.6 to 51.9 LLM-judge accuracy (+2.6% relative), with a −4.2% multi-hop regression; the gate rejected 355 of 5,882 utterances (6.0%). — [arXiv:2610.11270](https://arxiv.org/abs/2610.11270)
- Hedged speech is already inside Gated Memory's admission examples: an utterance of the form "I might switch to Android next year" is listed as REJECT because it carries no commitment, against an ADMIT twin with a definite plan. Its "provenance" label means stated-versus-inferred, not which speaker said it. — [arXiv:2610.11270](https://arxiv.org/abs/2610.11270)
- PASB comprises 1,600 eight-turn tasks (100 base items × 4 scenario framings × 4 delivery patterns), run on two agent stacks (Hermes-Agent, OpenClaw) with 12 backbones; conversation history is wiped between the persist stage and the query stage so that later influence must come from durable state. Mean per-turn failure was 45.0% for session-only episodes against 71.9% for committed ones (+27.0 points); status promotion appeared in 51.4% of episodes and attribution removal in 33.1%. — [arXiv:2607.10526 via alphaXiv report](https://www.alphaxiv.org/abs/2607.10526)
- TimlMemBench's release holds 208 reviewed samples (117 Chinese, 91 English), 1,566 sessions, 1,715 questions and 1,821 governance or activation cases, scored on nine metric families (Write, Revoke, Supersede, Preserve, Scope, Provenance, Boundary, Activation, Proactive). Its limitations section describes the dialogue as synthetic and human-corrected. — [ACL Anthology 2026.findings-emnlp.507](https://aclanthology.org/2026.findings-emnlp.507/), [PDF](https://aclanthology.org/2026.findings-emnlp.507.pdf)
- LOCOMO-CONV rewrites LoCoMo's QA pool into four query styles: 1,986 dialog, 1,986 implicit, 1,540 counterfactual and 1,069 composed items. "Counterfactual" there means a user query carrying a false premise, and "composed" means a query needing two source memories; neither is an intervention on memory nor a composition of linguistic operators. — [ACL Anthology 2026.findings-emnlp.1289](https://aclanthology.org/2026.findings-emnlp.1289/), [PDF](https://aclanthology.org/2026.findings-emnlp.1289.pdf)
- A small discrepancy exists inside LOCOMO-CONV's own record: the landing-page summary I received spoke of four memory systems, while the PDF abstract and setup section list five (AnchorMem, A-MEM, mem0, Memora, dense retrieval). — [landing page](https://aclanthology.org/2026.findings-emnlp.1289/); contradicted by [PDF](https://aclanthology.org/2026.findings-emnlp.1289.pdf)
- OP-Bench defines over-personalization as Irrelevance, Repetition and Sycophancy and supplies 1,700 verified instances over 20 users, built from LoCoMo; the proposal's description of it is accurate. — [ACL Anthology 2026.emnlp-main.1168](https://aclanthology.org/2026.emnlp-main.1168/)
- BELIEFMEM implements AGM-style belief revision as the write semantics of a never-deleting fact store and reports 85.5% on LoCoMo (1,540 questions) and 54.5% on BEAM (400 questions). It contributes no dataset. — [ACL Anthology 2026.findings-emnlp.576](https://aclanthology.org/2026.findings-emnlp.576/)
- SP-Mem separates a searchable sanitized memory from a protected store of exact private values and restores exact values only after a consent request; its companion benchmark has 1,000 synthetic profiles, 21,000 history dialogues and 54,000 test queries. — [arXiv:2608.16551 via alphaXiv report](https://www.alphaxiv.org/abs/2608.16551)
- The ACL 2027 call gives 4 January 2027 (11:59 PM UTC-12) as the ARR deadline for long and short papers, 8 and 4 pages respectively with one extra page at camera-ready, a main conference on 20–22 August 2027, a special theme on homogenization and knowledge collapse in LLMs, and a flat ban on dual submission. Notification and commitment dates were still "TBD" on the page. — [ACL 2027 CFP](https://2027.aclweb.org/calls/main/)
- Publication status of EMNLP 2026: both volumes carry Anthology IDs, DOIs and ISBNs (main 979-8-89176-459-0, Findings 979-8-89176-462-0), month October 2026, address Budapest, Hungary; the PDF header gives conference dates 24–29 October 2026 and the site footer shows a build on 19 November 2026. — [2026.emnlp-main.1168](https://aclanthology.org/2026.emnlp-main.1168/), [2026.findings-emnlp.507 PDF](https://aclanthology.org/2026.findings-emnlp.507.pdf)
- A third-party index lists 5,540 EMNLP 2026 entries with links in the `2026.emnlp-main.N` format. — [papers.cool EMNLP 2026](https://papers.cool/venue/EMNLP.2026)

### Inferences
- The fear that an AI-drafted proposal invented its references is not borne out here: 7 of 7 papers plus the CFP check out. The drafting model evidently worked from real abstracts.
- Three "delta" cells in the proposal's table are softer than they look once the full papers are read. (a) Against PASB, the proposal claims "causal write-state tests instead of only persistent failure", but PASB already isolates durable state by clearing history and reports a committed-versus-session-only contrast; what PASB lacks is randomized assignment of memory contents. (b) Against TimlMemBench, the proposal claims stage-wise intervention as new, but TimlMemBench's canonical-pool versus raw-native design is already a "clean memory versus self-ingested memory" contrast. (c) Against Gated Memory, hedged content is already handled; the true gap is that Gated Memory has no benchmark and no quotation/reported-speech/negation coverage.
- A faithful reproduction of Gated Memory as a baseline (proposal §7) looks risky: the text I read mentions no code release and uses an unnamed "open-source 8B instruction-tuned LLM".

### Gaps
- Raw PDFs of arXiv:2607.10526 and arXiv:2608.16551 were not opened; numbers for those rest on an AI-generated report.
- The CFP summary I received did not list "Discourse and Pragmatics" by name among topic areas (it listed dialogue systems, LLM agents, human-centered NLP, multilingual NLP, semantics, among others). Whether that exact track name exists for ACL 2027 is unverified; the summary may have been abbreviated.
- The proposal's statement that ACL "welcomes rigorous resources, reproduction, negative findings" was not checked against the CFP text.

## 2. Is the core idea already published? What was searched and what turned up

### Takeaway
No single paper matches the full package (human-annotated EN–VI benchmark of nested pragmatic operators + stage accounting + three-arm memory intervention). Every individual ingredient except the Vietnamese/compositional-linguistics one has, however, appeared in 2025–Nov 2026 work, most of it missing from the proposal's related-work table.

### Cited Findings

Searches run (a null result below is not proof of absence):
- alphaXiv semantic search, five queries: memory-governance and belief-revision benchmarks; memory write/extraction errors from hypothetical, quoted, reported, third-party, negated, sarcastic or role-play content; veridicality / event factuality / speaker commitment / reported speech / negation in LLMs; Vietnamese and EN–VI dialogue, pragmatics, kinship, code-switching; contextual-integrity and consent-aware memory plus multilingual memory benchmarks; plus a "historical" query on FactBank/UW/MegaVeridicality.
- Web search: the four benchmark names, the Anthology IDs, EMNLP 2026 proceedings, and a Vietnamese long-term conversational memory benchmark query.

Write-error and memory-formation work found:
- AgentMemGate names "speculation contamination" (a stated plan stored as current fact), builds a plan-to-outcome dataset and reports that Mem0 and Graphiti assert unresolved plans as current state for 35.2% and 27.3% of pending plans. — [arXiv:2610.07707](https://arxiv.org/abs/2610.07707)
- HaluMem scores memory systems separately on extraction, updating and question answering, with a False Memory Resistance metric on distractor content that the assistant mentions but the user never confirms. — [arXiv:2511.03506](https://arxiv.org/abs/2511.03506)
- MemGuard defines write-time, retrieval-time and composition-time contamination with categories such as "spurious_inference_stored", and its motivating example is a friend's experience with ibuprofen being stored as a general fact for the user. — [arXiv:2605.28009](https://arxiv.org/abs/2605.28009)
- DerivAudit ("Memory Is a Derivation") audits whether each written memory follows from pre-write history, cataloguing status mutations (plan rewritten as ongoing activity, "may" rewritten as "moved") and binding errors (an attribute or duration attached to the wrong entity). — [arXiv:2609.36130](https://arxiv.org/abs/2609.36130)
- A user study of 28 memory exports (457 entries) and a 32-person diary study (304 reports) yields a 14-type misalignment taxonomy whose intake stage includes "attribution confusion": third-party attributes, proxy questions asked for someone else, and fictional personas from creative writing being filed under the user's own profile. — [arXiv:2609.33623](https://arxiv.org/abs/2609.33623)
- MemAlign turns that taxonomy into 1,079 store / do-not-store cases (779 / 300) across ten reason categories, including attribution_confusion (15 cases), over_inference (55) and identity_mis_inference (11). — [arXiv:2610.33432](https://arxiv.org/abs/2610.33432)
- TWIST's unprompted-tension track specifies hard negatives that include hypotheticals, jokes, nostalgia and acknowledged changes of mind, priced with a paired false-flag metric. — [arXiv:2609.28575](https://arxiv.org/abs/2609.28575)
- "MemForm: Benchmarking Memory Formation Poisoning in LLM Agents" exists (USTC, Oct 2026) — abstract-level only. — [arXiv:2610.14431](https://www.alphaxiv.org/abs/2610.14431)
- "MemSecBench", tracking memory poisoning from persistence to consequence and repair — abstract-level only. — [arXiv:2607.27080](https://www.alphaxiv.org/abs/2607.27080)

Interventional / causal evaluation of memory contents found:
- DerivAudit's downstream probes hold the task fixed and supply a correct memory, a distorted one, or none; distorted memory raised failure by 83.8–93.0 points and withholding a valid memory by 92.8–99.5 points across three readers. — [arXiv:2609.36130](https://arxiv.org/abs/2609.36130)
- "The Memory Trap" compares fresh sessions with no memory, a raw transcript, or the agent's self-written note, and formalizes write-time versus read-time overgeneralization through the scope of the history versus the scope stated in the note. — [arXiv:2611.07554](https://arxiv.org/abs/2611.07554)
- ConMem decides admission by generating responses with and without the candidate memory and aggregating a "Counterfactual Memory Treatment Effect". — [arXiv:2610.33432](https://arxiv.org/abs/2610.33432)
- MemTrace re-supplies gold evidence on failed probes and finds 73.3% of sampled failures are "reached but unused" versus 7.0% reach misses, with oracle evidence lifting accuracy to roughly 80–85%. — [arXiv:2606.17328](https://arxiv.org/abs/2606.17328)
- "Stale, Misattributed, or Late" scores the memory block before generation and separates stale exposure from wrong-person exposure; its misattribution is a same-name serving error, not a speaker-commitment error at write time. — [arXiv:2610.10265](https://arxiv.org/abs/2610.10265)

Consent / contextual-integrity memory benchmarks found (all abstract-level only unless already audited above):
- "CIMemories: A Compositional Benchmark for Contextual Integrity of Persistent Memory in LLMs" (Meta, Nov 2025). — [arXiv:2511.14937](https://www.alphaxiv.org/abs/2511.14937)
- "PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?" (Feb 2026). — [arXiv:2602.01146](https://www.alphaxiv.org/abs/2602.01146)
- "GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents" (Jun 2026). — [arXiv:2606.18829](https://www.alphaxiv.org/abs/2606.18829)
- "ConCI: A Controlled Counterfactual Benchmark for Contextual Integrity in LLMs" (Oct 2026). — [arXiv:2610.24494](https://www.alphaxiv.org/abs/2610.24494)
- "MemJoin", latent privacy risks across sessions (Oct 2026). — [arXiv:2610.24359](https://www.alphaxiv.org/abs/2610.24359)

Linguistic side (veridicality, factuality, reported speech) — all abstract-level only:
- "Neural models of factuality" evaluates on FactBank, UW and MEANTIME. — [arXiv:1804.02472](https://www.alphaxiv.org/abs/1804.02472)
- "MAVEN-Fact: A Large-scale Event Factuality Detection Dataset" (2024). — [arXiv:2407.15352](https://www.alphaxiv.org/abs/2407.15352)
- "Zero-Shot Belief: A Hard Problem for LLMs" does source-and-target belief prediction on FactBank with LLMs (2025). — [arXiv:2502.08777](https://www.alphaxiv.org/abs/2502.08777)
- "He Thinks He Knows Better than the Doctors: BERT for Event Factuality Fails on Pragmatics" (2021). — [arXiv:2107.00807](https://www.alphaxiv.org/abs/2107.00807)
- "Training LLMs to Recognize Hedges in Spontaneous Narratives" (2024). — [arXiv:2408.03319](https://www.alphaxiv.org/abs/2408.03319)
- An assertion-aware re-score of an LLM judge that had counted reported teammate errors as hallucinations (Jun 2026) — the reported-versus-asserted confusion documented for judges rather than for memory writers. — [arXiv:2606.21666](https://www.alphaxiv.org/abs/2606.21666)
- AgentMemGate itself cites hedge detection and event-factuality research (Farkas et al. 2010; Saurí and Pustejovsky 2009) as the motivation for separating speculation from completed events, so the factuality-to-memory bridge has been drawn in print. — [arXiv:2610.07707](https://arxiv.org/abs/2610.07707)

Vietnamese and code-switching:
- No Vietnamese or English–Vietnamese long-term-memory benchmark surfaced in either the alphaXiv query or the web query; the web query returned only English/Chinese memory papers. — [web search results, e.g. EvolMem](https://arxiv.org/html/2601.03543)
- Vietnamese resources that did surface are in other areas: medical code-switching speech (ViMedCSS), a speech/deepfake corpus with code-switching (VietPrism), figurative language (VIVID), and dialect robustness — all abstract-level only. — [arXiv:2602.12911](https://www.alphaxiv.org/abs/2602.12911), [arXiv:2609.30005](https://www.alphaxiv.org/abs/2609.30005), [arXiv:2608.03095](https://www.alphaxiv.org/abs/2608.03095), [arXiv:2608.10414](https://www.alphaxiv.org/abs/2608.10414)
- PingPong, a human-authored multi-party code-switching dialogue benchmark, covers Indonesian–English, Javanese–Indonesian–English, Sundanese–Indonesian–English, Hausa–English and Algerian Arabic–Standard Arabic–French; Vietnamese is absent. Its reference list cites CanVEC, a Canberra Vietnamese–English code-switching natural speech corpus (Nguyen and Bryant, LREC 2020), which I did not open. — [arXiv:2601.17277](https://arxiv.org/abs/2601.17277)
- A generation benchmark for culturally specific kinship terms exists (Sep 2026) — abstract-level only; language coverage unknown. — [arXiv:2609.26942](https://www.alphaxiv.org/abs/2609.26942)
- Non-English memory benchmarks do exist for other languages: a Russian user-memory benchmark (RUMBA, abstract-level only), TimlMemBench's Chinese half, and MemAlign, whose authors say they primarily target Chinese-speaking chatbot users. — [arXiv:2607.21447](https://www.alphaxiv.org/abs/2607.21447), [2026.findings-emnlp.507](https://aclanthology.org/2026.findings-emnlp.507/), [arXiv:2610.33432](https://arxiv.org/abs/2610.33432)

### Inferences
- The proposal's §3 table lists none of AgentMemGate, HaluMem, MemGuard, DerivAudit, MemAlign/ConMem, the user-perspective taxonomy, Memory Trap, MemTrace, CIMemories or PersistBench. A referee active in this area will know several of them; the omission is the largest literature risk in the document.
- The field moved fast in the eight weeks before this audit (AgentMemGate 6 Oct, Gated Memory 8 Oct, ConMem 24 Oct, Memory Trap 5 Nov 2026). More overlap is likely to appear before a January deadline.
- "Multilingual" on its own is weakened as a selling point by the existence of Chinese–English and Russian memory benchmarks; the Vietnamese argument has to rest on language-specific phenomena, not on adding a language.

### Gaps
- Not searched or not reachable: OpenReview (ICLR 2027 submissions), Semantic Scholar, dblp, Hugging Face datasets, GitHub repositories of Mem0/Zep/Letta. Framework-level evaluations of extraction prompts were therefore not examined.
- MegaVeridicality, the UW factuality corpus, quote-attribution corpora and negation-scope benchmarks for LLMs were not retrieved as primary records in this session; I cannot say whether an LLM-era benchmark already crosses reported speech × conditional × negation outside the memory setting.
- Sarcasm and role-play as sources of memory-write errors: no dedicated benchmark surfaced, but the search was one query deep.
- MemForm, MemSecBench, CIMemories, PersistBench, GateMem, StateMemBench and MemoryAgentBench were not read; overlap with them is unassessed beyond their abstracts.

## 3. The closest works, with exact deltas

### Takeaway
Nine works sit close. Two of them (AgentMemGate and DerivAudit) reproduce the proposal's central causal story — a non-asserted statement becomes a stored fact and then corrupts later answers — for a narrower set of linguistic triggers, in English, with machine-generated or pre-existing data.

### Cited Findings

1. AgentMemGate — [arXiv:2610.07707](https://arxiv.org/abs/2610.07707) (NeurIPS 2026 PALM workshop per its footer)
   - Measures: the share of never-true plans sitting in a profile store as the current value, both while the plan is pending and at conversation end; plus task accuracy and an over-holding control on completed changes.
   - Data: 60 core, 147 held-out and 179 controlled-difficulty conversations; the controlled split varies hedge strength over five levels and confirmation wording over four.
   - Annotation: all splits are LLM-generated and author-reviewed; a blind human audit of 54 judge decisions reached κ = 0.74; classifier labels are model-voted with a 40-item human audit.
   - Languages: not stated; every example is English.
   - Delta to the proposal: one operator family only (speculative future plans), single-valued profile slots, no quotation, reported speech, third-party attribution or negation; no nesting; no human-authored dialogue; its "intervention" is gate on/off on an identical pipeline, not assignment of memory contents.

2. DerivAudit, "Memory Is a Derivation" — [arXiv:2609.36130](https://arxiv.org/abs/2609.36130)
   - Measures: whether each natural memory write is supported by pre-write history, at the level of "semantic obligations" (facts, relations, qualifications); admission reliability of verifiers; downstream effect of correct / distorted / absent memory.
   - Data: 400 unedited writes from LoCoMo and HaluMem-Medium (391 labelled), plus 70 matched controlled families.
   - Annotation: two model assessments with blinded adjudication; a stratified human review agreed 96.0%.
   - Findings: 17–21% of writes stay unsupported after evidence expansion; unsupported writes are admitted 59–89% of the time by verifiers.
   - Delta: no linguistic operator taxonomy, no speaker-commitment or quotation analysis, English only, labels are model-produced; but the three-condition downstream probe is structurally the proposal's Arm O / Arm N / Arm 0.

3. PASB — [arXiv:2607.10526](https://www.alphaxiv.org/abs/2607.10526) (cited by the proposal)
   - Measures: commit rate into durable state, status promotion, attribution removal, and six downstream failure dimensions after history is cleared.
   - Data: 1,600 tasks; 12 backbones × 2 frameworks; LLM judge plus manual persist-stage annotation.
   - Delta: content is biased or sycophancy-inducing claims, not truth-conditionally non-asserted utterances; framings are four coarse "roles", not composed operators; committed-versus-session-only is an observed split, not a randomized arm.

4. TimlMemBench — [2026.findings-emnlp.507](https://aclanthology.org/2026.findings-emnlp.507.pdf) (cited by the proposal)
   - Measures: nine governed-memory families after raw-session ingestion, alongside a canonical-pool control where every system reads the same clean memory pool.
   - Data: 208 samples, Chinese and English; a SKIP operation covers candidate facts that are unsupported, ephemeral or out of scope.
   - Annotation: synthetic then human-corrected; two annotators audited 90 cases with κ between 0.69 and 0.84.
   - Delta: no operator-level linguistic labels, no quotation/conditional/negation contrasts, no Vietnamese; its two-view design already separates "can answer from clean memory" from "can form memory correctly".

5. MemAlign / ConMem with the user-perspective taxonomy — [arXiv:2610.33432](https://arxiv.org/abs/2610.33432), [arXiv:2609.33623](https://arxiv.org/abs/2609.33623)
   - Measures: store / do-not-store decisions with reason categories; ConMem's treatment-effect score from with- and without-memory responses.
   - Data: 1,079 candidate memories with synthetic multi-session contexts (Qwen-generated, two researchers reviewing); the upstream taxonomy comes from real users' exported memories and diaries.
   - Delta: attribution confusion is present but tiny (15 cases) and coarse; contexts are synthetic; the user base is mainly Chinese; no span-level frames, no nesting, no later-session native-versus-oracle comparison.

6. HaluMem — [arXiv:2511.03506](https://arxiv.org/abs/2511.03506)
   - Measures: extraction recall/accuracy, false-memory resistance, update correctness and QA hallucination, each after the relevant session.
   - Data: 20 users, 14,948 memory points, 3,467 QA pairs in the Medium set; eight annotators rated 700 sessions and found 95.70% correct.
   - Findings: extraction accuracy stayed below 62% for all systems tested.
   - Delta: distractors are assistant-asserted false facts, not user utterances under modal, reportative or negative scope; synthetic; English; no operator analysis.

7. The Memory Trap — [arXiv:2611.07554](https://arxiv.org/abs/2611.07554)
   - Measures: unsafe or unreliable later behaviour with no memory, a transcript, or a self-written note; audits whether the note's stated scope exceeds what the interaction licensed.
   - Data: 20 formation tasks and 300 deployment scenarios for autonomy, plus sycophancy and cheating suites; six frontier models.
   - Delta: concerns scope broadening of preferences and procedures, not factual misattribution; no linguistic annotation; English; but it owns the "write-time versus read-time" decomposition with a formal definition.

8. Gated Memory — [arXiv:2610.11270](https://arxiv.org/abs/2610.11270) (cited by the proposal)
   - A method with hedged/transient rejection, stated-versus-inferred provenance and a no-new-entity grounding rule; evaluated only by LoCoMo QA accuracy.
   - Delta: no benchmark, no error taxonomy, no evidence about quotation or reported speech.

9. MemGuard — [arXiv:2605.28009](https://arxiv.org/abs/2605.28009)
   - A type-aware memory framework whose LLM-judged analysis of 300 LoCoMo failures ties 97.7% of unverifiability errors to write-time contamination.
   - Delta: stage attribution is post hoc and model-judged; the categories are memory-type confusions rather than pragmatic operators.

Supporting, slightly further away:
- TWIST Track B offers a worked precedent for human agreement on subtle pragmatic contrasts: raw κ of 0.565 on 200 candidates, rising to 0.851 only after 39 items were dropped. — [arXiv:2609.28575](https://arxiv.org/abs/2609.28575)
- LOCOMO-CONV documents an answer-time misattribution case in which the retrieved memory belongs to the other speaker. — [2026.findings-emnlp.1289 PDF](https://aclanthology.org/2026.findings-emnlp.1289.pdf)

### Inferences
- Does the delta matter to an ACL referee? For a Dialogue/LLM-agents reviewer, "hypothetical or temporary statements get stored as facts and then poison later answers" will read as known (AgentMemGate, DerivAudit, Gated Memory, MemGuard). For a Semantics/Discourse reviewer, the remaining delta — controlled composition of reportative, conditional, negative and quotative operators with human gold frames, in a language where person reference works differently — is a real and reviewable contribution, provided the data are natural and agreement is reported per layer.
- The three-arm estimand is no longer a differentiator by itself. DerivAudit (correct / distorted / none), Memory Trap (none / transcript / note), ConMem (with / without) and MemTrace (oracle evidence) each cover part of it. What is still open is applying the oracle-versus-native contrast to records that systems themselves produced from operator-labelled input, so that the downstream effect can be broken down by linguistic structure.
- The proposal's FUPR and LFRR metrics have close analogues in AgentMemGate's contamination rate and over-holding control and in MemAlign's Store / Do-Not-Store recall; they should be presented as adaptations.
- TWIST's agreement drop is a warning for the proposal's go/no-go gate 1: on contrast sets about what a speaker actually committed to, raw agreement near 0.57 is a realistic first outcome.

### Gaps
- Dataset language for AgentMemGate and DerivAudit is inferred from examples and source corpora, not stated.
- I did not open the GitHub artifacts of AgentMemGate, TWIST or MemAlign to inspect items; it is possible that some include quoted or reported-speech cases not described in the papers.
- PASB's exact author order and the full list of its "attribution removal" annotation rules were not checked against the PDF.

## 4. Which parts of the proposal remain unclaimed, and which are already covered

### Takeaway
Unclaimed after this search: nested operator composition with span-aligned frames, quotation and reported-speech attribution at write time, negation-scope write errors, and anything Vietnamese (pronoun and kinship person reference, null subjects, VI–EN code-switching). Covered or crowded: speculative/hedged statements, transient versus stable facts, third-party attribution as a coarse category, stage-wise accounting, memory-state interventions, and the consent/permission dimension.

### Cited Findings

Already covered:
- Hypothetical or planned content stored as fact: benchmarked with graded hedge strength. — [arXiv:2610.07707](https://arxiv.org/abs/2610.07707)
- Transient versus durable facts and conditional scope at formation time. — [arXiv:2610.11270](https://arxiv.org/abs/2610.11270)
- Third-party and fictional content filed as the user's own: observed in real user data and included as a benchmark category. — [arXiv:2609.33623](https://arxiv.org/abs/2609.33623), [arXiv:2610.33432](https://arxiv.org/abs/2610.33432)
- Stage-wise accounting across write, retrieval and answer stages. — [arXiv:2511.03506](https://arxiv.org/abs/2511.03506), [arXiv:2605.28009](https://arxiv.org/abs/2605.28009), [arXiv:2606.17328](https://arxiv.org/abs/2606.17328)
- Controlled contrasts over memory contents and their downstream effect. — [arXiv:2609.36130](https://arxiv.org/abs/2609.36130), [arXiv:2611.07554](https://arxiv.org/abs/2611.07554)
- Revocation, supersession, scope, boundary and restraint in Chinese and English. — [2026.findings-emnlp.507](https://aclanthology.org/2026.findings-emnlp.507/)
- Permission, consent and contextual integrity for persistent memory. — [arXiv:2608.16551](https://www.alphaxiv.org/abs/2608.16551), [arXiv:2511.14937](https://www.alphaxiv.org/abs/2511.14937), [arXiv:2602.01146](https://www.alphaxiv.org/abs/2602.01146)

Not found in any work read:
- A design that crosses two or more scope operators (for instance reported speech over a conditional over a first-person quote) and tests held-out operator combinations. The nearest thing is a single-factor hedge-strength sweep. — [arXiv:2610.07707](https://arxiv.org/abs/2610.07707)
- Span-aligned proposition frames with embedded-speaker, commitment and operator-order fields as gold. DerivAudit's obligations are free-form and model-labelled. — [arXiv:2609.36130](https://arxiv.org/abs/2609.36130)
- Vietnamese in any memory benchmark; the multilingual memory sets seen are Chinese–English and Russian. — [2026.findings-emnlp.507](https://aclanthology.org/2026.findings-emnlp.507/), [arXiv:2607.21447](https://www.alphaxiv.org/abs/2607.21447)
- Fully human-authored dialogue as the main data source for a memory-write benchmark. The memory benchmarks read here are LLM-generated with human review; the one fully human-authored dialogue resource found is a code-switching benchmark outside the memory area. — [arXiv:2601.17277](https://arxiv.org/abs/2601.17277)

### Inferences
- The defensible core is a linguistics-first resource: "which scope structures break memory writers, and does the breakage differ in a language with kinship-based person reference and frequent null subjects?" The proposal's own Example 1 (embedded "tôi" inside Lan's quoted conditional) is exactly the unclaimed territory.
- RQ2 (the authenticated permission ledger) adds an annotation layer in the most crowded sub-area and is the natural candidate to cut or demote to a single controlled factor.
- Negation deserves a caution: a negated statement such as "I have no plan to move" is itself an assertable user fact, so the benchmark must separate "stored the positive proposition" from "correctly stored the negative one"; none of the prior works read supplies a ready-made scoring rule for this.
- The Vietnamese contribution only counts if items are natively authored and include phenomena without an English counterpart; translated minimal pairs would reduce it to "one more language", which Chinese–English and Russian resources already undercut.

### Gaps
- Whether Mem0, Zep/Graphiti, Letta or A-MEM extraction prompts already contain rules about quotes, third parties or hypotheticals was not inspected; AgentMemGate reports that a "cautious" extractor modelled on published prompts cut contamination to 2.5% on its core set, which suggests strong prompting may erase part of the effect — the proposal's own null hypothesis. — [arXiv:2610.07707](https://arxiv.org/abs/2610.07707)
- No primary source was retrieved on Vietnamese pronoun or kinship-term resolution in NLP, so the difficulty of that phenomenon for current models is asserted by the proposal, not evidenced here.

## 5. Calibration: size and rigor of accepted benchmark papers on conversational memory

### Takeaway
Accepted ACL-family memory benchmarks in 2025–2026 carry roughly 1,000–5,000 scored items, are mostly LLM-generated with human review, validate with two or three annotators on 40–100 items (κ about 0.7–0.9), and evaluate between 5 and 30 system configurations. A pilot of 40–60 dialogue families is one to two orders of magnitude below that in raw item count unless each family expands into many scored contrasts.

### Cited Findings

| Paper (venue) | Size | Languages | Human annotation and agreement | Systems evaluated |
|---|---|---|---|---|
| TimlMemBench (Findings of EMNLP 2026) | 208 samples; 1,566 sessions; 1,715 questions; 1,821 cases | Chinese, English | 2 annotators on 90 cases, 84.4–93.3% agreement, κ 0.69–0.84; primary judge 87.8% accurate against adjudicated human labels on 90 outputs | 12 external memory systems plus controls |
| OP-Bench (EMNLP 2026 main) | 1,700 instances, 20 users; filtered from 10,000 generated candidates | English | 12 annotators, about 800 person-hours, double review with senior adjudication; 22.6% of items needed adjudication; judge–human correlation about 0.68 | 30 configurations (6 LLMs × 5 memory settings) |
| LOCOMO-CONV (Findings of EMNLP 2026) | 1,986 + 1,986 + 1,540 + 1,069 items | English | 3 annotators × 40 items per style; naturalness 4.6–4.8 of 5; three-judge Fleiss κ 0.745 | 5 memory systems |
| LoCoMo-Plus (ACL 2026 long, per the citation in LOCOMO-CONV) | size not stated in the pages retrieved; described as deliberately small and diagnostic | English | manual memory-worthiness check and elicitation validation; two human annotators agree 0.903 with each other, 0.80–0.82 with the judge | 11 LLMs, 3 RAG variants, 3 memory systems |
| Memora, "From Recall to Forgetting" (Findings of ACL 2026, per the citation in TWIST) | 10 personas; 600 questions across three horizons; 7,054 evaluation criteria | English | 3 annotators on 100 criteria; κ 0.86–0.90; judge–human agreement 88.3% | 4 LLMs and 6 memory agents |
| MemBench (Findings of ACL 2025) | 500 user graphs; about 53k questions over about 65k sessions | not stated | none reported in the pages retrieved | 7 memory mechanisms; 4 backbones |
| HaluMem (arXiv; venue unverified) | 20 users; 14,948 memory points; 3,467 QA | English | 8 annotators over 700 sessions; 95.70% correctness | 6 commercial or open memory systems |
| TWIST Track B (arXiv, vendor-authored) | 161 items retained from 200 | English | 2 annotators; κ 0.565 raw, 0.851 after adjudicated filtering | 13 configurations |
| PingPong (arXiv; venue unverified) | 500 human-authored dialogues, 100 per language combination | 5 code-switching combinations | 11–30 recruited native speakers per combination | about 11 models |

Sources: [TimlMemBench PDF](https://aclanthology.org/2026.findings-emnlp.507.pdf); [OP-Bench, arXiv:2601.13722](https://arxiv.org/abs/2601.13722) and [Anthology record](https://aclanthology.org/2026.emnlp-main.1168/); [LOCOMO-CONV PDF](https://aclanthology.org/2026.findings-emnlp.1289.pdf); [LoCoMo-Plus, arXiv:2602.10715](https://arxiv.org/abs/2602.10715); [Memora, arXiv:2604.20006](https://arxiv.org/abs/2604.20006); [MemBench, arXiv:2506.21605](https://arxiv.org/abs/2506.21605) with [Anthology ID 2025.findings-acl.989](https://aclanthology.org/2025.findings-acl.989); [HaluMem, arXiv:2511.03506](https://arxiv.org/abs/2511.03506); [TWIST, arXiv:2609.28575](https://arxiv.org/abs/2609.28575); [PingPong, arXiv:2601.17277](https://arxiv.org/abs/2601.17277).

Additional points:
- LoCoMo itself, the seed for four of the papers above, has ten conversations and 1,540 answerable questions (1,986 with the adversarial category). — [LOCOMO-CONV PDF](https://aclanthology.org/2026.findings-emnlp.1289.pdf)
- OP-Bench's own limitations section concedes English-only coverage and says norms of personalization may differ across cultures, an explicit opening that a Vietnamese resource can cite. — [arXiv:2601.13722](https://arxiv.org/abs/2601.13722)
- LoCoMo-Plus and TimlMemBench both list single-language or synthetic data among their limitations. — [arXiv:2602.10715](https://arxiv.org/abs/2602.10715), [TimlMemBench PDF](https://aclanthology.org/2026.findings-emnlp.507.pdf)

### Inferences
- Human-authored resources are accepted at smaller scale than synthetic ones, but the visible floor is in the low hundreds of dialogues, not tens. A credible ACL-main target for this proposal is on the order of 300–600 natively written families per language yielding a few thousand scored propositions, with full double annotation, per-layer κ, and at least 8–12 system configurations across three or more memory frameworks.
- On rigor the proposal's plan (two independent annotators on every item, a third adjudicator, per-layer agreement, clustered bootstrap, a non-LLM judged subset) exceeds what the accepted papers did; rigor is not the bottleneck, volume and time are.
- Timeline: the ARR deadline is 45 days after this audit and the proposal states that no data exist. The proposal's own milestone of 40–60 pairs by 27 November would produce a pilot the size of one ablation in DerivAudit (70 matched families). A Findings-level or workshop outcome is more plausible on that schedule than a main-track paper; a later ARR cycle would fit the required scale.

### Gaps
- No ACL/EMNLP/NAACL 2025–2026 resource paper specifically on pragmatics (as opposed to memory) was retrieved, so the calibration for a Discourse-and-Pragmatics-track submission rests on memory papers only.
- Venue claims for LoCoMo-Plus and Memora come from other papers' reference lists; their Anthology records were not opened.
- OP-Bench reports no chance-corrected agreement in the pages retrieved; whether an appendix table gives κ is unknown.
- The ARR rule on contemporaneous work (commonly described as a three-month window before submission) was not checked in this session. If it applies, AgentMemGate (6 Oct), Gated Memory (8 Oct), ConMem (24 Oct) and Memory Trap (5 Nov) fall inside the window before 4 January 2027, while DerivAudit (28 Sep), the user-perspective taxonomy (27 Sep), TWIST (23 Sep), PASB (July), MemTrace (June), MemGuard (May) and HaluMem (Nov 2025) fall outside it.

## 6. Verdict: novel, incremental, or anticipated

### Takeaway
Incremental as currently framed, with one genuinely unclaimed core. The memory-systems story (non-asserted content gets written, then corrupts later answers; measure it stage by stage with memory interventions) is anticipated piecewise by at least six 2025–2026 papers. The linguistics story (compositional scope operators, quotation and reported speech, Vietnamese person reference, human gold frames) was not found anywhere.

### Cited Findings
- Anticipated element 1, speculative content promoted to fact, with a contamination metric and a hedge-strength sweep. — [arXiv:2610.07707](https://arxiv.org/abs/2610.07707)
- Anticipated element 2, correct / distorted / absent memory arms with fixed downstream context. — [arXiv:2609.36130](https://arxiv.org/abs/2609.36130)
- Anticipated element 3, operation-level (extraction, update, answer) accounting. — [arXiv:2511.03506](https://arxiv.org/abs/2511.03506)
- Anticipated element 4, third-party and fictional attribution as a memory-intake failure in real user data. — [arXiv:2609.33623](https://arxiv.org/abs/2609.33623)
- Anticipated element 5, write-time versus read-time scope errors formalized and tested with memory arms. — [arXiv:2611.07554](https://arxiv.org/abs/2611.07554)
- Anticipated element 6, bilingual governed-memory benchmark with a clean-pool control at an ACL venue. — [2026.findings-emnlp.507](https://aclanthology.org/2026.findings-emnlp.507/)
- Open element: none of the above annotates operator nesting, embedded speakers or quotation, and none includes Vietnamese. — [arXiv:2610.07707](https://arxiv.org/abs/2610.07707), [arXiv:2609.36130](https://arxiv.org/abs/2609.36130), [2026.findings-emnlp.507 PDF](https://aclanthology.org/2026.findings-emnlp.507.pdf)

### Inferences
- Reasons for "incremental" rather than "anticipated": no paper found combines the pieces; the compositional-operator design and the Vietnamese angle are absent from all of them; and the proposal's plan for natural, double-annotated gold is stronger than the model-labelled or LLM-generated gold used by its nearest neighbours.
- Reasons against "novel": three of the proposal's four headline contributions (stage-wise accounting, controlled memory-state interventions, a write-gating baseline) each have a named precedent, and the proposal's related-work table omits the most damaging ones.
- What would move it toward acceptance: (1) recentre the title and claims on compositional pragmatics and cross-lingual person reference, treating the memory harness as the testbed; (2) cite and position against AgentMemGate, DerivAudit, HaluMem, MemGuard, MemAlign/ConMem, Memory Trap, MemTrace, CIMemories and PersistBench; (3) adopt AgentMemGate's "cautious extractor" and Gated Memory as strong baselines, since the first already suggests prompting alone removes much single-operator contamination; (4) drop or shrink the permission ledger; (5) show that nested or cross-lingual cases still fail when single-operator cases are solved — that result, positive or negative, is the publishable finding.
- What would sink it: a templated or translated dataset, single-operator items only, an LLM-judged endpoint without human adjudication, or a pilot-scale submission to the January cycle.

### Gaps
- The verdict depends on searches that could not reach OpenReview, Semantic Scholar or dblp; a concurrent ICLR 2027 or ARR submission on "pragmatic scope in agent memory" would not have been visible.
- No evidence was gathered on whether current frontier models actually fail on nested reported-speech cases; the proposal's central empirical bet is untested, and AgentMemGate's cautious-extractor result is a reason to expect small effects on simple cases.
