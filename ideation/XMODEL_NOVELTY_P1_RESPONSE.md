<!-- Cross-family review, saved verbatim. Reviewer model as self-reported: OpenAI GPT-6 (no finer version exposed). Run by the author on 2026-11-20 with the prompt and attachments in ideation/xmodel_kit/. Everything below this comment is the unedited response. -->

# **Independent Adversarial Prior-Art Review — P1 / ACL 2027**

**Proposal:** *Who Is “con”? Dyad-Anchored Person Reference When LLM Agents Write Memories in Vietnamese*\
**Target venue:** ACL 2027 via ACL Rolling Review — Discourse and Pragmatics\
**Search cutoff:** 20 November 2026\
**Materials reviewed:** `P1_PROPOSAL.md`, `P1_priorart_A.md`, `P1_priorart_B.md`, `P1_drift_scan.md`

## **Verdict: INCREMENTAL**

Conditional novelty

**I did not find a verified primary publication that anticipates the entire proposal.** In particular, I found no study directly testing how Vietnamese relational person terms are resolved through *embedded reported-speech dyads* when an LLM writes persistent memory.

However, substantial components already exist. Prior work covers person-attribution errors during dialogue rewriting, ambiguous-reference evaluation, source-aware memory consolidation, person-linked graph records, and downstream consequences of information loss.

**The defensible contribution is the specific linguistic–memory interaction and its controlled empirical demonstration—not a new general theory of memory attribution or a new provenance-aware storage architecture.**

This is a prior-art assessment, not an assessment of experimental success. The specification explicitly states that no data have been collected and no experiment has been run.

## **1. Searches run**

### **Sources and verification procedure**

I independently inspected primary records on arXiv, ACL Anthology, publisher websites, and original GitHub pull requests. I used the three earlier reports to identify candidates, but I did not accept their descriptions as verification.

| Source            | Search and verification performed                                                                                            | Coverage limitation                                                          |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| arXiv             | Exact paper IDs, title searches, overlapping-topic searches, accessible full-text HTML                                       | Search-engine recall is incomplete                                           |
| ACL Anthology     | Original paper records across coreference, pragmatics, dialogue summarization, kinship reasoning, memory, and Vietnamese NLP | Not an exhaustive machine scan of every volume                               |
| OpenReview        | Targeted public-web searches and direct attempts to access forum records                                                     | Direct forum and API access were restricted                                  |
| GitHub            | Original Graphiti PR discussions and searches for related implementation issues                                              | No pinned-version end-to-end execution                                       |
| Publisher records | Cambridge University Press, MDPI, *Tạp chí Ngân hàng*                                                                        | Some publisher full texts and institutional repositories remain inaccessible |
| Broader web       | English/Vietnamese terminology; adjacent HCI, software engineering, and multilingual memory                                  | Search indexing is not exhaustive                                            |

**Search date:** 20 November 2026. The review covers earlier work through that date, including 2026 conference proceedings and preprints.

### **Representative exact queries**

The following are search strings used during this independent pass, including searches that returned no directly anticipatory work:

```
"Vietnamese" "memory" "coreference" "kinship" agent language model 2026
"Vietnamese" "memory writer" "pronoun" "2026"
"dyad" "memory" "person" "LLM" "2026"
"kin terms" "reported speech" "memory" "LLM"
"person reference" "long-term memory" "Vietnamese"
"Vietnamese" "kinship" "coreference" dialogue
"terms of address" "dialogue" "coreference" Vietnamese
"Vietnamese" "reference resolution" kinship
"Vietnamese" "anaphora" "dialogue"
"Vietnamese" "pragmatics" "kinship" LLM
"Chinese" "zero pronouns" "conversation summarization" 2026
"indexical shift" "memory"
"perspective shift" dialogue third person transfer summarization
"memory" "wrong person" "later sessions" "coreference" LLM
"wrong person" "memory" "agent" "person reference" 2026
"entity conflation" "memory" "LLM agent" 2026
"cross-session" "entity merging" "memory" agent 2026
"coreference" "memory writes" LLM pronouns names
"speaker attribution" "memory consolidation" "Vietnamese"
"Vietnamese" "language" "chatbot" "kinship terms" "study" 2026
"Kinship Data Benchmark for Multi-hop Reasoning"
site:aclanthology.org/2026 "speaker attribution" "memory"
site:openreview.net/forum "Vietnamese" "kinship" "memory"
site:github.com/getzep/graphiti "dedup_helpers.py" "_normalize_name_for_fuzzy"
```

