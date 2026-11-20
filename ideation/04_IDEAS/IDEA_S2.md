# IDEA_S2: Borrowed voice: person-reference congruence as an implicit authority cue in indirect prompt injection (Vietnamese-English)

Source tags for identifiers: [notes] = in the research-notes files; [read] = primary record opened in this session (alphaXiv full text); [index] = alphaXiv index record only.

- Gap addressed: G2 (touches G12 through the English-pivot claim; a memory carry-over arm for G4 is left to the extension).

- Target venue and track: ACL 2027 main conference through the ARR January 2027 cycle; area "Multilingualism and Cross-Lingual NLP" (alternative: "Discourse and Pragmatics"); ARR contribution types "model analysis & interpretability" and "data resources".

- Problem (1 paragraph): An agent serving a non-English user sees three texts whose languages vary independently: the user's request, the surrounding tool or UI content, and any directive a third party has planted in that content. The three multilingual agent-security studies to date vary only the request language or are too small to separate effect from noise (2610.22244, 2610.23093, 2608.15392, all [notes]); chat-level work frames the risk as weaker safeguards in lower-resource languages (2610.27304 [read]). Whether an agent treats a directive as more authoritative because it sounds like its user is unknown, and English offers no clean way to ask the question.

- Key insight (the non-obvious observation; 2–3 sentences): English "I/you" says nothing about who is speaking, so injection research has located authority in position (which file or field the text sits in; 2610.38867 [read]). Vietnamese person reference is open-class: every utterance picks a self/addressee pair (anh/chị–em, cô/chú–cháu, mình–bạn, tôi–bạn ...) that encodes the dyad, and the user fixes their dyad with the assistant in the request. A planted directive must therefore choose a dyad; matching the user's claims the user's voice with no explicit claim, mismatching reveals another speaker, and this gives a minimal pair (same content, same position, same language) that tests whether agents assign authority by linguistic identity. Translated benchmarks cannot see this, because machine translation neutralises or drops the pair.

