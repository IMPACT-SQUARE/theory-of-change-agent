#!/usr/bin/env python3
"""
validate-critical.py — deterministic structural validator for KOICA PDM.

Pure-Python port of validate-critical.sh (no jq / no external deps) so the gate
runs anywhere python3 exists — including the Claude Desktop / Claude.ai code
execution sandbox. Rule logic is identical to the jq version.

Enforces the structurally-checkable Critical rules: C01, C02, C03, C04, C05, C08.
(C06 = noun-form is LLM-judged, not handled here. C07 single-outcome was removed
2026-06-05 — see rules/koica-rules.md §10.)

Usage:
  python3 validate-critical.py <pdm.json>            # GATE: exit 1 if any rule fails
  python3 validate-critical.py --audit <pdm.json>    # AUDIT: report only, always exit 0
  python3 validate-critical.py --json <pdm.json>     # emit {"C01":"pass",...}, exit 0
  python3 validate-critical.py --shape <pdm.json>    # shape pre-check, exit 1 if malformed
"""
import json
import sys


def _arr(d, key):
    """Return d[key] as a list, treating missing/null as []."""
    v = d.get(key) if isinstance(d, dict) else None
    return v if isinstance(v, list) else []


def _compact(value):
    """jq-style compact JSON (no spaces) for detail strings."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def evaluate(pdm):
    """Return an ordered list of {id, pass, detail} dicts mirroring the jq output."""
    outputs = _arr(pdm, "outputs")
    outcomes = _arr(pdm, "outcomes")
    activities = _arr(pdm, "activities")
    impact = pdm.get("impact") or {}

    # reference sets
    actref = set()
    for op in outputs:
        for a in _arr(op, "from_activities"):
            actref.add(a)
    opref = set()
    for oc in outcomes:
        for o in _arr(oc, "from_outputs"):
            opref.add(o)

    results = []

    # C01 — Impact has no indicators / no MoV
    imp_ind = len(_arr(impact, "indicators"))
    imp_mov = len(_arr(impact, "mov"))
    results.append({
        "id": "C01",
        "pass": imp_ind == 0 and imp_mov == 0,
        "detail": "impact indicators = %d, impact mov = %d (both must be 0)" % (imp_ind, imp_mov),
    })

    # C02 — Output count 3-4
    n_out = len(outputs)
    results.append({
        "id": "C02",
        "pass": 3 <= n_out <= 4,
        "detail": "outputs = %d (need 3-4)" % n_out,
    })

    # C03 — Each outcome has 1-3 indicators
    counts = [len(_arr(oc, "indicators")) for oc in outcomes]
    results.append({
        "id": "C03",
        "pass": all(1 <= c <= 3 for c in counts),
        "detail": "outcome indicator counts = %s (need 1-3)" % _compact(counts),
    })

    # C04 — Every output/outcome indicator has a non-empty MoV
    missing_mov = []
    for parent in outputs + outcomes:
        for ind in _arr(parent, "indicators"):
            mov = ind.get("mov") if isinstance(ind, dict) else None
            if not (isinstance(mov, str) and mov != ""):
                missing_mov.append(ind.get("id") if isinstance(ind, dict) else None)
    results.append({
        "id": "C04",
        "pass": len(missing_mov) == 0,
        "detail": "indicators missing MoV = %s" % _compact(missing_mov),
    })

    # C05 — Every output is referenced by some outcome.from_outputs
    not_fed = [op.get("id") for op in outputs if op.get("id") not in opref]
    results.append({
        "id": "C05",
        "pass": len(not_fed) == 0,
        "detail": "outputs not feeding any outcome = %s" % _compact(not_fed),
    })

    # C08 — No orphan activities (activity or one of its sub ids connects to an output)
    orphans = []
    for act in activities:
        ids = [act.get("id")] + [s.get("id") for s in _arr(act, "sub")]
        if not any(i in actref for i in ids):
            orphans.append(act.get("id"))
    results.append({
        "id": "C08",
        "pass": len(orphans) == 0,
        "detail": "orphan activities = %s" % _compact(orphans),
    })

    return results


def shape_ok(pdm):
    """Mirror the SKILL.md Phase 3 jq shape check."""
    return (
        isinstance(pdm, dict)
        and "meta" in pdm
        and "impact" in pdm
        and isinstance(pdm.get("outcomes"), list)
        and isinstance(pdm.get("outputs"), list)
        and isinstance(pdm.get("activities"), list)
        and "inputs" in pdm
    )


def main(argv):
    mode = "gate"
    out = "human"
    file = ""
    for a in argv:
        if a == "--audit":
            mode = "audit"
        elif a == "--json":
            out = "json"
        elif a == "--shape":
            out = "shape"
        elif a in ("-h", "--help"):
            sys.stdout.write(__doc__)
            return 0
        else:
            file = a

    if not file:
        sys.stderr.write("usage: validate-critical.py [--audit] [--json] [--shape] <pdm.json>\n")
        return 2

    try:
        with open(file, "r", encoding="utf-8") as fh:
            pdm = json.load(fh)
    except FileNotFoundError:
        sys.stderr.write("ERROR: %s not found\n" % file)
        return 2
    except (json.JSONDecodeError, ValueError):
        sys.stderr.write("ERROR: %s is not valid JSON\n" % file)
        return 2

    if out == "shape":
        return 0 if shape_ok(pdm) else 1

    results = evaluate(pdm)

    if out == "json":
        print(json.dumps({r["id"]: ("pass" if r["pass"] else "fail") for r in results}, ensure_ascii=False))
        return 0

    # human-readable
    for r in results:
        if r["pass"]:
            print("PASS " + r["id"])
        else:
            print("FAIL " + r["id"] + "  " + r["detail"])
    print("---")
    fails = sum(1 for r in results if not r["pass"])
    if fails == 0:
        print("ALL CRITICAL CHECKS PASSED (C01-C05, C08)")
        return 0
    print("CRITICAL CHECK FAILURES: %d" % fails)
    if mode == "audit":
        print("(audit mode: report-only, not blocking)")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
