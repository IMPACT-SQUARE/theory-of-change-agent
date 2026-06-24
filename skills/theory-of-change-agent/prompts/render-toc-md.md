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
Emit a Mermaid `flowchart LR` built from the `from_*` causal links. The point of a Theory of Change is
that activities connect to outputs, outputs to outcomes, outcomes to impact; **show those edges.**

Mapping (each `pdm.json` id → a Mermaid-safe node id by replacing non-alphanumerics with `_`, e.g.
`op-1` → `op_1`, `act-1.1` → `act_1_1`):
- One node per **활동(activity)** (include sub-activities), **산출물(output)**, **성과(outcome)**, and the
  **영향(impact)**. Node label = the node's narrative (display number prefix optional, e.g. `1.1 …`).
- A leading **사회문제(Social problem)** node from `results_chain.problem_analysis` (현상 → 원인, defined
  and corrected per `rules/value-rules.md` §V1) feeding the activities. The social problem anchors the
  chain: its **해결 크기 = the Outcome (사회적 가치, §V2)**.
- **투입물(Inputs)** node only when `meta.use_case = intl-dev` and `inputs` is present (ODA-specific —
  koica-rules §11.1). Omit for `biz-dev`/`csr-esg`.
- **Edges (follow the DAG, child→parent in data becomes upstream→downstream in the flow):**
  - activity `a` → output `o` for every `o` whose `from_activities` contains `a` (or a sub-id of `a`).
  - output `o` → outcome `c` for every `c` whose `from_outputs` contains `o`.
  - outcome `c` → impact for every outcome.
  - 사회문제 → each activity (or each top-level activity); 투입물(if shown) → each activity.
- Group each level with a `subgraph` (사회문제 / 투입물 / 활동 / 산출물 / 성과 / 영향) so the columns read
  left→right. Keep labels short; escape `"` in labels.

```
flowchart LR
  subgraph 활동 [활동 Activities]
    act_1["1.1 ..."]
  end
  subgraph 산출물 [산출물 Outputs]
    op_1["1.1 ..."]
  end
  ...
  act_1 --> op_1
  op_1 --> oc_1
  oc_1 --> imp_1
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
- Every activity/output/outcome/impact in `pdm.json` appears as a node; every `from_*` link appears as an
  edge (no silent drops, no invented edges).
- Mermaid node ids are unique and contain only `[A-Za-z0-9_]`.
- For `biz-dev`/`csr-esg`: no 수원기관/투입물 nodes are forced in.
