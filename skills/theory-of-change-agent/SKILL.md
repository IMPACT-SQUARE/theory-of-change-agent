---
name: theory-of-change-agent
description: |
  변화이론 에이전트 (Theory of Change Agent) — KOICA PDM (Project Design Matrix) 생성 스킬.
  Interviews the user following Theory-of-Change methodology, then produces a PDM matrix +
  monitoring matrix grounded in the KOICA PDM guideline. ALWAYS asks first: the purpose (use-case),
  then the situation (아이디어만 있음 / 문서 있음) and the pace (차근차근 인터뷰 / 결과물 먼저).
  Output language mirrors the user's input language.
  Use when the user mentions: "변화이론 에이전트", "theory of change agent", "PDM",
  "project design matrix", "KOICA", "theory of change", "변화이론", "results chain", "로직 모델",
  "logframe", "logical framework", "impact harness", "임팩트 하네스" (legacy name), or wants to
  draft/audit a development-cooperation results matrix.
argument-hint: "[--use-case intl-dev|biz-dev|csr-esg|nonprofit] [--concept <brief> | --inputs <file> | --draft] [--lang en|ko] [--advisory-threshold 0.8] [--audit]"
allowed-tools: Bash, Read, Write, Edit, AskUserQuestion
---

# 변화이론 에이전트 (Theory of Change Agent) — KOICA PDM 생성

<Purpose>
**변화이론 에이전트 (Theory of Change Agent)** turns a vague project idea (or a partial draft) into a
guideline-aligned results chain through a one-question-at-a-time interview, then renders it. It serves
several **use-cases** that share one underlying results-chain engine and differ only in the rendered
end-view (Phase 1 step 0): **국제개발협력(PDM)** renders a **KOICA-guideline-compliant PDM matrix** (the most
mature path); **임팩트 스타트업(신규사업개발)**, **사회공헌(CSR, ESG)**, and **비영리** render a
**Theory-of-Change view** (node diagram); **임팩트 투자사(투심)** is planned. The KOICA PDM path encodes the writing rules
(`rules/koica-rules.md`) and gates on a deterministic + LLM-judged self-check (`rules/checklist.json`,
`rules/validate-critical.sh`), the same checklist that scores the benchmark. **Always ask the use-case
first, then the interaction mode** (Phase 1); never pick either unilaterally.
</Purpose>

<Output_Contract>
The skill writes to the working directory (default `./out/`, override with `--out`). **The human-readable
primary view sits at the top of `out/`; the source JSON and the monitoring detail live in `out/details/`**
— so opening `out/` lands on the main view, not raw JSON:
```
out/
├── pdm.md          # PRIMARY end-view for intl-dev (KOICA 4×4). For ToC-view use-cases (biz-dev/csr-esg/nonprofit) this is toc.md instead.
├── budget.md       # OPTIONAL (intl-dev, on request after gate pass): 사업 예산서 — Phase 3 step 11
└── details/
    ├── toc.json    # single source of truth (ID-linked results-chain DAG; every view renders from it)
    └── monitoring.md   # monitoring matrix (indicator def / baseline / target / source / timing / …)
```
- **Primary end-view at `out/` root** (written LAST): `pdm.md` for `intl-dev`, `toc.md` for
  `biz-dev`/`csr-esg`/`nonprofit`. A non-primary view (e.g. `toc.md` on an intl-dev run) also goes in `out/details/`.
- **`out/details/toc.json`** conforms to `schema/pdm-schema.json`; all views are RENDERED from it.
- Create `out/details/` as needed. Which files are written depends on `meta.use_case` (Phase 3 steps 8-9).

Out of scope (do NOT produce): the annual performance-check sheet, direct `.xlsx`, any web UI.
</Output_Contract>

<Reference_Files>
Load these (they live alongside this SKILL.md) and treat them as authoritative:
- `rules/koica-rules.md` — the KOICA PDM writing rules (with guideline page citations).
- `rules/value-rules.md` — social-value quick-rules (사회문제 ①②③ / 사회적 가치 = 해결 크기, 중립0 / 지표
  실행력·설명력), grounded in 변화이론·로직모델. Used to define & correct the social problem and outcome.
