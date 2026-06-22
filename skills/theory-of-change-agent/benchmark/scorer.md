# Benchmark scorer & runner

The benchmark has three components. Run them from the skill root.

## Component 2 — Quantitative: detection accuracy (automated)
The deterministic rules (C01-C05, C08) are scored against the `expected_failures` matrix in each
`expected/*.json`. The fixtures are **synthetic, anonymized PDMs** (narratives fabricated; structure
preserved) modeled on the deviation patterns of real approved PDMs. This validates that the gate correctly
DETECTS known guideline deviations — it does NOT require a compliant-looking PDM to pass.

```
bash benchmark/run-benchmark.sh
```
Expected: **100% detection accuracy**. Known expected failures:
| Rule | synthetic-1 | synthetic-2 | synthetic-3 |
|------|-------------|-------------|-------------|
| C01 impact-no-indicators/MoV | FAIL | FAIL | PASS |
| C02,C03,C04,C05,C08 | PASS | PASS | PASS |

(C07 single-outcome was removed 2026-06-05 — see `rules/koica-rules.md` §10. All three reference PDMs
have multiple outcomes, which is now allowed.)

If a result does not match: investigate the rule logic OR the `expected_failures` encoding. **Do NOT
loosen Critical rules to make a real PDM pass** (real approved PDMs legitimately deviate from the 2017
guideline — that's what AUDIT mode is for).

## Component 1 — Qualitative: brief reverse-engineering (manual / LLM)
1. Feed `benchmark/sample-brief.md` (a synthetic concept brief) to the agent in Mode A
   (`/theory-of-change-agent --concept @benchmark/sample-brief.md`).
2. Run the interview (a tester answers as the brief implies) → produces `out/pdm.json`.
3. Sanity-check `out/pdm.json` on **"structurally comparable"** criteria:
   - a full results chain (impact → outcome(s) → 3-4 outputs → activities → inputs);
   - behavioral-change outcomes (facility-based delivery / care practices), impact tied to SDG 3 with
     **no** impact-level indicators;
   - comparable indicator types; assumptions covering retention, participation, and supply chain.
4. This is a structural sanity check (the brief can let a strong model reconstruct the structure), not a
   measure of interview quality.

## Component 3 — Round-trip: rendering fidelity (manual / LLM)
Render a generated `pdm.json` to `pdm.md` + `monitoring.md` and verify:
- Impact row shows `-` in the OVI and MoV columns;
- Activities row carries Inputs in the OVI column and Pre-conditions in the Assumptions column;
- every indicator in `pdm.json` appears in `monitoring.md` (no silent drops);
- output language matches `meta.lang`.

## Advisory scoring (LLM, for completeness)
The Advisory rules (A01-A08) are LLM-judged (see `prompts/refine-advisory.md`); they are scored per-rule-
type (≥80% to pass the gate) but are NOT part of the deterministic detection-accuracy target.
