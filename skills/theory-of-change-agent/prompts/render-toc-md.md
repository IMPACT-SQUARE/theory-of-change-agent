# Prompt: Render toc.md (Theory-of-Change view + node diagram)

ROLE: Render `OUT/details/toc.json` into `OUT/toc.md` — the **Theory-of-Change (변화이론) view** used for the
ToC-view use-cases (`biz-dev`/`csr-esg`/`nonprofit`; and optionally alongside the PDM for `intl-dev`). Same underlying data
as the PDM; this view emphasizes the **causal flow and node connections** rather than the KOICA 4×4 form.
Render only what is in the JSON. Keep structural labels bilingual; write content in `meta.lang`.
**No KOICA mentions in the rendered ToC output** (임팩톨로지 feedback 2026-07-21): this view serves non-ODA
use-cases — never emit "KOICA 가이드라인" / rule ids / internal source names in `toc.md`; ground any advice
in 변화이론·로직모델 wording. **Also avoid ODA/logframe abbreviations (OVI, MoV) in ToC-view output** —
use plain 지표 / 확인 방법·자료 출처 (2026-07-21 pilot feedback). (KOICA references and standard
abbreviations belong to the intl-dev PDM/monitoring surfaces only.)

## Header block
```
# 변화이론 (Theory of Change) — {meta.project_name}
```
If `meta.use_case` is present, note it (e.g. `임팩트 스타트업/신규사업개발 (biz-dev)` / `사회공헌 (csr-esg)` / `비영리 (nonprofit)`).
**Mission linkage (org drill-down):** when `meta.org_context.mission` is non-null, add directly under the
header: `> 🧭 조직 미션: "{mission}" — 본 프로젝트는 이 미션에 기여합니다 (문서에서 추출, 참고용).`
(2026-07-21 pilot: 특정 프로젝트로 내려가면 상위 미션 연결이 사라진다는 피드백.)

## 1. Node diagram (Mermaid) — the heart of the view
**Draft gate (important):** if `meta.gate_mode = "DRAFT"` (a draft-first draft not yet finalized), do
**NOT** emit the Mermaid diagram yet — the chain is still being shaped. Instead show a short, friendly
placeholder in `meta.lang`, e.g. ko: `> 📊 변화이론 도식은 **확정(finalize) 후** 그려집니다. 내용을 다듬고
"확정"이라고 하면 이 자리에 도식이 나타납니다.` / en: `> 📊 The Theory-of-Change diagram is drawn **after
you finalize**. Refine the content and say "확정"/finalize to generate it here.` Emit the **full diagram
only when finalized** (`meta.gate_mode` is `GATE`, or `AUDIT` for an existing PDM).

When you DO draw it, emit a Mermaid `flowchart LR` built from the `from_*` causal links. What makes it a
*theory* is the connections: **사회문제 → 활동 → 산출물 → 성과(+지표) → 영향**. Show every edge; keep the
nodes prominent.

