# Prompt: Render toc.md (Theory-of-Change view + node diagram)

ROLE: Render `OUT/pdm.json` into `OUT/toc.md` — the **Theory-of-Change (변화이론) view** used for the
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
- A leading **사회문제(Social problem)** node from `results_chain.problem_analysis` (or the impact's
  framing if no explicit problem) feeding the activities. *(The deeper social-problem sub-agent is
  planned — koica-rules §11.2; for now use what the interview captured.)*
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

## 3. 검증 (Verification) — placeholder (planned)
Add a short section noting that **outcome verification is planned** (logical output↔outcome check + IRIS+
similarity), pending 임팩트스퀘어 example cases (koica-rules §11.2). Do **not** fabricate IRIS+ matches.
> 예: "이 성과가 진짜 '성과(아웃컴)'인지, 어떤 글로벌 지표(IRIS+)와 가까운지에 대한 검증은 준비 중입니다."

## Fidelity checks (must hold)
- Every activity/output/outcome/impact in `pdm.json` appears as a node; every `from_*` link appears as an
  edge (no silent drops, no invented edges).
- Mermaid node ids are unique and contain only `[A-Za-z0-9_]`.
- For `biz-dev`/`csr-esg`: no 수원기관/투입물 nodes are forced in.
