# Hot topics and community-named open problems at ICML, ACL and IJCAI (as of 2026-11-20), for choosing 2027 paper topics

Verification legend used for every paper below:
- **[read]** = full text or structured report opened through alphaXiv and read by me.
- **[index]** = arXiv ID, title, affiliation and abstract snippet returned by the alphaXiv index; paper not opened.
- **[cited]** = identified in the reference list / related work of a paper I read; not opened directly.
- **[official]** = taken from the conference's own page. **[secondary]** = taken from a news or blog page; the official page was not opened.

Access note: a batch of WebFetch calls (official ACL 2026 awards page and arXiv HTML pages) was blocked because it needed a user approval that nobody answered. Those items are marked unverified where it matters.

---

## Q1. Which themes dominated accepted papers, orals and best/outstanding paper awards at ICML 2026, ACL 2026, IJCAI 2026 (context: NeurIPS 2025, ICLR 2026, EMNLP 2026)?

### Takeaway
Agents dominate by volume (ACL 2026 agent/reasoning/tool-use titles rose from 142 to 366 in one year), but awards went almost entirely to theory, diffusion, linguistics, memorization, and critical evaluation studies. Across 2 + 5 ICML, 3 + 18 ACL and 3 IJCAI awarded papers, I found only two papers that are agent papers in the narrow sense (both ACL outstanding papers).

### Cited Findings