Additional searches used Vietnamese expressions including `xưng hô`, `trợ lý ảo`, `đồng tham chiếu`, and `ChatGPT`.

I also opened and checked the original records for the principal works cited by the earlier reports: **DIAL-SUMMER, AmbiCoref, Correct-Detect, Vietnamese narrative coreference, the WMT 2026 dyadic-profile study, FACTWASH, AuthMem-Bench, CASK, Manufactured Confidence, and LAPSE**.

This was a new targeted hunt rather than a complete replication of the earlier reports' approximately thousands of OpenReview submissions and ACL bibliographic entries. Their search counts must not be treated as counts independently reproduced here.

## **2. Closest works — verified primary records**

Verification key: **[FT]** full text accessible and inspected; **[ABS]** original abstract inspected; **[SRC]** original code repository, issue or pull-request record inspected.

### **A. Strongest threats from persistent-memory research**

**1. CogMem — *From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-Term Dialogue***

**Identifier:** ACL Anthology `2026.emnlp-main.1014`; arXiv:2610.11314.\
**Verification:** [FT] arXiv article and [ABS] official EMNLP 2026 record.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org+1



**What it already does:** CogMem employs a Person–Event–Concept–Claim–Fact graph schema. Claim nodes explicitly preserve the source and target of subjective statements; event and fact nodes support other types of knowledge. Ingestion retains source-turn information, and consolidation maintains provenance-aware records.

**Exact delta:** It does not evaluate Vietnamese kin terms as person-reference expressions, embedded reported dyads, unexpressed possessors, diacritic-sensitive identity mistakes, or native-reader uncertainty distributions.

**Does the delta matter to an ACL referee?** **Very much.** This is the strongest additional threat to the proposal's C3 storage contribution.

A general claim that existing memory graphs cannot preserve who said something, or that introducing claim-source links is novel, would be indefensible. The proposed improvement must be specifically **relational-person anchor resolution and preservation**, not provenance-aware memory in general.

**2. SpeakerMem-R1 — *Speaker-Centered Dual-Track Memory for Multi-Party Dialogue***

**Identifier:** arXiv:2609.26780.\
**Verification:** [ABS] original arXiv record.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



**What it already does:** Maintains speaker-labelled verbatim messages alongside person-level and group-level derived memories. Its stated design objectives include distinguishing who spoke, whom an utterance concerns, and how participants perceive each other.

**Exact delta:** Speaker identity is available through dialogue labels; the work does not establish the referent of Vietnamese *anh/chị/con/em* within a separately reported dyad.

**Referee significance:** **High.** This anticipates person-centred memory writing as a systems problem. The paper must clearly distinguish *speaker identity* from *referent identification inside an embedded speech event*.

**3. AuthMem-Bench — *When Memory Becomes Authority***

**Identifier:** arXiv:2608.01679.\
**Verification:** [FT] original arXiv full-text HTML.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



**What it already does:** Uses paired histories that preserve the focal proposition but change the authority of its source. One setting promotes a third-party report into an apparent user fact. It evaluates wrongful promotion and authorized retention across multiple consolidators and backbones.

**Exact delta:** Its contrasts operate primarily over source channels and authority boundaries, not Vietnamese person-reference ambiguity inside the same user's utterance.

**Referee significance:** **Very high.** The proposal's paired tests, “wrongly stored versus correctly retained” accounting, and source-promotion framing are adaptations of existing methodology.

**4. CASK — *Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory***

**Identifier:** arXiv:2610.09008.\
**Verification:** [FT] original arXiv HTML.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



**What it already does:** Treats persistent memory admission as a discourse-ownership problem: information belongs to an actual world, hypothetical branch, or speaker's belief. It uses scope-aware commit rules rather than promoting every proposition into durable fact.

**Exact delta:** Not focused on Vietnamese kin-term reference, the identification of a proposition's subject through a reported speech event, or matched comprehension-versus-write measurements.

**Referee significance:** **High.** The proposal cannot claim to have introduced the idea that memory writes detach propositions from their original discourse frames.

**5. FACTWASH and Manufactured Confidence**

