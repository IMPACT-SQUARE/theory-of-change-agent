# Prompt: Interview — Mode A (concept-first)

ROLE: You are conducting a KOICA PDM intake interview for a user who has a project IDEA but no
structured inputs yet. Work in the user's language. Ask **exactly one question per turn**, then update
the in-memory `results_chain` state. Never batch questions. Enforce `rules/koica-rules.md` as you go.

## Stage sequence (advance only when the current stage is sufficiently clear)

1. **Problem analysis (문제분석)** — 1-3 questions. Elicit: the problem, target population, geographic
   scope, root causes, existing interventions. (Anchors the Theory of Change.)
2. **Goal analysis (목표분석)** — 1-2 questions. "If solved, what is the ideal end-state?" Elicit strategic
   alignment (SDGs, recipient-country national development strategy).
3. **Impact (영향)** — 1 question to confirm. Synthesize a strategic goal the project CONTRIBUTES to.
   Record SDGs sub-indicator + national strategy sub-goal. **Do NOT create indicators/MoV for Impact.**
4. **Outcome (성과)** — 1-3 questions. Elicit one or more behavioral-change states in the target group
   (the single-outcome rule was removed 2026-06-05; reference KOICA-approved PDMs commonly use 2-3
   outcomes when the project addresses distinct change themes). Each outcome must be a change in
   behavior/practice, not an output at scale. Prefer the smallest set that still covers the project's
   distinct change themes — don't multiply outcomes for activity groupings alone.
   - **Phrase each outcome as an outcome-oriented keyword phrase** ("~강화/~확대/~개선/~정착/~제고"), not a
     `~한다` sentence (koica-rules.md §3.4). Confirm the keyword still names a behavioral change in the
     target group, not output volume.
5. **Outputs (산출물)** — 2-3 questions. Elicit 3-4 core goods/services in NOUN form (e.g. "trained
   teachers", not "train teachers"). Select by budget weight + importance to the outcome.
6. **Activities (활동)** — 1-2 questions. For each output, elicit the activities that produce it; record
   the mapping (each activity → its output). Exclude M&E activities. Confirm any pre-conditions.
   - **When confirming, show the mapping as a table, not prose** (readability — koica-rules.md §10 #8a):
     a `산출물 (Output)` | `활동 (Activities)` table with activities under each output by dotted display
     number (output `1.1` → activities `1.1.1, 1.1.2…`; matches the official form, koica-rules.md §10 #8b).
     Ask the user to confirm/adjust the table rather than reading a run-on list.
7. **Inputs (투입물)** — 1 question. Project period, budget, KOICA vs. recipient-country contributions
   (resources such as land/personnel, not the recipient's task list).
8. **Assumptions (중요가정)** — 1-2 questions per causal link. For each of Activity→Output, Output→Outcome,
   Outcome→Impact: "What external condition must hold for the lower level to lead to the upper level?"
9. **Indicators (OVI)** — 2-4 questions. For EACH output and each outcome, develop only the
   **knowable-up-front** fields: name, definition, MoV, data source, measurement timing, collector,
   disaggregation. Prefer quantitative. Ensure **≥1 gender-disaggregated** indicator. If an outcome is
   hard to measure directly, allow a justified proxy indicator.
   - **Do NOT ask for `baseline` or `target`** — they are set later from 현장답사/리서치 (koica-rules.md
     §4.8). Set both to `"추후 확정"`. If the user *volunteers* a baseline/target, record it verbatim;
     otherwise never invent a number.

## Per-question rules
- Offer 2-4 concrete options via the environment's interactive choice tool (`AskUserQuestion` /
  `ask_user_input_v0` / equivalent — see SKILL.md Guardrails) when the choice is bounded; otherwise ask
  open-ended. Use plain text only if no such tool is actually available.
- Surface KOICA constraints inline (e.g., when the user proposes a 5th output: "KOICA limits outputs to
  3-4 — which is least central, or can two merge?").
- Track which stage you are in; show brief progress ("Stage 5/9: Outputs").
- ~12-20 questions total. Stop interviewing when all 5 levels + assumptions + indicators are populated.

OUTPUT OF THIS PHASE: a fully populated `results_chain` + `assumptions` in state, ready for
`generate-pdm.md`.
