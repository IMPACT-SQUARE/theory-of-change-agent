# Prompt: Build the budget block (PDM → 사업예산서, intl-dev MVP)

ROLE: After the PDM is **finalized** (gate passed), interview the user to build the `budget` block of
`OUT/details/toc.json`, mirroring the KOICA budget-sheet skeleton (koica-rules.md §12):
**관(직접/간접/일반관리) → 항(=PDM Output) → 목(=PDM Activity) → 세목(line)**. Then run the deterministic
rollup and render `out/budget.md` via `prompts/render-budget-md.md`.

Only for `meta.use_case = intl-dev` (MVP). One question at a time (티키타카), in `meta.lang`.

## Hard rules
- **NEVER do budget arithmetic yourself.** You collect 단가/수량/횟수/개월 and write them as `basis`;
  leave `amount: null` — `rules/budget-rollup.py` computes every amount, subtotal, ratio, and the
  일반관리비. The render embeds the script's numbers verbatim.
- **Never invent prices.** Every 단가 comes from the user (or their document). If the user doesn't know,
  leave the line out and it will surface as a B05 "예산 미배정 활동" warning — that's the honest state.
- The budget hangs off the **existing PDM ids** (`output_id`, `activity_id`) — never add chain nodes here.

## Interview flow
1. **재원 봉투 (funders).** Ask who funds the project and (if known) each pledge:
   e.g. KOICA 사업예산 + 파트너/수원기관 분담. → `budget.funders` (`pledged` optional).
   Derive `budget.years` from `inputs.koica.duration` (confirm: "3년 사업이면 1~3차년으로 잡을게요").
1b. **비율 프레임 — 규정 한도를 초반에 고정 (임팩톨로지 feedback 2026-07-21).** BEFORE collecting any
   line items, ask ONE question about the program's regulatory ratio limits and record them in
   `budget.caps`:
   - "비율 한도가 있나요? 예: **일반관리비 총사업비의 N% 이내**, **인건비 총사업비의 N% 이내**." →
     `caps.gm_rate` (default **0.05**; 사용자가 다른 값을 말하면 그 값), `caps.personnel_rate`
     (예: 0.3; 안 말하면 null = 검사 안 함). **Do NOT ask where the limit comes from** (규정 출처를
     되묻지 않는다 — user decision 2026-07-21); just take the numbers as stated.
   - **Never invent a limit** — defaults only where stated; the numbers vary by program.
   - From here on, tag every 인건비-type 세목 with `"category": "인건비"` so the deterministic check (B07)
     can total them. Relay the frame back: "일반관리비 {N}% · 인건비 {N}% 한도 안에서 잡겠습니다."
   The rollup enforces the frame: B03 checks 일반관리비 vs `caps.gm_rate`, B07 checks 인건비 vs
   `caps.personnel_rate` — breaches surface as warnings while you build, not at the end.
2. **직접사업비 — PDM Activity를 하나씩.** Iterate outputs (항) → their activities (목, via
   `from_activities`). For each activity ask: "이 활동에 어떤 비용이 드나요?" and capture 세목 lines.
   Offer the **산출근거 template** matching the cost type (user fills the numbers):
   - 인건비 → `월단가 × 인원 × 개월` (basis: unit_price=월단가, qty=인원, months=개월)
   - 지원금/투자 → `건단가 × 건수` (qty=건수)
   - 출장 → `단가 × 일수 × 횟수` (qty=일수, freq=횟수)
   - 행사/운영/기자재 → `단가 × 수량 × 횟수`
   Per line also ask (with defaults): **분담** (`shares` — default: 전액 주 공여자; per-line override OK)
   and **연차** (`year` — default 1차년 or 균등하게 나누고 싶으면 연차별 별도 라인).
   The user may **skip** an activity ("아직 몰라요") — do not press; B05 will flag it.
3. **간접사업비 (optional).** "현지사무소 운영이나 본부 사업지원 인건비 같은 간접비가 있나요?" →
   `budget.indirect` (결과사슬 밖 — PDM id에 연결하지 않는다).
4. **일반관리비.** Default `rate: 0.05` (KOICA 통상 5%), `amount: null` (script computes). Only change
   the rate if the user says so (>5% triggers a warning — tell them).

## Emit → verify → render
5. Write the `budget` block into `OUT/details/toc.json` (schema `budget` / `$defs.budget_line`).
6. Run `python3 rules/budget-rollup.py OUT/details/toc.json` —
   - **errors (exit 1)**: fix the data (B01 amount≠산출근거, B02 분담 합 불일치, B03 일반관리비,
     B04 없는 PDM id) and re-run. These are data bugs, not user questions.
   - **warnings**: relay to the user in `meta.lang` — B05 예산 미배정 활동 ("이 활동들엔 아직 예산이
     없어요 — 채울까요?"), B06 약정 vs 배분 차이, 분담 미배분 lines.
7. Render `out/budget.md` per `prompts/render-budget-md.md` (which re-runs the script with `--json`).

## PDM↔예산 connectivity (the point of doing this here)
After any later **PDM edit** (Phase 4), if the budget block exists, re-run `budget-rollup.py`: a removed/
renumbered activity turns its lines into B04 errors ("고아 예산 라인") — surface that immediately and ask
where the cost should move. Conversely a newly added activity shows up in B05 — nudge: "새 활동에 예산을
배정할까요?"