**Identifiers:** arXiv:2608.03372 and arXiv:2606.29279.\
**Verification:** [FT] primary arXiv full texts.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



**What they already do:** Demonstrate or detect the removal of attribution, hedging and epistemic qualifications during memory or text rewriting. They investigate memory systems including Mem0 and LangMem, and consequences for subsequent decisions.

**Exact delta:** Their central examples concern epistemic status, hearsay and authority—not resolving whether a Vietnamese kin term denotes the user, another participant, or a reported addressee.

**Referee significance:** **High for the motivation, moderate for the specific contribution.** They establish that losing a discourse frame at write time can affect later behaviour. They also provide required intervention baselines; a simple prompt might improve the proposed system more than the specification predicts.

**6. LAPSE — *Memory Consolidation Flattens the Temporal Shape of User Facts***

**Identifier:** arXiv:2609.36457, version 2 dated 11 November 2026.\
**Verification:** [FT] original arXiv record and accessible article.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



**What it already does:** Uses matched linguistic contrasts and evaluates native writers in Mem0, Graphiti and Letta, including consequences for readers that receive the resulting records.

**Exact delta:** The manipulated distinction is grammatical aspect, not relational person reference or reported-dyad anchoring.

**Referee significance:** **High methodologically.** Matched language pairs, native-framework evaluation and write-versus-read analysis are already part of the literature.

### **B. Strongest threats from discourse and pragmatics**

**7. DIAL-SUMMER — *A Structured Evaluation Framework of Hierarchical Errors in Dialogue Summaries***

**Identifier:** arXiv:2602.08149.\
**Verification:** [FT] original arXiv article.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



**What it already does:** Explicitly studies the conversion from first-/second-person dialogue into third-person summaries and categorizes errors including speaker misattribution and viewpoint distortion.

**Exact delta:** English dialogue summarization, not persistent memories; no dedicated test of Vietnamese relational person forms under embedded reported speech.

**Referee significance:** **Very high for C1.** The proposed “format gap” is not an entirely new kind of phenomenon. The novelty must lie in its **controlled differential effect for Vietnamese kin terms**, not merely in demonstrating that third-person rewriting causes mistakes.

**8. AmbiCoref and Correct-Detect**

**Identifiers:** `2023.findings-eacl.75` and `2025.emnlp-main.1527`.\
**Verification:** [ABS] original ACL Anthology records.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aclanthology.org\&sz=32)

ACL Anthology+1



**What they already do:** AmbiCoref compares human uncertainty and model behaviour on deliberately ambiguous referential constructions, including minimal-pair reporting contexts. Correct-Detect studies the tension between choosing a coreference interpretation and recognizing that the interpretation is ambiguous.

**Exact delta:** English pronoun coreference, not memory writing, Vietnamese relational terms, or error persistence.

**Referee significance:** **Very high for C2.** Both the diagnostic construction strategy and the underlying ambiguity-versus-commitment problem have precedents. Claiming discovery of either would invite a strong novelty objection.

**9. *He Said, She Said: Style Transfer for Shifting the Perspective of Dialogues***

**Identifier:** `2022.findings-emnlp.355`.\
**Verification:** [ABS] original ACL Anthology record.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aclanthology.org\&sz=32)

ACL Anthology



**What it already does:** Defines dialogue perspective shifting into third-person text and identifies coreference resolution as a necessary operation.

**Exact delta:** Does not evaluate long-term memory or Vietnamese reported-dyad kin-term reference.

**Referee significance:** **High.** This is an older, explicit precedent for the processing step the proposal describes as hidden in English.

**10. *Coreference Resolution for Vietnamese Narrative Texts***

**Identifier:** arXiv:2504.19606; corresponding ACL Anthology publication `2024.paclic-1.139`.\
**Verification:** [FT] original arXiv article.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



**What it already does:** Supplies an annotated Vietnamese person-coreference resource based on first-person narratives and evaluates GPT-3.5 and GPT-4.

**Exact delta:** Narrative text rather than assistant dialogue, no explicit reported-dyad intervention, and no persistent-memory write task.

**Referee significance:** **High.** The study disproves any broad assertion that Vietnamese person-reference evaluation with LLMs has never been done. It is an important external baseline, but not an anticipation of C1.

**11. *Evaluating Pragmatic Appropriateness in English–Vietnamese Machine Translation with Dyadic Profiles***

