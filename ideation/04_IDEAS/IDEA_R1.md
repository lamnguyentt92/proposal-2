# IDEA_R1 (merged): Red teaming as unseen-species sampling — missing-mass bounds on what the red team did not find

Merged by the coordinator from two independently generated cards that converged on the same idea. The full cards are the definition of the idea; read both:
- IDEA_S3.md (security perspective) — overlap between independent red-team campaigns gives a lower bound on the breakable fraction of a defended agent; rarefaction makes attackers with unequal budgets comparable.
- IDEA_M1.md (measurement perspective) — discovery probability (chance the next query exposes a new vulnerability class) estimated from singletons, with the adaptive-search-bias correction from fuzzing (STADS).
- Related theory card: IDEA_H1.md (horizon laws for ASR@k).

- Gap addressed: G8 (serves G5)
- Target venue and track: ICML 2027, area "Evaluation" (alternative IJCAI 2027 main track)
- Merged core: treat a red-teaming campaign as a species-discovery process; report budget-independent quantities (missing mass / discovery probability, lower bound on breakable fraction) instead of ASR@k; compare attackers by rarefaction.
- Contribution type: new measurement method (+ statistical guarantee)
- Generator perspective: merged (security + measurement)
