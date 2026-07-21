# 변화이론 에이전트

[English](README.md) · 한국어 · [日本語](README.ja.md) · [Tiếng Việt](README.vi.md)

사업의 문제와 해법은 분명하지만, PDM 문장과 지표로 정리하기 어려울 수 있습니다.
변화이론 에이전트가 질문을 통해 결과사슬을 정리해 줍니다.

질문에 하나씩 답하면 사회문제부터 활동, 산출물, 성과, 영향까지 결과사슬이 만들어집니다.
국제개발협력 사업에는 PDM(성과체계표)을, 임팩트 스타트업·CSR·비영리에는 변화이론 도식을 제공합니다.
Claude 같은 AI 환경에서 사용할 수 있고, 대화한 언어로 답합니다.

## 이럴 때 쓰세요

- 국제개발협력 사업의 PDM을 처음 작성할 때
- 제출 전 초안을 가이드라인에 맞춰 점검할 때
- 사업 아이디어를 임팩트 논리로 정리할 때

## 빠른 시작

1. 아래 방법으로 스킬을 설치하세요.
2. 채팅에 `변화이론 에이전트로 PDM 만들어줘`라고 입력하세요. 사업계획서나 연차보고서를 함께 올려도 됩니다.
3. 질문에 답하세요. 결과가 맞으면 `확정`이라고 입력하세요.
4. `out/`에서 결과를 확인하세요. 국제개발협력은 `pdm.md`, 그 밖의 용도는 `toc.md`로 저장됩니다.

## 용도별 결과물

| 할 일 | 결과물 | 준비하면 좋은 자료 |
|---|---|---|
| 국제개발협력 사업 | PDM | 아이디어, 제안서, 기존 PDM |
| 임팩트 스타트업·신규사업 | 변화이론 도식 | 사업계획서 또는 해결하려는 문제 |
| CSR·ESG 사업 | 변화이론 도식 | 사업 개요서 또는 제안서 |
| 비영리 프로그램 | 변화이론 도식 | 연차보고서 또는 프로그램 자료 |

새 PDM은 확정하기 전에 구조를 검사합니다. 이미 승인된 PDM은 감사 모드로 확인하세요.
문서는 바꾸지 않고, 가이드라인과 다른 부분만 알려 줍니다.

## 대화 예시

```
나:      변화이론 에이전트로 PDM 만들어줘.
에이전트: 어떤 사업인가요?
         ① 국제개발협력(PDM)  ② 임팩트 스타트업
         ③ CSR·ESG            ④ 비영리
나:      ① 라오스 모자보건 사업이야.
에이전트: 이 사업이 해결하려는 문제는 무엇인가요? 누가 어떤 어려움을 겪고 있나요?
나:      농촌 산모들이 집에서 분만해. 보건소가 멀고 믿지 못하기도 해.
에이전트: 핵심 문제는 높은 가정분만율이고, 원인은 시설 접근성과 신뢰 부족으로 보입니다.
         그러면 성과는 "시설분만을 선택하는 산모가 늘어난다"처럼 써 볼 수 있습니다.
         "교육 횟수를 늘린다"는 활동 또는 산출물에 가깝습니다. 이 방향이 맞을까요?
         …
나:      확정
에이전트: ✔ 핵심 규칙 8개를 통과했습니다.
         ⚠ 성과 2의 "교육 확대"는 횟수를 말합니다. 행동 변화를 나타내도록 수정해 보세요.
         최종 결과: out/pdm.md
```

## 작동 방식

인터뷰하고, 결과사슬을 만들고, 검토한 뒤 결과물을 생성합니다.

먼저 구조적이고 다수에게 실제 피해를 주는 사회문제를 정의합니다. 이어서 현상과 원인을 구분하고,
원인을 줄이는 상태 변화를 성과로 정리합니다. 활동의 확대나 포괄적인 기대효과는 성과와 구분합니다.

연차보고서처럼 여러 프로젝트를 담은 자료라면 조직 전체의 구조를 볼지, 특정 프로젝트 하나를
선택할지 먼저 묻습니다.

| 파일 | 내용 |
|---|---|
| `pdm.md` | 4×4 PDM 매트릭스 |
| `toc.md` | Mermaid 미지원 환경에서도 읽을 수 있는 텍스트 흐름을 포함한 변화이론 도식 |
| `details/monitoring.md` | 지표 정의, 산식, 기초치, 목표치, 출처, 수집 시기와 담당을 담은 측정 계획 |
| `budget.md` | 활동별 세목, 산출근거, 재원 분담, 연차 합계를 담은 예산서. 선택 사항 |
| `details/toc.json` | 각 결과물을 생성하는 원본 데이터 |

