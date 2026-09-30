# Feature: minuta-atenea-464-2026

Resumir la parte técnica del contrato interadministrativo **ATENEA-464-2026**
(ATENEA ↔ UNAL Sede Manizales) en un documento Markdown, y llevar ese resumen al deck
como **tres diapositivas nuevas** insertadas inmediatamente después de la portada
(`data-index="0"`).

- Feature doc: `odd/tasks/minuta-atenea-464-2026.md`
- Engram mirror: `odd/minuta-atenea-464-2026/tasks/tasks.md`
- Rama: `slides-admin`
- Fuente: `~/Downloads/MINUTA ATENEA 464-2026 UNAL_REVCC.pdf` (15 páginas)
- Estado: EN EJECUCIÓN

---

## 1. Plan

### 1.1 Objetivo

1. `docs/minuta-atenea-464-2026.md`: resumen técnico de la minuta con **objeto**, **alcance**,
   **objetivos** (conceptuales y técnicos), **entregables y compromisos técnicos de UNAL**,
   actividades relevantes y condiciones técnicas/legales que condicionan la ejecución.
2. `index.html`: tres diapositivas nuevas **después de la portada**:
   - **M1 · Objeto y objetivos** — qué se contrató y para qué.
   - **M2 · Compromisos** — los 8 componentes, los dos pagos y los hitos contractuales.
   - **M3 · Flujo de tiempo** — fases y entregables cada dos semanas hasta el cierre.

### 1.2 Hallazgo de alcance (limitación declarada)

La minuta **no incluye el Anexo Técnico** como anexo del PDF: solo lo referencia como
documento vinculante (cláusulas SEGUNDA, SÉPTIMA y VIGÉSIMA SEGUNDA). Por lo tanto:

- Los **nombres** de los 8 componentes (C1–C8) y su **agrupación en dos pagos** sí son datos
  literales de la minuta.
- El **detalle de actividades, productos por componente y cronograma oficial** vive en el
  Anexo Técnico y **no está en esta fuente**. No se inventa.
- La minuta **no tiene una sección formal de "objetivos específicos"**: los objetivos técnicos
  se derivan de las **obligaciones específicas del contratista** (cláusula TERCERA, literal b).
- El **cronograma quincenal** del slide M3 es un **plan de referencia derivado** (5 meses,
  10 quincenas), rotulado como tal en la diapositiva. No es el cronograma contractual.

### 1.3 Restricciones de implementación

- `assets/js/app.js` ordena las diapositivas por **posición en el DOM**
  (`querySelectorAll(".slide")`), no por `data-index`. `data-index` no se usa ni en JS ni en CSS.
- Los botones del rail usan `data-first` con el **índice posicional**; insertar 3 slides
  después de la portada **desplaza todos los `data-first` en +3**.
- `buildDots()` agrupa las pips por `data-module` y busca `#dots-<mod>`. Se añade un módulo
  de rail propio (`data-module="6"`, `#dots-6`) para que las slides nuevas sean alcanzables
  desde la navegación y no queden "invisibles" agrupadas con la portada.
- Sin cambios de CSS ni de JS: el marcado reutiliza `slide`, `slide-content`, `slide-kicker`,
  `slide-list`, `slide-figure`, `is-figure-wide` y el patrón de SVG inline existente
  (fuente Space Grotesk, cajas `rx=12` sobre `#F4F7FA`, paleta de acento del deck).

### 1.4 Superficies de edición

| Archivo | Cambio |
|---|---|
| `docs/minuta-atenea-464-2026.md` | nuevo (resumen técnico) |
| `index.html` | 3 `<article class="slide">` nuevas, 1 módulo de rail, `data-first` +3, `data-index` renumerado |
| `odd/tasks/minuta-atenea-464-2026.md` | nuevo (este documento) |
| `odd/minuta-atenea-464-2026/tasks/tasks.md` | nuevo (espejo) |

Sin commits: commit y push quedan a decisión del usuario (convención vigente del repo).

---

## 2. Tareas

- [x] T1 — Explorar la minuta, el deck y las convenciones del repo
- [x] T2 — Crear la rama `slides-admin` + doc de tarea
- [x] T3 — Redactar `docs/minuta-atenea-464-2026.md` (331 líneas, 10 secciones)
- [x] T4 — Insertar las 3 slides + módulo de rail + desplazar `data-first` + renumerar `data-index`
- [x] T5 — Levantar servidor local y verificar (render, overflow, navegación, conteo)
- [x] T6 — Reportar; commit y push a la rama `slides-admin` (sin merge a `main`)

### Ronda 2 — ajustes de contenido y cronograma oficial

- [x] T7 — Portada: enlace `lia.manizales.unal.edu.co` bajo el logo del laboratorio (+ regla `.cover-link`)
- [x] T8 — Slide 2: `h2` → **SDLC-IA Atenea**; retirar la cifra del alcance
- [x] T9 — Slide 3: `etapa 1` / `etapa 2` en lugar de “pago” y de cifras; SVG, subtítulo y `aria-label`
- [x] T10 — Slide 4: reconstruir el cronograma con el **cronograma oficial de la propuesta V3.0**
      (12 actividades + E1–E8) y sombreado de **HITO 1 (M1–M3)** y **HITO 2 (M4–M5)**
- [x] T11 — Actualizar `docs/minuta-atenea-464-2026.md` con §9.1 (E1–E8) y §9.2 (cronograma por mes)
- [x] T12 — Verificar en navegador y reportar

