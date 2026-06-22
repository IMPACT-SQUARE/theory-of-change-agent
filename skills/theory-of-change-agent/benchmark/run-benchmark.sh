#!/usr/bin/env bash
#
# run-benchmark.sh — runs the quantitative benchmark (Component 2): detection accuracy of the
# deterministic validator against the expected-failures matrix encoded in each benchmark/expected/*.json.
#
# Detection accuracy = (# of rule results that match the expected pass/fail) / (total rule results).
# Target: 100%. A "fail" expected_failures entry means the rule SHOULD flag a known guideline deviation.
# Note: only the deterministic rules (C01-C05, C08) are scored here; C06 + Advisory are LLM-judged.
# (C07 single-outcome was removed 2026-06-05 — see rules/koica-rules.md §10.)
#
# Usage: bash benchmark/run-benchmark.sh
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SKILL="$(dirname "$HERE")"
VALIDATOR="$SKILL/rules/validate-critical.sh"
DET_RULES='["C01","C02","C03","C04","C05","C08"]'

total=0; matched=0
for f in "$HERE"/expected/*.json; do
  name="$(basename "$f" .json)"
  actual="$(bash "$VALIDATOR" --json "$f")"     # {"C01":"pass",...} for deterministic rules
  expected="$(jq -c '.expected_failures' "$f")" # full expected incl. C06 (LLM)
  echo "== $name =="
  # Compare only the deterministic rules
  while read -r rule; do
    a="$(echo "$actual"   | jq -r --arg r "$rule" '.[$r] // "n/a"')"
    e="$(echo "$expected" | jq -r --arg r "$rule" '.[$r] // "n/a"')"
    total=$((total+1))
    if [ "$a" = "$e" ]; then matched=$((matched+1)); mark="OK "; else mark="XX "; fi
    printf "  %s %s  expected=%s actual=%s\n" "$mark" "$rule" "$e" "$a"
  done < <(echo "$DET_RULES" | jq -r '.[]')
done

echo "---"
echo "Detection accuracy: $matched / $total"
if [ "$matched" -eq "$total" ]; then
  echo "BENCHMARK PASS (100% detection accuracy on deterministic rules)"
  exit 0
else
  echo "BENCHMARK FAIL — investigate rule logic or expected_failures encoding (do NOT loosen Critical rules)"
  exit 1
fi
