# 변화이론 에이전트 (Theory of Change Agent)

**KOICA PDM(Project Design Matrix) 생성** 스킬 — 변화이론 에이전트의 한 기능. 유저와 한 번에 한 질문씩
티키타카 인터뷰(변화이론/Theory of Change 기반)를 한 뒤, **PDM 매트릭스 + 모니터링 매트릭스**를
산출한다. 시작 시 **세 가지 진행 방식 중 무엇으로 할지 반드시 먼저 묻는다.** 산출 언어는 입력 언어를
따라간다(한글 입력→한글, 영어→영어).

> 영감: OMC `/deep-interview`, gstack `/office-hours`. 규칙 근거: `docs/KOICA PDM 가이드라인(최종).pdf`.

## 빠른 시작 (로컬 설치)

이 스킬을 개인 스킬로 등록(모든 프로젝트에서 사용):
```bash
ln -s /Users/yeonjae/isqharness/skills/theory-of-change-agent ~/.claude/skills/theory-of-change-agent
```
또는 특정 프로젝트에서만 쓰려면 `<project>/.claude/skills/theory-of-change-agent/`에 두면 된다.
Claude Code가 `SKILL.md`를 자동 인식한다. 호출:
```
/theory-of-change-agent                          # 모드 선택부터
/theory-of-change-agent --concept "한 줄 컨셉"     # Mode A (컨셉부터, 가이드 인터뷰)
/theory-of-change-agent --inputs @brief.md        # Mode B (자료 보유)
/theory-of-change-agent --draft                   # Mode C (표 먼저 — 질문 1개 후 바로 초안 표)
/theory-of-change-agent --inputs @existing-pdm.md --audit   # 기존/승인 PDM 감사
```

요구사항: `python3` (결정적 검증기 — `rules/validate-critical.py`, 의존성 없는 stdlib만). jq 불필요라
Claude Code·Claude 데스크톱 샌드박스 어디서나 동작. 선택: `jq`(벤치마크 스크립트), `jsonschema`(빌드타임 스키마 검증).

## 쓰임새 먼저 선택 (use-case)
진입 시 **무엇을 하려는지** 먼저 묻고(**3개 선택지**), 그에 따라 결과물(엔드 뷰)을 정한다. 뒷단 결과사슬 로직은 동일하다.
- **국제개발/KOICA (`intl-dev`)** → PDM 매트릭스(`pdm.md`).
- **사업개발(소셜벤처·사회공헌·비영리, `biz-dev`)** → 변화이론 도식(`toc.md`). 수원기관 등 PDM 양식 강제 안 함.
- **CSR/ESG (`csr-esg`)** → 변화이론 도식(`toc.md`).

> **투심(임팩트 투자심사)** 은 **백로그**(koica-rules.md §11.3) — 선택지에서 제공하지 않는다.

## 진행 방식 — 두 가지를 친근하게 묻는다 (mode)
진입 시 ① **지금 어떤 상태인가**(input_source) ② **어떻게 진행할까**(interaction)를 차례로 묻고, 그 조합으로
내부 흐름을 정한다:
- **상태**: `아이디어만 있어요`(concept) / `문서가 있어요`(inputs — 사업계획서·초안·기존 PDM; 승인 PDM은 `--audit` 점검만).
- **방식**: `차근차근 인터뷰`(interview · 가장 꼼꼼, 아이디어 10–20분/문서 5–10분) / `표 먼저`(draft · 가장 빠름 2–5분).

| 상태 × 방식 | 내부 모드 | 동작 |
|---|---|---|
| 아이디어 + 인터뷰 | A | 문제·목표부터 한 번에 하나씩 결과사슬 구성 |
| 문서 + 인터뷰 | B | 문서 추출 후 빈칸만 질문 |
| 아이디어 + 표 먼저 | C | 질문 1개 → 바로 초안 표 → 그 위에서 수정 |
| 문서 + 표 먼저 | B→draft | 문서 추출 → 바로 초안 표 → 수정 |

