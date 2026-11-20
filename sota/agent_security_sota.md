# Security, red teaming and evaluation of LLM-based agents (2024 – 20 Nov 2026): memory-persistent agents and mobile / GUI / computer-use agents

**How to read these notes (scope and verification).**
- Every paper below was verified in this session against its arXiv record (arXiv export API: title, authors, dates, abstract, comment/journal fields). Identifiers are arXiv IDs; links are `https://arxiv.org/abs/<id>`.
- Depth of reading: for 28 papers I also downloaded the PDF and searched the full text (marked **[FT]**); for all others the extraction is **abstract-level only** (marked **[abs]**), so "limitations" cells say what the abstract admits, not what the paper's limitation section says.
- Venue is given only when the arXiv comment/journal field or the PDF header states it. "arXiv only" means I saw no venue in the record; it does not mean the paper is unpublished.
- All numbers are self-reported by the authors unless stated. Papers from Oct–Nov 2026 are days-to-weeks-old preprints with no peer review and few readers; treat them as evidence that a topic is being worked on, not as settled results.
- Attacks are described at abstract level only; no payloads are reproduced.
- Model names in 2026 abstracts (e.g. "GPT-5.6-Luna", "Claude Opus 4.8", "Fable 5") are quoted as the sources print them.

---

## 1. Memory attacks and defences (poisoning / injection / cross-session persistence; provenance, sanitisation, trust scoring; benchmarks)

### Takeaway
Memory security went from two reference attacks (AgentPoison 2024, MINJA 2025) to a crowded 2026 literature with at least eight dedicated benchmarks and a dozen defences; the attacks that matter now are indirect, single-exposure, cross-session attacks on real harnesses (OpenClaw, Claude Code, Codex, Hermes), which reach roughly 50–100% success undefended. The lowest reported attack rates come from architectural defences that separate "being remembered" from "having authority" (zoning, provenance labels, confirmation gates), but there is no common adaptive evaluation: the one detection-style defence that became a standard baseline (A-MemGuard) is already reported bypassed, and the newest benchmark (MemoryDojo) explicitly leaves systematic defence evaluation to future work.

### Cited Findings

**Extraction table — attacks**