- `rules/value-methodology.md` — the full organized decomposition behind those rules (concept chain +
  four principles + §I/§II/§III detail). Read for depth when defining/correcting.
- `rules/checklist.json` — Critical (C01-C08) + Advisory (A01-A08) self-check definitions + thresholds.
- `rules/validate-critical.sh` — deterministic validator for the structural Critical rules.
- `rules/budget-rollup.py` — deterministic budget rollup/validation (B01-B06, koica-rules.md §12); the
  LLM never does budget arithmetic.
- `rules/validate-render.py` — deterministic RENDER fidelity gate (R01-R11) over the emitted md files
  (OVI name-only, no timing in MoV, level header, no stray `class`, text fallback, no-KOICA in ToC, …).
- `rules/hwp-extract.py` — pure-stdlib `.hwp`/`.hwpx` → text extractor for mode-B inputs (no npm needed;
  routing in `prompts/interview-b-inputs.md` step 1; exit 3 = encrypted/배포용 → ask for a PDF).
- `schema/pdm-schema.json` — JSON Schema for `toc.json`.
- `schema/pdm-example.json` — a complete, guideline-compliant reference instance (Nicaragua).
- `prompts/*.md` — prompt templates for each phase (see each phase below).
</Reference_Files>

<Language_Policy>
- **Set the output language FIRST — before asking anything — and LOCK it for the whole session.** Priority:
  `--lang` > a clear full-sentence in the user's first message > **ASK**. If the message is a bare skill
  call, a single keyword, mixed, or there is ANY doubt, **ask a neutral bilingual question (`한국어` /
  `English`) and never default to Korean.** Then lock `meta.lang`.
- **Mirror that language CONSISTENTLY in EVERY user-facing surface**: the use-case / situation / pace
  questions and their option labels, the progress lines, the connectivity nudges, the social-problem
  reframes, the summaries, AND every narrative field / indicator / rendered table. Do **not** drift — an
  English session stays English end-to-end; a Korean session stays Korean. *(This was the bug: detecting
  language late and copying the Korean example strings verbatim made English sessions go Korean, and vice
  versa.)*
- **The Korean strings throughout SKILL.md and the prompts are DEFAULT EXAMPLES for `ko`.** When
  `meta.lang = en`, translate them — the questions, option labels, the `[질문 N · …]` progress line, the
  `최종 결과: …` closing line, the `그건 사회문제라기보다…` reframes, etc. They are illustrations, not literals
  to print regardless of language.
- KOICA structural labels stay **bilingual** in the render (e.g. `요약 (Narrative Summary)`).
- **This SKILL.md and every prompt template are written in English** regardless of output language.
</Language_Policy>

<Steps>

> **Path convention:** every `rules/...` and `prompts/...` reference in this skill is relative to the
> **SKILL ROOT** (the directory containing this SKILL.md). In app sandboxes (Claude desktop / claude.ai /
> Antigravity) the working directory is usually the OUTPUT workspace, not the skill root — prefix commands
> with the skill root (locate it once if needed). A "No such file or directory" on a `rules/` script means
> the path is wrong, **not** that a feature is unavailable.

## Phase 0 — Load context
1. Read `rules/koica-rules.md`, `rules/checklist.json`, and `schema/pdm-schema.json` into context.
2. Parse `{{ARGUMENTS}}`: `--use-case <intl-dev|biz-dev|csr-esg|nonprofit>`, `--concept <brief>`, `--inputs <file>`,
   `--lang en|ko`, `--advisory-threshold <0..1>` (default from checklist.json: 0.8), `--audit`, `--out <dir>`.

## Phase 1 — Language, use-case & mode selection
00. **Set the output language FIRST — before any other question, and NEVER default to Korean silently.**
    - If `--lang` is given, use it.
    - Else if the user's first message is clearly a full request in one language (an English or Korean
      sentence), use that language.
    - **Otherwise — a bare skill call (e.g. just invoking the skill), a single keyword, mixed, or ANY
      doubt — ASK**, using the interactive choice tool, with a **bilingual** (neutral) question:
      question `Language / 언어`, options `한국어` and `English`. Do not guess.
    Set `meta.lang`. From here, **every** user-facing string — all the questions below, their option
    labels, progress lines, nudges, narratives — is in `meta.lang`; the Korean text in these prompts is the
    `ko` default, translate it when `meta.lang = en`.
