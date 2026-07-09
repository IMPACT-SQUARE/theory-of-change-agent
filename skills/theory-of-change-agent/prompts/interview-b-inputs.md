# Prompt: Interview — Mode B (inputs-held)

ROLE: The user already has materials (a concept doc, ToC draft, partial or existing PDM). Extract, then
fill only the gaps. Work in the user's language. One question per turn. Enforce `rules/koica-rules.md`.

## Steps

1. **Ingest** — `Read` the provided file(s). Extract whatever results-chain / PDM structure exists into
   the `results_chain` state.
   **HWP files (`.hwp`/`.hwpx`)** cannot be `Read` directly — convert to text FIRST (routing per the
   k-skill hwp convention):
   - **Route 1 (rich, local only):** if `hwpjs` is available on PATH (`command -v hwpjs` — the
     `@ohah/hwpjs` npm CLI), prefer `hwpjs to-markdown input.hwp -o out/details/input.md` — it keeps
     tables/structure. Do NOT `npm install` on the user's machine without asking.
   - **Route 2 (always works, bundled):** `python3 rules/hwp-extract.py input.hwp -o out/details/input.txt`
     — pure-stdlib extractor (hwpx = zip+XML full text; hwp 5.x = CFB → BodyText records; falls back to
     the PrvText preview). Works in the desktop/Antigravity sandbox where npm is unavailable.
   - **Route 3 (fallback):** exit code 3 means password-encrypted or 배포용 문서 with no readable text —
     tell the user in `meta.lang` and ask for a **PDF export** of the same document instead.
   Then `Read` the converted text and proceed. Tell the user the conversion happened (one line).
   Map non-standard / pre-2017 labels to the canonical levels:
   - 목적 (Project Purpose) → 성과 (Outcome); 목표 (Goal) → 영향 (Impact); 사업목적 → 성과;
     상위목표 → 영향. Record any structure that does not fit the schema (e.g. year-by-year targets,
     multiple outcome groupings) as notes; do NOT force it.
2. **Decide gate mode** — if the user indicates this is an **already-approved / existing** PDM, set
   `gate_mode = AUDIT` (report-only). If they are drafting a NEW PDM from partial inputs, keep `GATE`.
3. **Gap identification** — compare the extracted structure against the full results chain + indicator
   fields. List exactly what is missing or under-specified (per level).
4. **Targeted fill** — ask ONE question per gap, in priority order (structure before indicators).
   After gap-identify, tell the user how many gaps remain, then prefix each question with a progress line,
   e.g. `[질문 3 · 남은 빈칸 4개]`, counting down as gaps close.
   Confirm (don't re-ask) anything already provided: "Your draft sets the outcome as X — keep it?"
5. **Assumptions & indicators** — run the same development as Mode A stages 8-9, but ONLY for gaps.

## Rules
- Do not re-interview fields the document already answers — verify them instead.
- In AUDIT mode, do NOT push the user to "fix" guideline deviations; note them for the audit report.
- In GATE mode, the same Critical rules apply as Mode A.

OUTPUT OF THIS PHASE: a populated/validated `results_chain` ready for `generate-pdm.md` (GATE) or for the
audit report (AUDIT).