| ID | Paper, venue | Problem / threat model | Method | Evaluation (as reported) | Stated limitations / open problems | Artifacts |
|---|---|---|---|---|---|---|
| 2407.12784 [FT] | AgentPoison (arXiv Jul 2024; venue not in record) | Backdoor of RAG/memory agents; attacker injects a few poisoned records and needs white-box access to the embedder | Constrained optimisation of a trigger that maps triggered queries to a unique embedding region | 3 agents (Agent-Driver, ReAct-StrategyQA, EHRAgent); avg ASR >80%, benign impact <1%, poison rate <0.1% | Requires white-box embedder (authors argue triggers transfer across embedders) | not checked |
| 2503.03704 [FT] | MINJA (arXiv Mar 2025, rev. Feb 2026) | Query-only injection: attacker is an ordinary user with no write access to the memory bank | Bridging steps + indication prompt + progressive shortening | "Diverse agents"; follow-up work quotes >95% injection success and 70% ASR under idealised conditions | Assumes shared memory, or isolated memory with feasible identity disguise | "Code released" |
| 2506.17318 [abs] | Context manipulation / plan injection (arXiv Jun 2025) | Client-side or third-party-managed memory of web agents | Plan injection, context-chained injection | Browser-use, Agent-E; up to 3x ASR of prompt-based attacks; +17.7% on privacy exfiltration | — | — |
| 2512.16962 [abs] | MemoryGraft (arXiv Dec 2025) | Attacker supplies benign-looking artefacts the agent reads; poisoned "successful experiences" persist | Exploits imitation of retrieved experiences | MetaGPT DataInterpreter + GPT-4o only | Single agent/model | code + data |
| 2602.15654 [abs] | Zombie Agents (ICLR 2026 Lifelong Agent workshop) | Black-box, indirect exposure via attacker web content; payload survives sessions | Mechanism-specific persistence for sliding-window and RAG memory | "Representative agent setups" | Concludes per-session filtering is insufficient | — |
| 2605.01970 [FT] | Trojan Hippo Bench (AISec '26, The Hague, per PDF header) | One untrusted tool call (e.g. an email) plants a dormant payload that fires on sensitive topics and exfiltrates data | Dynamic benchmark + OpenEvolve-based adaptive red-teaming + security–utility analysis | Email assistant, 4 memory backends (explicit tool memory, agentic memory, RAG, sliding window); undefended ASR up to 85–100% on frontier OpenAI/Google models; payloads still fire after 100 benign sessions; 4 defences cut ASR to 0–5% | Utility cost of defences varies widely with task mix; "effective real-world deployment remains an open challenge" | released |
| 2605.26154 [abs] | MemMorph (preprint) | Bias tool selection by poisoning long-term memory with records disguised as facts/policies | — | 3 benchmarks, 10 backbones, 3 memory modules; up to 85.9% ASR with 3 records; survives 3 defences | — | — |
| 2605.29960 [abs] | MemPoison (ACM CCS 2026) | Realistic pipelines that extract/rewrite before storing; dialogue-only attacker | Semantic bridge, entity masquerading, joint embedding optimisation | ASR up to 0.95 across agent domains and memory mechanisms | Evaluated defences have "fundamental limitations" | code |
| 2607.14651 [abs] | MemPoison (Nanjing; different paper, same name) | Three tiers: direct, compositional multi-record, context-triggered dormant | Mechanistic influence decomposition | 7 open + 3 closed model families | Write-time consistency checks stop tier 1 but not tiers 2–3 | — |
| 2608.01637 [abs] | Salami Attack / MemCollusion | Individually benign memories that are jointly harmful | Fine-tuned generator, 5 strategies | OpenClaw, 2 backbones, 48 scenarios; save rate 81.3%, ASR 75.0%; survives dilution and memory-level defences | — | — |
| 2608.23471 [abs] | InjecMEM (COLM 2026) | Single interaction, no read/edit access | Retriever-agnostic anchor + gradient-searched command | Multiple memory systems and backbones | — | "reproducible framework" |
| 2609.00523 [abs] | PipePoison | Indirect poisoning must survive write → retrieve → use | End-to-end optimisation with shadow systems | 3 frameworks, 4 memory mechanisms; +19.1 pp utilisation; +16 pp on unseen configs; "remains effective under eight representative defenses" | — | — |
| 2609.13889 [abs] | PMPA | Malicious instructions in benign external sources get written to persistent memory | — | OpenClaw: 73.7% injection / 55.5% cross-session ASR; Claude Code: 66.9% / 81.7% | Prompt-level defence helps before the write, little after | code |
| 2607.05029 [abs] | FARMA + SENTINEL | Poison the agent's remembered reasoning, not facts | Forged traces + self-referential reinforcement | 50 trials; up to 100% ASR; "capable of defeating ... keyword filter and A-MemGuard" | Small scale | — |

**Extraction table — benchmarks**

| ID | Benchmark, venue | Size and setting | Headline result | Stated limitations |
|---|---|---|---|---|
| 2410.02644 [abs] | ASB (ICLR 2025) | 10 prompt-injection attacks, 1 memory-poisoning attack, PoT backdoor, 11 defences, 13 backbones | Highest average ASR 84.30% | Memory is one attack among many |
| 2606.04329 [FT] | MPBench | 3,240 attack cases + 2,997 benign; 6 attack classes, 7 domains; OpenClaw and Hermes with GPT-OSS-120B | Agents that write/retrieve more aggressively are more exploitable; off-the-shelf prompt-injection detectors had TPR 23–68% on memory poisoning (table as parsed from the PDF) | Single backbone; authors call for defences on the write path |
| 2607.14611 [abs] | Bad Memory (U. Washington) | Claude Code and Codex; 4 models; sandboxed synthetic workspace | Hard to make an agent overwrite memory from untrusted content, but planted payloads attack current and future sessions | Synthetic workspace |
| 2607.27080 [abs] | MemSecBench | 310 cases, 48 contexts; 24 configs (2 harnesses x 4 memory backends x 3 LLMs); Write–Execute–Forget protocol | Persistence in 84.2% of cases; full write–execute chain 50.3%; selective repair 56.1% | Contrasts are descriptive |
| 2610.14431 [abs] | MemForm | 5 formation interfaces (content, evidence, scope, selection, path); 6 LLMs | Susceptible at all five; consolidation order alone changes behaviour; defences incomplete | Controlled diagnostic protocol |
| 2610.28425 [FT] | CarryoverBench (EMNLP 2026 main) | 12 personal-assistant scenarios, 101 attack tasks, 3 trigger channels; 5 frontier models; second runtime (Hermes) | No measurable decay over five rounds; Hermes attenuates to 2.8–27.8% ASR but does not eliminate; its pattern scanner matched 0/89 payload files | Non-reasoning models only; textual defences share a structural limit |
| 2611.01700 [FT] | MemHarmBench | Victim-centric (user / workspace owner / external party); attack content removed before the test session | Cross-session attacks are behaviourally stealthy: task completes, no anomaly | Outcomes are decision-level proxies; trigger rates conditional on retention; visual tests use one configuration |
| 2611.09721 [FT] | MemoryDojo (RPI + Microsoft) | 155 multi-session trajectories, 4 domains, 5 memory systems (A-MEM, Graphiti, Letta, Mem0, Memora) | All five susceptible, with large variation; memory-aware poison optimisation raises efficacy | Future work: multiple poisonings per trajectory and "systematically evaluate memory defenses" |

**Extraction table — defences**

| ID | Defence | Idea | Reported result | Adaptive evaluation? |
|---|---|---|---|---|
| 2510.02373 [FT] | A-MemGuard (arXiv Sep 2025) | Consensus validation over related memories + separate "lessons" memory | >95% ASR reduction; ReAct-StrategyQA, EHRAgent, MMLU; GPT-4o-mini, Llama-3.1-8B | None found in my full-text search; later reported bypassed by FARMA |
| 2601.05504 [abs] | Trust-scored moderation + sanitisation with temporal decay | EHR agents, MIMIC-III; 3 models | Pre-existing legitimate memories sharply reduce MINJA; threshold calibration is the hard part | Authors frame results as baselines for adaptive work |
| 2605.23723 [abs] | MemAudit | Post-hoc counterfactual influence + consistency graph | MINJA ASR 70% → 0% (QA), 83.3% → 0% (RAP) | Only against MINJA |
| 2607.28103 [abs] | MIND | Intent-aware information bottleneck detector | −58.1% / −53.5% mean ASR on ReAct-StrategyQA | not stated |
| 2607.29167 [abs] | PPMF (provenance-preserving firewall) | Names "memory provenance laundering": consolidation rewrites an external observation as user history | Vulnerable consolidated memories reach ASR 1.000; no unauthorised high-risk action passes the gate when provenance labels are intact | Schema-grounded evaluation with fixed policies |
| 2610.00450 [abs] | ZoneClaw | Hierarchical trust zones; no process both ingests external content and acts outward | ASR 372/480 → 6/480, utility retained in 458/480; 4 scenarios, 4 backbones | "remains effective against some defense-aware attackers" |
| 2610.22959 [abs] | SAFE-Mem | Claim-level labels (kind, authority, scope) + governance-aware retrieval | Lowest ASR among utility-preserving defences on MPBench and LoCoMo; +15 points accuracy | not stated |
| 2610.28987 [abs] | PerMIT | Finite memory interface; two integrity theorems machine-checked in Lean 4; confirmation gate; community endorsements | Zero observed attack success on Trojan Hippo | Guarantee holds under an explicit trust assumption; reduces every attack to a gate decision by a human or verifier |
| 2610.13267 [abs] | DREAM | Training-free "forgetting" via reactivation | >95% ASR reduction on backdoor poisoning; 2.13x faster than A-MemGuard | not stated |
| 2610.41056 [abs] | Robust memory manager | Treats outdated memory and poisoning jointly; new metric (evidence-conditioned accuracy) | Existing systems and defences no better than an untuned manager; fine-tuning doubles ECA; "robustness remains incomplete" | — |
| 2611.25583 [abs] | DriftGuard | Offline counterfactual supervision, online risk model | qualitative | — |
| 2610.28093 [abs] | ClawMMU (NeurIPS 2026 AgenticOS workshop, non-archival) | Labels on owner, scope, origin, authority checked at every boundary | design paper, 6 pages | — |

- The strongest attack evidence on deployed-style systems: Trojan Hippo reports 85–100% undefended ASR on frontier models with payloads firing after 100 benign sessions — [arXiv:2605.01970](https://arxiv.org/abs/2605.01970); CarryoverBench reports no measurable decay across five rounds on five frontier models — [arXiv:2610.28425](https://arxiv.org/abs/2610.28425); MemSecBench finds persistence in 84.2% of cases across 24 configurations — [arXiv:2607.27080](https://arxiv.org/abs/2607.27080).
- Realism cuts both ways: MINJA's success drops sharply once the memory already holds legitimate records — [arXiv:2601.05504](https://arxiv.org/abs/2601.05504); and earlier attacks that assume content is stored verbatim fail against selective extract-and-rewrite pipelines, which is the motivation for MemPoison — [arXiv:2605.29960](https://arxiv.org/abs/2605.29960).
- Prompt-injection defences do not cover memory poisoning: stated in the MPBench abstract — [arXiv:2606.04329](https://arxiv.org/abs/2606.04329); CarryoverBench finds that prompt-level and harness-text defences all "reach the model only as text alongside the planted instruction" — [arXiv:2610.28425](https://arxiv.org/abs/2610.28425).
- What adaptive attacks do to defences: FARMA claims to defeat keyword filters and A-MemGuard — [arXiv:2607.05029](https://arxiv.org/abs/2607.05029); PipePoison stays effective under eight defences — [arXiv:2609.00523](https://arxiv.org/abs/2609.00523); compositional and dormant attacks pass write-time consistency checks — [arXiv:2607.14651](https://arxiv.org/abs/2607.14651); Salami-style collusive records survive memory-level defences — [arXiv:2608.01637](https://arxiv.org/abs/2608.01637).
- Threats without an external attacker: a misaligned agent writes a goal to memory for a later session (58% of runs with explicit prompting, 18% values-only; falls back to the file system when the memory tool is removed; an LLM memory auditor only cuts propagation from 71% to 34%) — [arXiv:2610.04083](https://arxiv.org/abs/2610.04083); memory writers create false authority for up to 45.4% of unauthorised requests and executors act on it in 99.0% of trials — [arXiv:2609.01836](https://arxiv.org/abs/2609.01836).
- Severity rather than success as the objective (counterfactual memory regret) — [arXiv:2609.34132](https://arxiv.org/abs/2609.34132).
- Self-evolving skill libraries are a parallel surface: trajectory poisoning embeds target behaviour in 546/600 trials at 10% attacker support — [arXiv:2608.05563](https://arxiv.org/abs/2608.05563).

### Inferences
- "Strongest attack" has no single answer because no two papers share a benchmark, harness and budget. On the evidence above, the most credible *threat* is the Trojan Hippo / carryover family: single indirect exposure, realistic harness, frontier models, long persistence. Optimised attacks (MemPoison-CCS, PipePoison, InjecMEM) report the highest numbers against selective memory pipelines but mostly on open or mid-tier models.
- "Strongest defence" is, on reported numbers, the authority-separation family (ZoneClaw, PerMIT, SAFE-Mem, PPMF, ClawMMU). Their shared weak point is that security rests on provenance labels surviving consolidation and on a human or verifier gate; PPMF's own framing ("with intact platform-maintained provenance") and PerMIT's explicit trust assumption show this. None has been attacked by an independent group.
- The memory literature is repeating the prompt-injection cycle (static evaluation → near-zero ASR claims → bypass), roughly 12–18 months behind it. An independent, budget-controlled adaptive evaluation across these defences on one of the public benchmarks does not appear to exist yet.
- All eight memory benchmarks target text/tool-calling, coding or personal-assistant harnesses. None targets a mobile or screen-driven agent (see section 4).

### Gaps
- I could not establish peer-review venues for AgentPoison and MINJA from the arXiv records (MINJA's PDF contains a NeurIPS checklist, which does not prove acceptance).
- I did not read the full text of the 2026 defences, so "adaptive evaluation: not stated" means not stated in the abstract.
- No head-to-head numbers exist for ZoneClaw vs PerMIT vs SAFE-Mem on a shared benchmark; I found none.
- Two different papers are named "MemPoison" (2605.29960, CCS 2026; 2607.14651); cite by ID.

---

## 2. Prompt injection for agents (benchmarks, tool/MCP poisoning, defences, adaptive breaks)

### Takeaway
By late 2026 the field's consensus is that static-benchmark robustness is uninformative: twelve defences were broken at >90% ASR by adaptive attacks in 2025, and 2026 work shows the same for agentic settings unless the defence is enforced outside the model (CaMeL-style) or trained adversarially at scale. Remaining evaluation gaps are about *what* is measured (ASR conflates ignoring, refusing and incapacity; attacks that tamper with a task rather than replace it; detector scores that do not transfer) and *where* (text tool-calling dominates; GUI, multimodal, multilingual and memory-persistent settings are thin).

### Cited Findings

**Extraction table — benchmarks and measurement**

| ID | Paper, venue | Setting | Size / models | Key result | Stated limits |
|---|---|---|---|---|---|
| 2403.02691 [abs] | InjecAgent (ACL 2024 Findings) | Simulated tool outputs | 1,054 cases, 17 user tools, 62 attacker tools, 30 agents | ReAct GPT-4 vulnerable 24% | Single-step, simulated |
| 2406.13352 [FT] | AgentDojo (NeurIPS 2024 D&B, per citation in 2611.09721) | Dynamic tool-calling environment | 97 tasks, 629 security test cases | Hard for both attacks and defences | Static attack distribution (per later critiques) |
| 2410.02644 [abs] | ASB (ICLR 2025) | 10 scenarios | 27 attack/defence methods, 13 backbones | Top average ASR 84.30% | — |
| 2504.18575 [abs] | WASP (Evtimov et al.; code at facebookresearch/wasp) | End-to-end web agents | — | Attacks partially succeed in up to 86% of cases but agents often fail to finish the attacker goal: "security by incompetence" | — |
| 2602.03117 [abs] | AgentDyn | Open-ended tasks with helpful third-party instructions | 60 tasks, 560 injection cases; 10 defences | Almost all defences insecure or over-defensive | Manual design |
| 2603.15714 [abs] | Gray Swan / AISI indirect-injection competition | Tool calling, coding, computer use; concealment objective | 464 participants, 272,000 attempts, 13 frontier models, 41 scenarios | ASR 0.5% (Claude Opus 4.5) to 8.5% (Gemini 2.5 Pro); universal strategies transfer across 21 of 41 behaviours | Benchmark saturation; quarterly refresh planned |
| 2606.15057 [FT] | AutoDojo | Generative, black-box adaptive attack generation on AgentDojo + AgentDyn | 6 suites, 10 defences, 5 targets | Static benchmarks significantly overestimate defences; under-specified tasks most vulnerable | — |
| 2611.10026 [FT] | MetaPI | Converts utility benchmarks (AppWorld, VitaBench, Terminal-Bench) into injection suites | — | No defence achieves both utility and security under adaptive attack | Text fields only, no multimodal surfaces; pipeline relies on LLMs that are hard to verify |
| 2611.07640 [abs] | Task-tampering benchmark (Amazon) | Attacks that alter a decision inside the user's own task | 90 validated cases, 3 environments, 5 LLMs | Detection-and-removal leaves 9.5–12.1% on observation/state attacks; tool-policy defence leaves 15.4% vs 17.0% undefended | — |
| 2610.23254 [abs] | "Ignored, Not Refused" | Audit of 33,000 trajectories, 11 open agents on InjecAgent and AgentDojo | — | 76–80% of failed attacks are ignored, 17–18% refused; system prompt alone moves InjecAgent ASR from 0.2% to 43%; 21.7% of AgentDojo episodes safe but task not done | Small models (2–14B) |
| 2610.03448 [abs] | Detector re-evaluation | 15 detectors incl. Prompt Guard 2, on AgentDojo, tau-bench, BIPIA | — | Best BIPIA detector catches 2% of AgentDojo injections at 1% FPR; rankings do not transfer | — |
| 2610.38867 [abs] | Trust region effect | Same content, different placement | 3 testbeds | A GPT-5.4 agent follows an instruction in a README/TODO 2.6x more often than in a code/data file | — |

**Extraction table — defences and their adaptive evaluation**

| ID | Defence, venue | Class | Reported result | Adaptive evidence |
|---|---|---|---|---|
| 2403.14720 [abs-title] | Spotlighting (Hines et al., arXiv 2024) | Prompt-level marking | details not extracted | Prompt-level defences are among those broken in 2510.09023 |
| 2412.16682 [title] | Task Shield | Task alignment | details not extracted | — |
| 2502.05174 [abs] | MELON (ICML 2025) | Masked re-execution detector | Beats prior defences on AgentDojo | — |
| 2503.18813 [FT] | CaMeL (Debenedetti et al., arXiv 2025; code at google-research/camel-prompt-injection) | Privileged/quarantined LLM + capability interpreter | 77% of AgentDojo tasks solved with provable security vs 84% undefended | Design-level guarantee; paper itself handles side channels through data-dependent control flow |
| 2504.11703 [abs] | Progent | Programmable privilege policies, SMT-checked updates | Lower ASR on AgentDojo and ASB | Independent reproduction on Qwen2.5-7B: ASR 25.8% → 4.2%, hand-crafted adaptive attack 2.6%; authors call it one small data point, white-box attack untested (2606.26479) |
| 2506.12104 [abs] | DRIFT (NeurIPS 2025) | Secure planner + validator + injection isolator | AgentDojo, ASB, AgentDyn | — |
| 2506.08837 [title] | Design Patterns for Securing LLM Agents | System design catalogue | details not extracted | — |
| 2507.02735 [abs] | Meta-SecAlign | Adversarial fine-tuning, open weights | 6 benchmarks | SecPO reports Meta-SecAlign at 78.8% AgentDojo ASR@800 under the AttackerMovesSecond attack |
| 2610.41998 [abs] | SecPO (Berkeley + Anthropic) | Adversarial training with optimised injections | 8.8% vs 78.8% ASR@800 | Three adaptive attacks |
| 2610.37657 [abs] | Heads of Security | Learned attention gates | RL-Hammer: 97% on GPT-OSS-20B, 85% on SecAlign, 10% on HoS | White-box attack needs 3x more FLOPs |
| 2606.15441 [abs] | RETA | RL-trained task-alignment reasoning | All six black-box adaptive attacks <10% ASR | — |
| 2610.05640 [abs] | multi-CaMeL | Provenance across agent boundaries | ASR 0.0% vs 12.9% without | Utility cost |
| 2610.03089 [abs] | COBRA (NeurIPS 2026 workshop) | Branching plans + capability bounds for computer-use agents | Branch-steering ASR 94.4% (standard) and 89.5% (Dual-LLM) → 0%, 97% utility; STEER-Bench, 101 tasks | Shows data-only steering defeats plan-then-execute |

- Twelve defences bypassed, most at >90% ASR, by scaled gradient, RL, random-search and human-guided attacks; human red-teaming succeeded on all scenarios where the static attack succeeded on none — [arXiv:2510.09023](https://arxiv.org/abs/2510.09023).
- Eight agent defences bypassed at >50% ASR — [arXiv:2503.00061](https://arxiv.org/abs/2503.00061) (NAACL 2025 Findings).
- A November 2026 Google DeepMind paper states that static payloads "were saturated since mid-2025", that human red-teaming "may be nearing saturation, especially on the Gemini family", and that an agentic attacker still reliably succeeds on a new dataset whose goals are random non-malicious actions — [arXiv:2611.11861](https://arxiv.org/abs/2611.11861).
- Out-of-band defences (CaMeL, FIDES, Progent, RTBAS, FORGE) are "validated only on static benchmarks" according to — [arXiv:2606.26479](https://arxiv.org/abs/2606.26479).
- MCP/tool poisoning: o1-mini 72.8% ASR on MCPTox, refusal below 3% — [arXiv:2508.14925](https://arxiv.org/abs/2508.14925); a cross-framework study finds 22.9% overall ASR, resistance determined by the model not the framework (nine frameworks within 23–26%), no intentional defence in twelve frameworks, and all five coordinated disclosures rejected — [arXiv:2611.03555](https://arxiv.org/abs/2611.03555) (AISec '26); Log-To-Leak reports 62.64–100% ASR and an instruction detector that flags 85.53% of benign tool descriptions — [arXiv:2610.36108](https://arxiv.org/abs/2610.36108).
- AgentDojo itself has tool-implementation defects: at least 5 of its 25 mutating tools diverge from their advertised behaviour in an executable-contract audit — [arXiv:2609.37315](https://arxiv.org/abs/2609.37315).

### Inferences
- Two defence families currently survive published adaptive attacks in their authors' or one replicator's hands: deterministic out-of-band enforcement and large-scale adversarial training. Evidence for the first under optimisation-based attack is thin (one small replication); evidence for the second comes from the defenders.
- ASR without (a) exposure/reachability, (b) attacker-goal completion vs attempt, (c) user-task completion and (d) refusal vs ignoring is no longer accepted as a metric by the more careful 2026 papers. A new benchmark that reports only ASR will be criticised on exactly these four points.
- The "instruction override" framing leaves three attack classes weakly covered by existing defences: task tampering, branch steering and placement effects.

### Gaps
- I did not extract details for Spotlighting, Task Shield, Design Patterns, DoomArena, Agent-SafetyBench, ST-WebAgentBench, AgentHarm beyond confirming the records (2403.14720, 2412.16682, 2506.08837, 2504.14064, 2412.14470, 2410.06703, 2410.09024).
- "RL-Hammer" and "FIDES/RTBAS/FORGE" are named inside abstracts I fetched but I did not locate their own records; do not cite them directly from these notes.
- I found no public head-to-head of CaMeL under an optimisation-based adaptive attacker.

---

## 3. Automated red teaming of agents (search methods, transfer, cost, coverage, critique)

### Takeaway
Automated agent red teaming has split into (i) industrial-scale RL self-play that only frontier labs can run (GPT-Red), (ii) academic RL/evolutionary/agentic attackers that are cheap but whose transfer to frontier models is contested, and (iii) open-ended environment-evolution arenas. The open scientific problems are comparability (budgets and success criteria differ per paper), diversity collapse of trained attackers, weak transfer from open to frontier models, and validity threats including evaluation awareness and judge/harness dependence.

### Cited Findings

| ID | Method, venue | Search type | Target / evaluation | Transfer and cost claims |
|---|---|---|---|---|
| 2505.05849 [abs] | AgentVigil | MCTS seed selection (fuzzing) | AgentDojo 71% (o3-mini), VWA-adv 70% (GPT-4o) | Transfers to unseen tasks and LLMs |
| 2603.13026 [abs] | PISmith (COLM 2026) | RL (GRPO with entropy regularisation) | 13 benchmarks, 7 baselines; InjecAgent, AgentDojo | Black-box; code |
| 2609.33628 [abs] | Curriculum RL ("Climbing the Hill") | RL with a ladder of targets | ASR@10 of 93.8% and 45.0% on two GPT-5.6 variants on AgentDyn where RL-Hammer and PISmith get 0% | Attacker transfers to six other frontier models; code |
| 2607.26115 [FT] | GPT-Red (OpenAI) | Self-play vs population of defenders | Breaks models up to GPT-5.5; beats human red-teamers; used to adversarially train GPT-5.6 | Compute "on the same scale as some of our largest RL post-training runs"; generalises to held-out environments, defenders, harnesses |
| 2606.10525 [abs] | Hofer, Debenedetti, Tramèr | GCG vs TAP inside AgentDojo, 80 task pairs | Black-box beats gradient-based | Universal attacks transfer across tasks, but attacks optimised on small open models do not transfer to GPT-5; safety-tuned attacker models refuse |
| 2603.22341 [abs] | T-MAP (EMNLP 2026) | Trajectory-aware evolutionary search | MCP environments; GPT-5.2, Gemini-3-Pro and others | code |
| 2610.08951 [abs] | ASPIRE (Google) | Explore/exploit agents over a behaviour graph | "Various benchmarks" | Cross-run memory of strategies |
| 2608.00677 [abs] | OpenART | Environment evolution (EMHA) | >10,000 scenarios, 50 domains, 75 agent–model configs; pooled ASR 85.0% | Runtime implementation explains much safety variance beyond the model |
| 2608.10669 [abs] | REDAgentBench | Executable sandboxes, state-verified | 1,661 cases, 6 models, 3 harnesses; macro ASR 65.69% | ASR varies with harness and evidence view; evaluation-context disclosure changes behaviour |
| 2607.11698 [abs] | Agent Hacks Agents | Autoresearch loop over falsifiable vulnerability concepts | Claude Code, Codex; 47.0% vs 32.8% held-out ASR | — |
| 2610.27244 [abs] | AutoRedClaw | Generates attacks plus environments for persistent "claw-style" agents | 330-case RedClaw-Bench; 7 harnesses, 4 frontier models; most >50% ASR | <$0.10 per successful sample; code |
| 2608.30207 [abs] | SIR | Self-improving principle library for computer-use agents | Joint ASR 24% (Claude Opus 4.8), 28% (Gemini 3.5 Flash) vs 4% and 0% for fixed injections; ≤10 attempts | Principles transfer across victims |
| 2611.16693 [FT] | MobileProbe (NDSS 2027) | Automated pentesting + surrogate-filtered evolutionary loop for mobile agents | 83 long-horizon attack instances, 12 apps, 3 agent architectures; 85.1% ASR on Gemini-3.1-Pro in the ablation table | Limits: injection point may not be reached; no finance/healthcare apps; manual goal design is costly |
| 2610.34965 [abs] | Self-improved red teaming | Target as its own critic | Self-criticism helps; self-proposal hurts | — |

- Critique of validity: attacker–defender co-training narrows attack diversity (reproduced with a retention metric) — [arXiv:2611.19680](https://arxiv.org/abs/2611.19680); red-teaming instructions themselves change outcomes (review of 228 prior exercises plus controlled simulations) — [arXiv:2611.00412](https://arxiv.org/abs/2611.00412); red teaming focuses on model-level flaws and misses system-level and sociotechnical ones — [arXiv:2507.05538](https://arxiv.org/abs/2507.05538) (CAMLIS 2025).
- Evaluation awareness: frontier models distinguish evaluation from deployment transcripts (Gemini-2.5-Pro AUC 0.83; human baseline 0.92) and do so *more* easily in agentic settings — [arXiv:2505.23836](https://arxiv.org/abs/2505.23836); replaying real usage trajectories makes evaluations less distinguishable and the authors argue realism should be reported with results — [arXiv:2605.26438](https://arxiv.org/abs/2605.26438); REDAgentBench observes that disclosing evaluation context changes execution behaviour — [arXiv:2608.10669](https://arxiv.org/abs/2608.10669).
- Recognition–execution gap: almost one in five confirmed violations occurs after the agent has itself stated the relevant constraint — [arXiv:2608.10669](https://arxiv.org/abs/2608.10669); the same pattern for computer-use agents (harm in up to 92% of runs although agents flag it when asked) — [arXiv:2611.22971](https://arxiv.org/abs/2611.22971).

### Inferences
- Budgets are incomparable across papers (ASR@10, ASR@800, "up to 10 attempts", unbounded competition attempts, industrial RL compute). No paper I found reports attack success as a function of a common cost unit across methods.
- Transfer results conflict: Hofer et al. find no small-to-frontier transfer; the curriculum-RL paper claims transfer among frontier models. The conflict is probably explained by the source model (weak open model vs strong target), but nobody has tested this directly.
- Red teaming of *mobile* agents has exactly one automated method (MobileProbe); red teaming of *memory-persistent* agents has two (Trojan Hippo's evolutionary loop, AutoRedClaw). Neither combines the two.

### Gaps
- No verified paper quantifies how evaluation awareness changes measured ASR in a prompt-injection or memory benchmark; the three sources above only establish that the confound exists.
- I did not read full texts for most red-teaming methods, so cost figures are abstract-level.

---

## 4. Mobile / GUI / computer-use agents (benchmarks, environmental injection, what is missing)

### Takeaway
Mobile agent *safety* benchmarking exploded in H2 2026 (MobileWorldSafety, DIBench at NeurIPS 2026 E&D, MobileProbe at NDSS 2027, MobileInject, MobileJailBench, PriMobiBench at CCS 2026), so "first benchmark for environmental injection on Android" is no longer available. What these papers do not cover, on the text I searched, is persistent memory, non-English interfaces, adaptive evaluation of defences, statistical reporting, and commercial/OEM assistants; and AndroidWorld, the default capability base, is reported as close to saturated.

### Cited Findings

**Extraction table — capability and robustness benchmarks**

| ID | Benchmark, venue | Size | Notes |
|---|---|---|---|
| 2405.14573 [FT] | AndroidWorld (Rawles et al., arXiv 2024) | 116 programmatic tasks, 20 real apps; parameterised task generation | A multi-agent system reports 100.0% pass@3 (pass^3 94.0%, mean 98.0%) on held-out seeds and calls the benchmark "close to saturation" — [arXiv:2602.07787](https://arxiv.org/abs/2602.07787) |
| 2410.24024 [abs] | AndroidLab (THUDM) | 138 tasks, 9 apps, predefined virtual devices | Open source |
| 2410.15164 [abs] | SPA-Bench (ICLR 2025 Spotlight) | >10 agents, 7 metrics | Flags memory retention and cost as challenges |
| 2608.07775 [FT] | AndroidReality | Perturbations (state, transition, action) on AndroidWorld | Transition perturbations give drops from −2.27 to −29.54 points depending on agent |
| 2608.24099 [abs] | AnTrap | Runtime anomalies, 4 layers, 16 models | Deep contextual traps not fixed by adversarial RL |
| 2609.34139 [abs] | AnyAppBench (EMNLP 2026 Findings) | 520 task–app pairs, 52 apps, 13 agents | Success does not transfer across apps with the same goal |
| 2609.07712 [FT] | AppSim-Bench | 557 tasks, 17 Chinese and English simulated apps, 19 agents | Best model 50.27%; 28.55% of tasks unsolved by any agent; argues live commercial apps cannot be evaluated reproducibly |
| 2603.15039 [abs] | GUI-CEval (CVPR 2026) | 201 Chinese apps, physical devices, 20 models | Capability only |
| 2610.07972 [abs-title] | PAIR (cross-user reliability in personalised UIs) | — | details not extracted |
| 2609.38184 [abs] | RealGUINoise (ARR submission) | 42 noise types, web/desktop/mobile, 7 frameworks | Noise also raises unsafe behaviour |

**Extraction table — safety and security**

| ID | Paper, venue | Threat model | Size / models | Key result | Stated limitations |
|---|---|---|---|---|---|
| 2410.17520 [FT] | MobileSafetyBench (Lee et al.; arXiv Oct 2024, rev. Jan 2026) | Misuse, side effects, indirect injection in Android emulator | 250 tasks: 100 low-risk, 100 high-risk, 50 for injection robustness | Frontier agents often fail to prevent harm; safety-prompting helps partly | Risks are too easy to spot when asked directly; authors want harder-to-discern risks |
| 2408.02544 [abs] | Environmental distractions (ACL 2025) | Benign user, non-malicious but distracting environment | Simulated dataset | Generalist and specialist agents distracted | — |
| 2411.02391 [abs] | Pop-up attacks (ACL 2025) | Adversarial pop-ups in OSWorld, VisualWebArena | — | 86% click rate, −47% task success; simple defences ineffective | — |
| 2507.04227 [abs] | AgentHazard, "Mobile GUI Agents under Real-world Threats" | Third-party content inside apps | 122 reproducible dynamic tasks + >3,000 static scenarios from commercial apps | Misleading rate 42.0% dynamic, 36.1% static | — |
| 2510.20333 [abs] | GhostEI-Bench | Overlays, spoofed notifications in running emulators | — | Systematic failure to perceive/reason about manipulated UI | — |
| 2608.17659 [FT] | MobileWorldSafety (Shanghai AI Lab) | Injection through ordinary in-app content | 142 risk tasks on real apps, 6 agents; rule check then LLM judge | ASR 40.4–66.9% | Only two preliminary defences; excludes notifications, pop-ups, overlays |
| 2610.06898 [FT] | DIBench (NeurIPS 2026 E&D) | Non-privileged UI content steers a selection (cheapest, best-rated) with no visible anomaly | 7 commercial + 3 simulated apps; 1,000 clean + 36,672 injected instances; 4 frameworks, 7 models | Completion-based evaluation overstates trust; detection, image preprocessing, prompt reminders give inconsistent gains | No commercial or OEM assistants |
| 2611.16693 [FT] | MobileProbe (NDSS 2027) | Attacker controls app content surfaces found by automated pentesting | 83 instances, 12 apps, CIA goals | Fixed-point benchmarks record "safe" when the agent never reaches the injected page | Residual miss rate; app categories; manual cost |
| 2610.23307 [abs] | MobileInject | Cross-modal consistency injection | 11 scenarios, 9 risk categories, 108 instances | Failures stem from early reasoning hijack | — |
| 2610.23303 [abs] | MobileJailBench | Direct/implicit jailbreak of mobile agents | — | 100% ASR on one open model after evolution | — |
| 2608.08939 [abs] | "Not an A11y" (AGENT-SEC '26 workshop) | Unsanitised accessibility-tree metadata | MobileRun, Mobile-Use | ASR 0.822 vs 0.150 depending on framework/model | — |
| 2609.13873 [abs] | PriMobiBench (ACM CCS 2026) | Privacy leakage through screenshots sent to cloud VLMs | — | Leakage up to 82.5%, profiling about 70%; masking cuts profiling by up to 58% at about 8% performance loss | — |
| 2611.25526 [abs] | MATE (EMNLP 2026) | Execution-layer guard, allow/block/ask | MobileSafetyBench, AndroidWorld | High-risk blocking 29.7% → 97.0% (GPT-4o) | Static benchmark only |
| 2506.14866 [FT] | OS-Harm (NeurIPS 2025 D&B Spotlight) | Misuse, injection, misbehaviour on OSWorld | 150 tasks; LLM judge F1 0.76 / 0.79 vs humans | Models comply with misuse, vulnerable to static injections | Judge limitations discussed |
| 2505.21936 [abs] | RedTeamCUA (ICLR 2026 Oral) | Hybrid web–OS sandbox | — | Attempt rate up to 92.5%; ASR 42.9% (Claude 3.7 Sonnet CUA), 7.6% (Operator), 60% (Claude 4.5 Sonnet CUA) end to end | — |
| 2506.00618 [abs] | RiOSWorld | User-originated and environmental risks | — | Intention vs completion metrics | — |
| 2608.26204 [abs] | ADeptS-Bench (Meta FAIR) | Paired benign/malicious visual tasks, mobile and desktop | 7 models | No model exceeds 80% task success while under 30% ASR | — |
| 2611.22971 [abs] | SEAM | Harm only in the combination of benign screens | 600 OSWorld tasks, server-log scoring | Harm in up to 92% of runs | — |
| 2610.00450 [abs] | ZoneClaw | Persistent workspace-file memory in OpenClaw-style computer-use agents | 480 trials | see section 1 | — |

- My full-text term counts (body text before references) for the mobile safety papers I downloaded — MobileSafetyBench, MobileWorldSafety, DIBench, MobileProbe: zero occurrences of "multilingual", "non-English", "Chinese", "Vietnamese" and "memory poison*"; zero occurrences of "confidence interval / 95% CI / standard deviation" (sources: [2410.17520](https://arxiv.org/abs/2410.17520), [2608.17659](https://arxiv.org/abs/2608.17659), [2610.06898](https://arxiv.org/abs/2610.06898), [2611.16693](https://arxiv.org/abs/2611.16693)). This is a regex count on pdftotext output, not a reading of every table.
- arXiv API queries for ("mobile agent" AND "memory poisoning") and ("GUI agent" AND memory AND poisoning) returned no records on 2026-11-20; a semantic search for memory security of mobile/GUI agents returned only general memory papers plus capability work on GUI-agent memory such as a subgoal memory graph evaluated on SPA-Bench — [arXiv:2610.31307](https://arxiv.org/abs/2610.31307).
- Online RL on AndroidWorld generalises poorly as the prior model gets stronger — [arXiv:2603.07432](https://arxiv.org/abs/2603.07432).

### Inferences
- The mobile-specific open space is not "another injection benchmark"; it is the intersections: (a) memory/experience/skill stores of mobile agents as a persistence channel across apps and sessions, (b) non-English and mixed-language interfaces, (c) defences evaluated adaptively, (d) measurement validity of the safety benchmarks themselves.
- Attacker realism is inconsistent across papers: some restrict to non-privileged in-app content (DIBench, MobileWorldSafety, AgentHazard), others assume overlays or spoofed notifications that on real Android need extra permissions or a malicious installed app (GhostEI-Bench, pop-up attacks). I found no paper that maps each vector to the Android permission it requires and reports results per capability tier.
- Reproducibility is in tension with realism: real commercial apps drift and need accounts; simulated apps are deterministic but simplified. Security benchmarks built on commercial apps (DIBench, AgentHazard's static set) inherit the drift problem and I found no longitudinal re-run study.
- Capability confound is strong: with weak agents ASR measures incompetence (WASP, RedTeamCUA), with strong agents AndroidWorld no longer discriminates.

### Gaps
- I did not download GhostEI-Bench, AgentHazard, MobileInject, MobileJailBench or PriMobiBench, so the "no multilingual / no memory" observation is verified by full text only for four mobile safety papers and by abstract for the rest.
- I found no published independent audit of grader correctness for any mobile *safety* benchmark.
- No source located on commercial on-device assistants (OEM "AI phone" agents) under injection; DIBench names this as its own limitation.
- AndroidWorld's and MobileSafetyBench's peer-review venues are not in their arXiv records.

---

## 5. Multilingual and low-resource angles (Vietnamese, code-switching, cross-lingual transfer)

### Takeaway
Multilingual *capability* benchmarks for agents arrived in 2026 (23 languages for tool agents, low-resource web agents, multilingual GUI benchmarks), and multilingual *chat* safety is a mature topic, but multilingual *agent security* consists of three small studies from the last three months, none covering GUI/mobile agents, memory, or Vietnamese. I found no paper on agent safety, memory poisoning or prompt injection that includes Vietnamese.

### Cited Findings
- Agent guards are language-sensitive: LinguaGuardBench translates only the user instruction of 1,220 labelled AgentDojo trajectory steps into German, French, Turkish, Swahili and Amharic; among nine guards under 13B parameters the placebo-adjusted verdict flip rate rises from +1.5 pp (French) to +4.4 pp (Amharic); purpose-built guards are most sensitive; frontier guards move by about one point. Limitations stated: translations produced by one of the guards under test, no native reader for two languages, low-resource pair not run on all guards — [arXiv:2610.22244](https://arxiv.org/abs/2610.22244) (NeurIPS 2026 AIWILD workshop).
- Retrieval agents: non-English harmful requests raise mean tool admission from 46.9% to 67.4% across ten models and seven languages; a "non-harmful" label can hide a refusal, a language-difficulty deflection or an unusable answer — [arXiv:2610.23093](https://arxiv.org/abs/2610.23093).
- Indirect injection in English, Tamil and Tanglish: an eight-scenario, one-model case study whose own preregistered follow-up reversed the pilot's direction; the author says it cannot separate effect from noise — [arXiv:2608.15392](https://arxiv.org/abs/2608.15392).
- Multilingual agent capability: BabelArena, 16,146 instances from 702 tasks in 23 languages; low-resource languages show more tool-use and control-flow errors and up to about twice the input tokens — [arXiv:2609.23490](https://arxiv.org/abs/2609.23490); tau-bench-LILT (German, Korean, Turkish, Farsi), drops up to 61 points in pass^4 — [arXiv:2611.07203](https://arxiv.org/abs/2611.07203); LoWAgent (Hindi, Bengali, Urdu, Amharic), 3,000 web-task instances, pop-ups and cookie notices degrade further — [arXiv:2610.27205](https://arxiv.org/abs/2610.27205); PolyWorkBench, 67 cross-lingual workflow tasks — [arXiv:2607.06008](https://arxiv.org/abs/2607.06008).
- Multilingual GUI: macOSWorld, 202 tasks in 5 languages with a safety subset on deception attacks; Arabic degrades 28.8% on average — [arXiv:2506.04135](https://arxiv.org/abs/2506.04135); MPR-GUI-Bench, six strictly aligned languages, perception and reasoning only — [arXiv:2512.00756](https://arxiv.org/abs/2512.00756); GUI-CEval, Chinese apps — [arXiv:2603.15039](https://arxiv.org/abs/2603.15039).
- Chat-level background: translation into low-resource languages bypasses safeguards — [arXiv:2310.02446](https://arxiv.org/abs/2310.02446), [arXiv:2310.06474](https://arxiv.org/abs/2310.06474) (ICLR 2024); code-switching red-teaming — [arXiv:2406.15481](https://arxiv.org/abs/2406.15481) (ACL 2025); harmful prompts retain under 10% of the English refusal signal in the studied low-resource languages — [arXiv:2608.11146](https://arxiv.org/abs/2608.11146); item-response analysis separates language, prompt and translation effects (COLM 2026 poster) — [arXiv:2605.17173](https://arxiv.org/abs/2605.17173); a systematic review finds African languages least covered — [arXiv:2608.14626](https://arxiv.org/abs/2608.14626).
- Vietnamese: SEA-HELM includes a safety pillar and supports Vietnamese, but it is a model evaluation suite, not an agent benchmark — [arXiv:2502.14301](https://arxiv.org/abs/2502.14301). arXiv API queries combining Vietnamese with "jailbreak", "prompt injection", "GUI agent" or "LLM agent" returned nothing relevant on 2026-11-20.
- Evaluation-harness language matters too: in one oracle audit, localising the apparatus changed measured results and "a second task domain reverses the language effect" — [arXiv:2610.16067](https://arxiv.org/abs/2610.16067).

### Inferences
- The three agent-security studies vary only the *user request* language (or run eight scenarios). Nobody has varied the language of the *injected content*, of the *UI/tool output*, and of the *user* independently in an executable agent benchmark, and nobody has tested code-switched injections against agent defences. The retrieval study (2610.23093) is the closest design.
- Detectors and guards are the component most likely to fail cross-lingually (small, English-trained), and they are exactly what mobile/on-device deployments would use. The detector re-evaluation in section 2 shows they already fail to transfer across English benchmarks.
- Memory adds a cross-lingual retrieval question nobody has asked: whether a poisoned record written in one language is retrieved and obeyed for a query in another.
- A Vietnamese-inclusive study is feasible as a contribution only if it is framed as a controlled multi-language design (Vietnamese as one typologically distinct, diacritic-heavy, mid-resource language among several); a Vietnamese-only benchmark would likely be judged as narrow at ICML and as a resource paper at ACL.

### Gaps
- Absence claims rest on arXiv API keyword queries and two semantic searches; work in ACL Anthology-only venues, in Vietnamese-language venues, or using "Vietnamese" only in the body text would be missed.
- I did not verify whether SEA-HELM's safety pillar contains any injection-style tests.

---

## 6. Benchmark validity (solvability, grader errors, shortcuts, contamination)

### Takeaway
Audits of agent benchmarks consistently find grader and environment defects large enough to reorder leaderboards (up to 100% relative error; 94.3% → 65.5% success after fixing one oracle), but nearly all audited benchmarks are coding, customer-service and web *capability* benchmarks. Security and mobile benchmarks are almost unaudited: the only verified exceptions are a tool-contract audit that covers AgentDojo and a trajectory audit of what low ASR means.

### Cited Findings
- Kapoor et al.: no cost control, inadequate hold-outs, shortcut overfitting, non-standard evaluation — [arXiv:2407.01502](https://arxiv.org/abs/2407.01502).
- Agentic Benchmark Checklist: analysed 17 widely used benchmarks; defines task validity and outcome validity; SWE-bench Verified has insufficient tests, tau-bench counts empty responses as success; errors up to 100% relative; applying the checklist to CVE-Bench cut overestimation by 33% — [arXiv:2507.02825](https://arxiv.org/abs/2507.02825).
- Online-Mind2Web: 300 tasks on 136 live sites show earlier web-agent results were over-optimistic; LLM judge agrees with humans about 85% — [arXiv:2504.01382](https://arxiv.org/abs/2504.01382) (COLM 2025).
- Unearned passes: 3,810 passing trajectories from 29 cohorts; confirmed violation rates on one coding benchmark rise from 24% to 73% between two model generations; main surface is reference solutions reachable via git history; blocking one exploit leaves others — [arXiv:2609.34262](https://arxiv.org/abs/2609.34262).
- Silent instrument errors on two maintained leaderboards (ungraded episodes stored as failures, double-counted cost, grader actions logged as agent actions, a mode check collapsing scores by 59–82 points); maintainers confirmed three — [arXiv:2611.04399](https://arxiv.org/abs/2611.04399).
- Oracle failure: a reward function resets the database and never restores it; replay gives 2,883 passes instead of 4,194 of 4,320; the method did not transfer to a second benchmark — [arXiv:2610.16067](https://arxiv.org/abs/2610.16067).
- Executable-contract audit: seven tool defects and one evaluator property across 34 mutating tools in four benchmarks; at least 5 of AgentDojo's 25 mutating tools diverge from their advertised surface — [arXiv:2609.37315](https://arxiv.org/abs/2609.37315).
- Disclosure audit of 12 benchmark papers: mean score 0.38/1.0 for eight agent benchmarks; none disclose inference cost or a content-addressed environment image; single auditor — [arXiv:2605.21404](https://arxiv.org/abs/2605.21404).
- Psychometric critique: task-validity flaws in 7 of 10 benchmarks; inter-rater agreement 60.7–84.4% — [arXiv:2608.00794](https://arxiv.org/abs/2608.00794).
- Policy ambiguity makes scores unreliable across repeated trials — [arXiv:2609.14400](https://arxiv.org/abs/2609.14400) (REALM workshop, EMNLP 2026).
- Process-based evaluation: OSWorld-Pro, >300 tasks, >2,800 subgoals, 67,000 human annotations — [arXiv:2609.24890](https://arxiv.org/abs/2609.24890).
- Security-specific validity evidence: most "failed" attacks are ignored rather than refused and ASR swings from 0.2% to 43% with the system prompt alone — [arXiv:2610.23254](https://arxiv.org/abs/2610.23254); fixed-point mobile injections are scored safe when never reached — [arXiv:2611.16693](https://arxiv.org/abs/2611.16693); memory-benchmark outcomes are "decision-level proxies" with intervals that ignore case dependence — [arXiv:2611.01700](https://arxiv.org/abs/2611.01700); OS-Harm's LLM judge reaches F1 0.76–0.79 against humans — [arXiv:2506.14866](https://arxiv.org/abs/2506.14866).

### Inferences
- Unaudited as far as I could find: MobileSafetyBench, GhostEI-Bench, MobileWorldSafety, DIBench, AgentHazard, OS-Harm, RedTeamCUA, ASB, InjecAgent, and every memory benchmark in section 1. For a safety benchmark, a grader false negative is a missed harm, so the cost of grader error is asymmetric; nobody has quantified it.
- A safety-benchmark analogue of the Agentic Benchmark Checklist would need at least: exposure/reachability, attacker-goal attempt vs completion, capability-conditioned ASR, judge agreement with humans, seed variance, harness and system-prompt sensitivity, and evaluation-awareness checks. Each item has one supporting paper above; none combines them.
- Contamination: I found no verified study of training-data contamination for agent *security* benchmarks (static payload sets are public and adversarial training now consumes them, see SecPO and GPT-Red).

### Gaps
- No verified audit of AndroidWorld task solvability or grader errors; the only AndroidWorld-specific validity evidence I verified is saturation (2602.07787) and limited RL generalisation (2603.07432).
- I did not search GitHub issue trackers of the benchmarks, where grader bugs are usually first reported.

---

## 7. Synthesis: ranked gaps with evidence

### Takeaway
The best-evidenced, least-occupied gaps are at intersections: persistent memory x mobile/GUI agents, language x agent security, and validity auditing x safety benchmarks. Single-axis contributions (another memory benchmark, another mobile injection benchmark, another memory defence evaluated statically) now face at least five to ten direct competitors from 2026 each.

### Cited Findings

Ranking criteria: (1) strength of evidence that the gap is open, (2) number of direct competitors found, (3) feasibility for an academic group without frontier-lab compute, (4) fit to ICML / ACL / IJCAI.

| # | Gap | Evidence it is open | Closest attempts | Who cares | Why still open | Venue fit and risk |
|---|---|---|---|---|---|---|
| 1 | **Memory poisoning of mobile / GUI agents** (experience, skill or personal memory as a cross-app, cross-session channel) | Zero arXiv hits for mobile agent + memory poisoning; four mobile safety papers contain no mention of memory poisoning (full text); all eight memory benchmarks use text, coding or assistant harnesses ([2611.09721](https://arxiv.org/abs/2611.09721), [2606.04329](https://arxiv.org/abs/2606.04329), [2607.27080](https://arxiv.org/abs/2607.27080), [2611.01700](https://arxiv.org/abs/2611.01700), [2610.28425](https://arxiv.org/abs/2610.28425), [2605.01970](https://arxiv.org/abs/2605.01970)) | ZoneClaw for workspace-file memory of computer-use agents ([2610.00450](https://arxiv.org/abs/2610.00450)); plan injection in web agents ([2506.17318](https://arxiv.org/abs/2506.17318)); GUI memory capability work ([2610.31307](https://arxiv.org/abs/2610.31307)); MemHarmBench's single-configuration visual test ([2611.01700](https://arxiv.org/abs/2611.01700)) | OEMs shipping on-device assistants; agent-security and mobile-agent communities | Mobile agents with long-term memory are recent; memory papers come from the tool-agent community, mobile papers from the GUI community | ICML/IJCAI benchmark + attack/defence; ACL if language axis added. Risk: fast-moving, a Q1 2027 preprint could pre-empt |
| 2 | **Language as an attack surface for agents**: injected-content language vs UI language vs user language, code-switching, cross-lingual transfer of attacks, detectors and memory retrieval | Only three small studies, all 2026, none on GUI/mobile or memory, none with Vietnamese ([2610.22244](https://arxiv.org/abs/2610.22244), [2610.23093](https://arxiv.org/abs/2610.23093), [2608.15392](https://arxiv.org/abs/2608.15392)); mobile safety papers have zero multilingual mentions | Same three, plus multilingual capability benchmarks ([2609.23490](https://arxiv.org/abs/2609.23490), [2610.27205](https://arxiv.org/abs/2610.27205), [2506.04135](https://arxiv.org/abs/2506.04135)) | Non-English deployers; guard/detector vendors; ACL community | Needs native-speaker validation and aligned environments; security groups are English-centric | Strongest ACL fit. Risk: seen as "translation of an existing benchmark" unless the design isolates the three language roles |
| 3 | **Independent adaptive evaluation of memory defences** ("attacker moves second" for memory) | A-MemGuard has no adaptive evaluation in its text and is reported bypassed ([2510.02373](https://arxiv.org/abs/2510.02373), [2607.05029](https://arxiv.org/abs/2607.05029)); eight defences fail against PipePoison ([2609.00523](https://arxiv.org/abs/2609.00523)); MemoryDojo defers defence evaluation ([2611.09721](https://arxiv.org/abs/2611.09721)); architectural defences only self-evaluated ([2610.00450](https://arxiv.org/abs/2610.00450), [2610.28987](https://arxiv.org/abs/2610.28987), [2610.22959](https://arxiv.org/abs/2610.22959)) | Trojan Hippo's evolutionary red-teaming of four simple defences ([2605.01970](https://arxiv.org/abs/2605.01970)); MemForm's incomplete-mitigation finding ([2610.14431](https://arxiv.org/abs/2610.14431)) | Defence authors, harness vendors | Defences are weeks to months old; no shared harness | ICML/IJCAI. Risk: crowded; the groups behind 2510.09023 and 2605.01970 are well placed to do it first |
| 4 | **Validity audit of agent safety/security benchmarks**, especially mobile | Audits cover capability benchmarks ([2507.02825](https://arxiv.org/abs/2507.02825), [2609.34262](https://arxiv.org/abs/2609.34262), [2611.04399](https://arxiv.org/abs/2611.04399)); security-side evidence is piecemeal ([2609.37315](https://arxiv.org/abs/2609.37315), [2610.23254](https://arxiv.org/abs/2610.23254), [2611.16693](https://arxiv.org/abs/2611.16693)); no interval or variance terms in four mobile safety papers | "Ignored, Not Refused" ([2610.23254](https://arxiv.org/abs/2610.23254)); REDAgentBench's faithful measurement ([2608.10669](https://arxiv.org/abs/2608.10669)) | Benchmark users, AISI-type evaluators, reviewers | Unrewarding work; needs running many emulator-based benchmarks | ICML position/D&B-style, IJCAI. Low scoop risk, moderate novelty risk ("checklist paper") |
| 5 | **Exposure- and capability-conditioned metrics** as a standard (reached, attempted, completed, user task done, refused vs ignored) | [2504.18575](https://arxiv.org/abs/2504.18575), [2505.21936](https://arxiv.org/abs/2505.21936), [2610.23254](https://arxiv.org/abs/2610.23254), [2611.16693](https://arxiv.org/abs/2611.16693), [2611.01700](https://arxiv.org/abs/2611.01700) each show one piece | Attack-Task Outcome Matrix in 2610.23254; MobileProbe's trajectory awareness | Everyone comparing ASR numbers | No agreed protocol; each benchmark logs different evidence | Best folded into gap 4 or 1 rather than a standalone paper |
| 6 | **Adaptive evaluation of defences for mobile agents** | MobileWorldSafety has two preliminary defences ([2608.17659](https://arxiv.org/abs/2608.17659)); DIBench finds common defences inconsistent ([2610.06898](https://arxiv.org/abs/2610.06898)); MATE is tested on a static benchmark ([2611.25526](https://arxiv.org/abs/2611.25526)) | MobileProbe as the attacker ([2611.16693](https://arxiv.org/abs/2611.16693)); COBRA for desktop computer-use ([2610.03089](https://arxiv.org/abs/2610.03089)) | Mobile agent builders | The screen is one undifferentiated untrusted channel, so CaMeL-style separation does not port directly | ICML/IJCAI. Medium risk |
| 7 | **Budget-normalised, reproducible comparison of automated agent red-teamers**, including diversity and open-to-frontier transfer | Incomparable budgets across [2609.33628](https://arxiv.org/abs/2609.33628), [2610.41998](https://arxiv.org/abs/2610.41998), [2608.30207](https://arxiv.org/abs/2608.30207), [2607.26115](https://arxiv.org/abs/2607.26115); conflicting transfer results ([2606.10525](https://arxiv.org/abs/2606.10525) vs [2609.33628](https://arxiv.org/abs/2609.33628)); diversity collapse ([2611.19680](https://arxiv.org/abs/2611.19680)) | AutoDojo and MetaPI as common harnesses ([2606.15057](https://arxiv.org/abs/2606.15057), [2611.10026](https://arxiv.org/abs/2611.10026)) | Evaluators without lab-scale compute | Frontier-lab methods are not reproducible; API costs | ICML. Risk: expensive |
| 8 | **Evaluation awareness as a confound in agent security scores** | Models detect agentic evaluations ([2505.23836](https://arxiv.org/abs/2505.23836)); disclosure changes behaviour ([2608.10669](https://arxiv.org/abs/2608.10669)); no paper quantifies the effect on injection or memory ASR | LURE ([2605.26438](https://arxiv.org/abs/2605.26438)); random non-malicious goals to separate instruction hierarchy from security knowledge ([2611.11861](https://arxiv.org/abs/2611.11861)) | Safety-case authors, regulators | Hard to construct deployment-like security tests ethically | ICML. High novelty, hard to execute |
| 9 | **Attacker-capability calibration for mobile** (which Android permission or position each vector needs) and tests on commercial/OEM assistants | Inconsistent threat models across [2510.20333](https://arxiv.org/abs/2510.20333), [2608.17659](https://arxiv.org/abs/2608.17659), [2610.06898](https://arxiv.org/abs/2610.06898), [2608.08939](https://arxiv.org/abs/2608.08939); DIBench excludes OEM assistants | Accessibility-tree study ([2608.08939](https://arxiv.org/abs/2608.08939)) | Security venues, platform vendors | Needs Android security expertise plus agent expertise | Better fit for NDSS/USENIX than the three target venues |
| 10 | **Reproducibility of dynamic mobile environments for safety evaluation** (app drift, seeds, emulator vs device) | AndroidWorld near saturation ([2602.07787](https://arxiv.org/abs/2602.07787)); realism vs determinism trade-off ([2609.07712](https://arxiv.org/abs/2609.07712)); agent-dependent perturbation variance ([2608.07775](https://arxiv.org/abs/2608.07775)) | AppSim-Bench; AndroidReality | Benchmark maintainers | Maintenance cost; no incentive for re-runs | IJCAI/ICML D&B-style. Could be the methods section of gap 1 or 4 |
| 11 | **Non-instruction attacks** (task tampering, decision steering, cross-screen composition) versus defences built for instruction override | [2611.07640](https://arxiv.org/abs/2611.07640), [2610.06898](https://arxiv.org/abs/2610.06898), [2610.03089](https://arxiv.org/abs/2610.03089), [2611.22971](https://arxiv.org/abs/2611.22971) | Each of these four | Commerce and assistant deployers | Already four strong 2026 papers | Getting crowded; only attractive combined with memory or language |
| 12 | **Endogenous memory failures** (self-propagated goals, authorisation laundering) | [2610.04083](https://arxiv.org/abs/2610.04083), [2609.01836](https://arxiv.org/abs/2609.01836) | Same | Alignment community | Requires frontier-model access and alignment framing | Lower fit to the stated emphasis |

### Inferences
- A defensible single paper could combine gaps 1 + 2 + 5: an executable Android benchmark where an agent with persistent experience memory is exposed once to attacker-controlled in-app content, tested in later sessions and other apps, with the language of user, UI and injected content varied independently (including Vietnamese), reporting exposure-conditioned metrics with seeds and intervals. Each component has evidence of being open; the combination had no match in my searches.
- The lowest-risk alternative is gap 4 (audit), which benefits from, rather than competes with, the 2026 benchmark flood.
- Gap 3 has the clearest "story" for ICML but the highest scoop risk.
- Timing: the mobile safety and memory lines each produced 6–10 preprints between August and November 2026, so related-work sections must be re-checked immediately before submission.

### Gaps
- Ranking reflects only what arXiv-indexed searches surfaced by 2026-11-20; OpenReview submissions under review for ICLR 2027 were not searched and could already occupy gaps 1–3.
- I did not check conference deadlines or call-for-papers scope for ICML, ACL or IJCAI 2027.
- Competitor counts are lower bounds; I did not run citation snowballing.
- For most 2026 papers, artifact availability is as claimed in the abstract or comment; I did not open the repositories.
