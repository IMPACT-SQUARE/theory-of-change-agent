# 변화이론 에이전트 (Theory of Change Agent)

**KOICA PDM (Project Design Matrix) 생성** Claude Code 스킬·플러그인.
유저와 한 번에 한 질문씩 변화이론(Theory of Change) 기반 인터뷰를 진행한 뒤,
**PDM 매트릭스 + 모니터링 매트릭스**를 산출한다. 시작 시 **세 가지 진행 방식 중
무엇으로 할지 반드시 먼저 묻는다.** 산출 언어는 입력 언어를 미러링(한글→한글, 영어→영어).

영감: OMC `/deep-interview`, gstack `/office-hours`.
규칙 근거: KOICA 평가심사실 「PDM 가이드라인 (2018)」.

---

## 설치 (Claude Code)

### 방법 1 — 플러그인 마켓플레이스 (권장, 자동 업데이트)
Claude Code 안에서:
```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```
업데이트 (omc/gstack처럼 최신본 받기):
```
/plugin marketplace update impact-square
/plugin update theory-of-change-agent
```

### 방법 2 — 심볼릭 링크 (개발·빠른 설치)
```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```
업데이트는 `git pull`. 해제: `rm ~/.claude/skills/theory-of-change-agent` (원본 안전).

### 방법 3 — Claude 데스크톱 / claude.ai (Skills 업로드)
`skills/theory-of-change-agent/`를 zip으로 묶어 Settings → Skills 에 업로드.
자세히는 [`skills/theory-of-change-agent/INSTALL-desktop.md`](./skills/theory-of-change-agent/INSTALL-desktop.md).
> ⚠️ 앱에 업로드한 스킬은 **자동 업데이트되지 않는다** — 변경 시 새 zip 재업로드 필요.
> 자동 업데이트를 원하면 **방법 1(Claude Code 플러그인)** 을 쓴다.

### 요구사항
- **Claude Code** (CLI / 데스크탑 / IDE 통합 모두 가능)
- **`python3`** — 결정적 검증기(`rules/validate-critical.py`, 의존성 없는 stdlib만). **jq 불필요**라
  Claude Code·데스크톱 샌드박스 어디서나 동작.
- (선택) `jq` — 개발용 벤치마크 비교 스크립트 / `jsonschema` — 빌드타임 스키마 검증.

---

## 사용법

```
/theory-of-change-agent                                  # 진행 방식(A/B/C) 먼저 질문
/theory-of-change-agent --concept "한 줄 컨셉"             # Mode A: 컨셉부터 (가이드 인터뷰)
/theory-of-change-agent --inputs @brief.md                # Mode B: 자료 보유
/theory-of-change-agent --draft                           # Mode C: 표 먼저 (질문 1개 후 초안 표)
/theory-of-change-agent --inputs @existing-pdm.md --audit # 기존/승인 PDM 감사 (보고 전용)
```

세 가지 모드 — 진입 시 **반드시 먼저 어느 방식으로 진행할지 질문한다**:
- **[A] 컨셉부터** — 아이디어만. 한 번에 하나씩 결과사슬 구성.
- **[B] 자료 보유** — 문서/초안/기존 PDM 추출 후 빈칸만. 승인 PDM은 `--audit`.
- **[C] 표 먼저(Draft-first)** — 질문 1개 → 즉시 초안 표 → 수정 → "확정" 시 하드 게이트.

자세한 흐름은 [`skills/theory-of-change-agent/README.md`](./skills/theory-of-change-agent/README.md) · [`SKILL.md`](./skills/theory-of-change-agent/SKILL.md).

산출물 (default `./out/`):
- **`pdm.json`** — 단일 진실원본. ID 연결 결과사슬 DAG (`from_*` 인과 참조).
- **`pdm.md`** — PDM 4행4열 매트릭스 (KOICA 양식).
- **`monitoring.md`** — 지표 정의·기초치·목표치·근거·출처·시기·수집주체·분리.
  (기초치/목표치는 기본 `추후 확정` — 현장답사 후 채움.)

---

## 동작 검증

