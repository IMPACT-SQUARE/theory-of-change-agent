#!/usr/bin/env bash
#
# validate-critical.sh — thin wrapper around validate-critical.py (pure-Python, NO jq).
#
# Kept so existing `bash rules/validate-critical.sh ...` callers keep working, while the
# gate now runs anywhere python3 exists — including the Claude Desktop / Claude.ai code
# execution sandbox (which may not ship jq). All rule logic lives in validate-critical.py.
# Enforces the structural Critical rules: C01, C02, C03, C04, C05, C08.
# (C06 = noun-form is LLM-judged; C07 was removed 2026-06-05 — see rules/koica-rules.md §10.)
#
# Usage:
#   bash validate-critical.sh <pdm.json>            # GATE: exit 1 if any rule fails
#   bash validate-critical.sh --audit <pdm.json>    # AUDIT: report only, always exit 0
#   bash validate-critical.sh --json <pdm.json>     # emit {"C01":"pass",...}, exit 0
#   bash validate-critical.sh --shape <pdm.json>    # shape pre-check, exit 1 if malformed
#   bash validate-critical.sh --connectivity <pdm.json>  # broken-link lists (Phase 4 edit nudges)
HERE="$(cd "$(dirname "$0")" && pwd)"
if command -v python3 >/dev/null 2>&1; then
  exec python3 "$HERE/validate-critical.py" "$@"
elif command -v python >/dev/null 2>&1; then
  exec python "$HERE/validate-critical.py" "$@"
fi
echo "ERROR: python3 is required but not found on PATH" >&2
exit 2
