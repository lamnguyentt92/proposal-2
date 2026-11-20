<!-- Cross-family review, saved verbatim. Reviewer model as self-reported: OpenAI GPT-6 (no finer version exposed). Run by the author on 2026-11-20 with the prompt and attachments in ideation/xmodel_kit/. Everything below this comment is the unedited response. -->

Independent Referee Report — ACL 2027
Area: Discourse and Pragmatics · Review date: November 20, 2026 · Stage: Research proposal, before experimentation

Proposal: Who Is “con”? Dyad-Anchored Person Reference When LLM Agents Write Memories in Vietnamese

Evaluation basis: P1_PROPOSAL.md, P1_VENUES.md, both prior-art reports, the novelty drift scan, and independently checked publications.
Overall assessment
Provisional verdict: Weak Reject
Idea-stage assessment, not a prediction of experimental results

The proposal has a genuinely interesting linguistic core: resolving Vietnamese relational person terms using the speaker–addressee dyad of an embedded speech event, rather than automatically assigning them to the current user–assistant conversation.

I do not regard that core as already anticipated by the papers I checked. However, I am not yet convinced that the proposed experiments will establish a distinctive contribution about persistent agent memory, rather than rediscovering referential ambiguity and perspective-shift errors in another application.

The distinction is decisive. A strong Vietnamese discourse-resolution benchmark is potentially publishable, but it is not automatically an ACL main-track contribution about memory writing. The eventual paper must show what the memory operation adds causally beyond ordinary text interpretation, third-person rewriting, and decontextualization.

I would retain the idea for empirical validation, but I would not endorse the current formulation as a clear main-track submission.
1. Scores (1–5)
Scores assess the proposal's potential and design, not observed results. Higher is better.
Dimension	Score	One-line justification
Novelty	4/5	Dyad-anchored Vietnamese reference at memory-write time appears distinctive; ambiguity diagnostics and viewpoint-shift errors have substantial precedents.
Significance	3/5	Incorrect person attribution in persistent memory is consequential, but its prevalence in actual Vietnamese assistant conversations is unknown.
Technical depth	3/5	The factorial comparisons and error decomposition are meaningful, but the proposed interventions are mainly prompts, schemas, and deduplication changes.
Soundness potential	2/5	Causal identification is vulnerable to task-format confounds, underdetermined references, and defects in the proposed distributional metrics.
Evaluation	3/5	Strong diagnostic controls, graded gold, and explicit refutation criteria; weak ecological sampling and no budget-matched episodic-memory baseline.
Clarity	4/5	Explicit claims, outcomes, and kill conditions are excellent; several metrics and the meaning of a memory-specific effect remain underspecified.
Venue fit	4/5	The linguistic question fits Discourse and Pragmatics, provided the paper foregrounds reference interpretation instead of framework engineering.

Unweighted average
3.29/5




The key limitation is not that the proposal lacks a new model or theorem. ACL accepts substantive empirical and linguistic contributions. The problem is that the current design could produce statistically significant results without identifying the claimed memory-specific mechanism.
2. Likely reasons for rejection, ranked
R1. The paper may fail to isolate a memory-specific phenomenon
Severity: Critical · Affects C1, C3, C5

This is my principal concern.

The hypothesis that converting dialogue into third-person records introduces person-attribution errors has a close conceptual predecessor in DIAL-SUMMER (arXiv:2602.08149), which explicitly studies speaker misattribution and viewpoint distortion during dialogue summarization. 

arxiv.org

The proposal recognizes this and includes a one-shot third-person summary control. That is appropriate, but insufficient by itself.

Suppose the results are:
Condition	Wrong-person rate (hypothetical)
Direct comprehension	5%
Third-person summary	17%
Memory extraction	18%
Persistent memory after consolidation	19%

Even if C1 is statistically significant, the 13-point extraction-versus-comprehension gap would predominantly reflect a generic perspective-transformation cost. Very little would be attributable to persistent memory.

The relevant decomposition is:
\[
E_{\text{memory}} =
E_{\text{comprehension}}
+\Delta_{\text{rewriting}}
+\Delta_{\text{consolidation}}
\]

