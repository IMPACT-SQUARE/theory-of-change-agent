---
name: theory-of-change-agent
description: |
  변화이론 에이전트 (Theory of Change Agent) — KOICA PDM (Project Design Matrix) 생성 스킬.
  Interviews the user following Theory-of-Change methodology, then produces a PDM matrix +
  monitoring matrix grounded in the KOICA PDM guideline. ALWAYS asks the user first which of three
  approaches to use: [A] concept-first interview, [B] inputs-held, or [C] draft-first (table-first).
  Output language mirrors the user's input language.
  Use when the user mentions: "변화이론 에이전트", "theory of change agent", "PDM",
  "project design matrix", "KOICA", "theory of change", "변화이론", "results chain", "로직 모델",
  "logframe", "logical framework", "impact harness", "임팩트 하네스" (legacy name), or wants to
  draft/audit a development-cooperation results matrix.
argument-hint: "[--use-case intl-dev|biz-dev|csr-esg] [--concept <brief> | --inputs <file> | --draft] [--lang en|ko] [--advisory-threshold 0.8] [--audit]"
allowed-tools: Bash, Read, Write, Edit, AskUserQuestion
---

# 변화이론 에이전트 (Theory of Change Agent) — KOICA PDM 생성

<Purpose>
**변화이론 에이전트 (Theory of Change Agent)** turns a vague project idea (or a partial draft) into a
guideline-aligned results chain through a one-question-at-a-time interview, then renders it. It serves
several **use-cases** that share one underlying results-chain engine and differ only in the rendered
end-view (Phase 1 step 0): **국제개발/KOICA PDM** renders a **KOICA-compliant PDM matrix** (the most
mature path); **사업개발(소셜벤처·사회공헌·비영리)** and **CSR/ESG** render a **Theory-of-Change view**
(node diagram); **투심(임팩트 투자심사)** is planned. The KOICA PDM path encodes the writing rules
(`rules/koica-rules.md`) and gates on a deterministic + LLM-judged self-check (`rules/checklist.json`,
`rules/validate-critical.sh`), the same checklist that scores the benchmark. **Always ask the use-case
first, then the interaction mode** (Phase 1); never pick either unilaterally.
</Purpose>

<Output_Contract>
The skill writes files to the working directory (default `./out/`, override with `--out`):
- **`pdm.json`** — the single source of truth. An ID-linked results-chain DAG conforming to
  `schema/pdm-schema.json`. All other outputs are RENDERED from it.
- **`pdm.md`** — the PDM matrix (4-row × 4-column KOICA format). Primary end-view for `intl-dev`.
- **`toc.md`** — the Theory-of-Change view (Mermaid node diagram + ToC narrative). Primary end-view for
  `biz-dev`/`csr-esg`; optional for `intl-dev`.
- **`monitoring.md`** — the monitoring matrix (indicator definition / baseline / target / rationale /
  source / timing / collector / disaggregation). Produced for all use-cases.

Which files are written depends on `meta.use_case` (see Phase 3 step 8). Out of scope (do NOT produce):
the annual performance-check sheet, direct `.xlsx`, any web UI.
</Output_Contract>

<Reference_Files>
Load these (they live alongside this SKILL.md) and treat them as authoritative:
- `rules/koica-rules.md` — the KOICA PDM writing rules (with guideline page citations).
- `rules/checklist.json` — Critical (C01-C08) + Advisory (A01-A08) self-check definitions + thresholds.
- `rules/validate-critical.sh` — deterministic validator for the structural Critical rules.
- `schema/pdm-schema.json` — JSON Schema for `pdm.json`.
- `schema/pdm-example.json` — a complete, guideline-compliant reference instance (Nicaragua).
- `prompts/*.md` — prompt templates for each phase (see each phase below).
</Reference_Files>

<Language_Policy>
- **Output language MIRRORS the user's input language**: if the user converses in Korean, every narrative
  field, indicator, and rendered table is Korean; if English, English. (`--lang` overrides detection.)
- KOICA structural labels are always kept bilingual in the render (e.g. `요약 (Narrative Summary)`).
- **This SKILL.md and every prompt template are written in English** regardless of output language.
</Language_Policy>

<Steps>

