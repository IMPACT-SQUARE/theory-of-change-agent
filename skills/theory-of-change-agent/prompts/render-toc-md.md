# Prompt: Render toc.md (Theory-of-Change view + node diagram)

ROLE: Render `OUT/details/toc.json` into `OUT/toc.md` — the **Theory-of-Change (변화이론) view** used for the
ToC-view use-cases (`biz-dev`/`csr-esg`/`nonprofit`; and optionally alongside the PDM for `intl-dev`). Same underlying data
as the PDM; this view emphasizes the **causal flow and node connections** rather than the KOICA 4×4 form.
Render only what is in the JSON. Keep structural labels bilingual; write content in `meta.lang`.
**No KOICA mentions in the rendered ToC output** (임팩톨로지 feedback 2026-07-21): this view serves non-ODA
use-cases — never emit "KOICA 가이드라인" / rule ids / internal source names in `toc.md`; ground any advice
in 변화이론·로직모델 wording. (KOICA references belong to the intl-dev PDM/monitoring surfaces only.)

## Header block
```
# 변화이론 (Theory of Change) — {meta.project_name}
```
If `meta.use_case` is present, note it (e.g. `임팩트 스타트업/신규사업개발 (biz-dev)` / `사회공헌 (csr-esg)` / `비영리 (nonprofit)`).

## 1. Node diagram (Mermaid) — the heart of the view
**Draft gate (important):** if `meta.gate_mode = "DRAFT"` (a draft-first draft not yet finalized), do
**NOT** emit the Mermaid diagram yet — the chain is still being shaped. Instead show a short, friendly
placeholder in `meta.lang`, e.g. ko: `> 📊 변화이론 도식은 **확정(finalize) 후** 그려집니다. 내용을 다듬고
"확정"이라고 하면 이 자리에 도식이 나타납니다.` / en: `> 📊 The Theory-of-Change diagram is drawn **after
you finalize**. Refine the content and say "확정"/finalize to generate it here.` Emit the **full diagram
only when finalized** (`meta.gate_mode` is `GATE`, or `AUDIT` for an existing PDM).

When you DO draw it, emit a Mermaid `flowchart LR` built from the `from_*` causal links. What makes it a
*theory* is the connections: **사회문제 → 활동 → 산출물 → 성과(+지표) → 영향**. Show every edge; keep the
nodes prominent.

**No LEVEL boxes.** Do **NOT** wrap whole levels in `subgraph` containers — the big boxes hide the nodes
(임팩트스퀘어 feedback 2026-07-01). The `flowchart LR` flow already gives the left→right level ordering; use a
per-node `classDef` color for the level cue. *(A small per-**outcome** group IS allowed — see 성과지표 below;
the ban is on level-wide containers only.)*

**Level header row (임팩톨로지 feedback 2026-07-21):** the FIRST line of the graph is a chain of level-label
nodes (class `lvl`) so the 대목록 reads across the top: `사회문제 → 활동 → 산출물 → 성과(+지표) → 영향`
(insert `투입물` after 사회문제 only when the 투입물 node is shown, i.e. intl-dev). Labels bilingual
(e.g. `활동 (Activities)`).

**Readability (임팩톨로지 feedback 2026-07-21 — small/invisible text in Antigravity dark theme):**
- Start the block with an init directive that raises the font size:
  `%%{init: {"themeVariables": {"fontSize": "16px"}}}%%`
- **Every `classDef` includes `color:#000`** (black text). The fills are light, so without an explicit
  color, dark-theme apps (Antigravity) render white-on-light = unreadable.
- Zoom / image-export buttons are NOT possible inside a markdown file — do NOT emit any external-tool
  workaround tip (user decision 2026-07-21: interactive zoom/download is deferred to the web version).

Node id: each `toc.json` id → Mermaid-safe (replace non-alphanumerics with `_`: `op-1`→`op_1`,
`ind-oc-1.1`→`ind_oc_1_1`). Label = the narrative (display-number prefix optional). Escape `"` in labels.
**Class assignment: inline `:::className` ONLY.** Never emit separate `class node1,node2 className`
statement lines — some renderers (Antigravity/Gemini markdown preview) mis-parse them into a stray
bottom node labeled "CLASS" (임팩톨로지 bug report 2026-07-21). `classDef` definition lines are fine.

**Nodes & classes:**
- **사회문제** — one node from `results_chain.problem_analysis` (현상 → 원인, value-rules §V1); class `problem`.
  It anchors the chain (its 해결 크기 = the Outcome, §V2).
