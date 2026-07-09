# Theory of Change Agent (변화이론 에이전트)

[한국어](README.md) · **English** · [日本語](README.ja.md) · [Tiếng Việt](README.vi.md)

A tool that structures your project's results using a **Theory of Change**. Answer questions in a
conversational flow, and it produces a **PDM (Project Design Matrix)** for international development
cooperation projects, or a **Theory-of-Change diagram** for impact startups, corporate social
responsibility, and nonprofit projects. It runs on AI assistants such as Claude.

The goal is to remove that overwhelming moment of staring at an empty matrix, not knowing where to
start. Answer one question at a time, and you end up with a matrix aligned with the KOICA PDM
guideline. Answer in Korean and the output is Korean; answer in English and the output is English.

---

## What it helps with

- It asks questions following the **Theory of Change** flow (Inputs → Activities → Outputs → Outcomes →
  Impact) and builds the results chain with you.
- When done, it produces two documents: the **PDM matrix** and the **monitoring matrix**.
- It **verifies your Outcomes twice** — ① a **logical check** asking whether the stated change actually
  recovers the cause of the problem, and ② **nearest-metric matching** against the **593 metrics of
  IRIS+**, the global impact-metrics library, offered as a reference.
- Right before finishing, it **automatically checks** the output against the core rules of the KOICA
  guideline, catching the mistakes reviewers most often flag.

It is useful for:

- People writing a PDM for the first time for a KOICA application
- People with an existing draft who want it checked against the guideline
- People with only an idea and no results structure yet

---

## How to start

The tool asks three things in order.

**(1) What are you trying to do?** Pick one of four — **International development cooperation (PDM)**
produces a PDM matrix; **Impact startup (new business development)** · **Corporate social contribution
(CSR, ESG)** · **Nonprofit** produce a Theory-of-Change diagram. The underlying logic is identical;
only the shape of the final deliverable differs. (A fifth, **Impact investor (investment screening)**,
is planned.)

When you upload an **organization-level document** (a business plan, an annual report) — common for
nonprofits and impact startups — and multiple projects are detected, it asks whether you want the
**whole-organization view** (a map of how the mission connects to the projects) or a **single project**.

**(2) Where are you now?**

- **I only have an idea** — the concept exists but nothing is written down yet.
- **I have documents — a business plan, a draft, an existing PDM** — it reads and uses them. (If the
  PDM is already approved, you can get an audit-only review that changes nothing.)

**(3) How do you want to proceed?**

- **Step by step, one question at a time** — the most thorough. (~10–20 min from an idea, ~5–10 min
  from documents)
- **Draft first, then refine on top** — the fastest (~2–5 min). It generates a full draft deliverable,
  you fix what you don't like, and saying "finalize" runs the quality gate and wraps up.

---

## What you get

When the session ends, the results are saved as files.

- **PDM matrix (`pdm.md`)**: the KOICA format as-is — Impact / Outcome / Outputs / Activities in four
  columns (Summary, Indicators, Means of Verification, Important Assumptions). The default deliverable
  for international development projects.
- **Theory-of-Change diagram (`toc.md`)**: a node diagram showing how activities connect to outputs and
  outputs to outcomes. For impact startups, CSR, and nonprofits this is the default deliverable — and
  it also tells you which data you must collect yourself to measure your impact later.
- **Monitoring matrix (`monitoring.md`)**: per indicator — definition, formula, baseline, target,
  rationale, data source, timing, collector, and disaggregation.
- **Project budget (`budget.md`, optional)**: for international development (PDM) projects, it can also
  draft a budget linked to the PDM — line items per activity, calculation basis (unit price × quantity ×
  frequency), funder split, and general management cost. All sums are computed and verified
  deterministically by a script.

Baselines and targets are usually set after field surveys, so they start as `TBD (추후 확정)` and can be
filled in later.

Files are organized so that **the main deliverable (`pdm.md` or `toc.md`) sits at the top of `out/`**,
with the monitoring matrix and source data under `out/details/`:

```
out/
├── pdm.md          (or toc.md)   ← main deliverable
└── details/
    ├── monitoring.md
    └── pdm.json    (the source data all views are rendered from)
```

---

## How quality checking works

Right before finishing, it checks the PDM against the core rules of the KOICA guideline. For example:

- Impact carries no separate indicators.
- Outputs are consolidated to 3–4.
- Each outcome has 1–2 indicators (3 max).
- Every indicator states how it will be measured (means of verification).
- Every activity connects to an output, and every output to an outcome — no orphans.
- Outcomes are phrased as a **behavioral change** of the target group, not quantitative expansion.

