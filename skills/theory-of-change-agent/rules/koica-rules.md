# KOICA PDM Writing Rules (Rule Dictionary)

> **Purpose.** This file is the authoritative, machine-and-human-readable encoding of the KOICA PDM
> guideline rules that the 변화이론 에이전트 (Theory of Change Agent) skill follows when it (1) interviews a user, (2) generates
> `pdm.json`, and (3) self-checks the result. Every rule below is traceable to a page in the source
> guideline so it can be audited against the original.
>
> **Source of truth:** `docs/KOICA PDM 가이드라인(최종).pdf` (한국국제협력단 평가심사실, 2018-03, 36p).
> Page citations below are written as `[p.NN]`. Section numbers (§I–§VI) follow the guideline's TOC.
>
> **Cross-references:** `[C0x]` / `[A0x]` tags link a rule to the corresponding entry in
> `rules/checklist.json`. The full traceability matrix is at the end of this file.
>
> **Language policy:** This reference is written in English (skill-internal language) but preserves the
> exact KOICA Korean terms in parentheses, because those terms are the canonical labels that must appear
> verbatim in generated PDMs and in the official form.

---

## 0. Canonical terminology (2017 revision) [§IV, p.19]

The 2017 revision changed two terms. The harness uses the **new** terms.

| Old term | New term (use this) |
|---|---|
| 사업목적 (project purpose) | **성과 (Outcome)** |
| 상위목표 (overall goal) | **영향 (Impact)** |

Canonical level names (top→bottom of the results chain):
**영향 (Impacts)** → **성과 (Outcomes)** → **산출물 (Outputs)** → **활동 (Activities)** → **투입물 (Inputs)**.

---

## 1. Theory of Change → PDM (변화이론) [§II, pp.12–15]

### 1.1 Concept [p.12]
변화이론(Theory of Change) = a diagram of how **inputs → activities → outputs → outcomes → impacts**
produce the intended change. Results-based monitoring is distinguished from traditional monitoring
precisely because it accounts for the Theory of Change (Imas & Rist 2009) [p.12].

### 1.2 Results-chain elements [p.12]
- **Impacts (영향):** long-term change accumulating from outcomes; resembles the strategic goal.
- **Outcomes (성과):** behavioral change arising from the activity's goal or from the outputs.
- **Outputs (산출물):** goods/services produced as the direct result of activities.
- **Activities (활동):** activities actually carried out by the project.
- **Inputs (투입물):** resources put into the project (funds, personnel).

The chain can also include internal/external factors, target groups, and background [p.14]; the
**causal relationship** among 투입물–활동–산출물–성과–영향 is the core [p.15]. KOICA uses **PDM** as its
results-chain rendering [p.15].

### 1.3 Procedure to build a PDM from a Theory of Change [p.15]
1. From **problem analysis (문제분석)** and **objective analysis (목표분석)**, construct the Theory of
   Change, **including the key assumptions (주요가정)** linking each step.
2. Considering project scope and available resources, define **Activities, Outputs, Outcomes, Impacts**.
3. Add the **performance-management plan** (성과지표 and 정보출처/data sources) → write the PDM.

> A project may skip the explicit Theory-of-Change step, but **the PDM is still constructed on a
> Theory-of-Change basis** [p.15]. → In Mode A the harness elicits the chain explicitly; in Mode B it
> reconstructs/validates it.

---

## 2. PDM structure: the 4×4 matrix [§III, pp.16–18]

PDM = the final product of logical project planning; a **4-row × 4-column** planning &
performance-management tool [p.16].

### 2.1 Column / row layout [p.17–18]

| 요약 (Narrative Summary) | 객관적 검증지표 (OVI) | 검증수단 (MoV) | 중요가정 (Important Assumptions) |
|---|---|---|---|
| **영향 (Impacts)** | *(none — see §3.5)* | *(none)* | assumptions: Outcome→Impact |
| **성과 (Outcomes)** | outcome indicators | MoV | assumptions: Output→Outcome |
| **산출물 (Outputs)** | output indicators | MoV | assumptions: Activity→Output |
| **활동 (Activities)** | **투입물 (Inputs)** | | **선행조건 (Pre-conditions)** |

Note the special bottom row: in the **Activities** row, the OVI column holds **Inputs (투입물)** and the
Important-Assumptions column holds **Pre-conditions (선행조건)** [p.17, p.19].

### 2.2 Vertical logic (수직 논리) [p.17]
"투입물 ⇒ 활동 ⇒ 산출물 ⇒ 성과 ⇒ 영향" is a **causal chain**, advanced step-by-step via the
**중요가정 (assumptions)** on the right. The if–then ladder [p.17]:
- If **inputs** are provided **and** pre-conditions hold → **activities** are performed.
- If **activities** are performed **and** assumptions hold → **outputs** are produced.
- If **outputs** are produced **and** assumptions hold → the **outcome** is achieved.
- If the **outcome** is achieved **and** assumptions hold → it contributes to the **impact**.

