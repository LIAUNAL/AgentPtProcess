# Minuta ATENEA-464-2026 — resumen técnico

Resumen de la parte técnica de la minuta del **Contrato Interadministrativo No. ATENEA-464-2026**
suscrito entre la **Agencia Distrital para la Educación Superior, la Ciencia y la Tecnología — ATENEA**
(en adelante, la AGENCIA) y la **Universidad Nacional de Colombia — Sede Manizales** (en adelante, el
CONTRATISTA).

- **Fuente:** `MINUTA ATENEA 464-2026 UNAL_REVCC.pdf` (15 páginas, 30 cláusulas).
- **Formato de origen:** `CODIGO: F12_P11_C` · `VERSIÓN: 1` · `FECHA: 23/04/2026` · Proceso Gestión Contractual.
- **Alcance de este documento:** solo lo que la minuta dice. El **Anexo Técnico** se cita como documento
  vinculante pero **no forma parte del PDF**; ver [§9 Vacíos](#9-vacíos-e-información-no-incluida-en-el-pdf).

---

## 1. Identificación del contrato

| Campo | Valor |
|---|---|
| Tipo | Contrato interadministrativo |
| Número | ATENEA-464-2026 |
| Contratante / AGENCIA | Agencia Distrital para la Educación Superior, la Ciencia y la Tecnología — ATENEA (NIT 901.508.361-4) |
| Contratista / UNAL | Universidad Nacional de Colombia, Sede Manizales (NIT 899.999.063-3) |
| Ordenador del gasto (AGENCIA) | Diana Consuelo Blanco Garzón, Gerente de Gestión Corporativa (Res. 023 de 2024; delegación Res. DG-080 de 2025) |
| Ordenador del gasto (UNAL) | Juan Carlos Chica Mesa (Res. 102 de 2024; delegación Res. 1551 de 2014) |
| Valor total | **$300.000.000 COP** (cláusula SEXTA) |
| Plazo | **Hasta 5 meses** desde la suscripción del acta de inicio (cláusula CUARTA) |
| Lugar de ejecución | Bogotá D.C. (cláusula QUINTA) |
| Supervisión | Subgerente de Tecnologías de Información y Comunicaciones, o quien designe el ordenador del gasto (cláusula OCTAVA) |
| Códigos de la solicitud | `8122_1_883141_TIC_CTTO_077`, `8029_4_883141_TIC_CTTO_042`, `8122_1_883141_TIC_CTTO_043` |

**Perfeccionamiento y ejecución (cláusula TRIGÉSIMA).** El contrato se perfecciona con el acuerdo sobre
objeto y contraprestación elevado a escrito. La **ejecución** exige, además: registro presupuestal,
**aprobación de garantías** por la AGENCIA y **acta de inicio**. El perfeccionamiento en SECOP II se
entiende completo con la aprobación de las partes en la plataforma.

---

## 2. Objeto del proyecto

**Cláusula PRIMERA — Objeto (literal):**

> Prestar servicios para fortalecer las capacidades institucionales de la Agencia para mejorar
> el ciclo de vida de la ingeniería de software, mediante el uso de inteligencia artificial.

**Lectura técnica del objeto.** No es un contrato de desarrollo de software por demanda. Es un contrato de
**fortalecimiento de capacidades institucionales**: el entregable real es la capacidad de la AGENCIA de
operar su propio ciclo de vida de desarrollo mediado por IA, no únicamente un producto desplegado. Esa
diferencia gobierna todo el resto: metodología propia, gobernanza, transferencia y documentación cuentan
tanto como el código.

---

## 3. Alcance del objeto

**Cláusula SEGUNDA — Alcance.** El CONTRATISTA debe ejecutar las actividades y entregar los componentes
para incorporar IA en el ciclo de vida de la ingeniería de software de la AGENCIA, mediante la ejecución de
**ocho (8) componentes técnicos** detallados en el **Anexo Técnico**.

**Resultado comprometido (literal, cláusula SEGUNDA).** Al final de la ejecución la AGENCIA debe contar con:

1. Un **marco institucional propio** para el ciclo de vida de desarrollo de software mediado por IA.
2. Un **caso de uso funcional desplegado y operando** en un proceso misional.
3. Un **sistema de agentes y skills** implementado, con su **modelo de gobernanza**.
4. La **documentación técnica y operativa** que le permita operar, mantener, replicar y escalar esas
   capacidades de manera **autónoma**.

El cuarto punto es el criterio de aceptación más exigente: la entrega se mide por **autonomía operativa
transferida**, no por artefactos entregados.

---

## 4. Objetivos

### 4.1 Objetivo conceptual

Institucionalizar en la AGENCIA un **modelo propio de ciclo de vida de desarrollo de software mediado por
IA** (SDLC-IA) que sea:

- **Propio y no dependiente del proveedor:** el marco queda en la AGENCIA, con su gobernanza.
- **Replicable y escalable:** aplicable a nuevos casos de uso sin reeditar el proyecto.
- **Demostrado en producción:** validado en un proceso misional real, no en un piloto de laboratorio.

### 4.2 Objetivos técnicos

La minuta **no trae una sección formal de "objetivos específicos"**. Los objetivos técnicos se derivan de
las **obligaciones específicas del CONTRATISTA** (cláusula TERCERA, literal b), que son su formulación
contractual más próxima:

| # | Objetivo técnico | Obligación |
|---|---|---|
| OT-1 | Realizar el **diagnóstico técnico y operativo** del modelo de desarrollo de software actual de la AGENCIA | b.2, b.3 |
| OT-2 | Entregar el **informe de diagnóstico** para validación de la supervisión | b.3 |
| OT-3 | **Definir la metodología SDLC-IA** aplicable a las necesidades de la AGENCIA | b.4 |
| OT-4 | **Identificar y priorizar** un caso de uso institucional para aplicar la metodología | b.5 |
| OT-5 | **Desarrollar e implementar los agentes de IA con sus skills**, conforme a la metodología y al ciclo de vida definidos | b.6 |
| OT-6 | **Ejecutar el desarrollo del caso de uso** usando los agentes y la metodología definidos | b.7 |
| OT-7 | **Desplegar en el ambiente productivo** dispuesto por la entidad | b.8 |
| OT-8 | Elaborar y presentar la **documentación técnica + transferencia de conocimiento** | b.9 |
| OT-9 | Cumplir **cada componente del Anexo Técnico** y entregar los productos correspondientes | b.10 |

**Hito de arranque (obligación b.1).** Presentar el **plan de trabajo** dentro de los **ocho (8) días
hábiles** siguientes a la suscripción del acta de inicio o del perfeccionamiento contractual.
Es la primera fecha dura del contrato y condiciona el resto del cronograma.

---

## 5. Entregables y compromisos técnicos de UNAL

### 5.1 Los ocho componentes técnicos y su agrupación por pago

Los nombres de los componentes son **literales de la cláusula SÉPTIMA** (forma de pago). El detalle de
actividades y productos por componente vive en el Anexo Técnico.

**Primer pago — $150.000.000 COP**

| Código | Componente |
|---|---|
| C1 | Diagnóstico técnico, operativo y organizacional |
| C2 | Definición de la metodología SDLC-IA |
| C3 | Identificación y especificación del caso de uso institucional |
| C4 | Desarrollo e implementación de los agentes inteligentes |

**Segundo pago — $150.000.000 COP**

| Código | Componente |
|---|---|
| C5 | Puesta en marcha de los agentes y las skills |
| C6 | Ingeniería de pruebas y validación del caso de uso |
| C7 | Despliegue e implementación en un proceso misional |
| C8 | Documentación técnica, operativa y transferencia metodológica |

Los dos pagos son **iguales y secuenciales**: el segundo no se causa hasta el recibo a satisfacción de los
componentes C5–C8.

### 5.2 Compromisos técnicos exigibles

- **Plan de trabajo** dentro de 8 días hábiles del acta de inicio (b.1).
- **Diagnóstico** del modelo de desarrollo actual, con informe para validación de la supervisión (b.2, b.3).
- **Metodología SDLC-IA** definida y aplicable a la AGENCIA (b.4).
- **Caso de uso institucional** identificado, priorizado y especificado (b.5).
- **Agentes de IA y skills** desarrollados e implementados (b.6).
- **Caso de uso desarrollado** con la metodología y los agentes definidos (b.7).
- **Despliegue en ambiente productivo** dispuesto por la entidad (b.8).
- **Documentación técnica y operativa + transferencia de conocimiento** (b.9).
- **Cumplimiento completo de cada componente del Anexo Técnico** (b.10).
- **Asistencia a reuniones** presenciales y virtuales según necesidades de ejecución (b.11).

### 5.3 Compromisos de contraparte (AGENCIA) que condicionan la entrega

Son dependencias del contratista y conviene tenerlas visibles porque **la fecha de entrega depende de
ellas** (cláusula TERCERA, literal c):

1. Designar un **equipo técnico y funcional** con disponibilidad para sesiones de trabajo, validación de
   requerimientos y revisión de entregables.
2. Facilitar **acceso oportuno** a información, procesos, datos, documentación, usuarios clave, sistemas
   y ambientes.
3. Gestionar las **autorizaciones internas** de seguridad, privacidad, tratamiento de datos, conectividad,
   infraestructura y acceso a herramientas institucionales.
4. **Adquirir o habilitar** licencias, APIs, servicios de nube, modelos como servicio y otras herramientas
   externas cuando sean necesarias para la operación del caso de uso, según disponibilidad presupuestal.
5. **Revisar y aprobar oportunamente los entregables** conforme al cronograma y los mecanismos de
   seguimiento definidos.

> **Riesgo de cronograma.** Los puntos 2, 3 y 4 son prerrequisitos de C5–C7 y dependen de la AGENCIA. El
> informe de actividades y la certificación del supervisor condicionan cada pago (cláusula SÉPTIMA).

---

## 6. Actividades más importantes (secuencia de ejecución)

1. **Arranque contractual** — perfeccionamiento, aprobación de garantías, registro presupuestal, acta de
   inicio; entrega del plan de trabajo (≤8 días hábiles).
2. **Diagnóstico** (C1) — levantamiento técnico, operativo y organizacional del modelo de desarrollo
   actual; informe para validación.
3. **Metodología** (C2) — definición del SDLC-IA institucional.
4. **Caso de uso** (C3) — identificación, priorización y especificación.
5. **Agentes y skills** (C4) — desarrollo e implementación.
   → **Cierre del primer pago** ($150.000.000) tras recibo a satisfacción de C1–C4.
6. **Puesta en marcha** (C5) — activación de agentes y skills sobre el caso de uso.
7. **Pruebas y validación** (C6) — ingeniería de pruebas del caso de uso.
8. **Despliegue misional** (C7) — puesta en producción en un proceso misional.
9. **Documentación y transferencia** (C8) — documentación técnica y operativa, transferencia metodológica.
   → **Cierre del segundo pago** ($150.000.000) tras recibo a satisfacción de C5–C8.
10. **Liquidación** — acta de liquidación bilateral (cláusula DÉCIMA SEXTA).

---

## 7. Condiciones técnicas y legales que condicionan la ejecución

### 7.1 Forma de pago (cláusula SÉPTIMA)

Cada pago exige, de forma acumulativa:

- Presentación del **informe de actividades** por parte del contratista, cuando se requiera.
- **Certificación y/o aprobación del supervisor**.
- Comprobante de pago de **aportes al Sistema General de Seguridad Social y Riesgos Laborales**.
- **Factura** o documento equivalente, cuando aplique.

Plazo máximo de pago: **30 días calendario** desde el recibo del bien o servicio, con recibo a
satisfacción del supervisor y demás requisitos cumplidos (Ley 2024 de 2020; Decreto 1733 de 2020;
Decreto Distrital 189 de 2020).

### 7.2 Garantías (cláusula NOVENA)

Deben constituirse **dentro de los 3 días hábiles siguientes a la firma del contrato**:

| Amparo | Cuantía | Vigencia |
|---|---|---|
| Cumplimiento | 15 % del valor total | Plazo de ejecución + 6 meses |
| Calidad del servicio | 20 % del valor del contrato | Plazo de ejecución + 6 meses |
| Salarios, prestaciones sociales e indemnizaciones laborales | 5 % del valor del contrato | Plazo de ejecución + 3 años |

El monto debe restablecerse cuando se agote por multas impuestas. El amparo no puede cancelarse sin
autorización de ATENEA.

### 7.3 Confidencialidad (cláusula DÉCIMA)

Obligación de reserva estricta, **vigente incluso después de terminado el contrato**. Incluye deberes
operativos concretos:

- Usar la información **solo** para el objeto contractual.
- Acceder únicamente a la información **estrictamente necesaria** (principio de necesidad de conocer) y
  respetar los controles de acceso de ATENEA.
- **No almacenar** información confidencial en bases de datos, dispositivos o sitios que no cumplan las
  condiciones de seguridad de ATENEA; usar únicamente repositorios y sistemas que garanticen integridad,
  calidad y confidencialidad.
- **Reportar de inmediato** cualquier incidente de seguridad, acceso no autorizado, pérdida o sustracción.
- **Devolver** toda la información al término del contrato (físicos, digitales y copias).

Marco normativo exigido: Ley 1581 de 2012, Ley 1712 de 2014, Decreto 1074 de 2015, más la Política de
Tratamiento de Datos Personales, la Política de Seguridad y Privacidad de la Información y el Manual de
Políticas de Seguridad de ATENEA.

**Sanción por incumplimiento:** pena del **15 % del valor total contratado**, descontable de saldos a favor
y cobrable por vía ejecutiva.

> **Impacto técnico directo.** La combinación de "necesidad de conocer" + "no almacenar fuera de las
> condiciones de seguridad de ATENEA" define qué herramientas, repositorios y servicios de modelos pueden
> usarse con datos reales. **Debe resolverse antes de C4/C5**, porque condiciona el diseño de los agentes
> y de la memoria/contexto que consumen.

### 7.4 Seguridad de la información (cláusula DÉCIMA PRIMERA)

Prohibición de revelar información **pública clasificada** o **pública reservada** en los términos de los
artículos 18 y 19 de la Ley 1712 de 2014, sin consentimiento previo y escrito de ATENEA.

### 7.5 Propiedad intelectual (cláusula VIGÉSIMA CUARTA)

Los **derechos patrimoniales** sobre obras, metodologías, documentación, desarrollos de software, **código
fuente, algoritmos, modelos, agentes, skills, configuraciones y arneses de prueba** creados en ejecución
pertenecen **en forma exclusiva a la AGENCIA** (art. 20 Ley 23 de 1982, modificado por art. 28 Ley 1450 de
2011; art. 10 de la Decisión Andina 351 de 1993). La transferencia es sin limitación de tiempo, modo,
territorio o número de ejemplares, y **se entiende incluida en el valor del contrato**, sin regalía
adicional. El uso futuro de esa información por el contratista requiere autorización previa de ATENEA.

> **Impacto técnico.** El código y los agentes no son reutilizables libremente por el contratista ni por
> terceros. Requiere disciplina de licencias de dependencias y de procedencia del código generado, porque
> el resultado se transfiere íntegramente a una entidad pública.

### 7.6 Documentos vinculantes (cláusula VIGÉSIMA SEGUNDA)

Forman parte integral del contrato y son vinculantes: los estudios previos, la solicitud de ordenación
contractual, **la propuesta presentada por el contratista** y el **Anexo Técnico**.

### 7.7 Terminación (cláusula VIGÉSIMA TERCERA)

Tres causales: mutuo acuerdo (previa certificación del supervisor), agotamiento del objeto o vencimiento
del plazo, y fuerza mayor o caso fortuito. Solo en terminación anticipada se levanta acta con las razones.

### 7.8 Suspensión (cláusula DÉCIMA QUINTA)

El plazo puede suspenderse por acta motivada suscrita por las partes; el término suspendido **no se
computa** para los plazos del contrato.

---

## 8. Reparto de responsabilidad técnica

| Ámbito | UNAL (CONTRATISTA) | ATENEA (AGENCIA) |
|---|---|---|
| Diagnóstico del modelo actual | Ejecuta y entrega informe | Da acceso a procesos, sistemas, datos y usuarios clave |
| Metodología SDLC-IA | Define y documenta | Valida y acompaña con equipo funcional |
| Caso de uso | Identifica, prioriza, especifica, desarrolla | Prioriza institucionalmente y valida requerimientos |
| Agentes y skills | Desarrolla, implementa, pone en marcha | Autoriza accesos, herramientas y entornos |
| Ambiente productivo | Despliega | **Dispone** el ambiente y la infraestructura |
| Herramientas externas | Selecciona e integra | **Adquiere o habilita** licencias, APIs, nube y modelos como servicio |
| Pruebas | Ingeniería de pruebas y validación | Acepta y recibe a satisfacción |
| Documentación y transferencia | Elabora y transfiere | Recibe y aprueba; asume la operación autónoma |
| Propiedad intelectual | Transfiere la totalidad | Titular exclusiva de los derechos patrimoniales |

---

## 9. Vacíos e información no incluida en el PDF

Estos puntos **no pueden responderse con esta fuente** y no se infieren:

1. **Anexo Técnico ausente.** La minuta lo nombra como documento vinculante (cláusulas SEGUNDA, SÉPTIMA y
   VIGÉSIMA SEGUNDA) pero **no está incluido** en las 15 páginas del PDF. Ahí viven el detalle de
   actividades, los productos por componente, los criterios de aceptación y el **cronograma oficial**.
2. **Cronograma contractual.** La minuta fija el plazo (5 meses) y las condiciones de pago, pero **no
   contiene un cronograma de entregables** por fecha o por quincena.
3. **Objetivos específicos formales.** No existe una sección con ese nombre. Los objetivos técnicos de
   [§4.2](#42-objetivos-técnicos) son una derivación de las obligaciones específicas, no texto literal.
4. **Estudios previos y propuesta del contratista.** Son vinculantes pero no forman parte de este PDF.
5. **Equipo de trabajo, perfiles y dedicación** comprometidos por UNAL.
6. **Criterios de aceptación y recibo a satisfacción** de cada componente.
7. **Ambiente productivo, infraestructura y herramientas** concretas que dispondrá ATENEA (dependen de las
   autorizaciones y adquisiciones de §5.3).

> Para publicar el cronograma quincenal del deck (slide M3) se usó un **plan de referencia derivado** del
> plazo de 5 meses y de la secuencia de componentes/causales de pago. **No sustituye el cronograma del
> Anexo Técnico** y debe conciliarse con él antes de usarse como compromiso.

---

## 10. Preguntas abiertas para la contraparte

1. ¿Cuál es el cronograma oficial de entregables y el detalle por componente del Anexo Técnico?
2. ¿Qué entornos, repositorios y servicios de modelos quedan autorizados para el tratamiento de datos
   reales, bajo las condiciones de seguridad de ATENEA?
3. ¿Qué licencias, APIs y servicios de nube están presupuestados y con qué anticipación se habilitarán?
4. ¿Cuál es el equipo técnico y funcional designado por ATENEA y su disponibilidad para validaciones?
5. ¿Qué criterios de aceptación y qué mecanismo de seguimiento se aplicarán por componente?
6. ¿La propuesta del contratista y los estudios previos confirman o ajustan el alcance aquí resumido?

---

**Nota de trazabilidad.** Este resumen se construyó exclusivamente sobre el PDF de la minuta. Las
afirmaciones se anclan a la cláusula indicada; las que son derivación (objetivos técnicos, cronograma de
referencia) están rotuladas como tales. Antes de usar este documento como compromiso contractual debe
conciliarse con el Anexo Técnico, los estudios previos y la propuesta del contratista.
