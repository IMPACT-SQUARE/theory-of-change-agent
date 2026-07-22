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
`ind-oc-1.1`→`ind_oc_1_1`). Label = the narrative (display-number prefix optional). Escape `"` in labels.
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
  them below.) Indicator label = name with its `j-m` number; **NO
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
    act_1["1.1 …"]:::act
  end
  subgraph SG2 ["산출물 (Outputs)"]
    op_1["1.1 …"]:::out
  end
  subgraph SG3 ["성과 (Outcomes) · 지표"]
    subgraph oc_g1 [" "]
      direction TB
      oc_1["성과 1 …"]:::outcome
      ind_oc_1_1("1-1 지표명"):::ind
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
사회문제: 산모 사망 → [활동 1.1 산전관리 교육] → [산출물 1.1 교육 이수] → (성과 1 시설분만 실천 ↑) → 영향: 모자보건 개선
                                                                          └ 지표: [1-1 시설분만율]
```
Keep it compact; every node and edge in the Mermaid diagram must also appear here.

### 1c. toc.html — guaranteed-rendering diagram viewer (ALWAYS write alongside, 2026-07-22)
Markdown viewers render the diagram with whatever Mermaid version/extension they bundle — old ones lack
ELK (order scrambles) or mis-theme it. So ALSO write **`OUT/toc.html`**: a self-viewer that pins the
renderer INSIDE the file (Mermaid 11 + ELK from CDN), plus the zoom/save features markdown can't have.
Verified working (headless-render test). Template — fill `{PROJECT}` and paste the **identical** Mermaid
code from §1 (init line included) at `{MERMAID}`:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>변화이론 도식 — {PROJECT}</title>
<style>
 body { font-family: -apple-system, "Apple SD Gothic Neo", sans-serif; margin: 24px; background: #fff; color: #111; }
 .lvl { font-weight: bold; margin: 8px 0 16px; }
 .toolbar { position: sticky; top: 0; background: #fff; padding: 8px 0; border-bottom: 1px solid #eee; }
 .toolbar button { margin-right: 8px; padding: 6px 14px; cursor: pointer; }
 #wrap { overflow: auto; }
 #dia { transform-origin: 0 0; }
</style>
</head>
<body>
<h1>변화이론 (Theory of Change) — {PROJECT}</h1>
<p class="lvl">사회문제 → 활동 (Activities) → 산출물 (Outputs) → 성과 (Outcomes) · 지표 → 영향 (Impact)</p>
<div class="toolbar">
 <button onclick="zoomBy(1.25)">확대 +</button>
 <button onclick="zoomBy(0.8)">축소 −</button>
 <button onclick="zoomBy(0)">원래대로</button>
 <button onclick="saveSvg()">SVG 저장</button>
 <span style="color:#888">PDF가 필요하면: 브라우저 인쇄(Cmd/Ctrl+P) → PDF로 저장</span>
</div>
<div id="wrap"><div id="dia"><pre class="mermaid">
{MERMAID}
</pre></div></div>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
import elkLayouts from "https://cdn.jsdelivr.net/npm/@mermaid-js/layout-elk@0/dist/mermaid-layout-elk.esm.min.mjs";
mermaid.registerLayoutLoaders(elkLayouts);
mermaid.initialize({ startOnLoad: true });
let s = 1;
window.zoomBy = (f) => { s = f === 0 ? 1 : s * f; document.getElementById("dia").style.transform = `scale(${s})`; };
window.saveSvg = () => { const svg = document.querySelector("#dia svg"); if (!svg) return;
  const b = new Blob([new XMLSerializer().serializeToString(svg)], {type: "image/svg+xml"});
  const a = document.createElement("a"); a.href = URL.createObjectURL(b); a.download = "toc-diagram.svg"; a.click(); };
</script>
</body>
</html>
```
Rules: the Mermaid code MUST be byte-identical to §1's block (one source of truth is `toc.json` — render
once, paste twice). Do not add libraries beyond the two pinned CDN imports. Note to the user in the
closing summary: `toc.html`은 브라우저에서 열면 순서·색이 항상 정확하고 확대/SVG 저장 가능 (첫 로드에
인터넷 필요); `toc.md`는 원본. DRAFT gate: like §1, no diagram → no toc.html until finalized.

## 2. Narrative ToC (level by level)
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