Must-pass rules are refined together until they pass; advisory rules (SMART, CREAM,
gender-disaggregated indicators, etc.) are reported as a score.
The full rule list with guideline page citations is in
[`skills/theory-of-change-agent/rules/koica-rules.md`](./skills/theory-of-change-agent/rules/koica-rules.md).

---

## Installation

If you normally use the **Claude desktop app or claude.ai**, see **Method 3**.
If you are comfortable with **Claude Code** (the terminal tool), **Method 1** is easiest.

### Method 1. Claude Code plugin (auto-update, recommended)

Type these two lines inside Claude Code:

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

To update later:

```
/plugin marketplace update impact-square
/plugin update theory-of-change-agent
```

### Method 2. Direct link (quick install)

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

Update with `git pull`. To unlink, run `rm ~/.claude/skills/theory-of-change-agent` — the original
folder stays intact.

### Method 3. Upload a zip (Claude desktop · Antigravity · claude.ai)

To use it **directly in an app** rather than Claude Code, package the skill as a zip and upload it.

1. **Create the zip**: inside the downloaded repo's `skills` folder, run:
   ```bash
   cd skills
   zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
   (If the repo already ships a pre-built `theory-of-change-agent.zip`, use it as-is.)

2. **Upload** — depending on your app:
   - **Claude desktop**: `Settings → Skills → Add → Upload`, choose `theory-of-change-agent.zip` → Enable.
   - **Antigravity**: upload `theory-of-change-agent.zip` on the Skills screen.
   - **claude.ai (web)**: `Settings → Capabilities → Skills → Upload`.

   > Prerequisites: the Claude apps require a **paid plan + code execution enabled** (the quality gate
   > runs on python3). Menu names can differ slightly across versions.

3. **Use it**: type something like "Create a KOICA PDM with the Theory of Change Agent" in the chat.

#### When the Theory-of-Change diagram (Mermaid) doesn't render in Antigravity

The diagram in `out/toc.md` is drawn with **Mermaid `flowchart`**. Antigravity (and VS Code without a
Mermaid preview) does **not render** ```mermaid``` blocks by default, so it may look like code. Two fixes:

- **(Recommended) Install the Mermaid preview extension** — Antigravity is VS Code-based, so install
  **`Markdown Preview Mermaid Support`** (publisher `bierner`, id `bierner.markdown-mermaid`) from the
  **Open VSX** marketplace, and `toc.md` renders as a picture. *(Extensions must be installed in the
  app yourself — a skill cannot auto-install them.)*
- **Read it as-is, no install** — the skill always emits a **plain-text causal flow (→ arrows)** with
  the same content right below the Mermaid block, so the logic stays readable without the extension.
   The finished deliverables arrive as download links in the chat.

> Skills uploaded to an app do **not** auto-update. Re-upload a new zip when contents change.
> If you want auto-updates, use **Method 1 (the Claude Code plugin)**.

More details in
[`skills/theory-of-change-agent/INSTALL-desktop.md`](./skills/theory-of-change-agent/INSTALL-desktop.md).

### Requirements

- **Claude** (any of Claude Code, the desktop app, or the web)
- **`python3`**: used for the quality gate. Included by default in the desktop/web code-execution sandbox.

---

## Data policy

- The PDFs in `docs/` are public documents only (the KOICA PDM guideline, Theory of Change references).
- The benchmark data (`benchmark/`) consists of fictional PDMs with all real names and amounts removed —
  only the structure remains.
- Real project PDM originals are never stored in this repository; they are kept private elsewhere.

---

## Repository layout

```
theory-of-change-agent/
├── .claude-plugin/      plugin configuration
├── skills/
│   └── theory-of-change-agent/
│       ├── SKILL.md         the full procedure
│       ├── README.md        skill-level usage guide
│       ├── INSTALL-desktop.md  desktop/web install guide
│       ├── prompts/         interview & document-generation prompts
│       ├── rules/           KOICA rules and the automatic checker
│       ├── schema/          PDM data format and example
│       └── benchmark/       fictional examples for quality checks
├── docs/                public references
├── README.md            this document (Korean)
└── LICENSE              license (MIT)
```

---

## Status

Version 1.0 — three interaction modes, automatic quality checks, and Claude Code plugin distribution.
Formerly named "Impact Harness"; renamed to "Theory of Change Agent (변화이론 에이전트)" in June 2026.

---

## License

[MIT](./LICENSE) © 2026 IMPACT SQUARE