**Identifier:** `2026.wmt-main.16`.\
**Verification:** [ABS] original ACL Anthology record.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aclanthology.org\&sz=32)

ACL Anthology



**What it already does:** Tests how explicit sender–recipient relationship information changes the pragmatic appropriateness of Vietnamese person reference in translation, including role reversals.

**Exact delta:** Evaluates generation of appropriate address forms, not the recovery of a reported speaker's intended person referent while constructing memory.

**Referee significance:** **High.** Manipulating a dyadic relationship is not itself novel. What remains distinctive is **mapping reference through an embedded speech event rather than the outer conversation's dyad**.

### **C. Additional work missed or insufficiently covered in the earlier reports**

**12. *An Empirical Study on Enhancing Large Language Models for Long-Term Conversations in Korean***

**Identifier:** DOI:10.3390/app16073175, published 25 March 2026.\
**Verification:** [FT] original *Applied Sciences* article.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.mdpi.com\&sz=32)

MDPI



**What it already does:** Builds Korean-language multi-session conversation data, distinguishes persona from episode memory, and evaluates summarization, memory update and response generation.

**Exact delta:** Does not isolate kinship-based reported-person anchoring or the proposed Vietnamese comparisons.

**Referee significance:** **Moderate.** It directly defeats the broad positioning that long-term dialogue memory research is almost exclusively English or Chinese. A multilingual memory study in Korean already exists.

**13. Nguyen and Sim — *Stability and Change in Heritage Grammar: Variable Object Expression across Generations of Canberra Vietnamese***

**Identifier:** Cambridge University Press primary publication, 4 November 2026.\
**Verification:** [FT] original *Language Variation and Change* article.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.cambridge.org\&sz=32)

Cambridge Core



**What it already does:** Analyzes naturally occurring Vietnamese reference and explicitly treats kin terms, personal names and pronouns as functionally related reference forms. It reports person-sensitive distributional effects and coreferentiality patterns.

**Exact delta:** Human–human conversation and heritage-language variation, not user–assistant memory writing or embedded-dyad resolution tests.

**Referee significance:** **High for ACL Discourse and Pragmatics.** The linguistic mechanism has deep prior grounding. A contribution can be made in computational evaluation, but the paper must not frame Vietnamese relational person reference as a newly discovered property.

**14. *Nâng cao chất lượng Chatbot chăm sóc khách hàng tại các ngân hàng thương mại Việt Nam***

**Identifier:** *Tạp chí Ngân hàng*, 25 March 2024, original [publisher record](https://tapchinganhang.gov.vn/nang-cao-chat-luong-chatbot-cham-soc-khach-hang-tai-cac-ngan-hang-thuong-mai-viet-nam-10533.html?utm_source=chatgpt.com).\
**Verification:** [FT] original Vietnamese-language article.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://tapchinganhang.gov.vn\&sz=32)

Tạp chí Ngân Hàng



**What it already does:** Tests two Vietnamese banking chatbots with a set of 20 address-form variation questions, including *chú*, *bác*, and *cô*, and reports that they do not adapt their address forms satisfactorily.

**Exact delta:** Scripted chatbot testing, not a corpus measuring how real users naturally address assistants, and no memory writing or reported speech.

**Referee significance:** **Moderate but important.** The earlier drift scan's broad assertion that no empirical work exists on Vietnamese chatbot addressing is too strong. The narrower C0 claim—frequency of kin terms inside third-party reports in elicited user–assistant conversations—remains unanticipated in the records I verified.

**15. KinshipQA — *Kinship Data Benchmark for Multi-hop Reasoning***

**Identifier:** `2026.findings-emnlp.274`; DOI:10.18653/2026.findings-emnlp.274.\
**Verification:** [ABS] original ACL Anthology record.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aclanthology.org\&sz=32)

ACL Anthology



**What it already does:** Evaluates LLM compositional reasoning across seven anthropological kinship systems, including culturally dependent term interpretation and multi-hop relationships.

**Exact delta:** Kinship semantics and reasoning in artificial problems, not Vietnamese kin terms serving as conversational person references or memory-record ownership.

**Referee significance:** **Moderate.** The paper should separate *reasoning about family relationships* from *resolving who a relational expression refers to in discourse*.

## **3. Claim-by-claim anticipation status**