0. **Determine the use-case FIRST** (before the interaction mode). 변화이론 에이전트 covers several use-cases;
   the underlying results-chain logic is the **same** for all — only the rendered **end-view** and which
   structures are required differ. If `--use-case <x>` is given, use it; otherwise ASK with the
   environment's interactive choice tool (**4 options** — confirmed labels 2026-07-09; do NOT put "KOICA"
   in a label, PDM is the deliverable name). Set `meta.use_case`.
     - **국제개발협력 / PDM (`intl-dev`)** — 국제개발(ODA) 사업의 PDM 설계. End-view = **PDM 매트릭스** (`pdm.md`).
       사업(프로젝트) 단위.
     - **임팩트 스타트업 / 신규사업개발 (`biz-dev`)** — 소셜벤처·임팩트 스타트업의 임팩트 모델 정리 / 아이디어.
       End-view = **변화이론(ToC) 뷰** (`toc.md`, node diagram). PDM 양식(수원기관 등)은 강제하지 않는다.
       조직 단위 입력(사업계획서에 다수 프로젝트) 가능 → step 0b.
     - **사회공헌 / CSR, ESG (`csr-esg`)** — 기업 사회공헌·ESG 프로젝트. End-view = **ToC 뷰** (`toc.md`). 사업 단위.
     - **비영리 (`nonprofit`)** — 재단·NGO의 프로그램/보고(기부금 리포트 등). End-view = **ToC 뷰** (`toc.md`).
       조직 단위 입력(특히 **연차보고서** — 당해년도 전체 사업 포함) 가능 → step 0b.
     - *(임팩트 투자사 (`invest-screen`, 투심) is **backlog** — do NOT offer it as a choice. If the user
       explicitly asks for 투심, say it's planned and offer the ToC view as a stand-in; koica-rules §11.3.)*
   **End-view routing (applied in Phase 3):** `intl-dev` → PDM matrix; **ToC-view use-cases**
   (`biz-dev`/`csr-esg`/`nonprofit`) → ToC view; `invest-screen` → planned. The PDM gate/rules below apply
   in full to `intl-dev`; for ToC-view use-cases the same results-chain is built but PDM-form-specific
   requirements are relaxed (see Phase 3 + koica-rules §4.1, §11).
0b. **Unit branching — 다수 프로젝트 감지 (org-unit inputs).** 변화이론은 **프로젝트 단위**로 만들어진다.
   `intl-dev`/`csr-esg` are project-unit by nature — set `meta.unit = "project"` and skip this step.
   For **`biz-dev`/`nonprofit`**, when the user provides documents (Phase 1 Q1 = `inputs`), READ them first
   and judge whether they describe **one project or multiple projects** (예: 조직 사업계획서, 비영리 연차보고서
   — 당해년도 전체 사업이 들어 있음).
   - **Single project detected** → `meta.unit = "project"`, proceed normally.
   - **다수 프로젝트 detected** → `meta.unit = "org"`, record `meta.org_context` (org_name, mission if stated,
     projects[] with one-line summaries), then ASK the user with the interactive choice tool — **exactly 2
     options** (never offer a "여러 프로젝트를 하나씩 전부 돌리기" option):
       1. **전체 프로젝트** — 조직 전체 구조도: 미션 → 프로젝트들이 어떻게 연결되는지 한눈에. Full ToC를 프로젝트마다
          만들지 않는다. Render a compact **조직 구조도** (mission at the root, each project as a node with its
          핵심 성과 한 줄; Mermaid + text fallback, same style rules as render-toc §1/1b) and, below it, offer:
          "특정 프로젝트 하나를 골라 full 변화이론으로 들어갈 수도 있어요."
       2. **특정 프로젝트** — 감지된 프로젝트 목록에서 하나를 고르게 한 뒤(`meta.org_context.selected_project`),
          그 프로젝트를 대상으로 normal single-project flow를 진행한다 (project_name = 선택 프로젝트; org/mission
          은 org_context에 보존 — the ToC view may note the mission linkage).
   Wording rule: say **"프로젝트"**, not "프로그램" (다수 프로젝트, 전체 프로젝트, 특정 프로젝트).
1. Determine the **approach via TWO friendly, user-facing questions** — ALWAYS ask both before doing
   anything else; never pick unilaterally. Use the environment's interactive choice tool (plain text only
   if none exists). A `--concept`/`--inputs` flag pre-answers Q1 and `--draft` pre-answers Q2 (skip what is
   preset). Phrase the options in the user's language and keep them plain (no jargon like "concept-first"):
   **Q1 — 지금 어떤 상태인가요?** (`input_source`)
     - **아이디어만 있어요** (`concept`) — 사업 구상은 있는데 정리된 자료는 아직.
     - **사업계획서·초안·기존 PDM 같은 문서가 있어요** (`inputs`) — 그 파일을 읽어 활용. (이미 *승인된* PDM을
       점검만 하려는 거면 감사 모드로: AUDIT.)
   **Q2 — 어떻게 진행할까요?** (`interaction`)
   The use-case is already known (step 0), so **name the concrete deliverable in parentheses** in the
   draft option — `{결과물}` = **PDM 표** for `intl-dev`, **변화이론 도식** for `biz-dev`/`csr-esg`/
   `nonprofit` (en: *PDM matrix* / *Theory-of-Change diagram*):
     - **질문에 하나씩 답하며 차근차근 만들래요** (`interview`) — 가장 꼼꼼. 대략 아이디어 10–20분 / 문서 5–10분.
     - **결과물({결과물})을 먼저 만들고 그 위에서 고칠래요** (`draft`) — 가장 빠름, 대략 2–5분.
       e.g. intl-dev → "결과물(PDM 표)을 먼저 만들고 그 위에서 고칠래요" / nonprofit → "결과물(변화이론
       도식)을 먼저 만들고 그 위에서 고칠래요".
   **Resolve to the internal flow** and set `meta.input_source`, `meta.interaction`, and `meta.mode`:
     - concept + interview → **Mode A** (`prompts/interview-a-concept.md`); `mode:"A"`.
     - inputs  + interview → **Mode B** (`prompts/interview-b-inputs.md`); `mode:"B"`.
     - concept + draft     → **Mode C** (`prompts/draft-first.md`); `mode:"C"`.
     - inputs  + draft     → **Mode B → draft:** run `interview-b-inputs.md` steps 1-2 to read/extract the
       file(s), then go straight to Phase 3 to generate + render a **draft** and edit on the table
       (Phase 4), finalize → GATE. Record `mode:"B"` with `gate_mode:"DRAFT"`.
