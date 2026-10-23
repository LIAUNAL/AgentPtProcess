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
- [x] T3 E2 module (C2).
- [x] T4 E3 module (C3: 8 elements).
- [x] T5 E4 module (C4).
- [x] T6 Closing module (chapter 7), slide counts, README, hub card and `agent-presentador.md`; then reassemble `index.html`.
- [x] T7 Visual pass in Chrome (projector and mobile) and fixes; audit GREEN.

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

### T3 (done)
- Route: delegated direct (one writer; e2 block generated into `scripts/build_e1_e4.py`, regenerated `e1-e4.html` and `index.html`). Trigger: 2+ non-trivial files plus preparatory reading.
- Commit: 1e10399 `feat(deck): alinear módulo E2 con el informe y agregar roles, puertas, criterios, brechas y distribución`.
- Result: e2 = 15 slides (indices 21-35 in the deck): rediseño (full, §4.1), 2 concept maps (unchanged), Fig 4.1 flow (full), Tabla 4.1 (full, 6 columns, 8 rows), organización (§4.3), RACI Tabla 4.2, puntos de control (7 gates, §4.4), contexto Tabla 4.3 (3 SVG cards), CI/CD (§4.6), Tabla 4.4 split 1/2 and 2/2, Fig 4.2 brechas, Fig 4.3 + Tabla 4.5 distribución, ruta de adopción (§4.8). The old "5 puertas" content is replaced by the 7-gate strip.
- Lessons: a full-width table slide needs `style="flex:1 1 auto;min-height:0;height:auto"` on the wrapper (the `figcaption` CSS rule does not apply to `<caption>`); the three two-column SVG slides failed the 844x390 landscape rule, so they became full slides with `.mobile-alt`; the table `clamp()` minimum of 0.72rem must be lowered for 8-row tables.
- Checks: coverage -> all c1-* and c2-* PASS (only c3-*/c4-* fail, expected); rail PASS; layout PASS (1920x1080, 1366x768, 1280x720); mobile -> zero failures on e0-e2, 21 remaining on e3-e5 (expected); presentador_deck.py -> 0 errors.
- Informe ambiguities: §4.4 intro points to a "decision" column in Tabla 4.1 and gate markers in Fig 4.1 (4 red gates: firma del acta, aprueba spec y criterios, revisión y merge, despliegue), while the section lists 7 gates (the deck uses 7); Fig 4.1 shows the gate "firma del acta" under Negocio but Tabla 4.1 puts the spec approval with the líder de producto; Tabla 4.1 says Seguimiento "no existe" today; Fig 4.3 gives no "sí" branch for the periodic validation; Tabla 4.1 is shown condensed (wording shortened, same six columns); the informe has no numbered figure/table for §4.3, §4.4, §4.6 and §4.8 (captions use "Fuente: §N.M").

### T4 (done)
- Route: delegated direct (one writer; e3 block replaced in `scripts/build_e1_e4.py`, regenerated `e1-e4.html` and `index.html`). Trigger: 2+ non-trivial files plus preparatory reading.
- Commit: 57b0014 `feat(deck): agregar los ocho elementos de C3 y alinear la composición de E3 con el informe`.
- Result: e3 = 12 slides (deck indices 36-47): Fig 5.1 composición (full SVG, tipos de herramienta sin marcas), Tabla 5.1 split 1/2 (7 piezas del arnés) and 2/2 (6 herramientas de ATENEA) with status pills, Fig 5.2 levantamiento C3, then one slide per C3 element: c3-proceso (Tabla 5.2, 4-stage cards SVG), c3-requisitos (Tabla 5.3 table), c3-historias (Tabla 5.4 story-card SVG), c3-arquitectura-agentes (Tabla 5.5 6-phase pipeline SVG), c3-flujos (Tabla 5.6 table), c3-integraciones (Tabla 5.7 hub-and-spoke SVG), c3-datos (Tabla 5.8 table with Sí/No pills), c3-aceptacion (Tabla 5.9 table grouped por historia / punta a punta). All SVG slides carry `.mobile-alt`. The old invented-score slide was already gone (T2).
- Checks: coverage -> all c1-*, c2-*, c3-* PASS (only c4-* fail, expected); rail PASS; layout PASS; mobile -> zero failures on e0-e3, 16 remaining on e4-e5 slides; presentador_deck.py -> 0 errors. Screenshots reviewed at 1920x1080, 1366x768 and iPhone; fixed cramped SVG text, clipped borders (viewBox padding), table font size.
- Informe ambiguities: Tabla 5.7 names products (Keycloak, SharePoint, Figma, Azure Repos, Azure Pipelines) although §5.1 keeps tool types, so the deck follows each table as written; Fig 5.2 labels the elements 5.5-5.12 as sections and Tabla 5.5 cites BMAD/graphify/aracne-* names; Tabla 5.3 origins cite Tabla 3.3/3.10/4.4 and §6.9 (deck shows them as written; the source tags such as R2, R4 are omitted); Tabla 5.1 says the arnés is "implementado y probado fuera de ATENEA" yet "forma de uso por definir" (shown as ok pill plus qualifier); §5.4 caso de uso (candidates) is in E1 since T2.

