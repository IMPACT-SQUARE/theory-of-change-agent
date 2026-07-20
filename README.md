# Theory of Change Agent

**English** · [한국어](README.ko.md) · [日本語](README.ja.md) · [Tiếng Việt](README.vi.md)

Every impact practitioner knows the moment: a blank results matrix on the screen, a submission
deadline, and no idea which cell to fill first. The logic is in your head — the form refuses to
receive it.

**Theory of Change Agent is an AI interviewer that gets it out.** Answer one question at a time, in
plain language, and it builds your results chain — social problem → activities → outputs → outcomes →
impact — then renders it as a **KOICA-guideline PDM (Project Design Matrix)** for international
development projects, or a **Theory-of-Change diagram** for impact startups, CSR, and nonprofits.
It runs on AI assistants such as Claude, and answers in whatever language you speak to it.

It doesn't just fill cells. It pushes back — "that's an output at scale, not an outcome" — and it
proves its work: a deterministic quality gate scores **18/18 on our detection benchmark**, every rule
carries a **page citation from the 36-page KOICA guideline**, and the budget module reproduced two
real KOICA-style budget sheets **to the won**.

**Who this is for:**

- **First-time PDM writers** applying to KOICA or similar programs — structured questions instead of a blank form
- **Practitioners with a draft** who want it audited against the guideline before reviewers see it
- **Founders and CSR/nonprofit teams** with only an idea, who need their impact logic on one page

## Quick start

1. Install (30 seconds — see below)
2. Say: *"Create a PDM with the Theory of Change Agent"* — or attach your business plan / annual report
3. Answer the questions. Say **"finalize"** when it looks right.
4. Open `out/pdm.md`. You'll know if this is for you.

## See it work

```
You:    Create a PDM with the Theory of Change Agent.
Agent:  What are you working on?
        ① International development (PDM)  ② Impact startup
        ③ CSR / ESG                        ④ Nonprofit
You:    ① — a maternal health project in Laos.
Agent:  [Q1 · social problem] What problem does this project tackle —
        who is suffering, and what is the cause?
You:    Mothers in rural districts deliver at home. Clinics are far,
        and people don't trust them.
Agent:  That qualifies as a social problem (structural · affects many ·
        real harm). Phenomenon: high home-delivery rate. Cause: low
        access to and trust in facilities. So the outcome to aim for is
        a change of state: "facility-delivery practice takes root" —
        not "more training sessions delivered." Keep this framing?
        …
        [one question at a time: activities → outputs → indicators →
         assumptions — each answer wired into the results chain]
        …
You:    finalize
Agent:  ✔ Quality gate passed (8/8 critical rules).
        ⚠ Outcome 2 reads as an output at scale — "education expanded"
          counts sessions, not behavior change. Suggested rephrasing: …
        ◇ Nearest IRIS+ metrics suggested for indicator 1-1
          (reference only, not an official mapping).
        Final result: out/pdm.md
```

The agent listened to the *pain*, named the cause, and refused to let an output masquerade as an
outcome. That correction — the one reviewers always make — happened before submission, not after.

## How it works

**Interview → Build the chain → Verify → Gate → Render.** Each step feeds the next.

The interview follows the Theory of Change: it anchors on a properly-defined **social problem**
(structural · affects many · causes real harm), traces phenomenon → cause, and requires every
outcome to be a **change of state that recovers the cause** — not a scaled-up output, not generic
utility. Organization-level documents (a nonprofit's annual report, a startup's business plan) get a
project-detection step: view the **whole organization** as a mission-to-projects map, or drill into
**one project**.

| Deliverable | What it is |
|---|---|
| `pdm.md` | The KOICA 4×4 PDM matrix — Impact / Outcome / Outputs / Activities × Summary / Indicators / MoV / Assumptions |
| `toc.md` | Theory-of-Change node diagram (with a plain-text causal-flow fallback for viewers without Mermaid) + the data you must start collecting now to measure impact later |
| `monitoring.md` | Per-indicator measurement plan: definition, formula, baseline, target, source, timing, collector, disaggregation |
| `budget.md` *(optional)* | A PDM-linked budget: line items per activity, calculation basis (unit price × qty × frequency), funder split, per-year totals |
| `details/pdm.json` | The single source of truth — every view above is rendered from it |