대화로 시작하거나 PDF, 한글 파일(`.hwp`, `.hwpx`)을 올릴 수 있습니다. 한글 파일 추출기는 외부
라이브러리 없이 동작합니다.

## 확인 가능한 검증

- 결정적 품질 게이트: 순수 Python으로 핵심 구조 규칙 8개를 검사합니다. 영향 지표 금지,
  산출물 3개에서 4개, 검증수단 필수, 고아 노드 금지 등이 포함됩니다. [벤치마크](./skills/theory-of-change-agent/benchmark/)에서는 18개 위반을 모두 찾아냈습니다.
- 성과 검토: 성과가 원인을 다루는 변화인지 확인하고, 성과 지표는 IRIS+ 593개 지표 중 가까운 항목을 참고용으로 제안합니다. 공식 매핑은 아닙니다.
- 예산 계산: 합계, 비율, 재원 분담, 일반관리비 상한은 스크립트가 계산하고 검증합니다. 실제 예산서로 검증을 마쳤습니다.
- 권장 규칙: SMART, CREAM, 성별 분리 지표는 점수로만 알려 드립니다. 적용 여부는 사용자가 결정합니다.

## 설치

준비물은 Claude Code, Claude 데스크톱 또는 claude.ai와 `python3`입니다. 데스크톱과 웹의 코드 실행 환경에는 Python이 포함되어 있습니다.

### 가장 쉬운 방법: Claude Code에 아래를 붙여넣기

Claude Code를 열고 아래 문단을 그대로 붙여넣으세요. 나머지는 Claude가 알아서 합니다.

> 변화이론 에이전트 설치: `git clone --single-branch --depth 1 https://github.com/IMPACT-SQUARE/theory-of-change-agent.git ~/.claude/theory-of-change-agent && ln -snf ~/.claude/theory-of-change-agent/skills/theory-of-change-agent ~/.claude/skills/theory-of-change-agent` 를 실행하고, `~/.claude/skills/theory-of-change-agent/SKILL.md` 파일이 있는지 확인한 다음, "변화이론 에이전트로 PDM 만들어줘"라고 하면 시작할 수 있다는 것과, 업데이트는 `git -C ~/.claude/theory-of-change-agent pull` 로 하면 된다는 것을 알려줘.

### Claude Code

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

업데이트는 `/plugin update theory-of-change-agent`로 합니다.

### Claude 데스크톱, Antigravity, claude.ai

1. 스킬을 압축하거나 제공된 `theory-of-change-agent.zip`을 사용합니다.
   ```bash
   cd skills && zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
2. Claude 데스크톱의 `Settings → Skills → Add → Upload`, Antigravity의 Skills 화면, 또는 claude.ai의 `Settings → Capabilities → Skills → Upload`에서 업로드합니다. 코드 실행이 가능한 유료 플랜이 필요합니다.
3. 채팅에 `변화이론 에이전트로 PDM 만들어줘`라고 입력합니다.

> 앱에 올린 스킬은 자동으로 업데이트되지 않습니다. 변경 뒤에는 새 zip 파일을 다시 올리세요.
> Antigravity에서 Mermaid 도식이 코드로 보이면 Open VSX의 `bierner.markdown-mermaid`를 설치하거나,
> 함께 생성되는 텍스트 흐름을 확인하세요. 자세한 내용은 [INSTALL-desktop.md](./skills/theory-of-change-agent/INSTALL-desktop.md)에서 볼 수 있습니다.

### Git

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

## 데이터 정책

- `docs/`에는 변화이론 참고자료 등 공개 문서만 있습니다.
- `benchmark/`의 PDM은 가상 사례입니다. 실제 이름과 금액은 포함하지 않습니다.
- 실제 사업의 PDM과 예산 원본은 이 저장소에 저장하지 않습니다.

## 상태

버전 1.0은 국제개발협력, 임팩트 스타트업, CSR·ESG, 비영리를 지원합니다. 세 가지 진행 방식,
품질 게이트, 예산 기능, HWP 입력, 플러그인 배포를 포함합니다. 임팩트 투자 심사 기능은 준비 중입니다.

## 라이선스

[MIT](./LICENSE) © 2026 IMPACT SQUARE.
