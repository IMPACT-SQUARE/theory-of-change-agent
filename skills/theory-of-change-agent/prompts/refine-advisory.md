# Prompt: Advisory self-check + conversational refinement loop

ROLE: After the Critical gate passes, evaluate the Advisory rules (A01-A08 in `rules/checklist.json`) on
`OUT/pdm.json` and, if below threshold, refine conversationally with the user. LLM judgment; work in the
user's language.

## Scoring (per-rule-type)
- 8 rule types (A01-A08). A type **passes** or **fails**.
- For per-indicator rules **A01 (SMART)** and **A02 (CREAM)**: the type passes if **>50% of indicators**
  satisfy the criterion (soft majority). For others, apply the rule's `check` directly.
- `pass_rate = (#passing rule types) / 8`. Threshold = `advisory_threshold` (default 0.8 → ≤1 type may fail).

## Evaluation
For each Advisory rule, judge against its `check` and the guidance in `rules/koica-rules.md`:
- A01 SMART · A02 CREAM · A03 ≥1 gender-disaggregated indicator · A04 each proxy has justification ·
  A05 target realistic vs baseline · A06 measurable at end-of-project evaluation · A07 output is not a
  restatement of activities · A08 outcome is a behavioral change.
Produce a short report: per rule → pass/fail + (if fail) the specific node(s) and why.

## Refinement loop (only if pass_rate < threshold)
1. Present the failing rules and concrete suggestions.
2. For each, ask the user a targeted question OR propose a concrete edit to approve.
3. Apply approved edits to `pdm.json` (and mark dependents stale per SKILL Phase 4 if structure changes).
4. **Re-run ALL Advisory checks** (not just the previously-failing ones — catch regressions).
5. Repeat. **Max 3 rounds** (`--max-advisory-rounds`). Exit when: threshold met, max rounds reached, or
   the user says "accept as-is".
6. On exit, report the final pass_rate and any remaining failures (these are surfaced, not blocking).

## Important
- Advisory NEVER blocks finalization — it improves quality up to the threshold, then proceeds.
- Do not modify Critical-rule compliance while refining (re-run the deterministic validator if structure
  changed).
