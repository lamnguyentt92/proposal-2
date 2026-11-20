# Red-team review of IDEA_L1R (feasibility)

- Scores 1–5: novelty n/a, significance n/a, depth n/a, soundness potential 3, evaluation 3, clarity 3, venue fit 4.
  - Soundness potential 3: the window claim (C2) is non-trivial only for native frameworks, and only two of the four have a bounded window (see below).
  - Evaluation 3: every component can be obtained, but the grid as written (4 frameworks × 2–3 backbones) is not buildable as a like-for-like comparison.
  - Clarity 3: four things the build depends on are unspecified: what "window" means per framework, who the dyad is between (user–assistant or user–third party), how a record that keeps the kin term is scored, and how the "human floor" is measured.
  - Venue fit 4: the Responsible NLP checklist can be answered fully; resource + analysis papers of this size are normal at ACL.

- Feasibility findings (per item checked, with evidence and links):

  **0. Verdict and evidence key**
  - Verdict: **feasible with changes**. Reviewed 2026-11-20. Scope: technical, ethical and resource feasibility only (team size, person-weeks and deadlines are out of scope by rule).
  - Evidence levels: **[CODE]** repository cloned today and the file read; **[META]** registry or API record read today; **[PDF]** paper pages read today; **[WEB]** web page read today; **[EST]** my own arithmetic from measured sizes; **[RECALL]** from memory, not re-checked today.
  - Nothing was executed end to end: no framework was run on Vietnamese input. All framework statements are static readings of code at the commits named.

  **1. Memory frameworks**

  | | Mem0 OSS | Graphiti | LangMem | Letta |
  |---|---|---|---|---|
  | Version / commit read | 2.2.1, `fff8a64` (18 Nov 2026) | 0.31.2, `9b8a463` (20 Nov 2026) | 0.0.30, `4beb9c3` (16 Nov 2026) | `letta-ai/letta` `8816d3a` (18 Oct 2026); `letta-ai/letta-code` `7587357` (20 Nov 2026), npm 0.34.67 |
  | Licence | Apache-2.0 | Apache-2.0 | MIT | Apache-2.0 (both repos) |
  | Runs locally | yes | yes | yes | yes (`letta backend local`) |
  | Commercial + local LLM | yes: OpenAI (with base URL), Anthropic, Gemini, LiteLLM, Ollama, vLLM, LM Studio | yes: OpenAI, Anthropic, Gemini, Groq, `OpenAIGenericClient` for Ollama/vLLM | yes: any LangChain chat model; needs tool calling (`trustcall`) | yes: BYOK providers incl. Ollama, LM Studio, OpenAI-compatible |
  | Needs | embedder + local vector store + SQLite history; **no graph DB** (graph memory is platform-only) | graph DB (Neo4j ≥ 5.26, FalkorDB, or embedded `falkordblite` on Python ≥ 3.12) + embedder; structured JSON output | LangGraph store; embedder only for search | Node runtime; memory is a git-tracked folder of Markdown files |
  | Write-time context | new messages + **last 10 stored messages** + top-10 retrieved memories | current episode + **last 3 episodes** + graph context | **whatever the caller passes** (no window of its own) | the agent's whole context; writes are agent tool calls or a reflection sub-agent |
  | Dump of written records | `get_all(filters=…, top_k=…)` (default `top_k=20`, raise it), `history()` | `add_episode` returns nodes and edges; Cypher over the graph | manager returns `ExtractedMemory` list; `store.search` | read the memory folder, `git log -p` |
  | Vietnamese handling | English prompt and examples; no output-language rule in the OSS path | "same language as written"; relation labels in English | none | none |

  Details and evidence [CODE]:
  - **Mem0.** The current write path is a single-call "V3 phased batch pipeline" (`mem0/memory/main.py:918–960`). Context is `self.db.get_last_messages(session_scope, limit=10)`; the prompt text says "up to 20". The system prompt (`ADDITIVE_EXTRACTION_PROMPT`) is 33,693 characters, about 8,400 tokens per call. It tells the writer to "Replace all pronouns with specific names or 'User.'", so the writer is forced to commit to a person. A language block exists (`use_input_language`, including "For Japanese: explicitly resolve omitted subjects using conversation context") but nothing in the OSS package ever sets it to true; output language for Vietnamese input is therefore unspecified and must be measured. Telemetry is on unless `MEM0_TELEMETRY` is disabled. Repo: <https://github.com/mem0ai/mem0>.
  - **Graphiti.** `EPISODE_WINDOW_LEN = 3` (`graphiti_core/utils/maintenance/graph_data_operations.py:29`). Language rule in `llm_client/client.py:37–55`. The summary prompt still forbids reporting verbs (`prompts/extract_nodes.py:589`), as hunter B found. The README warns that structured output is unreliable on small local models and offers `structured_output_mode="json_object"`. The Kuzu driver that LAPSE used with 0.30.1 is gone from the current tree. Telemetry is opt-out. Repo: <https://github.com/getzep/graphiti>.
  - **Graphiti, Vietnamese-specific defect.** Fuzzy entity deduplication normalises names with `re.sub(r"[^a-z0-9' ]", ' ', …)` (`dedup_helpers.py:48`). I reproduced the regex in isolation: "chị Hằng", "chị Hùng" and "chị Hồng" all become `ch h ng` (entropy 1.92, above the 1.5 gate), which gives Jaccard 1.0 against a 0.9 merge threshold, with no LLM call. Read from code, not run in the framework: two differently named people can be merged into one node. This changes who a fact is attached to, independent of the backbone. It must be controlled (fictional names whose ASCII skeletons differ) or reported as a finding.
  - **LangMem.** `create_memory_manager` extracts from the message list it is given, so "frame outside the window" has no native meaning. Instruction: "Caveat uncertain or suppositional information with confidence levels (p(x))". Last PyPI release is October 2025; the repo only receives dependency bumps. Repo: <https://github.com/langchain-ai/langmem>.
  - **Letta.** On 18 Oct 2026 `letta-ai/letta` became a landing page. The Python server is retired to an `archive` branch; the PyPI name `letta` (0.34.12) now installs the Node CLI. The repo's `AGENTS.md` states that the archived server, old packages and Docker image should not be used for benchmarks or academic research and that results from them describe a retired system. That is the vendor's position, not a licence term (Apache-2.0 still applies). LAPSE's Letta row (0.16.8, May 2026) is that retired system. Current Letta (`letta-code`) is a coding-agent harness: memory is written by the agent itself or by a reflection sub-agent reading transcripts in chunks; there is no extractor with a fixed window. Repos: <https://github.com/letta-ai/letta>, <https://github.com/letta-ai/letta-code>.
  - **Zep.** Community Edition is deprecated; the notice points to Zep Cloud or Graphiti [WEB: <https://help.getzep.com/ce-deprecation-notice>]. Zep Cloud is hosted and, as far as I know, does not let the caller choose the LLM [RECALL]. Use Graphiti for the "Graphiti/Zep" row.

  Consequences for the design:
  - A native "extraction window" exists only in **Mem0** (10 messages) and **Graphiti** (3 episodes). They count different units, and the size of a batch or episode is chosen by the experimenter. The step-function prediction in C2 can be tested natively on two systems, not four.
  - In both, the frame can re-enter through earlier writes (Mem0 retrieves 10 existing memories; Graphiti passes existing nodes and summaries). An earlier record such as "User calls Lan *chị*" would act as a dyad register that the framework built itself. Every LLM call must be logged (logging proxy on the OpenAI-compatible endpoint) so that each item can be classified by whether the frame-setting turn, or a memory carrying it, was in the prompt.
  - The dyad register probe (step 5) can be implemented without patching: Mem0 accepts `custom_instructions`, Graphiti accepts `custom_extraction_instructions`. With a patch it is no longer the native writer and must be labelled so.

  **2. Baselines**

  | Work | Code | Licence | Can it be labelled a baseline? |
  |---|---|---|---|
  | FACTWASH, arXiv:2608.03372 | <https://github.com/collapseindex/factwash>, v0.5.0, `2e20496` (7 Aug 2026) [CODE] | Apache-2.0 | **English: yes, run as released** (`factwash.check(source, memory)`). **Vietnamese: no.** The README says "English-only, substring-matched"; a Vietnamese cue lexicon would be ours, so the label must be "FACTWASH-style". `wrap()` was verified against mem0 2.0.7, before the V3 pipeline; call `check()` directly. |
  | AgentMemGate, arXiv:2610.07707 | <https://github.com/DistylAI/agentmemgate-artifacts>, `9d3f012` (26 Aug 2026) [CODE] | README: CC BY 4.0 "upon publication"; **no LICENSE file** | **Yes for the cautious extractor**: `protocol/prompts/extractor.txt` and the pipeline in `src/memory_gating/` are there. It emits (entity, attribute, value, statement_span, confidence) tuples, so the scorer must accept tuples. Results were produced on a pinned snapshot (`gpt-5.5-2026-04-23`). Confirm the licence with the authors before redistributing the prompt. |
  | LAPSE, arXiv:2609.36457 | <https://github.com/aimsresearchlab/lapse>, `8ad8262` (10 Nov 2026) [CODE] | code MIT, data CC BY 4.0 | Not a method baseline. Its harness scripts for mem0 2.0.19, Graphiti 0.30.1 (Kuzu, fastembed `bge-small`) and Letta 0.16.8 are reusable templates. Its embedder is English; use a multilingual one for Vietnamese. |
  | AuthMem-Bench, arXiv:2608.01679 | **none found**: no URL in the arXiv record [META] or in the pages read [PDF]; GitHub repository search and Hugging Face dataset search return nothing | — | **Prompt-level only.** Appendix C reproduces every consolidator prompt, including the source-aware intervention, and A.4 defines Upgrade-all / Ret⁻ / Ret⁺. Label: "source-aware consolidator prompt, re-implemented from AuthMem-Bench App. C". Its "framework" rows are framework-inspired prompts in a common schema, not installed frameworks. Its data builds on APIGen-MT-5k (CC BY-NC 4.0); do not reuse it. |
  | Manufactured Confidence, arXiv:2606.29279 | <https://github.com/collapseindex/manufactured-confidence>, `9abbc2f` (23 Jul 2026) [CODE] | Apache-2.0 | **Yes, verbatim.** The hedge-preserving prompt is the `HEDGEKEEP` string in `experiments/prompt_fix.py`. |

  All three English prompt baselines can be applied to Vietnamese input unchanged; a translated variant is a separate, labelled condition.

  **3. Open models for a local Vietnamese backbone (1–2 GPUs, 24–48 GB)**
  - `aisingapore/Qwen-SEA-LION-v5-27B` — MIT, updated 18 Nov 2026, lists Vietnamese, 262k context, documents vLLM tool calling; evaluated on SEA-HELM, which covers Vietnamese, with a leaderboard snapshot of 17 Nov 2026 [META: <https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-27B>]. Per-language numbers are on <https://leaderboard.sea-lion.ai/>; I did not read them.
  - `Qwen/Qwen3.8-27B` — Apache-2.0, its base model; an FP8 build is published [META].
  - `google/gemma-4-31B-it` — Apache-2.0, 256k context, native function calling, QAT 4-bit builds, "35+ languages" [META].
  - `aisingapore/Gemma-SEA-LION-v4-27B-IT` — MIT, Vietnamese listed, function calling and structured output.
  - Not recommended: SeaLLMs-v3-7B (last updated 2024, "other" licence).
  - Fit [EST]: 27–31B weights are about 54–62 GB at 16-bit (does not fit), about 27–31 GB at FP8 (fits 48 GB), about 16–20 GB at 4-bit (fits 24 GB). Mem0 needs at least 12k tokens of context per call. Quantisation level must be reported.
  - No public benchmark tests kin-term person reference. The pilot's full-dialogue reader condition is the gate for the local model.

  **4. Annotation**
  - *Tool.* INCEpTION (Apache-2.0, <https://github.com/inception-project/inception>): custom span layers with several features, link features for the source chain, a curation mode for adjudication, built-in agreement. Its measure list (Cohen's κ, Krippendorff's α nominal and unitizing) is [RECALL]; the documentation site did not load today. Alternative: Label Studio Community 1.23.2 (Apache-2.0) with per-region attributes; agreement and adjudication then have to be scripted offline.
  - *Protocol.* (1) Guidelines from the 60-family pilot, in Vietnamese with an English translation. (2) Calibration round. (3) Independent double annotation, blind to the design label and to model output; **the two members of a pair go to different sessions in random order**, otherwise annotators infer that one must flip. (4) Per item: anchor span, holder chosen from the dialogue's entity list (multi-select = admissible set), polarity, condition span, ordered source chain, six-way commitment, naturalness 1–5, regional note. (5) Adjudication by a third native speaker who did not write the item. (6) Release both raw labels and the adjudicated one.
  - *Agreement statistics.* Per categorical field: Cohen's κ or Krippendorff's α with a family-clustered bootstrap interval, plus raw agreement and the confusion matrix (κ is unstable when one class dominates). Anchor spans: unitizing α or γ (Mathet et al. 2015; `pygamma-agreement`, MIT). Admissible sets: α with the MASI distance (Passonneau 2006). Whole frame: exact-match rate and α with a slot-wise distance (Braylan et al. 2022). Pair level: share of pairs where both annotators agree on both members, because the headline metrics are paired.
  - *Gaps in the human roster.* (a) Adjudication needs a third native speaker; the constraints guarantee two. (b) The "human floor" in C1 needs a native rater who did not contribute to the gold. (c) "Natively authored" English items cannot be claimed with Vietnamese L1 authors; either recruit native English validators or write "authored by fluent L2 speakers, validated by a native speaker". (d) Authors and annotators of an item must be different people.
  - *API cost* [EST]. About 5,000 dialogue instances. Token load per configuration, turn-by-turn ingestion: Mem0 ≈ 200M input (the 8.4k-token prompt repeats on every call); Graphiti ≈ 300M input + 30M output (several calls per episode); LangMem ≈ 25M; an extractor-only condition ≈ 15M input + 10M output; current Letta roughly 0.75–1.75B input. Scoring 5,000 × 18 record sets ≈ 90M input. At the list prices a third-party tracker reported for mid-2026 (frontier about $3–5 per million input and $15–30 output; cheap tier about $0.4–1.5 input; cached input about 10%; batch 50% off) [WEB: <https://www.cometapi.com/2026-llm-api-pricing-comparison-gpt-5-5-claude-gemini/>, not provider pages], the full grid run once is in the **low thousands of US dollars** if frontier models are kept for the extractor baselines, and around **$10,000 or more** if every framework row uses a frontier model or runs are repeated. Local-model rows cost GPU time only.

  **5. Two design points that decide whether Layer D can be built**
  - *Who is the dyad between?* The user is talking to an assistant, so two dyads are in play: user–assistant and user–third party. The card's example flips only under some combinations and under a quotation reading. The assistant's own turns also carry address terms and are inside both frameworks' windows. For the "far" condition, every intervening turn of both speakers must be frame-neutral and still rated natural. The yield of such families is unknown; it is the first number the pilot must produce.
  - *What is a correct record?* A Vietnamese record that keeps the kin term ("Lan bảo chị nên nghỉ việc") assigns no holder. The same-holder metric needs a third outcome (unresolved), and the scorer must handle Vietnamese, English and mixed records plus tuples and graph edges.
  - For a home-built extractor, "frame outside the window" means the information was withheld, so failure is guaranteed. C2 carries information only on native frameworks, and C1b only if translation sees the whole dialogue.

- Riskiest technical dependency:
  A controllable and observable extraction window in native writers. C2 and the distance manipulation rest on it, and today it exists in two of the four frameworks, in different units, with a side channel through earlier memories, on code that changed materially within the last three months (Mem0's V3 pipeline; Graphiti dropping Kuzu and adding combined extraction; Letta retiring its server on 18 Oct 2026). Mitigation: pin Mem0 2.2.1 and Graphiti 0.31.2, log every LLM call, treat LangMem as window-free, and carry the window claim on Mem0 + Graphiti plus one own extractor with a parametric window as the control.
  Second: holder scoring of free-text records in two languages, including the unresolved class. Third: native agreement on frame-flip items and the yield of natural string-identical pairs.

- Minimal viable version:
  - Data: Vietnamese Layer D only — 60–100 frame-flip families × 2 frames × 2 distances (inside and beyond the window), natively written, double-annotated, pair members annotated in separate sessions; plus about 60 EN/VI twin families for C3.
  - Systems: Mem0 2.2.1 and Graphiti 0.31.2 (FalkorDB), each with one commercial backbone and one local 27B model; a structured extractor; a full-dialogue reader; document-level translate-then-extract; the Manufactured Confidence prompt; FACTWASH v0.5.0 on the English twins only.
  - Measurement: three-way outcome (correct holder / wrong holder / unresolved), an LLM scorer validated against about 300 human-scored records, every prompt logged.
  - This still tests the key insight: same string, different holder; inside versus beyond the vendor's window; and whether translation commits to a person too early. Letta, LangMem window effects, the held-out composition split (C4) and the full 5,000-item scale are left out.

- Ethics, licences and disclosure:
  - *Data.* All dialogues fictional; no personal data. For checklist B4, document that every name, employer and place is invented and that items were screened for real persons. For B5, document regional variety (Northern and Southern kin terms differ) and the phenomena covered.
  - *Annotators* (checklist D1–D5, read today at <https://aclrollingreview.org/responsibleNLPresearch/>): full instructions in the appendix; recruitment and pay, with a statement that pay is adequate for where the annotators live (or that they are co-authors or colleagues); consent to release their labels; ethics-board approval or an exemption determination, or a justified statement if the institution has no board; region, age band and gender of annotators, which matter here because kin-term judgments vary with them. Answers may be negative, but ARR desk-rejects checklists that systematically lack sections or justifications.
  - *AI assistance* (E1): disclose AI-assisted ideation and any LLM drafting of items. The constraints file already bars copying this material into a manuscript where the venue forbids it.
  - *Licences.* Mem0, Graphiti, letta-code, FACTWASH, Manufactured Confidence, Label Studio, INCEpTION: Apache-2.0. LangMem, LAPSE code, Qwen-SEA-LION-v5: MIT. LAPSE data: CC BY 4.0. Qwen3.8-27B and Gemma 4: Apache-2.0. AgentMemGate artifacts: no licence file yet. LoCoMo (bundled in the AgentMemGate repo) and APIGen-MT-5k: CC BY-NC 4.0, keep out of the release. The PyPI `krippendorff` package is GPL-3.0: use it for analysis, do not vendor it. Released model outputs remain subject to each provider's terms.
  - *Vendor matters.* If a Letta row is reported on the archived server, say so in the table; the vendor has asked that such results not be presented as current Letta. Disable Mem0 and Graphiti telemetry and state it. The Graphiti deduplication defect should be reported upstream without a link to the paper during the anonymity period.
  - *Risks* (A2): the items could inform holder-confusion memory poisoning (cf. Role Grounding Attack, arXiv:2610.38209). Consider a canary string or gated release to limit training contamination.

- Likely reasons for rejection (feasibility-related):
  1. The window finding reads as true by construction, because for two frameworks and all home-built extractors the window is the experimenter's choice.
  2. Baselines labelled FACTWASH or AuthMem-Bench that are in fact a new Vietnamese lexicon or a re-implemented prompt.
  3. A Letta row on a server the vendor retired a month before submission, or a silent switch to a different product under the same name.
  4. Gold labels questioned: annotators saw both members of a pair; adjudicator also wrote the items; English items called native without a native author; "human floor" not measured.
  5. Automatic scoring not validated on Vietnamese records, or no category for records that keep the kin term.
  6. Local-model rows that mostly measure broken structured output in Graphiti rather than holder resolution.
  7. Framework-level artefacts (ASCII-only entity merging) mixed into what is presented as a discourse effect.

- What would make this a clear accept:
  1. A pilot that reports, before scale-up: the yield of natural frame-flip families, native agreement on them, and Mem0/Graphiti outcomes inside versus beyond the window with the prompt logs to prove what the writer saw.
  2. The dyad specified as a three-party structure, with assistant turns controlled.
  3. A three-way holder outcome and a scorer with reported agreement against humans in both languages.
  4. Frameworks pinned by version and commit, with the Letta and LangMem rows either dropped from the window analysis or described exactly.
  5. Every baseline labelled by what was actually run (released code, verbatim prompt, or re-implementation).
  6. A measured human floor from a rater outside the gold, and annotator documentation that answers D1–D5 without gaps.
  7. The Graphiti name-merging defect either controlled by item design or isolated as its own result.