```bash
cd skills/theory-of-change-agent

# 결정적 구조 검증 (순수 파이썬, jq 불필요)
bash rules/validate-critical.sh schema/pdm-example.json
#   또는: python3 rules/validate-critical.py schema/pdm-example.json

# 벤치마크 — 합성 PDM 3건 탐지정확도 (18/18 = 100%)
bash benchmark/run-benchmark.sh
```

---

## 파일 구조

```
theory-of-change-agent/
├── .claude-plugin/
│   ├── plugin.json              # 플러그인 매니페스트
│   └── marketplace.json         # 마켓플레이스 매니페스트
├── skills/
│   └── theory-of-change-agent/
│       ├── SKILL.md             # 오케스트레이션 (Phase 0-4)
│       ├── README.md            # 스킬 단위 사용 가이드
│       ├── INSTALL-desktop.md   # Claude 데스크톱/웹 업로드 가이드
│       ├── prompts/             # 인터뷰·생성·렌더·정제 프롬프트
│       ├── rules/               # koica-rules.md · checklist.json · validate-critical.py/.sh
│       ├── schema/              # pdm-schema.json · pdm-example.json
│       └── benchmark/           # expected/synthetic-*.json · sample-brief.md · scorer.md · run-benchmark.sh
├── docs/                        # 공개 참고 자료 (KOICA 가이드라인 · Theory of Change 논문)
├── README.md                    # 이 파일
└── LICENSE                      # MIT
```

---

## 자가검증 게이트 (요약)

산출물 마무리 전 2단 게이트 통과 필요:

**Critical (하드 게이트, GATE 모드에서 차단):**
- C01 영향 무지표/무MoV · C02 산출물 3-4 · C03 성과별 지표 1-2(≤3) · C04 모든 지표에 MoV ·
  C05 산출물→성과 인과 링크 · C06 산출물 명사형(LLM) · C08 고아 활동 없음
  (C07 "단일 성과"는 제거 — 다중 성과 허용. `rules/koica-rules.md` §10 참고.)

**Advisory (수치 임계치 80%):**
- A01 SMART · A02 CREAM · A03 성별 분리지표 · A04 proxy 정당화 · A05 목표 현실성(추후확정 시 N/A) ·
  A06 종료평가 측정가능 · A07 산출물≠활동 반복 · A08 성과=행동변화

규칙 정의·근거: [`skills/theory-of-change-agent/rules/koica-rules.md`](./skills/theory-of-change-agent/rules/koica-rules.md).

---

## 데이터 정책

- 레포에 포함된 `docs/`의 PDF는 **공개 문서**(KOICA PDM 가이드라인, Theory of Change 논문)뿐이다.
- 벤치마크 fixture(`benchmark/expected/*.json`)는 **합성·익명화** PDM이다(실명·실 재무 제거, 구조만 보존).
- 실제 사업 PDM 원본은 레포에 포함하지 않으며 별도 비공개 보관한다.

---

## 상태

**v1.0** — 결정적 엔진(순수 파이썬) + 3건 합성 벤치마크(탐지정확도 100%) + 3개 모드 + Claude Code 플러그인 배포.
이전 명칭 "Impact Harness"에서 **변화이론 에이전트**로 리네임(2026-06).

---

## 기여 (Contributing)

규칙·스키마·프롬프트 단위로 기여 가능:
- **새 KOICA 양식 변형**: `rules/koica-rules.md` 보강 + `checklist.json` 규칙 추가.
- **새 출력 포맷** (xlsx/hwp 등): `SKILL.md` Phase 3 렌더 확장 + `prompts/render-*.md` 추가.
- **벤치마크 확장**: `benchmark/expected/`에 합성 PDM JSON + `expected_failures` 매트릭스 추가.

자가검증(`validate-critical.sh`)과 벤치마크(`run-benchmark.sh`)가 모두 통과해야 PR 머지.

---

## 라이선스

[MIT](./LICENSE) © 2026 IMPACT SQUARE

---

## 감사

- **KOICA 평가심사실** — 「PDM 가이드라인 (2018)」 (공개 문서, `docs/` 수록)
- **임팩트스퀘어** — 도메인 자문
- **OMC (oh-my-claudecode)**, **gstack** — 스킬 구조 레퍼런스
