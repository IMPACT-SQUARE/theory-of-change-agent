#!/usr/bin/env python3
"""
build-iris-metrics.py — distill the GIIN IRIS+ Catalog of Metrics (Excel) into a compact JSON reference
used for grounded "nearest IRIS+ metric" suggestions (value-rules §V5).

Dev/build tool only (needs openpyxl). Output: rules/iris-metrics.json (git-ignored; GIIN-copyrighted data
is not redistributed in the public repo — each user builds it from their own IRIS+ download). The raw
Excel itself is git-ignored too.

Usage:
  python3 build-iris-metrics.py "IRIS 5.3c Catalog of Metrics 2026.xlsx" [rules/iris-metrics.json]

IRIS+ does NOT label metrics as "outcome" vs "output"; we filter to the IMPACT sections
(Product/Operational/Investment/Financial Impact) as the outcome-relevant universe, and drop
Description/Financial-Performance/discontinued rows. Source: IRIS+ Catalog of Metrics © GIIN,
iris.thegiin.org — attribute in any surfaced result.
"""
import json, sys, re

SHEET = "IRIS+ Catalog of Metrics (5.3c)"
# Filter by ID prefix, not the Section text column (which has typos / shifted-cell noise in the source):
#   PI = Product Impact, OI = Operational Impact, II = Investment Impact  → the impact/outcome universe.
#   PD/OD/ID = *Description* rows, FP = Financial Performance             → dropped (not outcomes).
KEEP_PREFIXES = ("PI", "OI", "II")
DROP_PREFIXES = ("PD", "OD", "ID", "FP")
DIMS = ["What", "Who", "How Much Scale", "How Much Depth", "How Much Duration",
        "Contribution Depth", "Contribution Duration", "Risk"]


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip() if s is not None else ""


def main(argv):
    import openpyxl
    src = argv[0] if argv else "IRIS 5.3c Catalog of Metrics 2026.xlsx"
    out = argv[1] if len(argv) > 1 else "rules/iris-metrics.json"
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    ws = wb[SHEET]
    rows = ws.iter_rows(values_only=True)
    header = list(next(rows))
    idx = {h: i for i, h in enumerate(header)}

    def g(row, col):
        i = idx.get(col)
        return norm(row[i]) if i is not None and i < len(row) else ""

    metrics = []
    for row in rows:
        if not row or not row[0]:
            continue
        mid = g(row, "ID")
        prefix = re.match(r"[A-Za-z]+", mid)
        prefix = prefix.group() if prefix else ""
        if prefix not in KEEP_PREFIXES:
            continue
        section = g(row, "Section")
        if "Discontinued" in section:
            continue
        dims = [d for d in DIMS if g(row, d)]  # which IMP dimensions this metric is tagged with
        metrics.append({
            "id": g(row, "ID"),
            "name": g(row, "Metric Name"),
            "definition": g(row, "Definition"),
            "category": g(row, "Primary Impact Category"),
            "theme": g(row, "Impact Category & Theme"),
            "sdgs": g(row, "SDGs"),
            "dimensions": dims,
        })

    doc = {
        "source": "IRIS+ Catalog of Metrics 5.3c (2026) © GIIN, iris.thegiin.org",
        "note": "Impact-section metrics only (Product/Operational/Investment/Financial Impact). "
                "IRIS+ does not label outcome vs output. For grounded 'nearest IRIS+ metric' suggestions — "
                "never invent a code; suggestions are 참고용, not an official mapping.",
        "count": len(metrics),
        "metrics": metrics,
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(f"wrote {out}: {len(metrics)} impact metrics")


if __name__ == "__main__":
    main(sys.argv[1:])