### T5 (done)
- Route: delegated direct (one writer; e4 block replaced in `scripts/build_e1_e4.py`, regenerated `e1-e4.html` and `index.html`). Trigger: 2+ non-trivial files plus preparatory reading.
- Commit: e211875 `feat(deck): alinear módulo E4 con Aracne-SDLC-AI 0.9.0 y agregar instalación, interacción, control humano, seguridad y trazabilidad`.
- Result: e4 = 10 slides (deck indices 48-57): Fig 6.1 flujo (full SVG, 3 fases, bucle de cambio), Tabla 6.1 split 1/2 and 2/2 (16 agent cards by phase with `aracne-*` id, origin colors), Tabla 6.2 split 1/2 (8 comandos) and 2/2 (3 comandos + 4 familias de skills), Fig 6.2 instalación (3 folder trees + `npx aracne-sdlc-ai init` + versiones fijadas), Fig 6.3 secuencia (10 participantes, 6 bandas, 3 puertas), Fig 6.4 recorrido 0-13 (7 puertas rojas: pasos 2, 3, 4, 6, 7, 11, 12) plus the 3 gates of §6.6, Tabla 6.4 seguridad (8 filas, terminal sin restricción en `/sw:build` y `/sw:bug`), trazabilidad §6.9 (cadena requisito a integración, `trace.json`, `changelog.jsonl`, 182 pruebas). All SVG slides carry `.mobile-alt`; tables use `td[data-label]` with a single `<span>` per mixed-content cell (a grid cell with inline code/pills would otherwise split into several grid items on phones).
- Checks: coverage PASS (all c1-c4 items); rail PASS; layout PASS (1920x1080, 1366x768, 1280x720); mobile -> zero failures on e0-e4, 8 remaining all on e5 slides (#58-#60, T6); presentador_deck.py -> 0 errors. Screenshots reviewed at 1920x1080, 1366x768 and iPhone; fixed clipped card text, arrow crossing a band title, gate label over the red dot, node text overflow.
- Informe ambiguities: Tabla 6.3 (14 steps) is not shown as a table (14 rows would not be legible; Fig 6.4 carries the same steps); the informe never names "UN-SpecWeaver"; Fig 6.4 marks 7 gates while §6.6 lists 3 (deck shows both, labelled); §6.9 chain is requisito, historia, contrato, código, prueba, integración (the brief listed necesidad, PRD, historia, contrato, código/prueba, cierre; the deck follows the informe); Tabla 6.1 counts the Revisores row as one of the 16 agents (8 Gentle-AI subagents behind it); 182 tests (§6.9) vs Annex B table B.4 total 162 (deck uses 182); `aracne-cicd` uses the GitHub CLI in 0.9.0 and needs adaptation for Azure DevOps.

### T6 (done)
- Route: delegated direct (one writer; e5 block replaced in `scripts/build_e1_e4.py`, CSS card fix, hub card, README, `agent-presentador.md`; regenerated `e1-e4.html` and `index.html`).
- Commits: see git log (`feat(deck): alinear cierre de E1-E4 con el capítulo 7 del informe`, `fix(deck): mantener celdas con código y pills en una sola línea en tarjetas móviles`, `docs(deck): actualizar conteos, README y guía del presentador para E1-E4`).
- Result: e5 = 5 slides (deck indices 58-62): decisiones §7.1 (SVG + mobile-alt), Tabla 7.1 información pendiente split 1/2 (6 filas) and 2/2 (5 filas), Tabla 7.2 compromisos (5 filas, pills abierto/parcial), hoja de ruta Hito 1 a Hito 2 (Fig 2.1) with the 4-step ruta de adopción §4.8 (SVG + mobile-alt). Deck totals: 63 slides (cover + 62) in 6 rail modules: e0 6, e1 14, e2 15, e3 12, e4 10, e5 5.
- Part B: the mixed-content split was a CSS cause (`td` as grid made each inline child its own grid item). Fixed once in `assets/css/styles.css` (td as block, label positioned), no per-cell spans needed. Cache-buster now `20261023_2` (build script, `assemble_index.py`, `kickoff.html`).
- Checks: `python3 scripts/audit_e1e4_deck.py` exit 0 (coverage, rail, layout, mobile PASS); `python3 scripts/presentador_deck.py` 0 errors; index.html?deck=kickoff (45 slides) and ?deck=e1-e4 (63) load with no page errors; screenshots reviewed at 1920x1080, 1366x768 and iPhone (e5, Tablas 5.1, 5.8, 3.10, 7.1).
- Finding: `kickoff.html` opened standalone shows 0 slides, pre-existing (same at 92e4e50): `initApp` picks `e1-e4` when `document.querySelector("[data-deck='e1-e4']")` matches the deck-selector card inside kickoff.html, and no slide has that deck. Not changed (out of scope); a fix would scope the query to `.slide[data-deck='e1-e4']`.
- Informe notes: the informe has no "próximos pasos" section (roadmap slide uses Fig 2.1 and §4.8); Tabla 7.2 lists a Subgerencia de TIC responsible for commitment 3; Tabla 7.1 references use the deck numbering (3.7 madurez, 3.8 DORA, 3.9 riesgos, 3.10 datos, 4.2 RACI, 4.4 terminado, 5.7, 5.8, 6.4, anexos D and E).

### T7 (fix part done; T7 stays open for the final visual pass)
- Route: delegated direct (one writer). Honest note: the earlier green layout results (T2-T6) were measured on the standalone `e1-e4.html`, whose shell (`main.deck-viewport > section.stage`) had no CSS, so slides covered the rail and footer and got the full window height. The standalone now uses the same shell as `index.html` and the audit defaults to `--target index`; on the real shell the layout check initially reported 47 problems at 1366x768 and 1280x720 (tables and figures clipped vertically) and 3 landscape-mobile problems (#1, #2, #35).
- Commits: 9c24ebc `fix(deck): usar el mismo contenedor de index en e1-e4.html independiente`; then `fix(deck): ajustar tablas al alto disponible ...` and `test(deck): auditar la vista de index por defecto ...` (see git log).
- Approach: `fitSlide()` in `assets/js/app.js` runs for the active slide on render, resize, orientationchange and fonts ready. It steps table font-size down 0.5px from the authored size to a 12px floor until the wrapper, figure and text column stop overflowing, then adds `.is-tight` (smaller paddings) and, for text columns, `.is-compact` (smaller list). It is skipped in single-column mobile (<=560px or portrait <=1000px) and in short landscape (<560px height). CSS: `.mobile-alt` is also shown (scrollable) in landscape <=520px height; `.fit-grid` (slide #16, svg + DORA table) takes the remaining height at projector size.
- Split: Tabla 4.1 (c2-fases) is now two slides (1/2: Entender a Traducir; 2/2: Construir a Incidentes), same data-item; no facts dropped. Deck totals: 64 slides (cover + 63), e2 = 16; README, `agent-presentador.md`, hub card and kickoff card updated. Cache-buster `20261023_3`.
- Audit: table body text (td computed font-size) must be >= 12px at the three projector viewports; the check is in `layout`.
- Checks: `python3 scripts/audit_e1e4_deck.py` (index) coverage/rail/layout/mobile PASS; `--target standalone` all PASS; `python3 scripts/presentador_deck.py` 0 errors; kickoff (45 slides) navigates at 1920x1080, 1366x768 and 1280x720 with no page errors. Screenshots in the scratchpad `t7fix` folder reviewed (#16, #25, #27, #32, #52, #18 at 1280x720/1366x768; #1, #2 landscape).
- Pending: the parent's final visual pass.


### T7 closing (parent)
- Route: parent inline for the small fixes; one delegated writer for the fit work (recorded above).
- The Chrome extension could not reach this machine's local servers (no request reached the server log), so the visual pass used Playwright screenshots (real Chromium) at 1920x1080, 1366x768, 1280x720, iPhone 13, Pixel 7, iPad and 844x390, read as contact sheets.
- The user asked mid-task to remove WildFly (and its version), PostgreSQL and Moodle from the deck: 4ee81fd (14 edits, 0 mentions left in e1-e4.html).
- 9c3a1ae: the table fit is scoped to the E1-E4 deck, so the Kick-off layout is unchanged; cache-buster 20261023_4.
- 771ed2f: the audit now detects SVG content drawn outside its viewBox. It failed (RED) only on slide 3, "Estado E1–E4", where the E4 card was clipped at every size.
- e3b872d: that viewBox was widened to 0 0 520 392 (GREEN).
- Final checks:
  - `python3 scripts/audit_e1e4_deck.py` (index): coverage, rail, layout and mobile all PASS.
  - `--target standalone`: all four PASS.
  - `presentador_deck.py`: 0 errors.
- Known limits, outside E1–E4 scope and left as they were:
  - In phone landscape, the index chrome (deck chips plus rail) takes about half of the 390px height.
  - `kickoff.html` opened on its own shows 0 slides. In `initApp`, `[data-deck='e1-e4']` matches the hub card.
  - The kickoff card still says "5 puertas humanas".

### Independent verification (parent)
- Risk assessment (`gentle-ai review assess`, RDD off): high (process_boundary in scripts) -> independent read-only verifier.
- Result: 58 captions and ~190 facts checked; 0 wrong facts or captions. Fixed: Tabla 5.1 (2/2) subtitle, Tabla 4.1 (2/2) wording, removed unsupported "Habilita/Cierra" links on §7.1 slide, counter default 01 / 64.
- Left as-is and reported to the user: concept maps (slides 23–24) and cover team names are not in the informe (pre-existing deck content); Tabla 3.10 says "Oracle Cloud Service" while Tablas 3.3/5.7 say Oracle Visual Builder (informe-internal).
- After fixes: audit (index) 4/4 PASS; presentador_deck.py OK.
