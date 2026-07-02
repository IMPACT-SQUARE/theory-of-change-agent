#!/usr/bin/env python3
"""
iris-search.py — deterministic keyword search over rules/iris-metrics.json for grounded
"nearest IRIS+ metric" suggestions (value-rules §V5b). Pure stdlib, no jq / no network.

The catalog has 593 impact metrics — too many to scan inline — so this returns the top-K
candidates for a query, and the agent picks/explains from THAT shortlist only (never invents a code).

Usage:
  python3 iris-search.py "clean cookstove adoption household air pollution"        # top 5, human table
  python3 iris-search.py --json --top 8 "energy access electricity connections"    # JSON for the agent
  python3 iris-search.py --db /path/to/iris-metrics.json "..."                      # explicit catalog path

Scoring is transparent token overlap (query tokens ∩ metric name/theme/definition), with a
higher weight on the metric NAME. English catalog: pass English keyword(s) distilled from the
outcome indicator (translate Korean indicators to a few English terms before searching).
Exit code 3 = catalog file missing (agent should then show "IRIS+ 매칭 준비 중").
"""
import json, sys, re, os

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.path.join(HERE, "iris-metrics.json")
STOP = {"the", "a", "an", "of", "and", "or", "to", "in", "for", "on", "by", "with", "at",
        "as", "is", "are", "be", "number", "value", "total", "per", "rate", "amount"}


def tokens(s):
    return [t for t in re.findall(r"[a-z0-9]+", (s or "").lower()) if t not in STOP and len(t) > 2]


def score(qtokens, m):
    name = set(tokens(m.get("name", "")))
    theme = set(tokens(m.get("theme", "")))
    body = set(tokens(m.get("definition", "")))
    s = 0.0
    for q in qtokens:
        if q in name:
            s += 3.0
        elif q in theme:
            s += 2.0
        elif q in body:
            s += 1.0
    return s


def main(argv):
    db = DEFAULT_DB
    top = 5
    as_json = False
    rest = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--json":
            as_json = True
        elif a == "--db":
            i += 1; db = argv[i]
        elif a == "--top":
            i += 1; top = int(argv[i])
        else:
            rest.append(a)
        i += 1
    query = " ".join(rest).strip()
    if not query:
        print("usage: iris-search.py [--json] [--top N] [--db PATH] \"query keywords\"", file=sys.stderr)
        return 2
    if not os.path.exists(db):
        print(f"IRIS+ catalog not found ({db}) — run build-iris-metrics.py. Show 'IRIS+ 매칭 준비 중'.",
              file=sys.stderr)
        return 3

    doc = json.load(open(db, encoding="utf-8"))
    metrics = doc.get("metrics", [])
    qtokens = tokens(query)
    ranked = sorted(((score(qtokens, m), m) for m in metrics), key=lambda x: x[0], reverse=True)
    hits = [(s, m) for s, m in ranked if s > 0][:top]

    if as_json:
        out = {
            "query": query,
            "source": doc.get("source", ""),
            "caveat": "참고용 유사 지표일 뿐, 공식 IRIS+ 매핑이 아님. 후보 목록 안에서만 고르고 코드를 창작하지 말 것.",
            "results": [{"id": m["id"], "name": m["name"], "score": s,
                         "definition": m["definition"][:300], "theme": m.get("theme", ""),
                         "sdgs": m.get("sdgs", "")} for s, m in hits],
        }
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        if not hits:
            print(f"No IRIS+ candidate for: {query}")
            return 0
        print(f"IRIS+ candidates for: {query}   (참고용, 공식 매핑 아님)")
        for s, m in hits:
            print(f"  [{s:4.0f}] {m['id']}  {m['name']}")
            print(f"         {m['definition'][:110]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
