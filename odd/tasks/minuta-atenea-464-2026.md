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

### Ronda 3 — nomenclatura de componentes

- [x] T13 — Slide 4: columna `Componente` con los códigos **C1–C8** espejo de la columna `Producto` (E1–E8)
- [x] T14 — Leyenda de columnas al pie del diagrama y `aria-label` ampliado con la correspondencia
- [x] T15 — Documentar en `docs/minuta-atenea-464-2026.md` §9.2 la correspondencia actividad → componente
      y marcarla explícitamente como **derivada** (no está publicada en ninguna fuente)

### Ronda 4 — cronograma a pantalla completa

- [x] T16 — Slide 4: eliminar la columna de texto y pasar la slide a `is-figure-full` (diagrama a todo el lienzo)
- [x] T17 — Rediseñar el SVG a `1200×736`: **actividades a la izquierda**, timeline de 5 meses al centro
      (con HITO 1 en M1–M3 y HITO 2 en M4–M5) y **entregables a la derecha**
- [x] T18 — Regla CSS `.slide.is-figure-full` + bump del `?v=` de `styles.css` para invalidar caché
- [x] T19 — Verificar en navegador (desktop 1440×900 y móvil 390×844)

### Ronda 5 — quitar el resalte de las siglas y revisión ortográfica

- [x] T20 — Quitar el subrayado punteado de `abbr[title]` (se confundía con un marcador de corrector)
- [x] T21 — Bump del `?v=` de `styles.css` para invalidar la caché del navegador
- [x] T22 — Revisión ortográfica del texto visible y de los `aria-label` del deck

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

### 3.5 Ronda 3 — columna `Componente` (C1–C8)

- El cronograma pasó a `viewBox="0 0 700 580"` (antes `660×568`) para alojar una segunda columna de
  códigos sin tocar la geometría de meses, barras ni separadores: columna `Producto` en `x=600` y
  `Componente` en `x=650`.
- **Correspondencia actividad → componente derivada** (no publicada en la minuta ni en la propuesta):
  C1 → kickoff y diagnóstico; C1/C3 → diagnóstico y priorización; C2 → SDLC-IA; C3 → arquitectura;
  C3/C4 → entornos y herramientas; C4 → agentes y skills; C4/C6 → pruebas y arneses; C4/C5 → integración;
  C6/C7 → despliegue y validación; C8 → workshop, documentación y cierre. Los 8 componentes quedan
  cubiertos. Registrada en `docs/minuta-atenea-464-2026.md` §9.2 como **punto frágil a validar**.
- **Verificación programática (Chromium 1440×900):** `viewBox` 700×580; **0 elementos** fuera del
  `viewBox`; **0 colisiones** entre la columna `Producto` y la columna `Componente` (comprobadas por
  `getBBox` fila a fila); 12 códigos E y 12 códigos C leídos en orden correcto; **0 desbordes** de
  contenido en las 44 slides; desborde de `body` = 0px; balance `svg` 38/38 y `text` 723/723.

### 3.6 Ronda 4 — layout a pantalla completa

- La slide 4 pasó de `slide is-figure-wide` a **`slide is-figure-full`** y perdió su `<div
  class="slide-content">` (21 líneas). El diagrama ocupa **99 % del ancho y 98 % del alto** de la slide.
- SVG reescrito a `1200×736`: columna izquierda de actividades (con prefijo **C**), columna derecha de
  entregables (con prefijo **E**), columna intermedia `E` con el producto asociado de cada actividad, y
  timeline central de 5 columnas de mes (`x=300…900`, 120 por mes) con los dos sombreados de hito.
- CSS nuevo (`.slide.is-figure-full`): `grid-template-columns: minmax(0,1fr)`,
  `grid-template-rows: minmax(0,1fr)` y `align-items: stretch`, con `.slide-figure { height: 100% }`.
  La especificidad `0,2,0` gana a la regla base `.slide` (`0,1,0`) **incluso dentro de los media
  queries**, porque `grid-template-rows` y `align-items` también están fijados en la regla nueva.
- **Falso negativo detectado y resuelto:** el CSS servido no se aplicaba porque el navegador reutilizó la
  caché con el `?v=20260929_1730` sin cambios. Se subió a `?v=20260929_2204` (convención del repo) y se
  recargó sin caché. Lección: cualquier cambio en `styles.css` requiere bumpear el `?v=` del `<link>`.
- **Verificación final (Chromium, viewport 1440×900, servidor `:8017`):** 44 slides; **0 desbordes**;
  **0 elementos SVG** fuera del `viewBox` en las 38 SVGs del deck; desborde de `body` = 0px;
  margen lateral del contenido dibujado ≈ 62 px sobre 5668 px (prácticamente full-bleed).
- **Móvil (390×844):** sin cambios respecto al comportamiento previo — en el media query la slide ya era
  de una columna, así que el ancho del diagrama es el mismo (~352 px) que antes. No es regresión, pero
  un Gantt de este tamaño es ilegible en un teléfono; pendiente ofrecido al usuario (scroll horizontal).

### 3.7 Ronda 5 — resalte de siglas y ortografía

- **Causa del “resalte”:** la regla `abbr[title] { text-decoration: underline dotted; text-underline-offset: 2px }`
  del feature de siglas marcaba **los 117 `<abbr>` del deck** con un subrayado punteado, indistinguible de
  un marcador de corrector ortográfico. Los fondos eran blancos normales: no había resaltado de color.
- **Arreglo:** `abbr[title] { text-decoration: none; cursor: help }`. Se conserva `cursor: help` para no
  perder el descubrimiento del tooltip, pero sin ninguna marca visual sobre el texto. `styles.css`
  re-versionado a `?v=20260929_2217`.
- **Verificación en Chromium:** 117 abbrs, `textDecorationLine` = `none` en **117/117**; `cursor` = `help`.
- **Revisión ortográfica — texto visible:** 0 errores reales. El único hallazgo del escaneo heurístico
  (“escenario”, slide 35) es un **falso positivo**: la palabra se escribe sin tilde.
- **Revisión ortográfica — `aria-label`:** **37 palabras sin tilde** en 13 slides (1, 2, 3, 7, 10, 11, 12,
  14, 19, 20, 21, 38, 39): `documentacion`, `metodologia`, `diagnostico`, `tecnica`, `autonomia`,
  `validacion`, `implementacion`, `definicion`, `especificacion`, `sesion`, `practica`, `integracion`,
  `presentacion`, `version`, `gestion`, `ultimo`, `segun`, `informacion`, `calculo`, `despues`,
  `politica`. Es una **convención previa del deck** (todos los `aria-label` se escribieron en ASCII);
  las slides 1–3 son las mías. **No es visible al ojo, pero es incorrecto para lectores de pantalla.**
  Se reporta al usuario con dos opciones (corregir solo las mías, o las 13) y no se cambia sin decisión.
- **Duplicados detectados por el escaneo (ambos falsos positivos o previos):**
  “plazo Plazo” en la slide 2 es el `h2` “…un plazo” seguido del primer bullet “**Plazo:**”;
  “Fuentes Fuentes” en la slide 43 (is-wide, preexistente) es el kicker “41 · Fuentes” seguido del `h2`
  “Fuentes”, que además conserva numeración de kicker desactualizada (“41” en la slide 44).
