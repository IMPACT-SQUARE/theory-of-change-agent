# Prompt: Render budget.md (사업 예산서)

ROLE: Render the `budget` block of `OUT/details/pdm.json` into **`out/budget.md`** — the 사업 예산서 view,
mirroring the KOICA budget-sheet layout (관 → 항 → 목 → 세목 + 산출근거 + 분담). Labels bilingual where
they are KOICA form labels; content in `meta.lang`.

## Numbers come from the script — VERBATIM
First run:
```
python3 rules/budget-rollup.py OUT/details/pdm.json --json
```
Every amount, subtotal (소계), total, 비율, and the 일반관리비 in the render **must be copied from this
JSON** (`amount`, `subtotal`, `direct_total`, `indirect_total`, `general_mgmt.amount`, `grand_total`,
`funder_totals`, `ratios`, plus each line's `basis_str`). Do NOT recompute or round differently. If the
script exits 1, stop and fix the data first (budget-build.md step 6); if it exits 3, there is no budget —
don't render this file.

## Layout
```
# 사업 예산서 (Detail Budget) — {meta.project_name}

| 총사업비 | {grand_total} | 기간 {inputs.koica.duration} · 통화 {currency} |
| 분담 | {funder}: {funder_totals[f]} ({funder_ratios[f]}) … | |
```

### 1. 총괄 (Summary by 관)
| 관 | 금액 | 비율 |
|---|---|---|
직접사업비 / 간접사업비 / 일반관리비({rate}) / **총사업비** — from `direct_total`, `indirect_total`,
`general_mgmt`, `grand_total`, `ratios`.

When `budget.years` has 2+ years, add a **연차별 (By year)** row set from `year_totals`
(one row per year, verbatim; note "일반관리비 제외" — GM is a single project-level amount).

### 2. 직접사업비 상세 (항=Output → 목=Activity → 세목)
One section per `direct[]` group, headed by the PDM output's display number + narrative
(`항 1. {output.narrative} — 소계 {subtotal}`). Under it, one table per activity
(`목 1.1 {activity.text} — 소계 {subtotal}`):

| 세목 | 산출근거 | 금액 | 분담 | 연차 | 비고 |
|---|---|---|---|---|---|

- 산출근거 column = `basis_str` (+ `basis_note` in parentheses when present) — e.g.
  `4,000,000원 × 1 × 13개월 (월 인건비 × 13개월)`. Empty basis → `-`.
- 분담 column = per-funder amounts from `shares`, e.g. `KOICA 200,000,000`. Unallocated → `미배분 ⚠`.

### 3. 간접사업비 · 일반관리비
Same table per `indirect[]` group; then one line for 일반관리비:
`일반관리비 ({rate} × (직접+간접)) — {general_mgmt.amount}`.

### 4. 검증 노트 (from the script's `warnings` / `unbudgeted_activities`)
- **예산 미배정 활동 (B05)** — list each with its PDM display number + text, and the nudge
  "이 활동에는 아직 예산이 배정되지 않았습니다."
- 약정 vs 배분 차이 (B06), 분담 미배분 lines — relay in `meta.lang`.
- If there are no warnings, say the rollup passed clean (`✅ 예산 롤업 검증 통과`).

## Fidelity checks (must hold)
- Every number matches the `--json` output exactly (same digits; thousands separators OK).
- Every PDM Output/Activity referenced in `budget.direct` appears with its display number and narrative
  from `pdm.json` — the budget stays readable against the PDM.
- No invented lines, prices, or totals; unallocated/unbudgeted items shown as warnings, never filled in.