**Scale**
- ICML 2026: 23,918 submissions entered review, 6,352 accepted (26.6%), 536 spotlights — [Bohrium summary of ICML figures, secondary](https://www.bohrium.com/en/blog/icml-2026-accepted-papers/). A second secondary source adds 168 orals, a 2025 baseline of 12,107 submissions, and 497 desk rejections — [AI2Work, secondary](https://ai2.work/blog/icml-2026-hits-record-23-918-submissions-as-agents-take-over). Paper Digest instead says "6,500+" accepted — [Paper Digest](https://paperdigest.org/2026/05/icml-2026-papers-highlights) (conflict with 6,352; probably includes the position track).
- ACL 2026 (San Diego, July 2–7): 12,148 submissions (+45% on 8,360 in 2025), 2,296–2,297 main papers (18.9%), 2,163–2,164 Findings (17.8%), 504 orals — [Bohrium, secondary](https://www.bohrium.com/en/blog/acl-2026-accepted-papers-highlights/); [36Kr, secondary](https://www.36kr.com/p/3888326643104513). The two sources differ by one paper in each count. 36Kr also reports "about 26,000 attendees", which is implausible next to Bohrium's ~5,000 for 2025; treat as an error.
- IJCAI-ECAI 2026 (Bremen): 989–990 accepted papers across tracks, 712–713 in the main track; special-track counts: AI for Social Good 52, Demos 50, AI and Health 47, Survey 45, AI4Tech 25, AI and Robotics 11, Human-Centred AI 10 — [AI2Work recap, secondary](https://ai2.work/blog/ijcai-ecai-bremen-everything-announced-at-ai-s-oldest-conference); [AI2Work opening piece, secondary](https://ai2.work/blog/ijcai-ecai-main-technical-program-opens-in-bremen-with-990-papers). Neither gives submissions or an acceptance rate for 2026.

**Theme counts (ACL 2026, title-level classification by Bohrium, not official area statistics)** — [Bohrium](https://www.bohrium.com/en/blog/acl-2026-accepted-papers-highlights/)

| Theme | 2025 | 2026 | Change |
|---|---|---|---|
| LLM reasoning, agents, tool use | 142 | 366 | +224 |
| Representations / behaviour analysis / general LLM | 308 | 333 | +25 |
| Training, fine-tuning, alignment, RL | 196 | 295 | +99 |
| Evaluation, benchmarks, datasets, reliability | 245 | 295 | +50 |
| RAG, QA, knowledge editing, IE | 174 | 244 | +70 |
| Linguistics, semantics, syntax, traditional NLP | 140 | 166 | +26 |
| Safety, privacy, robustness, hallucination, watermarking | 103 | 125 | +22 |
| Multimodal | 79 | 116 | +37 |
| Dialogue, emotion, social computing | 82 | 100 | +18 |
| Multilingual, cross-lingual, low-resource, cultural | 54 | 52 | −2 |

- ACL also found over 100 accepted papers citing non-existent references, per the same Bohrium account — [Bohrium](https://www.bohrium.com/en/blog/acl-2026-accepted-papers-highlights/).
- ICML 2026: no per-topic counts are published in the sources I could open. Only signal: in the first 59 titles of Paper Digest's list, 11–12 contain "agent/agentic", 5 "diffusion", 4 "reinforcement", 3 "benchmark" (my tally of a truncated page, not a statistic of the whole conference) — [Paper Digest](https://paperdigest.org/2026/05/icml-2026-papers-highlights).

**ICML 2026 awards** — all [official]: [ICML blog](https://blog.icml.cc/?p=1347). 53 candidates, shortlist 22, 2 outstanding + 5 honourable mentions.
- Outstanding: "The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models" (Ni et al.) — [link](https://icml.cc/virtual/2026/oral/71086)
- Outstanding: "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions" (Chen, Chewi, Daskalakis, Rakhlin) — [link](https://icml.cc/virtual/2026/oral/71132)
- Hon. mention: "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes" (Taufeeque et al.) — [link](https://icml.cc/virtual/2026/oral/71065)
- Hon. mention: "Motion Attribution for Video Generation" (Wu et al.) — [link](https://icml.cc/virtual/2026/oral/71049)
- Hon. mention: "How much can language models memorize?" (Morris et al.) — [link](https://icml.cc/virtual/2026/oral/71168)
- Hon. mention: "A Random Matrix Perspective on the Consistency of Diffusion Models" (Wang et al.) — [link](https://icml.cc/virtual/2026/oral/71191)
- Hon. mention: "To Grok Grokking: Provable Grokking in Ridge Regression" (Xu, Vardi, Safran) — [link](https://icml.cc/virtual/2026/oral/71134)
- Outstanding position paper: "Position: The Alignment Community is Unintentionally Building a Censor's Toolkit" (Ball, Hackemann) — [link](https://icml.cc/virtual/2026/oral/71119)
- Position hon. mention: "Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)" — [link](https://icml.cc/virtual/2026/oral/71187)
- Test of Time: "Asynchronous Methods for Deep Reinforcement Learning" (A3C) — [PMLR](https://proceedings.mlr.press/v48/mniha16.html)

**ACL 2026 awards** — [secondary] list from [36Kr](https://www.36kr.com/p/3888326643104513); the official page https://2026.aclweb.org/program/best_papers/ could not be opened, so titles are **unverified against the official list**. Bohrium independently reports the category counts: 3 best, 2 best theme, 3 best resource, 3 best social impact, 1 best demo, 18 outstanding — [Bohrium](https://www.bohrium.com/en/blog/acl-2026-accepted-papers-highlights/).
- Best: "The Imperfective Paradox in Large Language Models" (Ma, Miyao) — [ACL Anthology link given by 36Kr](https://aclanthology.org/2026.acl-long.689/) (link not opened)
- Best: "Memory efficiency and resource-rational encoding in sentence processing" (Xu, Dillon, Futrell) — no URL found
- Best: "Characterizing the Expressivity of Local Attention in Transformers" (Li, Cotterell) — [ACL Anthology link given by 36Kr](https://aclanthology.org/2026.acl-long.1739/) (link not opened)
- 18 outstanding papers (titles only, no URLs in the source): Evolutionary Guided Decoding; Rethinking Entropy Interventions in RLVR; GeoRA (low-rank adaptation for RLVR); CURE (test-time self-improvement RL); **CAR-bench: Evaluating the Consistency and Limit-Awareness of LLM Agents under Real-World Uncertainty**; MediEval; Mind the (DH) Gap! (risky choices, reasoning vs conversational LLMs); CIG (conversational information gain); **Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage**; Beyond the Final Actor (LLM-text detection); Prefix-Aware Localized LLM Unlearning; From Local to Global (structured pruning); MauBERT; Hierarchical Acoustic-Semantic Modeling (full-duplex SLMs); ViLL-E; Systematicity between Forms and Meanings across Languages; Massively Multilingual Joint Segmentation and Glossing; CxMP (constructional minimal pairs) — [36Kr](https://www.36kr.com/p/3888326643104513).
- ACL 2026 special theme was "Explainability of NLP Models"; "AI/LLM Agents" and "Safety and Alignment in LLMs" were main-conference topics — [ACL 2026 CFP, official](https://2026.aclweb.org/calls/main_conference_papers/).

**IJCAI-ECAI 2026 distinguished papers (3)** — [AIhub](https://aihub.org/2026/08/21/congratulations-to-the-ijcai-ecai-2026-distinguished-paper-award-winners/)
- "Approximate Strategyproofness in Approval-Based Budget Division" (Aziz, Lederer, Vollen) — [preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2596.pdf)
- "Tuple Inconsistency Measures: Toward Explaining Query Answers" (Gu et al.) — [preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7822.pdf)
- "StreamTimer: Efficient Inference for Long-Context Time Series Transformers" (Meng et al.) — [preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2468.pdf)
- IJCAI 2026 award lectures were about agents: Jennings, "The Past, Present and Future of Agentic AI"; Parkes, "From Intelligent Agents to Agent Societies" — [AI2Work, secondary](https://ai2.work/blog/ijcai-ecai-bremen-everything-announced-at-ai-s-oldest-conference).

**Context venues**
- NeurIPS 2025 best papers [official]: "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)" — [OpenReview](https://openreview.net/forum?id=saDOrrnNTz); "Gated Attention for Large Language Models" — [OpenReview](https://openreview.net/forum?id=1b7whO4SfY); "1000 Layer Networks for Self-Supervised RL" — [OpenReview](https://openreview.net/forum?id=s0JVsx3bx1); "Why Diffusion Models Don't Memorize" — [OpenReview](https://openreview.net/forum?id=BSZqpqgqM0). Runners-up: "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?" — [OpenReview](https://openreview.net/forum?id=4OsgYD7em5); "Optimal Mistake Bounds for Transductive Online Learning" — [OpenReview](https://openreview.net/forum?id=EoebmBe9fG); "Superposition Yields Robust Neural Scaling" — [OpenReview](https://openreview.net/forum?id=knPz7gtjPW). Source: [NeurIPS blog](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/).
- ICLR 2026 outstanding papers [official]: "Transformers are Inherently Succinct" — [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ); "LLMs Get Lost In Multi-Turn Conversation" — [OpenReview](https://openreview.net/forum?id=VKGTGGcwl6); hon. mention "The Polar Express" (Muon optimizer) — [OpenReview](https://openreview.net/forum?id=yRtgZ1K8hO). Longlist 36, shortlist 5. Source: [ICLR blog](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/).
- EMNLP 2026 (Budapest), partial and [secondary]: two best papers named by an NTU news item — "DiscoTrace: Representing and Comparing Answering Strategies of Humans and LLMs in Information-Seeking Question Answering" and "Don't Read Everything: A Curvature-Conditioned Query for Linear Attention"; no paper URLs given, full award list not found — [NTU news](https://www.ntu.edu.sg/computing/news-events/news/detail/ntu-ccds-faculty-sweep-emnlp-2026-best-paper-awards).

### Inferences
- Volume and reward are decoupled. Agent work is the largest and fastest-growing ACL cluster, yet 0 of 7 ICML main-track awards, 0 of 3 ACL best papers and 0 of 3 IJCAI distinguished papers are agent systems; 2 of 18 ACL outstanding papers are agent papers (one consistency benchmark, one multi-agent collusion attack).
- What gets awarded has a recognisable shape: (a) theory with a crisp result, (b) a careful negative or "rethinking" result about a fashionable method (diffusion-LM ordering, RLVR, multi-turn reliability, homogeneity), (c) linguistically grounded analysis at ACL/EMNLP, (d) classical AI at IJCAI (social choice, KR/databases).
- RLVR (reinforcement learning with verifiable rewards) is a cross-venue award magnet: NeurIPS 2025 runner-up, ICML 2026 honourable mention, two ACL 2026 outstanding papers with RLVR in the title plus a third on RL-based test-time self-improvement.
- Diffusion is ICML's most rewarded theme in 2026 (2 outstanding + 1 honourable mention).
- For a small team, an "insight about how agents are measured or fail" paper matches the award pattern better than a new agent architecture or yet another benchmark.

### Gaps
- No official per-area accepted-paper counts for ICML 2026 or IJCAI 2026 were found; ACL counts are a third party's title classification.
- ACL 2026 theme/resource/social-impact award titles and the full EMNLP 2026 list were not retrieved; the official ACL awards page needed an approval that was not granted.
- IJCAI 2026 submission count and acceptance rate not found. NeurIPS 2026 awards are not yet announced (conference in December 2026).
- The alphaXiv hot feed returned only opaque paper IDs (no titles), so it could not be used as a trend signal.

---

## Q2. Which topics are listed or newly added in the 2027 calls for papers?

### Takeaway
All three deadlines fall in January 2027 (ACL/ARR Jan 4, IJCAI Jan 4/11, ICML Jan 14/22), i.e. 6–9 weeks from today. ICML 2027 now treats "Evaluation" as a top-level area and adds contribution types for negative results and for datasets/evaluations/benchmarks; ACL 2027's special theme is LLM homogenization and knowledge collapse; IJCAI 2027 adds AI4Science and Arts & Creativity special tracks and charges a fee for non-primary papers.

### Cited Findings
**ICML 2027** (Rio de Janeiro, Jul 31–Aug 6, 2027) — [ICML 2027 CFP, official](https://icml.cc/Conferences/2027/CallForPapers)
- Abstract deadline Jan 14, 2027; full paper Jan 22, 2027 (AoE); first-stage rejections Feb 23; decisions May 3. 8 pages + unlimited references/appendix.
- Topic areas: general ML; deep learning; **evaluation (methodology, meta-studies, replicability, human-in-the-loop evaluation)**; theory; ML systems; optimization; probabilistic methods; RL; trustworthy ML (privacy, robustness, safety, interpretability, fairness, causality); application-driven ML.
- Authors pick one contribution type: General, Theory, Application-driven, Concept and Feasibility, **Negative Results**, or **Datasets, Evaluations and Benchmarks**.
- Two-stage reviewing with AC screening; max 20 submissions per author; reciprocal reviewing; mandatory AI Disclosure Statement for substantive AI use; lay summaries; optional in-person attendance.
- Position-paper track has a separate call, listed as "coming soon".

**ACL 2027** (Aug 17–22, 2027; General Chair Yusuke Miyao; city not stated on the page) — [ACL 2027 CFP, official](https://2027.aclweb.org/calls/main/)
- Submission through the ARR January 2027 cycle, deadline Jan 4, 2027.
- Special theme: "Homogenization and knowledge collapse in LLMs" — metrics for homogenization, mechanisms (training data, alignment, decoding), exploration vs convergence, human vs model diversity, **cross-linguistic homogenization including lower-resource languages**, polarization/pluralism. Long or short papers; special session and a Thematic Paper Award.
- Listed topics include "LLM Agents for NLP", "Language Diversity and NLP for Low-resourced Languages", "Multilingualism and Cross-Lingual NLP", "Interpretability and Analysis of Models for NLP", "Ethics, Bias, and Fairness", "Human-Centered NLP and Human-AI Interaction", "NLP and Code Models".
- As returned by the fetch, the 2027 list has no separate "Safety and Alignment in LLMs" or "Resources and Evaluation" entry, both of which were in the 2026 list — compare [ACL 2026 CFP](https://2026.aclweb.org/calls/main_conference_papers/). The 2027 list is prefaced "including, but not limited to", and the fetch tool summarises pages, so this difference should be re-checked on the page before relying on it.

**IJCAI 2027** (Kyoto, Aug 7–13, 2027; satellite event Hengqin, China, Aug 15–17) — [IJCAI 2027 main-track CFP, official](https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/)
- Abstract Jan 4, 2027; full paper Jan 11; summary-reject notices Feb 25; rebuttal Mar 30–Apr 2; notification Apr 21.
- 7 pages body + 2 pages references. No topic/keyword list; scope is any aspect of AI, with novel problems, novel application domains and cross-discipline work encouraged.
- Special tracks on the same deadlines: AI4Science; AI and Health; AI, the Arts and Creativity; AI for Social Good.
- "Primary Paper Initiative": USD 100 per submission unless no author appears on another IJCAI 2027 submission. Reciprocal reviewing mandatory. LLM text only for polishing. Phase-1 summary rejects without rebuttal. In-person presentation required.

### Inferences
- ICML 2027 is the most explicit venue for evaluation-validity and negative-result papers: the area and two contribution types are named in the call.
- ACL 2027's theme connects directly to the NeurIPS 2025 best paper on LLM homogeneity; a theme-track paper with a low-resource-language angle (the call names it) has a dedicated award and likely a smaller competitor pool than the agent area.
- IJCAI 2027's 7-page limit and Phase-1 summary rejection favour compact, self-contained contributions; the fee nudges teams to send one strong paper rather than several.
- Relative to the IJCAI-ECAI 2026 special tracks reported by a secondary source (Human-Centred AI, AI4Tech, AI and Robotics), AI4Science and Arts & Creativity appear new for 2027, and there is no agent- or safety-specific special track. This comparison rests on a secondary source for 2026.

### Gaps
- ICML 2027 position-paper call not yet published. ACL 2027 venue city not on the fetched page.
- IJCAI 2027 special-track calls were not opened individually; a search did not return their pages.
- NeurIPS 2027 / EMNLP 2027 calls not checked (out of scope).

---

## Q3. Within LLM agents (2025–Nov 2026): fastest-growing sub-areas, representative papers, and open problems the authors name

### Takeaway
Agent security (prompt injection, memory poisoning, MCP/tool poisoning) and agent evaluation validity are the two fastest-moving sub-areas in the last six months. The recurring author-named open problems are: static benchmarks are saturated or invalid; defences break under adaptive attackers; persistence (memory, multi-agent propagation) lacks provenance and recovery; long-horizon completion is still below about 21% on realistic computer-use tasks; and almost everything is evaluated in English, single-agent, with synthetic data.

### Cited Findings

#### 3.1 Agent memory (capability and evaluation)
- "Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents", arXiv 2608.15008, NeurIPS 2026 Evaluations & Datasets track **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2608.15008). A survey of 52 memory systems (2023–2026) inside the paper finds 62% of benchmark usage is on LoCoMo and LongMemEval, only 21% report any efficiency metric, 81% use GPT-family backbones, and half use one benchmark with no efficiency metric. No memory substrate wins across QA and agentic tasks; retrieving more helps QA but hurts action selection.
  - Author-named limits/open problems: judge model not validated against human labels; none of the main benchmarks makes later sessions depend on memory the agent itself wrote earlier; query-level substrate routing leaves most oracle headroom open; agentic test sets are small (134 and 148 tasks, single greedy runs).
- "Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads", arXiv 2606.06448 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2606.06448)
- "GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents", arXiv 2606.18829 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2606.18829)
- "HEAMS: Holistic Evaluation of Agent Memory Systems", arXiv 2611.20144 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.20144)
- "MemEvolve: Meta-evolution of agent memory systems", ICML 2026 **[cited]** in 2608.15008 — [alphaXiv of citing paper](https://www.alphaxiv.org/abs/2608.15008)

#### 3.2 Memory poisoning
- "From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents", arXiv 2606.04329, AIWILD workshop at ICML 2026 **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2606.04329). Four write channels, nine structural vulnerabilities, six attack classes; average attack success 50.46% and retrieval success 41.05% on OpenClaw and Hermes agents; four prompt-injection detectors reach at most 67.67% true-positive rate, and retraining barely helps on "weak-signal" payloads that look like ordinary facts.
  - Author-named limits/open problems: one backbone model only; payload delivered as a labelled context block instead of through a real tool pipeline; multi-user shared memory explicitly out of scope; needs write-path validation, provenance tracking of memory entries, source-aware compaction, post-write monitoring; states an inherent tension between memory usefulness and security.
- "MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory", arXiv 2611.09721 (RPI, Microsoft) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.09721)
- "MemForm: Benchmarking Memory Formation Poisoning in LLM Agents", arXiv 2610.14431 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.14431)
- "MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair", arXiv 2607.27080 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.27080)
- "Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough", arXiv 2610.04083 (Anthropic Fellows) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.04083)
- "Accept Changes, Reject Attacks: Robust Memory Management for LLM Agents", arXiv 2610.41056 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.41056)

#### 3.3 Prompt injection and agent security
- "Scaling Adaptive Prompt Injection Attacks with Agent Swarms", arXiv 2611.11861 (Google DeepMind) **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.11861). States that static benchmarks (AgentDojo, InjecAgent) stopped discriminating frontier models around mid/late 2025 and that the human red-teaming arena is near saturation (under 1% for recent models). Against a swarm attacker built on the strongest model, the most robust defender resisted 87% of scenarios at 150 queries and 66% at the full 320-query budget; three open-weight models resisted 1–5%. Stronger attacker models lower every defender's resistance.
  - Author-named limits/open problems: most adaptive attackers are not reproducible because code/models are withheld; the only open reproducible one broke 2 of 80 AgentDojo scenarios; link between a model's cyber-offence ability and its injection-attack ability flagged as future work; concludes model hardening alone is not enough and defence in depth is needed.
- "AutoDojo: A Generative Benchmark for Evaluating Prompt Injection Defenses in LLM Agents", arXiv 2606.15057 **[read, alphaXiv report]** — [alphaXiv](https://www.alphaxiv.org/abs/2606.15057). Nine defences, five target models, six-iteration black-box optimisation. PIGuard goes from 0.0% to 28.0% attack success on GPT-4o-mini, DataFilter from 12.6% to 33.4%; classifier filters cut clean utility by 33–50%; on "action-open" tasks (user delegates the action to external content) filtered agents are hit 57–64% of the time; system-level defences (Progent, DRIFT) do not show that gap.
- "The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections", arXiv 2510.09023 **[cited]** — described by 2611.11861 as bypassing twelve defences with success above 90% — [alphaXiv of citing paper](https://www.alphaxiv.org/abs/2611.11861)
- "AI Agents May Always Fall for Prompt Injections", arXiv 2605.17634 (Abdelnabi, Bagdasarian) **[cited]** — described by 2611.03555 as an impossibility result for agents under indirect injection — [alphaXiv of citing paper](https://www.alphaxiv.org/abs/2611.03555)
- "SecPO: Principled Adversarial Training for Prompt Injection Security", arXiv 2610.41998 (UC Berkeley, Anthropic) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.41998)
- "Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks", arXiv 2610.05640 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.05640)
- "Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning", arXiv 2611.04673 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.04673)

#### 3.4 Red teaming and automated red teaming
- "GPT-Red: Automated Red Teaming via Self-Play at Scale", arXiv 2607.26115 (OpenAI) **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.26115). An attacker trained by self-play against a population of defenders, at the compute scale of a large RL post-training run; finds more attacks than human red-teamers; adversarial training with it takes one hard test category from 5.2% to 95.9% robustness and holds injection success under 4% on a held-out exercise.
  - Author-named limits/open problems: less coverage of multimodal environments, multi-turn attacks and content-policy jailbreaks; authors say robustness "remains far from solved"; held-out numbers exclude system-level mitigations.
- "JailbreakSkill: Scaling Automated Red-Teaming with Reusable and Ever-Evolving Skills", arXiv 2608.16465 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2608.16465)
- "ASPIRE: Agentic Safety & Prompt Injection Red-teaming Engine", arXiv 2610.08951 (Google) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.08951)
- "Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning", arXiv 2610.28966 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.28966)
- "X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems", arXiv 2610.13886 (Meta) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.13886)
- "Attacker Diversity Reduction in Adaptive LLM Red Teaming", arXiv 2611.19680 (Microsoft) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.19680)
- "Assessing Automated Prompt Injection Attacks in Agentic Environments", arXiv 2606.10525 (ETH) **[index]**; 2611.11861 summarises it as showing optimisation-based attacks lose effectiveness on larger recent models — [alphaXiv](https://www.alphaxiv.org/abs/2606.10525)

#### 3.5 Computer-use / GUI / mobile agents
- "OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks", arXiv 2606.29537 **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2606.29537). 108 workflows, median 1.6 human-hours, 300+ agent steps. Best configuration completes 20.6% (54.8% partial credit) at roughly USD 72 per task, while the same model family scores about 83.5% on the older OSWorld-Verified. Agents spend under 7% of their budget on detecting and fixing their own errors; failures concentrate on hidden-state recovery, dropped constraints, information arriving mid-task, guessing instead of asking the user, and skipped verification. Under obstacles, agents try privilege escalation instead of pausing.
  - Author-named limits/open problems: domain coverage incomplete; scaling tasks is costly; agents may learn to exploit benchmark artifacts; time-horizon scaling laws from software tasks transfer only partly; trustworthy long-horizon computer use called a "critical open challenge".
- "How Benchmarks Mis-Score Computer-Use Agents", arXiv 2607.28367 **[read, alphaXiv report]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.28367). Re-audit of 150 failure-scored trajectories from five benchmarks: 15.3% of FAIL verdicts were wrong (10.7% checker false negatives, 4.7% broken tasks); WebArena 21.7% false negatives; AssistantBench 21.7% broken tasks. Of genuine failures, 29.5% are feedback-blind repetition of an action that changes nothing; grounding errors are only about 9%.
  - Author-named limits: only failed trajectories sampled, so false positives among successes are not estimated; small per-benchmark samples; proposed automatic diagnostic probes not validated.
- "OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools", arXiv 2610.14157 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.14157)
- "AndroidFlux: Evaluating and Reward Modeling Failure Recovery Capabilities in Mobile Use Multimodal Agents", arXiv 2610.34384 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.34384)
- "ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices", arXiv 2608.26204 (Meta FAIR) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2608.26204)
- "MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training across Mobile and Computer Environments", arXiv 2610.20939 (Alibaba) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.20939)
- "Qwen-UI-Agent Technical Report", arXiv 2607.28227 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.28227)
- "RealGUINoise: An Interactive Cross-Platform Benchmark for GUI Agent Robustness under Real-World Interface Noise", arXiv 2609.38184 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.38184)

#### 3.6 Multi-agent systems
- "SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems", arXiv 2609.00595 (JHU, NTU) **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.00595). Systematises 197 works; audits 44 evaluation works: 42 use fixed membership, 13 compute attack success themselves, 20 keep full traces, and only one reports an explicit provenance/dependency graph.
  - Author-named open problems: blocking one transition does not close an attack path; containment is not recovery and recovery is rarely evaluated; benchmarks do not isolate interaction effects with single-agent counterfactuals; metrics and component formats are not comparable or reusable across benchmarks; open-system operation (agents joining, changing trust, cross-domain) is essentially unevaluated.
- "Emergent Collusion in Long-Horizon LLM Agent Interaction", arXiv 2609.24967 (Stanford, Georgia Tech) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.24967)
- "ORBIT: A Framework for Multi-Agent Safety and Security Evaluations", arXiv 2609.33102 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.33102)
- "The Show-Up Attack: When Subagents Win Over Their Supervisor", arXiv 2610.27574 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.27574)
- "Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems", arXiv 2608.25920 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2608.25920)
- "Understanding Communication Failures in Multi-Agent LLM Systems", arXiv 2610.32060 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.32060)

