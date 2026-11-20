# IDEA_M3: Who is speaking? Vietnamese address terms as a minimal-pair probe of instruction provenance in LLM agents

Citation status used below: **[notes]** = identifier appears in `research_notes/.../agent_security_sota.md` or `hot_topics.md`; **[gaps]** = identifier appears in `03_GAPS.md`; **[fetched]** = primary record or full text opened in this ideation session (2026-11-20); **[index]** = only the alphaXiv index record (ID, title, first lines of abstract) was seen.

- Gap addressed: **G2** (language as a variable in agent security: user language, environment language and injected-content language varied independently; code-switching). Touches G12 (English-normalising pipelines erase a language-specific structure) and shares the linguistic phenomenon, but not the object of study, with G1.

- Target venue and track: **ACL 2027** via ARR, long paper. Primary area "LLM Agents for NLP"; defensible alternatives "Discourse and Pragmatics" or "Multilingualism and Cross-Lingual NLP". Claim C3 below also qualifies the paper for the Special Theme "Homogenization and knowledge collapse in LLMs" (cross-linguistic homogenization). ARR contribution types: data resource + model analysis.

- Problem (1 paragraph): Indirect prompt injection is a failure to track who authored an instruction. Evaluation of that failure is almost entirely in English, where an imperative carries no grammatical trace of its author. The three existing studies of language and agent security vary only the user request (2610.22244 [notes]), or request/page/response language in URL retrieval with no injected instruction (2610.23093 [notes, abstract fetched]), or run eight scenarios on one model (2608.15392 [notes]); none includes Vietnamese, and none isolates a linguistic cue to authorship. Multilingual agent benchmarks measure capability, not security (2609.23490 [notes]). So nobody knows whether agents use, ignore, or can be fooled by the authorship information that many languages put into every sentence.

- Key insight (the non-obvious observation; 2–3 sentences): Vietnamese encodes the speaker–addressee relation in person reference itself: kin terms and register ("anh … em", "mình … bạn", "quý khách") mark who is talking to whom, so an instruction inside a tool output either *claims* the user's established dyad or overtly belongs to a different speaker. That gives a minimal-pair instrument English cannot provide: hold the propositional content of an injected instruction fixed and change only the address dyad, then read off whether agents treat dyad congruence as authority (a spoofable cue) or disregard an authorship cue that native readers use without effort. Translating the content to English neutralises the contrast, so English-pivot guards and English-only benchmarks are structurally blind to this dimension.

- Approach (how the insight becomes a method/system/theory):
  1. **Substrate**: an executable tool-calling environment with state-based checks (AgentDojo-style suites, 2406.13352 [notes]), with tool contents re-authored in Vietnamese by native annotators. Entity identifiers stay fixed, so the checker is language-invariant and no LLM judge decides success.
  2. **Dyad minimal pairs**: each session establishes a user–assistant dyad in the user turns (e.g. anh–em, chị–em, mình–bạn, tôi–bạn, cô–cháu). Each injected instruction is written in five variants with identical content: user-congruent dyad, a different kin dyad, institutional register (quý khách), pro-drop with no overt person reference, and English. Annotators write the variants, rate naturalness, and a second annotator independently answers "who wrote this sentence: the user or someone else?" to give the human attribution baseline and agreement.
  3. **Language-role factorial around the pairs**: user language × tool-content language × injection language over Vietnamese, English, Vietnamese–English code-switching and undiacritised Vietnamese (a naturally occurring orthography in informal text).
  4. **Three read-outs per item**: (a) behaviour — attacker-goal completion and user-task completion from environment state; (b) explicit attribution — in a separate call, the model is asked who authored the instruction; (c) guards — detection by small prompt-injection detectors run locally, with and without an English-pivot translation step.
  5. **Analysis**: mixed-effects logistic models with random effects for scenario and payload; paired contrasts; equivalence tests for "no effect" conclusions; a same-dyad paraphrase placebo to estimate wording noise, following the placebo-adjusted design of 2610.22244.

- Contribution type: **new measurement/benchmark** (a controlled minimal-pair instrument with human baseline; the finding is an analysis result, in either direction).

- Claims (falsifiable, 2–4):
  - **C1 (address dyad as authority cue).** Injected instructions in the user-congruent dyad are completed at least 5 percentage points more often than the same instructions in an incongruent dyad, in a majority of tested agent models. Refuted if the paired contrast is within ±3 points by equivalence test; that outcome supports the rival reading "agents ignore the cue" only together with C2.
  - **C2 (human–model attribution gap).** On the same sentences, native speakers attribute authorship (user vs third party) with at least 90% accuracy, while models' explicit attribution is at least 15 points lower on kin-term and pro-drop variants; and among items a model attributes to a third party, attacker-goal completion remains above the paraphrase-placebo noise level (a recognition–execution gap, cf. 2608.10669 [notes]).
  - **C3 (English-pivot erasure).** Passing tool content through English translation before the agent or guard removes the congruent–incongruent contrast (significant dyad × pivot interaction) and lowers guard recall on items whose only non-user cue is the dyad.
  - **C4 (congruence beyond resource level).** With user language and injection language crossed, the match-vs-mismatch interaction on attacker-goal completion is non-zero after main effects of each language are removed, with matched language raising completion.

