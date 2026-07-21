# Theory of Change Agent

English · [한국어](README.ko.md) · [日本語](README.ja.md) · [Tiếng Việt](README.vi.md)

You know the problem, the activities, and the intended results, but turning them into a coherent
PDM can be difficult.

Theory of Change Agent guides you through that work in conversation. It asks one question at a
time and turns your answers into a results chain: social problem → activities → outputs → outcomes →
impact. For international-development projects, it produces a PDM (Project Design Matrix). For
impact startups, CSR, and nonprofits, it produces a Theory of Change diagram.
It works with AI assistants such as Claude and responds in the language you use.

## This helps when you need to

- Create a PDM for the first time
- Review a draft before submitting it
- Clarify the impact model for a new project

## Quick start

1. Install the skill below.
2. Enter `Create a PDM with the Theory of Change Agent`. You can also attach a business plan or annual report.
3. Answer the questions. When the result is right, enter `finalize`.
4. Open `out/`. International-development projects are saved as `pdm.md`; other use cases are saved as `toc.md`.

## Choose what you need

Start with the problem, identify its causes, and define a measurable change.

| Your situation | What the agent creates | Good starting material |
|---|---|---|
| International-development project | PDM | An idea, proposal, or PDM draft |
| Impact startup or new venture | Theory-of-Change diagram | A business plan or a problem statement |
| CSR or ESG project | Theory-of-Change diagram | A program brief or proposal |
| Nonprofit program or annual report | Theory-of-Change diagram | An annual report; choose the organization or one project |

New PDMs are checked before finalization. You can also revise a completed PDM through conversation.

## See it work

```
You:    Create a PDM with the Theory of Change Agent.
Agent:  What are you working on?
        ① International development (PDM)  ② Impact startup
        ③ CSR / ESG                        ④ Nonprofit
You:    ①. A maternal health project in Laos.
Agent:  [Q1 · social problem] What problem does this project tackle?
        who is suffering, and what is the cause?
You:    Mothers in rural districts deliver at home. Clinics are far,
        and people don't trust them.
Agent:  This is a social problem: it is structural, affects many people,
        and causes real harm. The immediate issue is a high rate of home
        deliveries. The causes are limited access to facilities and low
        trust in them. An outcome could be "more women give birth in
        health facilities," rather than "more training sessions delivered." Does
        that reflect the change you want to achieve?
        …
        [The agent asks about activities, outputs, indicators, and
         assumptions one at a time, and connects each answer to the results chain.]
        …
You:    finalize
Agent:  ✔ Quality gate passed (8/8 critical rules).
        ⚠ Outcome 2 describes delivery at a larger scale. "Expanded
          education" counts sessions rather than a change in behavior.
          Suggested revision: …
        ◇ Suggested IRIS+ metrics for indicator 1-1. These are references,
          not official mappings.
        Result: out/pdm.md
```

The interview separates activities and outputs from the change the project intends to achieve.

## How it works

The process is simple: interview, build the chain, verify, validate, and render.

The interview follows Theory of Change practice. It starts with a clearly defined social problem:
one that is structural, affects many people, and causes real harm. It then links the observed problem
to its causes and defines outcomes as changes that address those causes. Outputs and broad statements
of benefit are not treated as outcomes.

For organization-level documents, such as an annual report or business plan, the agent first checks
whether the material covers one project or several. You can map the whole organization from its
mission to its projects, or focus on one project.

| Deliverable | What it is |
|---|---|
| `pdm.md` | 4×4 PDM matrix: Impact / Outcome / Outputs / Activities × Summary / Indicators / MoV / Assumptions |
| `toc.md` | Theory of Change diagram, with a text version for viewers that do not support Mermaid, plus data needed for future impact measurement |
| `details/monitoring.md` | Per-indicator measurement plan: definition, formula, baseline, target, source, timing, collector, disaggregation |
| `budget.md` *(optional)* | A PDM-linked budget: line items per activity, calculation basis (unit price × qty × frequency), funder split, per-year totals |
| `details/toc.json` | Source data used to render every view above |

