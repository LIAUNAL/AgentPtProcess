# Feature: panel-presentaciones-e1-e4

Implementar un panel de control interactivo para seleccionar entre la presentación **Kick-off** (existente en el proyecto) y la nueva presentación **E1–E4** (derivada del informe técnico del contrato ATENEA-464-2026 en `informesAtenea/informe_atenea`), manteniendo estrictamente la estética, diseño responsivo, diagramas SVG y arquitectura de navegación del proyecto. Asimismo, formalizar el **Agent Presentador** con sus reglas de estilo, disposición y validación técnica.

- Feature doc: `odd/tasks/panel-presentaciones-e1-e4.md`
- Rama: `main`
- Fuente del informe técnico: `/Users/andresalvarez/Documents/informesAtenea/informe_atenea/` (`InformeTecnicoE1-E4__Atenea_UNAL_2026.pdf` y secciones LaTeX)
- Estado: COMPLETADO

---

## 1. Plan

### 1.1 Objetivos

1. **Panel de Control (Deck Switcher & Hub)**:
   - Componente visual interactivo y accesible en la interfaz para seleccionar y alternar entre presentaciones:
     - **Kick-off**: Presentación conceptual y propuesta sobre agentes de IA en el SDLC (45 diapositivas, 6 módulos + minuta).
     - **E1–E4**: Nueva presentación ejecutiva y técnica de avance del Hito 1 contractual ATENEA-464-2026 al 21 de octubre de 2026 (20 diapositivas, 6 módulos).
   - Selector en la barra de navegación superior (rail) con indicador de deck activo y botón para abrir el panel modal.
   - Modal con tarjetas detalladas de cada presentación (kicker, título, descripción, badges de diapositivas y módulos, temáticas y botón de acción directa).
   - Soporte para parámetros de URL (`?deck=kickoff`, `?deck=e1-e4`) y persistencia del último deck seleccionado en `localStorage`.
   - Generación de archivos independientes `kickoff.html` y `e1-e4.html`, además de la experiencia integrada en `index.html`.

2. **Nueva Presentación E1–E4**:
   - Estructuración rigurosa basada en el informe técnico y contractual:
     - **Módulo 1: Contrato ATENEA-464-2026 y Alcance** (Objeto, partes UNAL/ATENEA, valor $300M, 22 semanas, 4 resultados clave, estado del Hito 1).
     - **Módulo 2: E1 · Diagnóstico Técnico y de Capacidades** (Portafolio SICOR Posmedia y CTI/EMA, Keycloak, equipo y roles, ausencia de arquitecto, cuello de botella en PO y revisiones, stack: Angular 13, Java 17/Spring Boot 3, WildFly 34, migración a Azure, sin CI/CD ni pruebas automatizadas).
     - **Módulo 3: E2 · Metodología SDLC-IA para ATENEA** (Flujo de 6 fases: Entender, Decidir, Descomponer, Traducir, Construir, Cerrar; 5 puertas humanas indelegables; descomposición en historias estimables con criterios de aceptación; contratos verificables).
     - **Módulo 4: E3 · Arquitectura y Arnés Institucional** (Arnés LIA UNAL, orquestador por componente, integración sin reemplazo con SharePoint, Figma, Azure Boards, Azure Repos, CI/CD; soberanía en el repo; modelos por tarea recomendados).
     - **Módulo 5: E4 · Banco de Agentes y Skills** (Catálogo de comandos CLI: Iniciar, Adoptar, Planear olas, Construir, Cerrar, Cambio, Defecto, Ticket, Estado, Diagnóstico; skills de método y planeación; ejecución sobre Claude Code / OpenCode).
     - **Módulo 6: Decisiones, Compromisos y Próximos Pasos** (Las 3 decisiones clave de ATENEA: caso de uso C3, accesos a herramientas, validación de E1; tabla de los 5 compromisos abiertos de las sesiones técnicas; roadmap hacia el hito 2).
   - Diagramas vectoriales SVG exclusivos y semánticos para cada diapositiva (viewBox `0 0 520 360`, markers, tipografía Space Grotesk, colores temáticos).
   - Siglas y términos técnicos con etiquetas `<abbr title="...">` completas.

3. **Agent Presentador**:
   - Especificación formal de skill en `.agent/skills/presentador-atenea/SKILL.md`.
   - Guía exhaustiva en `agent-presentador.md` con las reglas de estilo, disposición, paleta cromática, diagramación y diseño editorial.
   - Script de validación técnica en Python (`scripts/presentador_deck.py`) para auditar la integridad de las diapositivas, navegación, módulos, SVG y accesibilidad.
   - Registro en `.atl/skill-registry.md`.

---

## 2. Ejecución

- [x] Análisis del informe técnico E1-E4 y actas en `informesAtenea`.
- [x] Actualización de la rama principal (`git pull origin main`).
- [x] Creación del Agent Presentador (`.agent/skills/presentador-atenea/SKILL.md`, `agent-presentador.md`).
- [x] Implementación del script de auditoría y validación (`scripts/presentador_deck.py`).
- [x] Diseño y redacción de las 20 diapositivas de E1-E4 con sus diagramas SVG y etiquetas `<abbr>`.
- [x] Implementación de los estilos CSS del Panel de Control en `assets/css/styles.css`.
- [x] Actualización de la lógica de navegación multi-deck en `assets/js/app.js`.
- [x] Integración del Panel de Control y las presentaciones en `index.html`.
- [x] Creación de archivos individuales `kickoff.html` y `e1-e4.html`.
- [x] Verificación técnica integral con `scripts/presentador_deck.py` (0 advertencias, 0 errores).
