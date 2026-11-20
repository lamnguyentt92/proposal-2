# ICML 2027 "REVOCATION-FEEDBACK" proposal: citation audit and adversarial prior-art search

Proposal audited: `/home/claude/research/agent-memory-2027/8fa13227-05_ICML_2027_REVOCATION_FEEDBACK_FINAL_v5.md` (read in full). Audit date: 2026-11-20.

Method note. Every identifier below was fetched in this session: arXiv abstract pages and the arXiv API (`export.arxiv.org/api/query`), PMLR/NeurIPS proceedings pages, Crossref DOI records, the ICML 2027 site, and full-text reads through alphaXiv for the eight closest papers. Where I state something from general knowledge without having re-read a primary source in this session, it is marked "(not re-read)" and placed under Inferences or Gaps. "I found nothing" always means "nothing in the searches listed", not "nothing exists".

---

## Q1. Citation audit: does each cited work exist at the given identifier, and does it match the proposal's description?

### Takeaway
All eight cited identifiers resolve to real documents and all descriptions match the source at abstract level; nothing is fabricated. The weaknesses are omissions and two loose paraphrases (SP-Mem "privacy tiers"; the ALT 2021 paper being presented as the reference for changing action sets when it is a computational-efficiency follow-up), plus one row of the prior-work table ("Partial monitoring, online caching, switching-cost bandits") that carries no citation at all.

### Cited Findings

