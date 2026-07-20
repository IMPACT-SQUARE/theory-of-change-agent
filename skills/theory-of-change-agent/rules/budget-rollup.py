#!/usr/bin/env python3
"""budget-rollup.py — deterministic rollup + validation for the pdm.json `budget` block.

Pure Python (stdlib only), same philosophy as validate-critical.py: the LLM never does
budget arithmetic — every sum, ratio, and derived amount comes from THIS script, and the
render prompt embeds the emitted numbers verbatim.

Usage:
  python3 rules/budget-rollup.py OUT/details/pdm.json          # human report (errors/warnings/totals)
  python3 rules/budget-rollup.py OUT/details/pdm.json --json   # computed rollup as JSON (for rendering)

Exit codes:
  0 = OK (warnings allowed)   1 = validation errors   2 = bad input   3 = no `budget` block
Checks (koica-rules.md §12):
  B01 line amount == unit_price × qty × freq × (months||1) when both basis & amount given
  B02 Σ(shares) == line amount (per line, when shares given)
  B03 (warning) 일반관리비 실효율 > caps.gm_rate (default 5%), base = 총사업비
  B04 every direct output_id / activity_id exists in the PDM results chain
  B05 (warning) PDM activities with NO budget line — 예산 미배정 활동
  B06 (warning) funder `pledged` vs rolled-up funder total mismatch
  B07 (warning) category cap breach — e.g. Σ(category="인건비") / 총사업비 > caps.personnel_rate
"""
import json, sys

TOL = 1.0  # KRW rounding tolerance


def line_amount(line):
    """Computed amount: prefer basis product; fall back to explicit amount."""
    b = line.get("basis")
    if b and b.get("unit_price") is not None and b.get("qty") is not None:
        return b["unit_price"] * b["qty"] * b.get("freq", 1) * (b.get("months") or 1)
    return line.get("amount")


