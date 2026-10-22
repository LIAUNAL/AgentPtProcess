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

### 2.1 Iteración 2: Hub Inicial Exclusivo, Remoción de Personal y Tablas/Diagramas Técnicos Completos (Capítulos 1 a 7)
- [x] Modificación de la pantalla de aterrizaje en `index.html`: ahora al abrir la raíz sin parámetros solo se muestra el **Hub Selector de Presentaciones** (`#deck-hub-view`), ocultando el visor de diapositivas hasta que se elija una presentación.
- [x] Eliminación de Juan Carlos Aguirre de todas las presentaciones y portadas.
- [x] Incorporación de todos los diagramas de flujo vectoriales SVG del informe técnico hasta el capítulo 7:
  - Cronograma de Gantt semanal S1 a S22 (Figura 2.1).
  - Flujo actual de un requerimiento en ATENEA con sus cuellos de botella (Figura 3.1).
  - Mapa de infraestructura y desarrollo actual en Azure (Figura 3.2).
  - Flujo SDLC-IA por etapas y carriles institucionales con las 5 compuertas humanas (Figura 4.1).
  - Composición de la propuesta y arquitectura institucional del arnés (Figura 5.1).
  - Flujo integral de artefactos de Aracne en 3 fases (Figura 6.1).
- [x] Incorporación de todas las tablas de datos estructuradas del informe técnico hasta el capítulo 7:
  - Condiciones generales del contrato (Tabla 2.1).
  - Obligaciones específicas del contratista (Tabla 2.2).
  - Componentes C1 a C8, Entregables E1 a E8 y esquema de pagos (Tablas 2.3 y 2.4).
  - Portafolio de sistemas y proyectos de ATENEA (Tabla 3.1).
  - Roles del ciclo de desarrollo y falencias asociadas (Tabla 3.2).
  - Stack tecnológico e inventario de licencias de IA (Tablas 3.3 y 3.4).
  - Matriz de los 10 puntos de fricción con datos probatorios (Tabla 3.5).
  - Intervención agéntica por etapa (Tabla 4.1).
  - Piezas de contexto del proyecto en el repositorio (Tabla 4.2).
  - Matriz de componentes de la propuesta (Tabla 5.1).
  - Comparación de candidatos a Caso de Uso frente a los 7 criterios (Tabla 5.2).
  - Sistema de agentes base de Aracne (Tabla 6.1).
  - Catálogo de comandos CLI y skills operativas (Tabla 6.2).
  - Compromisos de las sesiones técnicas (Tabla 7.1).
- [x] Exclusión estricta de tablas y figuras de la sección de anexos.
- [x] Total de diapositivas en E1–E4 ampliado a 26 diapositivas con maquetación responsiva y scroll interno en tablas.
- [x] Validación estructural completada con éxito en los tres archivos (`index.html`, `kickoff.html`, `e1-e4.html`).
