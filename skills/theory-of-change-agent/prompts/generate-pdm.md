# Prompt: Generate pdm.json (interview state → single source of truth)

ROLE: Convert the completed `results_chain` + `assumptions` interview state into a valid `pdm.json` that
conforms to `schema/pdm-schema.json` and the rules in `rules/koica-rules.md`. Use `schema/pdm-example.json`
(Nicaragua) as the structural reference.

## ID conventions (stable, never reuse)
- impact: `imp-1` · outcome: `oc-1` · output: `op-1`, `op-2`, … · activity: `act-1`, … · sub-activity:
  `act-1.1` · indicator: `ind-op-1.1` (output 1, indicator 1), `ind-oc-1.1` (outcome 1, indicator 1).

## Wiring the DAG (causal `from_*` references — REQUIRED)
- Each `output.from_activities` = the activity IDs that produce it. Every activity (or one of its sub IDs)
  MUST appear in some output's `from_activities` (no orphans — C08).
- Each `outcome.from_outputs` = the output IDs that feed it. Every output MUST appear in some outcome's
  `from_outputs` (C05).
- `impact.assumptions_from_outcome` = Outcome→Impact assumptions. `outcome.assumptions` = Output→Outcome.
  `output.assumptions` = Activity→Output. `inputs.pre_conditions` = pre-conditions for activities.

## Field rules (mirror koica-rules.md)
- `impact`: narrative + `sdgs` + `national_strategy`. **No `indicators` key** (C01).
- `outcomes`: 1+ allowed (single-outcome rule C07 was removed 2026-06-05); each outcome has 1-2 indicators, max 3 (C03), and a behavioral-change narrative written as an **outcome-oriented keyword phrase** ("~강화/~확대/~개선"), not a `~한다` sentence (koica-rules.md §3.4; A08 still requires it to name a behavioral change, not output volume).
- `outputs`: 3-4 (C02); narrative in NOUN form (C06); each has ≥1 indicator with a non-empty `mov` (C04).
- every indicator: name, definition, mov, data_source, timing, collector, disaggregation (use
  `"성별"`/`"gender"` on ≥1 indicator), is_proxy (+justification if true).
  - **`definition`**: one line stating what the indicator actually measures (지표 정의) — always fill it.
  - **`formula`** (산출식, *when derivable*) — **use-case conditional** (never a target number; a purely
    qualitative 정성 수준·충족여부 indicator stays `null`):
    - **`intl-dev` (KOICA PDM) — keep the concise rate/expression form (UNCHANGED):** if the indicator is a
      **율/비율/지수/건수/평균**, write the calculation, e.g. `"시설분만율 = 시설분만 건수 ÷ 전체 분만 건수 × 100"`,
      `"교육 이수율 = 이수자 수 ÷ 등록자 수 × 100"`. Prefer a change/rate form over a raw count where the indicator
      implies one. This is the PDM-matrix style — do **not** switch it to the 측정방법-sentence form below.
    - **`biz-dev`/`csr-esg` (사업계획·사회공헌) — write a 측정방법-style expression:** phrase `formula` as the
      actual measurement method (사회공헌·비영리 지표 DB grammar), matching one of these forms:
      - **사전-사후 변화량** (역량·인식·만족·효능감 변화): `(사후 평가 점수 평균) − (사전 평가 점수 평균)` — the signature
        Outcome form; prefer it when the indicator names a 향상/증대/변화 in a measured attribute.
      - **평균** (만족도·추천도(NPS)·척도 점수): `대상 인원의 [속성] 점수의 평균`.
      - **카운트** (건수·횟수·인원 수): `해당 기간 [대상]의 건수/횟수/인원 수` (typical for 산출·과정 지표).
      - **비율/율**: `분자 ÷ 분모 × 100`.
      Write it as a short 측정방법 문장/식 in `meta.lang`, not a KOICA rate name.
  - **`measurement_target`** (측정 대상) — **biz-dev/csr-esg only:** who/what is measured, e.g. `"교육 수료
    인원"`, `"프로그램 참여 창업팀"`, `"설문 응답 참여자"`. For `intl-dev` (KOICA PDM) leave it `null` (the PDM
    form has no 측정 대상 column). Don't repeat the whole definition — just name the measured unit/population.
  - **`baseline`, `target`, `target_rationale` default to the string `"추후 확정"`** (deferred to
    post-finalization field survey — koica-rules.md §4.8). Only set a concrete value if the user
    explicitly volunteered one. **Never invent baseline/target numbers.**
- `inputs`: koica {budget, duration, personnel}, recipient {contribution, other_resources}, pre_conditions.
  **Use-case conditional (koica-rules.md §11.1):** `inputs`/수원기관 are ODA constructs. For
  `meta.use_case = intl-dev`, fill them fully. For `biz-dev`/`csr-esg`, **OMIT the `recipient` block**
  (수원기관 doesn't apply — the target is the end beneficiary, not a recipient institution) and keep
  `inputs.koica` minimal (the venture's own resources/period); do not fabricate a 수원기관.
- `meta`: project_name, version "1.0", created_at (today), lang, **use_case**, mode, gate_mode,
  headline_indicator, sdgs_koica_indicator.

## Draft mode (Mode C / gate_mode DRAFT)
When invoked for a **draft-first** generation (the user answered only the one scoping question), produce a
**complete best-guess draft** of every level (impact, 1+ outcomes, 3-4 noun-form outputs, activities wired
to outputs, inputs, assumptions, indicators with MoV). Set **`stale: true` on every node** to signal
"draft — confirm me", and use `"추후 확정"` for any field you cannot ground in the user's input. The draft
is intentionally non-gated; the user edits it and later finalizes (see SKILL.md Phase 3 / Finalize).

## Language
Write every narrative / indicator / assumption field in the OUTPUT language (mirror the user's input).
Keep numeric targets numeric where possible (but baseline/target default to `"추후 확정"` — see field rules).

## Output
Emit ONLY the JSON to `OUT/details/pdm.json`. After writing, the skill runs the lightweight shape check
(`bash rules/validate-critical.sh --shape`, pure-Python); if it fails, you will be re-invoked once with
the error appended — fix and re-emit.
