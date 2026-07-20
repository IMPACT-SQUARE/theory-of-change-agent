# Prompt: Render monitoring.md (Monitoring Matrix)

ROLE: Render `OUT/details/pdm.json` into `OUT/details/monitoring.md` — the monitoring matrix listing every Output and
Outcome indicator with its full measurement plan. Render only JSON data; bilingual labels, content in
`meta.lang`.

## Layout
```
# Monitoring Matrix (모니터링 매트릭스)

| 사업명(기간/예산) (Project / period / budget) | {meta.project_name} / {inputs.koica.duration} / {inputs.koica.budget} |
```

Then two sections — **성과 (Outcomes)** then **산출물 (Outputs)** — each a table.

**intl-dev (KOICA PDM) — full 10 columns (unchanged):**

| 지표명 (Indicator) | 지표 정의 (Definition) | 산출식 (Formula) | 기초치 (Baseline) | 목표치 (Target) | 목표치 선정 근거 (Rationale) | 데이터 출처 (Source) | 측정 시기 (Timing) | 수집 주체 (Collector) | 분리 (Disaggregation) |
|---|---|---|---|---|---|---|---|---|---|

**ToC-view use-cases (`biz-dev`/`csr-esg`/`nonprofit`) — the 성과 (Outcomes) table DROPS
기초치/목표치/목표치 근거** (임팩톨로지 feedback 2026-07-21: they render as a wall of `추후 확정`), and adds
측정 대상 to mirror the 사회공헌 지표 DB order:

| 지표명 (Indicator) | 지표 정의 (Definition) | 측정 대상 (Target group) | 측정방법·산출식 (Method/Formula) | 데이터 출처 (Source) | 측정 시기 (Timing) | 수집 주체 (Collector) | 분리 (Disaggregation) |
|---|---|---|---|---|---|---|---|

(The 산출물 table keeps the full columns in both cases — output targets are usually real counts. If the
user volunteered a concrete outcome baseline/target, mention it in a line under the 성과 table instead of
resurrecting the columns.)

One row per indicator (iterate `outcomes[].indicators[]`, then `outputs[].indicators[]`). Use the
indicator fields: name, definition, **formula**, baseline, target, target_rationale, data_source, timing,
collector, disaggregation. Show empty fields as `-` (a qualitative indicator's `산출식` is `-`). For proxy
indicators, append "(proxy: {proxy_justification})" to the definition.

- **Prefix each 지표명 with its display number** (same scheme as `render-pdm-md.md` §Display numbering):
  output `j.k`'s m-th indicator → `j.k.m` (DOTS), outcome j's m-th indicator → `j-m` (DASH). e.g.
  `1.1.1 시설분만율`, `1-1 모자보건 실천율`. This keeps the monitoring rows aligned with the PDM matrix.

- **기초치 (Baseline) / 목표치 (Target) / 근거 (Rationale):** these are **deferred by default** — render
  the value verbatim, which is normally **`추후 확정`** (koica-rules.md §4.8). Keep the columns (they
  match KOICA's official monitoring form, where these get filled after 현장답사). Only show a number if
  the JSON carries one because the user volunteered it.

## Note (intl-dev ONLY — never emit for ToC-view use-cases)
For `intl-dev`, you MAY close with the one-line note that the PDM matrix omits baseline/target detail,
which lives here and stays `추후 확정` until the post-finalization field survey [KOICA guideline p.8–9,
p.29]. **For `biz-dev`/`csr-esg`/`nonprofit`, do NOT emit this note — no "KOICA" mention anywhere in
their monitoring.md** (임팩톨로지 feedback 2026-07-21; same no-KOICA rule as render-toc-md.md). The annual
performance-check sheet is out of scope for the MVP.