def basis_str(line):
    b = line.get("basis")
    if not b or b.get("unit_price") is None:
        return ""
    parts = [f"{b['unit_price']:,.0f}원", f"{b.get('qty', 1):g}"]
    if b.get("freq", 1) != 1:
        parts.append(f"{b['freq']:g}회")
    if b.get("months"):
        parts.append(f"{b['months']:g}개월")
    return " × ".join(parts)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if not args:
        print("usage: budget-rollup.py <pdm.json> [--json]", file=sys.stderr)
        return 2
    try:
        pdm = json.load(open(args[0], encoding="utf-8"))
    except Exception as e:
        print(f"cannot read {args[0]}: {e}", file=sys.stderr)
        return 2

    budget = pdm.get("budget")
    if not budget:
        print("no `budget` block in pdm.json — 예산 미작성 (run prompts/budget-build.md first)")
        return 3

    errors, warnings = [], []
    funder_ids = [f["id"] for f in budget.get("funders", [])]

    # PDM ids for B04/B05
    act_ids = set()
    for a in pdm.get("activities", []):
        act_ids.add(a["id"])
        for s in a.get("sub", []) or []:
            act_ids.add(s["id"])
    out_ids = {o["id"] for o in pdm.get("outputs", [])}

    def check_lines(lines, ctx):
        total = 0.0
        computed = []
        for ln in lines:
            amt = line_amount(ln)
            if amt is None:
                errors.append(f"[{ctx}] 세목 '{ln.get('name','?')}': basis도 amount도 없음")
                continue
            # B01
            if ln.get("amount") is not None and ln.get("basis") and abs(amt - ln["amount"]) > TOL:
                errors.append(f"[B01 {ctx}] '{ln['name']}': amount {ln['amount']:,.0f} ≠ 산출근거 {amt:,.0f}")
            # B02
            sh = ln.get("shares")
            if sh:
                bad = [k for k in sh if k not in funder_ids]
                if bad:
                    errors.append(f"[B02 {ctx}] '{ln['name']}': unknown funder {bad}")
                if abs(sum(sh.values()) - amt) > TOL:
                    errors.append(f"[B02 {ctx}] '{ln['name']}': Σshares {sum(sh.values()):,.0f} ≠ amount {amt:,.0f}")
            else:
                warnings.append(f"[{ctx}] '{ln.get('name','?')}': 분담(shares) 미배분")
            total += amt
            if ln.get("category"):
                category_totals[ln["category"]] = category_totals.get(ln["category"], 0) + amt
            computed.append({"name": ln.get("name"), "amount": amt, "basis_str": basis_str(ln),
                             "basis_note": (ln.get("basis") or {}).get("note"),
                             "category": ln.get("category"),
                             "shares": sh or {}, "year": ln.get("year"), "note": ln.get("note")})
        return total, computed

    rollup = {"currency": budget.get("currency", "KRW"), "direct": [], "indirect": [],
              "funder_totals": {f: 0.0 for f in funder_ids}}
    category_totals = {}
    budgeted_acts = set()

    # ---- direct (관: 직접사업비) ----
    direct_total = 0.0
    for grp in budget.get("direct", []):
        oid = grp.get("output_id")
        if oid not in out_ids:
            errors.append(f"[B04] direct output_id '{oid}' not in PDM outputs")
        g = {"output_id": oid, "activities": [], "subtotal": 0.0}
        for act in grp.get("activities", []):
            aid = act.get("activity_id")
            if aid not in act_ids:
                errors.append(f"[B04] activity_id '{aid}' not in PDM activities")
            else:
                budgeted_acts.add(aid.split(".")[0] if "." in aid else aid)
                budgeted_acts.add(aid)
            t, lines = check_lines(act.get("lines", []), f"직접 {oid}/{aid}")
            g["activities"].append({"activity_id": aid, "subtotal": t, "lines": lines})
            g["subtotal"] += t
        direct_total += g["subtotal"]
        rollup["direct"].append(g)

    # ---- indirect (관: 간접사업비) ----
    indirect_total = 0.0
    for grp in budget.get("indirect", []):
        t, lines = check_lines(grp.get("lines", []), f"간접 {grp.get('name','?')}")
        indirect_total += t
        rollup["indirect"].append({"name": grp.get("name"), "subtotal": t, "lines": lines})

    # ---- general management (관: 일반관리비) ----
    # Real budgets set 일반관리비 as an explicit amount UNDER the 5% cap (not a flat 5%).
    # The cap's base is the **총사업비 (grand total, GM 포함)** — verified against two real
    # sheets whose printed GM ratios (1.34% / 1.38% / 4.86%) all equal GM/총사업비; one runs
    # at 5.11% of (직접+간접), i.e. the old base would false-flag a legitimate budget.
    # Explicit amount wins; `rate` only COMPUTES when amount is null (gm = rate×base/(1-rate)
    # so that gm/총사업비 = rate). B03 checks the 5% cap, never equality.
    gm = budget.get("general_mgmt") or {}
    caps = budget.get("caps") or {}
    gm_cap = caps.get("gm_rate", 0.05)  # 규정 상한 — 프로그램별로 다름 (인터뷰 초반에 고정; 기본 5%)
    rate = gm.get("rate", gm_cap)
    gm_amount = gm.get("amount")
    base = direct_total + indirect_total
    gm_final = gm_amount if gm_amount is not None else (rate * base / (1 - rate) if rate < 1 else 0.0)
    grand_pre = base + gm_final
    eff_rate = gm_final / grand_pre if grand_pre else 0.0
    if eff_rate > gm_cap + 1e-9:  # B03: 일반관리비 상한 (총사업비 대비)
        warnings.append(f"[B03] 일반관리비 실효율 {eff_rate:.2%} > 상한 {gm_cap:.0%} "
                        f"({gm_final:,.0f} / 총사업비 {grand_pre:,.0f})")
    rate = eff_rate  # report the effective rate (of 총사업비), not the nominal default

    # ---- funder totals ----
    for section in rollup["direct"]:
        for act in section["activities"]:
            for ln in act["lines"]:
                for k, v in ln["shares"].items():
                    rollup["funder_totals"][k] = rollup["funder_totals"].get(k, 0) + v
    for grp in rollup["indirect"]:
        for ln in grp["lines"]:
            for k, v in ln["shares"].items():
                rollup["funder_totals"][k] = rollup["funder_totals"].get(k, 0) + v
    for f in budget.get("funders", []):
        if f.get("pledged") is not None:
            got = rollup["funder_totals"].get(f["id"], 0)
            # 약정액이 일반관리비 포함으로 표기되는 경우가 실무 표준 — 차이가 일반관리비와
            # 정확히 일치하면 정상으로 본다 (B06 헛경고 방지).
            if abs(got - f["pledged"]) > TOL and abs(got + gm_final - f["pledged"]) > TOL:  # B06
                warnings.append(f"[B06] {f['name']} 약정 {f['pledged']:,.0f} vs 배분 합계 {got:,.0f} (일반관리비 제외 {got:,.0f} / 포함 {got + gm_final:,.0f} 어느 쪽과도 불일치)")

    # ---- B05: activities with no budget ----
    unbudgeted = sorted(a for a in act_ids if "." not in a and a not in budgeted_acts)
    if unbudgeted:
        warnings.append(f"[B05] 예산 미배정 활동: {', '.join(unbudgeted)}")

    # ---- per-year totals (연차별 합계 — 총괄시트의 연차 컬럼; 일반관리비 제외) ----
    year_totals = {}
    for section in rollup["direct"]:
        for act in section["activities"]:
            for ln in act["lines"]:
                year_totals[ln["year"] or "미배분"] = year_totals.get(ln["year"] or "미배분", 0) + ln["amount"]
    for grp in rollup["indirect"]:
        for ln in grp["lines"]:
            year_totals[ln["year"] or "미배분"] = year_totals.get(ln["year"] or "미배분", 0) + ln["amount"]
    declared_years = budget.get("years") or []
    for y in year_totals:
        if y != "미배분" and declared_years and y not in declared_years:
            warnings.append(f"세목 연차 '{y}'가 budget.years {declared_years}에 없음")

    grand = direct_total + indirect_total + gm_final
    # B07: 규정상 카테고리 비율 한도 (예: 인건비 ≤ 총사업비의 30%) — caps는 인터뷰 초반에 고정
    pr = (budget.get("caps") or {}).get("personnel_rate")
    if pr is not None and grand:
        got = category_totals.get("인건비", 0.0) / grand
        if got > pr + 1e-9:
            warnings.append(f"[B07] 인건비 비율 {got:.1%} > 한도 {pr:.0%} "
                            f"({category_totals.get('인건비',0):,.0f} / 총사업비 {grand:,.0f})")
    rollup.update({
        "category_totals": category_totals,
        "category_ratios": {k: v / grand for k, v in category_totals.items()} if grand else {},
        "caps": budget.get("caps") or {},
        "year_totals": year_totals,
        "direct_total": direct_total, "indirect_total": indirect_total,
        "general_mgmt": {"rate": rate, "amount": gm_final},
        "grand_total": grand,
        "ratios": {"direct": direct_total / grand if grand else 0,
                   "indirect": indirect_total / grand if grand else 0,
                   "general_mgmt": gm_final / grand if grand else 0},
        "funder_ratios": {k: v / grand if grand else 0 for k, v in rollup["funder_totals"].items()},
        "unbudgeted_activities": unbudgeted,
        "errors": errors, "warnings": warnings,
    })

    if as_json:
        print(json.dumps(rollup, ensure_ascii=False, indent=2))
    else:
        print(f"직접사업비  {direct_total:>18,.0f}")
        print(f"간접사업비  {indirect_total:>18,.0f}")
        print(f"일반관리비  {gm_final:>18,.0f}  (rate {rate:.1%})")
        print(f"총사업비    {grand:>18,.0f}")
        for k, v in rollup["funder_totals"].items():
            print(f"  분담 {k}: {v:,.0f} ({rollup['funder_ratios'][k]:.1%})")
        for y in (budget.get("years") or sorted(year_totals)):
            if y in year_totals:
                print(f"  연차 {y}: {year_totals[y]:,.0f} (일반관리비 제외)")
        for c, v in category_totals.items():
            print(f"  카테고리 {c}: {v:,.0f} ({v / grand:.1%})" if grand else "")
        for w in warnings:
            print(f"WARN  {w}")
        for e in errors:
            print(f"ERROR {e}")
        print(f"=> {'FAIL' if errors else 'OK'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