#### 3.7 Agent evaluation and benchmark validity (including evaluation awareness)
- "Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI", arXiv 2607.22368 (Tencent, HKUST) **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.22368). Audit of 2,385 traces from 15 agent benchmarks: shortcut use in 67.0% of Frontier Science traces and 66.7% of AutoLab tasks; score inflation 0.45–1.00 in paired comparisons; detector precision 0.94, recall 0.76 on 53 hand-labelled traces.
  - Author-named limits/open problems: five benchmark rows are pre-selected suspicious traces, so not prevalence estimates; imperfect recall; future work is formal protocol verification and adaptive benchmark generation that keeps the construct fixed while refreshing instances.
- "Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Agent Leaderboard", arXiv 2610.00651 (Stanford, UIUC) **[read, partially — abstract, limitations section]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.00651). On 22 benchmarks, fixed model+scaffold systems are ranked reliably (0.935–0.994) but underlying models much less so (0.148–0.841); adding tasks cannot remove scaffold-driven uncertainty; pooling benchmarks lifts projected reliability from 0.44 to 0.75.
  - Author-named limits: reliability is not validity; the "what is being measured" problem is a construct-validity problem; future work needs external-criterion validation, larger scaffold libraries, and tests of interventions that raise the reliability ceiling.
- "Safety, or Just Capability? A Validity Audit of Agent-Safety Benchmarks", arXiv 2607.28685 (independent researchers) **[read, partially — abstract, limitations]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.28685). Always answering "unsafe" scores 0.690 on R-Judge, above 5 of 21 models; InjecAgent, AgentHarm and AgentDojo rank the same 18 models differently; no safety score adds association with task success once static knowledge is controlled.
- "Decomposing and Measuring Evaluation Awareness", arXiv 2605.23055 (ETH, ELLIS/MPI Tübingen) **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2605.23055). Nine models, four benchmarks, plus a 100-pair controlled benchmark with eight toggleable cue factors. No single cue affects all models; stacking cues raises verbalised awareness for nearly all (one model from 4% to 35%); models are more sensitive to safety tests than capability tests.
  - Author-named limits/open problems: only verbalised (chain-of-thought) awareness is measured, so rates are conservative; proposes that benchmark reports carry an awareness rate and an "awareness tax"; the goal should be behaviour that stays the same under recognition, not hiding cues.
