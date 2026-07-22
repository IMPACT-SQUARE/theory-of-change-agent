# Prompt: Outcome verification (logical) — is each 성과 a real Outcome?

ROLE: For each outcome, judge **logically** whether it is a genuine **Outcome(성과)** — a change-of-state
that addresses the social problem's cause — versus an **output-at-scale** or a **general utility gain**.
Ground the reasoning in **변화이론 / 로직모델** + `rules/value-methodology.md` §II/§III (and the neutral-0 /
counterfactual lens). Work in `meta.lang`. **Do NOT cite an internal source name to the user.**

This is a **non-blocking, advisory** check, emitted as a separate **"검증(Verification)"** section/comment
next to the outcome — it **never blocks** generation or the gate. *(IRIS+ similarity matching is a SEPARATE
step; see value-rules §V5.)*

## For EACH outcome (and its indicators), check three things
1. **변화(change-of-state)?** Is it a change in the target group's **condition/behavior**, or just an output
   scaled up (e.g. "…교육 확대", "보급 대수 증가")? Output-at-scale → **⚠️** and propose the change-of-state
   phrasing (e.g. "…역량 정착", "…이용 확대").
2. **원인 회복(사회적 가치)?** Trace **현상 → 원인 → 솔루션 → 성과**: does the outcome **recover the defined
   cause**, or is it utility **above the neutral baseline** (a general benefit, not 사회적 가치)? Utility →
   **⚠️** (value-methodology §II neutral-0) and reframe by tying it back to the cause.
3. **지표 = 변화분 + 실행력·설명력?** Does each outcome indicator measure a **change** (not 참석/제출/만족도
   alone), letting you judge improvement (**실행력**) and explain the real change (**설명력**)? (§III) If not →
   **⚠️** with a better indicator suggestion.

## Output — classify every finding, then ACT on it (2026-07-22 pilot fix)
Per outcome, one short block in `meta.lang`: **`✅ 부합`** (briefly why) or **`⚠️`** with a TYPE:

- **Type A — 결함 (our own rules violated):** the indicator is an output-level count posing as an outcome
  (건수·인원수 누적), or a 수준-only measure (만족도) standing alone — i.e. it fails 지표=변화분
  (value-rules §V3). **Do NOT just print advice** (2026-07-22 pilot: the flawed indicator stayed in
  toc.json and every rendered file): propose the concrete corrected indicator (예: "협력 예술가 참여 인원"
  → "협력 예술가 1인당 평균 소득 증가율" / "재계약(지속 협업) 비율"), get ONE quick user confirm
  ("이렇게 고칠까요?" — batch multiple Type-A fixes into one confirm), then **UPDATE `toc.json`**
  (indicator name/definition/formula; mark dependents per SKILL Phase 4) so every rendered view carries
  the corrected indicator. §4 then shows `✅ (교정 반영: 이전 → 이후)`. If the user declines, keep theirs
  and leave the `⚠️` with a one-line note.
- **Type B — 판단 사항 (legitimate design choice):** e.g. a peripheral outcome (가족 유대감) that may be
  부가 효용 vs an independent 성과. ASK the user (2 concrete options: 독립 성과 유지 / 파생 효과로 통합·
  삭제), apply their decision to `toc.json`, and record it in §4. Never auto-delete an outcome.

**AUDIT mode exception:** report-only — print findings with suggestions, never modify the document.

Keep it short. Reason it out (tie to the problem's cause; distinguish 회복 vs 일반 효용) — do
not appeal to authority. Example (ko):
> **⚠️ 성과 2 "가족 교류 확대"** — 이미 교류가 있던 관계의 교류가 더 느는 부분까지 포함돼 **일반 효용**에
> 가깝습니다. 정의한 원인이 "정서적 교류를 제공할 존재의 부재"였으니, **끊겨 있던 교류가 새로 생긴/회복된 정도**
> (예: "정서적 교류 관계 형성률")로 잡는 것이 사회적 가치에 부합합니다.
