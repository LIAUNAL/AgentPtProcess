# Manual de Operación: Agent Presentador · LIA UNAL

Este documento describe el rol, arquitectura, entrenamiento visual y directrices de ingeniería del **Agent Presentador** para el ecosistema de presentaciones web interactivas del Laboratorio de Inteligencia Artificial (LIA) de la Universidad Nacional de Colombia y el Contrato Interadministrativo ATENEA-464-2026.

---

## 1. Perfil del Agente

- **Identidad**: Arquitecto de Presentaciones Técnicas e Investigador Visual.
- **Entorno de Ejecución**: HTML5 / CSS3 moderno / JavaScript ES6 (sin dependencias ni frameworks pesados).
- **Proyectos de Referencia**:
  - `InformesAtenea`: Informe técnico y avance contractual de los entregables E1 a E4.
  - `agentesPtProcess`: Deck interactivo de propuesta (Kick-off) y nuevo deck de entregables (E1–E4).

---

## 2. Reglas del Estilo Visual

1. **Tema y Fondos**:
   - Fondo general: `#f4f7f3` con gradiente sutil verde (`rgba(8, 120, 77, 0.12)`) y cian (`rgba(0, 122, 159, 0.08)`).
   - Superficies de tarjetas (`.slide-content`, `.slide-figure`): Fondo blanco `#ffffff` con borde `#dde2ec` y radio de borde `16px`.
   - Efecto Glow temático: Cada diapositiva define un `--tone` y `--tone-glow` que tiñe los bordes del visor.
2. **Tipografía**:
   - Títulos de diapositivas (`h2`): `Source Serif 4`, serif elegante y legible en proyecciones.
   - Textos de contenido, kickers, botones y diagramas: `Space Grotesk`, sans-serif de trazo geométrico y técnico.
3. **Colores Temáticos de Diapositiva (`data-tone`)**:
   - `cyan`: Portada y contexto introductorio.
   - `blue`: Marco contractual, arquitectura y especificaciones.
   - `purple`: Metodología, flujos de procesos y ciclo de vida (SDLC).
   - `amber`: Diagnóstico actual, cuellos de botella y alertas.
   - `emerald`: Soluciones construidas, arnés y herramientas agénticas.
   - `rose`: Gobernanza, puertas de decisión humana y compromisos.

---

## 3. Disposición y Layout de las Diapositivas

1. **Estructura Estándar de 2 Columnas**:
   - Columna izquierda (`.slide-content`, 35%): Kicker, Título `h2`, viñetas con `<ul class="slide-list">`.
   - Columna derecha (`.slide-figure`, 65%): Diagrama vectorial SVG con `viewBox="0 0 520 360"`.
2. **Estructura de Portada (`.slide.is-cover`)**:
   - Logotipos institucionales alineados (ATENEA + UNAL LIA).
   - Título formal de la presentación en `Source Serif 4`.
   - Rejilla del equipo técnico y autores con sus cargos y roles.
   - Metadatos contractuales (Universidad, año, hito).
3. **Estructura de Diagrama Completo (`.slide.is-figure-full`)**:
   - Para cronogramas o mapas densos que ocupan todo el ancho, acompañados de su versión nativa en lista HTML para pantallas móviles (`.schedule-mobile`).

---

## 4. Reglas Editoriales y de Redacción

1. **Fórmulas de viñeta**:
   - Cada viñeta debe comenzar con una frase destacada en negrita: `<strong>Concepto clave:</strong> Detalle explicativo`.
   - Entre 4 y 6 viñetas por diapositiva para no saturar la carga cognitiva.
2. **Definición de Siglas**:
   - Utilizar `<abbr title="Definición completa">SIGLA</abbr>` para cualquier acrónimo técnico o legal.
3. **Fidelidad Documental**:
   - Toda afirmación de estado, plazos, valores o alcances debe corresponder exactamente con el informe técnico oficial (`InformeTecnicoE1-E4__Atenea_UNAL_2026.pdf` y la minuta ATENEA-464-2026).

---

## 5. Panel de Control de Presentaciones (Deck Switcher)

El Agent Presentador gestiona un panel interactivo que permite seleccionar y conmutar entre diferentes presentaciones:
- **Kick-off: Propuesta y Adopción SDLC-IA**: La propuesta conceptual de entendimiento de agentes en el SDLC (45 slides, 6 módulos + minuta).
- **Informe Técnico E1–E4: Contrato ATENEA-464-2026**: La presentación ejecutiva del avance del Hito 1 (64 slides: portada y 63 de contenido, 6 módulos: Contrato 6, E1 14, E2 16, E3 12, E4 10, Cierre 5; alineado con el informe vigente y con Aracne-SDLC-AI 0.9.0).
- **Mecanismos de activación**:
  1. Botón en la barra superior (rail).
  2. Atajo de teclado: `P` o `M`.
  3. Parámetro de URL: `?deck=kickoff` o `?deck=e1-e4`.
  4. Archivos independientes: `kickoff.html` y `e1-e4.html`.

### Convenciones del deck E1–E4

El deck se genera con `scripts/build_e1_e4.py` (luego `scripts/assemble_index.py`); nunca se edita el HTML generado.

1. **Cobertura**: cada elemento de C1 a C4 tiene una diapositiva marcada con `data-item="<id>"` que contiene una figura (SVG) o una tabla con su leyenda. La diapositiva lleva `data-module` (`e0` a `e5`).
2. **Leyendas en la numeración del informe**: `<figcaption class="fig-caption">Figura N.M — texto</figcaption>` o `<caption>Tabla N.M — texto</caption>`. Si el informe no numera la figura o la tabla, la leyenda es `Fuente: §N.M — texto` y la diapositiva lleva `data-caption-source="§N.M"`. Las tablas partidas en dos usan `(1/2)` y `(2/2)`.
3. **Estados con pills**: `<span class="pill pill--ok|partial|todo|risk">` (listo, parcial, por hacer, riesgo o pendiente); no se usan colores sueltos.
4. **Móvil**: todo diagrama con texto menor de 11 px en teléfono lleva una alternativa `<div class="mobile-alt">` (lista o tarjetas con el mismo contenido) como hijo directo de `figure.slide-figure`, junto al `<svg>`. Regla: el texto SVG se ve a 11 px o más en móvil, o hay `.mobile-alt`.
5. **Tablas**: cada `<td>` lleva `data-label="Columna"` para que se vean como tarjetas a 560 px o menos; si una celda mezcla texto con `<code>` o pills, esas celdas ya fluyen en línea (regla CSS de la tarjeta). Las tablas anchas que no caben como tarjetas usan `.is-scroll-x` en el contenedor.
6. **Auditoría**: `python3 scripts/audit_e1e4_deck.py [--only coverage|rail|layout|mobile] [--shots DIR]` debe terminar con código 0 (cobertura, rail, viewports 1920x1080, 1366x768 y 1280x720 sin recortes, y móvil sin scroll horizontal ni objetivos táctiles menores de 44 px). Con `--shots DIR` guarda una captura por diapositiva y viewport para revisarlas.
7. **Caché**: al cambiar `assets/css/styles.css` o `assets/js/app.js`, subir el sufijo `?v=` en `build_e1_e4.py`, `assemble_index.py` y `kickoff.html`.

---

## 6. Herramientas de Validación

El script `scripts/presentador_deck.py` audita:
- Correspondencia de IDs y contenedores de puntos (`dots-<mod>`).
- Integridad y accesibilidad de elementos SVG (`role="img"`, `aria-label`).
- Enlaces y rutas de imágenes (`assets/images/`).
- Consistencia del selector y modal del panel de control.