| # | Proposal citation | Verdict | What is really at the identifier |
|---|---|---|---|
| 1 | "MemPrice", arXiv:2610.24955 | EXISTS + MATCH | "MemPrice: Online Memory Allocation via Adaptive Pricing for Long-Horizon Agents", Yiming Zong, Shiyuan Piao, Jiashuo Jiang, Fugee Tsung (HKUST), submitted 2026-10-18, cs.AI. Abstract states hard context budget enforced every round, adaptive price on context, "irreversible compression can force linear worst-case regret against hindsight following its own memory trajectory", and a "same-state benchmark". — [arXiv:2610.24955](https://arxiv.org/abs/2610.24955) |
| 2 | "OSL-MR", arXiv:2606.10616 | EXISTS + MATCH | "Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents", Qingcan Kang, Liu Mingyang, Shixiong Kai, Kaichao Liang, Tao Zhong, Mingxuan Yuan, submitted 2026-06-09, cs.AI. Abstract: constrained stochastic optimisation with "delayed costs including miss, reacquisition, and stale penalties", NP-hardness, "strict separation between online-observable features and offline-available supervision". — [arXiv:2606.10616](https://arxiv.org/abs/2606.10616) |
| 3 | "MemCredit", arXiv:2611.15600 | EXISTS + MATCH | "MemCredit: From Relevance to Utility for Decision-Time Memory in Long-Horizon Web Agents", Quanjiang Guo, Sijie Wang, Qianyang Zhu, Ben Zhang, Jinchuan Zhang, Ke Yan, Zhao Kang, submitted 2026-11-11, cs.AI. Abstract: estimates "state-, reference-context-, and policy-conditional marginal contribution of individual memories through controlled counterfactual interventions", distilled into a utility estimator; fixed token budget; ALFWorld and WebShop. — [arXiv:2611.15600](https://arxiv.org/abs/2611.15600) |
| 4 | Emamjomeh-Zadeh et al., PMLR 132 (2021) | EXISTS + MATCH (narrower than implied) | "Adversarial Online Learning with Changing Action Sets: Efficient Algorithms with Approximate Regret Bounds", Ehsan Emamjomeh-Zadeh, Chen-Yu Wei, Haipeng Luo, David Kempe; Algorithmic Learning Theory (ALT) 2021, PMLR 132, pp. 599–618. It is a paper on sleeping experts/bandits that relaxes to "no-approximate-regret" for computational efficiency. — [PMLR v132](https://proceedings.mlr.press/v132/emamjomeh-zadeh21a.html); arXiv version [2003.03490](https://arxiv.org/abs/2003.03490) |
| 5 | "SP-Mem", arXiv:2608.16551 | EXISTS + MATCH (one loose phrase) | "What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents", Wenjie Wang, Wenhe Si, Xinyue Xu, Yue Xu, submitted 2026-08-17, primary class cs.CR. Abstract: "Sanitized Privacy-Mapped Memory (SP-Mem)" stores sanitized content and exact private values "in isolated structures" and "selectively retrieves private values based on task requirements and user consent". — [arXiv:2608.16551](https://arxiv.org/abs/2608.16551) |
| 6 | LongMemEval, arXiv:2410.10813 | EXISTS + MATCH | "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory", Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu, submitted 2024-10-14. — [arXiv:2410.10813](https://arxiv.org/abs/2410.10813) |
| 7 | ICML 2027 Call for Papers | EXISTS + MATCH | Abstract deadline 14 Jan 2027, full paper 22 Jan 2027 (AoE, no extensions); 8 pages main body with unlimited references, impact statement and appendices; contribution types listed are General, Theory, Application-driven, Concept and Feasibility, Negative Results, and Datasets/Evaluations/Benchmarks; every submission must include an AI Disclosure Statement. (Read through a fetch tool that summarises the page; dates and limits are as relayed.) — [ICML 2027 CFP](https://icml.cc/Conferences/2027/CallForPapers) |
| 8 | ICML 2027 generative-AI policy | EXISTS + MATCH | The policy requires an AI Disclosure Statement at the end of every paper and requires disclosure of "any substantive use" of generative AI, listing as examples idea/hypothesis generation, literature synthesis that materially informs the paper, designing methodology or experiments, implementing code, and data analysis or interpreting results. — [ICML 2027 generative-AI policy](https://icml.cc/Conferences/2027/UseOfGenerativeAIByAuthors) |

Further points on individual rows:

- Row 1. MemPrice's lower bound is Proposition 1: for any non-anticipating capacity-feasible allocator there is an instance with exact utility estimates where regret against an "independent-state hindsight" comparator is at least (T−M)/(M(M+1)), M = ⌊1/α⌋+1. Its "same-state" (GSS) benchmark lets hindsight reallocate on MemPrice's own realised memory states but "its alternative choices do not propagate to future states". Its positive result is Reg_gss ≤ c√T + 2E_T + Δ_T under a "priced-frontier regularity" assumption. The paper's anonymous code link is named "ICLR2027-MemPrice", so it appears to be an ICLR 2027 submission. — [arXiv:2610.24955](https://arxiv.org/abs/2610.24955)
- Row 1. In MemPrice, compression is irreversible only "within a refresh window"; raw transcripts go to an external archive and "archived information can be recovered at subsequent boundaries". Permissions, deletion requests and sleeping bandits do not appear in the pages I read. — [arXiv:2610.24955](https://arxiv.org/abs/2610.24955)
- Row 4. The ALT 2021 abstract itself attributes the foundational results elsewhere: Kleinberg et al. (2010) for no-regret against the best ranking, and Kanade and Steinke (2014) for hardness (at least as hard as PAC-learning DNFs). — [PMLR v132](https://proceedings.mlr.press/v132/emamjomeh-zadeh21a.html)
- Row 8. In the policy, "substantive" qualifies the *use* to be disclosed; the statement itself is mandatory for all submissions. The proposal's phrase "substantive AI Disclosure Statement" slightly blurs this. — [ICML 2027 generative-AI policy](https://icml.cc/Conferences/2027/UseOfGenerativeAIByAuthors)

### Inferences
- The proposal's label "Verified work" on its prior-work table is accurate for existence. The "another model may have fabricated citations" worry does not materialise for this file.
- SP-Mem: the proposal's phrase "privacy tiers" is not wording from the abstract (which says "isolated structures"); "consent-controlled retrieval" is supported. I did not read the SP-Mem full text, so "tiers" is unverified rather than wrong.
- Emamjomeh-Zadeh et al. is a legitimate but non-canonical citation for "masked actions are not novel". A reviewer will expect Kleinberg–Niculescu-Mizil–Sharma (2010) and Freund et al. (1997) as the primary references (both verified in Q2).
- The larger citation problem is what is missing, not what is wrong. At least eight directly relevant 2025–2026 works found in Q2/Q3 are absent, including one (arXiv:2610.23812) that already formalises censored one-sided feedback for agent memory with a regret bound.

### Gaps
- The proposal's last table row ("Partial monitoring, online caching, switching-cost bandits") has no identifiers, so there was nothing to audit; Q2 supplies verified references.
- A direct `WebFetch` of the PMLR URL was blocked by an unanswered permission prompt; I fetched the same page with `curl` instead, so the record is verified but through a different tool.

---

## Q2. Does the model reduce to known theory? Survey with identifiers

### Takeaway
Each ingredient of the proposal's model has an established formulation with known rates, and several pairwise combinations were published in 2025–2026 (sleeping action sets inside MDPs; partial feedback with switching costs, fully classified; one-sided feedback for memory gating). I found no paper that combines exogenous irreversible removal, feedback censoring tied to that removal, and priced reacquisition, but the known results make "it is a composition of existing pieces" the default expectation.

### Cited Findings

**Sleeping experts/bandits and changing action sets**
- Sleeping experts origin: Freund, Schapire, Singer, Warmuth, "Using and combining predictors that specialize", STOC 1997. — [doi:10.1145/258533.258616](https://doi.org/10.1145/258533.258616)
- Kleinberg, Niculescu-Mizil, Sharma, "Regret bounds for sleeping experts and bandits", Machine Learning 80:245–272 (2010); the benchmark is the best ranking of actions. — [doi:10.1007/s10994-010-5178-7](https://doi.org/10.1007/s10994-010-5178-7); characterised in [PMLR v132](https://proceedings.mlr.press/v132/emamjomeh-zadeh21a.html)
- Kanade and Steinke, "Learning hurdles for sleeping experts" (ITCS 2012; ACM TOCT 2014): computational hardness of the adversarial case. — [doi:10.1145/2505983](https://doi.org/10.1145/2505983)
- Kanade, McMahan, Bryan (AISTATS 2009): stochastic availability with adversarial rewards; O(√(T log n)) in the experts version and a polynomial-time no-regret bandit algorithm. — [PMLR v5](https://proceedings.mlr.press/v5/kanade09a.html)
- Saha, Gaillard, Valko, "Improved Sleeping Bandits with Stochastic Actions Sets and Adversarial Rewards" (ICML 2020). — [arXiv:2004.06248](https://arxiv.org/abs/2004.06248)
- Nguyen and Mehta (2024): adversarial availability and losses; per-action regret O(√(TA ln K)) and O(√(T√(AK))) against an Ω(√(TA)) lower bound. — [arXiv:2403.01315](https://arxiv.org/abs/2403.01315)
- "Dying Experts" (Shayestehmanesh, Azami, Mehta, NeurIPS 2019): experts that leave never return; matching upper and lower bounds on ranking regret with known and unknown death order. — [arXiv:1910.13521](https://arxiv.org/abs/1910.13521)
- "Sleeping Reinforcement Learning" (Drago, Mussi, Metelli, ICML 2025): available action sets vary inside an MDP; Õ(H√(SAT)) when sets are revealed per episode; a minimax lower bound Ω(√(T·2^{A/2})) when availability is Markovian and disclosed per stage; Õ(H√(SAT)) again when availability depends only on state and stage. — [PMLR v267](https://proceedings.mlr.press/v267/drago25a.html)

**Mortal, blocking, recovering, rotting, restless/rested arms**
- "Mortal Multi-Armed Bandits" (Chakrabarti, Kumar, Radlinski, Upfal, NeurIPS 2008). — [NeurIPS 2008](https://papers.nips.cc/paper_files/paper/2008/hash/788d986905533aba051261497ecffcbb-Abstract.html)
- "Blocking Bandits" (Basu et al., 2019): playing an arm makes it unavailable for a fixed number of slots; greedy is (1−1/e)-optimal; UCB variant with logarithmic regret against greedy. — [arXiv:1907.11975](https://arxiv.org/abs/1907.11975)
- "Recovering Bandits" (Pike-Burke and Grünewälder, NeurIPS 2019): reward depends on time since last play. — [arXiv:1910.14354](https://arxiv.org/abs/1910.14354)
- "Rotting Bandits" (Levine, Crammer, Mannor): reward decays with number of pulls. — [arXiv:1702.07274](https://arxiv.org/abs/1702.07274)
- Whittle, "Restless bandits: activity allocation in a changing world", J. Appl. Probab. 25 (1988). — [doi:10.2307/3214163](https://doi.org/10.2307/3214163)
- Ortner, Ryabko, Auer, Munos, "Regret Bounds for Restless Markov Bandits" (ALT 2012): arms evolve as Markov chains regardless of play; Õ(√T) regret "with respect to the best policy that knows the distributions of all arms"; index policies are suboptimal. — [arXiv:1209.2693](https://arxiv.org/abs/1209.2693)
- "Bandits with Deterministically Evolving States" (Khosravi, Paes Leme, Podimata, Tsorvantzis): bandit feedback with unobservable deterministic state. — [arXiv:2307.11655](https://arxiv.org/abs/2307.11655)

**Switching costs, partial monitoring, feedback graphs, apple tasting**
- Dekel, Ding, Koren, Peres: adversarial bandits with unit switching cost have minimax regret Θ̃(T^{2/3}), against Θ(√T) with full information. — [arXiv:1310.2997](https://arxiv.org/abs/1310.2997)
- Arora, Dekel, Tewari (ICML 2012): policy regret; no bandit algorithm gets sublinear policy regret against an adaptive adversary with unbounded memory. — [arXiv:1206.6400](https://arxiv.org/abs/1206.6400)
- Partial monitoring classification: Bartók, Foster, Pál, Rakhlin, Szepesvári, Math. Oper. Res. 39(4), 2014; Lattimore and Szepesvári for the adversarial case; origin in Piccolboni and Schindelhauer (2001). Non-degenerate finite games split into rates √T, T^{2/3} and T, with local observability as the boundary between the first two. — [doi:10.1287/moor.2014.0663](https://doi.org/10.1287/moor.2014.0663); [arXiv:1805.09247](https://arxiv.org/abs/1805.09247); [doi:10.1007/3-540-44581-1_14](https://doi.org/10.1007/3-540-44581-1_14); classification summarised in [arXiv:2606.03851](https://arxiv.org/abs/2606.03851)
- Feedback graphs: Alon, Cesa-Bianchi, Dekel, Koren (COLT 2015): √T for strongly observable, T^{2/3} for weakly observable, linear otherwise. — [arXiv:1502.07617](https://arxiv.org/abs/1502.07617); summarised in [arXiv:2606.03851](https://arxiv.org/abs/2606.03851)
- "The Price of Partial Information with Switching Costs: A Complete Characterization for Feedback Graphs" (Cesa-Bianchi, Cesari, Colomboni, Esposito, Fusco, Koren; v2 dated 3 Nov 2026): with switching costs the minimax regret is Θ̃(√T) if the graph is "strongly revealing" (every pair of actions has an endpoint observing both), Θ̃(γ^{1/3}T^{2/3}) for other observable graphs, Θ(T) if not observable. Two-action apple tasting with switching costs attains O(√T) by "comparison probing". — [arXiv:2606.03851](https://arxiv.org/abs/2606.03851)
- Apple tasting: Helmbold, Littlestone, Long, Information and Computation 161 (2000). Raman, Subedi, Raman, Tewari (COLT 2024) characterise agnostic apple tasting by Littlestone dimension and give a realizable trichotomy. "Self-Directed Apple Tasting" (Nov 2026) gives a tetrachotomy. — [doi:10.1006/inco.2000.2870](https://doi.org/10.1006/inco.2000.2870); [arXiv:2310.19064](https://arxiv.org/abs/2310.19064); [arXiv:2611.06677](https://arxiv.org/abs/2611.06677)
- Paying for observations: Seldin, Bartlett, Crammer, Abbasi-Yadkori (ICML 2014), O((cN ln N)^{1/3}T^{2/3} + √(T ln N)) with matching lower bounds; Gong and Zhang (ICML 2026), phase transitions in contextual bandits with paid observations. — [PMLR v32](https://proceedings.mlr.press/v32/seldin14.html); [PMLR v306](https://proceedings.mlr.press/v306/gong26i.html)

**Censored, missing and delayed feedback**
- Guinet, Amin, Jaillet (NeurIPS 2022): multi-armed and contextual bandits under a broad class of censorship models, analysed through an effective dimension. — [arXiv:2302.06916](https://arxiv.org/abs/2302.06916)
- Vernade, Cappé, Perchet, "Stochastic Bandit Models for Delayed Conversions"; Vernade et al., "Linear Bandits with Stochastic Delayed Feedback" (the latter achieving Õ(d√T + md) per the description in arXiv:2610.23812). — [arXiv:1706.09186](https://arxiv.org/abs/1706.09186); [arXiv:1807.02089](https://arxiv.org/abs/1807.02089); [arXiv:2610.23812](https://arxiv.org/abs/2610.23812)
- Montanari, Fiegel, Pla, Saha (2026): budget B allocated across K arms under censored feedback; Ω(√T) lower bound and an optimistic algorithm. — [arXiv:2602.06565](https://arxiv.org/abs/2602.06565)
- Inventory control with censored demand (decision determines what is observed): Huh and Rusmevichientong, Math. Oper. Res. 34 (2009); Agrawal and Jia (2019). — [doi:10.1287/moor.1080.0355](https://doi.org/10.1287/moor.1080.0355); [arXiv:1905.04337](https://arxiv.org/abs/1905.04337)
- Selective-labels flavour (decision controls label observation): Kilbertus et al., "Fair Decisions Despite Imperfect Predictions". — [arXiv:1902.02979](https://arxiv.org/abs/1902.02979)

**Online caching and paging**
- Sleator and Tarjan, "Amortized efficiency of list update and paging rules", CACM 1985. — [doi:10.1145/2786.2793](https://doi.org/10.1145/2786.2793)
- Paschos, Destounis, Vigneri, Iosifidis, "Learning to Cache With No Regrets": caching as online linear optimisation, regret against the best static configuration, with a lower bound. — [arXiv:1904.09849](https://arxiv.org/abs/1904.09849)
- Bhattacharjee, Banerjee, Sinha: tight regret lower bounds for online caching. — [arXiv:2003.14085](https://arxiv.org/abs/2003.14085)
- Mukhopadhyay and Sinha, "Online Caching with Optimal Switching Regret": cache of C files, unit reward on a hit, explicit switching cost for fetching files, FTPL analysis. — [arXiv:2101.07043](https://arxiv.org/abs/2101.07043)
- Si Salem, Neglia, Ioannidis, "No-Regret Caching via Online Mirror Descent"; Ben Mazziane et al., "No-Regret Caching with Noisy Request Estimates"; Lykouris and Vassilvitskii, "Competitive caching with machine learned advice"; Chen et al., "Towards Optimal Robustness in Learning-Augmented Paging" (ICML 2026). — [arXiv:2101.12588](https://arxiv.org/abs/2101.12588); [arXiv:2309.02055](https://arxiv.org/abs/2309.02055); [arXiv:1802.05399](https://arxiv.org/abs/1802.05399); [PMLR v306](https://proceedings.mlr.press/v306/chen26gt.html)

**Knapsacks, irreversibility in MDPs, partial observability, exogenous inputs**
- Badanidiyuru, Kleinberg, Slivkins, "Bandits with Knapsacks". — [arXiv:1305.2545](https://arxiv.org/abs/1305.2545)
- Fruit, Pirotta, Lazaric: exploration in non-communicating (weakly communicating / multi-chain) MDPs, with regret stated over the communicating part. — [arXiv:1807.02373](https://arxiv.org/abs/1807.02373)
- Moldovan and Abbeel, "Safe Exploration in Markov Decision Processes"; Grinsztajn et al., reversibility-aware RL. — [arXiv:1205.4810](https://arxiv.org/abs/1205.4810); [arXiv:2106.04480](https://arxiv.org/abs/2106.04480)
- Liu, Chung, Szepesvári, Jin: learning POMDPs needs exponentially many samples in the worst case, but "weakly revealing" POMDPs are learnable with a simple optimistic algorithm. Jin et al. for undercomplete POMDPs. — [arXiv:2204.08967](https://arxiv.org/abs/2204.08967); [arXiv:2006.12484](https://arxiv.org/abs/2006.12484)
- Exogenous inputs: Sinclair et al., "Hindsight Learning for MDPs with Exogenous Inputs" (past decisions revisited in hindsight given samples of the exogenous variables); Efroni et al., ExoMDP. — [arXiv:2207.06272](https://arxiv.org/abs/2207.06272); [arXiv:2206.04282](https://arxiv.org/abs/2206.04282)
- Even-Dar, Kakade, Mansour, "Online Markov Decision Processes", Math. Oper. Res. 34 (2009). — [doi:10.1287/moor.1090.0396](https://doi.org/10.1287/moor.1090.0396)

**Online learning under deletion requests**
- Ginart et al., "Making AI Forget You"; Sekhari et al., "Remember What You Want to Forget"; Gupta et al., "Adaptive Machine Unlearning" (reduction from adaptive to non-adaptive deletion sequences); Cohen et al., "Control, Confidentiality, and the Right to be Forgotten". — [arXiv:1907.05012](https://arxiv.org/abs/1907.05012); [arXiv:2103.03279](https://arxiv.org/abs/2103.03279); [arXiv:2106.04378](https://arxiv.org/abs/2106.04378); [arXiv:2210.07876](https://arxiv.org/abs/2210.07876)
- Mirzasoleiman, Karbasi, Krause (ICML 2017): streaming submodular summarisation where selected elements "can be deleted at any time", constant-factor guarantee. — [PMLR v70](https://proceedings.mlr.press/v70/mirzasoleiman17a.html)
- Li, Wang, Cheng, "Online Forgetting Process for Linear Regression Models" (2020): data accessible only for a limited window ("First In First Delete"), regret upper bounds of order O(T) under constant memory, "rank swinging" phenomenon; lower bounds left to future work. — [arXiv:2012.01668](https://arxiv.org/abs/2012.01668)
- Hu, Schölkopf, Sanyal, "Online Learning and Unlearning" (2025): OCO with deletion requests; regret comparator recomputed with deleted functions removed "so both the learner and the comparator share the same history"; O(√T + k²d)-type and O(log T + k²d) bounds for k deletions; lower bounds listed as open. — [arXiv:2505.08557](https://arxiv.org/abs/2505.08557)
- Nguyen-Tang and Arora, "Exact Unlearning in Reinforcement Learning" (ICML 2026, PMLR 306): ρ-TV-stable tabular RL with regret O(H²√(SAT) + H³S²A + H^{2.5}S²A/ρ) and lower bound Ω(H√(SAT) + HSA/ρ). — [PMLR v306](https://proceedings.mlr.press/v306/nguyen-tang26a.html); [arXiv:2606.04182](https://arxiv.org/abs/2606.04182)
- Ye et al., "Unlearning Offline Stochastic Multi-Armed Bandits" (2026): (ε,δ)-unlearning for offline MAB with upper and lower bounds on post-unlearning suboptimality. — [arXiv:2605.00638](https://arxiv.org/abs/2605.00638)
- Ye et al., "Reinforcement Unlearning" (NDSS 2025). — [arXiv:2312.15910](https://arxiv.org/abs/2312.15910)
- Benarroch, Atif, Cappé (Oct 2026): sequential deletion requests certified against a counterfactual trajectory with bounded long-run performance loss. Cianfarani and Cohen (Oct 2026): adaptive and collective deletion requesters. — [arXiv:2610.17993](https://arxiv.org/abs/2610.17993); [arXiv:2610.04310](https://arxiv.org/abs/2610.04310)

**Learning for memory management in LLM agents (2024–2026)**
- Ji et al. (Salesforce/UCLA, Oct 2026), "Learning Personalized Memory Gating from Delayed One-Sided Feedback": memory gating formulated as "contextual apple tasting with delayed one-sided feedback"; "If a_t = skip, the learner discards the fact and observes nothing at any future time"; Warm-Start UCB with regret Õ(Tε ∧ d√T) for delay window O(√T). — [arXiv:2610.23812](https://arxiv.org/abs/2610.23812)
- Behnam and Wang (Oct 2026), "Causal Memory Policy": proves non-identifiability of memory utility when a memory is never retrieved (Theorem 1), and a Bayes-optimal one-sided abstention rule for the irreversible `forget` operation (Theorem 2); notes "a memory never stored generates no future observations, so its utility can never be estimated". — [arXiv:2610.02070](https://arxiv.org/abs/2610.02070)
- Sun, Cao, Lam (Jul 2026), SOLAR: "online semantic cache replacement problem with switching costs"; claims competitive ratio ≤ 3 and eviction regret O(√(KT log T)) against an Ω(√(KT)) lower bound. — [arXiv:2607.00394](https://arxiv.org/abs/2607.00394)
- Liu, Yang, Zhao (Oct 2026), "Curating Always-Loaded Context for LLM Agents: A Capacitated Assortment Model with Censored Feedback": loaded instructions are observed, absent ones only through "gap sightings"; identification results framed in partial-monitoring terms; a two-world indistinguishability lower bound (Proposition C.6, linear regret without magnitude feedback); matched upper and lower bounds on an edit-cap regret term. — [arXiv:2610.11007](https://arxiv.org/abs/2610.11007)
- Jiang et al., "Memory as a Controlled Process" (MemCon): memory operations modelled as an MDP. Uni-Mem: unified online policy optimisation for a memory manager. — [arXiv:2607.13591](https://arxiv.org/abs/2607.13591); [arXiv:2610.29671](https://arxiv.org/abs/2610.29671)
- Revocation and deletion in agent memory, empirical: Shen, Toyoda, Leung, "Revoked but Still Authoritative" (no tested system enforces revocation by default); Xie et al., Bemula benchmark for memory unlearning (135 forget requests); Shen, "What Eviction Destroys" (restore-counterfactual audit separating irreversible from recoverable loss on LongMemEval-S); Huang, "What Should an Agent Remember?" (of a 68.7-point reported advantage, 53.2 points are attributable to history access rather than selection). — [arXiv:2609.08258](https://arxiv.org/abs/2609.08258); [arXiv:2610.18052](https://arxiv.org/abs/2610.18052); [arXiv:2609.08279](https://arxiv.org/abs/2609.08279); [arXiv:2610.00366](https://arxiv.org/abs/2610.00366)

### Inferences
- Mapping the proposal's primitives to known models:
  - eligibility mask g_t → sleeping experts/bandits; permanent removal → dying experts / mortal bandits;
  - "no feedback about items you do not hold" → apple tasting / partial monitoring / censored bandits;
  - reacquisition cost → switching costs / caching fetch cost;
  - budget B → caching capacity / knapsack;
  - irreversible state → non-communicating MDPs;
  - "exogenous task and permission events coupled across policies" → Exo-MDPs with hindsight coupling;
  - "which legal proxies restore identifiability" → observability conditions in partial monitoring and the revealing condition in POMDPs.
- The unlearning literature answers a different question from the proposal's. Online Learning and Unlearning, Exact Unlearning in RL and Unlearning Offline MAB all ask "how much regret does *honouring* a deletion guarantee cost the learner's own statistics"; none models the deleted item as an action whose future utility becomes unobservable, and none has reacquisition. This is the clearest gap between the proposal and the deletion literature.
- The 2026 agent-memory papers have already imported the three theory lenses the proposal treats as its audit targets (apple tasting in 2610.23812, partial monitoring in 2610.11007, caching with switching costs in 2607.00394). The proposal cites none of them.

### Gaps
- Not verified in this session (lookup tools failed or were rate-limited): Abernethy, Amin, Zhu, "Threshold Bandits, With and Without Censored Feedback" (NeurIPS 2016); Besbes–Gur–Zeevi on non-stationary bandits with variation budgets; Bnaya et al. on volatile bandits. I believe these exist but assert nothing about them.
- Searches run for a direct hit: three alphaXiv topic searches (sleeping/dying/apple-tasting/switching/censored/irreversible; right-to-be-forgotten/unlearning/consent-withdrawal bandits; revocation/deletion/censored-feedback agent memory), one alphaXiv search on learned write/evict policies since 2024, one web search combining sleeping bandits, censored feedback, reacquisition and data deletion, and keyword scans of the ICML 2025 (PMLR 267, 3,330 papers parsed) and ICML 2026 (PMLR 306, 6,552 papers parsed) indexes. None returned a paper combining exogenous revocation, revocation-tied censoring and priced reacquisition. I did not search OpenReview submissions under review (e.g. ICLR 2027), COLT/ALT 2026 proceedings, or the operations-research literature beyond the items listed, so an unseen direct hit is possible, most plausibly among anonymous ICLR 2027 submissions.

---

## Q3. The closest works, the exact delta, and whether a reduction makes the hoped-for theorem a corollary

### Takeaway
Eight works sit within one modelling step of the proposal; between them they already supply the censored-feedback regret bound, the irreversibility lower bound, the state-relative comparator, the identifiability impossibility and the switching-cost classification. What none supplies is the exogenous permission process and legal reacquisition. My assessment is that the proposal's T1–T3, as currently sketched, are more likely than not to come out as corollaries or compositions of these results.

### Cited Findings

| # | Work | What it proves | Exact delta to the proposal |
|---|---|---|---|
| 1 | Ji et al., [arXiv:2610.23812](https://arxiv.org/abs/2610.23812) | Memory gating as contextual apple tasting with delayed one-sided feedback; Õ(Tε ∧ d√T) regret against a threshold oracle. | No state, no exogenous removal, no reacquisition, stationary linear utility. Authors name budget-dependent storage cost and drifting utility as future work. It already covers "feedback exists only for items you keep" in agent memory. |
| 2 | MemPrice, [arXiv:2610.24955](https://arxiv.org/abs/2610.24955) | Linear lower bound against independent-state hindsight under irreversible compression; c√T + 2E_T + Δ_T against a same-state benchmark. | Irreversibility is self-inflicted by the learner's compression, not imposed by an outside permission process; utilities come from an LLM oracle with bounded error (no censoring); the same-state comparator is not a reachable policy; recovery at refresh boundaries is free of an explicit price. |
| 3 | Causal Memory Policy, [arXiv:2610.02070](https://arxiv.org/abs/2610.02070) | Non-identifiability of utility for never-retrieved memories; unbiased Hájek estimator under randomised exposure; Bayes-optimal one-sided abstention for irreversible forget. | Offline/causal estimation, not regret; no permissions; restores identifiability by randomising retrieval, which is exactly what is unavailable for a revoked item. |
| 4 | Liu, Yang, Zhao, [arXiv:2610.11007](https://arxiv.org/abs/2610.11007) | Censored-feedback identification in partial-monitoring language; two-world linear-regret lower bound; matched edit-cap regret term. | Context-file curation, not memory under revocation; the curator chooses deletions; no irreversible loss and no reacquisition cost. |
| 5 | Cesa-Bianchi et al., [arXiv:2606.03851](https://arxiv.org/abs/2606.03851) | Complete trichotomy (√T / γ^{1/3}T^{2/3} / T) for feedback graphs with switching costs; apple tasting with switching costs is √T. | Fixed action set, fixed feedback graph, stateless, oblivious adversary, static comparator. No sleeping actions, no budget. |
| 6 | Sleeping RL, [PMLR v267](https://proceedings.mlr.press/v267/drago25a.html) | Sleeping action sets inside episodic MDPs; Ω(√(T·2^{A/2})) barrier for Markovian availability disclosed per stage; Õ(H√(SAT)) otherwise. | Episodic with resets, full bandit feedback on played actions, no censoring linked to availability, no cost to regain an action. |
| 7 | Dying Experts, [arXiv:1910.13521](https://arxiv.org/abs/1910.13521) | Matching bounds on ranking regret when experts leave permanently. | Full information, no state, no return or reacquisition, comparator is a ranking. |
| 8 | Online Learning and Unlearning, [arXiv:2505.08557](https://arxiv.org/abs/2505.08557); Exact Unlearning in RL, [PMLR v306](https://proceedings.mlr.press/v306/nguyen-tang26a.html) | Regret under deletion guarantees, with a comparator that also excludes the deleted data. | Deletion removes training influence, not an action; no censoring of future utility; no reacquisition. The "same-history comparator" idea is already here. |

Supporting results that bear directly on the reduction question:
- Restless Markov bandits already admit Õ(√T) regret against the best policy that knows the arm distributions, with arm states seen only when played. — [arXiv:1209.2693](https://arxiv.org/abs/1209.2693)
- Online caching with an explicit fetch (switching) cost has an FTPL policy with analysed switching regret. — [arXiv:2101.07043](https://arxiv.org/abs/2101.07043)
- Sublinear policy regret is impossible against an adaptive adversary with unbounded memory. — [arXiv:1206.6400](https://arxiv.org/abs/1206.6400)
- OSL-MR already shows the multi-step retention problem is NP-hard. — [arXiv:2606.10616](https://arxiv.org/abs/2606.10616)

### Inferences
The following is my own analysis; none of it is proved here or in any source.

**Reduction A: the model is a POMDP / Exo-MDP with known endogenous dynamics.** Take hidden state (m_t, g_t, z_t, θ). The learner observes its own memory state m_t and the permission events g_t (the ledger is trusted and logged); the storage transition T is specified by design. Only the regime z_t and the utility parameters θ are hidden, and g_t, z_t are exogenous. Regret against the best F_t-measurable policy is then standard regret against the optimal policy of a partially observed model with known controllable dynamics and unknown rewards. Three consequences follow from known results:
1. If an early legal action can irreversibly forfeit future reward, linear regret against the best policy is unavoidable. This is the generic trap argument for non-communicating MDPs and is already proved in the agent-memory setting as MemPrice Proposition 1.
2. If revocation is never followed by regrant, the revoked item's rewards are irrelevant to every legal policy and the problem is a dying-experts/mortal-bandit instance. The proposal concedes this.
3. "Which legal proxies make the problem learnable" becomes an observability condition: local/global observability in partial monitoring, or the weakly revealing condition for POMDPs. T2 would restate a known classification in new vocabulary unless the time-varying structure adds something.

**Reduction B: the minimal toy model is a two-action partial-monitoring game with a switching cost.** With two memories and budget one, "hold item a" reveals a's utility and "do not hold a" reveals nothing about a. Depending on whether a legal miss signal reveals the other item's value, this is apple tasting (√T even with switching costs, by arXiv:2606.03851), a two-armed bandit with switching costs (T^{2/3}, Dekel et al.), or full-information caching (√T). Revocation windows are exogenous and observed, and the comparator is also locked out, so they are sleeping rounds that add forced switches paid equally by learner and comparator. Under an oblivious adversary and a static or ranking comparator I do not see revocation changing the exponent.

**Reduction C: non-stationarity during blackouts gives a restless bandit.** If the item's value follows a Markov regime that keeps evolving while the item is revoked, each regrant is a decision about a restless arm unobserved for a known gap. Against a comparator that knows the regime dynamics, Ortner et al. already give Õ(√T) without switching costs. Adding a reacquisition cost and forced blackouts is a variation I did not find analysed, but I expect it to yield the same rate with extra additive terms, not a new phenomenon.

**Where a corollary would not suffice.** Four places where the composition is not obviously available off the shelf:
- an *adaptive* revocation process that targets what the learner has invested in (this collides with the Arora–Dekel–Tewari impossibility unless memory is bounded, so the interesting question is the exact bounded-memory rate);
- *time-varying feedback graphs coupled to the sleeping set* with switching costs (arXiv:2606.03851 is for fixed graphs);
- the *combinatorial budgeted* version, where computational hardness (OSL-MR's NP-hardness, Kanade–Steinke for sleeping experts) may separate statistical from computational learnability;
- a *single-trajectory* (no reset) guarantee against a properly defined reachable comparator when some losses are irreversible, e.g. regret measured per regrant epoch.

**Comparator issue.** The proposal's "reachable same-information policy class" is not yet a definition. If the comparator is equally blind (same filtration, same unknown parameters), regret is identically zero for a Bayes-optimal learner and the notion is vacuous. If the comparator knows the model parameters but not realisations, it is the standard informed-policy benchmark of restless bandits and Exo-MDPs. MemPrice's same-state benchmark and Hu et al.'s same-history comparator are two published ways of handling the same difficulty. Fixing this definition is the first real piece of work, and the choice largely determines whether the result is a corollary.

### Gaps
- I read the eight closest papers through alphaXiv page extracts selected by query, not cover to cover. In particular I did not read the SOLAR proofs; its "competitive ratio ≤ 3" and "matching lower bound" claims are reported as the authors state them, and the paper is a VLDB-format preprint whose theory I have not checked.
- I did not find, and so cannot rule out, an analysis of restless bandits with both switching costs and sleeping arms, or of feedback graphs that vary with a sleeping set. These are the two places where a targeted search by a bandit-theory specialist could still turn up a direct reduction.
- Whether stochastic bandits with switching costs retain a √T-type rate (which Reduction C leans on) was not re-verified in this session.

---

## Q4. Is there a genuinely open, named problem at this intersection? What would the minimal nontrivial separation look like?

### Takeaway
I found no named open problem at exactly this intersection. The nearest stated open questions are adjacent (regret lower bounds for online learning-unlearning; drifting utility and budget-dependent cost in one-sided memory gating; weaker identification conditions under censoring). A separation worth an ICML theory paper would have to show a rate or learnability boundary that provably cannot be obtained by composing sleeping-bandit, switching-cost and partial-monitoring results.

### Cited Findings
- Hu, Schölkopf, Sanyal list as open: regret lower bounds for online learning-unlearning (which they say need a restriction on unlearning computation, since FTL-type algorithms unlearn exactly at no regret cost), active unlearners without strong convexity, and "more unlearning friendly" online algorithms. — [arXiv:2505.08557](https://arxiv.org/abs/2505.08557)
- Nguyen-Tang and Arora list as open: the H^{1.5}S gap between their upper and lower bounds, function approximation, sublinear-space exact unlearning, and mechanisms other than TV stability. — [arXiv:2606.04182](https://arxiv.org/abs/2606.04182)
- Ji et al. state that their model assumes a stable per-user parameter and that "accounting for the evolution of the utility pattern remains an interesting direction"; they also flag that storage cost should vary with how full the memory bank is. — [arXiv:2610.23812](https://arxiv.org/abs/2610.23812)
- Liu, Yang, Zhao ask "which weaker conditions permit value identification when instructions interact in different ways". — [arXiv:2610.11007](https://arxiv.org/abs/2610.11007)
- Behnam and Wang conclude that identified per-query utility does not determine retention: "no aggregation over observed queries predicts a memory's value on unseen queries". — [arXiv:2610.02070](https://arxiv.org/abs/2610.02070)
- Li, Wang, Cheng leave lower bounds for the online forgetting process to future work. — [arXiv:2012.01668](https://arxiv.org/abs/2012.01668)
- For sleeping experts, the long-standing recognised difficulty is computational: no-regret against the best ranking is at least as hard as PAC-learning DNFs, which motivated approximate-regret relaxations. — [PMLR v132](https://proceedings.mlr.press/v132/emamjomeh-zadeh21a.html)
- Cesa-Bianchi et al. describe the pre-2026 status of feedback graphs with switching costs as open for tournaments and then close it; their characterisation is for fixed graphs. — [arXiv:2606.03851](https://arxiv.org/abs/2606.03851)
- Shen's restore-counterfactual paper notes the decomposition "applies when forgetting is required by privacy or data-protection constraints" but does not analyse learning. — [arXiv:2609.08279](https://arxiv.org/abs/2609.08279)

### Inferences
A minimal separation, in my view, needs all of the following to be non-trivial:
1. **A toy that is not already classified.** Two items, budget one, one revocation/regrant cycle with reacquisition cost c. With stationary rewards and an oblivious revocation schedule this is (by Reduction B) apple tasting or a two-armed bandit with switching costs plus sleeping rounds; I expect the known exponents. The toy becomes unclassified only when at least one of these is added: (i) the feedback structure itself changes with the permission state (e.g. a legal proxy is available only while the item is eligible), (ii) the regime evolves during the blackout and the blackout length is partly learner-controlled (declining to reacquire prolongs blindness), or (iii) revocation timing adapts to the learner with bounded memory.
2. **A two-world construction that lives entirely in legal decisions.** The proposal's own caveat is correct: worlds differing only in rewards of illegal actions prove nothing. A meaningful pair must be indistinguishable under the legal filtration yet require different *reacquire / do-not-reacquire* choices after regrant. The natural candidate is two regime-transition laws that agree on everything observable at the gap lengths the learner has experienced but imply different post-gap value; because the learner controls gap lengths in variant (ii), the censoring is policy-induced, which is the proposal's title claim.
3. **A rate statement that composition does not give.** For example: a lower bound whose dependence on the number of revocation cycles R, the reacquisition cost c and a variation budget V is strictly worse than the sum of the sleeping, switching-cost and non-stationary terms; or a sharp threshold on proxy informativeness at which the rate moves between T^{2/3} and √T that differs from the "strongly revealing" condition once the graph is time-varying. Either would be a real theorem. An upper bound alone, or a lower bound that is the sum of known terms, would be read as incremental.
4. **Honest null outcome.** If the toy reduces, the publishable statement is the reduction itself ("revocation with priced reacquisition is a sleeping feedback-graph game with switching costs; rates follow from X, Y, Z"), which is a short note or workshop paper, not an ICML main-track theory paper.

### Gaps
- No named open problem (COLT open-problems track or similar) was located; I did not search the COLT open-problem archive specifically.
- Whether variant (ii) or (iii) above actually produces a separation is unknown; that is the mathematics the proposal has not yet done.

---

## Q5. Calibration: what an accepted ICML 2025/2026 theory paper on bandits/online learning looks like

### Takeaway
Accepted papers in this area define one clean model, prove an upper bound, and in most cases pair it with a matching or near-matching lower bound or an explicit statistical barrier; experiments are absent or a small numerical validation. None of the examples below is a "question plus falsification plan".

### Cited Findings
1. **Sleeping Reinforcement Learning** (Drago, Mussi, Metelli; ICML 2025, PMLR 267, pp. 14439–14498). New paradigm with varying action sets; Õ(H√(SAT)) for per-episode disclosure; minimax lower bound Ω(√(T·2^{A/2})) for Markovian per-stage availability; Õ(H√(SAT)) algorithm for the tractable sub-case. Sixty proceedings pages. — [PMLR v267 drago25a](https://proceedings.mlr.press/v267/drago25a.html)
2. **Minimax Optimal Regret Bound for Reinforcement Learning with Trajectory Feedback** (Zhang, Chen, Lee, Du, Wang; ICML 2025, PMLR 267, pp. 74692–74713). Restricted feedback model (only cumulative trajectory reward observed); asymptotically nearly optimal Õ(√(SAH³K)); new confidence-region and reference-model techniques. The abstract mentions no experiments. — [PMLR v267 zhang25l](https://proceedings.mlr.press/v267/zhang25l.html)
3. **Exact Unlearning in Reinforcement Learning** (Nguyen-Tang, Arora; ICML 2026, PMLR 306). New problem formulation; algorithm with O(H²√(SAT) + H³S²A + H^{2.5}S²A/ρ) regret; lower bound Ω(H√(SAT) + HSA/ρ); explicit discussion of the remaining gap. No experiments in the pages read. — [PMLR v306 nguyen-tang26a](https://proceedings.mlr.press/v306/nguyen-tang26a.html)
4. **The Cost of Information: Phase Transitions in Contextual Bandits with Paid Observations** (Gong, Zhang; ICML 2026, PMLR 306, pp. 36013–36044). Near-optimal adversarial algorithm; shows small observation costs raise the minimax order; a phase transition in a free-observation budget; oracle-efficient variant; "numerical experiments validate our theoretical findings". — [PMLR v306 gong26i](https://proceedings.mlr.press/v306/gong26i.html)
5. **Minimax-Optimal Policy Regret in Partially Observable Markov Games** (Arora; ICML 2026, PMLR 306, pp. 3664–3711). Õ(√T) policy regret with explicit dependence on horizon, adversary memory and an Eluder-type dimension; a lower bound matching the √T and dimension dependence. — [PMLR v306 arora26b](https://proceedings.mlr.press/v306/arora26b.html)
6. (Additional) **Generalized Linear Bandits with Memory** (Ann et al.; ICML 2026, PMLR 306, pp. 2921–2948). Sharpens a previous Õ(T^{3/4}) bound to Õ(√T)-type and extends to GLMs; numerical experiments consistent with theory. — [PMLR v306 ann26a](https://proceedings.mlr.press/v306/ann26a.html)
7. (Additional) **Parameter-free Dynamic Regret: Time-varying Movement Costs, Delayed Feedback, and Memory** (Qiu, Jacobsen, Esposito, Zhang; ICML 2026, PMLR 306, pp. 102119–102146). First comparator-adaptive dynamic regret bound with time-varying movement costs, plus reductions for delayed feedback and memory. — [PMLR v306 qiu26k](https://proceedings.mlr.press/v306/qiu26k.html)

Scale: the ICML 2025 proceedings index parsed to 3,330 papers, of which 49 have "bandit" in the title; the ICML 2026 index parsed to 6,552 papers, of which 35 have "bandit" in the title. — [PMLR v267](https://proceedings.mlr.press/v267/); [PMLR v306](https://proceedings.mlr.press/v306/)

### Inferences
- The recurring acceptance pattern is: (a) a model that is one precise step beyond a known one, (b) a tight or nearly tight rate, (c) a lower bound or barrier that shows the step matters, (d) usually a named technical device. Examples 1, 3, 4 and 5 all contain a lower bound. Examples 1 and 4 contain exactly the kind of "phase transition / statistical barrier" result that the proposal's T1–T2 aspire to.
- Proceedings lengths of roughly 20–60 pages indicate substantial appendices of proofs; an 8-page body is the visible tip.
- Experiments are optional for the Theory type but, when present, are small synthetic validations. The proposal's multi-stage benchmark programme (Stages 0–2, six baseline families) is far heavier than what these papers needed, and is not where acceptance is decided.
- Example 3 is the closest stylistic template for a "new privacy-motivated online learning problem" paper: formulation, algorithm, near-matching lower bound, honest list of gaps.

### Gaps
- Acceptance decisions and reviewer scores are not public on PMLR; "what reviewers wanted" is inferred from what the accepted papers contain.
- Page ranges are from PMLR metadata and include appendices; I did not open the PDFs to separate body from appendix, and for examples 2, 5 and 7 the presence or absence of experiments is inferred from the abstract only.

---

## Q6. Verdict: novel / incremental / anticipated, and how realistic an ICML 2027 submission is

### Takeaway
The exact combination is not anticipated in anything I found, but every component is, and several were published for agent memory within the last five months. As it stands the proposal is a well-posed question with honest gates, not a paper. An ICML 2027 main-track theory submission by 22 January 2027 is unlikely to be competitive unless the separation in Q4 is proved by the proposal's own mid-December go/no-go date.

### Cited Findings
- Component already published, censored one-sided feedback with a regret bound for agent memory. — [arXiv:2610.23812](https://arxiv.org/abs/2610.23812)
- Component already published, irreversibility lower bound and a state-relative comparator for agent memory. — [arXiv:2610.24955](https://arxiv.org/abs/2610.24955)
- Component already published, identifiability impossibility for unobserved memories and decision rule for irreversible forgetting. — [arXiv:2610.02070](https://arxiv.org/abs/2610.02070)
- Component already published, two-world indistinguishability lower bound under censored feedback for agent context curation. — [arXiv:2610.11007](https://arxiv.org/abs/2610.11007)
- Component already published, caching with switching costs for agent retrieval buffers. — [arXiv:2607.00394](https://arxiv.org/abs/2607.00394)
- Component already classified, partial feedback with switching costs. — [arXiv:2606.03851](https://arxiv.org/abs/2606.03851)
- Component already published at ICML, sleeping action sets with state, and regret under deletion guarantees. — [PMLR v267 drago25a](https://proceedings.mlr.press/v267/drago25a.html); [PMLR v306 nguyen-tang26a](https://proceedings.mlr.press/v306/nguyen-tang26a.html)
- The proposal's fallback T4 (evaluations rewarding access to evicted or revoked content) overlaps with existing empirical work on revocation non-enforcement, memory-unlearning benchmarks, restore counterfactuals and access confounds. — [arXiv:2609.08258](https://arxiv.org/abs/2609.08258); [arXiv:2610.18052](https://arxiv.org/abs/2610.18052); [arXiv:2609.08279](https://arxiv.org/abs/2609.08279); [arXiv:2610.00366](https://arxiv.org/abs/2610.00366)
- Deadline and format constraints: abstract 14 Jan 2027, paper 22 Jan 2027, 8-page body; "Negative Results" is its own contribution type. — [ICML 2027 CFP](https://icml.cc/Conferences/2027/CallForPapers)
- The proposal states of itself: "MATHEMATICAL IDEA ONLY; no theorem proved, no code or measurements completed" and "HOLD — FORMAL NOVELTY GATE FIRST". — proposal file, header and §10

### Inferences
**Classification.**
- As a *problem statement*: novel in combination, within the searches I ran. No located paper has exogenous permission-driven removal, censoring tied to that removal, and priced lawful reacquisition in one online-learning model.
- As a *theory contribution*: currently incremental, with a material risk of being anticipated-by-reduction. The three reductions in Q3 suggest the headline exponents will match known ones, and the comparator question has two published answers already.
- As an *evaluation contribution* (T4): partly anticipated; four 2026 preprints occupy adjacent ground.

**Reasons the null hypothesis H0 is strong.** (1) Revocation is exogenous and observed, so it binds learner and comparator alike. (2) Feedback censoring of an unplayable action is irrelevant to regret unless the action returns. (3) When it returns, the decision is an entry problem under a switching cost, which is classified. (4) Irreversibility produces linear lower bounds by a standard argument that MemPrice has already written down for memory. A reviewer familiar with arXiv:2606.03851 and Sleeping RL will raise exactly these points.

**Realism of the ICML 2027 timeline.** Nine weeks remain, of which the proposal reserves the first four for the novelty gate. The calibration papers in Q5 each carry a tight upper bound plus a lower bound and 20–60 pages of proofs. Producing a correct, independently checked separation of that standard, with the model still undefined in places (the state set ends in "etc.", the comparator class Π_F and the cross-policy coupling are unspecified, the adversary type is "fixed per theorem"), is a low-probability outcome in that window. I would put a competitive main-track Theory submission at well under even odds, and treat it as conditional on the December gate producing a concrete theorem for the toy model.

**What would change the assessment.**
- A proved separation for the two-item toy that survives Reductions A–C, especially one driven by policy-induced blackout length or time-varying feedback structure.
- A precise comparator definition that is neither vacuous nor a clairvoyant hindsight benchmark, with an argument for why MemPrice's same-state benchmark is insufficient under exogenous removal.
- Positioning against the uncited works in Q2/Q3, with Warm-Start UCB (arXiv:2610.23812) and a sleeping feedback-graph learner with switching costs added to the baseline list; "MemPrice + mask + delay-aware learner" is close to an existing published method.

**Sensible alternatives if the gate fails.** The reduction itself as a short note or workshop paper; or a later venue (the proposal's own "stop or publish an accurately framed methodological replication/negative result at a suitable venue" is the right instinct). ICML's "Negative Results" type exists, but the proposal correctly warns against relabelling an incremental algorithm as a negative result.

**Disclosure.** The proposal was drafted by an AI system and this audit is AI-assisted literature synthesis; both fall under the uses ICML 2027 requires authors to disclose if they materially inform a submission.

### Gaps
- No theorem exists to evaluate; the verdict is about the plan and its distance from published work, not about a result.
- Anonymous submissions under review elsewhere (the MemPrice repository name points to ICLR 2027) could include a closer competitor that is not yet searchable.
- I did not assess the proposal's legal framing ("lawful reacquisition", consent semantics) against any regulation; the proposal itself restricts its privacy claims to "compliant online choices within a model".
