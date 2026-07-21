#!/usr/bin/env python3
"""validate-render.py — deterministic fidelity gate for the RENDERED outputs (R01-R11).

The C-rules (validate-critical.py) check the DATA (toc.json); these R-rules check what the
LLM actually RENDERED into pdm.md / toc.md / monitoring.md — the layer where the 2026-07
pilot bugs lived (definitions leaking into OVI cells, timing in MoV, stray CLASS nodes,
missing level header, KOICA mentions in the ToC view). Pure Python, stdlib only.

Usage:
  python3 rules/validate-render.py <out_dir>           # report; exit 1 if any rule fails
  python3 rules/validate-render.py <out_dir> --json    # {"R01":"pass"|"fail"|"n/a",...}, exit 0

<out_dir> is the skill's output directory (contains pdm.md / toc.md and details/toc.json,
details/monitoring.md). Rules are n/a when their target file is absent.

Rules:
  R01 pdm.md   OVI cells carry indicator NAMES only — no indicator `definition` text anywhere
  R02 pdm.md   no indicator `timing` value anywhere (측정 시기 lives in monitoring.md)
  R03 pdm.md   no "추후 확정" placeholder (the matrix omits deferred values entirely)
  R04 toc.md   level header: bold markdown line above the block AND `:::lvl` chain in the graph
  R05 toc.md   no `class …` statement lines in the Mermaid block (stray-"CLASS"-node bug)
  R06 toc.md   every `classDef` carries color:#000 (dark-theme readability)
  R07 toc.md   renderer-independent text fallback block (with →) follows the Mermaid block
  R08 toc.md   no "KOICA" mention (also monitoring.md for ToC-view use-cases)
  R09 monitoring.md  성과 table columns match the use-case (intl-dev: 기초치 present;
                     ToC-view biz-dev/csr-esg/nonprofit: 기초치 absent)
  R10 toc.md   DRAFT → placeholder (no mermaid); GATE/AUDIT → mermaid present
  R11 toc.md   every outcome indicator appears in the diagram (no silent drops)
"""
import json, os, re, sys

TOC_VIEW = {"biz-dev", "csr-esg", "nonprofit"}


def read(path):
    try:
        return open(path, encoding="utf-8").read()
    except OSError:
        return None


def find_file(out_dir, name):
    for p in (os.path.join(out_dir, name), os.path.join(out_dir, "details", name)):
        if os.path.exists(p):
            return p
    return None


def mermaid_block(md):
    """First ```mermaid fenced block's inner text, or None."""
    m = re.search(r"```mermaid\s*\n(.*?)\n```", md, re.DOTALL)
    return m.group(1) if m else None


def after_mermaid(md):
    m = re.search(r"```mermaid\s*\n.*?\n```", md, re.DOTALL)
    return md[m.end():] if m else ""