### 2.3 Horizontal logic (수평 논리) [p.18]
Each row must provide: a **measurable indicator (OVI)**, a **means of verification (MoV)**, objective
evidence for monitoring & evaluation, transparency for stakeholders, and a check on **external factors
(assumptions)**.

---

## 3. Per-level writing rules [§IV, pp.19–24]

### 3.1 Inputs (투입물) [p.19–20]
- **Definition:** budget and personnel resources put in to run the project.
- **Write:** project period (사업기간), budget (예산), and recipient-country **input resources**
  (투입자원) — i.e., resources such as **land/personnel (토지, 인력)**, *not* the recipient's task/role
  description (분담사항/업무내용) [p.20].
- **Form example [p.19]:** KOICA → 사업기간, 사업비. 수원기관 → 분담재원, 기타재원(부지 등).

### 3.2 Activities (활동) [p.20]
- **Definition:** activities actually performed by the project (e.g., hospital construction, teacher
  training, curriculum development, workshops).
- **Checklist (guideline's own) [p.20]:**
  1. Does it include **all core activities** required to produce the outputs? **(exclude M&E activities)**
  2. Are the **pre-conditions** needed before execution/commencement recorded? (e.g., government
     certification, land acquisition)
  3. Given the project period and inputs, are the activities **realistic**?
- **Every activity must connect to ≥1 output (no orphan activities) `[C08]`** — *reviewer decision
  (2026-05-28): **Critical** (promoted from Advisory).* Even **support activities** must have an
  explainable linkage to an output. Grounded in checklist item #1 (activities exist to produce the
  outputs) [p.20] and the rule that outputs are **derived through activities** [p.21]. Structurally
  checkable → enforced by the deterministic validator.

### 3.3 Outputs (산출물) [p.21]
- **Definition:** goods or services **directly** produced through activities — **usually noun-form (명사형)**.
- **Write:** capacity/area figures corresponding to the target value go in the **OVI** column (not the
  narrative). Example [p.21]: 신축된 병원 → OVI "건축 공정율(총 면적 00㎡)"; 신규 개발된 교과과정 세트 3 →
  OVI "교과과정 개발 건수(4개)".
- **Count: limited to 3–4 core outputs [p.21] `[C02]`.** Selection criteria: (a) share of total budget
  (예산 비중), (b) importance to achieving the outcome (성과목표 달성 영향, 중요도).
- **Checklist [p.21]:**
  1. Does it include the core goods/services derived/produced through the activities?
  2. Does it include **all** outputs needed to achieve the outcome?
  3. Can all outputs be produced/derived within the period via inputs and activities?

### 3.4 Outcome (성과) [p.22]
- **Definition:** the **behavioral-change (행동변화) state** caused by the activity goal or by the outputs.
- **Phrasing form (house style, reviewer 2026-06-10) `[A08]`:** write the outcome narrative as an
  **outcome-oriented keyword phrase** — a 결과 상태 noun phrase such as **"~강화 / ~확대 / ~개선 / ~정착 /
  ~제고"** — **not** a full `~한다` sentence. A *state* reads more naturally as a phrase, and this keeps
  outcomes visually parallel with noun-form outputs (C06). **Guard:** the keyword must still name a
  **change in the target group's behavior/practice**, not an output scaled up (e.g. "주민 위생실천 정착"
  ✅, but "위생교육 확대" ❌ — that is output volume, not behavioral change). A08 judges *behavioral
  change*, independent of phrasing form.
- **Outcome count:** the 2017 normative text recommends a single outcome (do **not** split into
  initial/intermediate) [p.22], but the guideline's own inspection samples [pp.25–26] and every reference
  KOICA-approved PDM (reviewed during development) uses multiple outcomes. The harness therefore enforces **no** count
  constraint — single or multiple outcomes are both allowed. (See §10 reviewer decision 2026-06-05; the
  prior `[C07]` rule was removed.)
  - Set a project period that allows **at least one** measurement of outcome data (성과 발현 기간 고려).
  - If a mid/long-term outcome **cannot** be measured within the project period, record the
    **measurement timing in the MoV column** (e.g., "시스템 작동 1년 후 2020년 3월 측정예정") [p.22].
- **Indicator count: 1–2 is appropriate `[C03]`.** Even complex projects should **avoid exceeding 3**.
  When multiple indicators are used, label them (e.g., "1. 시설분만율, 2. 산전관리율") [p.22].
- **Checklist (7 items) [p.22]:**
  1. Does it record a **behavioral-change state** caused by the activity goal or outputs?
  2. Is it **realistically achievable** given period, inputs, and activities?
  3. Does it carry an outcome target at the **maximum level for which accountability can be secured**?
  4. Is it a **specific** target whose **scope and level can be clearly defined**?
  5. Is achievement/degree **measurable**?
  6. Is it **not** a mere restatement/recombination of outputs (산출물의 재구성 또는 동어반복)?  `[A07/A08]`
  7. Is it an outcome achievable through the outputs, and measurable at the **end-of-project evaluation**?

