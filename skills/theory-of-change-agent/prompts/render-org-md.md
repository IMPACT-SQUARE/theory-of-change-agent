# Prompt: Render org.md (조직 임팩트 맵 — org-unit view)

ROLE: Render the ORGANIZATION-level view for org-unit runs (`meta.unit = "org"`, primarily `nonprofit`,
also org-flavored `biz-dev`) into **`OUT/org.md`**. This is **NOT the results-chain pipeline** — a
foundation's portfolio is 미션 → 프로그램들, not one 사회문제→활동→산출물→성과 chain (2026-07-21 pilot:
forcing programs into chain slots read as "억지로 묶는 느낌"). Work in `meta.lang`.

## What this view is
**미션 → 프로그램(프로젝트) 포트폴리오 → 프로그램별 핵심 성과 한 줄.** No 산출물/활동 levels, no output-count
caps, no C-gate/R-gate — those belong to the single-project ToC. Source: `meta.org_context`
(org_name, mission, projects[]) + whatever the document states. **Render only what the document/user
provided — never invent programs, outcomes, or numbers.**

## Language rules
- Plain words only: **지표 / 확인 방법·자료 출처** — never OVI, MoV, logframe, or "KOICA" (same no-jargon
  rule as the ToC view).
- Say **"프로젝트"/"프로그램"** as the org's own document does; default to 프로젝트.

## Layout

### Header
```
# 조직 임팩트 맵 — {org_name}
```
- `> 🧭 미션: "{mission}"` (문서에서 추출; 미션이 문서에 없으면 사용자에게 한 번 물어보고, 그래도 없으면 생략 —
  지어내지 않는다.)

### 1. 구조도 (Mermaid + text fallback)
Mermaid `flowchart LR`, mission node at the root, one node per 프로젝트, each linked mission → project.
Under each project node, one small attached node with its **핵심 성과 한 줄** (문서 근거가 있을 때만).
- Style: same readability rules as render-toc §1 — every `classDef` carries `color:#000`, fontSize 16px
  init, inline `:::` only (no `class` statement lines). **No 5-level header row** — chain levels don't
  apply here.
- Directly below the Mermaid block, ALWAYS emit the renderer-independent **text fallback** (plain fenced
  block, `→` per mission→project line) — same reason as render-toc §1b.

### 2. 프로젝트 포트폴리오 (표)
| 프로젝트 | 한 줄 요약 | 핵심 성과(문서 기재 시) | 미션과의 연결 |
|---|---|---|---|
One row per detected project. 미션과의 연결 = one short clause on HOW this project serves the mission
(document-grounded; if unclear, write `연결 근거 불명확 — 확인 필요` rather than inventing one — that gap
itself is useful for 기부금 리포트/연차보고 작성자).

### 3. 다음 단계 제안
- "특정 프로젝트를 골라 **full 변화이론**으로 들어갈 수 있어요 — 어느 프로젝트로 갈까요?" (drill-down runs the
  normal single-project flow: interview → gates → `toc.md`, with the 🧭 mission-linkage line carried over.)
- 기부금 리포트/연차보고 관점 한 줄: 이 맵의 "미션과의 연결" 열이 보고서의 뼈대가 된다는 안내.

## Fidelity checks (must hold)
- Every project in `org_context.projects[]` appears in BOTH the diagram and the table (no silent drops).
- No 산출물/활동/성과 chain levels; no output-count language; no gate scores.
- No invented programs/outcomes/numbers; unclear mission links are marked `확인 필요`, not fabricated.
- No KOICA / OVI / MoV / logframe anywhere.
- Text fallback present under the Mermaid block; all classDefs carry `color:#000`.