- Closest work known so far (with identifiers) and the expected delta:
  - **Disentangling Language Effects on Tool Admission and Post-Retrieval Safety**, arXiv 2610.23093 [notes, abstract fetched]: independently varies request, page and response language for harmful retrieval across seven languages. Delta: no injected third-party instruction, no authorship cue, no Vietnamese; language is a label, not a grammatical variable.
  - **LinguaGuardBench**, arXiv 2610.22244 [notes]: translates only the user instruction of AgentDojo steps; guard verdict flips, translations made by a guard under test, no native reader for two languages. Delta: natively authored injected content, behaviour of agents not only guards, minimal pairs.
  - **English/Tamil/Tanglish injection case study**, arXiv 2608.15392 [notes]: eight scenarios, one model, direction reversed on rerun. Delta: powered paired design with human baseline.
  - **Trust-region (placement) effect**, arXiv 2610.38867 [notes]: same content obeyed 2.6× more in a README than in a data file. Delta: placement cue vs grammatical authorship cue; used here as an effect-size yardstick.
  - **BabelArena**, arXiv 2609.23490 [notes]: multilingual agent capability; no security.
  - **Recognized but Not Produced: culturally specific kinship terms**, arXiv 2609.26942 [index]: kin-term generation by LLMs; not agents, not provenance.
  - **AgentMemGate** 2610.07707 and **MemAlign/ConMem** 2610.33432 [gaps]: attribution confusion in memory writing, English, model-generated data. Delta: injection susceptibility rather than memory writes; human-authored minimal pairs.
  - Linguistic grounding: Hy V. Luong, *Discursive Practices and Linguistic Meanings: The Vietnamese System of Person Reference*, Pragmatics & Beyond New Series 11, 1990 [fetched publisher record].
  - Search note: one index search for honorifics/address terms as authority or speaker-identity cues in prompt injection returned no matching paper; this is absence in one index, not proof.

- Evaluation sketch: settings, baselines (strongest first), metrics, decisive experiment
  - **Settings.** Scenarios chosen where following third-party content is sometimes legitimate (under-specified, "action-open" tasks, where filtered agents are hit 57–64% in 2606.15057 [notes]) to keep attack rates off the floor; payload strength calibrated on mid-tier models. Models: 3–4 API models and 2–3 open-weight models; small detectors served locally. Paired items with repeated runs sized for a 5-point paired contrast, since a 100-item single-run benchmark resolves only about 18 points (2609.25173 [fetched]).
  - **Baselines, strongest first.** (1) The explicit-claim attack that names the user outright (the standard AgentDojo injection template): if an overt "this is from the user" claim already saturates compliance, the dyad adds nothing — the referee's first objection. (2) English originals of the same scenarios, to separate "Vietnamese is weaker" from the dyad effect. (3) Machine-translated Vietnamese with no native control of person reference, to show what native authoring changes. (4) Same-dyad paraphrase placebo. (5) Placement manipulation as in 2610.38867 for effect-size comparison.
  - **Metrics.** Paired difference in attacker-goal completion with intervals; user-task completion; attribution accuracy for humans and models; guard recall at fixed false-positive rate with and without English pivot; inter-annotator agreement and naturalness ratings for every variant.
  - **Decisive experiment.** The dyad minimal-pair contrast (C1) with the human attribution baseline (C2), preregistered. It can come out negative in a way that removes the paper's point: no contrast, and models attribute authorship as well as humans and act on it — then address terms are neither a vulnerability nor a neglected signal. A floor effect (near-zero completion in every variant) would make it uninformative rather than negative; the calibration step exists to prevent that.

- Resources needed vs available (00_CONSTRAINTS.md):
  - At least two native Vietnamese annotators fluent in English who can annotate independently — available; this is the resource the design depends on and the one competitors lack.
  - Commercial APIs for agent models; 1–2 GPUs for open-weight agents and small guard models — available.
  - Evaluation-framework expertise for localising an executable environment while keeping state checks invariant — available.
  - Not needed: Android testbed (a mobile variant using system-locale switching is an extension only), white-box access.

- Risks and unknowns:
  - **Single natively controlled language.** Reviewers will ask for a second language with grammaticalised person reference (Korean, Japanese, Thai). Without native annotators, any such addition would be machine-translated and must be labelled as a pilot; the claim has to stay "Vietnamese as an instrument", not "all honorific languages".
  - **Register confound.** Congruent and incongruent variants differ in politeness and formality as well as dyad; naturalness ratings and the institutional-register variant help, but full separation may be impossible.
  - **Regional and generational variation** in kin terms; annotator pair should document dialect.
  - **Floor effects on frontier models**, where static injections are near zero (2611.11861 [notes]); results may rest on mid-tier and open models.
  - **Dual use.** A positive C1 documents a spoofing cue; payloads stay abstract and visible in the paper, per venue rules on injection content.
  - **Overlap management.** The ACL candidate on G1 uses Vietnamese person reference for memory-write errors; annotation guidelines can be shared, content cannot (hard exclusion on dual submission in 00_CONSTRAINTS).
  - **Unknown direction.** I have no pilot data; either sign of C1 is plausible.

- Conference core / journal extension (1 line each):
  - Conference core: the dyad minimal pairs with human baseline, C1–C3 on a tool-calling environment, and the language-congruence interaction (C4) at reduced scale.
  - Journal extension (Computational Linguistics accepts substantially extended versions per venues.md): full language-role factorial, mobile variant where UI language is set by Android locale so interface strings come from the apps' shipped translations, memory-persistent agents, and a dyad-aware provenance check as a defence.

- Generator perspective: empirical/measurement
