# Prompt: IRIS+ nearest-metric matching (grounded, never fabricated)

ROLE: For each **outcome indicator**, suggest the nearest **real** IRIS+ metric(s) so the user can align
their measurement to a recognized standard. This is the second half of outcome verification (value-rules
§V5b); the **logical** check (`outcome-verify.md`) runs first. Advisory / 참고용 — **non-blocking**, never
gates. Work in `meta.lang`.

## Hard rules (grounding)
- **Only suggest metrics returned by the search tool.** Never invent an IRIS+ code, name, or definition.
- If the catalog is absent, show **"IRIS+ 유사 지표 매칭 준비 중"** and stop — do NOT guess.
- Always label suggestions **"참고용 · 공식 IRIS+ 매핑 아님"** and attribute **IRIS+ © GIIN (iris.thegiin.org)**.
- Match **outcome** indicators only (the change-of-state ones). Skip output/activity indicators.

## Steps (per outcome indicator)
1. **Distill English keywords.** The catalog is English. From the indicator's name + its outcome's
   narrative, extract 3–6 English content words (translate Korean → English; drop 수/율/총 etc.). Example:
   "청정 취사도구 이용 가구 비율" → `clean cookstove adoption household`.
2. **Run the deterministic search** (returns a shortlist from the 593-metric catalog; never scan the JSON
   inline). **Path: the script lives at `<SKILL_ROOT>/rules/iris-search.py`** where SKILL_ROOT is the
   directory containing SKILL.md (this prompt lives in `<SKILL_ROOT>/prompts/`). In app sandboxes the
   working directory is usually NOT the skill root — use the full path (or locate it once, e.g.
   `find / -name iris-search.py 2>/dev/null | head -1`):
   ```
   python3 <SKILL_ROOT>/rules/iris-search.py --json --top 6 "clean cookstove adoption household"
   ```
   - **Exit code 3 from a run that EXECUTED** (script printed "catalog not found") → emit
     "IRIS+ 유사 지표 매칭 준비 중" for the whole section and stop.
   - **"No such file or directory" / command failed → that is a PATH problem, NOT a missing catalog.**
     Find the script and retry — NEVER print "매칭 준비 중" for a path failure (2026-07-21 bug: sandbox
     CWD ≠ skill root made the relative call fail and the section wrongly showed 준비 중).
   - Empty `results` / all low scores → say "적합한 IRIS+ 유사 지표를 찾지 못했습니다" for that indicator.
3. **Pick from the shortlist only.** Choose the 1–2 candidates whose `name`+`definition` truly match the
   indicator's *change-of-state* (prefer a rate/level/change metric over a raw count when both appear).
   If none of the returned candidates genuinely fit, say so — do **not** force a match.
4. **Present** (per indicator, short): the outcome indicator → `IRIS+ 코드 이름` + one-line why it fits +
   the "참고용, 공식 매핑 아님" caveat. Note any gap (e.g. "IRIS+ has the count, not the rate — track both").

## Output shape (example, ko)
> **성과지표 1-1 "직업훈련 수료자 취업률"**
> → **IRIS+ `PI3527` Job Placement Rate** — 조직 클라이언트 중 취업에 연결된 비율로, 정의가 거의 일치합니다.
> (참고용 · 공식 IRIS+ 매핑 아님 · IRIS+ © GIIN)

Keep it to a couple of lines per indicator. This section lives under render-toc §4 "검증", after the logical
verdicts.