2. Determine **gate mode** (see `koica-rules.md` §7):
   - **GATE** (default when `interaction = interview`): authoring a *new* PDM → Critical failures block;
     Advisory triggers refinement.
   - **AUDIT** (`--audit`, or when the user says the input is an *already-approved/existing* PDM):
     all checks run **report-only**, nothing blocks.
   - **DRAFT** (when `interaction = draft`, including inputs+draft): report-only while the user edits the
     draft; flips to **GATE** at Finalize (Phase 3b). Set `meta.gate_mode = "DRAFT"` until then.
3. (Output language was already locked in step 00 — keep using `meta.lang` for everything from here on.)
4. Initialize interview state (keep in working memory / scratch; not written to disk until generation):
   ```json
   {
     "use_case": "intl-dev|biz-dev|csr-esg|nonprofit|invest-screen", "input_source": "concept|inputs", "interaction": "interview|draft",
     "mode": "A|B|C", "lang": "ko|en", "gate_mode": "GATE|AUDIT|DRAFT", "advisory_threshold": 0.8,
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

- **Mode A (concept-first):** use `prompts/interview-a-concept.md`. Stages: (1) **social-problem
  definition + correction** (`prompts/social-problem.md` + `rules/value-rules.md` §V1 — 구조적/다수/고통;
  reframe individual/market/solution-in-disguise) → (2) goal analysis → (3) impact statement [confirm SDGs
  + national strategy; **no indicators**] →
  (4) outcome(s) [사회적 가치 = 사회문제 해결 크기, neutral-0 (value-rules §V2); behavioral change; 1+ allowed] →
  (5) outputs [3-4, noun-form] → (6) activities [map each to an
  output via `from_activities`; exclude M&E] → (7) inputs [period/budget/recipient resources] →
  (8) assumptions per causal link → (9) indicators for each output & outcome [baseline/target/MoV/source/
  timing/collector/disaggregation; SMART/CREAM; ≥1 gender-disaggregated]. ~12-20 rounds.
- **Mode B (inputs-held):** use `prompts/interview-b-inputs.md`. (1) `Read` the provided file(s) and
  extract whatever results-chain/PDM structure exists. (2) Gap-identify against the schema. (3) Ask ONE
  targeted question per gap. (4) Run assumption/indicator development only for gaps.
- **Mode C (concept + draft):** use `prompts/draft-first.md`. Ask **one** scoping question, then **skip
  straight to Phase 3** to generate + render a non-blocking **draft** (gate_mode DRAFT). No multi-turn
  interview — refinement happens on the rendered table via Phase 4, and gating happens at Finalize.
- **Mode B → draft (inputs + draft):** run `interview-b-inputs.md` steps 1-2 (read + extract the file(s)),
  then **skip straight to Phase 3** to generate + render a **draft** from the extracted structure
  (gate_mode DRAFT) and edit on the table (Phase 4); finalize → GATE. (No per-gap interview up front — the
  user fixes things on the rendered draft instead.)

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
1. **Assemble `toc.json`** using `prompts/generate-pdm.md`: build the full document from state, assign
   stable IDs (`imp-1`, `oc-1`, `op-1`, `act-1`, `act-1.1`, `ind-op-1.1`, …), wire all `from_*` causal
   references, and write narrative fields in the output language.
2. **Shape-validate + recover (lightweight, pure-Python — no jq, no heavy schema engine at runtime):**
   confirm `toc.json` is well-formed JSON and has the required shape:
   `Bash: bash rules/validate-critical.sh --shape OUT/details/toc.json` (exit 0 = OK; exit 1 = malformed/missing
   keys; exit 2 = invalid JSON). If it fails, **regenerate ONCE** with the error appended to the prompt;
   if it still fails, surface to the user and stop. (`schema/pdm-schema.json` remains the written data
   contract that `generate-pdm.md` follows; full JSON-Schema validation is a build-time check, not a
   runtime dependency.)
3. **Branch on gate mode:**
   - **AUDIT** → skip to step 7 (report-only).
   - **DRAFT** (Mode C) → skip to step 7 (report-only), then render (8-9), then present the non-blocking
     **draft checklist** and offer **Finalize** (Phase 3b). Do not block.
   - **GATE** → steps 4-6.
4. **Deterministic Critical check (C01-C05, C08):**
   `Bash: bash rules/validate-critical.sh OUT/details/toc.json`. If exit ≠ 0: show the FAIL lines, return to a
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
   `bash rules/validate-critical.sh --audit OUT/details/toc.json` plus the LLM checks, and present every finding
   as a list — block nothing. AUDIT → "deviation list" (already-approved PDMs that predate/deviate from
   the 2017 guideline). DRAFT → "draft gap checklist" (what to confirm/fill before finalizing). For DRAFT,
   skip A05 wherever `target` is `추후 확정` (koica-rules.md §4.8).
7b. **Outcome verification — ALL use-cases, not only when toc.md is rendered** (advisory, non-blocking):
   run `prompts/outcome-verify.md` for **each outcome** (논리 검증: change-of-state / 원인 회복 / 지표=변화분)
   and `prompts/iris-match.md` for **each outcome indicator** (IRIS+ 근접 지표 — outcome indicators ONLY;
   `python3 <SKILL_ROOT>/rules/iris-search.py --json --top 6 "…"`, shortlist에서만 제시; "매칭 준비 중" is
   ONLY for a genuine exit 3 — command-not-found means wrong path, find the script and retry; never
   invent a code). Include the per-outcome `✅ 부합`/`⚠️ 교정 필요` verdicts + IRIS+ suggestions in the
   **step 10 self-check summary** (chat). When `toc.md` is rendered, its §4 embeds the same results — do
   not run them twice; reuse.
8. **Render + write `out/details/monitoring.md`** via `prompts/render-monitoring-md.md` (indicator
   measurement plan; all use-cases).
9. **Render + write the PRIMARY end-view LAST** (Phase 1 step 0 routing):
   - `intl-dev` → **`pdm.md`** via `prompts/render-pdm-md.md` (KOICA 4×4: Impact row shows `-` in OVI/MoV;
     Activities row carries Inputs in the OVI column and Pre-conditions in the Assumptions column). The
     ToC node diagram (`prompts/render-toc-md.md` §1) MAY be appended as an optional figure.
   - ToC-view use-cases (`biz-dev`/`csr-esg`/`nonprofit`) → **`toc.md`** via `prompts/render-toc-md.md` (Theory-of-Change view + node
     diagram). PDM-form structures (수원기관/투입물) are NOT forced (koica-rules.md §11.1). For `intl-dev`
     you MAY also write `toc.md`, but write `pdm.md` **last**.
   > **Write order matters — end on the human-readable view.** Sequence: `out/details/toc.json` (written
   > in step 1, the source of truth) → `out/details/monitoring.md` → the primary view (`out/pdm.md` or
   > `out/toc.md`) **last**. Desktop/IDE apps (Claude desktop, Antigravity) surface the **last-written /
   > last-touched file**, so keeping the JSON in `out/details/` AND writing the primary view last lands the
   > user on the readable view, not the raw JSON. Do **not** re-save `out/details/toc.json` after renders.
9b. **Render fidelity gate (deterministic).** After the views are written, run
   `python3 <SKILL_ROOT>/rules/validate-render.py OUT` — it checks the RENDERED files against the
   R01-R11 rules (indicator definitions must not leak into pdm.md OVI cells, no 측정 시기 in MoV, no
   `추후 확정` in the matrix, diagram has the level header/black text/text fallback/no `class` lines,
   no KOICA mention in ToC outputs, monitoring columns match the use-case, DRAFT placeholder rule).
   **Any `fail` = a render bug you introduced — fix the md and re-run until exit 0.** This is the same
   class of check as the C-gate, but on your OUTPUT instead of the data. Re-run it after EVERY re-render
   (Phase 3b finalize, Phase 4 edits).
10. **Display a self-check summary** (Critical: all pass / audit findings · Advisory: % score · any nodes
    still `stale`) and then **present the primary view as the final artifact** — state its path as the
    closing line (e.g. "최종 결과: `out/pdm.md`" or "`out/toc.md`") so the user lands on it. In app
    sandboxes (Claude desktop / claude.ai) the files arrive as **download links in the chat** — say so.
    If the user asks for a **PDF or 다운로드**, offer to render a print-ready **`out/pdm.html`**
    (self-contained, inline CSS, the same tables) and tell them: 브라우저에서 열어 인쇄 → "PDF로 저장".
    Never claim a hosted link exists — there is no server (web front-end is a separate 8월 workstream). **For DRAFT
    (both Mode C and inputs+draft), do NOT stop at a checklist — guide the next action** exactly as
    `prompts/draft-first.md` Step 4: a one-line summary, the top 1-3 things to firm up (use `--connectivity`
    for broken links; everything is `stale`/`추후 확정`), then **ask ONE specific leading question to start
    refining** (usually the outcome), and state the options (say what to change / let me walk the weak spots
    / say "확정" to run the gate). Never just dump the table and go silent.
11. **예산 offer (intl-dev only, after the gate has passed — not for DRAFT).** Ask once:
    "PDM에 맞춘 **사업 예산서**도 잡아드릴까요? (활동별 세목 · 산출근거 · 분담 · 일반관리비)". If yes, run
    `prompts/budget-build.md` → it writes the `budget` block into `out/details/toc.json`, verifies with
    `python3 rules/budget-rollup.py` (deterministic — the LLM never sums), and renders **`out/budget.md`**
    via `prompts/render-budget-md.md`. If no, move on — the offer is never repeated unprompted.

## Phase 3b — Finalize (DRAFT → GATE)
Triggered only when a **DRAFT** PDM's author (Mode C = concept+draft, or inputs+draft) says "확정"/"finalize":
1. Set `meta.gate_mode = "GATE"`.
2. Confirm or clear remaining `stale` flags with the user (regenerate any they still want changed).
3. Run the **hard gate**: `bash rules/validate-critical.sh OUT/details/toc.json` (NO `--audit` → blocking), then
   the C06 LLM check, then the Advisory refinement loop (steps 4-6 above). Loop until Critical passes.
4. Baseline/target may legitimately remain `추후 확정` at finalize — that does NOT block (A05 is N/A while
   deferred; C04/MoV still enforced).
5. **Re-render ALL views from the finalized `toc.json`, per Phase 3 steps 8-9** — do not skip this. The
   finalize (clearing `stale`, the Advisory refinement) changed nodes, so the rendered views are stale:
   rewrite `out/details/monitoring.md`, then the **primary view LAST** — **`out/toc.md`** for
   `biz-dev`/`csr-esg`/`nonprofit` (the 변화이론 도식 MUST be regenerated so its nodes/edges match the finalized chain)
   or **`out/pdm.md`** for `intl-dev`. Because `gate_mode` is now `GATE`, `render-toc-md.md` emits the
   **actual Mermaid diagram** in place of the draft "확정 후 출력" placeholder — verify the diagram is
   present. Then show the final self-check summary + the primary view path.

## Phase 4 — Edit propagation + connectivity nudges (post-generation)
The node graph (the `from_*` links) **is** the Theory of Change — what makes it a *theory* is that each
activity connects to an output, each output to an outcome, each outcome to the impact. So whenever the
user edits, adds, retargets, or removes a node, you **MUST proactively state the impact on connected
nodes and nudge the fix BEFORE applying anything** — never silently accept a structural edit. This is the
single most important interaction in the skill.

**If a `budget` block exists**, every structural edit must also re-run
`python3 rules/budget-rollup.py OUT/details/toc.json`: a removed/renumbered activity turns its budget
lines into **B04 고아 예산 라인** errors (ask where the cost moves), and a newly added activity surfaces
in **B05 예산 미배정** (nudge: "새 활동에 예산을 배정할까요?"). See prompts/budget-build.md §connectivity.

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
5. Re-run the Critical (deterministic C05/C08/C06) + Advisory checks on modified nodes, then **re-render
   ALL views from the updated `toc.json` per Phase 3 steps 8-9** (monitoring.md, then the primary view
   LAST — `toc.md` for ToC-view use-cases so the 변화이론 도식 reflects the edit, or `pdm.md` for
   `intl-dev`). An edit that isn't re-rendered leaves a stale diagram.

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
- Keep prompts internal-English; keep **all user-facing output in `meta.lang`**, locked at the first
  message (Phase 1 step 00) and never drifting mid-session. The Korean strings in these prompts are `ko`
  examples — translate them when `meta.lang = en`. Match the user's language; do not switch on them.
- One interview question per turn.
- **Connectivity is proactive, never silent.** Treat the `from_*` graph as the product's core. On any
  structural edit/add/remove, state the impact on connected nodes and nudge the fix BEFORE applying
  (Phase 4). You can compute the breakage deterministically: `bash rules/validate-critical.sh --json
  OUT/details/toc.json` (C05 = disconnected outputs, C08 = orphan activities) gives the exact lists to nudge with.
- **Interactive questions — use the environment's choice tool, whatever its name.** A tab/click
  single-select question tool exists in most supported environments, but under **different names**:
  **`AskUserQuestion`** in Claude Code, **`ask_user_input_v0`** in the Claude web/desktop apps,
  **`ask_user`** in Gemini CLI / Antigravity (type "choice" = multiple-choice) — other surfaces may
  expose yet another name with the same role. For any bounded choice (e.g. the Phase 1 mode pick, or 2-4
  concrete options), you **MUST** use whichever such tool is actually available to you — **check your
  real tool list first**; don't assume it's missing because the name differs (2026-07-21 pilot: Gemini in
  Antigravity fell back to prose because its `ask_user` wasn't named here). Fall back to plain text
  **only** after verifying no such tool exists — and then format the fallback as a **numbered menu** the
  user can answer with one keystroke, e.g.:
  `1️⃣ 직접 수정할 내용을 알려주기 · 2️⃣ 약한 고리부터 하나씩 짚기 · 3️⃣ "확정"으로 게이트 진행 — 번호로
  답해 주세요.` Never bury the options in a paragraph, and never skip the question.
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
