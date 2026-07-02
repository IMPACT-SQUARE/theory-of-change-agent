# Prompt: Draft-first — Mode C (table-first)

ROLE: The user wants to **see a draft fast and refine it by talking**, not answer a long interview. The
draft is the primary view for the use-case (the PDM table for `intl-dev`, the 변화이론 도식 `toc.md` for
`biz-dev`/`csr-esg`). Ask **one** scoping question, generate a full **draft**, render the primary view,
then **immediately start the refinement conversation** (Step 4) — do not go silent. Work in `meta.lang`.
This mode runs in **gate_mode `DRAFT`** (report-only) until the user says "확정". The guided interview
(interview modes + GATE) is the control; do NOT merge them.

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
- Populate **every** level: impact, **1+ outcomes** (behavioral-change), **3-4 noun-form outputs** (C06),
  activities wired to outputs (C08), inputs (where applicable), per-link assumptions, and indicators each
  with a **MoV** (C04). For `biz-dev`/`csr-esg` apply the use-case relaxations (no 수원기관; ToC framing —
  koica-rules §11).
- Best-guess anything the user didn't give; mark **`stale: true` on every node** ("draft — confirm me");
  use **`"추후 확정"`** for `baseline`/`target`/`target_rationale` (koica-rules §4.8).
- Set `meta.mode = "C"`, `meta.input_source = "concept"`, `meta.interaction = "draft"`, `meta.gate_mode = "DRAFT"`.

## Step 3 — Render the primary view immediately
- Write files per Phase 3 steps 8-9 (source + monitoring in `out/details/`, **primary view LAST**):
  the primary view is **`out/toc.md`** for `biz-dev`/`csr-esg` (변화이론 뷰) or **`out/pdm.md`** for
  `intl-dev`, plus `out/details/monitoring.md`.
- **In DRAFT, the ToC diagram is NOT drawn yet** — `toc.md` shows the narrative + a friendly placeholder
  ("📊 변화이론 도식은 확정 후 그려집니다", render-toc §1). The diagram is generated at Finalize (Step 6).
  Tell the user this in plain language so they know the picture comes after "확정".
- Compute the report-only checks for the nudges: `bash rules/validate-critical.sh --audit
  OUT/details/pdm.json` and `--connectivity OUT/details/pdm.json`. Block nothing.

## Step 4 — Guide the next action (DON'T just stop) ★
The draft is a **starting point, not the answer.** After showing it, immediately make the next step clear
and **start refining conversationally** — never dump the table and go silent. In the SAME turn:
1. **One-line summary** of what you drafted: the core 성과(아웃컴) + the 산출물, in plain language.
2. **Top 1-3 things to firm up** — the highest-leverage weak spots (everything is `stale`/`추후 확정`; use the
   `--connectivity` result for any orphan/disconnected node). Keep it short and specific, not a long dump.
   Prioritize the **outcome** (사회적 가치 = 사회문제 해결 크기, value-rules §V2) and any **broken links**.
3. **Ask ONE specific, leading question to start** — usually the outcome, since it's the crux, e.g.:
   "먼저 성과부터 맞춰볼게요. 지금 초안은 성과를 『…』로 잡았는데, 실제로 노리는 '변화'가 이게 맞나요? 아니면
   어떻게 바꿀까요?" Then go one node at a time.
4. **State the options once** so the path is clear:
   - 바꾸고 싶은 걸 그냥 말하면 됨 (예: "산출물 2를 ~로", "활동 하나 추가").
   - 제가 약한 곳부터 하나씩 여쭤보며 같이 다듬음 (기본).
   - 다 됐으면 **"확정"** → 품질 게이트.
   (Render all of this in `meta.lang`; the Korean above is the `ko` example.)

## Step 5 — Edit loop
Drive the refinement conversation; on **every** edit apply **SKILL Phase 4** — state the connectivity
impact and nudge BEFORE applying, mark dependents `stale`, regenerate only on consent, re-render (primary
view last). Stay in `DRAFT` (report-only).

## Step 6 — Finalize (on "확정"/"finalize")
Hand off to **SKILL.md Phase 3b**: flip `meta.gate_mode = "GATE"`, clear the `stale` flags the user has
confirmed, and run the **hard Critical gate** (`validate-critical.sh` without `--audit`, then C06, then the
Advisory loop). baseline/target may stay `추후 확정`. Only then is it finalized.
- **Now the ToC diagram gets drawn.** Because `gate_mode = "GATE"`, re-rendering `toc.md` (Phase 3b step 5)
  emits the full Mermaid diagram in place of the earlier "확정 후 출력" placeholder. Confirm the diagram is
  present in the finalized `toc.md`.

OUTPUT OF THIS PHASE: a rendered **draft** (primary view + monitoring, gate_mode DRAFT) followed by a
clear next-action prompt that has already started the refinement conversation.
