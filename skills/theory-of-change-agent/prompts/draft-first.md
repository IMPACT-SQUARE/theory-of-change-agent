# Prompt: Draft-first — Mode C (table-first)

ROLE: The user wants to **see a PDM table fast and edit on top of it**, not answer a long interview. Ask
**one** scoping question, then immediately generate a full **draft** PDM, render it, and hand control to
the edit loop. Work in the user's language. This mode runs in **gate_mode `DRAFT`** (report-only) until
the user finalizes. The existing guided interview (Mode A/B + GATE) is the control; do NOT merge them.

## Step 1 — One scoping question (the only required question)
Ask a single open question that captures enough to anchor the results chain. Suggested framing:

> "이 사업을 한 줄로 알려주세요 — **누가 / 어디서 / 무엇을 통해 / 어떤 변화(성과)를 노리는지**.
> (이미 가진 메모·목표·산출물 목록이 있으면 같이 붙여주셔도 좋아요.)"

- Offer 2-4 options via the environment's interactive choice tool (`AskUserQuestion` / `ask_user_input_v0`
  / equivalent — see SKILL.md Guardrails) ONLY if it helps the user pick an outcome scope; otherwise keep
  it open. Accept whatever detail the user gives — partial is fine.
- Do **not** chain follow-ups here. One question, then generate. (Refinement happens after the table.)

## Step 2 — Generate a full draft (best-guess)
Call `prompts/generate-pdm.md` in **draft mode**:
- Populate **every** level: impact (SDGs + national strategy), **1+ outcomes** (behavioral-change),
  **3-4 noun-form outputs** (C06), activities wired to outputs (C08), inputs, per-link assumptions, and
  indicators each with a **MoV** (C04).
- Best-guess any field the user did not give; mark **`stale: true` on every node** (signals "draft —
  confirm me"); use **`"추후 확정"`** for `baseline`/`target`/`target_rationale` and any other ungrounded
  value (koica-rules.md §4.8).
- Set `meta.mode = "C"`, `meta.gate_mode = "DRAFT"`.

## Step 3 — Render immediately + non-blocking report
- Render `pdm.md` and `monitoring.md` right away (`render-pdm-md.md`, `render-monitoring-md.md`).
- Run checks **report-only**: `bash rules/validate-critical.sh --audit OUT/details/pdm.json` + the LLM checks.
  Present results as a **draft checklist** ("아직 비어있거나 보완이 필요한 부분"), **blocking nothing**.
- Tell the user explicitly: *this is a draft — edit any cell, and say "확정"/"finalize" when ready to run
  the full quality gate.*

## Step 4 — Edit loop
Hand off to **SKILL.md Phase 4 (edit propagation)**: the user edits a node, you mark dependents stale and
regenerate only on consent. Stay in `DRAFT` (report-only) during editing.

## Step 5 — Finalize (on the user's request)
When the user says "확정"/"finalize", hand off to **SKILL.md Phase 3 Finalize**: flip
`meta.gate_mode = "GATE"`, clear `stale` flags the user has confirmed, and run the **hard Critical gate**
(`validate-critical.sh` without `--audit`, then C06, then the Advisory loop). Only a PDM that passes the
GATE gate is a finalized, guideline-compliant PDM.

OUTPUT OF THIS PHASE: a rendered **draft** PDM (pdm.json/pdm.md/monitoring.md, gate_mode DRAFT) plus a
non-blocking gap checklist, ready for editing and later finalization.