## Phase 0 — Load context
1. Read `rules/koica-rules.md`, `rules/checklist.json`, and `schema/pdm-schema.json` into context.
2. Parse `{{ARGUMENTS}}`: `--use-case <intl-dev|biz-dev|csr-esg>`, `--concept <brief>`, `--inputs <file>`,
   `--lang en|ko`, `--advisory-threshold <0..1>` (default from checklist.json: 0.8), `--audit`, `--out <dir>`.

## Phase 1 — Use-case & mode selection
0. **Determine the use-case FIRST** (before the interaction mode). 변화이론 에이전트 covers several use-cases;
   the underlying results-chain logic is the **same** for all — only the rendered **end-view** and which
   structures are required differ. If `--use-case <x>` is given, use it; otherwise ASK with the
   environment's interactive choice tool (4 options). Set `meta.use_case`.
     - **국제개발 / KOICA PDM (`intl-dev`)** — ODA·KOICA 사업의 PDM 설계. End-view = **PDM 매트릭스** (`pdm.md`).
     - **사업개발(`biz-dev`)** — 소셜벤처·사회공헌·비영리·창업의 임팩트 모델 정리 / 아이디어. End-view =
       **변화이론(ToC) 뷰** (`toc.md`, node diagram). PDM 양식(수원기관 등)은 강제하지 않는다.
     - **CSR / ESG (`csr-esg`)** — 기업 사회공헌/ESG 프로젝트. End-view = **ToC 뷰** (`toc.md`).
     - **투심 / 임팩트 투자심사 (`invest-screen`)** — **아직 준비 중**(meeting backlog). Politely say it is
       planned, and offer one of the other three (or produce a ToC view as a stand-in). Do **not** block.
   **End-view routing (applied in Phase 3):** `intl-dev` → PDM matrix; `biz-dev`/`csr-esg` → ToC view;
   `invest-screen` → planned. The PDM gate/rules below apply in full to `intl-dev`; for `biz-dev`/`csr-esg`
   the same results-chain is built but PDM-form-specific requirements are relaxed (see Phase 3 + koica-rules §4.1, §11).