### 3.5 Impact (영향) [p.23]
- **Definition:** a **strategic goal the project can CONTRIBUTE to** — *not* one it achieves on its own.
- **No indicators `[C01]`:** establish the long-term goal/expected effect for "영향," **but do NOT record
  성과지표 (indicators) or 검증수단 (MoV)** for it [p.23]. Direct performance-management scope at the
  individual-project level is **limited to Outputs and Outcomes**.
- **Strategic goal content:** record the recipient country's relevant **development-strategy sub-goal**
  **together with the corresponding SDGs sub-indicator** [p.23].
  - Example [p.23]: "1. SDGs 4.c 교사연수를 통해 자격있는 교사 공급의 증대 / 2. ICT 활용 교원 비중 증가
    (니카라과 교육발전전략 2017–21 제5목표)."
- **Checklist (4 items) [p.23]:**
  1. Does it express the broad, long-term change to which the project contributes?
  2. Is it appropriate as a change **accumulating** from the project's outcome plus other internal/external changes?
  3. Is it **linked to the project's Outcome**?
  4. Does it clearly state the strategic goal from **SDGs or the recipient country's national development strategy**?

### 3.6 PDM inspection points (점검 포인트) [pp.25–26]
When reviewing a finished PDM, check:
- **Logical linkage between Outputs and Outcome** (산출물–성과 간 논리적 연계성) [p.25].
- Is the **outcome** appropriate as an outcome? Are the **outputs** appropriate as outputs? [p.25–26]
- Is an output a **repetition of activity content** (활동내용의 반복)? [p.25] `[A07]`
- Is the **number of outcome indicators** appropriate? [p.25] `[C03]`
- Is the **impact phrasing** appropriate? [p.26]
- Are outcome **level and indicators** consistent (성과 수준과 지표가 부합)? [p.26]
- Are outputs phrased appropriately? Is the outcome target **measurable at end-of-project evaluation**? [p.26]

---

## 4. Indicator selection principles [§I, pp.6–10]

### 4.1 SMART + CREAM (selection principle, 선정원칙) [p.6] `[A01, A02]`
Indicators must be **clear, measurable, cost-reasonable, and timely**.

- **SMART** — Specific (명확·구체적), Measurable (측정 가능), Attainable (합리적 자원투입으로 데이터 수집
  가능), Relevant (달성 목표에 부합), Timely (필요 시점에 확보 가능).
- **CREAM** — Clear (명확·모호하지 않음), Relevant (측정 대상/주제에 적합), Economic (합리적 비용으로
  측정 가능), Adequate (M&E에 충분한 자료 제공), Monitorable (모니터링 가능). *(Source: World Bank 2013;
  Kusek & Rist 2004.)*

### 4.2 Quantitative-first (정량지표) [p.7]
- Prefer **objective, quantitative** indicators; qualitative indicators are **supplementary** only.
- For **Outcome** indicators, **avoid** submission/attendance status (제출/참석 여부) and satisfaction
  (만족도) type indicators [p.7].
- Good example [p.7]: 성과목표 "초등학생 학업성취도 개선" → 성과지표 "6학년 중 표준 수학/과학시험 70점
  이상 비중" 또는 "기초선 대비 표준 수학/과학시험 점수 개선 비중."

### 4.3 Target-alignment (목표 부합성) [p.7]
Measure the **degree of achievement of the intended goal, not the activity**. Contrast [p.7]:
- (산출물) 교육 횟수 / 참가자 수 / 완성된 마스터플랜 / 완성된 타당성분석보고서
- (성과) 교육내용 이해도 / 실제 활용도 / 정책 입법화 정도 / 수원국 투자결정·자금 확보

### 4.4 Disaggregation (분리지표) [p.7] `[A03]`
Disaggregate each indicator by group (성별/연령/지역) to capture differential demand and impact.
**Gender-disaggregated indicators are mandatory (성별분리 지표는 필수)** [p.7]; add other disaggregations
per the target area's socio-cultural structure.
- Example [p.7]: 성과지표 "초등학교 등록율(남/여학생, 도시/농촌지역)."

### 4.5 Proxy indicators (대리지표) [p.8] `[A04]`
When an outcome cannot be measured directly, a **proxy (대리지표)** may be selected. It is usually based
on **1–2 assumptions** linking it to the outcome, so it must be **clearly defined with evidence from
prior research** [p.8].
- Good example [p.8]: 성과목표 "농촌가구 소득 증대" → 대리지표 "농촌가구 지출액(달러 기준)" (assumes
  income↑ drives consumption/spending↑; grounded in prior research).
- Bad example [p.8]: 성과목표 "사법 서비스에 대한 접근성 제고" → 대리지표 "신규 설립된 법원 수" — improper
  if the real barrier is corruption/cost/awareness rather than physical access.

### 4.6 Baseline (기초선) [p.8–9]
- **Definition:** the indicator's initial value measured before the project (사업수행 이전 현재) — a
  reference point for judging change [p.8].