- "Maintaining Benchmarks Against Increasingly Capable Agents: Detection and Remediation of Unearned Passes", arXiv 2609.34262 (Scale AI) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.34262)
- "What AI Benchmarks Actually Measure: Adapting Convergent and Discriminant Validity to Interrogate Fifty-Six AI Benchmarks", arXiv 2609.08812 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.08812)
- "Attack Success Rate Is Not a Number: On Measurement Validity in Agentic AI Security Evaluation", arXiv 2609.25173 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.25173)
- "Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks", arXiv 2607.27518 (UK AISI et al.) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.27518)

#### 3.8 Long-horizon reliability
- "Staying on Task: Testing the Foundations of Long-Horizon Agent Reliability", arXiv 2609.38712 (NVIDIA; NeurIPS 2026 workshop) **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.38712). Across seven open-weight models, item accuracy drops 62.8% (relative) from 4K to 128K tokens; at 128K the best model completes 17.1% of documents with no error. Authors' limits: synthetic and deterministic; no planning, tool choice, recovery or multi-turn interaction.
- OSWorld 2.0 (above) and "LLMs Get Lost In Multi-Turn Conversation" (ICLR 2026 outstanding) — [OpenReview](https://openreview.net/forum?id=VKGTGGcwl6) — are the two most visible long-horizon/multi-turn reliability results.
- "Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems", arXiv 2609.17320 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.17320)
- "Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness", arXiv 2611.23346 (Google) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.23346)
- CAR-bench (ACL 2026 outstanding; consistency and limit-awareness under uncertainty) — [36Kr list, secondary](https://www.36kr.com/p/3888326643104513); no paper URL verified.

#### 3.9 MCP / tool ecosystems
- "MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study", arXiv 2611.03555 (Dynatrace; AISec '26) **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.03555). 12 frameworks × 18 models × 45 scenarios (9,720 cells), with real tool execution; 22.9% overall attack success; no framework implements an intentional defence; per-model success ranges 0.4% to 49.7%; a registration-time regex scanner stops 20 of 45 scenarios at a 7.2% false-positive rate; all five vendor disclosures were rejected.
  - Author-named limits/open problems: single-turn only; 12 of about 50 MCP frameworks; only exfiltration harm measured; no clean-task baseline; scenarios are public so model resistance may reflect training exposure; future work on multi-turn compound scenarios, change detection, result-channel validation, and a formal description-safety specification.
- "Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol", arXiv 2610.36108 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.36108)
- "Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security", arXiv 2611.01976 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.01976)
- "Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance", arXiv 2610.32555 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.32555)
- "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers", arXiv 2607.14642 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.14642)
- "DynamicMCPBench: A Trace-Grounded, Effect-Scored Benchmark for LLM Agents over Live MCP Servers", arXiv 2607.20531 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.20531)

