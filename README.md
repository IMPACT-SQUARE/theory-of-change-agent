# 변화이론 에이전트 (Theory of Change Agent)

사업의 성과 구조를 **변화이론(Theory of Change)** 으로 잡아 주는 도구입니다. 대화하듯 질문에 답하면,
국제개발(KOICA) 사업이면 **PDM(Project Design Matrix, 성과체계표)** 을, 소셜벤처·사회공헌 같은 사업이면
**변화이론 도식**을 만들어 줍니다. 클로드 같은 AI 비서 위에서 동작합니다.

빈 표를 앞에 두고 무엇부터 채워야 할지 막막한 순간을 줄이는 것이 목표입니다.
한 번에 하나씩 묻는 질문에 답하다 보면, KOICA PDM 가이드라인에 맞는 표가 완성됩니다.
한국어로 답하면 결과도 한국어로, 영어로 답하면 영어로 나옵니다.

---

## 무엇을 도와주나요

- **변화이론(Theory of Change)** 의 흐름(투입물 → 활동 → 산출물 → 성과 → 영향)에 따라
  질문을 던지고, 답을 정리해 결과사슬을 함께 세워 줍니다.
- 다 만들고 나면 **PDM 표**와 **모니터링 표** 두 가지 문서를 만들어 줍니다.
- 마지막에 KOICA 가이드라인의 핵심 규칙을 지켰는지 **자동으로 점검**해 주기 때문에,
  자주 지적받는 실수를 미리 걸러낼 수 있습니다.

이런 분들에게 유용합니다.

- KOICA 사업에 지원하려고 PDM을 처음 써 보는 분
- 이미 초안이 있는데 가이드라인에 맞는지 확인받고 싶은 분
- 아이디어만 있고 아직 성과 구조가 잡히지 않은 분

---

## 어떻게 시작하나요

이 도구는 시작할 때 두 가지를 먼저 물어봅니다.

**(1) 무엇을 하려고 하나요?** 국제개발(KOICA) 사업이면 PDM을, 사업 개발(소셜벤처·사회공헌·비영리)이나
CSR·ESG 프로젝트면 변화이론 도식을 만들어 줍니다. (임팩트 투자심사용은 준비 중입니다.) 어느 쪽이든 뒤에서
돌아가는 논리는 같고, 마지막에 보여 주는 결과물의 모양만 다릅니다.

**(2) 어떻게 진행할까요?** 아래 세 가지 중에서 고르면 됩니다.

1. **컨셉부터 시작하기**

   아이디어만 있을 때 고릅니다. 문제와 목표부터 하나씩 짚어 가며 성과 구조를 함께 만듭니다.

2. **자료를 가지고 시작하기**

   사업 기획서, 초안, 기존 PDM 같은 자료가 있을 때 고릅니다.
   가진 내용을 읽어 들이고 비어 있는 부분만 채워 갑니다.
   이미 승인된 PDM이라면 고치지 않고 점검만 받을 수도 있습니다.

3. **표를 먼저 보고 고치기**

   질문 하나만 답하면 곧바로 PDM 초안 표를 만들어 줍니다.
   그 표를 보면서 원하는 부분을 고쳐 나가고, 마지막에 "확정"이라고 하면 품질 점검을 거쳐 마무리합니다.

세 방식은 함께 제공되며, 본인에게 편한 방식을 그때그때 고르면 됩니다.

---

## 무엇이 만들어지나요

작업이 끝나면 결과물이 파일로 저장됩니다.

- **PDM 표 (`pdm.md`)**: KOICA 양식 그대로, 영향 / 성과 / 산출물 / 활동을 가로 4칸(요약, 검증지표, 검증수단, 중요가정)으로 정리한 표입니다. 국제개발(KOICA) 사업의 기본 결과물입니다.
- **변화이론 도식 (`toc.md`)**: 활동에서 산출물로, 산출물에서 성과로 이어지는 연결을 그림(노드 다이어그램)으로 보여 줍니다. 사업 개발·CSR/ESG에서는 이 도식이 기본 결과물이고, 임팩트를 측정하려면 어떤 데이터를 직접 모아 둬야 하는지도 함께 알려 줍니다.
- **모니터링 표 (`monitoring.md`)**: 지표마다 정의, 기초치, 목표치, 근거, 자료 출처, 측정 시기, 수집 주체, 분리 기준을 정리한 표입니다.

기초치와 목표치는 보통 현장 답사와 자료 조사를 거쳐 정해지기 때문에, 처음에는 `추후 확정`으로 비워 둡니다.
나중에 값이 정해지면 그 자리에 채워 넣으면 됩니다.

파일은 이렇게 정리됩니다. **메인 결과(`pdm.md` 또는 `toc.md`)가 `out/` 바로 아래에 있어 폴더를 열면 바로 보이고**,
모니터링 표와 원본 데이터는 `out/details/` 안에 둡니다.

```
out/
├── pdm.md          (또는 toc.md)   ← 메인 결과
└── details/
    ├── monitoring.md
    └── pdm.json    (위 표들이 자동으로 만들어지는 원본 데이터)
```

---

## 품질 점검은 어떻게 하나요

마무리 직전에, 만들어진 PDM이 KOICA 가이드라인의 핵심 규칙을 지키는지 스스로 확인합니다. 예를 들면 이런 점들입니다.