You can start with a conversation, a PDF, or a Korean HWP file (`.hwp` or `.hwpx`). The bundled extractor
has no external dependencies, so it can run in app sandboxes.

## Verification you can check

The checks are implemented in code and documented in this repository:

- Deterministic quality gate: Pure Python enforces eight critical structural rules, including no
  impact indicators, three to four outputs, indicator limits, required means of verification, no
  orphan nodes, and noun-form outputs. It reached 18/18 detection accuracy on the
  [seeded-violation benchmark](./skills/theory-of-change-agent/benchmark/).
- Outcome review: A logic check asks whether the intended change addresses its underlying cause.
  Outcome indicators are also matched to the closest of the 593 IRIS+ impact metrics for
  reference only. This is not an official IRIS+ mapping.
- Scripted budget arithmetic: A script calculates and validates every total, ratio, funder split,
  and general-management cap, verified against real budget sheets.
- Advisory rules: SMART, CREAM, and gender-disaggregated indicators are scored but not enforced.
  You decide whether to act on the findings.

## Install

You need Claude Code, Claude desktop, or claude.ai, plus `python3`. The desktop and web
code-execution sandboxes include Python.

### Easiest: paste this into Claude Code, Antigravity, or any local AI agent

Open your AI agent (Claude Code, Antigravity, Gemini CLI, …) and paste this. The agent does the rest.

> Install the Theory of Change Agent: run `git clone --single-branch --depth 1 https://github.com/IMPACT-SQUARE/theory-of-change-agent.git ~/theory-of-change-agent`, then symlink (or copy) the `skills/theory-of-change-agent` folder inside it into YOUR environment's global skills folder — Claude Code → `~/.claude/skills/`, Antigravity → `~/.gemini/config/skills/`, Gemini CLI → `~/.gemini/skills/` — confirm that `<skills folder>/theory-of-change-agent/SKILL.md` exists, then tell me that I can start by saying "Create a PDM with the Theory of Change Agent" (restart the session first in Antigravity) and that I can update later with `git -C ~/theory-of-change-agent pull`.

*(The Claude web/desktop chat sandbox has no access to your local files — use the plugin or zip methods below there.)*

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
2. Upload the archive in Claude desktop at `Settings → Skills → Add → Upload`, in Antigravity's
   Skills screen, or in claude.ai at `Settings → Capabilities → Skills → Upload`. A paid plan
   with code execution enabled is required.
3. Enter `Create a PDM with the Theory of Change Agent` in the chat.

> Skills uploaded to an app do not update automatically. Upload a new archive after each change. For
> Antigravity, install `bierner.markdown-mermaid` from Open VSX if Mermaid diagrams appear as code.
> You can also use the built-in text version. See:
> [`INSTALL-desktop.md`](./skills/theory-of-change-agent/INSTALL-desktop.md).

### Git (direct link)

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

## Data policy

- `docs/` contains public reference documents only.
- `benchmark/` PDMs are fictional. They retain the structure of the originals but omit real names and amounts.
- Real project PDMs and budgets are never stored in this repository.

## Repository layout

```
theory-of-change-agent/
├── .claude-plugin/          plugin configuration
├── skills/theory-of-change-agent/
│   ├── SKILL.md             the full procedure
│   ├── prompts/             interview & rendering prompts
│   ├── rules/               writing rules + deterministic validators (gate, budget, HWP)
│   ├── schema/              toc.json schema and reference example
│   └── benchmark/           seeded-violation fixtures
├── docs/                    public references
└── README.md                this document
```

## Status

Version 1.0 supports international development, impact startups, CSR and ESG, and nonprofits. It
includes three interaction modes, a deterministic quality gate, budget support, HWP input, and
plugin distribution. Impact-investor screening is planned. The project was renamed from Impact
Harness in June 2026.

## License

[MIT](./LICENSE) © 2026 IMPACT SQUARE.