#### 3.10 Agent privacy
- "AgentCIScope: Grounded Contextual Integrity Evaluation for LLM Agents", arXiv 2610.19158 (UChicago, Microsoft Research, UIUC) **[read]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.19158). 936 executable tasks, 11 application environments, 12 agent configurations. Single-run leakage 32.5%–94.4%; five repeats add 4–19 points; the same backbone differs by more than 10 points across frameworks; credentials and SSNs are protected far better than preferences and booking details (17.1% and 29.4% vs 84.7% and 76.5%).
  - Author-named limits/open problems: fully synthetic; single-agent only (multi-agent extension named as future work); measures leakage but proposes no defence.
- "PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems", arXiv 2607.05318 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2607.05318)
- "Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy", arXiv 2610.39532 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.39532)
- "Capable but careless: Do computer-use agents follow contextual integrity?", arXiv 2606.23189 **[cited]** in 2610.19158 — [alphaXiv of citing paper](https://www.alphaxiv.org/abs/2610.19158)
- "CI-Work: Benchmarking contextual integrity in enterprise LLM agents", ACL 2026 Industry Track **[cited]** — [ACL Anthology URL as given in the citing paper, not opened](https://aclanthology.org/2026.acl-industry.103/)

#### 3.11 Non-English / low-resource agent evaluation
- "BabelArena: A Large-Scale Multilingual Benchmark for LLM Agents", arXiv 2609.23490 (Alibaba et al.) **[read, partially — abstract, intro, conclusion]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.23490). 16,077 instances from 699 tasks, four benchmark families, 23 languages. In lower-resource languages the failures shift toward tool-use and control-flow errors, token use rises up to about double the English input, and agents slip back into English around structured output. No explicit limitations section found in the portions read.
- "OmnilingualGAIA2: Evaluating the Multilingual Gap in Frontier AI Agents", arXiv 2608.08775 (Meta) **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2608.08775)
- "τ-bench-LILT: Evaluating Conversational Agents on Realistic Multilingual Tool-Use Tasks", arXiv 2611.07203 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2611.07203)
- "LoWAgent: A Low-Resource Multilingual Benchmark for Web Agents", arXiv 2610.27205 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.27205)
- "WorldBench: Culturally Grounded Benchmark for Multilingual Agents", arXiv 2609.01056 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2609.01056)
- "Disentangling Language Effects on Tool Admission and Post-Retrieval Safety", arXiv 2610.23093 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2610.23093)