Inputs: plain conversation, PDF, and **Korean HWP files (.hwp/.hwpx)** — the bundled extractor is
dependency-free, so it works even in app sandboxes.

## Verification you can check

Nothing here is "trust the AI." The checks are code, and the receipts are in the repo:

- **Deterministic quality gate** — 8 critical KOICA rules (no impact indicators, 3–4 outputs,
  indicator caps, MoV required, no orphan nodes, noun-form outputs…) enforced by pure Python.
  **18/18 detection accuracy** on the seeded-violation benchmark in [`benchmark/`](./skills/theory-of-change-agent/benchmark/).
- **Page-cited rules** — every rule in
  [`koica-rules.md`](./skills/theory-of-change-agent/rules/koica-rules.md) cites its page in the
  official KOICA PDM guideline, so you can argue with the source, not with us.
- **Outcome double-check** — a logical test (does the change recover the cause?) plus
  nearest-metric matching against the **593 impact metrics of IRIS+** (reference only, © GIIN).
- **Budget arithmetic by script, never by AI** — every sum, ratio, funder split, and the
  general-management cap is computed and validated deterministically. Verified in three cycles
  against two real KOICA-style budget sheets: totals reproduced **to the won**, and the exercise
  caught (and fixed) three real rule bugs.
- Advisory rules (SMART, CREAM, gender-disaggregated indicators) are scored, not enforced —
  you stay in charge of taste.

## Install — 30 seconds

**Requirements:** Claude (Claude Code, desktop app, or claude.ai) · `python3` (bundled in the
desktop/web code-execution sandbox)

### Claude Code (auto-update, recommended)

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

Update later with `/plugin update theory-of-change-agent`.

### Claude desktop · Antigravity · claude.ai (zip upload)

1. Zip the skill (or use the pre-built `theory-of-change-agent.zip`):
   ```bash
   cd skills && zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
2. Upload: **Claude desktop** `Settings → Skills → Add → Upload` · **Antigravity** Skills screen ·
   **claude.ai** `Settings → Capabilities → Skills → Upload`. Requires a paid plan with code
   execution enabled.
3. Say *"Create a KOICA PDM with the Theory of Change Agent"* in the chat.

> App-uploaded skills don't auto-update — re-upload the zip when it changes. Details, including the
> fix when the Mermaid diagram shows as code in Antigravity (install `bierner.markdown-mermaid` from
> Open VSX, or just read the built-in text fallback):
> [`INSTALL-desktop.md`](./skills/theory-of-change-agent/INSTALL-desktop.md).

### Git (direct link)

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

## Data policy

- `docs/` contains public documents only (the KOICA PDM guideline, Theory of Change references).
- `benchmark/` PDMs are fictional — real names and amounts removed, structure kept.
- Real project PDMs and budgets are never stored in this repository.

## Repository layout

```
theory-of-change-agent/
├── .claude-plugin/          plugin configuration
├── skills/theory-of-change-agent/
│   ├── SKILL.md             the full procedure
│   ├── prompts/             interview & rendering prompts
│   ├── rules/               KOICA rules + deterministic validators (gate, budget, HWP)
│   ├── schema/              pdm.json schema and reference example
│   └── benchmark/           seeded-violation fixtures (18/18)
├── docs/                    public references
└── README.md                this document
```

## Status

v1.0 — four use cases (international development / impact startup / CSR·ESG / nonprofit), three
interaction modes, deterministic quality gate, budget module, HWP input, plugin distribution.
Impact-investor screening mode is planned. Formerly "Impact Harness" (renamed June 2026).

## License

[MIT](./LICENSE) © 2026 IMPACT SQUARE. Free forever. Go build your theory of change.
