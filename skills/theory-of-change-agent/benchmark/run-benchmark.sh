#!/usr/bin/env bash
#
# run-benchmark.sh — runs the quantitative benchmark: detection accuracy of the deterministic
# validators against expected-results matrices. Three layers (2026-07-21 expansion):
#
#   1. DATA gate    (validate-critical.sh)  C01-C05,C08 on expected/*.json          — 3×6  = 18
#   2. BUDGET gate  (budget-rollup.py)      B01-B07     on budget/*.json            — 2×7  = 14
#   3. RENDER gate  (validate-render.py)    R01-R11     on render/*/ fixture dirs   — 2×11 = 22
#                                                                            total    54
#
# Detection accuracy = (# of rule results matching expected) / (total). Target: 100%.
# A "fail" expectation means the rule SHOULD flag the seeded violation.
# C06 + Advisory (A01-A08) are LLM-judged and not scored here.
#
# Usage: bash benchmark/run-benchmark.sh          (dev-only; needs jq + python3)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SKILL="$(dirname "$HERE")"

total=0; matched=0

check() { # check <rule> <expected> <actual>
  total=$((total+1))
  if [ "$2" = "$3" ]; then matched=$((matched+1)); mark="OK "; else mark="XX "; fi
  printf "  %s %s  expected=%s actual=%s\n" "$mark" "$1" "$2" "$3"
}

# ---- 1. DATA gate (C-rules) ----
DET_RULES='["C01","C02","C03","C04","C05","C08"]'
for f in "$HERE"/expected/*.json; do
  name="$(basename "$f" .json)"
  actual="$(bash "$SKILL/rules/validate-critical.sh" --json "$f")"
  expected="$(jq -c '.expected_failures' "$f")"
  echo "== data: $name =="
  while read -r rule; do
    a="$(echo "$actual"   | jq -r --arg r "$rule" '.[$r] // "n/a"')"
    e="$(echo "$expected" | jq -r --arg r "$rule" '.[$r] // "n/a"')"
    check "$rule" "$e" "$a"
  done < <(echo "$DET_RULES" | jq -r '.[]')
done

# ---- 2. BUDGET gate (B-rules) ----
for f in "$HERE"/budget/*.json; do
  name="$(basename "$f" .json)"
  echo "== budget: $name =="
  report="$(python3 "$SKILL/rules/budget-rollup.py" "$f" 2>&1 || true)"
  for rule in B01 B02 B03 B04 B05 B06 B07; do
    if echo "$report" | grep -q "\[$rule"; then a="fail"; else a="pass"; fi
    e="$(jq -r --arg r "$rule" '.expected_budget[$r] // "n/a"' "$f")"
    check "$rule" "$e" "$a"
  done
done

# ---- 3. RENDER gate (R-rules) ----
for d in "$HERE"/render/*/; do
  name="$(basename "$d")"
  [ -f "$d/expected.json" ] || continue
  echo "== render: $name =="
  actual="$(python3 "$SKILL/rules/validate-render.py" "$d" --json)"
  while read -r rule; do
    a="$(echo "$actual" | jq -r --arg r "$rule" '.[$r] // "n/a"')"
    e="$(jq -r --arg r "$rule" '.[$r] // "n/a"' "$d/expected.json")"
    check "$rule" "$e" "$a"
  done < <(jq -r 'keys[]' "$d/expected.json")
done

echo "---"
echo "Detection accuracy: $matched / $total"
if [ "$matched" -eq "$total" ]; then
  echo "BENCHMARK PASS (100% detection accuracy on deterministic rules)"
  exit 0
else
  echo "BENCHMARK FAIL — investigate rule logic or expected encoding (do NOT loosen the rules)"
  exit 1
fi