- 영향(Impact)에는 별도의 지표를 넣지 않습니다.
- 산출물(Output)은 3~4개로 정리합니다.
- 성과당 지표는 1~2개(최대 3개)로 둡니다.
- 모든 지표에는 어떻게 측정할지(검증수단)가 적혀 있어야 합니다.
- 활동은 산출물로, 산출물은 성과로 빠짐없이 연결되어야 합니다.
- 성과는 양적 확대가 아니라 대상의 '행동 변화'로 표현합니다.

반드시 지켜야 하는 규칙은 통과할 때까지 함께 다듬은 뒤에 마무리하고,
권장 규칙(SMART, CREAM, 성별 분리지표 등)은 점수로 알려 줍니다.
규칙의 전체 목록과 가이드라인 쪽수 근거는 [`skills/theory-of-change-agent/rules/koica-rules.md`](./skills/theory-of-change-agent/rules/koica-rules.md)에 정리돼 있습니다.

---

## 설치하기

평소 **Claude 데스크톱 앱이나 웹(claude.ai)** 을 쓰신다면 **방법 3**을 보세요.
개발용 터미널 도구인 **Claude Code**에 익숙하시면 **방법 1**이 가장 편합니다.

### 방법 1. Claude Code 플러그인 (자동 업데이트, 권장)

Claude Code 안에서 아래 두 줄을 입력하면 설치됩니다.

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

나중에 최신 버전을 받고 싶을 때는 아래처럼 업데이트합니다.

```
/plugin marketplace update impact-square
/plugin update theory-of-change-agent
```

### 방법 2. 직접 연결하기 (빠른 설치)

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

업데이트는 `git pull`로 받습니다. 연결을 끊으려면 `rm ~/.claude/skills/theory-of-change-agent`를 입력합니다. 원본 폴더는 그대로 남습니다.

### 방법 3. Claude 데스크톱 / 웹(claude.ai)에 올리기

Claude Code가 아닌 데스크톱 앱이나 브라우저에서 쓰려면 스킬을 압축 파일(zip)로 만들어 올립니다.

1. **준비 사항**: 유료 요금제(Pro / Max / Team / Enterprise)와 **코드 실행(code execution) 기능 켜기**가 필요합니다.
2. **압축 파일 만들기**: 내려받은 폴더의 `skills` 폴더 안에서 아래 명령을 실행합니다.
   ```bash
   cd skills
   zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
3. **올리기**: 데스크톱 앱이나 claude.ai에서 `설정(Settings) → Capabilities → Skills → Upload`로 들어가
   방금 만든 `theory-of-change-agent.zip`을 선택하고 켜(Enable) 줍니다.
   (메뉴 이름은 버전에 따라 조금 다를 수 있으니, 설정 안에서 *Skills* 또는 *Capabilities* 항목을 찾으세요.)
4. **사용하기**: 채팅에 "변화이론 에이전트로 KOICA PDM 만들어줘"처럼 적으면 시작합니다.
   완성된 표(`pdm.md`, `monitoring.md`)는 채팅에 뜨는 다운로드 링크로 받습니다.

앱에 올린 스킬은 자동으로 업데이트되지 않습니다. 내용이 바뀌면 새 압축 파일을 다시 올려야 합니다.
자동 업데이트가 필요하면 방법 1을 사용하세요.

더 자세한 안내는 [`skills/theory-of-change-agent/INSTALL-desktop.md`](./skills/theory-of-change-agent/INSTALL-desktop.md)에 있습니다.

### 준비물

- **Claude** (Claude Code, 데스크톱 앱, 웹 중 무엇이든)
- **`python3`**: 품질 점검을 돌리는 데 쓰입니다. 데스크톱/웹의 코드 실행 환경에는 기본으로 들어 있습니다.

---

## 데이터 정책

- 이 저장소에 들어 있는 `docs/`의 PDF는 공개 문서(KOICA PDM 가이드라인, Theory of Change 자료)뿐입니다.
- 품질 점검용 예시 데이터(`benchmark/`)는 실명과 실제 금액을 모두 지운 가상의 PDM입니다. 구조만 남겨 두었습니다.
- 실제 사업 PDM 원본은 이 저장소에 넣지 않으며, 별도로 비공개 보관합니다.

---

## 폴더 구성

```
theory-of-change-agent/
├── .claude-plugin/      플러그인 설정 파일
├── skills/
│   └── theory-of-change-agent/
│       ├── SKILL.md         전체 진행 방식 설명
│       ├── README.md        스킬 단위 사용 안내
│       ├── INSTALL-desktop.md  데스크톱/웹 설치 안내
│       ├── prompts/         인터뷰와 문서 생성에 쓰는 안내문
│       ├── rules/           KOICA 규칙과 자동 점검 도구
│       ├── schema/          PDM 데이터 형식과 예시
│       └── benchmark/       품질 점검용 가상 예시
├── docs/                공개 참고 자료
├── README.md            이 문서
└── LICENSE              라이선스(MIT)
```

---

## 상태

버전 1.0입니다. 세 가지 진행 방식, 자동 품질 점검, Claude Code 플러그인 배포가 준비돼 있습니다.
이전 이름은 "Impact Harness"였고, 2026년 6월에 "변화이론 에이전트"로 이름을 바꿨습니다.

---

## 라이선스

[MIT](./LICENSE) © 2026 IMPACT SQUARE