- **Timing:** conducted **after the PDM is finalized**, before full-scale commencement, by agreement of
  the project manager, implementing agency, and recipient agency [p.8]. The later the baseline (after
  change has begun), the lower its accuracy and the higher the risk of under-evaluating the project [p.9].
- **Secondary-data check (2차자료 점검) [p.9]:** before deciding to collect a baseline, check for usable
  secondary data (census, international agencies, NGOs, M&E/evaluation reports); reliable, timely,
  monitor-able secondary data saves cost/time.
- **Survey/analysis design [p.9]:** for innovative/creative, strategically important, or
  evidence-scarce/contested projects, introduce a **comparison-group design** (사업 수행지역 vs 비
  수행지역; treatment vs comparison). For general projects, use **pre/post comparison** in the target area.
- **Collection methods [p.9]:** census/DB (secondary), surveys, interviews, **FGD (초점그룹면담)**,
  observation, measurement.

### 4.7 Target (목표치) [p.10] `[A05]`
- **Definition:** the quantitative performance level to achieve within the project period.
- **Formula [p.10]:** `기초선 수준 (baseline) + 기대하는 개선 수준 (expected improvement) = 목표치 (target,
  realistically achievable within the limited period)`.
- Set by considering baseline, available human/material resources, schedule; based on international
  standards, similar-project evaluation results, and trend analysis; **requires stakeholder agreement**;
  must be **realistic and concrete** [p.10].

### 4.8 Baseline/Target are DEFERRED ("추후 확정") by default [p.8–9, p.10, p.29] `[reviewer 2026-06-10]`
- **House policy (since 2026-06-10):** the harness does **NOT** elicit or invent `baseline`/`target`
  values during planning. They default to the placeholder **`"추후 확정"`** (TBD-after-field-survey).
- **Why this is guideline-consistent, not a deviation:** the guideline already says the **baseline is
  collected *after* the PDM is finalized** (PDM 확정 후, before full commencement) [p.8], and that
  **baseline/target are NOT recorded in the PDM itself** — they live in the separate monitoring /
  performance-check forms [p.29]. Targets follow from the baseline (`target = baseline + improvement`
  [p.10]), so neither can be set credibly at planning time; users set them from 현장답사/리서치 later.
- **What IS still elicited up-front** (knowable without a survey): indicator `name`, `definition`,
  `mov` `[C04]`, `data_source`, `timing`, `collector`, `disaggregation`, `is_proxy`.
- **Rendering:** the PDM matrix (`pdm.md`, the "end image") shows **no target numbers**; the monitoring
  matrix (`monitoring.md`) keeps the 기초치/목표치 columns but renders **`추후 확정`** until a value is
  supplied. A user may still volunteer a value, in which case it is recorded verbatim.
- **Gate impact:** `A05` (target realism) is evaluated **only when a concrete target is present** — a
  `추후 확정` placeholder is **N/A (counts as pass)**. `C04` (MoV) is unaffected — MoV is knowable up-front.

---

## 5. Monitoring stages & reporting [§I, pp.5–11]

### 5.1 Implementation stages of results-based monitoring [p.5]
- **Planning stage (기획·계획 수립):** ① build agreement on performance goals (성과목표 합의·수립) → ②
  select indicators (성과지표 선정) → ③ collect baseline (기초선) → ④ set targets (목표치).
- **Execution stage (시행):** ⑤ performance monitoring → ⑥ report results → ⑦ use results.

### 5.2 Reporting [p.10] and use [p.11]
- **Reporting system [p.10]:** define who reports to whom, in what format, at what cycle, alongside the
  performance-management plan. Use baseline/target comparison with charts; report shortfalls **and** the
  explanation/measures; significant results (positive or negative) must be reported promptly.
- **Use of results [p.11]:** evidence-based decision-making (budget/schedule changes, strategy),
  accountability & transparency, systematic accumulation of performance data for future evaluation.

---

## 6. PDM & project management; performance-check forms [§V–§VI, pp.27–31]

### 6.1 PDM regions ↔ management areas [p.28]
- **성과관리 (performance mgmt):** the Outcome narrative + OVI region.
- **위험관리 (risk mgmt):** the 중요가정 (assumptions) column.
- **일정관리 (schedule mgmt):** the Activities row.
- **예산관리 (budget mgmt):** the Inputs region.

### 6.2 Performance-check forms (성과점검 양식) [pp.29–31]
- Purpose: standardized form to aggregate performance data by country/sector/agency [p.29].
- **The PDM is a summary of the performance-management plan; baseline, target, and other performance
  data are NOT recorded in the PDM itself** — they go in the separate monitoring / annual
  performance-check forms [p.29].
- **Performance-management cycle [p.29]:** Outputs are managed by **annual data** for achievement rate;
  the **total target is set on the basis of the closing-report (종료보고) timepoint.**

> **MVP scope note:** the harness MVP generates the PDM matrix + the monitoring matrix (indicator
> definition/baseline/target/rationale/source/timing/collector/disaggregation). The **annual
> performance-check sheet (연간 성과점검표)** is **out of scope** for the MVP.