This is conceptual accounting, not an assumption that those terms are independently additive. The proposal must identify the increments experimentally.

The eventual paper needs a significant, practically meaningful \(\Delta_{\text{consolidation}}\), or a distinct persistence-related failure that an ordinary summarization pipeline does not exhibit.

Rejection trigger: C1 is positive, but the summary control performs similarly to memory extraction and no convincing additional store-level harm is established.
R2. The human gold standard and C2 metric are not yet sound
Severity: Critical · Affects C1, C2

C2 defines a problematic reading as one chosen by fewer than 10% of native raters. The evaluation proposes at least eight raters per diagnostic item.

If each rater selects one categorical reading, with eight raters the smallest nonzero observed proportion is:
\[
\frac{1}{8}=12.5\%.
\]

Therefore, a reading selected by fewer than 10% of raters is necessarily one selected by zero raters.

This creates a potentially degenerate metric. An in-sample human comparator has zero observed mass on the zero-vote class by construction, while an independent writer may produce a linguistically plausible reading absent from only eight observations.

The reported divergence can therefore be inflated by sparse estimation rather than genuine misinterpretation.

The proposal should use an independently held-out rater group or cross-fitted estimates, plus sensitivity analysis of the threshold. It must also operationally distinguish:
- A linguistically impossible reading.
- A plausible but minority reading.
- A genuinely underdetermined reference.
- A rater who cannot decide despite sufficient contextual evidence.
These are not equivalent errors.

The distinction matters because AmbiCoref and Correct-Detect already establish substantial human–model differences in ambiguity handling. The novel result must be better calibrated than those comparisons. 

ACL Anthology+1

R3. Natural occurrence is not established by scripted elicitation
Severity: Major · Affects C0 and significance

Study 0 asks Vietnamese speakers to converse with an assistant about family and work using open scenarios.

These topics may directly induce kin terms and reported speech. Consequently, a rate exceeding the preset 5% threshold may reflect the experimental scenario rather than ordinary assistant use.

The denominator—turns mentioning third parties—also makes the rate sensitive to topic selection.

I would require a genuinely open-topic elicitation arm, separated from the family/work-enriched diagnostic arm. The authors should report both proportions and avoid presenting either as the prevalence in naturally occurring conversations.

A threshold of 5% is usable as a preregistered decision rule, but it does not establish scientific or practical significance on its own.
R4. The strongest extractor and a simple prompt may erase the proposed effects
Severity: Major · Affects C1–C3

A particularly damaging outcome is that a frontier model, given a clear dyad-resolution instruction and an explicit abstention option, approaches native-rater performance.

That would not make the linguistic phenomena uninteresting. It would make the memory-specific failure claim much weaker.

This concern is supported by prior results showing that targeted extraction instructions can reduce some memory-rewriting errors. Manufactured Confidence (arXiv:2606.29279) reports a hedge-preserving intervention rather than requiring an entirely new architecture. 

arxiv.org

The current proposal already anticipates this risk through K2. I agree with retaining that criterion.
R5. C3 bundles two potentially unrelated mechanisms
Severity: Major · Affects causal interpretation

Dyad capture, ambiguous kin nouns, and diacritic-sensitive fuzzy name matching are not the same phenomenon.

I independently inspected Graphiti's dedup_helpers.py. Its fuzzy-normalization path removes characters outside an ASCII-restricted character class, while its entity-resolution logic includes exact matching and a separate fuzzy similarity path. 

GitHub+1

That establishes a plausible Unicode-dependent collision mechanism, not yet a demonstrated end-to-end Vietnamese identity merge.

If the paper mixes false merges caused by this engineering behavior with semantic misresolution of con, mẹ, or anh, a referee could reasonably conclude that C3 combines an NLP problem with a separate implementation defect.

Required separation: report reference-resolution errors, entity-identity merges caused by relational anchors, and Unicode/name-normalization collisions as three distinct outcomes.
R6. Limited practical contribution if safe abstention simply discards facts
Severity: Major · Affects C2–C4

A system can achieve an excellent wrong-person rate by declining to store uncertain information.

This is not automatically good memory.

Report an explicit risk–coverage frontier: wrong-person attribution versus correctly retained information, with actual retrieval and answering quality.