- **활동 / 산출물 / 성과 / 영향** — one node each (activities include sub-activities); classes
  `act` / `out` / `outcome` / `impact`.
- **성과지표 (outcome indicators)** — each outcome and its indicators go inside a **small per-outcome
  `subgraph` with `direction TB`**, outcome node first, indicator nodes (class `ind`) linked `-.->` below
  it. This puts the 지표 **UNDER its outcome**, not in the impact column (임팩톨로지 feedback 2026-07-21 —
  previously the `-.->` link alone ranked indicators at the same depth as 영향). Give the subgraph an
  empty title (`[" "]`) and a subtle style. Indicator label = name with its `j-m` number; **NO
  baseline/target numbers**. (Output/activity indicators stay in §3 + monitoring; add only on request.)
- **투입물(Inputs)** — a node only when `meta.use_case = intl-dev` and `inputs` is present (§11.1); class
  `input`. Omit for `biz-dev`/`csr-esg`/`nonprofit`.

**Edges** (child→parent in data = upstream→downstream in the flow):
- 사회문제 → each top-level activity; 투입물(if shown) → each activity.
- activity `a` → output `o` for every `o` whose `from_activities` contains `a` (or a sub-id).
- output `o` → outcome `c` for every `c` whose `from_outputs` contains `o` (link to the outcome node
  inside its group — Mermaid allows edges into subgraph members).
- outcome `c` → impact (every outcome).
- outcome `c` **-.->** each of its indicator nodes (dashed = "measured by"), inside the group.

Skeleton (light fills + black text; per-outcome TB group; level header first):
```
%%{init: {"themeVariables": {"fontSize": "16px"}}}%%
flowchart LR
  classDef lvl fill:#eceff1,stroke:#90a4ae,color:#000,font-weight:bold;
  classDef problem fill:#fdecea,stroke:#e57373,color:#000;
  classDef act fill:#fff3e0,stroke:#ffb74d,color:#000;
  classDef out fill:#e8f5e9,stroke:#81c784,color:#000;
  classDef outcome fill:#e3f2fd,stroke:#64b5f6,color:#000;
  classDef ind fill:#f5f5f5,stroke:#bdbdbd,color:#000;
  classDef impact fill:#ede7f6,stroke:#9575cd,color:#000;
  lv0["사회문제"]:::lvl --> lv1["활동 (Activities)"]:::lvl --> lv2["산출물 (Outputs)"]:::lvl --> lv3["성과 (Outcomes) · 지표"]:::lvl --> lv4["영향 (Impact)"]:::lvl
  prob(["사회문제: …"]):::problem
  act_1["1.1 …"]:::act
  op_1["1.1 …"]:::out
  subgraph oc_g1 [" "]
    direction TB
    oc_1["성과 1 …"]:::outcome
    ind_oc_1_1("1-1 지표명"):::ind
    oc_1 -.-> ind_oc_1_1
  end
  style oc_g1 fill:transparent,stroke:#90caf9,stroke-dasharray:4
  imp_1["영향 …"]:::impact
  prob --> act_1
  act_1 --> op_1
  op_1 --> oc_1
  oc_1 --> imp_1
```

### 1b. Text fallback (ALWAYS emit right below the Mermaid block, when drawn)
Some viewers don't render Mermaid (e.g. **Antigravity / VS Code without the Mermaid preview extension** — see
README "Antigravity"). So directly under the ```mermaid``` block, also emit a **renderer-independent ASCII
causal flow** in a plain (no-language) fenced block, built from the **same `from_*` links** — identical
content, never a reduced version. This guarantees the theory is visible everywhere. Format: one line per
chain, left→right with `→`, outcome indicators in `[ ]`, one indented `└─` branch when an output feeds
multiple outcomes. Example:
```
사회문제: 산모 사망 → [활동 1.1 산전관리 교육] → [산출물 1.1 교육 이수] → (성과 1 시설분만 실천 ↑) → 영향: 모자보건 개선
                                                                          └ 지표: [1-1 시설분만율]
```
Keep it compact; every node and edge in the Mermaid diagram must also appear here.

## 2. Narrative ToC (level by level)
Top→bottom: **사회문제 → 투입물(있을 때) → 활동 → 산출물 → 성과 → 영향**. For each level list the items with
their narratives. For 성과/산출물, show indicators by name only (NO baseline/target numbers — those live in
the monitoring view and default to `추후 확정`). Use the dotted/dash display numbering from
`render-pdm-md.md` (output `j.k`, output indicator `j.k.m`, outcome indicator `j-m`).