1. Determine **entry/interaction mode** — **ALWAYS ask the user which of the three approaches to use
   before doing anything else; never pick one unilaterally.** A `--concept`/`--inputs`/`--draft` flag
   counts as the user having already answered (use it directly and skip the question). Otherwise you MUST
   ask using the environment's interactive choice tool (`AskUserQuestion` / `ask_user_input_v0` /
   equivalent — see Guardrails; plain text only if none exists) which of the three:
     - **[A] Guided interview — concept-first** ("아이디어만 있음. 한 번에 하나씩 질문받으며 결과사슬 구성").
     - **[B] Guided interview — inputs-held** ("문서/ToC 초안/부분·기존 PDM 있음. 빈칸만 채움").
     - **[C] Draft-first (표 먼저)** ("질문 1개만 받고 바로 PDM 초안 표를 보고 그 위에서 수정"). *(Runs
       alongside A/B as an A/B-test of interaction style — koica-rules.md §10 #7.)*
2. Determine **gate mode** (see `koica-rules.md` §7):
   - **GATE** (default for Mode A/B): authoring a *new* PDM → Critical failures block; Advisory triggers
     refinement.
   - **AUDIT** (`--audit`, or Mode B when the user says the input is an *already-approved/existing* PDM):
     all checks run **report-only**, nothing blocks.
   - **DRAFT** (Mode C): report-only while the user edits the draft; flips to **GATE** at Finalize
     (Phase 3). Set `meta.gate_mode = "DRAFT"` until then.
3. Detect output language from the user's messages (or `--lang`).
4. Initialize interview state (keep in working memory / scratch; not written to disk until generation):
   ```json
   {
     "use_case": "intl-dev|biz-dev|csr-esg|invest-screen", "mode": "A|B|C", "lang": "ko|en", "gate_mode": "GATE|AUDIT|DRAFT", "advisory_threshold": 0.8,
     "results_chain": { "problem_analysis": null, "goal_analysis": null,
       "impact": null, "outcomes": [], "outputs": [], "activities": [], "inputs": null },
     "assumptions": {}, "interview_rounds": []
   }
   ```

## Phase 2 — Interview (one question at a time)
Follow the KOICA procedure (koica-rules.md §1.3): problem/goal analysis → build the results chain with
assumptions → add indicators. **Ask ONE question per turn** (deep-interview style); after each answer,
update `results_chain` in state. Enforce the per-level rules from `koica-rules.md` §3 AS YOU GO (don't
collect violations to reject later).

- **Mode A (concept-first):** use `prompts/interview-a-concept.md`. Stages: (1) problem analysis →
  (2) goal analysis → (3) impact statement [confirm SDGs + national strategy; **no indicators**] →
  (4) outcome(s) [behavioral change; 1+ allowed] → (5) outputs [3-4, noun-form] → (6) activities [map each to an
  output via `from_activities`; exclude M&E] → (7) inputs [period/budget/recipient resources] →
  (8) assumptions per causal link → (9) indicators for each output & outcome [baseline/target/MoV/source/
  timing/collector/disaggregation; SMART/CREAM; ≥1 gender-disaggregated]. ~12-20 rounds.
- **Mode B (inputs-held):** use `prompts/interview-b-inputs.md`. (1) `Read` the provided file(s) and
  extract whatever results-chain/PDM structure exists. (2) Gap-identify against the schema. (3) Ask ONE
  targeted question per gap. (4) Run assumption/indicator development only for gaps.
- **Mode C (draft-first):** use `prompts/draft-first.md`. Ask **one** scoping question, then **skip
  straight to Phase 3** to generate + render a non-blocking **draft** (gate_mode DRAFT). No multi-turn
  interview — refinement happens on the rendered table via Phase 4, and gating happens at Finalize.

Hard interview rules (mirror `koica-rules.md`):
- Impact carries **no** indicators/MoV `[C01]`.
- Outcome count is not constrained (the single-outcome rule was removed 2026-06-05 — see `koica-rules.md` §10); each outcome's indicators **1-2 (≤3)** `[C03]`; each outcome is a behavioral-change state.
- **3-4** outputs `[C02]`, noun-form, not a restatement of activities `[C06]`.
- Every output must feed the outcome (`from_outputs`) `[C05]`; every activity must feed an output
  (`from_activities`) `[C08]` — even support activities.
- Every output/outcome indicator needs a MoV `[C04]`.
- **Do NOT elicit or invent `baseline`/`target`** — default both to `"추후 확정"` (set later from
  현장답사; koica-rules.md §4.8). Record a value only if the user volunteers one.

## Phase 3 — Generation pipeline
1. **Assemble `pdm.json`** using `prompts/generate-pdm.md`: build the full document from state, assign
   stable IDs (`imp-1`, `oc-1`, `op-1`, `act-1`, `act-1.1`, `ind-op-1.1`, …), wire all `from_*` causal
   references, and write narrative fields in the output language.
2. **Shape-validate + recover (lightweight, pure-Python — no jq, no heavy schema engine at runtime):**
   confirm `pdm.json` is well-formed JSON and has the required shape:
   `Bash: bash rules/validate-critical.sh --shape OUT/pdm.json` (exit 0 = OK; exit 1 = malformed/missing
   keys; exit 2 = invalid JSON). If it fails, **regenerate ONCE** with the error appended to the prompt;
   if it still fails, surface to the user and stop. (`schema/pdm-schema.json` remains the written data
   contract that `generate-pdm.md` follows; full JSON-Schema validation is a build-time check, not a
   runtime dependency.)
3. **Branch on gate mode:**
   - **AUDIT** → skip to step 7 (report-only).
   - **DRAFT** (Mode C) → skip to step 7 (report-only), then render (8-10), then present the non-blocking
     **draft checklist** and offer **Finalize** (Phase 3b). Do not block.
   - **GATE** → steps 4-6.
4. **Deterministic Critical check (C01-C05, C08):**
   `Bash: bash rules/validate-critical.sh OUT/pdm.json`. If exit ≠ 0: show the FAIL lines, return to a
   **targeted** interview to fix exactly those rules, regenerate, and re-run. Loop until it passes.
5. **LLM Critical check (C06 noun-form):** judge each output narrative against the C06 rubric. If any
   fails, return to interview to fix; do not proceed until 100% Critical pass.
6. **Advisory gate (A01-A08):** evaluate each Advisory rule (LLM judgment) per
   `prompts/refine-advisory.md`. Scoring unit = **per-rule-type** (8 types → 80% means ≤1 may fail); for
   per-indicator rules (A01/A02) a type **passes if >50% of indicators satisfy** it. If pass-rate <
   `advisory_threshold`: enter the **refinement loop** — re-run ALL Advisory checks each round (catch
   regressions), **max 3 rounds** (`--max-advisory-rounds`). Exit on: threshold met, max rounds reached,
   or user says "accept as-is". Report the final score + remaining failures.
7. **Report-only check (AUDIT or DRAFT mode):** run ALL Critical + Advisory checks via
   `bash rules/validate-critical.sh --audit OUT/pdm.json` plus the LLM checks, and present every finding
   as a list — block nothing. AUDIT → "deviation list" (already-approved PDMs that predate/deviate from
   the 2017 guideline). DRAFT → "draft gap checklist" (what to confirm/fill before finalizing). For DRAFT,
   skip A05 wherever `target` is `추후 확정` (koica-rules.md §4.8).
8. **Render the end-view per `meta.use_case`** (Phase 1 step 0 routing):
   - `intl-dev` → **`pdm.md`** via `prompts/render-pdm-md.md` (KOICA 4×4: Impact row shows `-` in OVI/MoV;
     Activities row carries Inputs in the OVI column and Pre-conditions in the Assumptions column). The
     ToC node diagram (`prompts/render-toc-md.md` §1) MAY be appended as an optional figure.
   - `biz-dev` / `csr-esg` → **`toc.md`** via `prompts/render-toc-md.md` (Theory-of-Change view + node
     diagram). PDM-form structures (수원기관/투입물) are NOT forced (koica-rules.md §11.1). `pdm.md` MAY also
     be rendered if the user also wants the PDM form (the underlying logic is identical).
9. **Render `monitoring.md`** via `prompts/render-monitoring-md.md` (indicator measurement plan; applies to
   all use-cases).
10. Write the produced files to the out dir.
11. **Display a self-check summary**: Critical (all pass / audit findings) + Advisory (% score), plus any
    nodes still flagged `stale`. For DRAFT, frame it as a **draft checklist** and remind the user they can
    edit any cell (Phase 4) or say **"확정"/"finalize"** to run the full gate (Phase 3b).

## Phase 3b — Finalize (DRAFT → GATE)
Triggered only when a **Mode C / DRAFT** PDM's author says "확정"/"finalize":
1. Set `meta.gate_mode = "GATE"`.
2. Confirm or clear remaining `stale` flags with the user (regenerate any they still want changed).
3. Run the **hard gate**: `bash rules/validate-critical.sh OUT/pdm.json` (NO `--audit` → blocking), then
   the C06 LLM check, then the Advisory refinement loop (steps 4-6 above). Loop until Critical passes.
4. Baseline/target may legitimately remain `추후 확정` at finalize — that does NOT block (A05 is N/A while
   deferred; C04/MoV still enforced). Re-render and show the final self-check summary.

## Phase 4 — Edit propagation + connectivity nudges (post-generation)
The node graph (the `from_*` links) **is** the Theory of Change — what makes it a *theory* is that each
activity connects to an output, each output to an outcome, each outcome to the impact. So whenever the
user edits, adds, retargets, or removes a node, you **MUST proactively state the impact on connected
nodes and nudge the fix BEFORE applying anything** — never silently accept a structural edit. This is the
single most important interaction in the skill.

On any edit to node X:
1. **State the structural impact first (proactively, in plain language, naming specific nodes):**
   a. **Staleness (reverse lookup):** scan all nodes; collect those whose `from_*` arrays contain `X.id`;
      propagate **transitively**. "이 변경은 다음 하위 노드에 영향을 줍니다: […]."
   b. **Breakage check** — run the C05/C08 connectivity logic on the *edited* graph and call out any
      new disconnection BY NAME:
      - **Remove / retarget an activity** → does any output lose **all** its activities? If so that output
        is now produced by nothing. "act-3를 빼면 산출물 op-2를 만드는 활동이 없어집니다(고아 산출물)."
      - **Remove an output** → (i) every outcome that referenced it (`from_outputs`) loses an input;
        (ii) any activity that fed **only** that output becomes an orphan `[C08]`. Name both.
      - **Remove an outcome** → its outputs are no longer referenced by any outcome (`[C05]`,
        disconnected), and the impact loses an outcome. Name the now-dangling outputs.
      - **Add a node** → it is **dangling** until wired: a new activity must feed an output
        (`from_activities`), a new output must feed an outcome (`from_outputs`). Flag it as not-yet-connected.
2. **Nudge the concrete fix** (offer the choices; never auto-delete a connected node):
   "→ op-2도 함께 빼거나, 다른 활동(act-4 등)에 연결하시겠어요?" Let the user pick.
3. Set `stale: true` on every dependent (indicators inherit their parent's staleness).
4. Regenerate ONLY the nodes the user consents to; set their `stale: false`. Declined nodes stay
   `stale: true` and are listed in the self-check report.
5. Re-run the Critical (deterministic C05/C08/C06) + Advisory checks on modified nodes; re-render.

> **Worked example.** User edits `act-1`. Reverse-lookup finds `op-1` (its `from_activities` contains
> `"act-1"`) → `op-1` stale → `oc-1` (whose `from_outputs` contains `"op-1"`) stale transitively. If the
> edit *removed* `act-1` and `op-1` had no other activity, you FIRST say "op-1을 만드는 활동이 없어집니다"
> and nudge before applying. User regenerates `op-1` only → `op-1` cleared; `oc-1` stays stale and is listed.

> **The same connectivity nudges apply DURING the interview/draft, not only after generation.** The moment
> a proposed activity has no output, a proposed output feeds no outcome, or a node would be orphaned, say
> so and nudge immediately — don't wait for the final gate.
</Steps>

<Guardrails>
- ALWAYS `Read` a file before editing it; use absolute or out-dir-relative paths.
- The deterministic validator is the hard gate for structural rules — never finalize a GATE-mode PDM that
  fails `validate-critical.sh`.
- Do NOT auto-overwrite downstream nodes on an edit; regeneration is opt-in.
- Do NOT loosen Critical rules to make a real/approved PDM pass — use AUDIT mode to report deviations.
- Keep prompts internal-English; keep output in the user's language.
- One interview question per turn.
- **Connectivity is proactive, never silent.** Treat the `from_*` graph as the product's core. On any
  structural edit/add/remove, state the impact on connected nodes and nudge the fix BEFORE applying
  (Phase 4). You can compute the breakage deterministically: `bash rules/validate-critical.sh --json
  OUT/pdm.json` (C05 = disconnected outputs, C08 = orphan activities) gives the exact lists to nudge with.
- **Interactive questions — use the environment's choice tool, whatever its name.** A tab/click
  single-select question tool exists in every supported environment, but under **different names**:
  **`AskUserQuestion`** in Claude Code, **`ask_user_input_v0`** in the Claude web/desktop apps (other
  surfaces may expose yet another name with the same role). For any bounded choice (e.g. the Phase 1 mode
  pick, or 2-4 concrete options), you **MUST** use whichever such tool is actually available to you —
  check your real tool list, don't assume it's missing because the name differs. Fall back to a plain-text
  question **only** after verifying that no interactive choice tool exists; never default to plain text out
  of convenience, and never skip the question.
- **Files:** all file ops run in whatever sandbox/filesystem is available; in the Claude apps the three
  output files are written to the sandbox for the user to download.
</Guardrails>

<Self_Check_Reference>
Critical (hard gate in GATE mode): C01 impact-no-indicators · C02 outputs 3-4 · C03 per-outcome indicators
1-3 · C04 every indicator has MoV · C05 output→outcome link · C06 output noun-form (LLM) · C08 no orphan
activities. (C07 single-outcome was removed 2026-06-05 — see `koica-rules.md` §10.) Advisory (≥80% per-rule-type): A01 SMART · A02 CREAM · A03 gender
disaggregation · A04 proxy justified · A05 target realistic · A06 measurable at end-eval · A07 output ≠
activity restatement · A08 outcome = behavioral change. **Baseline/target are deferred (`추후 확정`) by
default — A05 is N/A while a target is deferred (koica-rules.md §4.8).** Full definitions + guideline
citations in `rules/checklist.json` and `rules/koica-rules.md`.
</Self_Check_Reference>
