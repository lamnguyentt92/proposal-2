# IDEA_F1 (merged): Estimating wrong PASS verdicts of mobile-agent benchmark graders without auditing the passes

Merged by the coordinator from two independently generated cards that attack the same quantity with complementary instruments. The full cards are the definition of the idea; read both:
- IDEA_T1.md (software-testing transfer) — "SeedCount": fault seeding of end-state faults on the emulator gives the grader's per-failure-mode detection probability agent-free; a Mills / Horvitz–Thompson estimator converts an agent's caught failures into an estimate (with interval) of its uncaught failures, i.e. false passes.
- IDEA_M2.md (measurement) — metamorphic state relations between tasks (a task and its inverse must return device state to the start up to a measured noise mask) certify wrong or extra effects on real agent runs with no human label.

- Gap addressed: G6 (+ G3)
- Target venue and track: ICML 2027, area "Evaluation", contribution type "Datasets, Evaluations and Benchmarks" (fallback "Negative Results")
- Merged core: two label-free instruments for the false-pass rate of state-based graders in Android agent benchmarks — (i) seeded-fault detection probability × caught failures → estimated uncaught failures per agent; (ii) cross-task metamorphic relations → certified lower bound on wrong/extra effects among passes. Validation against blind human audit of a sample of passes.
- Contribution type: new measurement instrument (+ audit findings)
- Generator perspective: merged (software-testing transfer + measurement)
