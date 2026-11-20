# IDEA_V1R: Does it sound like my user? Vietnamese person reference and force marking as a controlled test of role confusion in indirect prompt injection

Revision of IDEA_V1 (= IDEA_S2 + IDEA_M3 + IDEA_L3; read those cards for detail) after the Stage 5 novelty attack.
Hunter A: novel for the core instrument only; hunter B: incremental. This card applies their corrections.

- Gap addressed: G2.
- Target venue and track: ACL 2027 via ARR — "LLM Agents for NLP" or "Multilingualism and Cross-Lingual NLP".

- Problem: "Prompt Injection as Role Confusion" (arXiv:2603.12277, ICML 2026) shows models attribute text to a role by how it sounds, not by its role tag, and that stripping user-like style cuts attack success from 61% to 10%. But "style" there is an uncontrolled bundle in English. Whether a *single grammatical feature that identifies this particular user* drives role attribution is untested, and no natively authored non-English agent-security benchmark with a human attribution baseline exists.

- Key insight (revised): Vietnamese grammaticalises exactly the variable the role-confusion account needs. Self/addressee terms encode the speaker–addressee dyad of *this session*, so an injected directive can match or mismatch the user's established dyad with content, position, language and politeness level held constant; and bare verb phrases are ambiguous between log line, plan and command, so force marking (particles such as *hãy, đi, nhé*) can be varied independently. This gives a two-factor minimal-pair design (dyad congruence × force marking) with a native-speaker baseline for "who wrote this sentence, and is it an instruction?" — a controlled linguistic test of an account currently supported only by bundled English style manipulations.

- What is NOT claimed (already published): that models assign authority by linguistic identity (arXiv:2603.12277; role-spoofing probe in arXiv:2610.40396); the language-congruence effect (XIH-Bench arXiv:2607.23545; ACL Anthology 2026.oracle-main.13) — treated as replication; the identity-match asymmetry in English (AgentDojo arXiv:2406.13352, Table 2: correct user name 46.1% vs wrong name 23.2%); honorific form as a safety variable in direct requests (Korean, OpenReview s9A7n7Mllv, ARR Oct 2026; KCI DOI 10.33778/kcsa.2025.25.5.117).

- Claims (falsifiable):
  - C1: with register (politeness level) matched, dyad-congruent injected directives are followed more often than dyad-incongruent ones in Vietnamese; the effect exceeds the English name-match control. Refuted by a null effect at adequate power.
  - C2: the VI–EN gap in compliance and in detector recall concentrates on particle-less (force-unmarked) items; a flat gap across force marking refutes the insight.
  - C3: native readers attribute dyad-incongruent directives to a non-user source at a rate models do not match (human–model attribution gap).
  - C4: translating content to English before the agent or guard sees it erases the congruence effect and the cue.

- Required controls from the novelty attack: register-matched control (separates "sounds like the user" from speech level); English identity control (AgentDojo name match); machine-translated Vietnamese arm (WMT 2026 2026.wmt-main.16 suggests MT picks a plausible dyad); harmless out-of-task directives as the main instrument (no harmful payloads).

- Known competitors: BabelDojo (faerber-lab; multilingual AgentDojo extension with Vietnamese in its candidate pool; README says experiments not yet run); BrowseSafe++ (arXiv:2610.17457; contains 46 in-the-wild Vietnamese injections); the Korean honorification ARR submission.

- Resources: commercial APIs + 1–2 GPUs; ≥ 2 native Vietnamese annotators (available). Sandboxed tool environment only.

- Risks: floor effects on frontier models; one natively controlled language; same-cycle competitor on honorifics; the effect may be small (XIH-Bench congruence effects were 2–6 points).

- Status: reserve finalist for the ACL slot (shares its linguistic resource with IDEA_L1R; the two must not overlap in claims).
