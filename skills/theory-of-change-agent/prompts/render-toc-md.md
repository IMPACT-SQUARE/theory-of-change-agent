# Prompt: Render toc.md (Theory-of-Change view + node diagram)

ROLE: Render `OUT/details/pdm.json` into `OUT/toc.md` — the **Theory-of-Change (변화이론) view** used for the
`biz-dev` and `csr-esg` use-cases (and optionally alongside the PDM for `intl-dev`). Same underlying data
as the PDM; this view emphasizes the **causal flow and node connections** rather than the KOICA 4×4 form.
Render only what is in the JSON. Keep KOICA labels bilingual; write content in `meta.lang`.

## Header block
```
# 변화이론 (Theory of Change) — {meta.project_name}
```
If `meta.use_case` is present, note it (e.g. `사업개발 (biz-dev)` / `CSR·ESG (csr-esg)`).

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

**No level boxes.** Do **NOT** wrap levels in `subgraph` containers — the big boxes hide the nodes
(임팩트스퀘어 feedback 2026-07-01). The `flowchart LR` flow already gives the left→right level ordering; use a
per-node `classDef` color for the level cue *without* an outer box. Each node stays its own small box.

Node id: each `pdm.json` id → Mermaid-safe (replace non-alphanumerics with `_`: `op-1`→`op_1`,
`ind-oc-1.1`→`ind_oc_1_1`). Label = the narrative (display-number prefix optional). Escape `"` in labels.

**Nodes & classes:**
- **사회문제** — one node from `results_chain.problem_analysis` (현상 → 원인, value-rules §V1); class `problem`.
  It anchors the chain (its 해결 크기 = the Outcome, §V2).
- **활동 / 산출물 / 성과 / 영향** — one node each (activities include sub-activities); classes
  `act` / `out` / `outcome` / `impact`.
- **성과지표 (outcome indicators)** — render EACH outcome indicator as a **small node attached to its
  outcome** (class `ind`), so the outcome and its indicators appear together (임톨 스타일, per user
  2026-07-01). Label = the indicator name with its `j-m` number; **NO baseline/target numbers**. (Output/
  activity indicators stay in §3 + monitoring to keep the diagram readable; add them only on request.)
- **투입물(Inputs)** — a node only when `meta.use_case = intl-dev` and `inputs` is present (§11.1); class
  `input`. Omit for `biz-dev`/`csr-esg`.

**Edges** (child→parent in data = upstream→downstream in the flow):
- 사회문제 → each top-level activity; 투입물(if shown) → each activity.
- activity `a` → output `o` for every `o` whose `from_activities` contains `a` (or a sub-id).
- output `o` → outcome `c` for every `c` whose `from_outputs` contains `o`.
- outcome `c` → impact (every outcome).
- outcome `c` **-.->** each of its indicator nodes (dashed link = "measured by").

Skeleton (colors are light fills / thin borders — a level cue with no container box; renderers vary):
```
flowchart LR
  classDef problem fill:#fdecea,stroke:#e57373;
  classDef act fill:#fff3e0,stroke:#ffb74d;
  classDef out fill:#e8f5e9,stroke:#81c784;
  classDef outcome fill:#e3f2fd,stroke:#64b5f6;
  classDef ind fill:#f5f5f5,stroke:#bdbdbd,color:#555;
  classDef impact fill:#ede7f6,stroke:#9575cd;
  prob(["사회문제: …"]):::problem
  act_1["1.1 …"]:::act
  op_1["1.1 …"]:::out
  oc_1["성과 1 …"]:::outcome
  ind_oc_1_1("1-1 지표명"):::ind
  imp_1["영향 …"]:::impact
  prob --> act_1
  act_1 --> op_1
  op_1 --> oc_1
  oc_1 --> imp_1
  oc_1 -.-> ind_oc_1_1
```

## 2. Narrative ToC (level by level)
Top→bottom: **사회문제 → 투입물(있을 때) → 활동 → 산출물 → 성과 → 영향**. For each level list the items with
their narratives. For 성과/산출물, show indicators by name only (NO baseline/target numbers — those live in
the monitoring view and default to `추후 확정`). Use the dotted/dash display numbering from
`render-pdm-md.md` (output `j.k`, output indicator `j.k.m`, outcome indicator `j-m`).

## 3. 측정 준비 — 직접 수집해야 할 데이터 (Measurement readiness)
The most useful insight for a `biz-dev`/`csr-esg` user is: *"to measure your impact later, you must
collect THESE data."* The agent cannot collect these for the user, so make the to-do explicit. Build this
section **only from existing indicator fields** (`name`, `data_source`, `timing`, `collector`, `baseline`)
— do not invent indicators.

For every output and outcome indicator, list a row:
- **지표** (name) · **무엇을/어디서** (data_source) · **언제** (timing) · **누가** (collector).
- Mark **"직접 트래킹 필요"** when the data is not an operational by-product the team already has — i.e.
  survey / interview / FGD / assessment / 평가-based, or `collector` is the project team. Mark
  **"운영데이터(자동 확보)"** when it falls out of normal operations (e.g. 보급/판매 로그, 가입 로그).
  *(Example: 보급 대수 = 운영데이터; 교육 이수자 수·만족도·역량 평가 = 직접 트래킹 필요.)*
- Because `baseline` defaults to `추후 확정`, add a reminder: **착수 전(또는 초기)에 기초선(baseline)을
  측정해 두어야** 종료 시 변화를 입증할 수 있다 (koica-rules §4.6).

Render as a short table or checklist, ordered outcome-first (outcome indicators are the hardest and most
important to track).

## 4. 검증 (Verification) — placeholder (planned)
Add a short section noting that **outcome verification is planned** (logical output↔outcome check + IRIS+
similarity), pending 임팩트스퀘어 example cases (koica-rules §11.2). Do **not** fabricate IRIS+ matches.
> 예: "이 성과가 진짜 '성과(아웃컴)'인지, 어떤 글로벌 지표(IRIS+)와 가까운지에 대한 검증은 준비 중입니다."

## Fidelity checks (must hold)
- **DRAFT (`gate_mode=DRAFT`): §1 is the "확정 후 출력" placeholder, NOT a Mermaid diagram.** The full
  diagram appears only once finalized (`gate_mode` GATE/AUDIT).
- When drawn: every activity/output/outcome/impact in `pdm.json` appears as a node; every `from_*` link
  appears as an edge (no silent drops, no invented edges).
- **No `subgraph` level containers** — levels are shown by LR flow + per-node class color only.
- Each **outcome's indicators** appear as attached (`-.->`) nodes; no baseline/target numbers in the diagram.
- Mermaid node ids are unique and contain only `[A-Za-z0-9_]`.
- For `biz-dev`/`csr-esg`: no 수원기관/투입물 nodes are forced in.