The proposal mentions licensed-fact retention, but the decision criteria emphasize elimination of errors more than preservation of usable memory.

The decontextualization literature already provides both meaning-preserving rewriting and selective rejection as established approaches. 

ACL Anthology+1

R7. Secondary concerns
The natural and diagnostic layers may differ in difficulty, syntax, regional conventions, and degree of ambiguity. The English controls cannot always preserve the social-indexical semantics of a Vietnamese kin term. Three backbones improve robustness but do not automatically establish generality.

Technical and resource feasibility are otherwise credible: the proposed systems are inspectable, API-based comparisons are implementable, and the stated annotation volume is feasible with appropriate quality control. The main resource concern is statistical precision: approximately 600–1,200 diagnostic variants would require at least 4,800–9,600 rater judgments at eight ratings each, yet still leave only eight judgments per item's reading distribution.

The fictional-persona design reduces privacy risks. Participants and raters still require informed consent, fair compensation, secure handling of elicited conversations, and care not to release unintentionally disclosed personal information. None of these ethical requirements appears to be an intrinsic blocker.

3. Strongest missing baseline
Budget-matched, context-preserving episodic memory with retrieval.

This is the single comparison I would demand.

The specification includes a full-dialogue reader and a contextualize-then-extract frontier model. Neither is equivalent to an actual persistent memory system that stores the original utterances without rewriting them.

Use a simple episodic store that preserves the utterance text, original speaker, conversation identifier, and turn boundaries. At the later session, retrieve relevant episodes and let the same backbone resolve the question, with abstention available.
Required comparison
A — Extracted memory
Dialogue → resolve referents → write atomic records → consolidate → retrieve → answer

Early, persistent commitment to entity identity


B — Episodic memory
Dialogue → store original episodes → retrieve → resolve referents → answer

Reference resolution postponed until retrieval



Hold constant the backbone, retrieval corpus access, question set, token budget where feasible, and measured storage/retrieval costs. Report retrieval misses separately from reference errors.

This is not an invented baseline category. Manufactured Confidence (arXiv:2606.29279) used a verbatim-turn vector-retrieval control to distinguish errors introduced by rewriting from those occurring at retrieval and decision time. I opened the full text and checked this comparison. 

arxiv.org

Why this matters: If a simple, similarly budgeted episodic store performs as well as the proposed anchor-aware schema, the claimed design contribution becomes less compelling. Conversely, if the new schema retains the benefits of compression while approaching the correctness of episodic storage, that is a substantially stronger result.
4. Experiment most likely to produce a negative result
C4 — The English pivot relocates errors without lowering total error.

My prediction is that the second half of C4 is especially vulnerable: a strong document-level Vietnamese-to-English translation may reduce the combined wrong-person and unresolved-reference rate relative to direct Vietnamese extraction.

C4 requires two outcomes simultaneously: a particular change in the error distribution and failure of translation to improve the total error rate. There is no necessary linguistic reason both must hold.

A sufficiently capable translator might make the reported dyad explicit, preserve attribution, or correctly substitute names for contextual person forms. This could make English extraction easier rather than more error-prone.

The experiment could therefore find:
- Translation decreases both wrong-person errors and unresolved references.
- Translation improves accuracy but loses some relational nuances.
- Translation and direct Vietnamese extraction perform comparably.
Any of these would undermine the stated C4 prediction.

Consequence: This would not by itself kill the project. It would make translate-then-extract a credible mitigation and require C4 to be dropped as a headline claim, exactly as the proposal commits to doing.

