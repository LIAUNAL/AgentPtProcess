# Feature: e1-e4-consistencia-informe

Update the E1–E4 deck ("Informe Técnico E1–E4: Avance de Hito 1") so it is consistent with the current informe (`/home/carlos/Documents/projects/actas/informe_atenea/`, HEAD 79827b1, 13 figures and 36 tables in chapters 1–7). Every requested C-item gets at least one figure or table, placed in its entregable. The deck must read well when projected and work on mobile.

- Feature doc: `odd/tasks/e1-e4-consistencia-informe.md` (Engram mirror: `odd/e1-e4-consistencia-informe/tasks`)
- Branch: `feat/e1-e4-consistencia-informe`
- Source of truth: `scripts/build_e1_e4.py`. It generates `e1-e4.html`; then `scripts/assemble_index.py` generates `index.html`.
- TDD: strict (session configuration). Runner: `python3 scripts/audit_e1e4_deck.py` (Python Playwright, with Chromium cached).
- Delivery strategy: ask-on-risk. The forecast exceeds 400 lines because the change is generated HTML in one build script; push and PR remain the user's decisions.
- Route: delegated direct. There is one sequential writer per task. Trigger: 2+ non-trivial files, plus reading that prepares the write.

## Full plan
See `/home/carlos/.claude/plans/we-need-to-update-snuggly-summit.md` for:
- the slide plan
- the fate of the current 28 slides
- the mobile rules
- the table-versus-SVG decisions

## Acceptance criteria
- Every item in the list below has a slide whose `data-item` marks it and holds a figure (SVG or table) with a visible caption in the current informe numbering:
  - C1 (5 items)
  - C2 (5, including installation, methodology distribution and the gaps it closes)
  - C3 (8)
  - C4 (4)
- Facts match the informe `.tex`.
- The rail links land on the correct slides.
- At the projector and mobile viewports, nothing is clipped, nothing overlaps and the page never scrolls horizontally.
- SVG text renders at 11px or more on mobile, or the slide has a `.mobile-alt` version.

## Tasks
- [x] T0 Write the audit script `scripts/audit_e1e4_deck.py` (coverage manifest, rail, viewports, mobile rules) and run it to RED.
- [x] T1 Infrastructure:
  - [x] compute `data-first` at runtime in `app.js`
  - [x] add CSS for captions, status pills, mobile cards (`td[data-label]`), `.mobile-alt`, sticky first column and tap targets
- [x] T2 Contract module, then the E1 module (C1, plus the prioritized use case).
- [ ] T3 E2 module (C2).
- [ ] T4 E3 module (C3: 8 elements).
- [ ] T5 E4 module (C4).
- [ ] T6 Closing module (chapter 7), slide counts, README, hub card and `agent-presentador.md`; then reassemble `index.html`.
- [ ] T7 Visual pass in Chrome (projector and mobile) and fixes; audit GREEN.

## Known informe conflicts (to report)
- The executive summary says "5 decisiones", section 4.4 lists 7 gates and section 6.6 lists 3. The deck uses 7 in E2 and 3 in E4.
- Chapter 6 says 182 tests and Annex B (table B.4) totals 162. The deck uses 182.

## Progress / evidence
(per task: route, commit, checks)

### T0 (done)
- Route: delegated direct (one writer; trigger: 2+ files plus preparatory reading).
- Commit: 890de1e `test(deck): agregar auditoría Playwright ...`.
- Command: `python3 scripts/audit_e1e4_deck.py` -> exit 1 (RED). coverage FAIL (27 items, none has `data-item`), rail FAIL (e3 landed 17 vs 19, e4 20 vs 22, e5 23 vs 25), layout PASS, mobile FAIL (216 problems: dots < 32px, rail titles/buttons < 44px, SVG text 4-9px, tables without `data-label`).

### T1 (done)
- Route: delegated direct.
- Changes: `app.js` computes rail targets from `data-module` (fallback `data-first`); CSS for `.fig-caption`/table captions, `.pill--ok|partial|todo|risk`, `.mobile-alt`, `td[data-label]` cards, `.is-scroll-x`, 44px tap targets, 32px dot hit area, safe-area; cache-buster `20261023_1` (css and js).
- Command: `python3 scripts/audit_e1e4_deck.py` -> coverage FAIL (27, expected: content in T2-T5), rail PASS, layout PASS, mobile FAIL (64 problems, all slide content: SVG text < 11px on 11 slides, tables without `data-label` on 12 slides; chrome tap targets now clean).
- Smoke: index.html?deck=kickoff (45 slides) and ?deck=e1-e4 (28) navigate with ArrowRight and rail click, no page errors.
- CSS conventions for later tasks: `slide[data-item]`, `figcaption.fig-caption` ("Figura N.M — ..."), `table > caption`, `.mobile-alt` as direct child of `figure.slide-figure` next to the `svg`, `td[data-label]`, `.is-scroll-x` on wrapper for wide tables, `.pill` variants.


### T2 (done)
- Route: delegated direct (one writer; generated e0+e1 block into `scripts/build_e1_e4.py`, regenerated `e1-e4.html` and `index.html`).
- Result: e0 = 6 slides, e1 = 14 slides (Tabla 3.3 split in two, Tabla 3.4 on its own slide for legibility); e3 use-case slide moved to e1 as SVG matrix without invented scores. Tables use inline `font-size:clamp(...)` tuned per table (no `dense`).
- Checks: coverage -> c1-madurez/brechas/riesgos/datos PASS; c1-caso-uso FAIL only because the caption is "Fuente: §5.4 - ..." (no numbered table in the informe; slide carries `data-caption-source="§5.4"`, audit regex needs an exception). rail PASS. layout PASS (all viewports). mobile: zero failures on e0/e1; 35 remaining are e2-e5 slides (expected). presentador_deck.py: 0 errors.
- Informe ambiguities: Tabla 3.3 says code is in Oracle Visual Builder while Fig 3.2 shows Azure DevOps under developers and Tabla 3.10 says "Oracle Cloud Service"; hito 1 groups E1-E4 but E4 also covers C5 (pago 2); §5.4 lists 3 candidates and 7 criteria but gives no per-candidate scores.
