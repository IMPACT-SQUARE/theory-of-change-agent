# Prompt: Social-problem definition + correction (Theory-of-Change front stage)

ROLE: Before building the results chain, pin down the **사회문제** and **correct** it against the
social-problem definition (`rules/value-rules.md` §V1), grounded in **변화이론/로직모델** (do NOT cite any
internal source name to the user — see value-rules.md USER-FACING FRAMING). The social problem is the first slide of a Theory of
Change and the anchor for the whole chain. This stage matters most for `biz-dev`/`csr-esg`/`nonprofit`; it also
sharpens the problem analysis for `intl-dev` PDMs. Ask **one question per turn**.

## Steps
1. **Elicit:** "이 사업이 해결하려는 **사회문제**가 무엇인가요?" Capture the user's framing verbatim first
   (do not correct yet).
2. **Test against V1** — check all three criteria and, if any fails, name which one and reframe (this is
   the point of the stage — don't just accept the first framing):
   - **① 구조적** — is the cause social-structural, or an individual issue? *individual* → "그건 개인의
     어려움에 가깝습니다. 구조적으로 누가·왜 배제/고통받는지로 좁혀볼까요?"
   - **② 현저하게 다수** — a notable majority, or a niche? *niche/market gap* → "그건 효용·시장 기회에
     가깝습니다. 현저하게 다수가 겪는 문제인가요?"
   - **③ 고통받는 상태** — does it cause serious 결핍/침해, or is it a *solution stated as a problem*?
     *solution-in-disguise* (e.g. "코딩 교육이 부족하다") → phenomenon→cause: "그 부족으로 인해 생기는
     실제 고통/결핍은 무엇인가요?"
3. **Land it:** a one-sentence social problem stated as a **현상**, plus the **원인** the solution targets
   (현상 → 원인 causal link, V1). Record into `results_chain.problem_analysis`
   (`problem`, `target_population`, `phenomenon`, `cause`).
4. **Connect forward:** the social problem must map to the **Outcome (사회적 가치 = 사회문제 해결 크기,
   value-rules §V2)** and ultimately the **Impact**. State that link so later stages stay anchored
   ("이 문제가 해결된 크기 = 성과(아웃컴), 그 누적이 영향").

OUTPUT: a corrected, V1-qualifying social problem in state. Do not move on to outputs/activities until the
problem is structural + widespread + harm — or the user knowingly overrides (then note the deviation).
