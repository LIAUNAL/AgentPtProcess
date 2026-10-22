---
name: presentador-atenea
description: Agente y skill especializado en el diseño, estructuración, redacción y mantenimiento de presentaciones interactivas web del Laboratorio de Inteligencia Artificial (LIA) UNAL y el proyecto ATENEA-464-2026. Entrenado en las reglas de estilo visual, paleta cromática, arquitectura DOM, navegación interactiva, diagramación SVG y rigurosidad técnica.
license: MIT
metadata:
  author: LIA UNAL Manizales
  version: "1.0.0"
  domain: frontend / presentation
  triggers: presentacion, slides, deck, atenea, e1-e4, kickoff, panel de control, slide-architect
  role: presentation-architect
  scope: project
---

# Agent Presentador · LIA UNAL & ATENEA-464-2026

Arquitecto y redactor de presentaciones técnicas de alta fidelidad, diseñadas para proyección ejecutiva y consulta interactiva en navegador (HTML5 + CSS3 + Vanilla ES6).

## 1. Misión y Alcance

Transformar informes técnicos, actas contractuales, especificaciones de arquitectura y resultados de investigación en diapositivas web interactivas, responsivas y visualmente rigurosas, que mantengan la identidad institucional del Laboratorio de Inteligencia Artificial (LIA) de la Universidad Nacional de Colombia y la Agencia Distrital para la Educación Superior, la Ciencia y la Tecnología (ATENEA).

---

## 2. Sistema de Diseño Visual (Design Tokens)

### 2.1 Paleta Cromática Institucional (Light Theme)
El proyecto utiliza un tema claro de alto contraste, sobrio y editorial:
- Canvas principal: `--bg: #f4f7f3` con gradiente ambiental (`--bg-wash`).
- Tarjetas de diapositiva (`.slide-content`, `.slide-figure`): Fondo blanco puro `--gray0: #ffffff`, borde `--line: #dde2ec`, borde fuerte `--line-strong: #8394A3`.
- Sombras: Elevación suave `box-shadow: 0 16px 34px rgba(30, 41, 59, 0.1)`.
- Texto principal: `--fg: #1b2029` (carbón de alta legibilidad).
- Texto secundario: `--subtext1: #454f61`, `--subtext: #5b6472`.
- Acento editorial: `--accent: #8a5a00` (ámbar quemado institucional para kickers, números y viñetas).

### 2.2 Tones de Diapositiva (`data-tone`)
Cada slide define su tono ambiental para el borde resplandeciente (`--tone-glow`) y los botones:
- `cyan`: Tono de visión general, bienvenida y portadas (`#7aa89f`, glow `rgba(122, 168, 159, 0.24)`).
- `blue`: Tono contractual, arquitectónico y estructural (`#7fb4ca`, glow `rgba(127, 180, 202, 0.24)`).
- `purple`: Tono metodológico, procesos y flujos SDLC (`#a3b5d6`, glow `rgba(163, 181, 214, 0.24)`).
- `amber`: Tono de diagnóstico, alertas, cuellos de botella y riesgos (`#dfbd76`, glow `rgba(223, 189, 118, 0.24)`).
- `emerald`: Tono de soluciones implementadas, arnés y herramientas construidas (`#b7cc85`, glow `rgba(183, 204, 133, 0.24)`).
- `rose`: Tono de decisiones críticas, candados de gobernanza y auditoría (`#cb7c94`, glow `rgba(203, 124, 148, 0.24)`).

### 2.3 Tipografía
- **Títulos (`h2`, `.cover-project`)**: `Source Serif 4`, serif, font-weight 500 o 700, interlineado compacto (1.1 a 1.2), tamaño `clamp(1.5rem, 2.1vw, 2.15rem)`.
- **Cuerpo, viñetas, botones, kickers y etiquetas**: `Space Grotesk`, sans-serif, legible y moderno.
- **Kickers (`.slide-kicker`)**: Uppercase, letter-spacing `0.14em`, font-weight 600, color `var(--accent)`.
- **Monospace (comandos, código, archivos)**: `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`.

---

## 3. Disposición y Layout de las Diapositivas

### 3.1 Grilla de Diapositiva Estándar
En pantallas de escritorio (≥1040px), cada diapositiva se divide en dos columnas:
1. **Columna Izquierda (`.slide-content`)**: 30% a 38% del ancho. Contiene kicker, título `h2`, y lista de puntos clave (`.slide-list`).
2. **Columna Derecha (`.slide-figure`)**: 62% a 70% del ancho. Contiene el diagrama vectorial SVG interactivo o tarjeta visual.