def indicators(pdm):
    for oc in pdm.get("outcomes", []):
        for ind in oc.get("indicators", []) or []:
            yield "outcome", ind
    for op in pdm.get("outputs", []):
        for ind in op.get("indicators", []) or []:
            yield "output", ind


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if not args:
        print("usage: validate-render.py <out_dir> [--json]", file=sys.stderr)
        return 2
    out = args[0]

    toc_json_p = find_file(out, "toc.json")
    if not toc_json_p:
        print(f"details/toc.json not found under {out}", file=sys.stderr)
        return 2
    pdm = json.load(open(toc_json_p, encoding="utf-8"))
    meta = pdm.get("meta", {})
    use_case = meta.get("use_case", "intl-dev")
    gate = meta.get("gate_mode", "GATE")

    pdm_md = read(find_file(out, "pdm.md") or "")
    toc_md = read(find_file(out, "toc.md") or "")
    mon_md = read(find_file(out, "monitoring.md") or "")
    mm = mermaid_block(toc_md) if toc_md else None

    R = {}
    notes = []

    def set_rule(rule, ok, note=None):
        R[rule] = "pass" if ok else "fail"
        if not ok and note:
            notes.append(f"[{rule}] {note}")

    # ---- pdm.md rules ----
    if pdm_md is None:
        R["R01"] = R["R02"] = R["R03"] = "n/a"
    else:
        leaked = [i["name"] for _, i in indicators(pdm)
                  if len((i.get("definition") or "").strip()) >= 6
                  and i["definition"].strip() in pdm_md]
        set_rule("R01", not leaked, f"지표 정의문이 pdm.md에 노출: {leaked[:2]}")
        t_leaked = sorted({(i.get("timing") or "").strip() for _, i in indicators(pdm)
                           if len((i.get("timing") or "").strip()) >= 2
                           and (i.get("timing") or "").strip() in pdm_md})
        set_rule("R02", not t_leaked, f"측정 시기 값이 pdm.md에 노출: {t_leaked[:3]}")
        set_rule("R03", "추후 확정" not in pdm_md, "pdm.md에 '추후 확정' placeholder 출력됨")

    # ---- toc.md rules ----
    if toc_md is None:
        for r in ("R04", "R05", "R06", "R07", "R08", "R10", "R11"):
            R[r] = "n/a"
    else:
        # R10: draft gate
        if gate == "DRAFT":
            set_rule("R10", mm is None, "DRAFT인데 Mermaid 도식이 그려짐 (placeholder여야 함)")
        else:
            set_rule("R10", mm is not None, f"gate_mode={gate}인데 Mermaid 도식 없음")
        if mm is None:
            for r in ("R04", "R05", "R06", "R07", "R11"):
                R[r] = "n/a"
        else:
            pre = toc_md.split("```mermaid")[0]
            md_line = bool(re.search(r"\*\*[^\n]*사회문제[^\n]*→[^\n]*영향[^\n]*\*\*", pre))
            set_rule("R04", mm.count(":::lvl") >= 2 and md_line,
                     "레벨 헤더 누락 — 도식 내 :::lvl 체인과 블록 위 굵은 대목록 줄이 모두 필요")
            stray = re.findall(r"^\s*class\s+\S+", mm, re.MULTILINE)
            set_rule("R05", not stray, f"`class` 문장 라인 발견(유령 CLASS 노드 유발): {stray[:2]}")
            bad_defs = [ln.strip() for ln in mm.splitlines()
                        if "classDef" in ln and "color:#000" not in ln]
            set_rule("R06", not bad_defs, f"color:#000 없는 classDef: {bad_defs[:2]}")
            tail = after_mermaid(toc_md)
            fb = re.search(r"```[a-zA-Z]*\s*\n(.*?)\n```", tail, re.DOTALL)
            set_rule("R07", bool(fb and "→" in fb.group(1)), "Mermaid 아래 텍스트 인과 흐름(→) 폴백 블록 없음")
            missing = [i["name"] for k, i in indicators(pdm) if k == "outcome"
                       and len(i.get("name", "")) >= 5 and i["name"] not in toc_md]
            set_rule("R11", not missing, f"toc.md에서 누락된 성과지표: {missing[:2]}")
        koica_hit = "KOICA" in toc_md
        if use_case in TOC_VIEW and mon_md is not None:
            koica_hit = koica_hit or ("KOICA" in mon_md)
        set_rule("R08", not koica_hit, "ToC 산출물에 'KOICA' 언급 존재")

    # ---- monitoring.md rules ----
    if mon_md is None:
        R["R09"] = "n/a"
    else:
        headers = [ln for ln in mon_md.splitlines() if ln.strip().startswith("|") and "지표명" in ln]
        if not headers:
            set_rule("R09", False, "monitoring.md에서 지표 표 헤더(지표명)를 찾지 못함")
        else:
            oc_header = headers[0]  # 성과 (Outcomes) section renders first per the layout
            has_baseline = "기초치" in oc_header
            if use_case in TOC_VIEW:
                set_rule("R09", not has_baseline, "ToC 뷰인데 성과 표에 기초치/목표치 컬럼 존재")
            else:
                set_rule("R09", has_baseline, "intl-dev인데 성과 표에 기초치 컬럼 없음 (KOICA 양식 이탈)")

    order = [f"R{n:02d}" for n in range(1, 12)]
    if as_json:
        print(json.dumps({r: R.get(r, "n/a") for r in order}, ensure_ascii=False))
        return 0
    fails = [r for r in order if R.get(r) == "fail"]
    for r in order:
        print(f"  {r}: {R.get(r, 'n/a')}")
    for n in notes:
        print(f"  ! {n}")
    print(f"=> {'FAIL' if fails else 'OK'} ({len(fails)} render-fidelity violations)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
