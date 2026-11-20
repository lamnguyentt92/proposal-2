# Cross-model novelty check — P2

**How to use (manual route):** open a new chat with a model from another family (e.g. GPT or Gemini) with web search enabled, attach the files listed below in full, paste everything under the line, and save the complete answer verbatim as `XMODEL_NOVELTY_P2_RESPONSE.md` with the model name and date.

**Files to attach:** `PROPOSAL.md` (= 09_IDEA_SPEC_P2_ICML.md); from `ideation/05_NOVELTY/`: IDEA_F1_priorart_A.md, IDEA_F1_priorart_B.md, IDEA_F1S_drift_scan.md.

---

Role: you are an independent prior-art hunter. Your job is adversarial: try to find the research idea in the attached specification ALREADY PUBLISHED, in whole or in part. You succeed when you find anticipation, not when you confirm novelty.

Venue: ICML 2027, topic area Evaluation, contribution type Datasets, Evaluations and Benchmarks. Today's date: use the current date; cover work up to today.

Task:
1. Read the specification and the attached prior-art reports. Do not trust them: re-check their three closest works yourself.
2. Search widely (arXiv, OpenReview including submissions under review, ACL Anthology, proceedings of ICML/NeurIPS/ICLR/ACL/EMNLP, software-engineering and security venues where relevant, GitHub, theses, workshops). Use synonyms and older terminology. Give priority to anything the attached reports say they could NOT search.
3. For each claim in section 5 of the specification, state whether you found it anticipated, partly anticipated, or not found.

Rules: cite only works whose primary record you opened, with an identifier (arXiv ID, DOI, URL) and how you verified it (full text / abstract / index listing). Never invent a paper. A search that finds nothing is not proof that nothing exists: list your queries.

Output format:
- Searches run (queries, sources, dates)
- Closest works (3–5 or more): identifier — what it does — exact delta — does the delta matter to a referee?
- Claim-by-claim status
- Verdict: novel | incremental | anticipated — reason
- What you could not search