표 먼저(draft)는 비차단 게이트(`DRAFT`)로 시작하고 **"확정/finalize"** 시 하드 게이트(`GATE`)로 전환된다.
> **기초치/목표치(baseline·target)는 기본 "추후 확정"** — 현장답사·리서치 후 채운다. 인터뷰에서 묻지
> 않고 PDM 본표엔 표시하지 않으며, 모니터링 매트릭스에 `추후 확정`으로 남는다(koica-rules.md §4.8, §10 #6).

## 산출물 (`./out/`)
메인 뷰는 `out/` 루트, 원본 json·모니터링은 `out/details/`에 둔다(폴더를 열면 메인 뷰가 먼저 보이도록):
- `out/pdm.md` — PDM 4행4열 매트릭스(영향/성과/산출물/활동 × 요약/OVI/MoV/중요가정). **국제개발 메인 뷰**.
- `out/toc.md` — 변화이론 뷰: `from_*` 링크로 그린 노드 도식(Mermaid) + 측정 준비(직접 수집할 데이터). **사업개발·CSR/ESG 메인 뷰**.
- `out/details/toc.json` — 단일 진실원본. ID로 연결된 결과사슬 DAG(`from_*` 인과 참조). 모든 렌더의 원본.
- `out/details/monitoring.md` — 모니터링 매트릭스(지표정의·기초치·목표치·근거·출처·시기·수집주체·분리).
- 메인 뷰를 **마지막에 써서** 데스크톱/IDE 앱이 그 파일을 띄우게 한다(원본 json이 뜨지 않도록).

## 자가검증 (2단 게이트)
- **Critical (하드 게이트, GATE 모드에서 차단):** C01 영향 무지표/무MoV · C02 산출물 3-4 ·
  C03 성과별 지표 1-2(≤3) · C04 모든 지표에 MoV · C05 산출물→성과 연결 · C06 산출물 명사형(LLM) ·
  C08 고아 활동 없음. (C07 "단일 성과"는 2026-06-05 제거 — `rules/koica-rules.md` §10 참고.)
- **Advisory (수치 임계치, 기본 80%):** A01 SMART · A02 CREAM · A03 성별 분리지표 · A04 proxy 정당화 ·
  A05 목표 현실성 · A06 종료평가 측정가능 · A07 산출물≠활동 반복 · A08 성과=행동변화.
  (A05는 목표치가 "추후 확정"이면 N/A로 통과 — 기초치/목표치 기본 추후확정, koica-rules.md §4.8.)
- 규칙 정의/근거: `rules/checklist.json`, `rules/koica-rules.md`(가이드라인 페이지 인용).

```bash
# 구조 Critical 검증 (결정적)
bash rules/validate-critical.sh out/toc.json            # GATE: 실패 시 exit 1
bash rules/validate-critical.sh --audit out/toc.json    # AUDIT: 보고 전용
bash rules/validate-critical.sh --json out/toc.json     # {"C01":"pass",...}

# 벤치마크: 실제 PDM 3건에 대한 탐지정확도 (목표 100%)
bash benchmark/run-benchmark.sh
```

## 파일 구조
```
theory-of-change-agent/
  SKILL.md                     # 오케스트레이션 (Phase 0-4)
  prompts/                     # interview-a/b, generate-pdm, render-*, refine-advisory
  rules/                       # koica-rules.md, checklist.json, validate-critical.sh
  schema/                      # pdm-schema.json, pdm-example.json (니카라과)
  benchmark/                   # expected/synthetic-{1,2,3}.json (합성), sample-brief.md, scorer.md, run-benchmark.sh
```

## 배포 (다른 사람과 공유)
개인/프로젝트 로컬 사용엔 GitHub가 필요 없다(위 "빠른 시작"). 배포하려면 **플러그인**으로 패키징한다:
```
theory-of-change-agent-plugin/            # git repo (GitHub 권장)
  .claude-plugin/
    plugin.json                   # { "name", "version", "skills": "./skills/", "repository" }
    marketplace.json              # { "name", "plugins": [{ "name", "version", "source": "./" }] }
  skills/theory-of-change-agent/          # 이 디렉토리 전체
```
사용자는 마켓플레이스를 등록 후 설치:
```
/plugin marketplace add <owner>/<repo>
/plugin install theory-of-change-agent@<marketplace-name>
```

## 다른 AI 플랫폼에서 쓰기 (이식성)
이 스킬의 **내용물은 플랫폼 중립적**이다. 일반 마크다운(SKILL.md + 프롬프트) + 의존성 없는 파이썬 검증기
(`rules/validate-critical.py`, jq 불필요) + JSON 스키마뿐이라, 특정 모델에 묶이지 않는다.

- **선택지 질문 도구**는 이름이 아니라 역할로 호출한다 — Claude Code는 `AskUserQuestion`, Claude 앱은
  `ask_user_input_v0`, 다른 환경은 또 다른 이름일 수 있다(SKILL.md Guardrails 참고). Claude 전용 의존성은
  런타임 경로에 없다.
- **Claude Code**: 플러그인 마켓플레이스(위 "배포") — 자동 업데이트.
- **Claude 데스크톱/웹**: zip 업로드(`INSTALL-desktop.md`).
- **Antigravity (Gemini)**: **동작 확인됨(2026-07-02).** Skills에 zip 업로드로 설치. (설치: 위 방법 3 / `INSTALL-desktop.md`)
- **그 외 (Codex 등)**: 마크다운+파이썬이라 이식 가능. 패키징(확장/스킬 등록) 방식은 플랫폼마다 달라 약간의 변환이 필요할 수 있다.

## 범위 / 한계 (MVP)
- 포함: PDM 매트릭스 + 모니터링 매트릭스, 2단 자가검증, 3건 벤치마크.
- 제외(후속): `.xlsx` 직접 생성, 연간 성과점검표, 웹 프론트(orangeimpact builder 스타일), 다국어.
- 영향(Impact) 지표 정책: GATE는 가이드라인 normative text(영향 무지표)를 강제, AUDIT는 편차를 보고.
