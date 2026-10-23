# Agentes de <abbr title="Inteligencia Artificial">IA</abbr> en el ciclo de vida del desarrollo de software

Plataforma de presentaciones ejecutivas y técnicas sobre la implementación de agentes de <abbr title="Inteligencia Artificial">IA</abbr> en el ciclo de vida de la ingeniería de software (<abbr title="Software Development Life Cycle">SDLC</abbr>), desarrollada por el Laboratorio de Inteligencia Artificial (<abbr title="Laboratorio de Inteligencia Artificial">LIA</abbr>) de la Universidad Nacional de Colombia sede Manizales en el marco del Contrato Interadministrativo **ATENEA-464-2026**.

**Presentación en vivo: [https://liaunal.github.io/AgentPtProcess/atenea/](https://liaunal.github.io/AgentPtProcess/atenea/)**

---

## Panel de Control y Presentaciones Disponibles

El proyecto cuenta con un **Panel de Control interactivo** que permite seleccionar la presentación de interés en cualquier momento mediante el botón en la barra superior o presionando <kbd>P</kbd> / <kbd>M</kbd>:

1. **Kick-off: Propuesta y Adopción SDLC-IA** (`?deck=kickoff` o [`kickoff.html`](kickoff.html)):
   - 45 diapositivas estructuradas en 7 módulos (Minuta contractual, Motivación, Perfiles en evolución, Chat vs Agente, Evidencia empírica, La respuesta metodológica y UN-SpecWeaver).
   - Enfoque conceptual, pedagógico y de adopción institucional.
2. **Informe Técnico E1–E4: Contrato ATENEA-464-2026** (`?deck=e1-e4` o [`e1-e4.html`](e1-e4.html)):
   - 64 diapositivas (portada y 63 de contenido) en 6 módulos: Contrato & Alcance, E1 Diagnóstico, E2 Metodología SDLC-IA, E3 Arquitectura y caso de uso, E4 Agentes y skills con Aracne-SDLC-AI 0.9.0, y Decisiones & Cierre.
   - Alineado con el informe técnico vigente (`informe_atenea`, capítulos 1 a 7): cada figura y tabla lleva su leyenda con la numeración del informe (o "Fuente: §N.M" cuando no está numerada) y cada elemento de los componentes C1 a C4 (E1 a E4) tiene su diapositiva marcada con `data-item`.
   - Funciona en móvil: tablas como tarjetas, alternativas `.mobile-alt` para los diagramas y áreas táctiles de 44 px.

---

## Contenido de las Presentaciones

### A. Deck Kick-off (Propuesta Inicial)
| # | Módulo | Tema |
|---|--------|------|
| 0 | Minuta ATENEA-464-2026 | Objeto, objetivos, los ocho componentes técnicos, los dos pagos y el flujo quincenal |
| 1 | Motivación | Ciclo de vida tradicional y su reconstrucción con <abbr title="Inteligencia Artificial">IA</abbr> |
| 2 | Perfiles en evolución | Perfiles tradicionales, <abbr title="Product Owner">PO</abbr>/analistas de requerimientos y reparto <abbr title="Inteligencia Artificial">IA</abbr>/humano por etapa |
| 3 | Chat vs Agente | Diferencia chat/agente y benchmarks de agentes de código en el mercado |
| 4 | Evidencia | Estadísticas citadas de productividad y adopción, amplificación de <abbr title="Inteligencia Artificial">IA</abbr> y riesgos |
| 5 | La respuesta | Contexto amplio, ingeniería aplicada a la <abbr title="Inteligencia Artificial">IA</abbr> y flujo brief &rarr; <abbr title="Product Requirements Document">PRD</abbr> &rarr; épicas &rarr; memoria |
| 6 | <abbr title="Stack de especificaciones del deck">UN-SpecWeaver</abbr> | El stack de herramientas, tutorial práctico en terminal con comandos CLI y capturas reales |

### B. Deck E1–E4 (Informe Técnico de Avance ATENEA-464-2026)
Mapeo de componentes: C1 a C4 corresponden a los entregables E1 a E4. La portada y 62 diapositivas se reparten así:

| # | Módulo | Diapositivas | Tema |
|---|--------|--------------|------|
| 1 | Contrato & Alcance | 6 | Estado de E1 a E4 (Tabla 1.1), minuta, obligaciones, entregables y pagos, y cronograma S1 a S22 (Figura 2.1) |
| 2 | E1 · Diagnóstico ATENEA (C1) | 14 | Portafolio, roles, flujo actual, infraestructura, licencias, brechas, fricción, madurez, DORA, riesgos, datos y caso de uso priorizado |
| 3 | E2 · Metodología SDLC-IA (C2) | 15 | Seis fases y flujo, intervención agéntica, RACI, siete puntos de control, contexto, CI/CD, definición de terminado, cierre de brechas, distribución y ruta de adopción |
| 4 | E3 · Arquitectura y caso de uso (C3) | 12 | Composición del arnés, componentes y estado, y los ocho elementos del caso (proceso, requisitos, historias, agentes, flujos, integraciones, datos y aceptación) |
| 5 | E4 · Agentes y Skills (C4) | 10 | Aracne-SDLC-AI 0.9.0: flujo, 16 agentes, comandos y skills, instalación, interacción entre agentes, control humano, seguridad y trazabilidad |
| 6 | Decisiones & Cierre | 5 | Tres decisiones de ATENEA (§7.1), información pendiente (Tabla 7.1), compromisos (Tabla 7.2) y hoja de ruta Hito 1 a Hito 2 con la ruta de adopción |

---|--------|------|
| 1 | Contrato & Alcance | Objeto, partes UNAL/ATENEA, valor $300M, 22 semanas, 4 resultados y estado del Hito 1 |
| 2 | E1 · Diagnóstico ATENEA | Portafolio (SICOR Posmedia, CTI/EMA, Keycloak), roles, cuello de botella en revisión y stack técnico |
| 3 | E2 · Flujo SDLC-IA | Flujo de 6 fases (Entender, Decidir, Descomponer, Traducir, Construir, Cerrar) y 5 puertas humanas |
| 4 | E3 · Arquitectura Arnés | Arnés institucional propio LIA UNAL, soberanía en el repo y estrategia de modelos por tarea |
| 5 | E4 · Agentes & Skills | Catálogo de comandos CLI (/iniciar, /adoptar, /planear-olas, /construir, /cerrar) y banco de skills |
| 6 | Decisiones & Cierre | 3 decisiones prioritarias para ATENEA, tabla de 5 compromisos abiertos y hoja de ruta |

---

## Agent Presentador y Skill del Proyecto

El proyecto incluye la especificación formal del **Agent Presentador**:
- **Definición de Skill**: [`.agent/skills/presentador-atenea/SKILL.md`](.agent/skills/presentador-atenea/SKILL.md)
- **Manual Operativo**: [`agent-presentador.md`](agent-presentador.md)
- **Auditor Automatizado**: [`scripts/presentador_deck.py`](scripts/presentador_deck.py)

### Reglas Clave del Agent Presentador:
1. **Estilo Visual**: Tema claro de alto contraste (`#f4f7f3` / `#ffffff`), tipografía híbrida (`Source Serif 4` en títulos y `Space Grotesk` en cuerpo), tonos temáticos (`cyan`, `blue`, `purple`, `amber`, `emerald`, `rose`).
2. **Disposición**: Rejilla de 2 columnas (35% texto analítico con leads en negrita, 65% diagramas vectoriales SVG con `viewBox="0 0 520 360"` y atributos de accesibilidad).
3. **Gobernanza y Rigor**: Uso estricto de `<abbr>` para acrónimos, máximo 5 viñetas por diapositiva y fidelidad absoluta a las fuentes documentales y contractuales.

---

## Navegación y Atajos de Teclado

| Acción | Teclas |
|--------|--------|
| Siguiente slide | `→`, `PageDown`, `Espacio` |
| Slide anterior | `←`, `PageUp` |
| Primer / último slide | `Home` / `End` |
| **Panel de Control (Cambiar presentación)** | <kbd>P</kbd>, <kbd>M</kbd> |
| Modo enfoque / Pantalla completa | <kbd>F</kbd> |

---

## Ejecutar Localmente y Validar

No requiere compilación ni dependencias externas:

```bash
# Iniciar servidor local
python3 -m http.server 8000

# Auditar integridad de presentaciones y accesibilidad
python3 scripts/presentador_deck.py

# Auditar el deck E1-E4 (cobertura C1-C4, rail, viewports y móvil; requiere Playwright para Python)
python3 scripts/audit_e1e4_deck.py [--only coverage|rail|layout|mobile] [--shots DIR]

# Regenerar el deck E1-E4 y el index.html (nunca editar el HTML a mano)
python3 scripts/build_e1_e4.py && python3 scripts/assemble_index.py
```

Abre http://localhost:8000/ en tu navegador.