It would also weaken the argument that preserving Vietnamese relational structure explicitly inside a memory schema is necessary for good performance. C1 and C3 would have to carry that argument independently.
5. Boundary cases and counterexamples for every Section 5 claim
The following are counterexamples to the specific claims, not arguments that the underlying linguistic problem does not exist.
Claim	Condition under which it fails	Condition under which it becomes vacuous or uninformative
C0 — Natural occurrence	Fewer than 5% of eligible turns contain the target construction.	Family/work scenarios elicit the construction artificially; the measured frequency says little about open-domain assistant use.
C1 — Format gap	Writing and comprehension errors are equivalent after matching difficulty, prompts, and output/abstention options.	The difference comes entirely from third-person rewriting, or controls have a ceiling effect that mechanically favors a larger Vietnamese gap.
C2 — Divergence from native readers	Writers match held-out human distributions and abstain appropriately on underdetermined items.	The 10% rare-reading threshold selects zero-vote readings with eight raters, or the native writer is structurally forced to select a person even when the input contains no recoverable answer.
C3 — Store-level conflation	There is no excess kin-related conflation, or the localized instruction resolves both record and consolidation errors.	The apparent improvement is achieved by dropping uncertain facts, or the measured merge is caused entirely by a separate name-normalization defect rather than relational person reference.
C4 — English pivot	Translation reduces the combined error rate below direct Vietnamese extraction or fails to produce the predicted shift in error types.	Wrong assignment and safe non-resolution are aggregated as equivalent costs, masking opposite effects on downstream utility.
C5 — Persistence	A wrong record does not increase wrong-person answers, or native versus oracle records produce similar downstream outcomes.	The later question is constructed so that it can only repeat the planted record, making the oracle correction and consequent improvement essentially predetermined.

Three particularly important counterexamples
Counterexample A — A genuinely unresolved kin term

Consider a context in which two people could each plausibly be the intended referent of mẹ, and the available dialogue does not identify the possessor.

A writer that stores an unresolved relational reference has not necessarily failed. Neither has a reader that says it cannot determine the referent.

For this case, the correct target is not an entity ID but a set or distribution of admissible readings.

The proposal must distinguish failure to resolve a resolvable reference from appropriate abstention on an unresolvable one.

Counterexample B — Correct resolution, incorrect identity merging

Suppose the extractor correctly resolves two references to different individuals, but Graphiti's fuzzy entity-resolution path later merges their names.

That is a consolidation error, not evidence that Vietnamese dyad anchoring is poorly understood.

A diacritic-safe normalization fix may solve it without using a dyad-aware record schema. This result is still useful engineering evidence, but it cannot support the central linguistic mechanism by itself.

Counterexample C — Correct memory with no premature resolution

Consider a system storing an original utterance, its speaker, and its reporting context. It postpones identifying con until the information is actually requested.

The central premise that a persistent record must force an immediate person assignment does not apply to this design.

This is why the claim should be about particular decontextualizing memory-write architectures, not persistent memory in general.

6. Kill argument — strongest case for rejection
Committed argument: The paper does not establish an independently identifiable memory-specific contribution. Approximately 200 words.
The paper claims to discover a distinctive failure of persistent LLM memory involving Vietnamese relational person reference. However, its empirical design does not establish that memory is the source of the failure. C1 compares an explicit referent-comprehension question with a record-generation task, so any observed gap may reflect prompt salience, output constraints, or the familiar difficulty of decontextualization. The proposed third-person summary control further threatens the claim: if summaries exhibit the same errors, the result is not memory-specific.

C2 largely repackages established findings about model overcommitment under ambiguous coreference. C3 combines referent-resolution mistakes with an implementation-specific entity-deduplication problem, without demonstrating a common linguistic mechanism. C5 establishes that storing an erroneous fact can affect later answers, but this is a predictable consequence of the injected error, not an independent scientific contribution.

The remaining novelty is a Vietnamese dataset containing challenging examples of perspective-dependent kin-term reference. Such a resource could be valuable, but its naturally occurring frequency and generality are not established. Without a controlled demonstration of additional error introduced specifically by persistent memory operations, beyond ordinary rewriting and referent resolution, the paper overstates its contribution. I would therefore reject it as a language-specific ambiguity benchmark presented under an insufficiently supported memory-systems narrative.

This argument is grounded in the distinction between coreference ambiguity, perspective-shift rewriting, and memory rewriting established in AmbiCoref, DIAL-SUMMER, and Manufactured Confidence. 

ACL Anthology+2

It is the argument I would expect a skeptical reviewer to defend during discussion.
7. What would make this a clear accept?
I would change my assessment to Accept or Strong Accept if a completed paper established all four results below.

A. Demonstrated linguistic and ecological relevance