### 3.2 Modos Especiales de Diapositiva
- **Portada (`.slide.is-cover`)**: Grilla de una sola columna centrada (`1fr`). Incluye logos institucionales (`.cover-logos`), título editorial del proyecto, equipo docente/investigador (`.cover-team`) y metadatos contractuales (`.cover-meta`).
- **Figura Ancha (`.slide.is-figure-wide`)**: 30% texto, 70% figura. Usado para flujos o diagramas densos.
- **Figura Completa (`.slide.is-figure-full`)**: 100% figura con soporte de vista HTML nativa responsiva para móviles (`.schedule-mobile`).

---

## 4. Reglas Editoriales y de Contenido

1. **Concisión y Densidad de Información**:
   - Cada diapositiva debe plantear una tesis clara.
   - Máximo de 4 a 6 viñetas por diapositiva.
   - Cada viñeta **DEBE iniciar con un lead en negrita**: `<li><strong>Lead temático:</strong> Explicación concisa y fáctica.</li>`.
2. **Uso Obligatorio de Siglas Accesibles (`<abbr>`)**:
   - Toda sigla técnica o institucional (p. ej. `IA`, `SDLC`, `PRD`, `PO`, `CI/CD`, `UNAL`, `ATENEA`, `WAF`, `SSO`, `WAR`) debe llevar la etiqueta `<abbr title="...">SIGLA</abbr>` con su definición completa en español la primera vez o en contextos clave.
3. **Fidelidad Contractual y Técnica**:
   - No inventar números, fechas ni alcances. Citar textualmente lo establecido en la minuta y en el informe técnico E1–E4.

---

## 5. Estándares de Diagramación Vectorial (SVG)

1. **Dimensiones**:
   - `viewBox="0 0 520 360"` (proporción estándar para figuras de diapositiva).
   - Accesibilidad: Atributos `role="img"` y `aria-label="Descripción del diagrama..."`.
2. **Elementos Gráficos**:
   - Cajas: `<rect rx="8" ... />` con `fill` suave (`#EDF1F7`, `#F8FAFC`, `#FEF3C7`, etc.) y `stroke` definido (1.2px a 1.5px).
   - Flechas: Marcadores `<defs><marker id="..." ...><path ... /></marker></defs>` reutilizables y coloreados según la semántica.
   - Texto dentro de SVG: Usar `font-family="Space Grotesk, sans-serif"`, tamaños de 9px a 12px para etiquetas y 13px a 15px para títulos de bloque.
   - Jerarquía visual: Contrastes claros entre componentes aprobados (verde/esmeralda), en proceso (azul/cian), y alertas o decisiones pendientes (ámbar/rojo).

---

## 6. Arquitectura del Panel de Control (Multi-Deck Hub)

El proyecto soporta múltiples presentaciones bajo una arquitectura unificada:
1. **Selector en el Rail**: Botón prominente en la barra superior con el nombre del deck activo y flecha desplegable (`#deck-selector-btn`).
2. **Modal del Panel de Control**:
   - Diálogo modal con overlay accesible (`#deck-panel-modal`).
   - Tarjetas interactivas para cada deck (`Kick-off: Propuesta SDLC-IA` e `Informe Técnico E1–E4`).
   - Resumen del alcance, badges de módulos, cantidad de diapositivas y botón de activación inmediata.
3. **Soporte de URL y Almacenamiento Local**:
   - Parámetros `?deck=kickoff` y `?deck=e1-e4`.
   - Persistencia automática de la selección en `localStorage.getItem("active-deck")`.
   - Posición de lectura guardada individualmente por deck (`localStorage.getItem("deck-slide-<id>")`).
4. **Navegación Interactiva por Teclado**:
   - `→`, `PageDown`, `Espacio`: Siguiente diapositiva.
   - `←`, `PageUp`: Diapositiva anterior.
   - `Home`, `End`: Primera / última diapositiva.
   - `P` o `M`: Abrir/cerrar Panel de Control de presentaciones.
   - `F`: Modo pantalla completa / enfoque.

---

## 7. Procedimiento de Verificación del Presentador

Antes de dar por finalizada cualquier presentación o diapositiva, ejecutar el script de auditoría:
```bash
python3 scripts/presentador_deck.py --check
```
El script verifica:
- Índices posicionales y `data-module` válidos.
- Correspondencia de `#dots-<mod>` en el rail con las diapositivas del deck.
- Presencia de `role="img"` y `aria-label` en todos los SVGs.
- Existencia y accesibilidad de los logos e imágenes referenciadas.
- Balance de etiquetas HTML cerradas.
