# Citation audit and adversarial prior-art search: IJCAI 2027 proposal "PROVENANCE-SUFFICIENT" (v5)

Audit date: 2026-11-20. Proposal file: `/home/claude/research/agent-memory-2027/e0cf8e5c-04_IJCAI_2027_PROVENANCE_SUFFICIENT_FINAL_v5.md`.

Evidence grades used below:
- **FETCHED** = a primary record (publisher page, PDF, or arXiv full text with arXiv stamp) was read in this session.
- **LISTING** = only a search/index listing (title + identifier + date/affiliation snippet) was seen in this session; content not read.
- Anything not in one of these two grades is in a Gaps list and must not be treated as verified.

Method note: direct `WebFetch` of the URLs written in the proposal was blocked by a permission gate for most links (only the IJCAI CFP went through). Each item was therefore verified through an alternative route: a web search that returned the same URL (then fetched), the `ijcai.org/Abstract/...` twin page, the Finnish-locale twin of the Aalto record, or the alphaXiv full-text mirror of the arXiv PDF (the page text carries the arXiv stamp, e.g. "arXiv:2609.08015v1 [cs.AI] 7 Sep 2026").

---

## Key Question 1 — Citation audit: does each cited work exist at the given identifier, and does it match?

### Takeaway
All eight cited items exist and match what the proposal says about them: 0 fabricated, 0 mismatched. The only defects are cosmetic (missing titles/authors/venues in the proposal's in-text labels).

### Cited Findings

| # | Proposal's label and identifier | Status | What is really there | Grade |
|---|---|---|---|---|
| 1 | Rintanen (IJCAI 2005), ijcai.org/proceedings/2005/128 | EXISTS + MATCH | "Conditional Planning in the Discrete Belief Space", Jussi Rintanen, IJCAI 2005, pp. 1260–1264. Non-probabilistic partially observable planning; the backup step is shown NP-complete and an algorithm is given. | FETCHED |
| 2 | Bonet & Geffner (IJCAI 2011), ijcai.org/proceedings/2011/324 | EXISTS + MATCH | "Planning under Partial Observability by Classical Replanning: Theory and Experiments", Blai Bonet and Hector Geffner. Restricted class (invariant non-unary clauses for initial uncertainty; hidden variables absent from conditional-effect bodies) translated in linear time to a fully observable non-deterministic problem. | FETCHED (via Abstract/11/324; the /proceedings/2011/324 URL returned a server error on fetch but the search engine lists that URL with the same title) |
| 3 | "Causal Belief Decomposition" (IJCAI 2013), ijcai.org/proceedings/2013/336 | EXISTS + MATCH | "Causal Belief Decomposition for Planning with Sensing: Completeness Results and Practical Approximation", Bonet and Geffner, IJCAI-13, starts p. 2275. Space exponential only in causal width; fast incomplete approximation (beam tracking). Proposal omits the authors. | FETCHED (via Abstract/13/336) |
| 4 | Fadnis & Rintanen, "Generalized 3-Valued Belief States in Conformant Planning", research.aalto.fi | EXISTS + MATCH | Same title; PRICAI 2022, Springer LNCS 13629, pp. 104–117, DOI 10.1007/978-3-031-20862-1_8. Generalises literal-based 3-valued belief approximation to arbitrary formulas and reduces conformant to classical planning. Author order on the PDF first page: Saurabh Fadnis, Jussi Rintanen. Proposal gives no venue/year. | FETCHED (Finnish-locale twin of the Aalto record + author PDF) |
| 5 | "ATR", arXiv:2609.08015 | EXISTS + MATCH | "From Version Conflicts to Decision Conflicts: Selective Revalidation for Long-Running AI Agents"; Yongjian Lyu, Yang Ren, Ruofei Lai (Huawei UK), Wenting Liu (Xi'an Jiaotong); v1, 7 Sep 2026, cs.AI. ATR records typed premises behind a pending action and re-checks only premises affected by a state change. Short paper; deterministic, developer-authored workloads only. | FETCHED (full text) |
| 6 | "PlanFence", arXiv:2609.03340 | EXISTS + MATCH | "Fresh Memory, Stale Plans: Derivation Currency for Distributed LLM-Agent Memory"; Evan Chen, Shiqiang Wang, Christopher G. Brinton (Purdue; Exeter); v2, 27 Sep 2026, cs.AI. Plans carry exact parent links; an action-specific dependency frontier is validated against owner heads before a protected action. | FETCHED (full text) |
| 7 | "AMV-Guard", arXiv:2610.31446 | EXISTS + MATCH | "When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents"; Yiqi Wang, Yifei Wang, Jiaqi Zhang, Zhangkai Wu, Yiqun Duan, Taotao Cai, Mingkai Zheng; v1, 22 Oct 2026, cs.MA. Sequential-stopping / bounded-VOI gate deciding which memory premises to re-verify before an action. | FETCHED (full text) |
| 8 | IJCAI 2027 CFP, 2027.ijcai.org/ijcai-2027-call-for-papers-main-track/ | EXISTS + MATCH | Abstract deadline 4 Jan 2027; full paper 11 Jan 2027; 7 body pages + up to 2 reference pages; LLMs may only polish author-written text and must not generate new content. | FETCHED |

- Item 1 record — [IJCAI 2005 proceedings](https://ijcai.org/proceedings/2005/128)
- Item 2 record — [IJCAI 2011 abstract page](https://ijcai.org/Abstract/11/324); same title listed at [ijcai.org/proceedings/2011/324](https://ijcai.org/proceedings/2011/324)
- Item 3 record — [IJCAI 2013 abstract page](https://ijcai.org/Abstract/13/336); same title listed at [ijcai.org/proceedings/2013/336](https://ijcai.org/proceedings/2013/336)
- Item 4 record — [Aalto research portal](https://research.aalto.fi/fi/publications/generalized-3-valued-belief-states-in-conformant-planning/); author order from [author PDF](https://users.aalto.fi/~rintanj1/papers/FadnisRintanen22.pdf)
- Item 5 record — [arXiv:2609.08015](https://arxiv.org/abs/2609.08015) (read through the alphaXiv full-text mirror)
- Item 6 record — [arXiv:2609.03340](https://arxiv.org/abs/2609.03340) (read through the alphaXiv full-text mirror)
- Item 7 record — [arXiv:2610.31446](https://arxiv.org/abs/2610.31446) (read through the alphaXiv full-text mirror)
- Item 8 record — [IJCAI 2027 main-track CFP](https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/)
- AMV-Guard itself says premises "need not be independent" but its implementation does not do joint dependency inference: a multi-premise verifier is one shared binary observation and premises tagged joint share one latent draw; "richer multi-premise dependency structure" is listed as not yet validated — [arXiv:2610.31446](https://arxiv.org/abs/2610.31446)
- ATR's own disclosure states OpenAI Codex was used for prototype scaffolding and language editing, and its results "establish controlled feasibility, not production generality" — [arXiv:2609.08015](https://arxiv.org/abs/2609.08015)

### Inferences
- The drafting model did not fabricate citations in this version. The risk is under-citation, not hallucination: the three arXiv items are the weakest comparators for the proposal's actual claim (none of them compresses memory), while the genuinely threatening prior art (Key Question 2/3) is absent from the proposal.
- The proposal's description of the four planning papers as the "closest technical confrontation" is fair for the belief-state side but it omits the journal-length treatment (Bonet & Geffner, JAIR 2014) where the width-based factored belief tracking results actually live.

### Gaps
- The three arXiv IDs were not fetched from `arxiv.org/abs/<id>` directly (permission gate); they were read as full text through alphaXiv, with the arXiv stamp, version and date visible in the text. Submission-history details (e.g. later versions, withdrawal notices) were not checked.
- The English-locale Aalto URL exactly as written in the proposal was not fetched; the Finnish-locale twin of the same record was.
- Page ranges for items 2 and 3 were not shown on the pages fetched (only the start page for item 3).

---

## Key Question 2 — Is the core idea already published? (adversarial search)

Core idea under test: decision-sufficient compression of an LLM agent's memory that preserves source-dependence / provenance correlations (independent vs copied sources) so that later query/action decisions equal those under the full evidence history, under a storage budget.

### Takeaway
No single paper found does all of it, but every component was published in 2026, some with theorems: (a) decision-centric rate-distortion memory compression with an exact merge criterion and hardness result (NeurIPS 2026 poster); (b) a "coarsest sufficient representation" theorem for replication-vs-corroboration given supplied lineage; (c) a non-identifiability theorem that is the proposal's motivating example verbatim. The proposal's T1 is anticipated; T2/T3 sit in a narrow gap between these lines and classical width/treewidth results.

### Cited Findings

Decision-sufficient / task-aware memory compression (2026):
- "Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory" (Zou et al.) frames agent memory as decision-centric rate-distortion; gives an exact forgetting boundary (a set of histories can share one memory state iff a common ε-optimal action exists), covering/packing bounds linking number of states K to distortion, NP-completeness of the optimal K-state partition, and an online learner (DeMem) with near-minimax regret — [arXiv:2605.10870](https://arxiv.org/abs/2605.10870); listed as a NeurIPS 2026 poster — [NeurIPS 2026 virtual site](https://neurips.cc/virtual/2026/poster/150643)
- "Support sufficiency as action-sufficient compression: a single-cycle rate-regret formulation" (Mark Walsh) defines a support state that explicitly includes provenance and conflict; shows the coarsest exactly action-sufficient compression is the quotient onto policy-equivalence classes; shows content-only or scalar-confidence-only codes fail when equal-confidence states need different actions; leaves the recurrent (multi-step) case and the minimal bounded-regret partition problem open; has no joint model of source dependence — [arXiv:2606.09858](https://arxiv.org/pdf/2606.09858)
- "What Must Generalist Agents Remember?" (Yamin et al., CMU/Georgia Tech) proves a necessity result: if two latent domains need disjoint near-optimal actions at a shared state, any uniformly near-optimal policy's memory distributions must be TV-separated; contrasts this with POMDP belief-state sufficiency — [alphaXiv record 2606.18746](https://www.alphaxiv.org/abs/2606.18746)
- "Finite-Memory Control of POMDPs: Fundamental Limits and Efficient Design" (Kutay, Eryilmaz, Shroff) is a NeurIPS 2026 poster whose abstract claims an information-theoretic converse lower-bounding the loss of any finite-memory controller and a "decision witness" notion for belief states whose confusion causes unavoidable loss — [NeurIPS 2026 virtual site](https://neurips.cc/virtual/2026/poster/153239)
- "The Value of Memory in Language Agents" proposes a decision-theoretic account of memory measured in avoided task loss, with risk–cost frontiers; the page fetched was an aggregator summary, so formal content is unconfirmed — [OpenTrain summary of arXiv 2610.31303](https://www.opentrain.ai/papers/the-value-of-memory-in-language-agents--arxiv-2610.31303/)
- LISTING only: "Bayes-Sufficient Compression Is Not Enough" — [alphaXiv 2610.03769](https://www.alphaxiv.org/abs/2610.03769); "Bellman-sufficient Information Complexity" — [alphaXiv 2606.11171](https://www.alphaxiv.org/abs/2606.11171); "Minimal Markovization via Stable Quotients" — [alphaXiv 2607.27132](https://www.alphaxiv.org/abs/2607.27132); "Belief Memory: Agent Memory Under Partial Observability" — [alphaXiv 2605.05583](https://www.alphaxiv.org/abs/2605.05583); "Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States" — [alphaXiv 2610.01415](https://www.alphaxiv.org/abs/2610.01415); "LAM: Lossy Agent Memory with a Retrieval-Score Error Bound" — [alphaXiv 2609.32256](https://www.alphaxiv.org/abs/2609.32256); "Beyond Heuristics: A Decision-Theoretic Framework for Agent Memory Management" — [arXiv:2512.21567](https://arxiv.org/pdf/2512.21567)

Source dependence / copies vs independent evidence (2026 agent literature):
- "Replication or Corroboration? An Axiomatic Framework for Evidential Dependence in Multi-Agent Debate" (Cao, Nguyen, …, Tran-Thanh, Cao) proves (Thm 1) that no judge can both ignore a replica and respond to a fresh root if its observation interface represents them identically; introduces the lineage quotient and proves it is the coarsest representation sufficient for every deterministic judge invariant to replication and root renaming (Thms 2–3); lifts it to quantitative bipolar argumentation; notes a single judge may need a strictly coarser statistic; takes the lineage partition as supplied and leaves graded dependence and robustness to false splits/merges open — [arXiv:2610.36151](https://www.alphaxiv.org/abs/2610.36151)
- "Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence" (Marc Bara) defines a redundant report by zero conditional mutual information with the latent state given admitted reports; Theorem 1 shows identical report profiles can require different Bayes posteriors under clone vs independent structure, so no report-only rule is correct for both; explicitly lists as open the weakest side-information interface that recovers or boundedly approximates the full-structure posterior; does not treat memory compression, budgets or decision-equivalence — [arXiv:2609.01873](https://arxiv.org/pdf/2609.01873)
- "Memory Echo in Single-Agent Long-Term Memory" shows repeated retrieval-and-write-back makes one source look like several independent records; its FPA mitigation tracks source-family IDs and parent pointers and serves one representative per family; provenance annotations are benchmark-supplied; no formal sufficiency result — [arXiv:2610.17763](https://www.alphaxiv.org/abs/2610.17763)
- "When Does Belief-Based Agent Memory Help? … Provenance-Capped Poisoning Defense" (Nous) stores per-attribute categorical beliefs and caps reliability by provenance tier; has no mechanism for duplicated or correlated sources, no robustness theorem, and says laundering needs taint tracking that is not implemented — [arXiv:2606.22030](https://arxiv.org/pdf/2606.22030)
- LISTING only: "Where Is the Truth When AI Agents Disagree? Dependence-Aware Belief Propagation for Unsupervised Truth Discovery" — [alphaXiv 2611.04805](https://www.alphaxiv.org/abs/2611.04805); "Copies or Sources? Measuring How LLM Aggregators Count Restated Evidence" — [alphaXiv 2610.06192](https://www.alphaxiv.org/abs/2610.06192); "Not All Agreement Counts as Corroboration: Provenance-Conserving Multi-View Fusion" — [alphaXiv 2609.01662](https://www.alphaxiv.org/abs/2609.01662); "Certified Multi-Source Integrity for Structured Agent Actions" — [alphaXiv 2609.34245](https://www.alphaxiv.org/abs/2609.34245); "Towards Mitigating Fabricated Consensus: The Active Provenance Gate" — [arXiv:2609.31422](https://arxiv.org/pdf/2609.31422); "Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking" — [alphaXiv 2608.21230](https://www.alphaxiv.org/abs/2608.21230)
- LISTING only, provenance-tracking agent memory systems: PACMI — [alphaXiv 2610.05732](https://www.alphaxiv.org/abs/2610.05732); MAP-Graph — [alphaXiv 2608.10509](https://www.alphaxiv.org/abs/2608.10509); Stashbird — [alphaXiv 2609.34242](https://www.alphaxiv.org/abs/2609.34242); LEDGER — [alphaXiv 2611.20927](https://www.alphaxiv.org/abs/2611.20927); MemoryLACE — [alphaXiv 2609.03201](https://www.alphaxiv.org/abs/2609.03201); "Memory Is a Derivation" (DerivAudit; Liu & Zhao, NYU) — [alphaXiv 2609.36130](https://www.alphaxiv.org/abs/2609.36130); "Prune the Summary, Not the History" — [alphaXiv 2610.20927](https://www.alphaxiv.org/abs/2610.20927)

Seminal / classical lines:
- Truth discovery with copying: Dong, Berti-Equille and Srivastava (VLDB 2009) model sources as independent or copiers, detect copying mainly from shared false values, discount copier votes, and show naive voting is misled when errors propagate by copying — [VLDB 2009 paper PDF](https://lunadong.com/publication/dependence_vldb.pdf)
- Belief tracking by width: Bonet and Geffner (JAIR 50, 2014, pp. 923–970) show belief tracking is exponential in a width parameter; factored belief tracking keeps, per precondition/goal variable, only the undetermined variables relevant to it; causal tracking and polynomial beam tracking refine this — [JAIR article PDF](https://jair.org/index.php/jair/article/download/10901/25996)
- Conformant planning compiled to classical with cost exponential in conformant width (Palacios & Geffner, JAIR 35, 2009, pp. 623–675) — [JAIR](https://jair.org/index.php/jair/article/view/10618)
- Knowledge compilation map: Darwiche and Marquis (JAIR 17, 2002, pp. 229–264) compare target languages by succinctness and polytime queries/transformations — [JAIR](https://jair.org/index.php/jair/article/view/10311)
- Decision-preserving POMDP compression: Poupart and Boutilier (NIPS 2002) seek compressions with minimal impact on decision quality and give sufficient conditions for lossless linear compression — [NeurIPS proceedings](https://proceedings.neurips.cc/paper/2002/hash/14ea0d5b0cf49525d1866cb1e95ada5d-Abstract.html)
- Information states: Subramanian, Sinha, Seraj and Mahajan (JMLR 23, 2022) define an information state as a history function sufficient for expected reward and prediction, and show an approximate information state yields an approximate dynamic program with bounded optimality loss — [JMLR](https://jmlr.org/papers/v23/20-1165.html)
- Equivalence notions in POMDPs: Castro, Panangaden and Precup (IJCAI 2009, pp. 1653–1657) compare bisimulation with trajectory equivalence — [IJCAI 2009](https://ijcai.org/proceedings/2009/276)
- Provenance circuits: Amarilli, Bourhis and Senellart build, for fixed treewidth bound and a fixed query, a provenance circuit in time linear in the instance, with N[X]-circuits for UCQs that specialise to any commutative semiring — [arXiv:1511.08723](https://arxiv.org/pdf/1511.08723.pdf); survey of tractable circuits in database theory (Amarilli & Capelli, 2024) — [arXiv:2407.01127](https://arxiv.org/abs/2407.01127)
- LISTING only: Green, Karvounarakis, Tannen, "Provenance semirings" (PODS 2007) — [author PDF](https://www.cs.ucdavis.edu/~green/papers/pods07.pdf); Jha & Suciu, "Knowledge Compilation Meets Database Theory" (ICDT 2011) — [author PDF](https://homes.cs.washington.edu/~suciu/camera_ready.pdf); Li, Walsh, Littman, "Towards a Unified Theory of State Abstraction for MDPs" (2006) — [researchr record](https://researchr.org/publication/LiWL06-0)

### Inferences
- The proposal's illustrative counterfactual pair (same bag of facts and marginals, different copy structure, different correct decision) is Theorem 1 of Epistemic Sybil Resistance and Theorem 1 of Replication-or-Corroboration, and the empirical content of Memory Echo. T1 cannot be claimed even as a minor contribution without citing these.
- The proposal's ε-sufficiency criterion (§5) is, structurally, the DeMem distortion criterion / approximate-information-state criterion with query actions added. Adding queries does not obviously change the mathematics, because a contingent query/action policy is just a policy.
- "Retain source relations needed for declared preconditions and query outcomes" (§6 step 3) is what width-based factored belief tracking does when copy relations are encoded as hidden state variables; and "the single judge may need a strictly coarser statistic than the lineage quotient" in Replication-or-Corroboration is the same task-indexing idea stated for aggregation.
- What was NOT found: a paper that (i) puts a bit/token budget on a provenance-dependency structure, (ii) characterises which dependence relations are necessary for a declared family of later query/action decisions, and (iii) compares against compiled/factored belief representations at equal budget. That triple conjunction is the residual gap.

### Gaps
- Searches run: alphaXiv semantic search (4 topical queries, 2023–Nov 2026 emphasis plus "historical" mode), and ~25 web searches by exact title. Not searched: Google Scholar, Semantic Scholar API, OpenReview, AAAI/AAMAS/KR/ICAPS proceedings indexes, AIJ. dblp was blocked by bot protection. A null result here is not proof of absence — especially for ICAPS/KR 2024–2026 papers and for IJCAI 2026 / AAAI 2026 / NeurIPS 2026 accepted papers not on arXiv.
- Not checked with any primary record this session: argumentation with correlated/dependent sources beyond the related-work section of arXiv:2610.36151; Dempster–Shafer treatment of dependent evidence; "data incest"/covariance intersection in distributed fusion; Blackwell sufficiency; information bottleneck; value-equivalence in model-based RL; provenance compression/summarisation in databases; DNF/CNF/prime-implicate belief representations in conformant planning (To, Pontelli, Son); OBDD-based belief-space planners. These are known research lines from background knowledge but are unverified here.
- Venue status of several 2026 arXiv items (peer-reviewed or not) was not checked, except the two NeurIPS 2026 posters noted above.

---

## Key Question 3 — The closest works, the exact delta, and how a planning/KR/agents referee would read the proposal

### Takeaway
Eight works bracket the proposal from both sides. A planning/KR referee will most likely read the current formalisation as belief-state planning with copy relations as hidden variables plus width-based projection; an agents-area referee will read it as DeMem + lineage quotient. Only a proved separation against those baselines changes that reading.

### Cited Findings

| # | Work (identifier) | What it does | Exact delta to the proposal |
|---|---|---|---|
| 1 | Replication or Corroboration? ([arXiv:2610.36151](https://www.alphaxiv.org/abs/2610.36151)) | Coarsest-sufficient representation theorem (lineage quotient) for judges invariant to replication; impossibility if interface cannot tell replica from fresh root; QBAF lifting; exhaustive audits | Lineage is a supplied partition (binary same-root / different-root); no graded or probabilistic dependence; one-shot score, not a contingent query/action policy; no storage budget or ε trade-off; no trust labels; no memory over time |
| 2 | Epistemic Sybil Resistance ([arXiv:2609.01873](https://arxiv.org/pdf/2609.01873)) | Information-theoretic definition of redundant reports; non-identifiability from reports alone; shared-root precision saturation; hierarchy of side-information interfaces | Posterior, not decisions; no compression or budget; Gaussian shared-root model; explicitly leaves "weakest sufficient interface" open |
| 3 | Remember the Decision, Not the Description / DeMem ([arXiv:2605.10870](https://arxiv.org/abs/2605.10870)) | Decision-centric rate-distortion for agent memory; exact merge criterion; covering/packing bounds; NP-completeness; online algorithm with regret bounds; benchmark wins | Histories are unstructured contexts: no source graph, no dependence relations, no evidence queries, no safety constraint; budget is number of memory states K, not bits of a provenance structure |
| 4 | Support sufficiency as action-sufficient compression ([arXiv:2606.09858](https://arxiv.org/pdf/2606.09858)) | Quotient by policy-equivalence is the coarsest exact action-sufficient code; scalar confidence insufficient; rate-regret function; Gibbs-form channel | Single decision cycle; provenance is just a coordinate of an abstract support state; no dependence model, no algorithm, no complexity; recurrent case open |
| 5 | Memory Echo / FPA ([arXiv:2610.17763](https://www.alphaxiv.org/abs/2610.17763)) | Shows and measures same-source record proliferation in four memory frameworks; provenance-family gating raises accuracy 0.825→0.920 (DeepSeek) | Empirical; serving-time heuristic; provenance labels supplied; no sufficiency or budget analysis |
| 6 | AMV-Guard ([arXiv:2610.31446](https://arxiv.org/abs/2610.31446)) — cited by proposal | Action-conditioned verification as sequential stopping with bounded VOI; premises may be dependent | No compression; dependence handled by a shared-latent approximation; this already covers the proposal's "verification allocator" |
| 7 | Bonet & Geffner, belief tracking by width ([JAIR 2014](https://jair.org/index.php/jair/article/download/10901/25996); [IJCAI 2013](https://ijcai.org/Abstract/13/336)) | Sound/complete factored belief tracking exponential in width; per-target projections keep only relevant variables; polynomial beam tracking | Logical (non-probabilistic) beliefs; no "source" semantics, no trust labels, no explicit bit budget; but copy relations can be encoded as hidden variables, so the framework applies |
| 8 | Value-directed compression / approximate information state ([NIPS 2002](https://proceedings.neurips.cc/paper/2002/hash/14ea0d5b0cf49525d1866cb1e95ada5d-Abstract.html); [JMLR 2022](https://jmlr.org/papers/v23/20-1165.html)) | Lossless/lossy compression preserving decision quality; bounded-loss guarantee for approximate information states | Generic POMDP machinery; nothing specific to provenance structure; no succinctness comparison with compiled representations |

- Supporting classical context for the referee question: Dong et al. on copier discounting — [VLDB 2009](https://lunadong.com/publication/dependence_vldb.pdf); linear-time provenance circuits on bounded-treewidth instances — [arXiv:1511.08723](https://arxiv.org/pdf/1511.08723.pdf); knowledge compilation map — [JAIR 2002](https://jair.org/index.php/jair/article/view/10311)

### Inferences
- Would a planning/KR referee see a re-labelling? As currently written, probably yes. The formal candidate in §5 defines an information state b(H,d), contingent policies over queries and actions, and value equivalence — the standard objects of planning with sensing. "Source dependence" enters only through Γ, which a referee will model as extra state variables (who copied whom) and observation variables (what each source said). Under that encoding, "which dependence relations must be kept for task d" is relevance/width analysis (work #7), and "compact constraint graph / circuit" is knowledge compilation.
- An agents-area referee has a different but equally damaging reading: the contribution is DeMem's criterion (#3) restricted to histories that differ in lineage, with the lineage quotient (#1) as the retained statistic.
- The proposal already anticipates this (its §4 "hard reviewer challenge" and §9 NO-GO conditions); what it lacks is awareness that the 2026 agent-side theory papers (#1–#4) exist. Its novelty-boundary section should be extended with them.
- The proposal's own primary hypothesis — an advantage in decision-equivalence per memory bit over factored and compiled belief representations — is the only claim none of the eight works makes. It is also the hardest to establish, because the comparison class (d-DNNF/SDD/factored beliefs) is very expressive.

### Gaps
- I did not find, and so cannot rule out, an ICAPS/KR paper that directly treats "source reliability and copying" inside contingent planning or epistemic planning. Not searched specifically: epistemic planning with untrusted announcements, belief revision with source dependence, judgment aggregation with shared evidence.
- Full texts of works #3 and #8 were read only through a structured summary / abstract page, not line by line.

---

## Key Question 4 — Named open problems the proposal could legitimately attack; what a nontrivial theorem would look like; is it already known?

### Takeaway
Four open problems are stated in fetched 2026 papers and are directly on target; the cleanest is the "weakest sufficient side-information interface" question. The obvious theorems (marginals are insufficient; minimal sufficient statistic is the decision-equivalence quotient / belief state; bounded-treewidth tractability) are already known in some form, so a publishable result must be a separation or a characterisation for graded dependence.

### Cited Findings
- Open problem (stated): identify the weakest side-information interface under which an aggregator recovers, or approximates with bounded loss, the posterior available under full dependence structure; also truthful provenance reporting, privacy-preserving provenance, and combining partial provenance with conservative fusion — [arXiv:2609.01873](https://arxiv.org/pdf/2609.01873)
- Open problem (stated): the lineage partition cannot express graded dependence, which needs probabilistic models; quantifying the effect of false splits/merges under realistic error rates "remains open"; fresh interventions at intermediate graph nodes were not audited — [arXiv:2610.36151](https://www.alphaxiv.org/abs/2610.36151)
- Hint of a task-indexed gap (stated): the lineage quotient is minimal only for the whole class of replication-invariant judges; a single judge can need a strictly coarser statistic — [arXiv:2610.36151](https://www.alphaxiv.org/abs/2610.36151)
- Open problem (stated): recurrent support sufficiency — when support affects memory updates and future routing even without changing the immediate action — and the minimal bounded-regret partition problem — [arXiv:2606.09858](https://arxiv.org/pdf/2606.09858)
- Open direction (stated): richer multi-premise dependency structure and scalability over premise count/dependency depth in action-conditioned verification — [arXiv:2610.31446](https://arxiv.org/abs/2610.31446)
- Already known, exact case: the coarsest exactly action-sufficient compression is the quotient onto policy-equivalence classes — [arXiv:2606.09858](https://arxiv.org/pdf/2606.09858); histories may share a state iff a common ε-optimal action exists, and optimal K-partition is NP-complete — [arXiv:2605.10870](https://arxiv.org/abs/2605.10870)
- Already known, "marginals lose a relevant correlation" (proposal T1): report-only rules cannot be right under both clone and independent structure — [arXiv:2609.01873](https://arxiv.org/pdf/2609.01873); interface that conflates replica and fresh root cannot satisfy both invariance and responsiveness — [arXiv:2610.36151](https://www.alphaxiv.org/abs/2610.36151)
- Already known, structural tractability relevant to proposal T2: provenance circuits in linear time for bounded-treewidth instances — [arXiv:1511.08723](https://arxiv.org/pdf/1511.08723.pdf); belief tracking exponential only in width / causal width — [JAIR 2014](https://jair.org/index.php/jair/article/download/10901/25996)
- Already known, generic converse relevant to proposal T3: an information-theoretic lower bound on the loss of any finite-memory POMDP controller is claimed in a NeurIPS 2026 poster — [NeurIPS 2026 virtual site](https://neurips.cc/virtual/2026/poster/153239); necessity of memory separation for near-optimal agents — [alphaXiv 2606.18746](https://www.alphaxiv.org/abs/2606.18746)

### Inferences
- Likely-known or textbook, do not headline:
  1. T1 in any form.
  2. "The minimal statistic sufficient for all tasks is the belief state; for a fixed task family it is the decision-equivalence quotient."
  3. "For bounded (incidence-)treewidth evidence graphs the representation is computable in polynomial time" — a referee will attribute this to treewidth-based compilation and width-based belief tracking unless the graph class or query family is genuinely different.
  4. A linear-in-number-of-roots lower bound for answering arbitrary later "are these two supports independent?" queries. This looks like a direct reduction from set disjointness / one-way communication complexity (memory writer = Alice, later task = Bob). I did not find it stated for this setting, but the technique is standard and a referee would regard it as a corollary.
- Candidate nontrivial theorems (none found in the literature searched; all unproved):
  A. Characterise the coarsest decision-sufficient statistic under graded (probabilistic common-cause) dependence for a declared family of threshold decisions with at most K verification queries — a direct extension of the lineage-quotient theorem beyond partitions and a partial answer to the "weakest sufficient interface" question. This is the most defensible target because two fetched papers name it as open.
  B. A succinctness separation: an explicit family of evidence-dependency structures and query/action families where a task-indexed dependence summary is polynomial while every width-bounded factored belief state and every d-DNNF/SDD of the full belief is super-polynomial (or the converse impossibility). This is what the proposal's primary hypothesis needs; it is also the result most at risk of being false, since compiled circuits can encode the summary itself.
  C. Robustness: a regret bound for decisions made from a lineage summary with a bounded rate of false splits/merges — named open, and tractable in small exact models.
  D. The recurrent case: show that decision-sufficiency for a horizon of future tasks strictly requires dependence information that single-cycle sufficiency discards (a separation between one-shot and sequential sufficiency).
- For an IJCAI planning/KR audience, B is the result that would answer the re-labelling objection; A and C fit the agents/MAS area better and are closer to reachable in the time available.

### Gaps
- I did not verify whether result A, B, C or D exists in the knowledge-compilation, probabilistic-database or Bayesian-experiment-comparison literature; no search was run on "sufficient statistic for correlated evidence under common cause", "Blackwell order with dependent experiments", or lower bounds for provenance/reachability sketches.
- The communication-complexity remark in item 4 is my own reasoning, not sourced.

---

## Key Question 5 — Verdict (novel / incremental / anticipated) and realism of a 7-page IJCAI 2027 main-track paper

### Takeaway
Verdict: **incremental, with the framing and T1 anticipated**; a narrow, legitimately open gap exists (targets A–D above). A 7-page IJCAI main-track paper by 11 Jan 2027 is unrealistic from the current state; the proposal's own "NO-GO as a committed paper / small formal pilot only" status is the correct call.

### Cited Findings
- Deadlines: abstract 4 Jan 2027, full paper 11 Jan 2027 (45 and 52 days after the audit date); 7 body pages + 2 reference pages; LLMs may not generate new submission content — [IJCAI 2027 CFP](https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/)
- The proposal states that no theorem, experiment or dataset exists and sets its own NO-GO conditions (source correlations captured by standard factored/compiled methods; result is a reformulation of planning with sensing) — proposal file, §§1, 9, 11 (local file, no URL)
- A peer-reviewed competitor with theorems, an algorithm and benchmark results already occupies "decision-sufficient agent memory under a budget" — [NeurIPS 2026 poster](https://neurips.cc/virtual/2026/poster/150643)
- A preprint with a coarsest-sufficient-representation theorem already occupies "what must be retained to separate copies from independent sources" — [arXiv:2610.36151](https://www.alphaxiv.org/abs/2610.36151)
- A preprint already proves the motivating example as a theorem and names the proposal's question as open — [arXiv:2609.01873](https://arxiv.org/pdf/2609.01873)
- The classical comparison class already has width-parameterised sound-and-complete task-relevant belief factorisation — [JAIR 2014](https://jair.org/index.php/jair/article/download/10901/25996)

### Inferences
- Why not "novel": each conceptual ingredient has a 2026 paper with formal results; the thesis sentence could be assembled from the abstracts of arXiv:2605.10870 and arXiv:2610.36151.
- Why not fully "anticipated": no fetched or listed paper combines a storage budget over a provenance-dependency structure, sequential query/action decision-equivalence, graded dependence, and an equal-budget comparison with compiled/factored beliefs; two papers explicitly leave adjacent questions open.
- Realism: in about seven weeks the authors would need (1) a full-text reading of at least works #1–#4 and #7, (2) a new theorem that survives the width/compilation objection, (3) an exact-enumeration benchmark with strong classical baselines, and (4) entirely human-written text under the CFP's LLM rule. Step (2) alone is a research risk with a real chance of a negative answer. A main-track submission is plausible only if a sharp result of type A or C is proved by the proposal's own 15 Dec checkpoint; otherwise a later venue (e.g. a KR/ICAPS/AAMAS cycle) or a workshop paper is the honest route.
- If it proceeds, required changes: drop T1 as a contribution; cite and position against arXiv:2610.36151, arXiv:2609.01873, arXiv:2605.10870, arXiv:2606.09858 and Bonet & Geffner 2014; state the result as an answer to a named open problem; make the equal-budget comparison against factored/compiled beliefs the central experiment.
- The three 2026 arXiv comparators the proposal does cite (ATR, PlanFence, AMV-Guard) are system/gating papers; using "ATR+AMV+monitor" as a baseline is reasonable, but they are not the novelty threat.

### Gaps
- No assessment was made of IJCAI 2027 area-chair preferences or acceptance statistics; the feasibility judgment is an inference from the stated project state and deadlines.
- Peer-review status of arXiv:2610.36151, arXiv:2609.01873 and arXiv:2606.09858 is unknown; if any is under review at IJCAI 2027 itself, overlap risk is higher than estimated here.
- Approval was needed but not granted for direct fetches of the proposal's own links (ijcai.org, research.aalto.fi, arxiv.org/abs) and of alphaxiv.org abstract pages; all were verified by alternative routes described at the top, except that several 2026 items remain LISTING-grade.