Independently validated native-speaker judgments show that dyad anchoring changes the intended referent. The relevant constructions occur at a meaningful rate in a minimally prompted conversation sample, not just in author-designed examples.




B. A robust causal decomposition

Across several backbones, a statistically and practically meaningful writing gap survives difficulty-matched controls. More importantly, consolidation introduces an additional identifiable error beyond the third-person summary condition, with corresponding consequences in later sessions.




C. A solution that adds value beyond simple alternatives

Anchor-aware records and consolidation reduce incorrect identity assignments beyond localized prompts and ordinary decontextualization. They preserve correctly attributable facts and offer a defensible utility–storage trade-off relative to verbatim episodic retrieval.




D. A credible, reusable linguistic resource

The benchmark includes native-authored diagnostic cases, adjudicated referent frames, calibrated disagreement distributions, documented regional variation, explicit context boundaries, and reproducible scoring and intervention code.



The highest-value result would be a three-way dissociation:
1. The backbone can interpret the original Vietnamese reference.
2. A decontextualizing memory write nevertheless assigns it incorrectly, with consolidation introducing an additional measurable failure.
3. An anchor-aware design removes that additional failure without disproportionately sacrificing memory retention or downstream answer quality.
That would identify a mechanism, demonstrate its consequences, and show how to mitigate it.

I would not require a second language for an ACL main-track accept. The ARR guidelines explicitly caution against dismissing contributions merely because they study a non-English language. The burden is instead to support the stated scope and conclusions. 

GitHub

8. Acceptance-probability judgment
ACL 2027 main track — conditional on competent execution of the current specification
10–25%





0%10–25% judgment band100%

This is a subjective referee forecast, not a calibrated statistical probability or the conference acceptance rate.

My reasoning is that the central linguistic variable is novel enough to interest ACL reviewers, but too many of the proposed results may fail for valid scientific reasons: C0 may show limited occurrence, C1 may vanish under strong prompting or collapse into a summary-format effect, C3 may prove to be an independent deduplication issue, and C4 may favor English-pivot translation.

Competent implementation does not guarantee that the claims are empirically true.

If the proposal produces the causal decomposition and mitigation evidence described in Section 7, I would regard it as a substantially stronger submission, potentially deserving clear acceptance.

Final referee decision on the idea as specified: Conditional scientific merit, but Weak Reject at present. The critical question is not whether Vietnamese con, anh, chị, or mẹ can challenge an LLM. It is whether the act of writing and consolidating persistent memory introduces a distinct, measurable, and avoidable failure beyond ordinary discourse interpretation.

Independently checked literature
The following records distinguish what I opened myself from what was reported in the attachments. “Opened” does not imply that I reproduced the experiments.
Work and identifier	My verification
DIAL-SUMMER — arXiv:2602.08149	Opened full text in arXiv's web rendering; checked viewpoint-distortion and speaker-attribution categories.  arxiv.org
Manufactured Confidence — arXiv:2606.29279	Opened full text; checked the extraction interventions and verbatim episodic-store control.  arxiv.org
AmbiCoref — 2023.findings-eacl.75	Opened ACL Anthology record and abstract, not full paper.  ACL Anthology
Correct-Detect — 2025.emnlp-main.1527	Opened ACL Anthology record and abstract, not full paper.  ACL Anthology
Decontextualization — 2021.tacl-1.27	Opened ACL Anthology record and abstract, not full paper.  ACL Anthology
Learning to Reject with a Fixed Predictor — arXiv:2301.09044	Opened arXiv abstract, not full paper.  arxiv.org
Whose Memory Is It? / CASK — arXiv:2610.09008	Opened full text; confirms that discourse ownership and memory-commit boundaries are already proposed in prior work, though not Vietnamese dyad reference.  arxiv.org
Coreference Resolution for Vietnamese Narrative Texts — arXiv:2504.19606	Opened arXiv record and abstract; establishes Vietnamese coreference work outside the proposed dialogue-memory setting.  arxiv.org

For Graphiti, I also opened the public dedup_helpers.py source, rather than relying solely on the prior-art reports. That inspection does not substitute for an end-to-end execution against a pinned framework version. 

GitHub

Model: OpenAI GPT-6. A finer-grained internal build identifier is not exposed to me.