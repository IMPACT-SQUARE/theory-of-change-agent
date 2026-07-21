# Social-value rules (grounded in Theory of Change / logic model)

> Encodes working definitions of **사회문제 / 사회적 가치(=Outcome) / 지표** so the agent can *define and
> correct* them during the interview — most important for `biz-dev`/`csr-esg`/`nonprofit`, but it also sharpens the
> Outcome for `intl-dev` PDMs. These definitions are grounded in **변화이론(Theory of Change) / 로직모델**
> and standard impact-measurement principles (the **counterfactual / 반사실** and **부가성(additionality)**,
> and **과대추정 지양(conservatism)**). Cross-ref: `koica-rules.md` §3.4 (outcome), §11.
>
> **USER-FACING FRAMING (important):** when you explain or correct something to the user, cite
> **변화이론·로직모델** and these standard concepts — NOT "임팩트스퀘어 방법론" or any internal source name.
> Reason it out (tie the outcome back to the problem's cause; distinguish 회복 vs 일반 효용); don't appeal
> to authority. *(Provenance for maintainers only: adapted from the shared "Theory [draft]" notes; never
> surface an internal source name to the user.)*
>
> **Full organized decomposition:** `rules/value-methodology.md` (the concept chain 사회문제→사회적 가치→
> 지표→산출식→보고서, the four principles 실행력>설명력>일관성>보수성, and the §I/§II/§III detail). This file
> is the concise operational quick-rules.

## V1. 사회문제 (Social problem) — define AND correct
A Theory of Change starts from a clearly-defined social problem (현상 → 원인). Not every 문제 is a 사회문제;
a **사회문제** is a state that is **simultaneously**:
- **① 구조적 (structural):** the cause is social-structural, NOT self-correctable by individual effort.
- **② 현저하게 다수 (widespread):** affects or is recognized by a notable majority, not a small minority.
- **③ 고통받는 상태 (harm):** absent intervention it produces serious deficiency / 침해 (suffering).

Operationalize through the **현상 → 원인** causal link; the project's solution must target the **cause**,
not just the symptom.

**Correction behavior (do this, don't just accept the first framing):** if the stated problem is really an
*individual* problem, a *market/utility* gap, or a *solution stated as a problem*, name it and reframe —
e.g. "그건 사회문제라기보다 개인의 어려움/시장 기회에 가깝습니다. 변화이론에서 사회문제는 ①구조적으로 발생하고
②현저하게 다수가 ③고통받는 상태를 말합니다 — 이렇게 좁혀볼까요?" Re-elicit until it qualifies (or the user
knowingly proceeds).

## V2. 사회적 가치 = the Outcome (사회문제가 해결된 정도)
In a logic model the **Outcome(성과)** is the **change in the target group** caused by the outputs — and,
for impact, specifically the change that **addresses the social problem's cause**. So **사회적 가치 = how
much the 사회문제 is resolved (recovered)**, which is different from general 효용가치.
- **Counterfactual / 반사실 lens (neutral baseline):** count only the improvement that **recovers the
  harmed state back toward a neutral baseline** — the part attributable to solving the problem. Extra
  utility **beyond** that baseline (however positive) is a general benefit, **not** 사회적 가치. This is
  the standard **부가성(additionality)** + **과대추정 지양** principle; use it to push back when a proposed
  성과 is just utility expansion. *(Explain it by tying the outcome to the problem's cause, e.g. "우리가
  정의한 원인은 '…의 부재'였으니, 성과는 그 부재가 해소된 정도여야 합니다. '…확대'라고 하면 이미 있던 것이 더
  늘어난 부분까지 포함돼 일반 효용에 가까워집니다.")*
- 사회적 가치 is complex/qualitative, so pick **one representative characteristic** to measure (like using
  당도/Brix to stand in for a fruit's 맛); distinguish **핵심 vs 보조** 사회적 가치.
- This **is** the Outcome(성과) in the results chain — a change-of-state, **not** output volume (consistent
  with `koica-rules.md` §3.4 and rule A08).

## V3. Indicator quality — 실행력 & 설명력
A social-value indicator has the shape **"솔루션을 통한 어떤 현상의 어떤 변화분"**. Judge each on:
- **실행력 (actionability):** from this value, can you tell whether the org is doing well and what to improve?
- **설명력 (explanatory power):** does it explain the org's **real** change (not a process by-product)?

Type axes — choose deliberately: 전후(A vs B) vs 변화분(A−B); 단위당 vs 총량; 화폐 vs 비화폐; 정량 vs 정성.
(Maps onto `koica-rules.md` A01 SMART / A02 CREAM.)

## V4. Overall principles (priority order)
**실행력 > 설명력 > 일관성 > 보수성.** When sub-rules conflict, the earlier principle wins. Be
**conservative** — do not overstate the value (cf. SROI "do not over-claim", GRI reporting principles).

## V5. Outcome verification (2-way)
- **(a) Logical check — IMPLEMENTED.** `prompts/outcome-verify.md`: for each outcome, judge (change-of-state
  vs output-at-scale; recovers the problem's cause vs general utility; indicator = 변화분 with 실행력·설명력).
  Advisory, emitted in the "검증" section (render-toc §4). No example set required.
- **(b) Nearest-IRIS+ metric — IMPLEMENTED (grounded, never fabricated).** `prompts/iris-match.md`: for each
  **outcome** indicator, distill English keywords → `python3 rules/iris-search.py --json --top 6 "…"` (a
  deterministic keyword search over the catalog) → suggest the nearest metric(s) **from the returned
  shortlist only**, tagged "참고용 · 공식 매핑 아님 · IRIS+ © GIIN". If the catalog is absent (search exits 3),
  show "IRIS+ 매칭 준비 중" and **NEVER invent an IRIS+ code**. Emitted in render-toc §4 after the logical verdicts.
  > **Catalog build:** `rules/iris-metrics.json` (593 impact metrics: ID + name + definition + theme/SDG) is
  > produced by `build-iris-metrics.py` from the GIIN IRIS+ Excel, filtered by ID prefix **PI/OI/II**
  > (Product/Operational/Investment Impact — IRIS+ has no explicit outcome label; Description/Financial rows
  > dropped). The JSON is **committed to the public repo with an embedded GIIN attribution/copyright
  > block** (2026-07-21 — the IRIS+ ToU permits free redistribution with attribution; sale prohibited; raw
  > Excel stays out). All install paths get matching out of the box; "매칭 준비 중" now only means a truly
  > missing/deleted catalog.
