# Prompt: Render pdm.md (PDM matrix, KOICA 4×4)

ROLE: Render `OUT/pdm.json` into `OUT/pdm.md` as the KOICA 4-row × 4-column PDM matrix. Do not invent
data — render only what is in the JSON. Keep KOICA labels bilingual; write content in `meta.lang`.

## Header block
```
# PDM (Project Design Matrix)

| 사업명 (Project) | {meta.project_name} |
| 대표 수혜자 지표 / 목표치 | {meta.headline_indicator} |
| 작성일 (Created) | {meta.created_at} | 버전 (Version) | {meta.version} |
```

## Display numbering (DOTTED 3-level — matches the official submission form; koica-rules.md §10 #8b)
Assign **dotted hierarchical display numbers** from array order (independent of the internal `op-*`/
`ind-*` IDs). The form nests each indicator UNDER its output: output **`1.1`** → indicators **`1.1.1`,
`1.1.2`**. Scheme (each `.` adds one level deeper in the results chain):
- **Outcomes:** the j-th outcome (`outcomes[]` order) → **`j`** (`성과 1, 2, …`).
- **Outputs:** root each output under the outcome it feeds; the k-th output of outcome j → **`j.k`**
  (single-outcome project → `1.1, 1.2, 1.3, …`, exactly like the source form). An output feeding multiple
  outcomes is numbered under its first outcome (note "(공통)").
- **Output indicators:** the m-th indicator of output `j.k` → **`j.k.m`** with DOTS (`1.1.1`, `1.2.1`,
  `1.2.2`, …).
- **Outcome indicators:** the m-th indicator of outcome j → **`j-m`** with a DASH (`1-1, 1-2`). The dash
  form (confirmed from the form) is what distinguishes 성과 검증지표 from dotted output numbers like `1.1`.
- **Activities:** group by the output they produce; an activity for output `j.k` → **`j.k.m`** with DOTS
  in the 활동 table (`1.2.1`; sub-activities → `j.k.m.s`).

> **Confirmed against the user's form:** 성과 검증지표 use **dashes** (`1-1, 1-2`); 산출물 and 활동 use
> **dots** (output `1.1`, output indicator `1.1.1`, activity `1.2.1`). The differing separators keep the
> two namespaces distinct even though both root at the outcome number.

## Matrix (rows = levels, columns = 요약 / OVI / MoV / 중요가정)
| 요약 (Narrative Summary) | 객관적 검증지표 (OVI) | 검증수단 (MoV) | 중요가정 (Important Assumptions) |
|---|---|---|---|

Row-by-row:
- **Impacts (영향):** narrative (incl. SDGs + national strategy). **OVI column = `-`. MoV column = `-`.**
  Assumptions column = `impact.assumptions_from_outcome`.
- **Outcomes (성과):** one sub-row per outcome: `성과 j` + keyword narrative · its indicators numbered
  `j-m` (DASH: `1-1, 1-2`) (**name + definition only — NO target/baseline numbers**) · `outcome.mov` ·
  `outcome.assumptions`.
- **Outputs (산출물) — render as ONE consolidated table** (matches the submission form): one sub-row per
  output indicator so the numbering aligns. Columns = `산출물 j.k` (narrative, shown once per output) ·
  OVI `j.k.m` (indicator name/definition, **no target numbers**) · that indicator's MoV · the output's
  assumptions. Outputs with multiple indicators span consecutive `j.k.1, j.k.2…` rows under the same
  `산출물 j.k`.

> **Target/baseline are NOT shown in the PDM matrix** (the "end image"): the guideline keeps them out of
> the PDM [p.29] and the harness defers them to `"추후 확정"` (koica-rules.md §4.8). They appear only in
> the monitoring matrix. Do **not** print `추후 확정` placeholders in this matrix — just omit the number.

- **Activities (활동) — render as a table grouped by output** (not prose, koica-rules.md §10 #8a): a small
  table with columns `산출물 (Output)` | `활동 (Activities)`, one row per output (`산출물 j.k`) listing its
  activities by display number (`j.k.1, j.k.2…`, sub-activities indented). This table goes in the 요약 column of the
  Activities row. In THIS row the OVI column holds **Inputs (투입물)** — KOICA (period/budget) + recipient
  (contribution/other) — and the Important-Assumptions column holds **Pre-conditions (선행조건)** from
  `inputs.pre_conditions`.

## Fidelity checks (must hold)
- Impact row literally shows `-` in OVI and MoV.
- Activities row carries Inputs in the OVI column and Pre-conditions in the Assumptions column.
- Every indicator present in pdm.json appears somewhere in the matrix (no silent drops).
- Display numbers are consistent and parent-aligned: indicator `j.k.m` sits under `산출물 j.k`; activity
  `j.k.m` is listed under output `j.k`; no number is skipped or duplicated.