**Levels = INVISIBLE subgraphs whose titles are the column headers (2026-07-22, render-verified).**
Wrap each level's nodes in a `subgraph` carrying the bilingual level title, then make the BOX invisible:
`style SGn fill:none,stroke:none,color:#888,font-weight:bold` (mid-gray titles — they sit on the PAGE
background, which may be dark; #000 disappears on dark themes). The title sits above its own column and is
ATTACHED to it — it can never detach or drop to another row (the failure mode of the old disconnected
label chain). **VISIBLE level boxes remain banned** (2026-07-01 feedback: boxes hide the nodes) — style
the box away; only the title shows. Per-**outcome** groups nest INSIDE the 성과 level subgraph.

**Level header (대목록) — two complementary carriers (2026-07-22 final):**
1. **The bold markdown line DIRECTLY ABOVE the ```mermaid block** (always — gated by R04):
   `**사회문제 → 활동 (Activities) → 산출물 (Outputs) → 성과 (Outcomes) · 지표 → 영향 (Impact)**`
2. **In-diagram: the invisible level-subgraph titles** (column-attached, cannot detach — see above).
**Never a disconnected level-label node chain** (`:::lvl` — banned, R04): its position is
renderer-dependent (drops to the 2nd row on larger graphs), and `~~~` anchoring scatters the labels into
the graph body — both failure modes render-verified 2026-07-22.
Insert `투입물` after 사회문제 only when the 투입물 node is shown (intl-dev). Labels bilingual.

**Layout engine & ordering:** request **ELK** in the init directive (skeleton below). With ELK, columns
keep declaration order (활동 1..n renders 1..n top-to-bottom — render-verified). Where a viewer lacks ELK,
Mermaid falls back to dagre: the titles stay column-attached, but vertical order within a column may be
crossing-minimized — it is NOT semantic; the display numbers carry the order. Declare nodes and edges in
display-number order either way.

**Readability (임팩톨로지 feedback 2026-07-21 — small/invisible text in Antigravity dark theme):**
- **Pin the THEME, not just node colors** (2026-07-22 pilot: viewer dark themes made arrows white/
  invisible — edges inherit the theme unless pinned). Start the block with an init directive selecting
  ELK, `theme: base`, and explicit `lineColor` (#888 reads on light AND dark backgrounds):
  `%%{init: {"flowchart": {"defaultRenderer": "elk"}, "theme": "base", "themeVariables": {"fontSize": "16px", "lineColor": "#888", "primaryTextColor": "#000", "clusterBkg": "transparent", "clusterBorder": "#90a4ae", "edgeLabelBackground": "#ffffff"}}}%%`
- **Every `classDef` includes `color:#000`** (black text). The fills are light, so without an explicit
  color, dark-theme apps (Antigravity) render white-on-light = unreadable.
- Zoom / image-export buttons are NOT possible inside a markdown file — do NOT emit any external-tool
  workaround tip (user decision 2026-07-21: interactive zoom/download is deferred to the web version).

Node id: each `toc.json` id → Mermaid-safe (replace non-alphanumerics with `_`: `op-1`→`op_1`,
`ind-oc-1.1`→`ind_oc_1_1`). Label = the narrative text ONLY — **NO display numbers in diagram labels** (no `1.1`, `1-1`, `성과 1`;
2026-07-22: renderers may reorder rows within a column, and numbered labels then read as "순서가
틀렸다". The numbers live in §2/§3 and monitoring.md). Escape `"` in labels.
**Class assignment: inline `:::className` ONLY.** Never emit separate `class node1,node2 className`
statement lines — some renderers (Antigravity/Gemini markdown preview) mis-parse them into a stray
bottom node labeled "CLASS" (임팩톨로지 bug report 2026-07-21). `classDef` definition lines are fine.

**Nodes & classes:**
- **사회문제** — one node from `results_chain.problem_analysis` (현상 → 원인, value-rules §V1); class `problem`.
  It anchors the chain (its 해결 크기 = the Outcome, §V2).
- **활동 / 산출물 / 성과 / 영향** — one node each (activities include sub-activities); classes
  `act` / `out` / `outcome` / `impact`.
- **성과지표 (outcome indicators)** — each outcome and its indicators go inside a **small per-outcome
  `subgraph` with `direction TB`**, outcome node first, indicator nodes (class `ind`) linked `-.->` below
  it. This puts the 지표 **UNDER its outcome**, not in the impact column (임팩톨로지 feedback 2026-07-21 —
  previously the `-.->` link alone ranked indicators at the same depth as 영향). Give the subgraph an
  empty title (`[" "]`), a subtle style, and NEST it inside the 성과 level subgraph. (Under ELK the
  indicators may sit BESIDE the outcome within the dashed group — acceptable; the dagre fallback stacks
  them below.) Indicator label = the indicator NAME only (no `j-m` prefix); **NO
  baseline/target numbers**. (Output/activity indicators stay in §3 + monitoring; add only on request.)
- **투입물(Inputs)** — a node only when `meta.use_case = intl-dev` and `inputs` is present (§11.1); class
  `input`. Omit for `biz-dev`/`csr-esg`/`nonprofit`.

**Edges** (child→parent in data = upstream→downstream in the flow):
- 사회문제 → each top-level activity; 투입물(if shown) → each activity.
- activity `a` → output `o` for every `o` whose `from_activities` contains `a` (or a sub-id).
- output `o` → outcome `c` for every `c` whose `from_outputs` contains `o` (link to the outcome node
  inside its group — Mermaid allows edges into subgraph members).
- outcome `c` → impact (every outcome).
- outcome `c` **-.->** each of its indicator nodes (dashed = "measured by"), inside the group.

Skeleton (ELK + invisible level subgraphs; light fills + black text):
```
%%{init: {"flowchart": {"defaultRenderer": "elk"}, "theme": "base", "themeVariables": {"fontSize": "16px", "lineColor": "#888", "primaryTextColor": "#000", "clusterBkg": "transparent", "clusterBorder": "#90a4ae", "edgeLabelBackground": "#ffffff"}}}%%
flowchart LR
  classDef problem fill:#fdecea,stroke:#e57373,color:#000;
  classDef act fill:#fff3e0,stroke:#ffb74d,color:#000;
  classDef out fill:#e8f5e9,stroke:#81c784,color:#000;
  classDef outcome fill:#e3f2fd,stroke:#64b5f6,color:#000;
  classDef ind fill:#f5f5f5,stroke:#bdbdbd,color:#000;
  classDef impact fill:#ede7f6,stroke:#9575cd,color:#000;
  subgraph SG0 ["사회문제"]
    prob(["사회문제: …"]):::problem
  end
  subgraph SG1 ["활동 (Activities)"]
    act_1["활동 서술 …"]:::act
  end
  subgraph SG2 ["산출물 (Outputs)"]
    op_1["산출물 서술 …"]:::out
  end
  subgraph SG3 ["성과 (Outcomes) · 지표"]
    subgraph oc_g1 [" "]
      direction TB
      oc_1["성과 서술 …"]:::outcome
      ind_oc_1_1("지표명"):::ind
      oc_1 -.-> ind_oc_1_1
    end
  end
  subgraph SG4 ["영향 (Impact)"]
    imp_1["영향 …"]:::impact
  end
  prob --> act_1
  act_1 --> op_1
  op_1 --> oc_1
  oc_1 --> imp_1
  style SG0 fill:none,stroke:none,color:#888,font-weight:bold
  style SG1 fill:none,stroke:none,color:#888,font-weight:bold
  style SG2 fill:none,stroke:none,color:#888,font-weight:bold
  style SG3 fill:none,stroke:none,color:#888,font-weight:bold
  style SG4 fill:none,stroke:none,color:#888,font-weight:bold
  style oc_g1 fill:transparent,stroke:#90caf9,stroke-dasharray:4
```

### 1b. Text fallback (ALWAYS emit right below the Mermaid block, when drawn)
Some viewers don't render Mermaid (e.g. **Antigravity / VS Code without the Mermaid preview extension** — see
README "Antigravity"). So directly under the ```mermaid``` block, also emit a **renderer-independent ASCII
causal flow** in a plain (no-language) fenced block, built from the **same `from_*` links** — identical
content, never a reduced version. This guarantees the theory is visible everywhere. Format: one line per
chain, left→right with `→`, outcome indicators in `[ ]`, one indented `└─` branch when an output feeds
multiple outcomes. Example:
```
사회문제: 산모 사망 → [산전관리 교육] → [교육 이수] → (시설분만 실천 ↑) → 영향: 모자보건 개선
                                                          └ 지표: [시설분만율]
```
Keep it compact; every node and edge in the Mermaid diagram must also appear here.

### 1c. toc.html — the designed document view (ALWAYS write alongside, 2026-07-22 v2)
Markdown previews render with whatever Mermaid the viewer bundles (old = scrambled order / bad theming),
and md can't be styled. So ALSO write **`OUT/toc.html`** — a **full, designed document** mirroring ALL of
toc.md's content (not just the diagram; pilot feedback: "도식만 있으니 이상하다"), with the renderer pinned
inside the file (Mermaid 11 + ELK from CDN). No toolbar/buttons (removed by user decision — browser zoom
and Cmd/Ctrl+P cover it). `toc.md` stays the plain-text source view; internet is needed on first open.

Fill the placeholders; the Mermaid at `{MERMAID}` MUST be byte-identical to §1's block (init included).
Convert the §2/§3/§4 content into the markup patterns shown — keep the CSS exactly as given:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>변화이론 — {PROJECT}</title>
<style>
  :root { --ink:#1c1917; --muted:#78716c; --line:#e7e5e4; --soft:#fafaf9;
          --blue:#2f6fb3; --green:#2e7d5b; --amber:#b45309; }
  * { box-sizing: border-box; }
  body { font-family:-apple-system,BlinkMacSystemFont,"Pretendard","Apple SD Gothic Neo","Noto Sans KR",sans-serif;
         margin:0; color:var(--ink); background:#fff; line-height:1.65; }
  .page { max-width:1080px; margin:0 auto; padding:48px 32px 80px; }
  header.doc { border-bottom:2px solid var(--ink); padding-bottom:20px; margin-bottom:8px; }
  .kicker { font-size:13px; letter-spacing:.12em; color:var(--muted); text-transform:uppercase; margin-bottom:6px; }
  h1 { font-size:30px; line-height:1.3; margin:0 0 10px; font-weight:700; }
  .meta { font-size:13.5px; color:var(--muted); display:flex; gap:14px; flex-wrap:wrap; }
  .chip { border:1px solid var(--line); border-radius:999px; padding:2px 12px; background:var(--soft); }
  .mission { margin:22px 0 0; padding:14px 18px; background:var(--soft); border-left:3px solid var(--blue);
             border-radius:0 8px 8px 0; font-size:15px; }
  .mission b { color:var(--blue); }
  section { margin-top:44px; }
  h2 { font-size:20px; margin:0 0 4px; display:flex; align-items:baseline; gap:10px; }
  h2 .no { color:var(--muted); font-size:15px; font-weight:600; }
  .h2sub { color:var(--muted); font-size:13.5px; margin:0 0 16px; }
  .flowline { font-size:13.5px; font-weight:600; color:var(--muted); margin:0 0 10px; letter-spacing:.01em; }
  .diagram { border:1px solid var(--line); border-radius:12px; padding:18px 14px; overflow-x:auto; background:#fff; }
  .levels { display:grid; gap:14px; }
  .level { display:grid; grid-template-columns:130px 1fr; gap:14px; padding:14px 0; border-bottom:1px solid var(--line); }
  .level:last-child { border-bottom:none; }
  .lvname { font-weight:700; font-size:14px; }
  .lvname .en { display:block; font-weight:500; color:var(--muted); font-size:12px; }
  .lvbody { font-size:14.5px; }
  .lvbody ul { margin:0; padding-left:18px; }
  .lvbody li { margin:3px 0; }
  .ind { color:var(--muted); font-size:13px; }
  table { width:100%; border-collapse:collapse; font-size:13.5px; margin-top:6px; }
  th { text-align:left; background:var(--soft); border-bottom:1.5px solid var(--line); padding:9px 10px;
       font-size:12.5px; color:var(--muted); white-space:nowrap; }
  td { border-bottom:1px solid var(--line); padding:9px 10px; vertical-align:top; }
  .badge { display:inline-block; border-radius:6px; padding:1px 8px; font-size:12px; font-weight:600; white-space:nowrap; }
  .b-track { background:#fef3c7; color:var(--amber); }
  .b-auto  { background:#d1fae5; color:var(--green); }
  .verify p { margin:0 0 10px; font-size:14px; }
  .verify .label { font-weight:700; }
  .note { font-size:13px; color:var(--muted); margin-top:14px; }
  footer { margin-top:64px; padding-top:16px; border-top:1px solid var(--line); font-size:12.5px; color:var(--muted); }
  @media print { .page { padding:0 } .diagram { border:none } section { break-inside:avoid } }
</style>
</head>
<body>
<div class="page">
<header class="doc">
  <div class="kicker">Theory of Change</div>
  <h1>{PROJECT}</h1>
  <div class="meta"><span class="chip">{USE_CASE_LABEL}</span><span>{CREATED} · v{VERSION} · {GATE_LABEL}</span></div>
  {MISSION_BLOCK: only when meta.org_context.mission →
  <div class="mission"><b>🧭 미션</b> — {mission} <span style="color:var(--muted)">(문서에서 추출, 참고용)</span></div>}
</header>
<section>
  <h2><span class="no">1</span>변화이론 도식</h2>
  <p class="h2sub">활동에서 영향까지의 인과 연결 — 화살표가 곧 이 사업의 논리입니다.</p>
  <p class="flowline">사회문제 → 활동 (Activities) → 산출물 (Outputs) → 성과 (Outcomes) · 지표 → 영향 (Impact)</p>
  <div class="diagram"><pre class="mermaid">
{MERMAID}
  </pre></div>
</section>
<section>
  <h2><span class="no">2</span>변화 경로</h2>
  <p class="h2sub">각 층위의 내용과 지표</p>
  <div class="levels">
    {LEVEL_ROWS: one per level (사회문제/활동/산출물/성과/영향), pattern →
    <div class="level"><div class="lvname">성과<span class="en">Outcomes</span></div>
      <div class="lvbody"><ul><li><b>성과 1</b> {narrative} <span class="ind">지표 {j-m} {이름}</span></li></ul></div></div>}
  </div>
</section>
<section>
  <h2><span class="no">3</span>측정 준비 — 직접 수집해야 할 데이터</h2>
  <p class="h2sub">임팩트를 나중에 입증하려면 지금부터 모아야 하는 데이터입니다.</p>
  <table>
    <thead><tr><th>지표</th><th>지표 정의</th><th>측정 대상</th><th>측정방법·산출식</th><th>언제</th><th>수집</th></tr></thead>
    <tbody>{MEASUREMENT_ROWS: outcome indicators first; 수집 cell =
      <span class="badge b-track">직접 트래킹</span> or <span class="badge b-auto">운영데이터</span>}</tbody>
  </table>
  <p class="note">착수 전(또는 초기)에 성과 지표의 기초선을 반드시 측정해 두어야 종료 시점에 변화를 입증할 수 있습니다.</p>
</section>
<section>
  <h2><span class="no">4</span>검증</h2>
  <p class="h2sub">논리 검증(원인 회복 여부) · IRIS+ 유사 지표(참고용)</p>
  <div class="verify">{VERIFY_ITEMS: plain paragraphs, NO icons/cards/color decoration →
    <p><span class="label">성과 1 — 부합.</span> {요지}</p>
    <p><span class="label">성과 2 — 교정 필요.</span> {사유와 제안}</p>
    <p><span class="label">IRIS+ 유사 지표.</span> {제안} (참고용 · 공식 매핑 아님 · IRIS+ © GIIN)</p>}</div>
</section>
<footer>변화이론 에이전트(Theory of Change Agent)로 생성 · 원본 데이터: details/toc.json · 이 문서의 도식은 내장 렌더러로 항상 동일하게 표시됩니다</footer>
</div>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
import elkLayouts from "https://cdn.jsdelivr.net/npm/@mermaid-js/layout-elk@0/dist/mermaid-layout-elk.esm.min.mjs";
mermaid.registerLayoutLoaders(elkLayouts);
mermaid.initialize({ startOnLoad: true });
</script>
</body>
</html>
```
Rules: no extra libraries beyond the two pinned CDN imports; no toolbar/buttons; keep the CSS verbatim
(it is the design system); DRAFT gate applies (no diagram/doc until finalized); ToC-view language rules
apply (no KOICA/OVI/MoV). Closing summary tells the user: `toc.html`을 브라우저로 열면 항상 같은 모습
(순서·색 보장)이며, `toc.md`는 텍스트 원본.

## 2. Narrative ToC (level by level)
**Rendered heading: 「변화 경로」** (2026-07-22 — "서사형 변화이론" replaced; en: *Change Pathway*).
Top→bottom: **사회문제 → 투입물(있을 때) → 활동 → 산출물 → 성과 → 영향**. For each level list the items with
their narratives. For 성과/산출물, show indicators by name only (NO baseline/target numbers — those live in
the monitoring view and default to `추후 확정`). Use the dotted/dash display numbering from
`render-pdm-md.md` (output `j.k`, output indicator `j.k.m`, outcome indicator `j-m`).

## 3. 측정 준비 — 직접 수집해야 할 데이터 (Measurement readiness)
The most useful insight for a ToC-view (`biz-dev`/`csr-esg`/`nonprofit`) user is: *"to measure your impact later, you must
collect THESE data."* The agent cannot collect these for the user, so make the to-do explicit. Build this
section **only from existing indicator fields** (`name`, `definition`, `measurement_target`, `formula`,
`data_source`, `timing`, `collector`, `baseline`) — do not invent indicators.

For every output and outcome indicator, list a row (this mirrors the 사회공헌 지표 DB: 지표명 · 지표 정의 ·
측정 대상 · 측정방법):
- **지표** (name) · **지표 정의** (definition) · **측정 대상** (measurement_target, `-` if null) ·
  **측정방법·산출식** (formula — the 사회공헌 지표 DB style: a short 측정방법 문장/식 such as `(사후 평균) − (사전 평균)`
  or `해당 기간 … 인원 수`; `-` if qualitative) · **무엇을/어디서** (data_source) · **언제** (timing) · **누가**
  (collector).
- Mark **"직접 트래킹 필요"** when the data is not an operational by-product the team already has — i.e.
  survey / interview / FGD / assessment / 평가-based, or `collector` is the project team. Mark
  **"운영데이터(자동 확보)"** when it falls out of normal operations (e.g. 보급/판매 로그, 가입 로그).
  *(Example: 보급 대수 = 운영데이터; 교육 이수자 수·만족도·역량 평가 = 직접 트래킹 필요.)*
- Because `baseline` defaults to `추후 확정`, add a reminder in plain language: **착수 전(또는 초기)에
  기초선(baseline)을 측정해 두어야** 종료 시 변화를 입증할 수 있다. *(No KOICA/rule-id citation in the
  rendered text — see the no-KOICA rule above.)*

Render as a short table or checklist, ordered outcome-first (outcome indicators are the hardest and most
important to track).

## 4. 검증 (Verification)
- **논리 검증:** emit the FINAL per-outcome verdicts from SKILL step 7b (which ran before this render and
  already applied confirmed corrections to `toc.json`): `✅ 부합`, **`✅ (교정 반영: "이전 지표" → "새 지표")`**
  for fixed Type-A findings, or `⚠️` only where the user chose to keep as-is / for open Type-B decisions.
  In `meta.lang`, grounded in 변화이론·로직모델. The verdicts must describe the CURRENT (post-correction)
  indicators — never critique an indicator that no longer exists in the data.
- **IRIS+ 유사 지표 (implemented):** run `prompts/iris-match.md` for each **outcome** indicator — it distills
  English keywords, calls `python3 <SKILL_ROOT>/rules/iris-search.py --json --top 6 "…"` (deterministic
  search over the 593-metric IRIS+ catalog; use the skill root, NOT a CWD-relative path — see
  iris-match.md step 2), and suggests the nearest metric(s) **from the returned shortlist only**, tagged
  "참고용 · 공식 매핑 아님 · IRIS+ © GIIN". Show "IRIS+ 유사 지표 매칭 준비 중" ONLY on a genuine exit 3
  (catalog absent); a command-not-found is a path problem — retry with the right path. **NEVER invent an
  IRIS+ code**.

## Fidelity checks (must hold)
- **DRAFT (`gate_mode=DRAFT`): §1 is the "확정 후 출력" placeholder, NOT a Mermaid diagram.** The full
  diagram appears only once finalized (`gate_mode` GATE/AUDIT).
- When drawn: every activity/output/outcome/impact in `toc.json` appears as a node; every `from_*` link
  appears as an edge (no silent drops, no invented edges).
- **When drawn, the §1b text fallback is ALSO emitted** (plain fenced block) with the same nodes/edges — so
  the flow is visible in viewers without Mermaid (Antigravity).
- **Measurement tables (§3, monitoring) carry `지표 정의` and `산출식`** (formula `-` when qualitative); the
  §3 사회공헌 table also carries `측정 대상` (`-` when null / for intl-dev).
- **Level subgraphs present and INVISIBLE** (`fill:none,stroke:none` — titles show, boxes don't); no
  VISIBLE level boxes; per-outcome groups nested inside the 성과 subgraph.
- **The bold 대목록 line sits directly above the ```mermaid block; NO level-node chain inside the
  diagram**; every `classDef` carries `color:#000`.
- **No external-tool tip lines** (mermaid.live etc.) in the output.
- **`toc.html` written alongside `toc.md`** (GATE/AUDIT only), Mermaid code identical to §1.
- Each **outcome's indicators sit BELOW it inside its TB group** (`-.->`); no baseline/target numbers in
  the diagram.
- **`toc.md` contains no "KOICA" mention** (labels, notes, citations — none).
- **No `class …` statement lines in the Mermaid block** — only inline `:::` (stray-"CLASS"-node bug).
- Mermaid node ids are unique and contain only `[A-Za-z0-9_]`.
- For `biz-dev`/`csr-esg`/`nonprofit`: no 수원기관/투입물 nodes are forced in.