- Approach (how the insight becomes a method/system/theory):
  1. Executable sandbox scenarios (tool-calling tasks with state-verified outcomes; an Android-app slice is optional). Primary instrument: out-of-task but harmless directives, following the non-malicious-goal design of 2611.11861 [read], so that effects are measurable above the floor and no harmful content is needed; a small state-verified security subset checks external validity.
  2. Factorial manipulation: user language (Vietnamese, English, Vietnamese-English code-switched) x content/UI language (Vietnamese, English) x directive language (Vietnamese, English, code-switched) x dyad (matches the user's, neutral, a different natural dyad; defined where the directive contains Vietnamese).
  3. All Vietnamese and code-switched text is written, not machine-translated, and cross-validated by two native annotators for naturalness in isolation, propositional equivalence across conditions, and the dyad reading, with agreement reported.
  4. Analysis: mixed-effects logistic regression with scenario and model random effects; pre-registered contrasts for the congruence interaction and the dyad ordering; outcomes conditioned on the agent having read the directive.
  5. Two probes of mechanism: English-centric injection detectors and guards scored on the same items; and a translate-first condition that forces the English pivot documented in 2608.11110 [read], to test whether pivoting erases the cue.

- Contribution type: new problem

- Claims (falsifiable, 2–4):
  - C1 (language congruence): with content and position fixed, directives in the user's language are followed more often than directives in the other language, in both directions; the effect is an interaction, not a main effect of directive language or resource level.
  - C2 (dyad congruence): within Vietnamese, compliance is ordered matched > neutral > different dyad, with a pre-registered minimum gap between matched and different.
  - C3 (blind detectors): at a fixed false-positive rate, English-trained detectors and guards do not separate matched from different-dyad directives and detect Vietnamese and code-switched directives less often than English ones.
  - C4 (pivot erasure): forcing translation into English before the agent reads the content shrinks the dyad effect, i.e. homogenising the input removes a provenance signal.

- Closest work known so far (with identifiers) and the expected delta:
  - 2610.38867 [read]: same directive, different placement, up to 2.6x difference in compliance. Delta: holds placement fixed and varies linguistic identity; effect sizes are compared directly.
  - 2610.22244 [notes]: guard verdicts flip when only the user instruction is translated (five languages, translations by a guard under test, no Vietnamese). 2610.23093 [notes]: request language changes tool admission for harmful requests. 2608.15392 [notes]: English/Tamil/Tanglish injections, eight scenarios, one model, inconclusive. Delta: three language roles varied independently, executable environment, native-authored items, a linguistic mechanism instead of a resource-level account.
  - 2608.11110 [read]: agents route non-English tasks through English and keep the pivot under instruction. Delta: tests a security consequence of the pivot.
  - 2611.11861 [read]: non-malicious attacker goals isolate instruction hierarchy from security knowledge. Delta: reused as the measurement instrument, crossed with language and dyad.
  - 2406.15481 [notes] (code-switching red teaming, chat level), 2610.27304 [read] (translation bypass across 79 languages), 2609.23490 [notes] (multilingual agent capability). Honorific/kinship work on other tasks exists (2609.26942, 2610.14769 [index]) but I found none on authority or injection; an alphaXiv search on 2026-11-20 for Vietnamese address terms combined with speaker attribution or injection returned nothing relevant (absence of evidence only).

- Evaluation sketch: settings, baselines (strongest first), metrics, decisive experiment
  - Settings: about 40 base scenarios, each realised in all cells; five or six commercial models and two or three open models; exposure verified per run.
  - Baselines: (1) an explicit authority claim in the directive (it states it comes from the user) versus the dyad alone, to see whether the implicit cue rivals the explicit one; (2) placement manipulation after 2610.38867 as an effect-size yardstick; (3) machine-translated versions of the same items, the result a translated benchmark would report; (4) an English identity control (the directive uses the user's name) to test whether the effect is specific to grammaticalised person reference; (5) the resource-level main-effects model as the competing explanation; (6) prompt-level marking of untrusted content (spotlighting, 2403.14720 [notes]) to see whether it removes the dyad effect.
  - Metrics: compliance conditional on exposure, attempt vs. completion, user-task completion, ignore vs. refuse; odds ratios with intervals; detector true-positive rate at fixed false-positive rate.
  - Decisive experiment: Vietnamese-Vietnamese minimal pairs differing only in dyad, both members rated natural by both annotators. If the matched-minus-different difference has an interval covering zero for every frontier model and the congruence interaction is null, the insight is wrong and agents assign authority by channel only.

- Resources needed vs available (00_CONSTRAINTS.md): two or more native Vietnamese annotators fluent in English are exactly the scarce resource this design needs and the constraint file lists them; commercial APIs cover the agents; 1–2 GPUs cover open models and detectors; the optional Android slice uses existing emulator expertise. Data are fictional; no real conversations.

- Risks and unknowns: frontier models may sit at the floor even for harmless directives; a "different" dyad may differ in register as well as speaker, so naturalness and register need separate ratings; regional variation in address terms; a Vietnamese-centred study can be judged narrow, so the paper must frame Vietnamese as the test case for a class (open-class person reference also exists in Thai, Japanese, Korean, Indonesian) and show the English name control; the result tells an attacker to mirror the user's dyad, which calls for evaluating a mitigation in the same paper and a careful ethics section; I did not verify whether ACL 2027 keeps a safety area (the notes flag the area list as needing a re-check).

- Conference core / journal extension (1 line each):
  - Core: the factorial with native-authored minimal pairs, the detector probe and the pivot test.
  - Extension (Computational Linguistics): does memory consolidation preserve or erase the dyad and language of a stored directive (provenance laundering, 2607.29167 [notes]), further languages with open-class person reference, and localised mobile UIs.

- Generator perspective: adversarial/security