---

## 3. Evidencia

- `~/Downloads/MINUTA ATENEA 464-2026 UNAL_REVCC.pdf` — 15 páginas, 30 cláusulas; encabezado
  `CODIGO: F12_P11_C`, `VERSIÓN 1`, `FECHA: 23/04/2026`.
- Deck base: `main` @ `4d23022`, 41 slides (portada + 40), 6 módulos.

### 3.1 Resultado de la implementación

- `index.html`: 44 `<article class="slide">`, `data-index` secuencial 0–43; nuevo módulo de rail
  `data-module="6"` (`#dots-6`, 3 pips, label "Minuta ATENEA-464-2026", `data-first="1"`);
  `data-first` restantes desplazados a 4, 6, 9, 11, 15, 28 (verificado contra el orden real de las
  slides). `docs/` añadido; README actualizado a 44 slides / 7 módulos.
- Diff: **solo** atributos `data-first` (6), `data-index` (41) y el comentario `<!-- M0 -->` movido;
  ninguna línea de contenido de las slides preexistentes cambió. 315 inserciones / 48 borrados.
- Tag balance: `article` 44/44, `figure` 37/37, `svg` 38/38, `div` 75/75, `ul` 45/45, `li` 220/220,
  `text` 691/691, `tspan` 15/15, `abbr` 116/116. Los 13 `</rect>` no auto-cerrados son preexistentes.

### 3.2 Verificación en navegador (Chromium, 1440×900, servidor local `:8017`)

- `totalSlides = 44`, contador `01 / 44`.
- Las 3 slides nuevas renderizan con kicker, `h2`, bullets (5/5/4) y SVG (16/20/29 `<text>`) correctos;
  `aria-label` presente en los tres diagramas (633/784/815 caracteres).
- **Recorrido completo de las 44 slides**: 0 slides con desborde de `.slide-content`;
  desborde de `body` = 0px en ancho y alto.
- 0 elementos SVG fuera del `viewBox` en las 3 slides nuevas.
- Consola: único error = `GET /favicon.ico → 404` (preexistente; el repo no tiene favicon).
- Defecto detectado y corregido: el eje vertical del Gantt se dibujaba antes de las bandas alternas y
  quedaba tapado; reordenado (bandas → eje).
- Capturas: `/tmp` (3 slides del módulo Minuta + verificación de orden de bandas).

### 3.3 Entrega

- Commit único de contenido: **`f53b6e2`** — `feat(deck): add ATENEA-464-2026 contract context slides and technical summary`
  (5 archivos, 763 inserciones, 48 borrados).
- Rama **`slides-admin`** publicada en `origin` con upstream configurado:
  `local slides-admin == origin/slides-admin == f53b6e2`.
- **Sin merge a `main`** (verificado con `git merge-base --is-ancestor slides-admin main` → falso;
  `main` y `origin/main` siguen en `4d23022`).
- El workflow `Deploy to GitHub Pages` solo dispara con push a `main`, y no se registró ningún run:
  el push no desplegó nada.
- Verificación local posterior al commit (servidor `:8017`, recarga sin caché): 44 slides,
  `railOrderMatchesSlides = true`, 0 desbordes en las 44 slides, desborde de `body` = 0px.
- Estado final del árbol de trabajo: limpio.

### 3.4 Ronda 2 — fuente nueva y verificación

- **Fuente añadida:** `~/Downloads/4. Propuesta_ATENEA_IA_UNAL_Manizales_V3.0.docx.pdf` (13 secciones).
  Sección **9** → entregables **E1–E8** con momento estimado; sección **11** → cronograma de **12
  actividades** por mes con producto asociado; sección **10** → dirección del proyecto (profesores Jorge
  Iván Montes Monsalve y Andrés Marino Álvarez Meza). La propuesta **no usa** la palabra “etapa”.
- **Decisión de nomenclatura:** el deck usa `etapa 1` / `etapa 2` en lugar de “pago” y **no publica
  cifras**. Retirados de las slides: `$300.000.000 COP` y `$150.000.000` (×2). Las **cifras se conservan**
  en `docs/minuta-atenea-464-2026.md` por ser un resumen técnico interno — decisión registrada como
  pregunta abierta al usuario.
- **Cronograma del slide 4:** sustituido el plan derivado (10 quincenas, F1–F8) por el de la propuesta
  (5 columnas de mes, 12 filas de actividad + 8 filas de entregable, columna `Producto` con E1–E8,
  sombreado `HITO 1` en M1–M3 y `HITO 2` en M4–M5, diamantes de cierre de etapa).
  El SVG pasó de 70 a 126 líneas.
- **Verificación programática (Chromium, 1440×900, servicio en `:8017`):** 44 slides; enlace de portada
  con `href` correcto, `target="_blank"`, visible y con color de acento `rgb(138,90,0)`; 5 autores;
  `h2` de las tres slides = “SDLC-IA Atenea”, “Ocho componentes, dos etapas, un plazo”, “Cronograma y
  entregables por mes”; **0 desbordes** de contenido en las 44 slides; **0 elementos SVG** fuera del
  `viewBox`; desborde de `body` = 0px; balance `svg` 38/38.
- **Cifras restantes en `index.html`:** solo precios de modelos y de infraestructura en slides ajenas al
  contrato (líneas 1371–1451 y 4063–4126), fuera del módulo Minuta. Ocurrencias de “pago” dentro del
  módulo Minuta: 0.