---

## 7. Guideline-normative text vs. the guideline's own examples (IMPORTANT)

There is a real, documented tension the harness must handle deliberately:

- **Normative text [p.23]:** "영향(Impact)에 대한 성과지표와 검증수단은 기재 불요" → Impact has **no**
  indicators/MoV.
- **But the guideline's own inspection samples [pp.25–26]** show Impact rows **with** indicators
  (e.g., "수혜 주민 만족도," "8호선 경로 교통수단 대체율"), **and all 3 reference PDMs reviewed during development** also
  put indicators at the Impact level (see `benchmark/` expected-failures matrix).

**Harness policy:**
- **GATE mode** (authoring a *new* PDM): enforce the **2017 normative text** → Impact must have no
  indicators/MoV `[C01]`.
- **AUDIT mode** (ingesting an *already-approved/existing* PDM): **report** the deviation, do **not**
  block — a KOICA-approved PDM that deviates from the guideline should not be rejected by the tool.

This choice is intentional and is the reason the benchmark expects real PDMs to "fail" C01 — that is
**correct detection behavior**, not a rule error. Do **not** loosen C01 to make real PDMs pass.

> **Reviewer decision (2026-05-28):** house practice follows the **normative text** for Impact — Impact
> carries **no** indicators/MoV. `[C01]` stays **Critical** in GATE mode.
>
> **Reviewer decision (2026-06-05):** the parallel single-outcome rule `[C07]` was **removed** (was
> Critical, now no rule). All three reference KOICA-approved PDMs use 2–3 outcomes, and the guideline's
> own inspection samples [pp.25–26] show multiple-outcome examples — keeping C07 as Critical (or even as
> Advisory) would misrepresent KOICA practice. See §10.

---

## 8. Quick rule summary (the numbers)

| Level | Indicators? | Count rule | Form |
|---|---|---|---|
| 영향 Impact | **No** indicators/MoV `[C01]` | n/a | strategic goal = SDGs sub-indicator + national strategy sub-goal |
| 성과 Outcome | Yes | per-outcome: **1–2** indicators ideal, **≤3** hard cap `[C03]`; outcome count is not constrained (C07 removed 2026-06-05) | behavioral-change state |
| 산출물 Output | Yes | **3–4** `[C02]` | **noun-form**, distinct from activities `[C06/A07]` |
| 활동 Activity | (Inputs go in OVI col) | core only, exclude M&E | verb/process; pre-conditions recorded |
| 투입물 Input | n/a | n/a | period, budget, recipient input resources |

Every output/outcome indicator must have a **MoV** `[C04]`. Every output must be referenced by some
outcome (`from_outputs`) `[C05]`. Every activity **must** be referenced by some output
(`from_activities`) `[C08]`.

**Baseline/target are deferred** (`"추후 확정"`) at planning time `[§4.8, reviewer 2026-06-10]` — not in
the PDM matrix, kept as `추후 확정` in the monitoring matrix, filled later from 현장답사. `A05` is N/A
while a target is deferred.

---

## 9. Traceability matrix (checklist rule → guideline source)

> Audit aid: verify each row against the cited page in `docs/KOICA PDM 가이드라인(최종).pdf`.