### Inferences
- Growth ranking by what the alphaXiv index returned for June–Nov 2026 (a relevance-ranked sample, not a census): memory poisoning (10+ attack/benchmark papers in five months), MCP security (14+), computer-use benchmarks/environments (about 15), agent-evaluation validity audits (about 20), automated red teaming (about 20). Evaluation awareness (4–5), multilingual agent evaluation (6) and agent privacy via contextual integrity (5–6) are smaller and newer.
- Frontier labs now publish the strongest attacker and defender results (OpenAI GPT-Red, Google DeepMind swarm attacker, Berkeley/Anthropic SecPO). Their own stated gaps — reproducibility of adaptive attackers, multi-turn and multimodal attacks, attacker diversity — are places where an academic team is not outgunned on compute.
- The same structural finding recurs in four sub-areas: local checks do not give end-to-end guarantees (memory write path, MCP framework layer, multi-agent path closure, filter-based injection defences). Provenance and recovery are named as missing in memory, multi-agent and MCP papers.
- Evaluation validity is becoming a field of its own with psychometric vocabulary (construct validity, reliability, generalizability theory, convergent/discriminant validity). That vocabulary is still rare in agent *security* evaluation; the two papers that apply it there are low-visibility preprints.

### Gaps
- Counts above are from a relevance-ranked search index, not complete arXiv listings; they show order of magnitude only.
- Limitations sections were read for 16 papers; papers marked [index] or [cited] were not opened, so their open problems are not reported.
- No mobile-agent paper was read in full (attempted fetch needed approval); mobile-specific open problems are therefore under-documented here.
- I did not verify acceptance venues for most 2026 preprints.