## 3. 측정 준비 — 직접 수집해야 할 데이터 (Measurement readiness)
The most useful insight for a ToC-view (`biz-dev`/`csr-esg`/`nonprofit`) user is: *"to measure your impact later, you must
collect THESE data."* The agent cannot collect these for the user, so make the to-do explicit. Build this
section **only from existing indicator fields** (`name`, `definition`, `measurement_target`, `formula`,
`data_source`, `timing`, `collector`, `baseline`) — do not invent indicators.

For every output and outcome indicator, list a row (this mirrors the 사회공헌 지표 DB: 지표명 · 지표 정의 ·
측정 대상 · 측정방법):
- **지표** (name) · **지표 정의** (definition) · **측정 대상** (measurement_target, `-` if null) ·
  **측정방법·산출식** (formula — the 사회공헌 지표 DB style: a short 측정방법 문장/식 such as `(사후 평균) − (사전 평균)`
  or `해당 기간 … 인원 수`; `-` if qualitative) · **무엇을/어디서** (data_source) · **언제** (timing) · **누가**
  (collector).
- Mark **"직접 트래킹 필요"** when the data is not an operational by-product the team already has — i.e.
  survey / interview / FGD / assessment / 평가-based, or `collector` is the project team. Mark
  **"운영데이터(자동 확보)"** when it falls out of normal operations (e.g. 보급/판매 로그, 가입 로그).
  *(Example: 보급 대수 = 운영데이터; 교육 이수자 수·만족도·역량 평가 = 직접 트래킹 필요.)*
- Because `baseline` defaults to `추후 확정`, add a reminder in plain language: **착수 전(또는 초기)에
  기초선(baseline)을 측정해 두어야** 종료 시 변화를 입증할 수 있다. *(No KOICA/rule-id citation in the
  rendered text — see the no-KOICA rule above.)*

Render as a short table or checklist, ordered outcome-first (outcome indicators are the hardest and most
important to track).

## 4. 검증 (Verification)
- **논리 검증 (implemented):** run `prompts/outcome-verify.md` for each outcome — is it a real Outcome (a
  change-of-state recovering the problem's cause), or output-at-scale / general utility? Emit the per-outcome
  `✅ 부합` / `⚠️ 교정 필요` verdicts here, in `meta.lang`, grounded in 변화이론·로직모델. Advisory (non-blocking).
- **IRIS+ 유사 지표 (implemented):** run `prompts/iris-match.md` for each **outcome** indicator — it distills
  English keywords, calls `python3 rules/iris-search.py --json --top 6 "…"` (deterministic search over the
  593-metric IRIS+ catalog), and suggests the nearest metric(s) **from the returned shortlist only**, tagged
  "참고용 · 공식 매핑 아님 · IRIS+ © GIIN". If `iris-search.py` exits 3 (catalog `rules/iris-metrics.json`
  absent), show "IRIS+ 유사 지표 매칭 준비 중" and **NEVER invent an IRIS+ code**.

## Fidelity checks (must hold)
- **DRAFT (`gate_mode=DRAFT`): §1 is the "확정 후 출력" placeholder, NOT a Mermaid diagram.** The full
  diagram appears only once finalized (`gate_mode` GATE/AUDIT).
- When drawn: every activity/output/outcome/impact in `toc.json` appears as a node; every `from_*` link
  appears as an edge (no silent drops, no invented edges).
- **When drawn, the §1b text fallback is ALSO emitted** (plain fenced block) with the same nodes/edges — so
  the flow is visible in viewers without Mermaid (Antigravity).
- **Measurement tables (§3, monitoring) carry `지표 정의` and `산출식`** (formula `-` when qualitative); the
  §3 사회공헌 table also carries `측정 대상` (`-` when null / for intl-dev).
- **No `subgraph` LEVEL containers** — levels are shown by LR flow + class color + the `lvl` header row.
  (Per-outcome TB groups are the one allowed subgraph use.)
- **Level header row (`lvl` chain) is the first line of the graph**; every `classDef` carries `color:#000`.
- **No external-tool tip lines** (mermaid.live etc.) in the output.
- Each **outcome's indicators sit BELOW it inside its TB group** (`-.->`); no baseline/target numbers in
  the diagram.
- **`toc.md` contains no "KOICA" mention** (labels, notes, citations — none).
- **No `class …` statement lines in the Mermaid block** — only inline `:::` (stray-"CLASS"-node bug).
- Mermaid node ids are unique and contain only `[A-Za-z0-9_]`.
- For `biz-dev`/`csr-esg`/`nonprofit`: no 수원기관/투입물 nodes are forced in.
