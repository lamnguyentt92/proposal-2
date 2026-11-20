# IDEA_T3: LocaleLadder — pseudo-localization as a placebo that separates "language" from "letters and layout" in mobile-agent evaluation

- Gap addressed: G2 (language as a variable in agent reliability/safety; no GUI/mobile, no Vietnamese), with G3 (locale-invariance of the grader as a validity check).

- Target venue and track: ACL 2027 via ARR (long paper), area "Multilingualism and Cross-Lingual NLP" (alternative: "LLM Agents for NLP"; ARR's own list also has "Resources and Evaluation").

- Problem (1 paragraph):
  Multilingual agent benchmarks report large drops when the environment is localised and attribute them to language. SEATauBench (2606.28715), which includes Vietnamese, localises dialogue, tool schemas and domain content one surface at a time and finds the steepest losses under full localisation; BabelArena (2609.23490), LoWAgent (2610.27205) and macOSWorld (2506.04135) report similar gaps. But localising a surface changes three things at once: (a) surface form — non-ASCII glyphs, diacritics, tokenisation; (b) layout — longer strings, truncation, wrapping, mirrored direction; (c) the language in which meaning must be grounded against the instruction. No existing design separates them, translations are machine-produced and then patched (SEATauBench records 2,894 approved corrections), and the apparatus itself can break under localisation (2610.16067 finds a language effect that reverses in a second domain). For executable mobile GUI agents I found no multilingual benchmark at all: GUI-CEval (2603.15039) is Chinese-only capability testing and MPR-GUI-Bench (2512.00756) covers perception and reasoning only; the four mobile safety papers in the notes contain no multilingual terms.

- Key insight (the non-obvious observation; 2–3 sentences):
  Software internationalisation testing already has a placebo for this confound: pseudo-localization. Android ships two pseudolocales — en-XA (accented, expanded, bracketed English) and ar-XB (English forced right-to-left) — that perturb surface form and layout while the meaning stays English, and Android's resource system swaps UI strings without touching app logic, database schema or a state-based checker. So UI language becomes an independent variable under which the oracle is invariant by construction, and the share of the "language gap" that is really a letters-and-layout gap can be measured without translating a single string.

- Approach (how the insight becomes a method/system/theory):
  1. Ladder of conditions on the same tasks, apps and checkers: en -> en-XA (surface) -> ar-XB (layout direction) -> real UI locale (vi, plus any other locale the apps already ship) -> + Vietnamese instruction -> + Vietnamese user content (contact, note, file names seeded by task setup). Instruction language, UI locale and content language are crossed, not nested, so matched and mismatched cells both exist.
  2. Vietnamese-specific strata that need native speakers: instructions typed without diacritics (common user behaviour) against a diacritic UI, and partially localised apps (community translations with untranslated strings).
  3. Grader metamorphic relation: a gold script keyed on resource-ids (not strings) must PASS under every locale. Any failure is a locale-dependent checker defect (string match on an English label, date or decimal format) and is repaired before agents are scored; the count is itself a result.
  4. Human work: two native annotators independently translate and adjudicate the instructions, rate the app-shipped Vietnamese strings, and write the no-diacritic variants. UI strings for other locales need no annotators because they are the apps' own resources.
  5. Analysis: mixed-effects logistic model with task random effects; decomposition of the en -> fully-Vietnamese drop into surface, layout, UI-semantic, instruction, content and interaction terms; screenshot-only versus accessibility-tree agents to separate recognition from tokenisation.
  6. Secondary security arm (addresses the independent-variation design named in G2): on an injection subset, cross injected-content language (en / vi / code-switched) with UI and instruction language, and report exposure-conditioned outcomes.
  Engineering note: pseudolocales must be enabled at build time (`pseudoLocalesEnabled`, per https://developer.android.com/guide/topics/resources/pseudolocales), so the open-source apps are rebuilt in a debug variant or given generated pseudo-localised resources; the page describes devices only, emulator behaviour must be checked.

- Contribution type: new measurement/benchmark (a controlled design with a placebo; the result may be a negative finding about "language gaps").

- Claims (falsifiable, 2–4):
  C1. For screenshot-based agents, at least one third of the en -> Vietnamese-UI success drop is reproduced by en-XA alone, with no change of language. Falsified if en-XA is within the interval of en while the Vietnamese UI drops.
  C2. Mismatched cells (English instruction with Vietnamese UI, or the reverse) lose more than the fully Vietnamese matched cell: the cost lies in cross-lingual grounding, not in Vietnamese as such.
  C3. A non-zero number of native success checkers are not locale-invariant (the gold script fails under at least one locale); left unrepaired they would be read as agent language deficits.
  C4. (Security arm) An English injection inside a Vietnamese UI is followed more often than a Vietnamese injection inside an English UI, after conditioning on the agent having reached the injected screen.

- Closest work known so far (with identifiers) and the expected delta:
  Prior-art check run in this session (queries: "pseudo-localization GUI agent benchmark", "multilingual Android/AndroidWorld locale", "metamorphic testing LLM agent evaluation"): no use of pseudo-localization with agents was returned; no multilingual executable Android benchmark was returned. "Not found" is not "does not exist"; ACL Anthology-only papers may be missed.
  - 2606.28715 SEATauBench [read]: progressive localisation for a text tool-agent benchmark in five languages incl. Vietnamese, machine translation with native audit, canonical execution layer. Delta: every rung changes language and surface together; no placebo; no GUI.
  - 2610.22244 LinguaGuardBench [read]: translates only the user instruction; controls are a whitespace placebo and six English rewordings; guards, not agents. Delta: its placebo cannot reproduce script or layout change; no UI axis.
  - 2506.04135 macOSWorld (5 languages, instructions + OS UI), 2512.00756 MPR-GUI-Bench (six aligned languages, perception/reasoning), 2603.15039 GUI-CEval (Chinese apps), 2609.23490 BabelArena, 2610.27205 LoWAgent, 2610.23093 (language effects on tool admission), 2610.16067 (localising the apparatus moves the measurement). Delta: none separates surface, layout and meaning; none verifies grader invariance with reference scripts.
  - MAPS (Findings of EACL 2026) is cited inside 2606.28715 and 2610.16067 as translating instructions of existing agent benchmarks; I did not open it.
  Expected delta in one line: first executable mobile-agent evaluation in which UI language is varied with a meaning-preserving placebo and a provably unchanged oracle, giving a decomposition of the cross-lingual gap rather than a single drop.

- Evaluation sketch: settings, baselines (strongest first), metrics, decisive experiment
  Settings: AndroidWorld 2405.14573 tasks whose apps ship Vietnamese resources (coverage reported); injection subset from MobileSafetyBench 2410.17520 for the security arm. 5–6 agents: frontier API models with screenshot and with accessibility-tree input, plus open GUI models on the GPUs; 3 seeds per cell; fractional factorial to bound cost.
  Baselines: (B1) the same ladder without the pseudolocale rungs, i.e. the SEATauBench-style reading, to show which conclusion the placebo changes; (B2) translate-then-act: the agent receives the accessibility tree machine-translated into English — the mitigation a referee will ask for; (B3) instruction-only controls in the style of 2610.22244 (whitespace placebo, English paraphrase).
  Metrics: success with task-clustered intervals; variance shares of the decomposition; step-level grounding error rate; number of locale-dependent checkers; for the security arm, exposure-conditioned attack outcomes.
  Decisive experiment: en vs en-XA vs Vietnamese UI, English instruction held fixed, all agents. If en-XA equals en within the interval while the Vietnamese UI drops, the letters-and-layout hypothesis (C1) is refuted and the gap is linguistic.

- Resources needed vs available (00_CONSTRAINTS.md):
  Needed: emulator images and rebuilt open-source apps with pseudolocales, gold scripts keyed on resource-ids, API budget for a factorial of roughly tasks x 3 seeds x 6–8 cells x 5 agents, 1–2 GPUs for open GUI models, two native Vietnamese annotators fluent in English working independently. Available: all of these match the stated constraints (Android testing expertise, commercial APIs + 1–2 GPUs, >=2 native annotators). Emulator availability to be confirmed.

- Risks and unknowns:
  1. Frontier agents may show no drop in any cell; the paper then rests on open models and on C3, and reads as a negative result.
  2. Vietnamese resource coverage of the benchmark apps may be partial; rebuilding apps with pseudolocales may be laborious for some.
  3. One human-validated target language can be judged narrow; mitigated because the UI axis can include every locale the apps already ship, but instruction-side claims stay Vietnamese-only.
  4. Fit at ACL: must be framed as cross-lingual grounding and evaluation methodology, not as a GUI systems paper.
  5. en-XA also lengthens strings, so surface and expansion effects are partly entangled; a length-only control (padded English resources) may be needed.
  6. Overlap check required against the project's G1/G12 Vietnamese memory idea: this card shares annotators, not content.

- Conference core / journal extension (1 line each):
  Core: the ladder, the decomposition and the checker-invariance audit on one mobile benchmark, with the security arm as a secondary study.
  Extension: full injection-language factorial with detectors/guards, further languages with native annotators, mitigation study, for Computational Linguistics (accepts substantially extended conference papers).

- Generator perspective: cross-domain transfer (software testing)