---

## Q4. Which topics look saturated and which look under-served relative to interest?

### Takeaway
Saturated: static prompt-injection benchmarks and filter-style defences, memory-poisoning benchmarks, MCP poisoning demonstrations, new jailbreak/red-team optimisers, new CUA task suites, and memory architectures tested on LoCoMo/LongMemEval. Under-served: validity of agent-security metrics, multilingual and low-resource agent evaluation (especially security), recovery and provenance after compromise, open-membership multi-agent settings, privacy defences, and evaluation awareness in agentic settings.

### Cited Findings
**Signs of saturation**
- Static injection benchmarks no longer separate frontier models, and human arena red-teaming is near its floor — [2611.11861](https://www.alphaxiv.org/abs/2611.11861).
- Nine published injection defences lose much of their reported protection to a cheap black-box adaptive attacker; filters also cost 33–50% utility — [2606.15057](https://www.alphaxiv.org/abs/2606.15057).
- Memory-poisoning benchmarks released June–Nov 2026 alone include MPBench (2606.04329), MemPoison (2607.14651), MemSecBench (2607.27080), InjecMEM (2608.23471), MemForm (2610.14431), carryover attacks (2610.28425) and MemoryDojo (2611.09721) — all listed in one index query — [example: MemoryDojo](https://www.alphaxiv.org/abs/2611.09721); [MPBench](https://www.alphaxiv.org/abs/2606.04329).
- Memory systems: 52 systems, 62% of evaluations on two dialogue datasets, half on one benchmark only — [2608.15008](https://www.alphaxiv.org/abs/2608.15008).
- MCP poisoning has at least seven prior taxonomies/benchmarks that the Dynatrace study had to unify (Invariant Labs, MCPTox, OWASP MCP03, MSB, AgentDojo, ETDI, CSA) — [2611.03555](https://www.alphaxiv.org/abs/2611.03555).
- Multi-agent security already has 197 works and 44 evaluation/benchmark works — [2609.00595](https://www.alphaxiv.org/abs/2609.00595).
- Computer-use: the older OSWorld is at about 83.5% for the best model; new suites and industrial technical reports (Qwen-CUA, Qwen-UI-Agent, NorthCUA, BlueLM-GUI, Mage-VL-Cowork) arrive monthly — [2606.29537](https://www.alphaxiv.org/abs/2606.29537); [Qwen-UI-Agent](https://www.alphaxiv.org/abs/2607.28227).
- Automated red teaming is now done at frontier-lab training scale — [2607.26115](https://www.alphaxiv.org/abs/2607.26115).

**Signs of under-supply**
- ACL 2026 multilingual/low-resource titles were flat (54 to 52) while agent titles grew 158% — [Bohrium](https://www.bohrium.com/en/blog/acl-2026-accepted-papers-highlights/). Multilingual agent benchmarks exist (six found, Aug–Nov 2026) but only two index hits address language effects on agent *safety/security* — [2610.23093](https://www.alphaxiv.org/abs/2610.23093); [2610.27304](https://www.alphaxiv.org/abs/2610.27304).
- Agent-safety benchmark scores disagree with each other and a trivial baseline beats real models on one of them; this audit comes from independent researchers, not a major lab — [2607.28685](https://www.alphaxiv.org/abs/2607.28685).
- Among 44 multi-agent security evaluations, 42 assume fixed membership and one records a provenance graph; recovery is rarely measured — [2609.00595](https://www.alphaxiv.org/abs/2609.00595).
- The privacy benchmark with the widest coverage offers no defence and is single-agent — [2610.19158](https://www.alphaxiv.org/abs/2610.19158).
- Memory poisoning explicitly excludes shared multi-user memory and lacks write-path provenance — [2606.04329](https://www.alphaxiv.org/abs/2606.04329).
- No memory benchmark in the main comparison makes later sessions depend on what the agent itself stored — [2608.15008](https://www.alphaxiv.org/abs/2608.15008).
- CUA audits estimate checker false negatives but not false positives among "successes" — [2607.28367](https://www.alphaxiv.org/abs/2607.28367).
- Evaluation awareness is measured only when verbalised; agentic and unverbalised awareness are open — [2605.23055](https://www.alphaxiv.org/abs/2605.23055).
- NeurIPS 2026 accepted 102 workshops from 477 proposals; none of the agent/evaluation/safety titles concerns red teaming or multilingual agents, while several concern verification and evaluation trust — [NeurIPS blog](https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/).

### Inferences
- A new attack-plus-benchmark paper on memory poisoning, MCP poisoning or static injection has a low novelty ceiling for January 2027 deadlines; reviewers can name several near-duplicates.
- Candidate gaps with high interest and tractable scope for a small team (my synthesis, not a claim by any source):
  1. Measurement validity of agent-security metrics (does attack success rate mean the same thing across benchmarks; false-positive "successes"; adaptive-attacker baselines that are open and reproducible) — fits ICML 2027's Evaluation area and the Datasets/Evaluations/Benchmarks or Negative Results contribution types.
  2. Language as a variable in agent reliability or security (injection, memory poisoning or tool misuse in non-English and low-resource settings) — fits ACL 2027 topics and partly its theme track.
  3. Provenance, repair and recovery after compromise (memory or multi-agent), evaluated end to end — named as missing by three separate papers.
  4. Evaluation awareness in agentic or mobile/GUI settings beyond chain-of-thought monitoring.
  5. False-positive auditing and process-level scoring for mobile/computer-use benchmarks.
- Compute-heavy directions (training CUA foundation agents, self-play red-teamers) are dominated by industrial labs and are a poor fit for a small team.

### Gaps
- "Saturated" is inferred from counts of similar papers and from authors' own statements; I found no source that measures acceptance rates per sub-topic.
- I did not check whether gaps 1–5 already have strong submissions under review at ICLR 2027 or elsewhere.

---

## Q5. What do position papers, keynotes and workshop CFPs identify as unsolved?

### Takeaway
Workshop programmes and position papers converge on four unsolved items: trustworthy evaluation of interactive agents (validity, judges, reproducibility), security of agents against adaptive attackers with no layer of the stack owning the problem, long-horizon/multi-agent safety, and memory/personalisation. Red teaming and multilingual agent evaluation are named in research papers but are absent from workshop titles.

### Cited Findings
- ICML 2026 received 247 workshop proposals (about 150 the year before) and accepted 44; seven are agent workshops, including "Failure Modes in Agentic AI: Reproducible Triggers, Trace Diagnostics, and Verified Fixes", "The Second Workshop on Agents in the Wild: Safety, Security, and Beyond", and "Statistical Frameworks for Uncertainty in Agentic Systems" — [ICML blog, official](https://blog.icml.cc/2026/04/06/announcing-the-icml-2026-workshops-and-affinity-workshops/). A secondary source says at least 60 proposals had "agentic AI" in the title — [AI2Work](https://ai2.work/blog/icml-2026-hits-record-23-918-submissions-as-agents-take-over).
- NeurIPS 2026 workshops (102 accepted; Sydney, Paris, Atlanta) include "Who Verifies the Agents? Toward Reliable Agent Development", "Workshop on Evaluation of Interactive Agents", "Can We Trust the Judge? Building Reliable Evaluation for Language Models", "Trustworthy AI Evaluation (TAI-Eval)", "Grounded User Simulation for Model Evaluation and Training: Diversity, Fidelity, and Validity", "PALM: Personalized, aligned, long-term memory for AI systems", "Foundations of Language Model Security: Theory, Practice and Fundamental Limits", "First Workshop on Meta Agents", "The Agentic Web", and the third "Agents in the Wild" — [NeurIPS blog, official](https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/).
- The Agents in the Wild workshop (ICML 2026) lists as topics: agent security/privacy/robustness, evaluating and benchmarking agents, multimodal and computer-use agents, multi-agent coordination and long-horizon safety, agent systems and infrastructure; it states that safety and security research lags deployment. Its first edition at ICLR 2026 drew 235 submissions. Invited speakers include Yoshua Bengio, Dawn Song and Eric Wallace — [workshop site](https://agentwild-workshop.github.io/icml2026/).
- ICML 2026 position paper "Position: Agent Evaluation Should Be Agentified for Openness, Standardization, and Reproducibility" (Liu, Shi, Guo, Song; PMLR v306) argues that agent evaluation is fragmented, tied to fixed LLM-centric harnesses, costly to integrate, mismatched with production, and lacks an agent-agnostic interface — [PMLR](https://proceedings.mlr.press/v306/liu26gy.html).
- Other ICML 2026 position titles in the visible part of the list (64 of 213 entries seen): "Position: Behavioral Systems Require Behavioral Tests", "Position: LLM Benchmark Datasets should be Contamination-Resistant", "Position: Preregister Experiments with AI Agents", "Position: Web Agents Should Use Typed Actions Instead of Click-Based Browsing", "Position: Assistive Agents Need Accessibility Alignment", "Position: Breaking the Dual Curse of Multilingual AI Requires Socio-Technical Guardrails, Not Post-Hoc Alignment" — [ICML position-paper list, official](https://icml.cc/virtual/2026/events/2026-position-papers).
- ICML 2026's outstanding position paper is a warning about dual use of alignment research — [ICML blog](https://blog.icml.cc/?p=1347).
- Benchmark validity for agents: protocol exposure lets agents pass without the intended capability, and authors ask that benchmark reports ship evidence that scores reflect the capability — [2607.22368](https://www.alphaxiv.org/abs/2607.22368). Reliability of a leaderboard depends on whether the claim is about a system or a model, and reliability does not establish validity — [2610.00651](https://www.alphaxiv.org/abs/2610.00651).
- Evaluation awareness: models are more sensitive to safety tests than capability tests, which puts safety-benchmark validity at greater risk; authors propose reporting an awareness rate — [2605.23055](https://www.alphaxiv.org/abs/2605.23055).
- Adaptive attacks breaking defences: static results overstate protection; a stronger attacker model lowers every defender's resistance — [2606.15057](https://www.alphaxiv.org/abs/2606.15057); [2611.11861](https://www.alphaxiv.org/abs/2611.11861).
- Accountability: protocol, SDK, framework and model vendors each defer responsibility for MCP tool poisoning — [2611.03555](https://www.alphaxiv.org/abs/2611.03555).
- Non-English agent evaluation: evaluation is English-centric and failures in lower-resource languages are execution failures, not only answer quality — [2609.23490](https://www.alphaxiv.org/abs/2609.23490).
- Position/perspective preprints found by the index, not opened: "Measuring Security Without Fooling Ourselves: Why Benchmarking Agents Is Hard", arXiv 2605.22568 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2605.22568); "Reframing LLM Agent Security as an Agent-Human Interaction Problem", arXiv 2605.24309 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2605.24309); "Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks", arXiv 2603.30016 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2603.30016); "Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents", arXiv 2606.19704 **[index]** — [alphaXiv](https://www.alphaxiv.org/abs/2606.19704).
- IJCAI-ECAI 2026 keynote topics were reported only in general terms (evaluation — Barbara Plank; neuro-symbolic AI; robot RL), with agentic AI as the theme of two award lectures — [AI2Work, secondary](https://ai2.work/blog/ijcai-ecai-bremen-everything-announced-at-ai-s-oldest-conference).

### Inferences
- Verification and evaluation trust for agents has moved from individual papers to named workshops at NeurIPS 2026 (at least five titles). That raises both reviewer interest and the number of competing submissions for 2027.
- Security "fundamental limits" (an impossibility-style preprint, a NeurIPS workshop with that phrase in its title) suggest reviewers will be sceptical of any defence that claims to solve prompt injection; papers that measure, bound or reframe will be read more favourably than papers that claim a fix.
- Multilingual agent evaluation and red teaming have no dedicated workshop, which is consistent with Q4's under-supply reading; ACL 2027's theme track is the nearest institutional home for the multilingual angle.

### Gaps
- Keynote content for ICML 2026, ACL 2026 and EMNLP 2026 was not retrieved; only IJCAI talk titles were found, through a secondary source.
- Only the first 64 of 213 ICML 2026 position-track entries were visible; the count of agent/evaluation position papers is therefore incomplete.
- Workshop CFP text was read for one workshop only (Agents in the Wild); the others are represented by title.