| Rule | Type | Statement | Guideline source |
|---|---|---|---|
| **C01** | Critical | Impact has no OVI/MoV | §IV p.23 (normative) |
| **C02** | Critical | Outputs count = 3–4 | §IV p.21 |
| **C03** | Critical | Outcome indicators 1–2, max 3 | §IV p.22; §IV p.25 (inspection) |
| **C04** | Critical | Every output/outcome indicator has a MoV | §III p.18 (horizontal logic) |
| **C05** | Critical | Every output referenced by an outcome | §III p.17 (vertical causal chain) |
| **C06** | Critical (LLM) | Output is noun-form, not an activity restatement | §IV p.21 (noun-form); p.25 (inspection) |
| ~~**C07**~~ | ~~Critical~~ | ~~Exactly one outcome~~ — **removed 2026-06-05** (see §10) | ~~§IV p.22~~ |
| **C08** | Critical | No orphan activities — every activity connects to ≥1 output | §IV p.20 (activity checklist #1), p.21 |
| **A01** | Advisory (LLM) | Indicator satisfies SMART | §I p.6 |
| **A02** | Advisory (LLM) | Indicator satisfies CREAM | §I p.6 |
| **A03** | Advisory | Gender-disaggregated indicator present | §I p.7 (mandatory) |
| **A04** | Advisory | Proxy indicator justified with assumption | §I p.8 |
| **A05** | Advisory (LLM) | Target realistic vs. baseline | §I p.10 (target = baseline + expected improvement) |
| **A06** | Advisory (LLM) | Measurable at end-of-project evaluation | §IV p.22 (outcome checklist #7) |
| **A07** | Advisory (LLM) | Output is not a restatement of activities | §IV p.21, p.25 |
| **A08** | Advisory (LLM) | Outcome describes behavioral change | §IV p.22 (outcome checklist #1) |

> **Note on C04/C05/C08:** these are DAG-integrity rules that operationalize the guideline's vertical &
> horizontal logic (§III) and the output-from-activity / outcome-from-output requirements (§IV); they are
> the harness's explicit encoding of the implicit "logical linkage" inspection point [p.25], not new
> rules invented outside the guideline.

---

## 10. Reviewer decisions

### 2026-05-28
1. **C04 = per-indicator MoV (RESOLVED).** Every indicator must carry its own MoV — stricter than the
   guideline's per-level wording (§III). Confirmed by reviewer.
2. **Activity→Output = Critical `[C08]` (RESOLVED, promoted from Advisory).** Every activity must connect
   to ≥1 output; **even support activities must have an explainable output linkage**. (C05 output→outcome
   was already Critical.) C08 is structurally checkable → added to the deterministic validator.
3. **Impact has no indicators — `[C01]` Critical (RESOLVED).** House practice follows the guideline's
   **normative text** [p.23], not its example tables. GATE blocks Impact-level indicators; AUDIT reports
   the deviation for already-approved PDMs.
4. **One reference PDM used pre-2017 terminology (RESOLVED).** One development-era reference PDM reflects
   pre-revision terms. Extraction maps: **목적 (Project Purpose) → 성과 (Outcome)** and **목표 (Goal) →
   영향 (Impact)**.

### 2026-06-05
5. **C07 single-outcome rule REMOVED (reverses 2026-05-28 decision to keep it Critical).** Evidence:
   all three reference PDMs reviewed during development use multiple outcomes (2–3 each), and the
   guideline's own inspection samples [pp.25–26] also show multi-outcome
   examples. The 2017 normative text [p.22] saying "set one outcome" is in tension with KOICA's actual
   practice; enforcing C07 (even as Advisory) would misrepresent that practice. Outcome count is now
   unconstrained at every gate. Per-outcome rules (C03 1–3 indicators, A08 behavioral-change) still
   apply to **each** outcome individually. Affected: `checklist.json`, `validate-critical.sh`,
   `prompts/interview-a-concept.md`, `prompts/generate-pdm.md`, `benchmark/expected/*.json`.

### 2026-06-10
6. **Baseline/Target DEFERRED ("추후 확정") by default (NEW — see §4.8).** Source: two independent pilot
   users (기획 부문) reported that 기대치/목표치 are set from 현장답사·리서치 *after* planning, so being
   asked for them up-front forces fabricated numbers. This is **guideline-consistent**, not a deviation:
   the guideline already places baseline collection *after* PDM finalization [p.8] and keeps
   baseline/target **out of the PDM matrix** [p.29]. Policy: do not elicit/invent baseline/target; default
   to `"추후 확정"`; render no target in `pdm.md`; show `추후 확정` in `monitoring.md`; `A05` is N/A while
   deferred; `C04` (MoV) unchanged. Affected: `checklist.json` (A05 note), `schema/pdm-schema.json`,
   `prompts/interview-a-concept.md`, `prompts/generate-pdm.md`, `prompts/render-pdm-md.md`,
   `prompts/render-monitoring-md.md`.
7. **Draft-first mode ADDED (Mode C, gate_mode DRAFT) — runs alongside the existing guided interview for
   A/B feedback.** Rationale: pilot users prefer a "표 먼저 → 그 위에서 수정" flow over a long up-front
   interview. Mode C asks **one** question (project one-liner + outcome scope), immediately generates a
   full **draft** `pdm.json` (all nodes `stale: true`, unknowns `추후 확정`), renders the tables, and runs
   checks **non-blocking** (gate_mode `DRAFT`, report-only like AUDIT). The user edits on top of the table
   (Phase 4 propagation); a later **Finalize** step flips gate_mode to `GATE` and enforces the hard
   Critical gate. The existing guided interview (Mode A/B + GATE) is **unchanged** so the two interaction
   models can be compared. Affected: `SKILL.md`, `schema/pdm-schema.json` (meta.mode `C`, gate_mode
   `DRAFT`), `prompts/draft-first.md` (new), `prompts/generate-pdm.md`, `README.md`.
8. **Outcome phrasing = keyword form; activities & indicators get hierarchical display numbering; outputs
   render as one consolidated table (NEW — pilot-user readability feedback).** (a) Outcome narratives use
   an outcome-oriented keyword phrase (~강화/~확대/~개선) rather than a `~한다` sentence (see §3.4; A08
   still judges behavioral change, not form). (b) The rendered PDM uses **dotted 3-level display numbering
   matching the official submission form** (confirmed against a user-supplied form sample). Separators
   differ by level: **산출물·활동 use dots, 성과 검증지표 use a dash.** Output `j.k` (k-th output of
   outcome j) → its indicators `j.k.m` with dots (e.g. `1.1` → `1.1.1, 1.1.2`); activities producing output
   `j.k` → `j.k.m` with dots (e.g. `1.2.1`); outcome j's indicators → `j-m` with a dash (e.g. `1-1, 1-2`) —
   the dash distinguishes 성과 검증지표 from dotted output numbers like `1.1`. Display numbers derive from
   array order at render time — internal IDs (`op-*`, `ind-*`) are unchanged. (c) Outputs + their indicators render as a **single consolidated table** (matches the official
   submission form), and the Activities row renders activities **as a table grouped by output** instead of
   prose. These are render/style changes only — no Critical/Advisory rule logic changes. Affected:
   `prompts/render-pdm-md.md`, `prompts/render-monitoring-md.md`, `prompts/interview-a-concept.md`,
   `prompts/generate-pdm.md`.

### 2026-07-01
9. **ToC node diagram redesign (임팩트스퀘어/세라 feedback + user decisions).** The `toc.md` Mermaid diagram
   (`prompts/render-toc-md.md` §1): (a) **remove the `subgraph` level containers** — the big level boxes
   hid the nodes; levels are now shown by LR flow + per-node `classDef` color only. (b) **Outcome
   indicators render as small nodes attached (`-.->`) to their outcome** so 아웃컴+지표 show together (임톨
   image-2 style). (c) Keep **LR** orientation and **single-level** outcomes for now; Mermaid stays the
   renderer (a polished PPT/SVG export is a separate future track). Render/style only — no rule changes.

변화이론 에이전트 is broader than KOICA PDM. The results-chain engine (problem → activities → outputs →
outcomes → impact, wired by `from_*`) is shared; only the **end-view** and which structures are required
differ per `meta.use_case` (SKILL.md Phase 1 step 0).

| use_case | who | end-view | PDM-form requirements |
|---|---|---|---|
| `intl-dev` | 국제개발 / KOICA 사업 | PDM 매트릭스 (`pdm.md`) | full (this file applies in full) |
| `biz-dev` | 임팩트 스타트업 / 신규사업개발 (소셜벤처) — 조직 단위 가능 | ToC 뷰 (`toc.md`, node diagram) | relaxed (no 수원기관, inputs optional — §4.1, §11.1) |
| `csr-esg` | 사회공헌 / CSR, ESG (기업) | ToC 뷰 (`toc.md`) | relaxed |
| `nonprofit` | 비영리 (재단·NGO) — 조직 단위 가능(연차보고서) | ToC 뷰 (`toc.md`) | relaxed (same as biz-dev/csr-esg) |
| `invest-screen` | 투심 / 임팩트 투자심사 | (planned) prose opinion | n/a |

### 11.1 ODA-form requirements are use-case-specific
- **`inputs` (투입물) and the recipient/수원기관 column are ODA/`intl-dev` constructs** [§3.1, p.19–20].
  KOICA 사업은 전체 예산 기반이라 투입물·수원기관이 핵심이지만, 창업·사회공헌 모델은 인풋 규모가 자유롭고
  대상이 기관이 아니라 최종 수혜자다. For `biz-dev`/`csr-esg`/`nonprofit`, **OMIT the `recipient`/수원기관 block**
  and keep `inputs` minimal (the venture's own resources/period); do not force a 수원기관 row. The
  variable, behavioral logic (활동 → 산출물 → 성과) is what matters there. (`schema/pdm-schema.json` makes
  `inputs.recipient` optional accordingly; `inputs` itself stays present for shape validity.)
- C-rules unaffected: the deterministic gate (C01–C08) never inspects `inputs`/recipient, so relaxing
  them does not change benchmark behavior.

### 11.2 Social-value methodology — IMPLEMENTED (2026-06-24, from 임팩트스퀘어 "Theory")
The 2026-06-23 meeting deferred these until 임팩트스퀘어's material arrived. It arrived (the "Theory"
working notes), so the **definition** parts are now implemented in `rules/value-rules.md`:
1. **Social-problem definition + correction (DONE).** `value-rules.md` §V1 + `prompts/social-problem.md`:
   a front sub-stage that elicits and **corrects** the 사회문제 against ① 구조적 ② 현저한 다수 ③ 고통, via
   현상 → 원인. Wired into the Mode-A interview stage 1.
2. **Outcome = 사회적 가치 definition (DONE).** `value-rules.md` §V2: 사회문제 해결 크기, neutral-0 baseline
   (only −→0 counts), 핵심 대표 특성. Indicator quality = 실행력·설명력 (§V3). Wired into outcome stage.

**Outcome cross-verification (2-way):**
3a. **Logical check — IMPLEMENTED (2026-07-02).** `prompts/outcome-verify.md` judges each outcome
    (change-of-state vs output-at-scale; recovers the cause vs utility; indicator = 변화분 with 실행력·
    설명력). Advisory, in the "검증" section. No example set needed (reasoned, not example-matched).
3b. **Nearest-IRIS+ metric — IMPLEMENTED (2026-07-02, grounded).** `prompts/iris-match.md` +
    `rules/iris-search.py` (deterministic keyword search) suggest the nearest metric for each outcome
    indicator from the real IRIS+ catalog (`rules/iris-metrics.json`, 593 PI/OI/II impact metrics;
    `build-iris-metrics.py`, GIIN-attributed). Shortlist-only, "참고용 · 공식 매핑 아님"; never invent a
    code; catalog absent → "매칭 준비 중". JSON git-ignored (GIIN-copyright), shipped in local zip only.
    (value-rules §V5b.)
4. **Case-based verification** against real measured cases — still pending.

### 11.3 Backlog (separate workstream, see meeting minutes)
- **투심 모드** — prose impact-review of an IR/business model (different output shape).
- ~~**PDM ↔ 예산표 연결**~~ → **IMPLEMENTED as MVP (2026-07-09) — see §12.**

## 12. 예산 (PDM ↔ 사업예산서) — MVP 2026-07-09

Grounded in two real KOICA-style budget sheets (private, `budget/` git-ignored). Both share one skeleton,
which the `budget` block of `pdm.json` mirrors (schema `budget` / `$defs.budget_line`):

```
관(대분류)         항(=PDM Output)      목(=PDM Activity)     세목(line + 산출근거)
직접사업비          1. …                 1.1 …                 단가 × 수량 × 횟수 (× 개월)
간접사업비          (결과사슬 밖)          현지사무소 운영 / 본부 인건비 등
일반관리비          rate × (직접+간접)     KOICA 통상 5%
```

**Observed rules (→ deterministic checks in `rules/budget-rollup.py`; LLM never does the arithmetic):**
- **B01** 세목 금액 = 산출근거 곱 (`unit_price × qty × freq × (months||1)`). 인건비 = 월단가×인원×개월; 출장 =
  단가×일수×횟수; 지원금 = 건단가×건수. amount는 null로 두면 스크립트가 계산.
- **B02** 세목별 **분담 split** (KOICA/파트너): Σ(shares) = 금액; funder id must exist.
- **B03** 일반관리비: 명시 금액이 있으면 그 값을 쓰고(실무 예산은 5% 정액이 아니라 **상한 내 임의 금액**), **실효율 > 5%만 warning**. 상한의 분모는 **총사업비(일반관리비 포함)** — 실제 시트 2종의 표기 비율(1.34%/1.38%/4.86%)이 모두 GM/총사업비와 일치하며, 그중 하나는 GM/(직접+간접)으로는 5.11%라 옛 분모였으면 합법 예산을 오탐. amount가 null일 때만 rate로 계산(gm = rate×(직접+간접)/(1−rate), 즉 gm/총사업비 = rate). (2026-07-16 실데이터 검증 3사이클에서 equality→상한, 분모 직접+간접→총사업비로 두 차례 수정.)
- **B04** 모든 직접비 라인은 실재하는 PDM `output_id`/`activity_id`에 연결 (예산의 연결성 = C05/C08의 예산판).
  PDM 노드가 삭제/변경되면 라인이 고아가 됨 → Phase 4에서 재실행해 경고.
- **B05** (warning) 예산 미배정 활동 — every PDM activity should carry ≥1 budget line; missing ones are
  listed, never silently ignored (and never invented).
- **연차별 합계**: `year_totals` (직접+간접, 일반관리비 제외) — 총괄시트의 연차 컬럼; 세목의 `year`가 `budget.years`에 없으면 warning. (2026-07-16 5개년 총괄시트 검증에서 추가.)
- **비율 프레임 (`budget.caps`, 2026-07-21 피드백):** 규정상 한도를 **인터뷰 초반에 고정**하고 세우는
  방식 — `caps.gm_rate` (일반관리비 상한; 기본 5%, 프로그램 규정이 다르면 사용자 값), `caps.personnel_rate`
  (인건비 상한, 예 30%; 규정에 없으면 검사 안 함), `caps.note` (규정 출처). 한도를 지어내지 않는다.
- **B07** (warning) 인건비 비율 한도 — `category:"인건비"` 세목 합 ÷ 총사업비 > `caps.personnel_rate`.
- **B06** (warning) funder 약정(pledged) vs 배분 합계 mismatch — 약정액은 **일반관리비 포함** 표기가 실무 표준이므로, 차이가 일반관리비와 정확히 일치하면 정상 처리 (헛경고 방지).
- **간접사업비·일반관리비는 결과사슬 밖** — PDM 노드에 연결하지 않는다 (Inputs/관리 성격). Outcome/Impact에는
  예산 라인이 없다 (성과는 비용이 아니다).

**Flow:** gate pass 후 offer (SKILL Phase 3 step 11) → `prompts/budget-build.md` interview (단가·수량은
사용자에게서만; never invent prices) → `budget` block in `pdm.json` → `budget-rollup.py` verify →
`prompts/render-budget-md.md` → `out/budget.md` (숫자는 스크립트 출력 그대로). intl-dev only (MVP);
연차 정교화·xlsx 내보내기·양방향 자동 동기화는 후속.