These labels address whether **the specific claim in §5** was found previously investigated or established. They do not indicate whether the proposal's predicted result will hold experimentally.

| Claim                                                                                                                                  | Status                 | Adversarial assessment                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **C0** — At least 5% of third-party-mention turns in elicited Vietnamese user–assistant conversations contain kin terms inside reports | **Not found**          | Existing Vietnamese chatbot-address testing and human–human linguistic corpora partly predate the motivation, but neither gives this exact rate or denominator. The 5% hypothesis remains completely unverified.                                                    |
| **C1** — Larger writing-versus-comprehension person-assignment gap on Vietnamese kin-term items than on explicit-name/English controls | **Not found**          | Dialogue perspective-shift errors and Vietnamese coreference are established, but I found no verified primary test of this exact information-matched interaction in memory writers. It is one of the two strongest surviving novelty claims.                        |
| **C2** — Writers diverge from native-rater distributions, including persistent assignment when raters frequently cannot tell           | **Partly anticipated** | AmbiCoref, Correct-Detect and related ambiguity work establish the general behaviour and method. What survives is comparing graded human readings with actual stored person assignments and pricing retention within memory systems.                                |
| **C3** — Kin-term-specific store conflation persists after prompt localization but is removed by schema/dedup modifications            | **Partly anticipated** | CogMem and SpeakerMem-R1 already provide structured person/source-aware memory; the general schema remedy is not novel. The proposed Vietnamese error decomposition and evidence that prompt-only localization fails remain unverified and potentially distinctive. |
| **C4** — Translate-then-extract shifts errors toward wrong-person assignments without improving total error                            | **Not found**          | Dyad-aware translation is studied, but this exact translation-pivot error-mix prediction was not found. Importantly, this is a risky hypothesis: translation could instead improve resolution.                                                                      |
| **C5** — Wrong-person writes yield additional later-session wrong-person answers, removed by oracle-record substitution                | **Partly anticipated** | The broader causal chain “faulty memory write → downstream error” is established by AuthMem-Bench, Manufactured Confidence and LAPSE. The wrong-person-specific three-way intervention is not found.                                                                |

### **Most valuable unanticipated claim**

**C1 is currently the clearest candidate for a genuinely differentiating scientific result.**

A particularly persuasive finding would be:

- On the same examples, a backbone correctly interprets the intended person when asked directly.
- When asked to produce a standalone memory record, the same backbone assigns that fact to the wrong person.
- The effect remains larger for Vietnamese kin terms than for **difficulty-matched non-kin constructions**, not merely easier explicit-name controls.
- The difference persists when the model receives a Vietnamese dyad-resolution instruction.

That would isolate a meaningful effect associated with *converting context-bound reference into a committed record*, rather than merely showing Vietnamese coreference is difficult.

### **C2 measurement concern**

The proposal specifies at least **eight native raters per item** and discusses readings chosen by **less than 10%** of raters.

With eight raters, one vote represents 12.5%; a reading below 10% is effectively a reading with **zero votes**. This makes the metric sensitive to sample size and rare alternative interpretations. An adversarial referee could also question how a deterministic writer's single record is converted into “probability mass.”

The scoring protocol should therefore explicitly define repeated stochastic runs or a categorical empirical output distribution, report sensitivity to the number of raters, and avoid equating zero observed votes with an impossible interpretation.

## **4. The Graphiti claim requires a narrower formulation**

The earlier reports flag Graphiti's ASCII-centric fuzzy-name normalization. I independently opened both original pull requests:

- **getzep/graphiti PR #1357**, opened March 2026: non-ASCII/CJK names fail a fuzzy-deduplication fast path.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

  GitHub

- **getzep/graphiti PR #1850**, opened September 2026: proposed broader non-Latin name handling.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

  GitHub



Both appeared open when checked.

These records establish that a non-ASCII normalization problem was already publicly identified. They **do not demonstrate an end-to-end Vietnamese false merge**.

This distinction matters because a faulty normalization path can cause a missed candidate match, a spurious candidate match, or merely extra work in a fallback path. None of those outcomes automatically establishes that Graphiti has persisted two distinct people as one entity.

**Verdict on the engineering subclaim:** the suspected mechanism has prior art; the Vietnamese-specific false-merge consequence is **not found**, but is currently an unproven prediction rather than an observed result.

