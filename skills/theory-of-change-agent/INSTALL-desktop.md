# 변화이론 에이전트 (Theory of Change Agent) — Claude 데스크톱 / Claude.ai 설치 가이드

이 스킬은 Anthropic **Agent Skills** 표준 포맷이라 Claude Code뿐 아니라 **Claude 데스크톱 앱**과
**claude.ai**에서도 쓸 수 있습니다. 결정적 게이트는 `jq` 없이 **순수 파이썬**(`rules/validate-critical.py`)으로
돌아가므로, 코드 실행 샌드박스에서 그대로 동작합니다.

---

## 0. 전제 조건

- **유료 플랜**: Pro / Max / Team / Enterprise 중 하나.
- **코드 실행(code execution / Analysis) 기능 ON** — 스킬의 검증 스크립트가 샌드박스에서 실행됩니다.
  - 설정 위치(버전에 따라 명칭 다를 수 있음): `Settings → Capabilities`(또는 `Features`) → **Code execution** 켜기.
- 스킬 기능(Skills)이 계정에서 활성화되어 있어야 합니다.

> ⚠️ 메뉴 명칭/위치는 앱 버전에 따라 바뀔 수 있습니다. 아래는 일반적인 경로이며, 정확한 위치는
> `Settings` 안의 **Skills / Capabilities** 항목을 찾으세요.

---

## 1. 패키지(.zip) 준비

배포용 zip을 직접 만들려면 레포 루트에서:

```bash
cd skills
zip -r theory-of-change-agent.zip theory-of-change-agent \
  -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
```

- `theory-of-change-agent.zip` 안에 `theory-of-change-agent/SKILL.md`가 들어가야 합니다(폴더째 압축).
- `out/`(예전 샘플 산출물)은 제외 — 스킬이 실행 시 새로 생성합니다.
- **IRIS+ 매칭 데이터(`rules/iris-metrics.json`)** 는 이제 레포에 포함되어(출처: IRIS+ © GIIN, 무료
  재배포·출처 표기 조건) zip·플러그인 어느 경로로 설치해도 IRIS+ 유사 지표 매칭이 바로 동작합니다.
- 이미 만들어진 zip을 받았다면 이 단계는 건너뜁니다.

---

## 2. 앱에 업로드 (zip)

쓰는 앱에 맞춰 `theory-of-change-agent.zip`을 업로드합니다.

- **Claude 데스크톱**: `Settings → Skills → Add → Upload` 에서 `theory-of-change-agent.zip` 선택 → 목록에서 **Enable**.
- **Antigravity**: Skills 화면에서 `theory-of-change-agent.zip` 을 업로드.
- **claude.ai(웹)**: `Settings → Capabilities → Skills → Upload`.

업로드 후 **Code execution이 켜져 있는지** 확인하세요(품질 점검이 python3로 돕니다). 메뉴 이름은 앱/버전에 따라 조금 다를 수 있으니, 설정 안에서 *Skills* 항목을 찾으면 됩니다.

> **Antigravity 팁 — 결과 파일이 클릭·미리보기로 뜨게 하려면:** 채팅만 열지 말고 **프로젝트 폴더를 연
> 상태(워크스페이스)에서 실행**하세요. 폴더 없이 실행하면 산출물이 Antigravity 스크래치 경로
> (`~/.gemini/antigravity/scratch/…`)에 생성되어 미리보기 카드가 뜨지 않고 경로 텍스트만 남습니다.
>
> **변화이론 도식(Mermaid)이 Antigravity에서 코드처럼 보이면:** Open VSX에서 **`Markdown Preview Mermaid Support`**(`bierner.markdown-mermaid`) 확장을 설치하면 `toc.md`가 그림으로 렌더됩니다. 설치 없이도 스킬이 도식 아래에 **텍스트 인과 흐름**을 함께 출력하므로 논리 흐름은 그대로 읽을 수 있습니다. (루트 `README.md` 방법 3 참고.)

---

## 2b. 업데이트 (2026-07 기준)

- **Desktop 플러그인 설치**(Customize → Plugins → Browse에서 설치): 자동 업데이트 없음 —
  **Customize → Plugins → 해당 마켓플레이스의 "Update" 버튼**으로 수동 갱신.
- **zip 업로드**: 자동 업데이트 없음 — 새 zip 재업로드.
- **자동 업데이트가 필요하면**: ① Claude Code 플러그인(마켓플레이스 autoUpdate 지원), 또는
  ② **Team/Enterprise 조직 관리형 마켓플레이스** — 관리자가 GitHub 레포를 등록하면 main 머지마다
  팀 전원에게 자동 동기화(≤30분).

---

## 3. 사용법

채팅에서 자연스럽게 호출하면 됩니다(스킬 설명의 트리거 키워드로 자동 활성화):

```
KOICA PDM 초안 하나 만들어줘.
변화이론 에이전트로 우리 사업 PDM 좀 잡아줘.
결과물 먼저 보여주는 방식(draft-first)으로 PDM 그려줘.
```

- 입력 언어를 따라 출력 언어가 정해집니다(한글 입력 → 한글 산출).
- 인터뷰가 끝나면 샌드박스에 **`pdm.md`**(PDM 매트릭스), **`monitoring.md`**(모니터링 매트릭스),
  **`toc.json`**(원본)이 생성됩니다 → 채팅의 **다운로드 링크**로 받으세요.
- 세 모드:
  - **컨셉부터(A)** — 아이디어만 있을 때, 한 번에 하나씩 인터뷰.
  - **자료 보유(B)** — 문서/초안/기존 PDM 첨부 후 빈칸만. 승인 PDM은 감사(보고 전용).
  - **결과물 먼저(C, Draft-first)** — 질문 1개 → 즉시 초안 결과물 → 수정 → "확정" 시 게이트.

---

## 4. Claude Code와 다른 점 (참고)

| | Claude Code | Claude 데스크톱 / claude.ai |
|---|---|---|
| 실행 위치 | 로컬 셸·파일시스템 | 코드 실행 **샌드박스** |
| 결과 파일 | 작업 폴더에 저장 | 샌드박스 생성 → **다운로드** |
| 선택지 질문 | `AskUserQuestion` | `ask_user_input_v0` (이름만 다르고 동일 역할 — 탭 선택 UI). Antigravity/Gemini는 `ask_user`; 없으면 번호 메뉴 텍스트로 폴백 |
| 검증기 | `python3`(jq 불필요) | `python3`(샌드박스 기본 제공) |

---

## 5. 트러블슈팅

- **스킬이 안 불려요** → 메시지에 `변화이론 에이전트`, `PDM`, `KOICA`, `theory of change` 같은 키워드를 포함하거나,
  "theory-of-change-agent 스킬로 …"라고 직접 지정하세요.
- **검증 단계에서 에러** → 코드 실행 기능이 켜져 있는지 확인. (게이트는 `python3`만 필요하며 샌드박스에 기본 포함)
- **파일을 못 받겠어요** → 산출물은 샌드박스에 생성되며 채팅 메시지의 다운로드 링크로 제공됩니다.
- **jq 관련 메시지** → 런타임에는 jq가 필요 없습니다. jq는 개발용 벤치마크 스크립트에서만 쓰입니다.

---

## 6. 대안 설치 경로

- **Claude Code(로컬)**: `ln -s <repo>/skills/theory-of-change-agent ~/.claude/skills/theory-of-change-agent`
  (README의 "빠른 시작" 참고).
- **API / Console**: Agent Skills를 API로 업로드해 Console·에이전트에서 사용(코드 실행 도구 필요).
