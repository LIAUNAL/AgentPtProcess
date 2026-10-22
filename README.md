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
   - 21 diapositivas ejecutivas y técnicas estructuradas en 6 módulos (Contrato & Alcance, E1 Diagnóstico de software, E2 Metodología SDLC-IA de 6 fases y 5 decisiones humanas, E3 Arquitectura del arnés institucional, E4 Banco de agentes y skills, y Decisiones y compromisos).
   - Extraído con rigor técnico del informe de avance contractual (`informesAtenea/informe_atenea`).

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
| # | Módulo | Tema |
|---|--------|------|
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
```

Abre http://localhost:8000/ en tu navegador.