To support C3, the paper needs pinned-commit tests with actual end-to-end entity resolution and stored graph contents—not just string-normalization examples.

## **5. Independent novelty assessment**

### **What has already been anticipated**

The following should not be claimed as novel contributions:

- Converting first-/second-person dialogue into third-person text requires coreference resolution.
- Dialogue rewriting can produce speaker or viewpoint attribution errors.
- LLMs can commit to an interpretation when human readers recognize ambiguity.
- Persistent-memory consolidation can erase source, hedge or temporal information.
- Memory systems can preserve provenance, person-linked claims and speaker-labelled records.
- Controlled linguistic minimal pairs and native-framework writer evaluations can expose information loss.
- Downstream agents may act incorrectly because stored memory omitted important context.

These propositions are supported by multiple independently verified primary records cited above.

### **What I did not find anticipated**

I found no verified primary publication jointly implementing and evaluating all of the following:

1. A **Vietnamese reported-speech dyad** distinct from the outer user–assistant dyad.
2. Resolution of a kin term or unexpressed possessor through that reported dyad.
3. The **same-backbone, same-context comprehension-versus-memory-write comparison** with matched non-kin controls.
4. A human distribution over admissible referents, including an explicit “cannot tell” option, compared with persistent person assignments.
5. An end-to-end analysis distinguishing reference resolution, record construction, person consolidation and downstream effects for those same cases.

That conjunction is the proposal's remaining credible novelty. It is not evidence that nobody has studied any of the components individually.

## **6. Verdict for ACL 2027**

**INCREMENTAL — with a plausible route to a genuinely novel empirical contribution.**

My reason for choosing *incremental* rather than *novel* is that the conceptual machinery and much of the evaluation design have already appeared in the literature. The strongest additional find, CogMem, substantially narrows the defensible schema contribution. The older discourse literature likewise narrows the claim that dialogue-to-memory person resolution is an entirely new problem.

I do **not** choose *anticipated*, because no verified work reproduces the proposal's defining Vietnamese embedded-dyad memory experiment or demonstrates its main C1 contrast.

For ACL 2027's Discourse and Pragmatics area, the paper's scientific contribution should be framed as:

> A controlled study of how relational person reference anchored to embedded speech events behaves when LLMs transform Vietnamese dialogue into persistent, context-independent records, separating comprehension error from record-construction and consolidation error.

The proposal should proceed only conditionally. The pilot needs to show a nontrivial C1 effect and a genuinely separate store-level C3 effect. If the writing gap disappears after difficulty matching, or the entire problem is resolved by a simple dyad-aware prompt, the project becomes a narrower Vietnamese reference-resolution evaluation rather than a strong memory-systems contribution.

### **Changes I would require before an ACL submission**

The related-work section must add **CogMem**, **SpeakerMem-R1**, the **Korean multi-session-memory study**, the recent Cambridge Vietnamese reference study, and the 2024 Vietnamese chatbot-address evaluation. They address gaps or broad assertions that the attached reports leave vulnerable.

The contribution statement should also distinguish *a new computational diagnosis of relational reference at memory-write time* from older ideas about source attribution, third-person perspective shifting and provenance-aware graph storage.

## **7. What I could not search or conclusively verify**

**OpenReview is the largest outstanding blind spot.** Direct forum access and the available API route were restricted during this pass. I attempted public-web searches, but could not independently inspect the full text, reviews, attachments or current revisions of all relevant ICLR 2027 and ARR 2026 submissions. The earlier reports contain candidate OpenReview records, but I have not treated an inaccessible listing as verified full-text evidence.

Other limitations include incomplete coverage of Google Scholar, Semantic Scholar and OpenAlex; some ACM and IEEE full-text collections; unpublished or institutional theses; Vietnamese university and national-journal repositories; Japanese, Korean, Chinese and Thai local-language venues; and private or non-public ARR submissions.

I also did not run Mem0, LangMem or Graphiti on the proposed Vietnamese cases, and therefore cannot validate the empirical predictions, affected software versions or reported-dyad failure rates.

These are meaningful search limitations. **Failure to locate a matching work is not proof of novelty.** The conclusion is limited to independently verified primary records discoverable through this pass, together with the uploaded reports treated as untrusted leads.

**Model: GPT-6.** A more specific internal model version or build identifier is not available to me.