#!/usr/bin/env python3
"""
Generador de e1-e4.html con todas las tablas y diagramas de flujo del informe técnico (Capítulos 1 a 7).
"""

import sys
from pathlib import Path

def generate_e1_e4_html():
    html = '''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, viewport-fit=cover"
    />
    <title>Informe Técnico E1–E4: Contrato ATENEA-464-2026 | LIA UNAL</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Source+Serif+4:wght@500;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="assets/css/styles.css?v=20261023_1" />
  </head>
  <body class="view-deck">
    <div class="ambient"></div>
    <div class="deck-app">
      <div class="rail-bar-wrapper">
        <a href="index.html" class="deck-selector-btn" style="text-decoration:none;" title="Volver al Panel Selector de Presentaciones">
          <span class="deck-selector-badge">DECK</span>
          <span class="deck-selector-name">E1–E4: Informe de Avance</span>
          <span class="deck-selector-switch" style="font-size:0.75rem; color:var(--accent); font-weight:700; margin-left:6px;">← Selector</span>
        </a>
        <nav class="rail" aria-label="Módulos">
          <div class="rail-module" data-deck="e1-e4" data-module="cover">
            <button class="rail-title" type="button" data-first="0">Portada</button>
            <div class="rail-dots" id="dots-cover"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e0">
            <button class="rail-title" type="button" data-first="1">1 · Marco Contractual</button>
            <div class="rail-dots" id="dots-e0"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e1">
            <button class="rail-title" type="button" data-first="6">2 · Diagnóstico E1</button>
            <div class="rail-dots" id="dots-e1"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e2">
            <button class="rail-title" type="button" data-first="12">3 · Metodología E2</button>
            <div class="rail-dots" id="dots-e2"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e3">
            <button class="rail-title" type="button" data-first="17">4 · Arquitectura E3</button>
            <div class="rail-dots" id="dots-e3"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e4">
            <button class="rail-title" type="button" data-first="20">5 · Agentes y Skills E4</button>
            <div class="rail-dots" id="dots-e4"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e5">
            <button class="rail-title" type="button" data-first="23">6 · Decisiones y Cierre</button>
            <div class="rail-dots" id="dots-e5"></div>
          </div>
        </nav>
      </div>

      <main class="deck-viewport">
        <section class="stage">
          <!-- Slide 0: Portada E1-E4 -->
          <article
            class="slide is-cover is-active"
            data-deck="e1-e4"
            data-module="cover"
            id="slide-e-cover"
          >
            <div class="cover-card">
              <div class="cover-header">
                <div class="cover-logos">
                  <img
                    class="cover-logo"
                    src="assets/images/escudo_unal.png"
                    alt="Universidad Nacional de Colombia"
                  />
                  <img
                    class="cover-logo"
                    src="assets/images/logo_labIA.png"
                    alt="Laboratorio de Inteligencia Artificial"
                  />
                  <img
                    class="cover-logo"
                    src="assets/images/logo-atenea.png"
                    alt="Agencia Distrital ATENEA"
                  />
                </div>
                <span class="cover-badge">INFORME TÉCNICO DE AVANCE &middot; HITO 1</span>
              </div>
              <h1 class="cover-title">
                Fortalecimiento del ciclo de vida de ingeniería de software con inteligencia artificial en ATENEA
              </h1>
              <p class="cover-subtitle">
                Entregables E1 a E4: Diagnóstico institucional, Metodología SDLC-IA, Arquitectura End-to-End y Sistema de Agentes y Skills al 21 de octubre de 2026.
              </p>
              <div class="cover-team">
                <p class="cover-team-label">Equipo de Trabajo &middot; LIA UNAL Manizales:</p>
                <ul class="cover-members">
                  <li class="cover-member">
                    <span class="cover-member-name">Prof. Jorge Iván Montes Monsalve</span>
                    <span class="cover-member-role">Profesor Asociado &middot; Fac. de Administración (Sede Manizales)</span>
                  </li>
                  <li class="cover-member">
                    <span class="cover-member-name">Prof. Andrés Marino Álvarez Meza</span>
                    <span class="cover-member-role">Profesor Asociado - Fac. Ingeniería y Arquitectura, Dir. LIA-UNAL</span>
                  </li>
                  <li class="cover-member">
                    <span class="cover-member-name">Carlos Andrés Pérez Aguirre</span>
                    <span class="cover-member-role">Estudiante de Doctorado en Ingeniería</span>
                  </li>
                  <li class="cover-member">
                    <span class="cover-member-name">Diego Armando Pérez Rosero</span>
                    <span class="cover-member-role">Estudiante de Doctorado en Ingeniería</span>
                  </li>
                  <li class="cover-member">
                    <span class="cover-member-name">Juan Sebastián Méndez Rondón</span>
                    <span class="cover-member-role">Candidato a Ph.D. en Ingeniería</span>
                  </li>
                </ul>
              </div>
              <p class="cover-meta">
                <span>Contrato Interadministrativo ATENEA-464-2026 &middot; Hito 1</span>
                <span>Bogotá D.C. &middot; Manizales, 21 de octubre de 2026</span>
              </p>
            </div>
          </article>

          <!-- ========================================================================= -->
          <!-- MÓDULO 1: Marco Contractual y Cronograma (Capítulos 1 y 2)                -->
          <!-- ========================================================================= -->

          <!-- Slide 1: Objeto contractual y cuatro resultados -->
          <article class="slide" data-deck="e1-e4" data-module="e0">
            <div class="slide-content">
              <p class="slide-kicker">1 &middot; Marco Contractual y Alcance</p>
              <h2>Contrato ATENEA-464-2026: objeto y cuatro resultados exigidos</h2>
              <ul class="slide-list">
                <li>
                  <strong>Objeto (cláusula primera):</strong> prestar servicios para fortalecer las capacidades de la Agencia para mejorar el ciclo de vida de la ingeniería de software, mediante el uso de <abbr title="Inteligencia Artificial">IA</abbr>.
                </li>
                <li>
                  <strong>Partes:</strong> la Agencia Distrital <abbr title="Agencia Distrital para la Educación Superior, la Ciencia y la Tecnología">ATENEA</abbr> y la <abbr title="Universidad Nacional de Colombia">UNAL</abbr> Sede Manizales.
                </li>
                <li>
                  <strong>Alcance (cláusula segunda):</strong> ocho componentes técnicos que, al terminar, dejan a la Agencia cuatro resultados.
                </li>
                <li>
                  <strong>Valor y plazo:</strong> $300.000.000 en dos pagos de $150.000.000 y hasta cinco meses desde el acta de inicio (22 semanas).
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 340" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Estructura del contrato ATENEA-464-2026 y sus cuatro resultados esperados">
              <rect x="8" y="8" width="504" height="86" rx="10" fill="#EDF1F7" stroke="#2C6B87" stroke-width="1.5" />
              <text x="24" y="34" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">CONTRATO ATENEA-464-2026</text>
              <text x="24" y="58" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">ATENEA ↔ UNAL Sede Manizales</text>
              <text x="24" y="80" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">$300.000.000 · 8 componentes · 22 semanas</text>
              <text x="260" y="124" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle" letter-spacing="1">CUATRO RESULTADOS AL TERMINAR</text>
              <rect x="8" y="138" width="248" height="92" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.5" />
              <rect x="18" y="148" width="30" height="22" rx="4" fill="#7FB4CA" />
              <text x="33" y="164" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">R1</text>
              <text x="56" y="165" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Marco institucional</text>
              <text x="20" y="188" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">propio para el ciclo de vida</text>
              <text x="20" y="204" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">de desarrollo de software</text>
              <text x="20" y="220" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">mediado por IA</text>
              <rect x="264" y="138" width="248" height="92" rx="8" fill="#F8FAFC" stroke="#7AA89F" stroke-width="1.5" />
              <rect x="274" y="148" width="30" height="22" rx="4" fill="#7AA89F" />
              <text x="289" y="164" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">R2</text>
              <text x="312" y="165" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Caso de uso funcional</text>
              <text x="276" y="188" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">desplegado y operando</text>
              <text x="276" y="204" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">en un proceso misional</text>
              <rect x="8" y="238" width="248" height="92" rx="8" fill="#F8FAFC" stroke="#B7CC85" stroke-width="1.5" />
              <rect x="18" y="248" width="30" height="22" rx="4" fill="#B7CC85" />
              <text x="33" y="264" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">R3</text>
              <text x="56" y="265" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Agentes y skills</text>
              <text x="20" y="288" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">sistema implementado con</text>
              <text x="20" y="304" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">su modelo de gobernanza</text>
              <rect x="264" y="238" width="248" height="92" rx="8" fill="#F8FAFC" stroke="#DFBD76" stroke-width="1.5" />
              <rect x="274" y="248" width="30" height="22" rx="4" fill="#DFBD76" />
              <text x="289" y="264" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">R4</text>
              <text x="312" y="265" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Documentación técnica</text>
              <text x="276" y="288" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">y operativa para operar,</text>
              <text x="276" y="304" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">mantener, replicar y</text>
              <text x="276" y="320" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">escalar de forma autónoma</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Cuatro resultados al terminar</p>
                <ol class="slide-list" style="margin:8px 0;">
                  <li><strong>R1 Marco institucional:</strong> propio para el ciclo de vida de desarrollo de software mediado por IA.</li>
                  <li><strong>R2 Caso de uso funcional:</strong> desplegado y operando en un proceso misional.</li>
                  <li><strong>R3 Agentes y skills:</strong> sistema implementado con su modelo de gobernanza.</li>
                  <li><strong>R4 Documentación técnica:</strong> operativa, para operar, mantener, replicar y escalar de forma autónoma.</li>
                </ol>
              </div>
            </figure>
          </article>

          <!-- Slide 2: Estado de E1 a E4 (Tabla 1.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e0">
            <div class="slide-content">
              <p class="slide-kicker">1 &middot; Marco Contractual y Alcance</p>
              <h2>Estado de E1 a E4 al corte: qué está listo y qué falta</h2>
              <ul class="slide-list">
                <li>
                  <strong>Corte al 21 de octubre de 2026:</strong> el informe se apoya en la minuta, el acta 01 del 7 de octubre y tres sesiones grabadas con ATENEA.
                </li>
                <li>
                  <strong>Hito 1:</strong> E1 a E4 integran el hito 1 del cronograma contractual.
                </li>
                <li>
                  <strong>E1:</strong> diagnóstico completo, a la espera de la validación de ATENEA.
                </li>
                <li>
                  <strong>E2 a E4:</strong> propuesta definida; falta la validación de ATENEA, el caso de uso y los accesos, y la instalación del arnés.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 352" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Estado de los entregables E1 a E4 al 21 de octubre de 2026: estado al corte y qué falta">
              <rect x="6" y="6" width="508" height="93" rx="9" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
              <rect x="6" y="6" width="112" height="93" rx="9" fill="#1E5631" />
              <rect x="100" y="6" width="18" height="93" fill="#1E5631" />
              <text x="62" y="50.5" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700" text-anchor="middle">E1</text>
              <text x="62" y="70.5" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Diagnóstico</text>
              <text x="130" y="28" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Diagnóstico completo para validación</text>
              <text x="130" y="46" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Falta: Validación de ATENEA; documentos de</text>
              <text x="130" y="62" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">arquitectura de SICORE Posmedia y SICORE CTeI;</text>
              <text x="130" y="78" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">informe de seguridad</text>
              <rect x="6" y="107" width="508" height="74" rx="9" fill="#FFF7ED" stroke="#8A5A00" stroke-width="1.5" />
              <rect x="6" y="107" width="112" height="74" rx="9" fill="#8A5A00" />
              <rect x="100" y="107" width="18" height="74" fill="#8A5A00" />
              <text x="62" y="142.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700" text-anchor="middle">E2</text>
              <text x="62" y="162.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">SDLC-IA</text>
              <text x="130" y="129" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Flujo propuesto por etapa</text>
              <text x="130" y="147" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Falta: Validación de ATENEA; alcance de CI/CD</text>
              <rect x="6" y="189" width="508" height="94" rx="9" fill="#FFF7ED" stroke="#8A5A00" stroke-width="1.5" />
              <rect x="6" y="189" width="112" height="94" rx="9" fill="#8A5A00" />
              <rect x="100" y="189" width="18" height="94" fill="#8A5A00" />
              <text x="62" y="234.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700" text-anchor="middle">E3</text>
              <text x="62" y="254.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Arquitectura</text>
              <text x="130" y="211" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Composición definida por tipo de</text>
              <text x="130" y="228" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">componente</text>
              <text x="130" y="246" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Falta: Caso de uso y accesos a las</text>
              <text x="130" y="262" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">herramientas de ATENEA</text>
              <rect x="6" y="291" width="508" height="94" rx="9" fill="#FFF7ED" stroke="#8A5A00" stroke-width="1.5" />
              <rect x="6" y="291" width="112" height="94" rx="9" fill="#8A5A00" />
              <rect x="100" y="291" width="18" height="94" fill="#8A5A00" />
              <text x="62" y="336.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700" text-anchor="middle">E4</text>
              <text x="62" y="356.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Agentes y skills</text>
              <text x="130" y="313" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Arnés propuesto y probado fuera de</text>
              <text x="130" y="330" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">ATENEA</text>
              <text x="130" y="348" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Falta: Adaptación a las condiciones de ATENEA</text>
              <text x="130" y="364" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">e instalación</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Estado de E1 a E4 al corte</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>E1 Diagnóstico:</strong> <span class="pill pill--ok">Diagnóstico completo para validación</span><br />Falta: Validación de ATENEA; documentos de arquitectura de SICORE Posmedia y SICORE CTeI; informe de seguridad.</li>
                  <li><strong>E2 SDLC-IA:</strong> <span class="pill pill--partial">Flujo propuesto por etapa</span><br />Falta: Validación de ATENEA; alcance de CI/CD.</li>
                  <li><strong>E3 Arquitectura:</strong> <span class="pill pill--partial">Composición definida por tipo de componente</span><br />Falta: Caso de uso y accesos a las herramientas de ATENEA.</li>
                  <li><strong>E4 Agentes y skills:</strong> <span class="pill pill--partial">Arnés propuesto y probado fuera de ATENEA</span><br />Falta: Adaptación a las condiciones de ATENEA e instalación.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Tabla 1.1 — Estado de E1 a E4 al 21 de octubre de 2026 y lo que falta para cerrar cada entregable</figcaption>
            </figure>
          </article>

          <!-- Slide 3: Condiciones generales y cláusulas (Tabla 2.1 y sección 2.6) -->
          <article class="slide" data-deck="e1-e4" data-module="e0">
            <div class="slide-content">
              <p class="slide-kicker">1 &middot; Marco Contractual y Alcance</p>
              <h2>Condiciones generales y cláusulas que condicionan el diseño técnico</h2>
              <ul class="slide-list">
                <li>
                  <strong>Cuatro cláusulas condicionan el diseño técnico</strong> de la arquitectura de E3 y del sistema de agentes de E4 (§2.6).
                </li>
                <li>
                  <strong>Confidencialidad (décima):</strong> la información de ATENEA solo se almacena en sistemas que cumplan su seguridad; el incumplimiento acarrea una pena del 15 % del valor total.
                </li>
                <li>
                  <strong>Seguridad de la información (undécima):</strong> prohíbe revelar información pública clasificada o reservada sin consentimiento escrito.
                </li>
                <li>
                  <strong>Propiedad intelectual (vigésima cuarta):</strong> metodologías, código, modelos, agentes, skills y arneses pertenecen a ATENEA.
                </li>
                <li>
                  <strong>Recursos institucionales (vigésima novena):</strong> los equipos y sistemas de ATENEA pueden ser monitoreados y auditados.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.2vw,2.14vh),1.5rem);">
                  <caption>Tabla 2.1 — Condiciones generales del contrato según la minuta</caption>
                  <thead>
                    <tr>
                      <th style="width:28%;font-size:0.82em;">Elemento</th>
                      <th style="font-size:0.82em;">Condición en la minuta</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Elemento"><strong>Plazo (cláusula cuarta)</strong></td>
                      <td data-label="Condición en la minuta">Hasta cinco meses a partir de la suscripción del acta de inicio, previo cumplimiento de los requisitos de perfeccionamiento y ejecución.</td>
                    </tr>
                    <tr>
                      <td data-label="Elemento"><strong>Lugar (quinta)</strong></td>
                      <td data-label="Condición en la minuta">Bogotá D.C.</td>
                    </tr>
                    <tr>
                      <td data-label="Elemento"><strong>Valor (sexta)</strong></td>
                      <td data-label="Condición en la minuta"><strong>$300.000.000</strong>, con impuestos y costos directos e indirectos incluidos; la propuesta del contratista forma parte integral del contrato.</td>
                    </tr>
                    <tr>
                      <td data-label="Elemento"><strong>Supervisión (octava)</strong></td>
                      <td data-label="Condición en la minuta">Subgerente de Tecnologías de Información y Comunicaciones, o quien designe por escrito el ordenador del gasto.</td>
                    </tr>
                    <tr>
                      <td data-label="Elemento"><strong>Garantías (novena)</strong></td>
                      <td data-label="Condición en la minuta">Dentro de los tres días hábiles siguientes a la firma: cumplimiento (15 %, plazo más seis meses), calidad del servicio (20 %, plazo más seis meses) y salarios y prestaciones (5 %, plazo más tres años).</td>
                    </tr>
                    <tr>
                      <td data-label="Elemento"><strong>Liquidación (decimosexta)</strong></td>
                      <td data-label="Condición en la minuta">De mutuo acuerdo dentro de los cuatro meses siguientes al vencimiento del plazo.</td>
                    </tr>
                    <tr>
                      <td data-label="Elemento"><strong>Ejecución (trigésima)</strong></td>
                      <td data-label="Condición en la minuta">Requiere registro presupuestal, aprobación de garantías y acta de inicio; el perfeccionamiento se completa en SECOP II.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 4: Obligaciones específicas (Tabla 2.2) -->
          <article class="slide" data-deck="e1-e4" data-module="e0">
            <div class="slide-content">
              <p class="slide-kicker">1 &middot; Marco Contractual y Alcance</p>
              <h2>Obligaciones específicas del contratista</h2>
              <ul class="slide-list">
                <li>
                  <strong>11 obligaciones específicas</strong> definen el trabajo técnico; las 24 generales son de orden administrativo y ético.
                </li>
                <li>
                  <strong>Cada obligación se apoya en componentes:</strong> de C1 a C8, con el arranque y las reuniones como casos transversales.
                </li>
                <li>
                  <strong>Cinco obligaciones de la Agencia (literal c):</strong> equipo técnico y funcional, acceso a información y sistemas, autorizaciones de seguridad y datos, licencias, API y modelos, y revisión de entregables.
                </li>
                <li>
                  <strong>Las decisiones pendientes de E3 y E4</strong> corresponden a las obligaciones 7 y 8 de la Agencia.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.15vw,2.05vh),1.5rem);">
                  <caption>Tabla 2.2 — Obligaciones específicas del contratista (literal b de la cláusula tercera)</caption>
                  <thead>
                    <tr>
                      <th style="width:7%;font-size:0.82em;">N.º</th>
                      <th style="font-size:0.82em;">Obligación</th>
                      <th style="width:17%;font-size:0.82em;">Componente</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="N.º"><strong>1</strong></td>
                      <td data-label="Obligación">Presentar el plan de trabajo dentro de los ocho días hábiles siguientes a la suscripción del acta de inicio o del perfeccionamiento</td>
                      <td data-label="Componente"><span class="table-tag tag-blue">Arranque</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>2</strong></td>
                      <td data-label="Obligación">Realizar el diagnóstico técnico y operativo del modelo de desarrollo de software actual de la entidad</td>
                      <td data-label="Componente"><span class="table-tag tag-green">C1</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>3</strong></td>
                      <td data-label="Obligación">Entregar para validación de la supervisión el informe del diagnóstico</td>
                      <td data-label="Componente"><span class="table-tag tag-green">C1</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>4</strong></td>
                      <td data-label="Obligación">Definir una metodología SDLC-IA aplicable a las necesidades de la entidad</td>
                      <td data-label="Componente"><span class="table-tag tag-green">C2</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>5</strong></td>
                      <td data-label="Obligación">Identificar y priorizar un caso de uso institucional para aplicar la metodología</td>
                      <td data-label="Componente"><span class="table-tag tag-green">C3</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>6</strong></td>
                      <td data-label="Obligación">Desarrollar e implementar los agentes de IA con sus skills, acorde a la metodología y al ciclo de vida definido</td>
                      <td data-label="Componente"><span class="table-tag tag-blue">C4, C5</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>7</strong></td>
                      <td data-label="Obligación">Ejecutar el desarrollo del caso de uso con los agentes y la metodología</td>
                      <td data-label="Componente"><span class="table-tag tag-blue">C5, C6</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>8</strong></td>
                      <td data-label="Obligación">Desplegar el caso de uso en el ambiente productivo dispuesto por la entidad</td>
                      <td data-label="Componente"><span class="table-tag tag-blue">C7</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>9</strong></td>
                      <td data-label="Obligación">Elaborar la documentación técnica con su transferencia de conocimiento</td>
                      <td data-label="Componente"><span class="table-tag tag-blue">C8</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>10</strong></td>
                      <td data-label="Obligación">Cumplir cada componente del anexo técnico y entregar sus productos</td>
                      <td data-label="Componente"><span class="table-tag tag-amber">C1 a C8</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>11</strong></td>
                      <td data-label="Obligación">Asistir a las reuniones presenciales y virtuales que requiera la ejecución</td>
                      <td data-label="Componente"><span class="table-tag tag-amber">Transversal</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 5: Entregables, componentes y pagos (Tablas 2.3 y 2.4) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e0">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">1 &middot; Marco Contractual y Alcance</p>
                <h2 style="margin-bottom:4px;">Entregables E1 a E8, componentes C1 a C8 y pagos</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">La correspondencia no es uno a uno: el cumplimiento se verifica por componente y cada pago agrupa cuatro.</p>
              </div>
              <svg viewBox="0 0 1200 540" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mapa entre entregables E1 a E8 y componentes C1 a C8, agrupados por pago contractual">
              <rect x="12" y="32.0" width="486" height="242.0" rx="10" fill="#F4FAF5" stroke="#1E5631" stroke-width="1.3" />
              <text x="26" y="52.0" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">HITO 1 · SEMANA 13</text>
              <rect x="12" y="274.0" width="486" height="242.0" rx="10" fill="#F2F7FA" stroke="#2C6B87" stroke-width="1.3" />
              <text x="26" y="294.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">HITO 2 · SEMANA 22</text>
              <rect x="702" y="32.0" width="486" height="242.0" rx="10" fill="#F4FAF5" stroke="#1E5631" stroke-width="1.3" />
              <text x="716" y="52.0" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">PAGO 1 · $150.000.000</text>
              <rect x="702" y="274.0" width="486" height="242.0" rx="10" fill="#F2F7FA" stroke="#2C6B87" stroke-width="1.3" />
              <text x="716" y="294.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">PAGO 2 · $150.000.000</text>
              <path d="M490 86.0 C600.0 86.0 600.0 86.0 710 86.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 86.0 C600.0 86.0 600.0 190.0 710 190.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 138.0 C600.0 138.0 600.0 138.0 710 138.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 190.0 C600.0 190.0 600.0 190.0 710 190.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 242.0 C600.0 242.0 600.0 242.0 710 242.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 242.0 C600.0 242.0 600.0 328.0 710 328.0" stroke="#8A5A00" stroke-width="3" stroke-dasharray="6,4" fill="none" />
              <path d="M490 328.0 C600.0 328.0 600.0 380.0 710 380.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 328.0 C600.0 328.0 600.0 432.0 710 432.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 380.0 C600.0 380.0 600.0 484.0 710 484.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 432.0 C600.0 432.0 600.0 484.0 710 484.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <path d="M490 484.0 C600.0 484.0 600.0 484.0 710 484.0" stroke="#6E8CA0" stroke-width="2" fill="none" />
              <rect x="20" y="66.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
              <rect x="20" y="66.0" width="48" height="40" rx="7" fill="#2C6B87" />
              <rect x="50" y="66.0" width="18" height="40" fill="#2C6B87" />
              <text x="44" y="92.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">E1</text>
              <text x="78" y="92.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600">Informe de diagnóstico institucional</text>
              <text x="480" y="92.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Mes 1 a 2</text>
              <rect x="20" y="118.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
              <rect x="20" y="118.0" width="48" height="40" rx="7" fill="#2C6B87" />
              <rect x="50" y="118.0" width="18" height="40" fill="#2C6B87" />
              <text x="44" y="144.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">E2</text>
              <text x="78" y="144.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600">Metodología SDLC-IA para ATENEA</text>
              <text x="480" y="144.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Mes 2</text>
              <rect x="20" y="170.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
              <rect x="20" y="170.0" width="48" height="40" rx="7" fill="#2C6B87" />
              <rect x="50" y="170.0" width="18" height="40" fill="#2C6B87" />
              <text x="44" y="196.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">E3</text>
              <text x="78" y="196.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600">Arquitectura End-to-End</text>
              <text x="480" y="196.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Mes 2</text>
              <rect x="20" y="222.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
              <rect x="20" y="222.0" width="48" height="40" rx="7" fill="#2C6B87" />
              <rect x="50" y="222.0" width="18" height="40" fill="#2C6B87" />
              <text x="44" y="248.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">E4</text>
              <text x="78" y="248.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600">Sistema de agentes y skills</text>
              <text x="480" y="248.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Mes 3 a 4</text>
              <rect x="20" y="308.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
              <rect x="20" y="308.0" width="48" height="40" rx="7" fill="#2C6B87" />
              <rect x="50" y="308.0" width="18" height="40" fill="#2C6B87" />
              <text x="44" y="334.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">E5</text>
              <text x="78" y="334.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600">Despliegue y validación misional</text>
              <text x="480" y="334.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Mes 4 a 5</text>
              <rect x="20" y="360.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
              <rect x="20" y="360.0" width="48" height="40" rx="7" fill="#2C6B87" />
              <rect x="50" y="360.0" width="18" height="40" fill="#2C6B87" />
              <text x="44" y="386.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">E6</text>
              <text x="78" y="386.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600">Documentación técnica y operativa</text>
              <text x="480" y="386.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Mes 5</text>
              <rect x="20" y="412.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
              <rect x="20" y="412.0" width="48" height="40" rx="7" fill="#2C6B87" />
              <rect x="50" y="412.0" width="18" height="40" fill="#2C6B87" />
              <text x="44" y="438.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">E7</text>
              <text x="78" y="438.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600">Workshop de transferencia</text>
              <text x="480" y="438.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Mes 2 a 5</text>
              <rect x="20" y="464.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
              <rect x="20" y="464.0" width="48" height="40" rx="7" fill="#2C6B87" />
              <rect x="50" y="464.0" width="18" height="40" fill="#2C6B87" />
              <text x="44" y="490.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">E8</text>
              <text x="78" y="490.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600">Informe final y cierre</text>
              <text x="480" y="490.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Mes 5</text>
              <rect x="710" y="66.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.3" />
              <rect x="710" y="66.0" width="48" height="40" rx="7" fill="#4F8B7E" />
              <rect x="740" y="66.0" width="18" height="40" fill="#4F8B7E" />
              <text x="734" y="92.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">C1</text>
              <text x="768" y="84.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">Diagnóstico técnico, operativo y</text>
              <text x="768" y="100.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">organizacional</text>
              <rect x="710" y="118.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.3" />
              <rect x="710" y="118.0" width="48" height="40" rx="7" fill="#4F8B7E" />
              <rect x="740" y="118.0" width="18" height="40" fill="#4F8B7E" />
              <text x="734" y="144.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">C2</text>
              <text x="768" y="144.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">Definición de la metodología SDLC-IA</text>
              <rect x="710" y="170.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.3" />
              <rect x="710" y="170.0" width="48" height="40" rx="7" fill="#4F8B7E" />
              <rect x="740" y="170.0" width="18" height="40" fill="#4F8B7E" />
              <text x="734" y="196.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">C3</text>
              <text x="768" y="188.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">Identificación y especificación del caso de</text>
              <text x="768" y="204.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">uso institucional</text>
              <rect x="710" y="222.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.3" />
              <rect x="710" y="222.0" width="48" height="40" rx="7" fill="#4F8B7E" />
              <rect x="740" y="222.0" width="18" height="40" fill="#4F8B7E" />
              <text x="734" y="248.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">C4</text>
              <text x="768" y="240.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">Desarrollo e implementación de los agentes</text>
              <text x="768" y="256.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">inteligentes</text>
              <rect x="710" y="308.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.3" />
              <rect x="710" y="308.0" width="48" height="40" rx="7" fill="#4F8B7E" />
              <rect x="740" y="308.0" width="18" height="40" fill="#4F8B7E" />
              <text x="734" y="334.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">C5</text>
              <text x="768" y="334.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">Puesta en marcha de los agentes y las skills</text>
              <rect x="710" y="360.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.3" />
              <rect x="710" y="360.0" width="48" height="40" rx="7" fill="#4F8B7E" />
              <rect x="740" y="360.0" width="18" height="40" fill="#4F8B7E" />
              <text x="734" y="386.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">C6</text>
              <text x="768" y="378.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">Ingeniería de pruebas y validación del caso</text>
              <text x="768" y="394.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">de uso</text>
              <rect x="710" y="412.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.3" />
              <rect x="710" y="412.0" width="48" height="40" rx="7" fill="#4F8B7E" />
              <rect x="740" y="412.0" width="18" height="40" fill="#4F8B7E" />
              <text x="734" y="438.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">C7</text>
              <text x="768" y="430.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">Despliegue e implementación en un proceso</text>
              <text x="768" y="446.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">misional</text>
              <rect x="710" y="464.0" width="470" height="40" rx="7" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.3" />
              <rect x="710" y="464.0" width="48" height="40" rx="7" fill="#4F8B7E" />
              <rect x="740" y="464.0" width="18" height="40" fill="#4F8B7E" />
              <text x="734" y="490.0" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">C8</text>
              <text x="768" y="482.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">Documentación técnica, operativa y</text>
              <text x="768" y="498.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="600">transferencia metodológica</text>
              <path d="M20 521 H70" stroke="#6E8CA0" stroke-width="2" />
              <text x="80" y="526" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">Aporta al componente</text>
              <path d="M270 521 H320" stroke="#8A5A00" stroke-width="3" stroke-dasharray="6,4" />
              <text x="330" y="526" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">E4 cubre C4 (primer pago) y C5 (segundo pago)</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Componentes, entregables y pagos</p>
                <p class="sched-sub">Pago 1 · $150.000.000 · hito 1 (semana 13)</p>
                <ul class="slide-list" style="margin:6px 0;">
                  <li><strong>C1</strong> Diagnóstico técnico, operativo y organizacional ← E1</li>
                  <li><strong>C2</strong> Definición de la metodología SDLC-IA ← E2</li>
                  <li><strong>C3</strong> Caso de uso institucional ← E1 y E3</li>
                  <li><strong>C4</strong> Agentes inteligentes ← E4</li>
                </ul>
                <p class="sched-sub">Pago 2 · $150.000.000 · hito 2 (semana 22)</p>
                <ul class="slide-list" style="margin:6px 0;">
                  <li><strong>C5</strong> Puesta en marcha de agentes y skills ← E4</li>
                  <li><strong>C6</strong> Ingeniería de pruebas y validación ← E5</li>
                  <li><strong>C7</strong> Despliegue en un proceso misional ← E5</li>
                  <li><strong>C8</strong> Documentación y transferencia ← E6, E7 y E8</li>
                </ul>
                <p class="sched-note">E4 cubre C4 (primer pago) y C5 (segundo pago): para el primer pago cuenta el documento de definición del sistema de agentes.</p>
              </div>
              <figcaption class="fig-caption">Tabla 2.4 — Entregables E1 a E8 y su relación con los componentes C1 a C8; pagos según la Tabla 2.3</figcaption>
            </figure>
          </article>

          <!-- Slide 6: Cronograma operativo (Figura 2.1) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e0">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">1 &middot; Marco Contractual y Alcance</p>
                <h2 style="margin-bottom:4px;">Cronograma operativo semanal y distribución de hitos</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El hito 1 vence en la semana 13; la meta interna de la semana 4 del plan de seguimiento no condiciona pagos.</p>
              </div>
              <svg viewBox="0 0 1200 560" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cronograma operativo semanal S1 a S22 con los hitos contractuales H1c en la semana 13 y H2 en la semana 22">
              <rect x="431.0" y="6" width="134.36363636363637" height="26" rx="4" fill="#EDF1F7" stroke="#BAC7D5" />
              <text x="498.1818181818182" y="25" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Mes 1</text>
              <rect x="567.3636363636364" y="6" width="168.45454545454547" height="26" rx="4" fill="#EDF1F7" stroke="#BAC7D5" />
              <text x="651.5909090909091" y="25" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Mes 2</text>
              <rect x="737.8181818181819" y="6" width="134.36363636363637" height="26" rx="4" fill="#EDF1F7" stroke="#BAC7D5" />
              <text x="805.0" y="25" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Mes 3</text>
              <rect x="874.1818181818182" y="6" width="168.45454545454547" height="26" rx="4" fill="#EDF1F7" stroke="#BAC7D5" />
              <text x="958.409090909091" y="25" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Mes 4</text>
              <rect x="1044.6363636363637" y="6" width="134.36363636363637" height="26" rx="4" fill="#EDF1F7" stroke="#BAC7D5" />
              <text x="1111.818181818182" y="25" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Mes 5</text>
              <text x="447.04545454545456" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">1</text>
              <text x="481.1363636363637" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">2</text>
              <text x="515.2272727272727" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">3</text>
              <text x="549.3181818181818" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">4</text>
              <text x="583.4090909090909" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">5</text>
              <text x="617.5" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">6</text>
              <text x="651.590909090909" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">7</text>
              <text x="685.6818181818181" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">8</text>
              <text x="719.7727272727273" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">9</text>
              <text x="753.8636363636364" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">10</text>
              <text x="787.9545454545455" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">11</text>
              <text x="822.0454545454545" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">12</text>
              <text x="856.1363636363636" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">13</text>
              <text x="890.2272727272727" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">14</text>
              <text x="924.3181818181818" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">15</text>
              <text x="958.4090909090909" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">16</text>
              <text x="992.5" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">17</text>
              <text x="1026.5909090909092" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">18</text>
              <text x="1060.6818181818182" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">19</text>
              <text x="1094.7727272727273" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">20</text>
              <text x="1128.8636363636365" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">21</text>
              <text x="1162.9545454545455" y="50" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12" text-anchor="middle">22</text>
              <line x1="430.0" y1="58" x2="430.0" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="464.0909090909091" y1="58" x2="464.0909090909091" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="498.1818181818182" y1="58" x2="498.1818181818182" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="532.2727272727273" y1="58" x2="532.2727272727273" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="566.3636363636364" y1="58" x2="566.3636363636364" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="600.4545454545455" y1="58" x2="600.4545454545455" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="634.5454545454545" y1="58" x2="634.5454545454545" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="668.6363636363636" y1="58" x2="668.6363636363636" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="702.7272727272727" y1="58" x2="702.7272727272727" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="736.8181818181819" y1="58" x2="736.8181818181819" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="770.909090909091" y1="58" x2="770.909090909091" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="805.0" y1="58" x2="805.0" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="839.0909090909091" y1="58" x2="839.0909090909091" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="873.1818181818182" y1="58" x2="873.1818181818182" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="907.2727272727273" y1="58" x2="907.2727272727273" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="941.3636363636364" y1="58" x2="941.3636363636364" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="975.4545454545455" y1="58" x2="975.4545454545455" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="1009.5454545454546" y1="58" x2="1009.5454545454546" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="1043.6363636363637" y1="58" x2="1043.6363636363637" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="1077.7272727272727" y1="58" x2="1077.7272727272727" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="1111.818181818182" y1="58" x2="1111.818181818182" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="1145.909090909091" y1="58" x2="1145.909090909091" y2="512" stroke="#000" stroke-opacity="0.09" />
              <line x1="1180.0" y1="58" x2="1180.0" y2="512" stroke="#000" stroke-opacity="0.09" />
              <rect x="430.0" y="65" width="443.18181818181824" height="19" rx="3" fill="#2C6B87" />
              <text x="24" y="80" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Hito 1 (C1 a C4, E1 a E4)</text>
              <text x="24" y="105" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A1 Kickoff, garantías y plan</text>
              <rect x="431.0" y="91" width="66.18181818181819" height="17" rx="3" fill="#9DB7C9" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="130" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A2 Diagnóstico [E1]</text>
              <rect x="431.0" y="116" width="66.18181818181819" height="17" rx="3" fill="#7FB4CA" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="155" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A3 Metodología SDLC-IA [E2]</text>
              <rect x="465.0909090909091" y="141" width="32.09090909090909" height="17" rx="3" fill="#7FB4CA" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="180" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A4 Caso de uso y arquitectura [E3]</text>
              <rect x="465.0909090909091" y="166" width="66.18181818181819" height="17" rx="3" fill="#7FB4CA" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="205" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A5 Entornos, herramientas y accesos</text>
              <rect x="499.1818181818182" y="191" width="32.09090909090909" height="17" rx="3" fill="#9DB7C9" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="230" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A6 Primer conjunto de agentes y skills [E4]</text>
              <rect x="499.1818181818182" y="216" width="66.18181818181819" height="17" rx="3" fill="#B7CC85" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="255" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A7 Arneses iniciales [E4]</text>
              <rect x="533.2727272727273" y="241" width="32.09090909090909" height="17" rx="3" fill="#B7CC85" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="280" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A8 Ingeniería de pruebas [E5]</text>
              <rect x="567.3636363636364" y="266" width="66.18181818181819" height="17" rx="3" fill="#7AA89F" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="305" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A9 Integración en flujos [E4]</text>
              <rect x="567.3636363636364" y="291" width="100.27272727272728" height="17" rx="3" fill="#B7CC85" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="330" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A10 Puesta en marcha [E4]</text>
              <rect x="635.5454545454545" y="316" width="100.27272727272728" height="17" rx="3" fill="#B7CC85" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="355" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A11 Workshop #1 [E7]</text>
              <rect x="669.6363636363636" y="341" width="32.09090909090909" height="17" rx="3" fill="#DFBD76" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="380" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A12 Despliegue piloto [E5]</text>
              <rect x="737.8181818181819" y="366" width="100.27272727272728" height="17" rx="3" fill="#7AA89F" stroke="#2C6B87" stroke-opacity="0.5" />
              <text x="24" y="405" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A13 Validación y ajustes [E5]</text>
              <rect x="771.909090909091" y="391" width="100.27272727272728" height="17" rx="3" fill="#7AA89F" stroke="#2C6B87" stroke-opacity="0.5" />
              <polygon points="856.1363636363636,415 866.1363636363636,424.5 856.1363636363636,434 846.1363636363636,424.5" fill="#8A5A00" />
              <text x="24" y="430" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">H1c · hito 1 contractual (semana 13)</text>
              <rect x="873.1818181818182" y="440" width="306.81818181818187" height="19" rx="3" fill="#5B6472" />
              <text x="24" y="455" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Hito 2 (C5 a C8, E5 a E8)</text>
              <text x="24" y="480" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">A14 a A20 · Ampliación, documentación, talleres y cierre</text>
              <rect x="874.1818181818182" y="466" width="304.81818181818187" height="17" rx="3" fill="#BAC7D5" stroke="#5B6472" stroke-opacity="0.5" />
              <polygon points="1160.9545454545455,490 1170.9545454545455,499.5 1160.9545454545455,509 1150.9545454545455,499.5" fill="#8A5A00" />
              <text x="24" y="505" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">H2 · hito 2 contractual (semana 22)</text>
              <line x1="873.1818181818182" y1="58" x2="873.1818181818182" y2="512" stroke="#1E5631" stroke-width="2.5" stroke-dasharray="5,4" />
              <line x1="1180.0" y1="58" x2="1180.0" y2="512" stroke="#8A5A00" stroke-width="2.5" stroke-dasharray="5,4" />
              <text x="24" y="552" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">Semanas S1 a S22 contadas desde el acta de inicio. Las actividades A14 a A20 aparecen agrupadas.</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Cronograma S1 a S22</p>
                <p class="sched-sub">Mes 1: S1-S4 · Mes 2: S5-S9 · Mes 3: S10-S13 · Mes 4: S14-S18 · Mes 5: S19-S22</p>
                <p class="sched-h">Hito 1 · C1 a C4 y E1 a E4 · semana 13</p>
                <ul class="slide-list" style="margin:6px 0;">
                  <li><strong>A1</strong> Kickoff, garantías y plan · S1-S2</li>
                  <li><strong>A2</strong> Diagnóstico [E1] · S1-S2</li>
                  <li><strong>A3</strong> Metodología SDLC-IA [E2] · S2</li>
                  <li><strong>A4</strong> Caso de uso y arquitectura [E3] · S2-S3</li>
                  <li><strong>A5</strong> Entornos, herramientas y accesos · S3</li>
                  <li><strong>A6</strong> Primer conjunto de agentes y skills [E4] · S3-S4</li>
                  <li><strong>A7</strong> Arneses iniciales [E4] · S4</li>
                  <li><strong>A8</strong> Ingeniería de pruebas [E5] · S5-S6</li>
                  <li><strong>A9</strong> Integración en flujos [E4] · S5-S7</li>
                  <li><strong>A10</strong> Puesta en marcha [E4] · S7-S9</li>
                  <li><strong>A11</strong> Workshop #1 [E7] · S8</li>
                  <li><strong>A12</strong> Despliegue piloto [E5] · S10-S12</li>
                  <li><strong>A13</strong> Validación y ajustes [E5] · S11-S13</li>
                </ul>
                <p class="sched-h">Hito 2 · C5 a C8 y E5 a E8 · semana 22</p>
                <ul class="slide-list" style="margin:6px 0;">
                  <li><strong>A14 a A20</strong> Ampliación, documentación, talleres y cierre · S14-S22</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 2.1 — Cronograma operativo semanal S1 a S22 con los hitos contractuales H1c y H2 (las actividades A14 a A20 aparecen agrupadas)</figcaption>
            </figure>
          </article>

          <!-- ========================================================================= -->
          <!-- MÓDULO 2: E1 · Diagnóstico Técnico y de Capacidades (Capítulo 3)          -->
          <!-- ========================================================================= -->

          <!-- Slide 7: Portafolio (Tabla 3.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Portafolio de sistemas: aplicaciones misionales y alcance</h2>
              <ul class="slide-list">
                <li>
                  <strong>Modelo autogestionado:</strong> ATENEA construye, entrega y mantiene sus sistemas con su propio equipo de desarrollo.
                </li>
                <li>
                  <strong>Núcleo misional:</strong> <abbr title="Sistema de Información Core">SICORE</abbr> Posmedia (<abbr title="Gerencia de Educación Posmedia">GEPM</abbr>) y SICORE CTeI, también conocida como HEMA; datos, ambientes y operación son internos.
                </li>
                <li>
                  <strong>Trabajo en curso:</strong> evolutivos sobre esas aplicaciones y el servicio unificado de usuarios, roles y permisos con Keycloak.
                </li>
                <li>
                  <strong>Límites expresos:</strong> Academia Atenea es solo referencia y Hermes queda fuera del contrato por decisión de ATENEA.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.2vw,2.14vh),1.5rem);">
                  <caption>Tabla 3.1 — Portafolio de sistemas y proyectos de ATENEA y su relación con el contrato</caption>
                  <thead>
                    <tr>
                      <th style="width:22%;font-size:0.82em;">Sistema o proyecto</th>
                      <th style="width:30%;font-size:0.82em;">Tipo</th>
                      <th style="width:22%;font-size:0.82em;">Estado</th>
                      <th style="font-size:0.82em;">Relación con el contrato</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Sistema o proyecto"><strong>SICORE Posmedia</strong></td>
                      <td data-label="Tipo">Aplicación misional; evolutivos sobre el sistema existente</td>
                      <td data-label="Estado">En operación, con proyectos activos</td>
                      <td data-label="Relación con el contrato"><span class="pill pill--ok">En alcance</span> candidata a caso de uso</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema o proyecto"><strong>SICORE CTeI (HEMA)</strong></td>
                      <td data-label="Tipo">Aplicación misional; evolutivos sobre el sistema existente</td>
                      <td data-label="Estado">En operación; dos desarrolladores dedicados</td>
                      <td data-label="Relación con el contrato"><span class="pill pill--ok">En alcance</span></td>
                    </tr>
                    <tr>
                      <td data-label="Sistema o proyecto"><strong>Servicio unificado de usuarios, roles y permisos</strong></td>
                      <td data-label="Tipo">Desarrollo transversal nuevo; Keycloak como inicio de sesión único y conexión al directorio activo</td>
                      <td data-label="Estado">En incorporación</td>
                      <td data-label="Relación con el contrato"><span class="pill pill--ok">En alcance</span> candidato a caso de uso</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema o proyecto"><strong>Academia Atenea</strong></td>
                      <td data-label="Tipo">Plataforma de formación sobre Moodle 4.5</td>
                      <td data-label="Estado">En operación, fuera del núcleo SICORE</td>
                      <td data-label="Relación con el contrato"><span class="pill pill--partial">Referencia</span> no prioritaria</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema o proyecto"><strong>Hermes</strong></td>
                      <td data-label="Tipo">Asistente de orientación socio-ocupacional y atención al ciudadano; tercerizado y alojado por su proveedor</td>
                      <td data-label="Estado">Migración a Azure como proyecto paralelo, con arquitectura propia</td>
                      <td data-label="Relación con el contrato"><span class="pill pill--todo">Fuera del contrato</span> por decisión de ATENEA</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema o proyecto"><strong>Migración de Oracle Cloud a Azure</strong></td>
                      <td data-label="Tipo">Proyecto de infraestructura en dos fases</td>
                      <td data-label="Estado">Fase 1 en curso; fase 2 sin decisión</td>
                      <td data-label="Relación con el contrato"><span class="pill pill--partial">Condiciona</span> el entorno del agente y el pipeline</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 8: Equipo y roles (Tabla 3.2) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Equipo y roles: concentración de funciones y ausencia de arquitecto</h2>
              <ul class="slide-list">
                <li>
                  <strong>PO sobrecargado:</strong> cuatro líderes de producto levantan con negocio, redactan el acta y gestionan firmas sin apoyo para descomponer.
                </li>
                <li>
                  <strong>Cuello de botella de revisión:</strong> la líder del equipo revisa a mano cada cambio, sin reglas escritas contra las cuales revisar.
                </li>
                <li>
                  <strong>Sin arquitecto (0 personas):</strong> nadie define ni vigila estándares; cada desarrollador estructura el código a su criterio.
                </li>
                <li>
                  <strong>Despliegue dependiente de una persona:</strong> infraestructura recibe los compilados y despliega.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(0.98vw,1.75vh),1.5rem);">
                  <caption>Tabla 3.2 — Roles del ciclo de desarrollo, número de personas y falencia asociada</caption>
                  <thead>
                    <tr>
                      <th style="width:19%;font-size:0.82em;">Rol</th>
                      <th style="width:17%;font-size:0.82em;">Personas</th>
                      <th style="width:34%;font-size:0.82em;">Qué hace hoy</th>
                      <th style="font-size:0.82em;">Falencia</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Rol"><strong>Negocio o área cliente</strong></td>
                      <td data-label="Personas">Varias áreas (p. ej., Posmedia, Tesorería)</td>
                      <td data-label="Qué hace hoy">Plantea la necesidad, aprueba el Figma de palabra y firma el acta</td>
                      <td data-label="Falencia">La firma llega semanas después y puede traer cambios</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Líder de producto (PO de facto)</strong></td>
                      <td data-label="Personas">4; el acta 01 registró 2 o 3</td>
                      <td data-label="Qué hace hoy">Cada uno atiende un módulo: levanta con negocio, redacta el acta y gestiona firmas</td>
                      <td data-label="Falencia">Concentra levantamiento, especificación y aprobación sin apoyo para descomponer</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Diseño UI/UX</strong></td>
                      <td data-label="Personas">1</td>
                      <td data-label="Qué hace hoy">Participa en las mesas, en forma virtual, y produce el Figma comentado</td>
                      <td data-label="Falencia">Es la única validación previa a construir</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Líder del equipo de desarrollo</strong></td>
                      <td data-label="Personas">1</td>
                      <td data-label="Qué hace hoy">Revisa a mano cada cambio antes de integrarlo; define el enfoque técnico</td>
                      <td data-label="Falencia">Cuello de botella de revisión; sin reglas escritas contra las cuales revisar</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Base de datos</strong></td>
                      <td data-label="Personas">1</td>
                      <td data-label="Qué hace hoy">Define con la líder el enfoque técnico de cada proyecto</td>
                      <td data-label="Falencia">Decisiones técnicas sin registro</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Desarrolladores</strong></td>
                      <td data-label="Personas">1 de front-end y 1 de back-end por módulo; 2 dedicados a SICORE CTeI</td>
                      <td data-label="Qué hace hoy">Estiman, construyen y generan los compilados; desde 2027 se busca un perfil full stack</td>
                      <td data-label="Falencia">Cada quien estructura el código a su criterio</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Infraestructura</strong></td>
                      <td data-label="Personas">1</td>
                      <td data-label="Qué hace hoy">Recibe los compilados, despliega y lidera la migración a Azure</td>
                      <td data-label="Falencia">Despliegue dependiente de una persona</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Seguridad</strong></td>
                      <td data-label="Personas">2</td>
                      <td data-label="Qué hace hoy">Se vincularon a los sistemas de desarrollo este año</td>
                      <td data-label="Falencia">Primera revisión de seguridad de las aplicaciones, cerca de un mes antes del 7 de octubre</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Arquitecto de software</strong></td>
                      <td data-label="Personas"><span class="pill pill--risk">0 personas</span></td>
                      <td data-label="Qué hace hoy">No aplica</td>
                      <td data-label="Falencia">Nadie define ni vigila estándares</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 9: Flujo actual (Figura 3.1) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e1" data-tone="amber">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
                <h2 style="margin-bottom:4px;">Flujo actual de un requerimiento: actas extensas y cambios tardíos</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">La construcción arranca asumiendo la aceptación; la firma llega tarde y trae cambios que regresan a construcción.</p>
              </div>
              <svg viewBox="0 0 1200 650" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Flujo actual de un requerimiento en ATENEA por procesos y artefactos: cinco carriles y cuatro columnas, con el inicio asumiendo aceptación en verde y los cambios tardíos en rojo">
              <defs>
              <marker id="fa-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1 L10 5 L0 9 z" fill="#4E93B0" /></marker>
              <marker id="fa-g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1 L10 5 L0 9 z" fill="#1E5631" /></marker>
              <marker id="fa-r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1 L10 5 L0 9 z" fill="#B71C1C" /></marker>
              </defs>
              <rect x="261.0" y="8" width="218" height="30" rx="5" fill="#EDF1F7" />
              <text x="370" y="29" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Entender</text>
              <rect x="491.0" y="8" width="218" height="30" rx="5" fill="#EDF1F7" />
              <text x="600" y="29" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Validar y aprobar</text>
              <rect x="721.0" y="8" width="218" height="30" rx="5" fill="#EDF1F7" />
              <text x="830" y="29" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Construir</text>
              <rect x="951.0" y="8" width="218" height="30" rx="5" fill="#EDF1F7" />
              <text x="1060" y="29" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Desplegar</text>
              <rect x="20" y="74" width="1160" height="92" fill="#F3F7FB" stroke="#4E93B0" stroke-opacity="0.2" />
              <text x="34" y="117.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">01 ·</text>
              <text x="72" y="117.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Requerimiento</text>
              <text x="72" y="134.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">y especificación</text>
              <rect x="20" y="166" width="1160" height="92" fill="#FFFFFF" stroke="#4E93B0" stroke-opacity="0.2" />
              <text x="34" y="209.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">02 ·</text>
              <text x="72" y="209.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Documentación</text>
              <text x="72" y="226.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">y evidencia</text>
              <rect x="20" y="258" width="1160" height="92" fill="#F3F7FB" stroke="#4E93B0" stroke-opacity="0.2" />
              <text x="34" y="301.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">03 ·</text>
              <text x="72" y="301.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Diseño</text>
              <text x="72" y="318.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">y aprobación</text>
              <rect x="20" y="350" width="1160" height="92" fill="#FFFFFF" stroke="#4E93B0" stroke-opacity="0.2" />
              <text x="34" y="401.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">04 ·</text>
              <text x="72" y="401.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Construcción</text>
              <rect x="20" y="442" width="1160" height="92" fill="#F3F7FB" stroke="#4E93B0" stroke-opacity="0.2" />
              <text x="34" y="485.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">05 ·</text>
              <text x="72" y="485.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Entrega</text>
              <text x="72" y="502.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">y ambientes</text>
              <line x1="485.0" y1="68" x2="485.0" y2="534" stroke="#4E93B0" stroke-opacity="0.35" stroke-dasharray="5,4" />
              <line x1="715.0" y1="68" x2="715.0" y2="534" stroke="#4E93B0" stroke-opacity="0.35" stroke-dasharray="5,4" />
              <line x1="945.0" y1="68" x2="945.0" y2="534" stroke="#4E93B0" stroke-opacity="0.35" stroke-dasharray="5,4" />
              <rect x="284.0" y="86.0" width="172" height="68" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="370" y="108.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Levantamiento</text>
              <text x="370" y="124.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">conversación con</text>
              <text x="370" y="140.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">el cliente</text>
              <rect x="514.0" y="86.0" width="172" height="68" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="600" y="116.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Especificación</text>
              <text x="600" y="132.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">acta extensa ~ épica</text>
              <rect x="744.0" y="178.0" width="172" height="68" rx="7" fill="#E4EEF7" stroke="#4E93B0" stroke-width="1.6" />
              <text x="830" y="200.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">SharePoint</text>
              <text x="830" y="216.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">acta firmada +</text>
              <text x="830" y="232.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">enlace Figma</text>
              <rect x="514.0" y="270.0" width="172" height="68" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="600" y="292.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Validación de</text>
              <text x="600" y="308.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">diseño</text>
              <text x="600" y="324.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">prototipo en Figma</text>
              <rect x="744.0" y="270.0" width="172" height="68" rx="7" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.6" />
              <text x="830" y="300.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Aprobación formal</text>
              <text x="830" y="316.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">firma por correo</text>
              <rect x="744.0" y="362.0" width="172" height="68" rx="7" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
              <text x="830" y="384.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Construcción</text>
              <text x="830" y="400.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">código back-end</text>
              <text x="830" y="416.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">y front-end</text>
              <rect x="744.0" y="454.0" width="172" height="68" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="830" y="476.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Entrega a</text>
              <text x="830" y="492.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">infraestructura</text>
              <text x="830" y="508.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">compilados, sin CI/CD</text>
              <rect x="990.0" y="454.0" width="176" height="68" rx="7" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="1078" y="476.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">QA → Preprod → Prod</text>
              <text x="1078" y="492.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">esquemas Oracle</text>
              <text x="1078" y="508.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">por ambiente</text>
              <path d="M456.0 120.0 L514.0 120.0" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fa-b)" />
              <path d="M600 154.0 L600 270.0" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fa-b)" />
              <path d="M686.0 120.0 H830 V178.0" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fa-b)" />
              <text x="694.0" y="112.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">acta + Figma</text>
              <path d="M686.0 304.0 L744.0 304.0" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fa-b)" />
              <text x="715.0" y="296.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">correo</text>
              <path d="M830 270.0 L830 246.0" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fa-b)" />
              <text x="838" y="263.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">archiva</text>
              <path d="M600 338.0 V396.0 H744.0" stroke="#1E5631" stroke-width="2.6" fill="none" marker-end="url(#fa-g)" />
              <text x="610" y="366.0" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">inicio asumiendo</text>
              <text x="610" y="382.0" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">aceptación</text>
              <path d="M916.0 304.0 H952.0 V396.0 H916.0" stroke="#B71C1C" stroke-width="2.6" stroke-dasharray="7,5" fill="none" marker-end="url(#fa-r)" />
              <text x="962.0" y="355.0" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">cambios tardíos</text>
              <path d="M830 430.0 L830 454.0" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fa-b)" />
              <text x="838" y="447.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">compila</text>
              <path d="M916.0 488.0 L990 488.0" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fa-b)" />
              <text x="953.0" y="480.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">copia</text>
              <text x="953.0" y="509.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">manual</text>
              <path d="M24 559 H74" stroke="#1E5631" stroke-width="2.6" />
              <text x="84" y="564" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Inicio de la construcción que da por hecha la aceptación</text>
              <path d="M520 559 H570" stroke="#B71C1C" stroke-width="2.6" stroke-dasharray="7,5" />
              <text x="580" y="564" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Cambios tardíos que regresan a construcción</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Flujo actual por carriles</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>01 Requerimiento y especificación:</strong> Levantamiento (conversación con el cliente) → Especificación (acta extensa ~ épica).</li>
                  <li><strong>02 Documentación y evidencia:</strong> SharePoint guarda el acta firmada y el enlace a Figma.</li>
                  <li><strong>03 Diseño y aprobación:</strong> Validación de diseño (prototipo en Figma) → Aprobación formal (firma por correo), que se archiva en SharePoint.</li>
                  <li><strong>04 Construcción:</strong> código de back-end y front-end.</li>
                  <li><strong>05 Entrega y ambientes:</strong> Entrega a infraestructura (compilados, sin CI/CD) → copia manual a QA, preproducción y producción (esquemas Oracle por ambiente).</li>
                </ul>
                <p style="color:#1E5631;font-weight:700;">Verde: la construcción inicia asumiendo la aceptación.</p>
                <p style="color:#B71C1C;font-weight:700;">Rojo discontinuo: los cambios tardíos regresan a construcción.</p>
              </div>
              <figcaption class="fig-caption">Figura 3.1 — Flujo actual de un requerimiento en ATENEA, por procesos y artefactos</figcaption>
            </figure>
          </article>

          <!-- Slide 10: Infraestructura (Figura 3.2) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e1" data-tone="amber">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
                <h2 style="margin-bottom:4px;">Infraestructura y desarrollo: clúster en Oracle Cloud y migración a Azure</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Los ambientes viven en OCI; el código está en Oracle Visual Builder, en migración a Azure DevOps.</p>
              </div>
              <svg viewBox="0 0 1220 590" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Elementos de infraestructura y desarrollo de ATENEA: herramientas de trabajo, clúster de ambientes en Oracle Cloud y Azure como destino de la migración">
              <defs>
              <marker id="fi-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1 L10 5 L0 9 z" fill="#4E93B0" /></marker>
              <marker id="fi-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1 L10 5 L0 9 z" fill="#DFBD76" /></marker>
              </defs>
              <rect x="335" y="328" width="870" height="252" rx="10" fill="#E4EEF7" fill-opacity="0.6" stroke="#4E93B0" stroke-width="1.6" stroke-dasharray="8,5" />
              <text x="349" y="354" fill="#1B3A4F" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Clúster ATENEA en OCI: QA · Preproducción · Producción</text>
              <rect x="305.0" y="92.0" width="330" height="76" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.6" />
              <text x="470" y="126.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Asistente de IA (chat)</text>
              <text x="470" y="143.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Claude, licencias compartidas</text>
              <rect x="50.0" y="224.0" width="200" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="150" y="258.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">SharePoint</text>
              <text x="150" y="275.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">actas firmadas + Figma</text>
              <rect x="345.0" y="224.0" width="250" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="470" y="249.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Desarrolladores</text>
              <text x="470" y="266.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">front-end y back-end</text>
              <text x="470" y="283.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Azure DevOps</text>
              <rect x="685.0" y="224.0" width="210" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="790" y="249.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Infraestructura</text>
              <text x="790" y="266.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">despliegue manual</text>
              <text x="790" y="283.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">en Docker</text>
              <rect x="995.0" y="224.0" width="200" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="1095" y="258.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Microsoft Azure</text>
              <text x="1095" y="275.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">migración OCI, fase 1</text>
              <rect x="50.0" y="382.0" width="200" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="150" y="416.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Clientes / áreas</text>
              <text x="150" y="433.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">usuarios finales</text>
              <rect x="360.0" y="382.0" width="220" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="470" y="416.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Front-end Angular 13</text>
              <text x="470" y="433.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Node, contenedor Docker</text>
              <rect x="680.0" y="382.0" width="220" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="790" y="416.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Back-end Java 17</text>
              <text x="790" y="433.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Spring Boot 3 + WildFly 34</text>
              <rect x="995.0" y="382.0" width="200" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="1095" y="416.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Oracle Autonomous</text>
              <text x="1095" y="433.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">un esquema por ambiente</text>
              <rect x="675.0" y="490.0" width="230" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="790" y="515.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Keycloak</text>
              <text x="790" y="532.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">SSO + PostgreSQL</text>
              <text x="790" y="549.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">en incorporación</text>
              <path d="M470 224.0 V168.0" stroke="#DFBD76" stroke-width="2.2" fill="none" stroke-dasharray="6,4" marker-end="url(#fi-a)" marker-start="url(#fi-a)" />
              <text x="480" y="201.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">consultas</text>
              <path d="M250 262 H345" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fi-b)" />
              <text x="297.5" y="254" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">acta + Figma</text>
              <path d="M595 262 H685" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fi-b)" />
              <text x="640.0" y="254" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">compilados</text>
              <path d="M895 262 H995" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fi-b)" />
              <text x="945.0" y="254" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">migración</text>
              <path d="M790 300.0 V328" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fi-b)" />
              <text x="800" y="319.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">copia al clúster</text>
              <path d="M250 420 H360" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fi-b)" />
              <text x="305.0" y="412" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">HTTPS</text>
              <path d="M580 420 H680" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fi-b)" />
              <text x="630.0" y="412" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">API</text>
              <path d="M900 420 H995" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fi-b)" />
              <text x="947.5" y="412" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">SQL</text>
              <path d="M790 458.0 V490.0" stroke="#4E93B0" stroke-width="2.2" fill="none" marker-end="url(#fi-b)" marker-start="url(#fi-b)" />
              <text x="800" y="479.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">autenticación</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Infraestructura y desarrollo</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>Herramientas de trabajo:</strong> SharePoint (actas firmadas y Figma) → Desarrolladores (front-end y back-end, Azure DevOps) → Infraestructura (despliegue manual en Docker).</li>
                  <li><strong>Asistente de IA (chat):</strong> Claude con licencias compartidas; los desarrolladores le hacen consultas.</li>
                  <li><strong>Clúster ATENEA en OCI (QA, preproducción y producción):</strong> Front-end Angular 13 en Docker → Back-end Java 17 con Spring Boot 3 y WildFly 34 → Oracle Autonomous con un esquema por ambiente; el back-end se autentica con Keycloak (SSO + PostgreSQL, en incorporación).</li>
                  <li><strong>Clientes y áreas</strong> acceden al front-end por HTTPS.</li>
                  <li><strong>Microsoft Azure:</strong> destino de la migración, fase 1, desde Oracle Cloud.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 3.2 — Elementos de infraestructura y desarrollo de ATENEA: el recuadro agrupa los tres ambientes del clúster en Oracle Cloud; Azure es el destino de la migración en curso</figcaption>
            </figure>
          </article>

          <!-- Slide 11: Stack tecnológico 1/2 (Tabla 3.3) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Stack de aplicación: tecnología y situación (1/2)</h2>
              <ul class="slide-list">
                <li>
                  <strong>Front-end con deuda:</strong> Angular 13 está fuera de soporte; ATENEA reconoce que debe subir a la versión 22 o 23.
                </li>
                <li>
                  <strong>Back-end vigente:</strong> Java 17, Spring Boot 3 y WildFly 34 en Docker; la actualización a Java 21 está pendiente.
                </li>
                <li>
                  <strong>Código y documentación dispersos:</strong> Oracle Visual Builder en migración a Azure DevOps; actas en SharePoint y prototipos en Figma.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.2vw,2.14vh),1.5rem);">
                  <caption>Tabla 3.3 — Elementos de infraestructura y desarrollo, con su tecnología y su situación (parte 1 de 2)</caption>
                  <thead>
                    <tr>
                      <th style="width:20%;font-size:0.82em;">Capa o función</th>
                      <th style="width:34%;font-size:0.82em;">Tecnología</th>
                      <th style="font-size:0.82em;">Observaciones</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Capa o función"><strong>Front-end</strong></td>
                      <td data-label="Tecnología">Angular 13 sobre Node, en contenedor Docker</td>
                      <td data-label="Observaciones">Fuera de soporte; ATENEA reconoce que debe subir a la versión 22 o 23</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Back-end</strong></td>
                      <td data-label="Tecnología">Java 17 con Spring Boot 3, empaquetado como .war</td>
                      <td data-label="Observaciones">Actualización a Java 21 pendiente</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Servidor de aplicaciones</strong></td>
                      <td data-label="Tecnología">WildFly 34, en Docker sobre Linux Ubuntu</td>
                      <td data-label="Observaciones">Reemplazó a WebLogic a comienzos de 2026</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Base de datos</strong></td>
                      <td data-label="Tecnología">Oracle Autonomous; cuatro esquemas, tres oficiales (desarrollo o QA, preproducción, producción)</td>
                      <td data-label="Observaciones">Un servidor para producción y otro para los preproductivos; producto del Marketplace de Azure</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Identidad</strong></td>
                      <td data-label="Tecnología">Keycloak con PostgreSQL</td>
                      <td data-label="Observaciones">En incorporación como inicio de sesión único, con conexión al directorio activo</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Código fuente</strong></td>
                      <td data-label="Tecnología">Oracle Visual Builder, en migración a Azure DevOps</td>
                      <td data-label="Observaciones">Azure DevOps habilitado; ramas sin documentar. El acta 01 registró GitHub y las sesiones posteriores lo corrigieron</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Requerimientos y documentación</strong></td>
                      <td data-label="Tecnología">Actas en SharePoint, prototipos en Figma, firmas por correo</td>
                      <td data-label="Observaciones">Sin gestor de trabajo ni estados; sin documentos técnicos por aplicación</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 12: Ambientes, nube, seguridad y despliegue 2/2 (Tabla 3.3) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Ambientes, nube, seguridad y despliegue (2/2)</h2>
              <ul class="slide-list">
                <li>
                  <strong>Ambientes en OCI:</strong> QA, preproducción y producción; la preproducción sirve para pruebas con universidades por VPN.
                </li>
                <li>
                  <strong>Migración en dos fases:</strong> la fase 1 mueve cómputo, bases de datos y código sin refactorizar; la fase 2 no tiene decisión.
                </li>
                <li>
                  <strong>Seguridad de aplicaciones incipiente:</strong> primera revisión en 2026, con librerías desactualizadas y el token de sesión en local storage.
                </li>
                <li>
                  <strong>Sin CI/CD ni pruebas automatizadas:</strong> los compilados se entregan a mano y la validación es manual.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.2vw,2.14vh),1.5rem);">
                  <caption>Tabla 3.3 — Elementos de infraestructura y desarrollo, con su tecnología y su situación (parte 2 de 2)</caption>
                  <thead>
                    <tr>
                      <th style="width:20%;font-size:0.82em;">Capa o función</th>
                      <th style="width:34%;font-size:0.82em;">Tecnología</th>
                      <th style="font-size:0.82em;">Observaciones</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Capa o función"><strong>Ambientes</strong></td>
                      <td data-label="Tecnología">QA, preproducción y producción en Oracle Cloud (OCI)</td>
                      <td data-label="Observaciones">Preproducción es copia cercana a producción; pruebas con universidades por VPN</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Nube y migración</strong></td>
                      <td data-label="Tecnología">Azure contratado por CSP, con créditos gestionados internamente</td>
                      <td data-label="Observaciones">Fase 1 (menos de 15 días): cómputo y bases de datos sin refactorizar y código a Azure DevOps. Fase 2, sin decisión: Kubernetes, Web Apps, Container Registry y versionado de imágenes. Objetivo: una sola nube pública</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Seguridad de infraestructura</strong></td>
                      <td data-label="Tecnología">Topología hub and spoke; WAF en modo escucha que pasará a protección; Defender for Cloud; solo HTTP y HTTPS con certificado</td>
                      <td data-label="Observaciones">Copias georreplicadas e inmutables por ambiente, VPN, accesos por usuario, grupo, red, ambiente y puerto, y doble factor en Microsoft 365</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Seguridad de aplicaciones</strong></td>
                      <td data-label="Tecnología">Primera revisión en 2026</td>
                      <td data-label="Observaciones">Librerías desactualizadas y token de sesión en local storage; sin análisis de código ni de dependencias confirmado</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Pruebas</strong></td>
                      <td data-label="Tecnología">Sin cobertura automatizada documentada</td>
                      <td data-label="Observaciones">Validación manual en preproducción</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Integración y despliegue</strong></td>
                      <td data-label="Tecnología">No hay CI/CD</td>
                      <td data-label="Observaciones">Compilados entregados a mano; sin histórico de versiones de imágenes</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 13: Licencias y servicios de IA (Tabla 3.4) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Licencias y servicios de IA disponibles en ATENEA</h2>
              <ul class="slide-list">
                <li>
                  <strong>IA como chat:</strong> el equipo usa licencias compartidas de Claude como asistente general, en modo chat y sin método.
                </li>
                <li>
                  <strong>Sin política:</strong> no hay restricciones de seguridad específicas para herramientas de IA ni para compartir código.
                </li>
                <li>
                  <strong>Plazos exigentes:</strong> según la líder del equipo, las licencias han dado agilidad y por eso se exigen plazos de una a dos semanas.
                </li>
                <li>
                  <strong>Por definir:</strong> condiciones de datos de cada servicio, cuentas por persona y quién mide y paga el consumo.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.2vw,2.14vh),1.5rem);">
                  <caption>Tabla 3.4 — Licencias y servicios de IA disponibles en ATENEA</caption>
                  <thead>
                    <tr>
                      <th style="width:28%;font-size:0.82em;">Recurso</th>
                      <th style="width:38%;font-size:0.82em;">Cantidad</th>
                      <th style="font-size:0.82em;">Uso actual</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Recurso"><strong>Claude, plan Teams</strong></td>
                      <td data-label="Cantidad">Unos 6 asientos; unos 9 meses de suscripción restantes</td>
                      <td data-label="Uso actual">Chat compartido</td>
                    </tr>
                    <tr>
                      <td data-label="Recurso"><strong>OpenRouter</strong></td>
                      <td data-label="Cantidad">Unos USD 400 en créditos</td>
                      <td data-label="Uso actual">Adquirido tras reuniones previas con la Universidad</td>
                    </tr>
                    <tr>
                      <td data-label="Recurso"><strong>ChatGPT con Codex</strong></td>
                      <td data-label="Cantidad">Acceso disponible</td>
                      <td data-label="Uso actual">Sin uso reportado</td>
                    </tr>
                    <tr>
                      <td data-label="Recurso"><strong>Microsoft 365 Copilot</strong></td>
                      <td data-label="Cantidad">Cuentas limitadas</td>
                      <td data-label="Uso actual">Toma de notas</td>
                    </tr>
                    <tr>
                      <td data-label="Recurso"><strong>Figma</strong></td>
                      <td data-label="Cantidad">Algunos asientos</td>
                      <td data-label="Uso actual">Prototipos del levantamiento</td>
                    </tr>
                    <tr>
                      <td data-label="Recurso"><strong>Microsoft 365, Power Automate, Power Apps</strong></td>
                      <td data-label="Cantidad">Licenciamiento activo</td>
                      <td data-label="Uso actual">Sin uso reportado</td>
                    </tr>
                    <tr>
                      <td data-label="Recurso"><strong>Azure (créditos CSP)</strong></td>
                      <td data-label="Cantidad">Servicios activables bajo demanda: Foundry, Databricks, Data Factory, almacenamiento</td>
                      <td data-label="Uso actual">Dos lagos de datos pequeños para analítica</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 14: Capacidades y brechas (Tabla 3.5) [c1-brechas] -->
          <article class="slide" data-deck="e1-e4" data-module="e1" data-item="c1-brechas">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Mapa de capacidades y brechas por área de trabajo</h2>
              <ul class="slide-list">
                <li>
                  <strong>Siete áreas de trabajo</strong> contrastan lo que ATENEA tiene hoy con lo que le falta para operar con agentes de IA.
                </li>
                <li>
                  <strong>Sin hallazgos nuevos:</strong> los datos provienen de las secciones anteriores del diagnóstico.
                </li>
                <li>
                  <strong>Cuatro conclusiones</strong> desarrollan las brechas: desglose de requerimientos, estandarización de la arquitectura, agentes de IA para ampliar la capacidad del equipo y centralización de la documentación.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.12vw,2.0vh),1.5rem);">
                  <caption>Tabla 3.5 — Capacidades actuales y brechas de ATENEA en cada área de trabajo</caption>
                  <thead>
                    <tr>
                      <th style="width:19%;font-size:0.82em;">Área</th>
                      <th style="width:38%;font-size:0.82em;">Capacidad actual</th>
                      <th style="font-size:0.82em;">Brecha</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Área"><strong>Requerimientos y especificación</strong></td>
                      <td data-label="Capacidad actual">Cuatro líderes de producto levantan con negocio, redactan el acta y gestionan firmas; diseño produce el Figma</td>
                      <td data-label="Brecha">Acta de 12 páginas como épica, sin historias, tareas ni criterios de aceptación separados</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Arquitectura y estándares</strong></td>
                      <td data-label="Capacidad actual">La líder del equipo y la persona de base de datos definen el enfoque técnico de cada proyecto</td>
                      <td data-label="Brecha">Sin arquitecto ni documento que fije cómo desarrollar; decisiones técnicas sin registro</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Construcción y tecnología</strong></td>
                      <td data-label="Capacidad actual">Un desarrollador de front-end en Angular y uno de back-end en Java por módulo; WildFly 34 desde 2026</td>
                      <td data-label="Brecha">Angular 13 fuera de soporte y actualización a Java 21 pendiente</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Revisión, pruebas y despliegue</strong></td>
                      <td data-label="Capacidad actual">Revisión manual de la líder del equipo y validación en preproducción</td>
                      <td data-label="Brecha">Sin CI/CD ni cobertura automatizada documentada; despliegue que depende de una persona</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Seguridad</strong></td>
                      <td data-label="Capacidad actual">Dos personas de seguridad vinculadas este año; WAF, Defender for Cloud y copias por ambiente</td>
                      <td data-label="Brecha">Primera revisión de seguridad de las aplicaciones en 2026; sin análisis de código ni de dependencias confirmado</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Inteligencia artificial</strong></td>
                      <td data-label="Capacidad actual">Licencias de Claude, créditos en OpenRouter y acceso a ChatGPT con Codex</td>
                      <td data-label="Brecha">Uso como chat compartido, sin método ni política, y con condiciones de datos por definir</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Documentación y trazabilidad</strong></td>
                      <td data-label="Capacidad actual">Actas en SharePoint, prototipos en Figma y Azure DevOps habilitado</td>
                      <td data-label="Brecha">Sin gestor de trabajo con estados, sin documentos técnicos por aplicación y sin vínculo entre acta y código</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 15: Puntos de fricción (Tabla 3.6) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Puntos de fricción del diagnóstico (F-01 a F-10)</h2>
              <ul class="slide-list">
                <li>
                  <strong>Tres condiciones del entorno:</strong> la auditoría de la Contraloría, el presupuesto (servicios del Marketplace de Azure) y la confidencialidad y propiedad que fija la minuta.
                </li>
                <li>
                  <strong>Fricción de mayor peso (F-04):</strong> sin arquitecto ni reglas escritas, un agente de IA replica el desorden más rápido.
                </li>
                <li>
                  <strong>El cuello de botella no es escribir código:</strong> está en la formalización y la estabilidad de los requerimientos.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(0.97vw,1.73vh),1.5rem);">
                  <caption>Tabla 3.6 — Puntos de fricción del acta 01 con el dato que los sustenta</caption>
                  <thead>
                    <tr>
                      <th style="width:7%;font-size:0.82em;">ID</th>
                      <th style="width:27%;font-size:0.82em;">Fricción</th>
                      <th style="width:30%;font-size:0.82em;">Efecto</th>
                      <th style="font-size:0.82em;">Dato</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="ID"><strong>F-01</strong></td>
                      <td data-label="Fricción">El acta es una épica sin descomponer</td>
                      <td data-label="Efecto">Difícil de estimar, paralelizar y verificar por partes</td>
                      <td data-label="Dato">Acta de 12 páginas para un módulo; 0 historias y tareas derivadas</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-02</strong></td>
                      <td data-label="Fricción">El desarrollo arranca sin una validación o aceptación final del cliente</td>
                      <td data-label="Efecto">Reprocesos cuando la firma trae cambios</td>
                      <td data-label="Dato">Un módulo del año anterior rechazado en pruebas</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-03</strong></td>
                      <td data-label="Fricción">La única documentación es el acta y el Figma</td>
                      <td data-label="Efecto">Conocimiento en las personas; auditoría apoyada en un documento</td>
                      <td data-label="Dato">0 documentos técnicos o de arquitectura por aplicación</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong style="color:var(--accent);">F-04</strong></td>
                      <td data-label="Fricción"><strong>Sin arquitecto ni estándar de desarrollo</strong></td>
                      <td data-label="Efecto">Código heterogéneo y deuda técnica</td>
                      <td data-label="Dato">0 arquitectos; estructura de carpetas a criterio de cada desarrollador</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-05</strong></td>
                      <td data-label="Fricción">La calidad se valida al final</td>
                      <td data-label="Efecto">Defectos cerca de producción</td>
                      <td data-label="Dato">Validación en preproducción; sin cobertura automatizada documentada</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-06</strong></td>
                      <td data-label="Fricción">Despliegue manual, sin CI/CD</td>
                      <td data-label="Efecto">Dependencia de una persona y sin traza</td>
                      <td data-label="Dato">0 pipelines; 1 persona despliega; solo se conserva la última versión</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-07</strong></td>
                      <td data-label="Fricción">Estimaciones poco confiables y presión de plazos</td>
                      <td data-label="Efecto">Compromisos difíciles de cumplir</td>
                      <td data-label="Dato">Estimación recortada en dos instancias; 1 a 2,5 semanas por interfaz</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-08</strong></td>
                      <td data-label="Fricción">IA como chat con licencias compartidas</td>
                      <td data-label="Efecto">Beneficio limitado, riesgo de fuga y sin traza</td>
                      <td data-label="Dato">Unos 6 asientos de Claude compartidos; sin política de uso</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-09</strong></td>
                      <td data-label="Fricción">Angular 13 fuera de soporte</td>
                      <td data-label="Efecto">Riesgo de seguridad y herramientas modernas incompatibles</td>
                      <td data-label="Dato">Distancia de 9 a 10 versiones mayores frente a la 22 o 23</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-10</strong></td>
                      <td data-label="Fricción">Migración a Azure sin flujo de ingeniería definido</td>
                      <td data-label="Efecto">Riesgo de replicar el proceso manual en la nube</td>
                      <td data-label="Dato">Fase 1 sin refactorización; fase 2 sin decisión</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 16: Línea base de madurez y DORA (Tablas 3.7 y 3.8) [c1-madurez] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e1" data-item="c1-madurez" data-tone="amber">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
                <h2 style="margin-bottom:4px;">Línea base de madurez: seis de nueve dimensiones en nivel inicial</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Ninguna dimensión supera el nivel 2; los más bajos están en estándares, trazabilidad, calidad y despliegue. Las métricas DORA completan la línea base.</p>
              </div>
              <div style="flex:1 1 auto;min-height:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));gap:14px;align-items:start;">
                <figure style="margin:0;display:flex;flex-direction:column;min-height:0;min-width:0;">
                  <svg viewBox="0 0 520 372" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Línea base de madurez de nueve dimensiones: nivel actual de ATENEA frente al nivel objetivo al cierre del contrato, en una escala de 1 a 5">
                  <line x1="228" y1="30" x2="228" y2="318" stroke="#BAC7D5" stroke-width="1" />
                  <text x="228" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">1</text>
                  <line x1="296" y1="30" x2="296" y2="318" stroke="#BAC7D5" stroke-width="1" />
                  <text x="296" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">2</text>
                  <line x1="364" y1="30" x2="364" y2="318" stroke="#BAC7D5" stroke-width="1" />
                  <text x="364" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">3</text>
                  <line x1="432" y1="30" x2="432" y2="318" stroke="#BAC7D5" stroke-width="1" />
                  <text x="432" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">4</text>
                  <line x1="500" y1="30" x2="500" y2="318" stroke="#BAC7D5" stroke-width="1" />
                  <text x="500" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">5</text>
                  <rect x="0" y="30" width="520" height="32" fill="#F3F7FB" />
                  <text x="200" y="51" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Requerimientos</text>
                  <line x1="296" y1="46" x2="364" y2="46" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="364" cy="46" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="364" y="51" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="296" cy="46" r="11" fill="#8A5A00" />
                  <text x="296" y="51" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">2</text>
                  <text x="200" y="83" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Arquitectura y estándares</text>
                  <line x1="228" y1="78" x2="364" y2="78" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="364" cy="78" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="364" y="83" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="228" cy="78" r="11" fill="#B71C1C" />
                  <text x="228" y="83" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">1</text>
                  <rect x="0" y="94" width="520" height="32" fill="#F3F7FB" />
                  <text x="200" y="115" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Calidad y pruebas</text>
                  <line x1="228" y1="110" x2="364" y2="110" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="364" cy="110" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="364" y="115" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="228" cy="110" r="11" fill="#B71C1C" />
                  <text x="228" y="115" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">1</text>
                  <text x="200" y="147" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Integración y despliegue</text>
                  <line x1="228" y1="142" x2="364" y2="142" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="364" cy="142" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="364" y="147" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="228" cy="142" r="11" fill="#B71C1C" />
                  <text x="228" y="147" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">1</text>
                  <rect x="0" y="158" width="520" height="32" fill="#F3F7FB" />
                  <text x="200" y="179" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Estimación y planeación</text>
                  <line x1="228" y1="174" x2="296" y2="174" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="296" cy="174" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="296" y="179" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">2</text>
                  <circle cx="228" cy="174" r="11" fill="#B71C1C" />
                  <text x="228" y="179" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">1</text>
                  <text x="200" y="211" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Trazabilidad</text>
                  <line x1="228" y1="206" x2="364" y2="206" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="364" cy="206" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="364" y="211" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="228" cy="206" r="11" fill="#B71C1C" />
                  <text x="228" y="211" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">1</text>
                  <rect x="0" y="222" width="520" height="32" fill="#F3F7FB" />
                  <text x="200" y="243" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Seguridad</text>
                  <line x1="296" y1="238" x2="364" y2="238" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="364" cy="238" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="364" y="243" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="296" cy="238" r="11" fill="#8A5A00" />
                  <text x="296" y="243" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">2</text>
                  <text x="200" y="275" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Uso de IA</text>
                  <line x1="228" y1="270" x2="364" y2="270" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="364" cy="270" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="364" y="275" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="228" cy="270" r="11" fill="#B71C1C" />
                  <text x="228" y="275" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">1</text>
                  <rect x="0" y="286" width="520" height="32" fill="#F3F7FB" />
                  <text x="200" y="307" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="end">Datos y ambientes</text>
                  <line x1="296" y1="302" x2="364" y2="302" stroke="#6E8CA0" stroke-width="3" />
                  <circle cx="364" cy="302" r="11" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="364" y="307" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="296" cy="302" r="11" fill="#8A5A00" />
                  <text x="296" y="307" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">2</text>
                  <circle cx="20" cy="344" r="9" fill="#B71C1C" />
                  <text x="36" y="349" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Nivel hoy</text>
                  <circle cx="132" cy="344" r="9" fill="#FFFFFF" stroke="#1E5631" stroke-width="3" />
                  <text x="148" y="349" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Objetivo al cierre del contrato</text>
                  </svg>
                  <figcaption class="fig-caption">Tabla 3.7 — Línea base de madurez por dimensión (niveles CMMI 1 a 5) y nivel objetivo al cierre del contrato</figcaption>
                </figure>
                <figure style="margin:0;min-height:0;min-width:0;overflow:auto;">
                  <div class="data-table-wrapper">
                    <table class="data-table" style="font-size:clamp(0.72rem,min(0.98vw,1.75vh),1.5rem);">
                      <caption>Tabla 3.8 — Métricas DORA: situación actual y dato que debe aportar ATENEA</caption>
                      <thead>
                        <tr>
                          <th style="width:24%;font-size:0.82em;">Métrica</th>
                          <th style="width:42%;font-size:0.82em;">Situación actual</th>
                          <th style="font-size:0.82em;">Por confirmar por ATENEA</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td data-label="Métrica"><strong>Frecuencia de despliegue</strong></td>
                          <td data-label="Situación actual">Sin registro; cada despliegue es manual y a demanda</td>
                          <td data-label="Por confirmar por ATENEA">Despliegues por mes y por aplicación</td>
                        </tr>
                        <tr>
                          <td data-label="Métrica"><strong>Tiempo de espera de los cambios</strong></td>
                          <td data-label="Situación actual">Aproximado por la estimación: 1 a 2,5 semanas por interfaz, máximo un mes</td>
                          <td data-label="Por confirmar por ATENEA">Tiempo real desde la firma del acta hasta producción</td>
                        </tr>
                        <tr>
                          <td data-label="Métrica"><strong>Tasa de fallos por cambio</strong></td>
                          <td data-label="Situación actual">Sin registro; al menos un módulo del año anterior rechazado en pruebas</td>
                          <td data-label="Por confirmar por ATENEA">Cambios que exigieron corrección o reversión</td>
                        </tr>
                        <tr>
                          <td data-label="Métrica"><strong>Tiempo de recuperación de despliegues fallidos</strong></td>
                          <td data-label="Situación actual">Sin registro; al conservarse solo la última imagen, revertir exige reconstruir la versión anterior</td>
                          <td data-label="Por confirmar por ATENEA">Tiempo medio para restablecer el servicio</td>
                        </tr>
                        <tr>
                          <td data-label="Métrica"><strong>Tasa de retrabajo en despliegues</strong></td>
                          <td data-label="Situación actual">Sin registro; los cambios de la firma tardía regresan a construcción (F-02)</td>
                          <td data-label="Por confirmar por ATENEA">Despliegues no planeados para corregir otro despliegue</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </figure>
              </div>
              <div class="mobile-alt">
                <p class="sched-title">Madurez por dimensión (hoy → objetivo)</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>Requerimientos:</strong> nivel 2 → objetivo 3</li>
                  <li><strong>Arquitectura y estándares:</strong> nivel 1 → objetivo 3</li>
                  <li><strong>Calidad y pruebas:</strong> nivel 1 → objetivo 3</li>
                  <li><strong>Integración y despliegue:</strong> nivel 1 → objetivo 3</li>
                  <li><strong>Estimación y planeación:</strong> nivel 1 → objetivo 2</li>
                  <li><strong>Trazabilidad:</strong> nivel 1 → objetivo 3</li>
                  <li><strong>Seguridad:</strong> nivel 2 → objetivo 3</li>
                  <li><strong>Uso de IA:</strong> nivel 1 → objetivo 3</li>
                  <li><strong>Datos y ambientes:</strong> nivel 2 → objetivo 3</li>
                </ul>
                <p class="sched-sub">Escala CMMI: 1 inicial · 2 gestionado · 3 definido · 4 gestionado cuantitativamente · 5 en optimización.</p>
              </div>
            </figure>
          </article>

          <!-- Slide 17: Mapa de calor de riesgos (Figura 3.3) [c1-riesgos] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e1" data-item="c1-riesgos" data-tone="amber">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
                <h2 style="margin-bottom:4px;">Mapa de calor de riesgos técnicos: dos extremos y diez altos</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Probabilidad de 1 (raro) a 5 (casi cierto) e impacto de 1 (insignificante) a 5 (catastrófico); la valoración preliminar debe validarla ATENEA.</p>
              </div>
              <svg viewBox="0 0 1200 470" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mapa de calor 5 por 5 de los riesgos técnicos RT-01 a RT-13 según probabilidad e impacto, con las bandas bajo, medio, alto y extremo">
              <text x="203" y="55.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15" text-anchor="end">Casi cierto 5</text>
              <rect x="215" y="14" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <rect x="343" y="14" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <rect x="471" y="14" width="128" height="70" fill="#EDB4B4" stroke="#FFFFFF" stroke-width="2" />
              <rect x="599" y="14" width="128" height="70" fill="#EDB4B4" stroke="#FFFFFF" stroke-width="2" />
              <rect x="727" y="14" width="128" height="70" fill="#EDB4B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="203" y="125.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15" text-anchor="end">Probable 4</text>
              <rect x="215" y="84" width="128" height="70" fill="#FBF0D2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="343" y="84" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <rect x="471" y="84" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="505.0" y="115.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-04</text>
              <text x="565.0" y="115.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-06</text>
              <text x="505.0" y="134.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-09</text>
              <text x="565.0" y="134.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-10</text>
              <rect x="599" y="84" width="128" height="70" fill="#EDB4B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="663.0" y="115.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-01</text>
              <text x="663.0" y="134.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-02</text>
              <rect x="727" y="84" width="128" height="70" fill="#EDB4B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="203" y="195.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15" text-anchor="end">Posible 3</text>
              <rect x="215" y="154" width="128" height="70" fill="#DCEFE2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="343" y="154" width="128" height="70" fill="#FBF0D2" stroke="#FFFFFF" stroke-width="2" />
              <text x="407.0" y="194.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-12</text>
              <rect x="471" y="154" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="535.0" y="185.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-08</text>
              <text x="535.0" y="204.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-13</text>
              <rect x="599" y="154" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="633.0" y="185.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-03</text>
              <text x="693.0" y="185.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-05</text>
              <text x="633.0" y="204.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-07</text>
              <text x="693.0" y="204.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">RT-11</text>
              <rect x="727" y="154" width="128" height="70" fill="#EDB4B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="203" y="265.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15" text-anchor="end">Improbable 2</text>
              <rect x="215" y="224" width="128" height="70" fill="#DCEFE2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="343" y="224" width="128" height="70" fill="#DCEFE2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="471" y="224" width="128" height="70" fill="#FBF0D2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="599" y="224" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <rect x="727" y="224" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="203" y="335.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15" text-anchor="end">Raro 1</text>
              <rect x="215" y="294" width="128" height="70" fill="#DCEFE2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="343" y="294" width="128" height="70" fill="#DCEFE2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="471" y="294" width="128" height="70" fill="#DCEFE2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="599" y="294" width="128" height="70" fill="#FBF0D2" stroke="#FFFFFF" stroke-width="2" />
              <rect x="727" y="294" width="128" height="70" fill="#F6D3B4" stroke="#FFFFFF" stroke-width="2" />
              <text x="279.0" y="386" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">1 Insignificante</text>
              <text x="407.0" y="386" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">2 Menor</text>
              <text x="535.0" y="386" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">3 Moderado</text>
              <text x="663.0" y="386" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">4 Mayor</text>
              <text x="791.0" y="386" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">5 Catastrófico</text>
              <text x="535.0" y="412" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Impacto</text>
              <text x="34" y="189.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle" transform="rotate(-90 34 189.0)">Probabilidad</text>
              <text x="905" y="34" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Valoración V = P + I</text>
              <rect x="905" y="58" width="22" height="22" rx="4" fill="#EDB4B4" stroke="#8A97A8" />
              <text x="937" y="75" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Extremo (8 a 10)</text>
              <text x="937" y="98" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">RT-01, RT-02</text>
              <rect x="905" y="134" width="22" height="22" rx="4" fill="#F6D3B4" stroke="#8A97A8" />
              <text x="937" y="151" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Alto (6 y 7)</text>
              <text x="937" y="174" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">RT-03 a RT-11 y RT-13</text>
              <rect x="905" y="210" width="22" height="22" rx="4" fill="#FBF0D2" stroke="#8A97A8" />
              <text x="937" y="227" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Medio (5)</text>
              <text x="937" y="250" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">RT-12</text>
              <rect x="905" y="286" width="22" height="22" rx="4" fill="#DCEFE2" stroke="#8A97A8" />
              <text x="937" y="303" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Bajo (2 a 4)</text>
              <text x="937" y="326" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">ninguno</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Riesgos por banda de valoración</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><span class="pill pill--risk">Extremo (8 a 10)</span> RT-01 y RT-02 (probabilidad 4, impacto 4).</li>
                  <li><span class="pill pill--partial">Alto (6 y 7)</span> RT-04, RT-06, RT-09 y RT-10 (P 4, I 3); RT-03, RT-05, RT-07 y RT-11 (P 3, I 4); RT-08 y RT-13 (P 3, I 3).</li>
                  <li><span class="pill pill--ok">Medio (5)</span> RT-12 (P 3, I 2).</li>
                  <li><span class="pill pill--todo">Bajo (2 a 4)</span> ningún riesgo.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 3.3 — Mapa de calor de los riesgos técnicos según su probabilidad y su impacto, con las categorías de valoración de los estudios previos</figcaption>
            </figure>
          </article>

          <!-- Slide 18: Matriz de riesgos (Tabla 3.9) [c1-riesgos] -->
          <article class="slide" data-deck="e1-e4" data-module="e1" data-item="c1-riesgos">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Matriz de riesgos técnicos RT-01 a RT-13</h2>
              <ul class="slide-list">
                <li>
                  <strong>Metodología de los estudios previos:</strong> P de 1 a 5, I de 1 a 5 y valoración V = P + I; bajo (2 a 4), medio (5), alto (6 y 7) y extremo (8 a 10).
                </li>
                <li>
                  <strong>Dos riesgos extremos con tratamiento dentro del contrato:</strong> la política de uso de IA (RT-01) y el análisis de dependencias en el pipeline (RT-02).
                </li>
                <li>
                  <strong>Estimación preliminar de la Universidad:</strong> ATENEA debe validarla, junto con los responsables de cada tratamiento.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper is-scroll-x">
                <table class="data-table is-scroll-x" style="font-size:clamp(0.72rem,min(1.02vw,1.8vh),1.5rem);">
                  <caption>Tabla 3.9 — Matriz de riesgos técnicos, versión condensada (P: probabilidad; I: impacto; V = P + I); el informe añade tratamiento y responsable</caption>
                  <thead>
                    <tr>
                      <th style="width:8%;font-size:0.82em;">ID</th>
                      <th style="font-size:0.82em;">Riesgo</th>
                      <th style="width:5%;font-size:0.82em;">P</th>
                      <th style="width:5%;font-size:0.82em;">I</th>
                      <th style="width:5%;font-size:0.82em;">V</th>
                      <th style="width:12%;font-size:0.82em;">Banda</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="ID"><strong>RT-01</strong></td>
                      <td data-label="Riesgo">Fuga de código o de datos por usar IA sin política de uso (F-08)</td>
                      <td data-label="P">4</td>
                      <td data-label="I">4</td>
                      <td data-label="V">8</td>
                      <td data-label="Banda"><span class="pill pill--risk">Extremo</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-02</strong></td>
                      <td data-label="Riesgo">Vulnerabilidades por Angular 13 fuera de soporte y librerías desactualizadas (F-09)</td>
                      <td data-label="P">4</td>
                      <td data-label="I">4</td>
                      <td data-label="V">8</td>
                      <td data-label="Banda"><span class="pill pill--risk">Extremo</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-03</strong></td>
                      <td data-label="Riesgo">Token de sesión guardado en local storage</td>
                      <td data-label="P">3</td>
                      <td data-label="I">4</td>
                      <td data-label="V">7</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-04</strong></td>
                      <td data-label="Riesgo">Una sola persona despliega y una sola revisa el código antes de integrar (F-06)</td>
                      <td data-label="P">4</td>
                      <td data-label="I">3</td>
                      <td data-label="V">7</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-05</strong></td>
                      <td data-label="Riesgo">No se puede revertir un despliegue: solo se conserva la última imagen</td>
                      <td data-label="P">3</td>
                      <td data-label="I">4</td>
                      <td data-label="V">7</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-06</strong></td>
                      <td data-label="Riesgo">La firma tardía del acta trae cambios con la construcción ya iniciada (F-02)</td>
                      <td data-label="P">4</td>
                      <td data-label="I">3</td>
                      <td data-label="V">7</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-07</strong></td>
                      <td data-label="Riesgo">Un agente ejecuta acciones no autorizadas por inyección de instrucciones o abuso de herramientas</td>
                      <td data-label="P">3</td>
                      <td data-label="I">4</td>
                      <td data-label="V">7</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-08</strong></td>
                      <td data-label="Riesgo">Las salidas de los agentes no cumplen los criterios de aceptación</td>
                      <td data-label="P">3</td>
                      <td data-label="I">3</td>
                      <td data-label="V">6</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-09</strong></td>
                      <td data-label="Riesgo">La migración a Azure compite por el tiempo del equipo y cambia el entorno (F-10)</td>
                      <td data-label="P">4</td>
                      <td data-label="I">3</td>
                      <td data-label="V">7</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-10</strong></td>
                      <td data-label="Riesgo">Demoras en accesos, documentos y en la decisión del caso de uso</td>
                      <td data-label="P">4</td>
                      <td data-label="I">3</td>
                      <td data-label="V">7</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-11</strong></td>
                      <td data-label="Riesgo">La evidencia no basta ante la Contraloría: no hay traza entre acta y código</td>
                      <td data-label="P">3</td>
                      <td data-label="I">4</td>
                      <td data-label="V">7</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-12</strong></td>
                      <td data-label="Riesgo">Consumo de modelos sin medición ni techo de gasto</td>
                      <td data-label="P">3</td>
                      <td data-label="I">2</td>
                      <td data-label="V">5</td>
                      <td data-label="Banda"><span class="pill pill--ok">Medio</span></td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RT-13</strong></td>
                      <td data-label="Riesgo">Servicios del Marketplace de Azure fuera del plan anual de adquisiciones</td>
                      <td data-label="P">3</td>
                      <td data-label="I">3</td>
                      <td data-label="V">6</td>
                      <td data-label="Banda"><span class="pill pill--partial">Alto</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 19: Inventario de datos (Tabla 3.10) [c1-datos] -->
          <article class="slide" data-deck="e1-e4" data-module="e1" data-item="c1-datos">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Inventario de sistemas y fuentes de datos</h2>
              <ul class="slide-list">
                <li>
                  <strong>Clasificación por la cláusula décima:</strong> datos personales, sensibles, de menores, información académica e información estratégica de convocatorias son confidenciales.
                </li>
                <li>
                  <strong>Regla propuesta el 16 de octubre:</strong> los datos personales no deben llegar nunca al modelo; de las bases solo viaja la estructura.
                </li>
                <li>
                  <strong>Solo dos fuentes llegan al modelo:</strong> el código fuente y las actas y prototipos con datos de ejemplo anonimizados.
                </li>
                <li>
                  <strong>Pendiente de ATENEA:</strong> responsable y volumen de cada fuente, datos reales o enmascarados en QA y condiciones de datos de cada licencia de IA.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.05vw,1.87vh),1.5rem);">
                  <caption>Tabla 3.10 — Inventario de sistemas y fuentes de datos, con su clasificación y su uso permitido por los agentes de IA</caption>
                  <thead>
                    <tr>
                      <th style="width:20%;font-size:0.82em;">Fuente</th>
                      <th style="width:24%;font-size:0.82em;">Tecnología</th>
                      <th style="width:27%;font-size:0.82em;">Clasificación (cláusula décima)</th>
                      <th style="font-size:0.82em;">¿Llega al modelo?</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Fuente"><strong>Base de datos de SICORE Posmedia</strong></td>
                      <td data-label="Tecnología">Oracle Autonomous</td>
                      <td data-label="Clasificación (cláusula décima)">Confidencial: datos personales e información académica</td>
                      <td data-label="¿Llega al modelo?"><span class="pill pill--risk">No</span> solo la estructura (tablas y columnas), sin registros</td>
                    </tr>
                    <tr>
                      <td data-label="Fuente"><strong>Base de datos de SICORE CTeI (HEMA)</strong></td>
                      <td data-label="Tecnología">Oracle Autonomous</td>
                      <td data-label="Clasificación (cláusula décima)">Confidencial: datos personales y convocatorias no publicadas</td>
                      <td data-label="¿Llega al modelo?"><span class="pill pill--risk">No</span> solo la estructura</td>
                    </tr>
                    <tr>
                      <td data-label="Fuente"><strong>Servidor de archivos</strong></td>
                      <td data-label="Tecnología">Servidor de la aplicación</td>
                      <td data-label="Clasificación (cláusula décima)">Confidencial: datos personales, posiblemente sensibles</td>
                      <td data-label="¿Llega al modelo?"><span class="pill pill--risk">No</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fuente"><strong>Identidad</strong></td>
                      <td data-label="Tecnología">Keycloak</td>
                      <td data-label="Clasificación (cláusula décima)">Confidencial: credenciales</td>
                      <td data-label="¿Llega al modelo?"><span class="pill pill--risk">No</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fuente"><strong>Academia Atenea</strong></td>
                      <td data-label="Tecnología">Moodle</td>
                      <td data-label="Clasificación (cláusula décima)">Confidencial: información académica</td>
                      <td data-label="¿Llega al modelo?"><span class="pill pill--risk">No</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fuente"><strong>Analítica</strong></td>
                      <td data-label="Tecnología">Azure Databricks y Data Factory; dos lagos de datos pequeños</td>
                      <td data-label="Clasificación (cláusula décima)">Confidencial mientras no se anonimicen</td>
                      <td data-label="¿Llega al modelo?"><span class="pill pill--risk">No</span> <span class="pill pill--partial">Por confirmar</span> agregados anónimos</td>
                    </tr>
                    <tr>
                      <td data-label="Fuente"><strong>Código fuente</strong></td>
                      <td data-label="Tecnología">Oracle Visual Builder, en migración a Azure DevOps</td>
                      <td data-label="Clasificación (cláusula décima)">Propiedad de ATENEA</td>
                      <td data-label="¿Llega al modelo?"><span class="pill pill--ok">Sí</span> con la licencia institucional y sin entrenamiento del proveedor</td>
                    </tr>
                    <tr>
                      <td data-label="Fuente"><strong>Actas y prototipos</strong></td>
                      <td data-label="Tecnología">SharePoint y Figma</td>
                      <td data-label="Clasificación (cláusula décima)">Interna; puede contener datos de ejemplo</td>
                      <td data-label="¿Llega al modelo?"><span class="pill pill--ok">Sí</span> con datos de ejemplo anonimizados</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 20: Caso de uso priorizado (sección 5.4) [c1-caso-uso] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e1" data-item="c1-caso-uso" data-caption-source="§5.4" data-tone="amber">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
                <h2 style="margin-bottom:4px;">Caso de uso priorizado: tres candidatos frente a siete criterios</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">La minuta encarga identificar y priorizar el caso de uso (obligación 5); el informe lo deja a ATENEA y aún no está seleccionado.</p>
              </div>
              <svg viewBox="0 0 1200 540" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Matriz de tres candidatos de caso de uso frente a siete criterios de selección; el informe no puntúa a los candidatos y ATENEA aún no decide">
              <rect x="474" y="8" width="228" height="170" rx="9" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.4" />
              <circle cx="496" cy="32" r="14" fill="#2C6B87" />
              <text x="496" y="38" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">1</text>
              <text x="516" y="32" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Servicio unificado</text>
              <text x="516" y="49" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">con Keycloak</text>
              <text x="484" y="75" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">Usuarios, roles y permisos</text>
              <text x="484" y="92" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">de SICORE Posmedia y SICORE</text>
              <text x="484" y="109" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">CTeI; la líder del equipo</text>
              <text x="484" y="126" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">lo consideró probable (R2)</text>
              <rect x="710" y="8" width="228" height="170" rx="9" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.4" />
              <circle cx="732" cy="32" r="14" fill="#2C6B87" />
              <text x="732" y="38" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">2</text>
              <text x="752" y="32" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Creación de</text>
              <text x="752" y="49" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">terceros, SICORE</text>
              <text x="752" y="66" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Posmedia</text>
              <text x="720" y="92" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">Recomendado en el análisis</text>
              <text x="720" y="109" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">de inconsistencias (A2); es</text>
              <text x="720" y="126" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">el caso de referencia de</text>
              <text x="720" y="143" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">los ocho elementos de C3</text>
              <rect x="946" y="8" width="228" height="170" rx="9" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.4" />
              <circle cx="968" cy="32" r="14" fill="#2C6B87" />
              <text x="968" y="38" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">3</text>
              <text x="988" y="32" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">SICORE, HEMA o</text>
              <text x="988" y="49" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Academia Atenea</text>
              <text x="956" y="75" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">Opción general planteada</text>
              <text x="956" y="92" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">por ATENEA (R4)</text>
              <text x="20" y="168" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">7 criterios propuestos</text>
              <rect x="16" y="186" width="1158" height="42" fill="#F3F7FB" />
              <circle cx="34" cy="207.0" r="12" fill="#7FB4CA" />
              <text x="34" y="212.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">1</text>
              <text x="58" y="213.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Valor para ATENEA</text>
              <circle cx="588.0" cy="207.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="824.0" cy="207.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="1060.0" cy="207.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <rect x="16" y="228" width="1158" height="42" fill="#FFFFFF" />
              <circle cx="34" cy="249.0" r="12" fill="#7FB4CA" />
              <text x="34" y="254.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">2</text>
              <text x="58" y="255.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Cabe en el plazo con el equipo disponible</text>
              <circle cx="588.0" cy="249.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="824.0" cy="249.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="1060.0" cy="249.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <rect x="16" y="270" width="1158" height="42" fill="#F3F7FB" />
              <circle cx="34" cy="291.0" r="12" fill="#7FB4CA" />
              <text x="34" y="296.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">3</text>
              <text x="58" y="297.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Hay especificación, diseño y acceso al código</text>
              <circle cx="588.0" cy="291.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="824.0" cy="291.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="1060.0" cy="291.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <rect x="16" y="312" width="1158" height="42" fill="#FFFFFF" />
              <circle cx="34" cy="333.0" r="12" fill="#7FB4CA" />
              <text x="34" y="338.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">4</text>
              <text x="58" y="339.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Se pueden escribir criterios y pruebas</text>
              <circle cx="588.0" cy="333.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="824.0" cy="333.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="1060.0" cy="333.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <rect x="16" y="354" width="1158" height="42" fill="#F3F7FB" />
              <circle cx="34" cy="375.0" r="12" fill="#7FB4CA" />
              <text x="34" y="380.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">5</text>
              <text x="58" y="381.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">No requiere datos personales reales</text>
              <circle cx="588.0" cy="375.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="824.0" cy="375.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="1060.0" cy="375.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <rect x="16" y="396" width="1158" height="42" fill="#FFFFFF" />
              <circle cx="34" cy="417.0" r="12" fill="#7FB4CA" />
              <text x="34" y="422.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">6</text>
              <text x="58" y="423.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">No depende de decisiones abiertas de la migración</text>
              <circle cx="588.0" cy="417.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="824.0" cy="417.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="1060.0" cy="417.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <rect x="16" y="438" width="1158" height="42" fill="#F3F7FB" />
              <circle cx="34" cy="459.0" r="12" fill="#7FB4CA" />
              <text x="34" y="464.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">7</text>
              <text x="58" y="465.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Recorre el ciclo completo hasta el despliegue</text>
              <circle cx="588.0" cy="459.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="824.0" cy="459.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <circle cx="1060.0" cy="459.0" r="11" fill="#FFFFFF" stroke="#9DB7C9" stroke-width="2" stroke-dasharray="4,3" />
              <rect x="16" y="492" width="1158" height="36" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.4" />
              <text x="30" y="516" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">ATENEA aún no decide: el 14 de octubre se acordó que la Agencia define y comunica el caso de uso (R3, R4).</text>
              </svg>
              <p class="fig-caption" style="margin:0;padding:2px 10px 0;font-size:clamp(0.78rem,0.95vw,0.95rem);">Círculo punteado: sin valorar; el informe propone los criterios, pero no puntúa a cada candidato.</p>
              <div class="mobile-alt">
                <p class="sched-title">Candidatos y criterios</p>
                <p class="sched-sub">ATENEA aún no decide el caso de uso.</p>
                <ol class="slide-list" style="margin:8px 0;">
                  <li><strong>Servicio unificado con Keycloak:</strong> usuarios, roles y permisos de SICORE Posmedia y SICORE CTeI; la líder del equipo lo consideró probable.</li>
                  <li><strong>Creación de terceros, SICORE Posmedia:</strong> recomendado en el análisis de inconsistencias; es el caso de referencia de los ocho elementos de C3.</li>
                  <li><strong>SICORE, HEMA o Academia Atenea:</strong> opción general planteada por ATENEA.</li>
                </ol>
                <p class="sched-sub">Siete criterios propuestos (el informe no puntúa a los candidatos):</p>
                <ol class="slide-list" style="margin:6px 0;">
                  <li>Valor para ATENEA.</li>
                  <li>Cabe en el plazo con el equipo disponible.</li>
                  <li>Hay especificación, diseño y acceso al código.</li>
                  <li>Se pueden escribir criterios y pruebas.</li>
                  <li>No requiere datos personales reales.</li>
                  <li>No depende de decisiones abiertas de la migración.</li>
                  <li>Recorre el ciclo completo hasta el despliegue.</li>
                </ol>
              </div>
              <figcaption class="fig-caption">Fuente: §5.4 — Caso de uso institucional: tres candidatos y siete criterios de selección (sin tabla ni figura numerada en el informe)</figcaption>
            </figure>
          </article>


          <!-- ========================================================================= -->
          <!-- MÓDULO 3: E2 · Metodología SDLC-IA para ATENEA (Capítulo 4)               -->
          <!-- ========================================================================= -->

          <!-- Slide E2-1: Rediseño del ciclo (principio y seis fases, §4.1) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Rediseño del ciclo de desarrollo: la IA ejecuta, las personas deciden</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">La especificación aprobada con el cliente es la entrada de un ciclo guiado por especificaciones; la verificación ocurre al construir y al cerrar, y el seguimiento y el control de cambios atraviesan todo el ciclo.</p>
              </div>
              <svg viewBox="0 0 1200 466" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Principio del rediseño del ciclo de desarrollo y las seis fases del flujo SDLC-IA">
              <rect x="0" y="0" width="1200" height="88" rx="8" fill="#EDF1F7" stroke="#2C6B87" stroke-width="1.3" />
              <text x="18" y="28" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">PRINCIPIO DEL REDISEÑO: LA IA EJECUTA Y LAS PERSONAS DECIDEN</text>
              <text x="18" y="56" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Cierra tres brechas del diagnóstico: el desglose en unidades estimables y trazables, la arquitectura decidida una vez y aplicada por todos,</text>
              <text x="18" y="76" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">y la estandarización del flujo de desarrollo y de su evidencia.</text>
              <rect x="0" y="104" width="388" height="156" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.5" />
              <rect x="12" y="116" width="30" height="28" rx="5" fill="#7FB4CA" stroke="#7FB4CA" stroke-width="0" />
              <text x="27" y="136" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">1</text>
              <text x="54" y="137" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Entender</text>
              <text x="14" y="170" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Notas y diseño validado</text>
              <text x="14" y="193" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Requisitos numerados</text>
              <text x="14" y="216" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Preguntas de aclaración</text>
              <text x="14" y="246" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">/sw:new · /sw:adopt</text>
              <rect x="406" y="104" width="388" height="156" rx="8" fill="#F8FAFC" stroke="#7AA89F" stroke-width="1.5" />
              <rect x="418" y="116" width="30" height="28" rx="5" fill="#7AA89F" stroke="#7AA89F" stroke-width="0" />
              <text x="433" y="136" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">2</text>
              <text x="460" y="137" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Decidir</text>
              <text x="420" y="170" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Arquitectura y experiencia</text>
              <text x="420" y="193" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Servicios, datos, integraciones</text>
              <text x="420" y="216" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Aprueban PO, LT y BD</text>
              <text x="420" y="246" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Arquitectura vinculante</text>
              <rect x="812" y="104" width="388" height="156" rx="8" fill="#F8FAFC" stroke="#B7CC85" stroke-width="1.5" />
              <rect x="824" y="116" width="30" height="28" rx="5" fill="#B7CC85" stroke="#B7CC85" stroke-width="0" />
              <text x="839" y="136" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">3</text>
              <text x="866" y="137" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Descomponer</text>
              <text x="826" y="170" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Épicas e historias</text>
              <text x="826" y="193" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Criterios de aceptación</text>
              <text x="826" y="216" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Plan de olas en paralelo</text>
              <text x="826" y="246" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">/sw:sprint</text>
              <rect x="0" y="272" width="388" height="156" rx="8" fill="#F8FAFC" stroke="#DFBD76" stroke-width="1.5" />
              <rect x="12" y="284" width="30" height="28" rx="5" fill="#DFBD76" stroke="#DFBD76" stroke-width="0" />
              <text x="27" y="304" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">4</text>
              <text x="54" y="305" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Traducir</text>
              <text x="14" y="338" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Contrato por historia</text>
              <text x="14" y="361" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Traducción determinista</text>
              <text x="14" y="384" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Traza requisito a contrato</text>
              <text x="14" y="414" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Puente OpenSpec</text>
              <rect x="406" y="272" width="388" height="156" rx="8" fill="#F8FAFC" stroke="#7AA89F" stroke-width="1.5" />
              <rect x="418" y="284" width="30" height="28" rx="5" fill="#7AA89F" stroke="#7AA89F" stroke-width="0" />
              <text x="433" y="304" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">5</text>
              <text x="460" y="305" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Construir</text>
              <text x="420" y="338" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Una historia a la vez</text>
              <text x="420" y="361" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Código y prueba por escenario</text>
              <text x="420" y="384" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Cambios: control de cambios</text>
              <text x="420" y="414" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">/sw:build</text>
              <rect x="812" y="272" width="388" height="156" rx="8" fill="#F8FAFC" stroke="#2C6B87" stroke-width="1.5" />
              <rect x="824" y="284" width="30" height="28" rx="5" fill="#2C6B87" stroke="#2C6B87" stroke-width="0" />
              <text x="839" y="304" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">6</text>
              <text x="866" y="305" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Cerrar</text>
              <text x="826" y="338" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Contrato validado en modo estricto</text>
              <text x="826" y="361" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Línea base y memoria</text>
              <text x="826" y="384" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16">Despliega infraestructura</text>
              <text x="826" y="414" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">/sw:close</text>
              <text x="0" y="458" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">Transversal a todo el ciclo: /sw:status (seguimiento) · /sw:change (cambios) · /sw:bug (defectos)</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Las seis fases del flujo SDLC-IA</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>1. Entender:</strong> Notas y diseño validado; Requisitos numerados; Preguntas de aclaración. <em>/sw:new · /sw:adopt</em></li>
                  <li><strong>2. Decidir:</strong> Arquitectura y experiencia; Servicios, datos, integraciones; Aprueban PO, LT y BD. <em>Arquitectura vinculante</em></li>
                  <li><strong>3. Descomponer:</strong> Épicas e historias; Criterios de aceptación; Plan de olas en paralelo. <em>/sw:sprint</em></li>
                  <li><strong>4. Traducir:</strong> Contrato por historia; Traducción determinista; Traza requisito a contrato. <em>Puente OpenSpec</em></li>
                  <li><strong>5. Construir:</strong> Una historia a la vez; Código y prueba por escenario; Cambios: control de cambios. <em>/sw:build</em></li>
                  <li><strong>6. Cerrar:</strong> Contrato validado en modo estricto; Línea base y memoria; Despliega infraestructura. <em>/sw:close</em></li>
                </ul>
                <p style="margin:6px 0 0;">Transversal: /sw:status, /sw:change y /sw:bug.</p>
              </div>
              <figcaption class="fig-caption">Fuente: §4.1 — Las seis fases del flujo SDLC-IA y la herramienta agéntica de cada una (sin figura ni tabla numerada en el informe)</figcaption>
            </figure>
          </article>

          <!-- Slide 15: Mapa Conceptual 1/2: Del Vibe Coding al Arnés de IA (ciclos y componentes) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-tone="emerald">
            <figure class="slide-figure">
              <svg viewBox="0 0 1200 726" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mapa conceptual 1 de 2: del vibe coding al SDLC-IA y al ADLC, y los cuatro componentes del arnés de IA: Graph Engineering, SDD, agente en closed loop y TDD más ODD">
                <defs>
                  <marker id="cm-arr-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#B71C1C" />
                  </marker>
                  <marker id="cm-arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" />
                  </marker>
                  <marker id="cm-arr-gold" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#8A5A00" />
                  </marker>
                  <marker id="cm-arr-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#5E35B1" />
                  </marker>
                </defs>

                <!-- Encabezado -->
                <text x="30" y="30" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">3 · METODOLOGÍA SDLC-IA (E2) · MAPA CONCEPTUAL 1/2</text>
                <text x="30" y="66" fill="#1B2029" font-family="'Source Serif 4',serif" font-size="28" font-weight="700">Del Vibe Coding al Arnés de IA: ciclos y componentes</text>
                <text x="30" y="94" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16" font-style="italic">El humano especifica y audita; la IA construye y valida dentro del arnés.</text>

                <!-- Fila 1: Vibe Coding → SDLC-IA → ADLC -->
                <rect x="30" y="114" width="340" height="214" rx="10" fill="#FFF5F5" stroke="#B71C1C" stroke-width="1.5" />
                <rect x="44" y="126" width="312" height="32" rx="5" fill="#B71C1C" />
                <text x="200" y="148" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">VIBE CODING (ANTIPATRÓN)</text>
                <text x="48" y="190" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">• Prompts ad-hoc en chat</text>
                <text x="48" y="218" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">• Iteración a ciegas</text>
                <text x="48" y="246" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">• Alucinaciones y roturas</text>
                <rect x="44" y="274" width="312" height="38" rx="5" fill="#FFEAEA" stroke="#B71C1C" stroke-width="0.8" />
                <text x="200" y="299" text-anchor="middle" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">⚠ Deuda técnica y reproceso</text>

                <path d="M372 221 H386" stroke="#B71C1C" stroke-width="2" stroke-dasharray="3,2" marker-end="url(#cm-arr-red)" />

                <rect x="390" y="114" width="440" height="214" rx="10" fill="#F4F8FA" stroke="#2C6B87" stroke-width="1.5" />
                <rect x="404" y="126" width="412" height="32" rx="5" fill="#2C6B87" />
                <text x="610" y="148" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">SDLC TRADICIONAL → SDLC-IA</text>
                <text x="408" y="188" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">• 6 etapas gobernadas con IA:</text>
                <rect x="404" y="202" width="412" height="112" rx="6" fill="#FFFFFF" stroke="#BAC7D5" stroke-width="0.8" />
                <line x1="541" y1="210" x2="541" y2="306" stroke="#E2E8F0" stroke-width="1" />
                <line x1="679" y1="210" x2="679" y2="306" stroke="#E2E8F0" stroke-width="1" />
                <line x1="412" y1="258" x2="808" y2="258" stroke="#E2E8F0" stroke-width="1" />
                <text x="472" y="227" text-anchor="middle" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">1. Entender</text>
                <text x="472" y="248" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13.5">PRD y dudas</text>
                <text x="610" y="227" text-anchor="middle" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">2. Decidir</text>
                <text x="610" y="248" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13.5">Arquitectura</text>
                <text x="748" y="227" text-anchor="middle" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">3. Descomponer</text>
                <text x="748" y="248" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13.5">Plan de olas</text>
                <text x="472" y="280" text-anchor="middle" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">4. Traducir</text>
                <text x="472" y="301" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13.5">OpenSpec</text>
                <text x="610" y="280" text-anchor="middle" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">5. Construir</text>
                <text x="610" y="301" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13.5">TDD 1 a 1</text>
                <text x="748" y="280" text-anchor="middle" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">6. Cerrar</text>
                <text x="748" y="301" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13.5">Línea base</text>

                <path d="M832 221 H846" stroke="#5E35B1" stroke-width="2" marker-end="url(#cm-arr-purple)" />

                <rect x="850" y="114" width="320" height="214" rx="10" fill="#FBF8FF" stroke="#5E35B1" stroke-width="1.5" />
                <rect x="864" y="126" width="292" height="32" rx="5" fill="#5E35B1" />
                <text x="1010" y="148" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">ADLC (CICLO DE AGENTES)</text>
                <text x="868" y="190" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">• Roles y tools MCP</text>
                <text x="868" y="218" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">• Presupuesto de contexto</text>
                <text x="868" y="246" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">• Calibración en benchmarks</text>
                <rect x="864" y="274" width="292" height="38" rx="5" fill="#EDE7F6" stroke="#5E35B1" stroke-width="0.8" />
                <text x="1010" y="299" text-anchor="middle" fill="#5E35B1" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">◆ Calibra a los agentes</text>

                <!-- Fila 2: el arnés y sus 4 componentes -->
                <rect x="30" y="346" width="1140" height="370" rx="12" fill="#FFFFFF" stroke="#1E5631" stroke-width="2" />
                <path d="M 30 358 A 12 12 0 0 1 42 346 H 1158 A 12 12 0 0 1 1170 358 V 384 H 30 Z" fill="#1E5631" />
                <text x="48" y="371" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="800" letter-spacing="0.8">EL ARNÉS DE IA: INTEGRA Y CONFINA</text>
                <text x="1152" y="371" text-anchor="end" fill="#B7CC85" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="600">Contexto real · contratos inmutables · tests deterministas</text>

                <!-- Bucle de autocorrección TDD+ODD → Closed Loop -->
                <path d="M1028 426 V404 H744 V422" fill="none" stroke="#B71C1C" stroke-width="1.5" stroke-dasharray="3,2" marker-end="url(#cm-arr-red)" />
                <rect x="790" y="393" width="192" height="22" rx="4" fill="#FFFFFF" stroke="#B71C1C" stroke-width="0.8" />
                <text x="886" y="409" text-anchor="middle" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Si falla el test: auto-corrige</text>

                <!-- C1 Graph Engineering -->
                <rect x="45" y="428" width="258" height="274" rx="9" fill="#F0F7FB" stroke="#2C6B87" stroke-width="1.5" />
                <rect x="55" y="438" width="238" height="30" rx="5" fill="#2C6B87" />
                <text x="174" y="458" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">GRAPH ENGINEERING</text>
                <text x="59" y="496" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">• Grafo del código (AST)</text>
                <text x="71" y="520" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">dependencias, tipos</text>
                <text x="71" y="542" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">y llamadas (Graphify)</text>
                <text x="59" y="576" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">• Contexto determinista</text>
                <text x="71" y="600" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">no adivina archivos</text>
                <text x="71" y="622" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">ni rutas</text>
                <rect x="55" y="650" width="238" height="36" rx="5" fill="#E1EEF5" stroke="#2C6B87" stroke-width="0.8" />
                <text x="174" y="674" text-anchor="middle" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">✓ Cero alucinaciones</text>

                <path d="M305 565 H325" stroke="#2C6B87" stroke-width="2" marker-end="url(#cm-arr-blue)" />

                <!-- C2 SDD -->
                <rect x="329" y="428" width="258" height="274" rx="9" fill="#FFFDF5" stroke="#8A5A00" stroke-width="1.5" />
                <rect x="339" y="438" width="238" height="30" rx="5" fill="#8A5A00" />
                <text x="458" y="458" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">SDD (SPEC-DRIVEN)</text>
                <text x="343" y="496" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">• Spec = única verdad</text>
                <text x="355" y="520" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">PRD formal con</text>
                <text x="355" y="542" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">requisitos FR / NFR</text>
                <text x="343" y="576" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">• Contratos OpenSpec</text>
                <text x="355" y="600" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">inmutables y verificables</text>
                <text x="355" y="622" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">(Given / When / Then)</text>
                <rect x="339" y="650" width="238" height="36" rx="5" fill="#FFF3CD" stroke="#8A5A00" stroke-width="0.8" />
                <text x="458" y="674" text-anchor="middle" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">✓ Sin ambigüedad verbal</text>

                <path d="M589 565 H609" stroke="#8A5A00" stroke-width="2" marker-end="url(#cm-arr-gold)" />

                <!-- C3 Agente en Closed Loop -->
                <rect x="613" y="428" width="258" height="274" rx="9" fill="#F8F5FF" stroke="#5E35B1" stroke-width="1.5" />
                <rect x="623" y="438" width="238" height="30" rx="5" fill="#5E35B1" />
                <text x="742" y="458" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">AGENTE EN CLOSED LOOP</text>
                <text x="627" y="496" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">• Bucle ReAct cerrado</text>
                <text x="639" y="520" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">pensar, actuar (MCP),</text>
                <text x="639" y="542" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">observar y corregir</text>
                <text x="627" y="576" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">• Memoria (Engram)</text>
                <text x="639" y="600" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">lecciones, decisiones</text>
                <text x="639" y="622" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">y estado persistentes</text>
                <rect x="623" y="650" width="238" height="36" rx="5" fill="#EDE7F6" stroke="#5E35B1" stroke-width="0.8" />
                <text x="742" y="674" text-anchor="middle" fill="#5E35B1" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">✓ Ejecución confinada</text>

                <path d="M873 565 H893" stroke="#5E35B1" stroke-width="2" marker-end="url(#cm-arr-purple)" />

                <!-- C4 TDD + ODD -->
                <rect x="897" y="428" width="258" height="274" rx="9" fill="#F4FAF5" stroke="#1E5631" stroke-width="1.5" />
                <rect x="907" y="438" width="238" height="30" rx="5" fill="#1E5631" />
                <text x="1026" y="458" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">TDD + ODD (VERIFICA)</text>
                <text x="911" y="496" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">• Test previo (TDD)</text>
                <text x="923" y="520" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">1 escenario = 1 test,</text>
                <text x="923" y="542" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">función de parada</text>
                <text x="911" y="576" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">• Confinamiento ODD</text>
                <text x="923" y="600" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">edición acotada,</text>
                <text x="923" y="622" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="15">cero colaterales</text>
                <rect x="907" y="650" width="238" height="36" rx="5" fill="#D6EAD8" stroke="#1E5631" stroke-width="0.8" />
                <text x="1026" y="674" text-anchor="middle" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">✓ Criterio: 100 % verde</text>
              </svg>

              <div class="schedule-mobile">
                <p class="sched-title">Mapa conceptual 1/2: del Vibe Coding al Arnés de IA</p>
                <p class="sched-sub">Ciclos de desarrollo y componentes del arnés</p>
                <ul class="slide-list" style="padding-left:1.2em; font-size:0.82rem; margin:8px 0;">
                  <li><strong>Vibe Coding (antipatrón):</strong> prompts ad-hoc e iteración a ciegas generan deuda técnica y reproceso.</li>
                  <li><strong>SDLC-IA y ADLC:</strong> 6 etapas gobernadas con IA, ejecutadas por agentes calibrados en su propio ciclo (ADLC).</li>
                  <li><strong>Arnés de IA:</strong> Graph Engineering (contexto real), SDD (spec como única verdad), agente en closed loop y TDD + ODD (tests como función de parada).</li>
                </ul>
              </div>
            </figure>
          </article>

          <!-- Slide 16: Mapa Conceptual 2/2: Del Vibe Coding al Arnés de IA (roles y tesis) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-tone="emerald">
            <figure class="slide-figure">
              <svg viewBox="0 0 1200 726" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mapa conceptual 2 de 2: el humano especifica, el arnés con agentes deriva el código y el humano audita en compuertas; tesis unificadora del arnés de IA">
                <defs>
                  <marker id="cm2-arr-gold" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#8A5A00" />
                  </marker>
                  <marker id="cm2-arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#1E5631" />
                  </marker>
                </defs>

                <!-- Encabezado -->
                <text x="30" y="30" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">3 · METODOLOGÍA SDLC-IA (E2) · MAPA CONCEPTUAL 2/2</text>
                <text x="30" y="66" fill="#1B2029" font-family="'Source Serif 4',serif" font-size="28" font-weight="700">Del Vibe Coding al Arnés de IA: nuevo reparto de roles</text>
                <text x="30" y="94" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="16" font-style="italic">El código pasa a ser un subproducto de la especificación, el arnés y los tests.</text>

                <!-- R1 Humano especificador -->
                <rect x="30" y="114" width="366" height="350" rx="10" fill="#FFFDF8" stroke="#DFBD76" stroke-width="1.8" />
                <rect x="44" y="126" width="338" height="36" rx="5" fill="#8A5A00" />
                <text x="213" y="150" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">1. HUMANO: ESPECIFICADOR</text>
                <text x="48" y="200" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700">• Ya no escribe sintaxis</text>
                <text x="62" y="228" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">se enfoca en negocio</text>
                <text x="62" y="254" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">y arquitectura</text>
                <text x="48" y="296" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700">• Especificación formal</text>
                <text x="62" y="324" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">casos de uso y BDD</text>
                <text x="62" y="350" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">(Given / When / Then)</text>
                <rect x="44" y="402" width="338" height="44" rx="5" fill="#FFF8E7" stroke="#DFBD76" stroke-width="0.8" />
                <text x="213" y="430" text-anchor="middle" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="15.5" font-weight="700">ACTIVO PERENNE: la spec</text>

                <path d="M398 289 H412" stroke="#8A5A00" stroke-width="2.5" marker-end="url(#cm2-arr-gold)" />

                <!-- R2 Arnés + agentes -->
                <rect x="416" y="114" width="368" height="350" rx="10" fill="#F4FAF5" stroke="#1E5631" stroke-width="1.8" />
                <rect x="430" y="126" width="340" height="36" rx="5" fill="#1E5631" />
                <text x="600" y="150" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">2. ARNÉS + AGENTES: CÓDIGO</text>
                <text x="434" y="200" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700">• Código derivado</text>
                <text x="448" y="228" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">efímero, descartable</text>
                <text x="448" y="254" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">y regenerable</text>
                <text x="434" y="296" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700">• Construcción agéntica</text>
                <text x="448" y="324" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">toma spec + grafo e itera</text>
                <text x="448" y="350" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">hasta tests en verde</text>
                <rect x="430" y="402" width="340" height="44" rx="5" fill="#E3F4E5" stroke="#1E5631" stroke-width="0.8" />
                <text x="600" y="430" text-anchor="middle" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15.5" font-weight="700">Código = Spec + Arnés + Tests</text>

                <path d="M786 289 H800" stroke="#1E5631" stroke-width="2.5" marker-end="url(#cm2-arr-green)" />

                <!-- R3 Humano juez -->
                <rect x="804" y="114" width="366" height="350" rx="10" fill="#FFF8F8" stroke="#C62828" stroke-width="1.8" />
                <rect x="818" y="126" width="338" height="36" rx="5" fill="#C62828" />
                <text x="987" y="150" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">3. HUMANO: JUEZ Y AUDITOR</text>
                <text x="822" y="200" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700">• Compuertas de calidad</text>
                <text x="836" y="228" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">revisa diffs atómicos</text>
                <text x="836" y="254" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">y superficies permitidas</text>
                <text x="822" y="296" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700">• Aprobación soberana</text>
                <text x="836" y="324" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">valida PRs y el paso</text>
                <text x="836" y="350" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="17">a producción</text>
                <rect x="818" y="402" width="338" height="44" rx="5" fill="#FFEBEE" stroke="#C62828" stroke-width="0.8" />
                <text x="987" y="430" text-anchor="middle" fill="#C62828" font-family="Space Grotesk,sans-serif" font-size="15.5" font-weight="700">GOBERNANZA: control de la entidad</text>

                <!-- Tesis unificadora -->
                <rect x="30" y="486" width="1140" height="230" rx="12" fill="#1B2029" stroke="#1E5631" stroke-width="2" />
                <text x="56" y="526" fill="#B7CC85" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="800" letter-spacing="0.8">TESIS: ¿PUEDE EL ARNÉS DE IA ENGLOBAR ESTOS CONCEPTOS?</text>
                <text x="56" y="574" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="19"><tspan font-weight="800" fill="#DFBD76">SÍ.</tspan> El <tspan font-weight="700">Arnés de IA</tspan> es el andamiaje que erradica el <tspan font-weight="700" fill="#EF9A9A">vibe coding</tspan>.</text>
                <text x="56" y="618" fill="#EDF1F7" font-family="Space Grotesk,sans-serif" font-size="19">Articula el <tspan font-weight="700" fill="#7FB4CA">SDLC-IA</tspan> con agentes calibrados (<tspan font-weight="700" fill="#CE93D8">ADLC</tspan>), grafo de código (<tspan font-weight="700" fill="#7FB4CA">AST</tspan>) y <tspan font-weight="700" fill="#CE93D8">closed loop</tspan>.</text>
                <text x="56" y="662" fill="#EDF1F7" font-family="Space Grotesk,sans-serif" font-size="19">El humano especifica (<tspan font-weight="700" fill="#DFBD76">SDD</tspan>) y decide en <tspan font-weight="700" fill="#EF9A9A">compuertas</tspan>; la verificación es objetiva (<tspan font-weight="700" fill="#B7CC85">TDD / ODD</tspan>).</text>
              </svg>

              <div class="schedule-mobile">
                <p class="sched-title">Mapa conceptual 2/2: nuevo reparto de roles</p>
                <p class="sched-sub">El arnés de IA como sistema unificador</p>
                <ul class="slide-list" style="padding-left:1.2em; font-size:0.82rem; margin:8px 0;">
                  <li><strong>Humano especificador:</strong> deja la sintaxis y redacta la especificación formal (casos de uso y BDD), el activo perenne.</li>
                  <li><strong>Arnés + agentes:</strong> el código es derivado y regenerable; el agente itera sobre spec + grafo hasta tests en verde.</li>
                  <li><strong>Humano juez y auditor:</strong> compuertas de calidad sobre diffs atómicos y aprobación soberana de PRs y producción.</li>
                  <li><strong>Tesis:</strong> el arnés articula SDLC-IA, ADLC, AST y closed loop; el humano especifica y decide, la verificación es objetiva (TDD / ODD).</li>
                </ul>
              </div>
            </figure>
          </article>

          <!-- Slide E2-4: Flujo SDLC-IA por fases y carriles (Figura 4.1) [c2-fases] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-fases" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Flujo SDLC-IA por fases y carriles: quién interviene en cada etapa</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El arnés Aracne-SDLC-AI del LIA UNAL produce el artefacto de cada fase y una persona decide en las puertas en rojo.</p>
              </div>
              <svg viewBox="0 0 1200 592" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figura 4.1: flujo SDLC-IA por fases y carriles, con las puertas humanas en rojo">
              <defs>
              <marker id="f41-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
              <marker id="f41-r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#B71C1C" /></marker>
              <marker id="f41-g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#1E5631" /></marker>
              </defs>
              <rect x="0" y="58" width="1200" height="78" fill="#EDF1F7" />
              <path d="M0 58 H1200" stroke="#D6DEE8" stroke-width="1" />
              <text x="78" y="93.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Negocio o</text>
              <text x="78" y="110.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">área cliente</text>
              <rect x="0" y="136" width="1200" height="78" fill="#FFFFFF" />
              <path d="M0 136 H1200" stroke="#D6DEE8" stroke-width="1" />
              <text x="78" y="171.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Líder de producto</text>
              <text x="78" y="188.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">y diseño UI/UX</text>
              <rect x="0" y="214" width="1200" height="78" fill="#EDF1F7" />
              <path d="M0 214 H1200" stroke="#D6DEE8" stroke-width="1" />
              <text x="78" y="249.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Arnés de agentes</text>
              <text x="78" y="266.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">(LIA UNAL)</text>
              <rect x="0" y="292" width="1200" height="78" fill="#FFFFFF" />
              <path d="M0 292 H1200" stroke="#D6DEE8" stroke-width="1" />
              <text x="78" y="327.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Líder técnico, BD</text>
              <text x="78" y="344.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">y desarrollo</text>
              <rect x="0" y="370" width="1200" height="78" fill="#EDF1F7" />
              <path d="M0 370 H1200" stroke="#D6DEE8" stroke-width="1" />
              <text x="78" y="405.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">Infraestructura</text>
              <text x="78" y="422.4" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">y seguridad</text>
              <path d="M0 448 H1200" stroke="#D6DEE8" stroke-width="1" />
              <text x="246.0" y="24" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Entender</text>
              <text x="246.0" y="45" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">hoy: levantamiento</text>
              <text x="418.0" y="24" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Decidir</text>
              <text x="418.0" y="45" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">hoy: acta + Figma</text>
              <path d="M332 10 V448" stroke="#D6DEE8" stroke-width="1" stroke-dasharray="4,4" />
              <text x="590.0" y="24" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Descomponer</text>
              <text x="590.0" y="45" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">hoy: no existe</text>
              <path d="M504 10 V448" stroke="#D6DEE8" stroke-width="1" stroke-dasharray="4,4" />
              <text x="762.0" y="24" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Traducir</text>
              <text x="762.0" y="45" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">hoy: no existe</text>
              <path d="M676 10 V448" stroke="#D6DEE8" stroke-width="1" stroke-dasharray="4,4" />
              <text x="934.0" y="24" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Construir</text>
              <text x="934.0" y="45" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">hoy: desarrollo</text>
              <path d="M848 10 V448" stroke="#D6DEE8" stroke-width="1" stroke-dasharray="4,4" />
              <text x="1106.0" y="24" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Cerrar</text>
              <text x="1106.0" y="45" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">hoy: compilados</text>
              <path d="M1020 10 V448" stroke="#D6DEE8" stroke-width="1" stroke-dasharray="4,4" />
              <rect x="164" y="68.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="244.0" y="85.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Plantea necesidad</text>
              <text x="244.0" y="101.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">en mesas de</text>
              <text x="244.0" y="117.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">trabajo</text>
              <rect x="336" y="68.0" width="160" height="58" rx="6" fill="#FFF2F2" stroke="#B71C1C" stroke-width="2.0" />
              <text x="416.0" y="93.5" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Puerta:</text>
              <text x="416.0" y="109.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">firma del acta</text>
              <rect x="1024" y="68.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="1104.0" y="93.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Validación final</text>
              <text x="1104.0" y="109.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">en preproducción</text>
              <rect x="164" y="146.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="244.0" y="163.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Conversa con</text>
              <text x="244.0" y="179.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">cliente; notas</text>
              <text x="244.0" y="195.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">y Figma</text>
              <rect x="336" y="146.0" width="160" height="58" rx="6" fill="#FFF2F2" stroke="#B71C1C" stroke-width="2.0" />
              <text x="416.0" y="171.5" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Puerta: aprueba</text>
              <text x="416.0" y="187.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">spec y criterios</text>
              <rect x="508" y="146.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="588.0" y="171.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Ajusta historias</text>
              <text x="588.0" y="187.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">y prioridades</text>
              <rect x="164" y="224.0" width="160" height="58" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.4" />
              <text x="244.0" y="249.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">/sw:new / adopt:</text>
              <text x="244.0" y="265.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">PRD y preguntas</text>
              <rect x="336" y="224.0" width="160" height="58" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.4" />
              <text x="416.0" y="249.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Arquitectura y UX</text>
              <text x="416.0" y="265.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">(BMAD); spec formal</text>
              <rect x="508" y="224.0" width="160" height="58" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.4" />
              <text x="588.0" y="249.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Épicas e historias;</text>
              <text x="588.0" y="265.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">plan de olas /sprint</text>
              <rect x="680" y="224.0" width="160" height="58" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.4" />
              <text x="760.0" y="241.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Puente OpenSpec:</text>
              <text x="760.0" y="257.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">contrato por</text>
              <text x="760.0" y="273.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">historia</text>
              <rect x="852" y="224.0" width="160" height="58" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.4" />
              <text x="932.0" y="241.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">/sw:build: código</text>
              <text x="932.0" y="257.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">y prueba por</text>
              <text x="932.0" y="273.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">escenario</text>
              <rect x="1024" y="224.0" width="160" height="58" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.4" />
              <text x="1104.0" y="249.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">/sw:close: valida,</text>
              <text x="1104.0" y="265.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">archiva y memoria</text>
              <rect x="336" y="302.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="416.0" y="327.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Decisiones técnicas:</text>
              <text x="416.0" y="343.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">líder técnico y BD</text>
              <rect x="508" y="302.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="588.0" y="327.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Estiman esfuerzo</text>
              <text x="588.0" y="343.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">por historia</text>
              <rect x="680" y="302.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="760.0" y="327.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Revisan el contrato</text>
              <text x="760.0" y="343.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">verificable</text>
              <rect x="852" y="302.0" width="160" height="58" rx="6" fill="#FFF2F2" stroke="#B71C1C" stroke-width="2.0" />
              <text x="932.0" y="327.5" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Puerta:</text>
              <text x="932.0" y="343.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">revisión y merge</text>
              <rect x="164" y="380.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="244.0" y="405.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Política de uso IA</text>
              <text x="244.0" y="421.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">(con Subgerencia)</text>
              <rect x="852" y="380.0" width="160" height="58" rx="6" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="932.0" y="405.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Pipeline CI/CD</text>
              <text x="932.0" y="421.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Azure (objetivo)</text>
              <rect x="1024" y="380.0" width="160" height="58" rx="6" fill="#FFF2F2" stroke="#B71C1C" stroke-width="2.0" />
              <text x="1104.0" y="405.5" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Puerta: despliegue</text>
              <text x="1104.0" y="421.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">en ambiente</text>
              <path d="M324 253.0 L336 253.0" stroke="#1E5631" stroke-width="1.6" marker-end="url(#f41-g)" />
              <path d="M496 253.0 L508 253.0" stroke="#1E5631" stroke-width="1.6" marker-end="url(#f41-g)" />
              <path d="M668 253.0 L680 253.0" stroke="#1E5631" stroke-width="1.6" marker-end="url(#f41-g)" />
              <path d="M840 253.0 L852 253.0" stroke="#1E5631" stroke-width="1.6" marker-end="url(#f41-g)" />
              <path d="M1012 253.0 L1024 253.0" stroke="#1E5631" stroke-width="1.6" marker-end="url(#f41-g)" />
              <path d="M244.0 126.0 L244.0 146.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#f41-b)" />
              <path d="M244.0 204.0 L244.0 224.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#f41-b)" />
              <path d="M416.0 224.0 L416.0 204.0" stroke="#B71C1C" stroke-width="1.6" marker-end="url(#f41-r)" />
              <path d="M416.0 146.0 L416.0 126.0" stroke="#B71C1C" stroke-width="1.6" marker-end="url(#f41-r)" />
              <path d="M416.0 282.0 L416.0 302.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#f41-b)" />
              <path d="M588.0 224.0 L588.0 204.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#f41-b)" />
              <path d="M588.0 282.0 L588.0 302.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#f41-b)" />
              <path d="M760.0 282.0 L760.0 302.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#f41-b)" />
              <path d="M932.0 282.0 L932.0 302.0" stroke="#B71C1C" stroke-width="1.6" marker-end="url(#f41-r)" />
              <path d="M932.0 360.0 L932.0 380.0" stroke="#B71C1C" stroke-width="1.6" marker-end="url(#f41-r)" />
              <path d="M1012 409.0 L1024 409.0" stroke="#B71C1C" stroke-width="1.6" marker-end="url(#f41-r)" />
              <path d="M1104.0 282.0 L1104.0 380.0" stroke="#2C6B87" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#f41-b)" />
              <path d="M1184 409.0 H1194 V97.0 H1185" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#f41-b)" />
              <rect x="0" y="458" width="1200" height="30" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.2" />
              <text x="14" y="478" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14"><tspan font-weight="700" fill="#1E5631">Contexto del proyecto:</tspan> reglas y negocio (architecture-base.md) · arquitectura (BMAD y graphify) · memoria persistente (Engram)</text>
              <rect x="0" y="494" width="1200" height="30" rx="6" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.2" />
              <text x="14" y="514" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14"><tspan font-weight="700" fill="#2C6B87">Gobierno transversal:</tspan> seguimiento con /sw:status · control de cambios con /sw:change · gestión de defectos con /sw:bug</text>
              <rect x="0" y="530" width="1200" height="30" rx="6" fill="#EDF1F7" stroke="#454F61" stroke-width="1.2" />
              <text x="14" y="550" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14"><tspan font-weight="700" fill="#454F61">Roles institucionales:</tspan> LIA UNAL propone y acompaña · Subgerencia de TIC valida caso de uso, accesos y modelos</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Fases y carriles del flujo SDLC-IA</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>1. Entender</strong> (hoy: levantamiento)<br><em>Negocio:</em> Plantea necesidad en mesas de trabajo<br><em>Líder de producto y UX:</em> Conversa con cliente; notas y Figma<br><em>Arnés de agentes (LIA UNAL):</em> /sw:new / adopt: PRD y preguntas<br><em>Infraestructura y seguridad:</em> Política de uso IA (con Subgerencia)</li>
                  <li><strong>2. Decidir</strong> (hoy: acta + Figma)<br><em>Negocio:</em> <span class="pill pill--risk">firma del acta</span> (puerta humana)<br><em>Líder de producto y UX:</em> <span class="pill pill--risk">aprueba spec y criterios</span> (puerta humana)<br><em>Arnés de agentes (LIA UNAL):</em> Arquitectura y UX (BMAD); spec formal<br><em>Líder técnico, BD y desarrollo:</em> Decisiones técnicas: líder técnico y BD</li>
                  <li><strong>3. Descomponer</strong> (hoy: no existe)<br><em>Líder de producto y UX:</em> Ajusta historias y prioridades<br><em>Arnés de agentes (LIA UNAL):</em> Épicas e historias; plan de olas /sprint<br><em>Líder técnico, BD y desarrollo:</em> Estiman esfuerzo por historia</li>
                  <li><strong>4. Traducir</strong> (hoy: no existe)<br><em>Arnés de agentes (LIA UNAL):</em> Puente OpenSpec: contrato por historia<br><em>Líder técnico, BD y desarrollo:</em> Revisan el contrato verificable</li>
                  <li><strong>5. Construir</strong> (hoy: desarrollo)<br><em>Arnés de agentes (LIA UNAL):</em> /sw:build: código y prueba por escenario<br><em>Líder técnico, BD y desarrollo:</em> <span class="pill pill--risk">revisión y merge</span> (puerta humana)<br><em>Infraestructura y seguridad:</em> Pipeline CI/CD Azure (objetivo)</li>
                  <li><strong>6. Cerrar</strong> (hoy: compilados)<br><em>Negocio:</em> Validación final en preproducción<br><em>Arnés de agentes (LIA UNAL):</em> /sw:close: valida, archiva y memoria<br><em>Infraestructura y seguridad:</em> <span class="pill pill--risk">despliegue en ambiente</span> (puerta humana)</li>
                </ul>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>Contexto del proyecto:</strong> reglas y negocio (architecture-base.md) · arquitectura (BMAD y graphify) · memoria persistente (Engram)</li>
                  <li><strong>Gobierno transversal:</strong> seguimiento con /sw:status · control de cambios con /sw:change · gestión de defectos con /sw:bug</li>
                  <li><strong>Roles institucionales:</strong> LIA UNAL propone y acompaña · Subgerencia de TIC valida caso de uso, accesos y modelos</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 4.1 — Flujo SDLC-IA por etapas: cada carril representa a quien interviene y cada columna, una fase; el flujo agéntico (arnés) produce los artefactos de cada etapa y el contexto del proyecto los alimenta. En rojo, las puertas humanas, que no se delegan</figcaption>
            </figure>
          </article>

          <!-- Slide E2-5: Fases y artefactos (Tabla 4.1) [c2-fases] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-fases">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Fases y artefactos: qué hace el flujo agéntico y qué decide la persona</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Cada etapa de ATENEA tiene un comando conectado al flujo; Descomponer y Traducir no existen hoy y dos filas atraviesan todo el ciclo.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.62rem,min(0.95vw,1.55vh),1.5rem);">
                  <caption>Tabla 4.1 — Intervención agéntica por etapa: brecha que atiende, función del flujo, decisión humana y resultado (texto condensado)</caption>
                  <thead>
                    <tr>
                      <th style="width:10%;font-size:0.82em;">Etapa actual</th>
                      <th style="width:9%;font-size:0.82em;">Fase</th>
                      <th style="width:12%;font-size:0.82em;">Brecha que atiende</th>
                      <th style="width:30%;font-size:0.82em;">Qué hace el flujo agéntico</th>
                      <th style="width:21%;font-size:0.82em;">Decisión humana</th>
                      <th style="font-size:0.82em;">Resultado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Etapa actual">Levantamiento con el cliente</td>
                      <td data-label="Fase"><strong>Entender</strong></td>
                      <td data-label="Brecha que atiende">Requerimiento extenso sin estructura</td>
                      <td data-label="Qué hace el flujo agéntico">Propone una especificación con requisitos numerados, supuestos marcados y preguntas de aclaración a partir de las notas y el diseño validado; en un sistema existente, acota el área de código</td>
                      <td data-label="Decisión humana">El líder de producto fija intención y alcance y resuelve las preguntas</td>
                      <td data-label="Resultado">Especificación de requisitos, para aprobación</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Especificación y validación de diseño</td>
                      <td data-label="Fase"><strong>Decidir</strong></td>
                      <td data-label="Brecha que atiende">Decisiones técnicas sin registro</td>
                      <td data-label="Qué hace el flujo agéntico">Redacta la arquitectura y la experiencia: servicios a reutilizar, modelo de datos, integraciones y restricciones; contrasta la arquitectura declarada con la real</td>
                      <td data-label="Decisión humana">El líder de producto aprueba la especificación y sus criterios; la líder técnica y base de datos aprueban las decisiones técnicas</td>
                      <td data-label="Resultado">Especificación aprobada y arquitectura vinculante, en el repositorio</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">No existe</td>
                      <td data-label="Fase"><strong>Descomponer</strong></td>
                      <td data-label="Brecha que atiende">Sin desglose ni criterios por unidad</td>
                      <td data-label="Qué hace el flujo agéntico">Propone épicas e historias que una persona puede terminar, con criterios de aceptación y los requisitos que cubren; calcula olas de trabajo paralelo según las dependencias</td>
                      <td data-label="Decisión humana">El líder de producto aprueba las historias; lo de bajo riesgo puede iniciarse con aprobación parcial explícita</td>
                      <td data-label="Resultado">Historias estimables y plan de olas; estimación por historia, no por requerimiento completo</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">No existe</td>
                      <td data-label="Fase"><strong>Traducir</strong></td>
                      <td data-label="Brecha que atiende">Estándar dependiente de cada persona</td>
                      <td data-label="Qué hace el flujo agéntico">Genera, de forma determinista, un contrato verificable por historia con las reglas del proyecto y registra la traza requisito, historia y contrato</td>
                      <td data-label="Decisión humana">El desarrollador revisa el contrato; si está mal, se corrige la historia y se regenera</td>
                      <td data-label="Resultado">Contratos verificables; los escenarios son los casos de prueba</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Desarrollo</td>
                      <td data-label="Fase"><strong>Construir</strong></td>
                      <td data-label="Brecha que atiende">Código heterogéneo; calidad validada al final</td>
                      <td data-label="Qué hace el flujo agéntico">Carga reglas, arquitectura, memoria y grafo del código y construye una historia a la vez: código y una prueba por escenario; lo que sale de la historia pasa por control de cambios</td>
                      <td data-label="Decisión humana">El desarrollador revisa y ajusta; la líder técnica aprueba la integración a ramas protegidas</td>
                      <td data-label="Resultado">Rama con código y pruebas verificadas antes de integrar</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Compilados a infraestructura</td>
                      <td data-label="Fase"><strong>Cerrar</strong></td>
                      <td data-label="Brecha que atiende">Sin traza ni línea base</td>
                      <td data-label="Qué hace el flujo agéntico">Valida el contrato en modo estricto, lo archiva como línea base y actualiza la memoria del proyecto y el tablero</td>
                      <td data-label="Decisión humana">Infraestructura despliega en cada ambiente; negocio valida en preproducción</td>
                      <td data-label="Resultado">Traza especificación, código y pruebas; línea base para medir cambios</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Transversal · hoy: no existe</td>
                      <td data-label="Fase"><strong>Seguimiento</strong></td>
                      <td data-label="Brecha que atiende">Plazos sin sustento</td>
                      <td data-label="Qué hace el flujo agéntico">Interpreta el tablero: requisitos, historias, contratos, tareas y esfuerzo por etapa; enruta incidencias</td>
                      <td data-label="Decisión humana">Prioridades y compromisos del líder de producto y la dirección</td>
                      <td data-label="Resultado">Avance real por historia</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Transversal</td>
                      <td data-label="Fase"><strong>Incidentes y cambios</strong></td>
                      <td data-label="Brecha que atiende">Cambios tardíos absorbidos por desarrollo</td>
                      <td data-label="Qué hace el flujo agéntico">Clasifica el alcance de un cambio antes de tocar archivos y regenera solo lo afectado; corrige defectos sin abrir el alcance</td>
                      <td data-label="Decisión humana">El líder de producto decide si el cambio cabe en lo acordado, lo amplía o abre otra épica</td>
                      <td data-label="Resultado">Decisión registrada; regeneración acotada</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide E2-6: Organización del equipo (§4.3) [c2-organizacion] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-organizacion" data-caption-source="§4.3" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Organización del equipo: una célula por caso de uso, sin perfiles nuevos</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El método reparte responsabilidades entre los roles que ATENEA ya tiene; ATENEA debe definir la dedicación de cada rol al designar su equipo (obligación 5 de la Agencia).</p>
              </div>
              <svg viewBox="0 0 1200 500" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Célula de trabajo por caso de uso, tres responsabilidades que se formalizan y regla de trabajo entre la Universidad y ATENEA">
              <defs>
              <marker id="org-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
              </defs>
              <rect x="0" y="0" width="570" height="262" rx="10" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.5" stroke-dasharray="6,4" />
              <text x="16" y="28" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700">Célula por caso de uso</text>
              <rect x="16" y="48" width="258" height="80" rx="8" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="145" y="95" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">Líder de producto</text>
              <rect x="288" y="48" width="258" height="80" rx="8" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="417" y="95" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">Diseñadora</text>
              <rect x="16" y="144" width="258" height="80" rx="8" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="145" y="191" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">Desarrollador de front-end</text>
              <rect x="288" y="144" width="258" height="80" rx="8" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="417" y="191" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">Desarrollador de back-end</text>
              <path d="M285 262 L285 306" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#org-b)" />
              <rect x="0" y="310" width="570" height="62" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.4" />
              <text x="16" y="336" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Revisión de la líder del equipo</text>
              <text x="16" y="360" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">y despliegue de infraestructura</text>
              <text x="556" y="336" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="end">Conformación actual</text>
              <text x="556" y="358" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="end">por módulo</text>
              <text x="610" y="22" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Tres responsabilidades que hoy recaen en las personas sin estar escritas</text>
              <rect x="610" y="36" width="590" height="102" rx="8" fill="#F8FAFC" stroke="#B7CC85" stroke-width="1.4" />
              <rect x="610" y="36" width="8" height="102" rx="3" fill="#B7CC85" stroke="#B7CC85" stroke-width="0" />
              <text x="632" y="64" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">1. Custodia de la arquitectura base</text>
              <text x="632" y="88" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">La líder del equipo y la persona de base de datos mantienen el</text>
              <text x="632" y="107" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">documento de arquitectura base y las reglas que aplican los agentes</text>
              <text x="632" y="126" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">(respuesta a F-04).</text>
              <rect x="610" y="148" width="590" height="102" rx="8" fill="#F8FAFC" stroke="#B7CC85" stroke-width="1.4" />
              <rect x="610" y="148" width="8" height="102" rx="3" fill="#B7CC85" stroke="#B7CC85" stroke-width="0" />
              <text x="632" y="176" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">2. Referente del arnés</text>
              <text x="632" y="200" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">Un desarrollador por equipo instala y actualiza el arnés, atiende sus</text>
              <text x="632" y="219" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">diagnósticos y es el punto de contacto con la Universidad.</text>
              <rect x="610" y="260" width="590" height="102" rx="8" fill="#F8FAFC" stroke="#B7CC85" stroke-width="1.4" />
              <rect x="610" y="260" width="8" height="102" rx="3" fill="#B7CC85" stroke="#B7CC85" stroke-width="0" />
              <text x="632" y="288" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">3. Aprobación de historias</text>
              <text x="632" y="312" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">El líder de producto aprueba las historias y sus criterios antes de</text>
              <text x="632" y="331" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">traducirlas a contratos; la firma del acta deja de llegar después de</text>
              <text x="632" y="350" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">iniciada la construcción (RT-06).</text>
              <rect x="0" y="392" width="1200" height="100" rx="8" fill="#EDF1F7" stroke="#2C6B87" stroke-width="1.3" />
              <text x="18" y="420" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Regla de trabajo acordada el 14 de octubre</text>
              <text x="18" y="446" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">La Universidad propone la metodología y las herramientas y ATENEA valida. Durante el contrato la Universidad opera el arnés junto al</text>
              <text x="18" y="466" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">equipo; al cierre, la operación queda en ATENEA (componente C8).</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Célula por caso de uso y responsabilidades</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>Célula por caso de uso:</strong> líder de producto, diseñadora, desarrollador de front-end y desarrollador de back-end, con la revisión de la líder del equipo y el despliegue de infraestructura (conformación actual por módulo).</li>
                  <li><strong>Custodia de la arquitectura base:</strong> La líder del equipo y la persona de base de datos mantienen el documento de arquitectura base y las reglas que aplican los agentes (respuesta a F-04).</li>
                  <li><strong>Referente del arnés:</strong> Un desarrollador por equipo instala y actualiza el arnés, atiende sus diagnósticos y es el punto de contacto con la Universidad.</li>
                  <li><strong>Aprobación de historias:</strong> El líder de producto aprueba las historias y sus criterios antes de traducirlas a contratos; la firma del acta deja de llegar después de iniciada la construcción (RT-06).</li>
                  <li><strong>Regla de trabajo (14 de octubre):</strong> la Universidad propone la metodología y las herramientas y ATENEA valida. Durante el contrato la Universidad opera el arnés junto al equipo; al cierre, la operación queda en ATENEA (componente C8).</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Fuente: §4.3 — Célula de trabajo por caso de uso y tres responsabilidades que se formalizan (sin figura ni tabla numerada en el informe)</figcaption>
            </figure>
          </article>

          <!-- Slide E2-7: Roles RACI (Tabla 4.2) [c2-roles] -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e2" data-item="c2-roles">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Roles y responsabilidades por fase: matriz RACI</h2>
              <ul class="slide-list">
                <li>
                  <strong>R ejecuta, A aprueba y responde, C es consultado, I es informado.</strong> Cada actividad tiene una sola A.
                </li>
                <li>
                  <strong>Roles:</strong> PO líder de producto; UX diseño; LT líder del equipo; BD base de datos; Dev desarrolladores; Inf infraestructura; Seg seguridad; TIC Subgerencia de TIC; UN Universidad durante el contrato.
                </li>
                <li>
                  <strong>La Universidad participa</strong> en la operación del arnés y su transferencia, y en el apoyo a cada fase.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper is-scroll-x">
                <table class="data-table is-scroll-x" style="font-size:clamp(0.72rem,min(1.12vw,2.1vh),1.5rem);">
                  <caption>Tabla 4.2 — Matriz RACI del SDLC-IA: R ejecuta; A aprueba y responde por el resultado; C es consultado; I es informado</caption>
                  <thead>
                    <tr>
                      <th style="width:25%;font-size:0.82em;">Fase o actividad</th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Líder de producto">PO</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Diseño">UX</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Líder del equipo">LT</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Base de datos">BD</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Desarrolladores">Dev</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Infraestructura">Inf</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Seguridad">Seg</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Subgerencia de TIC">TIC</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Universidad durante el contrato">UN</abbr></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Entender: especificación de requisitos</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#B8DCC4;color:#14401F;font-weight:700;">A/R</span></td>
                      <td data-label="UX"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="Inf"></td>
                      <td data-label="Seg"></td>
                      <td data-label="TIC"></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Decidir: diseño de la experiencia</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="UX"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="Inf"></td>
                      <td data-label="Seg"></td>
                      <td data-label="TIC"></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Decidir: arquitectura y decisiones técnicas</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="UX"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#B8DCC4;color:#14401F;font-weight:700;">A/R</span></td>
                      <td data-label="BD"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="Inf"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="Seg"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="TIC"></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Descomponer: épicas, historias y estimación</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="UX"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="Inf"></td>
                      <td data-label="Seg"></td>
                      <td data-label="TIC"></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Traducir: contratos verificables</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="UX"></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="Inf"></td>
                      <td data-label="Seg"></td>
                      <td data-label="TIC"></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Construir: código y pruebas por escenario</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="UX"></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="BD"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="Inf"></td>
                      <td data-label="Seg"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="TIC"></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Cerrar: validación en preproducción</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="UX"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="Inf"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="Seg"></td>
                      <td data-label="TIC"></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Cerrar: despliegue a producción</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="UX"></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="Inf"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="Seg"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="TIC"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Control de cambios y defectos</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="UX"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="Inf"></td>
                      <td data-label="Seg"></td>
                      <td data-label="TIC"></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Política de uso de IA y accesos</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="UX"></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="Inf"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                      <td data-label="Seg"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="TIC"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#FBF0D2;color:#7A4E00;">C</span></td>
                    </tr>
                    <tr>
                      <td data-label="Fase o actividad"><strong>Operación del arnés y transferencia</strong></td>
                      <td data-label="PO"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="UX"></td>
                      <td data-label="LT"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D6EBDD;color:#1E5631;font-weight:700;">A</span></td>
                      <td data-label="BD"></td>
                      <td data-label="Dev"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                      <td data-label="Inf"></td>
                      <td data-label="Seg"></td>
                      <td data-label="TIC"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#EEF1F5;color:#4A5468;">I</span></td>
                      <td data-label="UN"><span style="display:block;border-radius:6px;padding:2px 0;text-align:center;background:#D4E6F2;color:#1F536C;font-weight:700;">R</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide E2-8: Puntos de control humano (§4.4) [c2-control-humano] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-control-humano" data-caption-source="§4.4" data-tone="rose">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Puntos de control humano: siete decisiones que no se delegan</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">En el flujo, el agente propone y la persona decide: seis puertas por fase y una para los cambios tardíos.</p>
              </div>
              <svg viewBox="0 0 1200 596" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Siete puntos de control humano: uno por cada una de las seis fases y uno para los cambios tardíos">
              <path d="M0.0 0 H178.0 L192.0 24 L178.0 48 H0.0 L14.0 24 Z" fill="#7FB4CA" />
              <text x="100.0" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Entender</text>
              <path d="M96.0 48 V74" stroke="#B71C1C" stroke-width="2" />
              <circle cx="96.0" cy="88" r="16" fill="#B71C1C" />
              <text x="96.0" y="94" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">1</text>
              <rect x="0.0" y="112" width="192" height="276" rx="8" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.4" />
              <text x="10.0" y="138" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">DECIDE</text>
              <text x="10.0" y="160" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Líder de producto</text>
              <text x="10.0" y="189" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">Fija la intención y</text>
              <text x="10.0" y="209" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">el alcance, resuelve</text>
              <text x="10.0" y="229" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">las preguntas de</text>
              <text x="10.0" y="249" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">aclaración y aprueba</text>
              <text x="10.0" y="269" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">la especificación.</text>
              <path d="M201.6 0 H379.6 L393.6 24 L379.6 48 H201.6 L215.6 24 Z" fill="#7AA89F" />
              <text x="301.6" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Decidir</text>
              <path d="M297.6 48 V74" stroke="#B71C1C" stroke-width="2" />
              <circle cx="297.6" cy="88" r="16" fill="#B71C1C" />
              <text x="297.6" y="94" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">2</text>
              <rect x="201.6" y="112" width="192" height="276" rx="8" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.4" />
              <text x="211.6" y="138" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">DECIDE</text>
              <text x="211.6" y="160" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Líder técnica y</text>
              <text x="211.6" y="181" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">base de datos</text>
              <text x="211.6" y="210" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">Aprueban las</text>
              <text x="211.6" y="230" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">decisiones técnicas</text>
              <text x="211.6" y="250" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">que quedan como</text>
              <text x="211.6" y="270" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">arquitectura</text>
              <text x="211.6" y="290" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">vinculante.</text>
              <path d="M403.2 0 H581.2 L595.2 24 L581.2 48 H403.2 L417.2 24 Z" fill="#B7CC85" />
              <text x="503.2" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Descomponer</text>
              <path d="M499.2 48 V74" stroke="#B71C1C" stroke-width="2" />
              <circle cx="499.2" cy="88" r="16" fill="#B71C1C" />
              <text x="499.2" y="94" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">3</text>
              <rect x="403.2" y="112" width="192" height="276" rx="8" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.4" />
              <text x="413.2" y="138" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">DECIDE</text>
              <text x="413.2" y="160" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Líder de producto</text>
              <text x="413.2" y="189" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">Aprueba las historias</text>
              <text x="413.2" y="209" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">y sus criterios de</text>
              <text x="413.2" y="229" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">aceptación antes de</text>
              <text x="413.2" y="249" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">que se traduzcan a</text>
              <text x="413.2" y="269" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">contratos.</text>
              <path d="M604.8 0 H782.8 L796.8 24 L782.8 48 H604.8 L618.8 24 Z" fill="#DFBD76" />
              <text x="704.8" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Traducir</text>
              <path d="M700.8 48 V74" stroke="#B71C1C" stroke-width="2" />
              <circle cx="700.8" cy="88" r="16" fill="#B71C1C" />
              <text x="700.8" y="94" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">4</text>
              <rect x="604.8" y="112" width="192" height="276" rx="8" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.4" />
              <text x="614.8" y="138" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">DECIDE</text>
              <text x="614.8" y="160" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Desarrollador</text>
              <text x="614.8" y="189" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">Revisa el contrato;</text>
              <text x="614.8" y="209" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">si está mal, se</text>
              <text x="614.8" y="229" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">corrige la historia y</text>
              <text x="614.8" y="249" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">se regenera.</text>
              <path d="M806.4 0 H984.4 L998.4 24 L984.4 48 H806.4 L820.4 24 Z" fill="#7AA89F" />
              <text x="906.4" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Construir</text>
              <path d="M902.4 48 V74" stroke="#B71C1C" stroke-width="2" />
              <circle cx="902.4" cy="88" r="16" fill="#B71C1C" />
              <text x="902.4" y="94" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">5</text>
              <rect x="806.4" y="112" width="192" height="276" rx="8" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.4" />
              <text x="816.4" y="138" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">DECIDE</text>
              <text x="816.4" y="160" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Desarrollador y</text>
              <text x="816.4" y="181" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">líder técnica</text>
              <text x="816.4" y="210" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">El desarrollador</text>
              <text x="816.4" y="230" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">revisa y ajusta; la</text>
              <text x="816.4" y="250" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">líder técnica aprueba</text>
              <text x="816.4" y="270" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">la integración a las</text>
              <text x="816.4" y="290" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">ramas protegidas.</text>
              <path d="M1008.0 0 H1186.0 L1200.0 24 L1186.0 48 H1008.0 L1022.0 24 Z" fill="#2C6B87" />
              <text x="1108.0" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="18" font-weight="700" text-anchor="middle">Cerrar</text>
              <path d="M1104.0 48 V74" stroke="#B71C1C" stroke-width="2" />
              <circle cx="1104.0" cy="88" r="16" fill="#B71C1C" />
              <text x="1104.0" y="94" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">6</text>
              <rect x="1008.0" y="112" width="192" height="276" rx="8" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.4" />
              <text x="1018.0" y="138" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">DECIDE</text>
              <text x="1018.0" y="160" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Infraestructura y</text>
              <text x="1018.0" y="181" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">negocio</text>
              <text x="1018.0" y="210" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">Infraestructura</text>
              <text x="1018.0" y="230" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">despliega en cada</text>
              <text x="1018.0" y="250" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">ambiente y negocio</text>
              <text x="1018.0" y="270" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">valida en</text>
              <text x="1018.0" y="290" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">preproducción; la</text>
              <text x="1018.0" y="310" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">aprobación para</text>
              <text x="1018.0" y="330" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">preproducción y</text>
              <text x="1018.0" y="350" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">producción sigue</text>
              <text x="1018.0" y="370" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15.5">siendo humana.</text>
              <path d="M0 408 H1200" stroke="#D6DEE8" stroke-width="1" />
              <rect x="0" y="422" width="1200" height="98" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.4" />
              <circle cx="38" cy="464" r="16" fill="#B71C1C" />
              <text x="38" y="470" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">7</text>
              <text x="70" y="452" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Cambios tardíos: transversal a todo el ciclo</text>
              <text x="70" y="476" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Decide: Líder de producto. Decide si el cambio cabe en lo acordado, lo amplía o abre otra épica.</text>
              <text x="70" y="498" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">Un defecto no pasa por esta clasificación, porque lo acordado no cambió.</text>
              <text x="0" y="544" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">El agente propone y la persona decide: ninguna de estas siete decisiones se delega.</text>
              <text x="0" y="566" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">Cómo el sistema de agentes hace cumplir estas puertas se describe en el capítulo 6 (E4).</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Siete puntos de control humano</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>1. Entender:</strong> <span class="pill pill--risk">Líder de producto</span> Fija la intención y el alcance, resuelve las preguntas de aclaración y aprueba la especificación.</li>
                  <li><strong>2. Decidir:</strong> <span class="pill pill--risk">Líder técnica y base de datos</span> Aprueban las decisiones técnicas que quedan como arquitectura vinculante.</li>
                  <li><strong>3. Descomponer:</strong> <span class="pill pill--risk">Líder de producto</span> Aprueba las historias y sus criterios de aceptación antes de que se traduzcan a contratos.</li>
                  <li><strong>4. Traducir:</strong> <span class="pill pill--risk">Desarrollador</span> Revisa el contrato; si está mal, se corrige la historia y se regenera.</li>
                  <li><strong>5. Construir:</strong> <span class="pill pill--risk">Desarrollador y líder técnica</span> El desarrollador revisa y ajusta; la líder técnica aprueba la integración a las ramas protegidas.</li>
                  <li><strong>6. Cerrar:</strong> <span class="pill pill--risk">Infraestructura y negocio</span> Infraestructura despliega en cada ambiente y negocio valida en preproducción; la aprobación para preproducción y producción sigue siendo humana.</li>
                  <li><strong>7. Cambios tardíos:</strong> <span class="pill pill--risk">Líder de producto</span> Decide si el cambio cabe en lo acordado, lo amplía o abre otra épica.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Fuente: §4.4 — Siete puntos de control humano: una puerta por fase y una para los cambios tardíos, sin cambiar a quién corresponde cada una (sin tabla numerada en el informe)</figcaption>
            </figure>
          </article>

          <!-- Slide E2-9: Contexto del proyecto (Tabla 4.3) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-contexto" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Contexto del proyecto: tres piezas que alimentan el flujo</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El contexto vive en el repositorio y entra en las fases en las que las reglas, la arquitectura o la memoria cambian lo que el agente propone.</p>
              </div>
              <svg viewBox="0 0 1200 470" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tabla 4.3 como tres tarjetas: reglas y negocio, arquitectura y memoria, con su contenido, fases y dónde viven">
              <rect x="0" y="0" width="388" height="466" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.6" />
              <rect x="0" y="0" width="388" height="46" rx="10" fill="#7FB4CA" stroke="#7FB4CA" stroke-width="0" />
              <text x="16" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700">Reglas y negocio</text>
              <text x="16" y="74" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">CONTENIDO Y ORIGEN</text>
              <text x="16" y="98" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">Reglas de cada sistema, glosario,</text>
              <text x="16" y="120" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">normativa, convenciones y versiones del</text>
              <text x="16" y="142" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">stack (Angular 13, Java 17, WildFly 34);</text>
              <text x="16" y="164" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">salen de la documentación de</text>
              <text x="16" y="186" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">requerimientos existente y de</text>
              <text x="16" y="208" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">entrevistas con el equipo.</text>
              <text x="16" y="240" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">FASES DONDE ENTRA</text>
              <rect x="16" y="252" width="92" height="28" rx="14" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="62.0" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">Entender</text>
              <rect x="116" y="252" width="83" height="28" rx="14" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="157.5" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">Decidir</text>
              <rect x="207" y="252" width="101" height="28" rx="14" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="1.4" />
              <text x="257.5" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">Construir</text>
              <text x="16" y="310" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">DÓNDE VIVE</text>
              <text x="16" y="334" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">Documento de arquitectura base del</text>
              <text x="16" y="356" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">repositorio, que manda sobre los valores</text>
              <text x="16" y="378" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">por defecto del agente.</text>
              <rect x="406" y="0" width="388" height="466" rx="8" fill="#F8FAFC" stroke="#7AA89F" stroke-width="1.6" />
              <rect x="406" y="0" width="388" height="46" rx="10" fill="#7AA89F" stroke="#7AA89F" stroke-width="0" />
              <text x="422" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700">Arquitectura</text>
              <text x="422" y="74" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">CONTENIDO Y ORIGEN</text>
              <text x="422" y="98" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">Módulos, integraciones, modelo de datos</text>
              <text x="422" y="120" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">de Oracle y decisiones registradas;</text>
              <text x="422" y="142" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">ingeniería inversa asistida y validada</text>
              <text x="422" y="164" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">por el equipo.</text>
              <text x="422" y="240" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">FASES DONDE ENTRA</text>
              <rect x="422" y="252" width="83" height="28" rx="14" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.4" />
              <text x="463.5" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">Decidir</text>
              <rect x="513" y="252" width="101" height="28" rx="14" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.4" />
              <text x="563.5" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">Construir</text>
              <rect x="622" y="252" width="83" height="28" rx="14" fill="#FFFFFF" stroke="#7AA89F" stroke-width="1.4" />
              <text x="663.5" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">cambios</text>
              <text x="422" y="310" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">DÓNDE VIVE</text>
              <text x="422" y="334" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">Arquitectura del proyecto y grafo del</text>
              <text x="422" y="356" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">código, solo de código.</text>
              <rect x="812" y="0" width="388" height="466" rx="8" fill="#F8FAFC" stroke="#DFBD76" stroke-width="1.6" />
              <rect x="812" y="0" width="388" height="46" rx="10" fill="#DFBD76" stroke="#DFBD76" stroke-width="0" />
              <text x="828" y="31" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700">Memoria</text>
              <text x="828" y="74" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">CONTENIDO Y ORIGEN</text>
              <text x="828" y="98" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">Qué se hizo, por qué, qué falló y qué</text>
              <text x="828" y="120" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">falta; la genera el flujo desde el</text>
              <text x="828" y="142" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">primer caso de uso.</text>
              <text x="828" y="240" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">FASES DONDE ENTRA</text>
              <rect x="828" y="252" width="101" height="28" rx="14" fill="#FFFFFF" stroke="#DFBD76" stroke-width="1.4" />
              <text x="878.5" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">Construir</text>
              <rect x="937" y="252" width="74" height="28" rx="14" fill="#FFFFFF" stroke="#DFBD76" stroke-width="1.4" />
              <text x="974.0" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">Cerrar</text>
              <rect x="1019" y="252" width="83" height="28" rx="14" fill="#FFFFFF" stroke="#DFBD76" stroke-width="1.4" />
              <text x="1060.5" y="272" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="600" text-anchor="middle">cambios</text>
              <text x="828" y="310" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" letter-spacing="1">DÓNDE VIVE</text>
              <text x="828" y="334" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">Memoria por proyecto dentro del</text>
              <text x="828" y="356" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">repositorio.</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Tres piezas de contexto</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>Reglas y negocio.</strong> Reglas de cada sistema, glosario, normativa, convenciones y versiones del stack (Angular 13, Java 17, WildFly 34); salen de la documentación de requerimientos existente y de entrevistas con el equipo. <em>Fases:</em> Entender, Decidir, Construir. <em>Dónde vive:</em> Documento de arquitectura base del repositorio, que manda sobre los valores por defecto del agente.</li>
                  <li><strong>Arquitectura.</strong> Módulos, integraciones, modelo de datos de Oracle y decisiones registradas; ingeniería inversa asistida y validada por el equipo. <em>Fases:</em> Decidir, Construir, cambios. <em>Dónde vive:</em> Arquitectura del proyecto y grafo del código, solo de código.</li>
                  <li><strong>Memoria.</strong> Qué se hizo, por qué, qué falló y qué falta; la genera el flujo desde el primer caso de uso. <em>Fases:</em> Construir, Cerrar, cambios. <em>Dónde vive:</em> Memoria por proyecto dentro del repositorio.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Tabla 4.3 — Piezas de contexto, contenido, fases donde entran y dónde viven</figcaption>
            </figure>
          </article>

          <!-- Slide E2-10: Verificación y CI/CD (§4.6) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-cicd" data-caption-source="§4.6" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Verificación, integración y despliegue: de la validación de contratos a la entrega continua</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">La revisión humana sigue siendo la aprobación: en la etapa B al integrar y en la etapa C para preproducción y producción.</p>
              </div>
              <svg viewBox="0 0 1200 430" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tres etapas de verificación, integración y despliegue: A con el proceso actual, B integración continua y C entrega continua">
              <defs>
              <marker id="ci-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
              </defs>
              <rect x="0" y="0" width="372" height="292" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.6" />
              <rect x="16" y="16" width="52" height="52" rx="9" fill="#7FB4CA" stroke="#7FB4CA" stroke-width="0" />
              <text x="42" y="53" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="28" font-weight="700" text-anchor="middle">A</text>
              <text x="82" y="36" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">Etapa A</text>
              <text x="82" y="60" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Con el proceso actual</text>
              <text x="16" y="100" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">Validación de contratos y pruebas</text>
              <text x="16" y="125" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">de la historia en el entorno de</text>
              <text x="16" y="150" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">desarrollo antes de pedir la</text>
              <text x="16" y="175" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">integración; el despliegue sigue</text>
              <text x="16" y="200" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">siendo manual.</text>
              <path d="M374 146 L410 146" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ci-b)" />
              <rect x="414" y="0" width="372" height="292" rx="8" fill="#F8FAFC" stroke="#7AA89F" stroke-width="1.6" />
              <rect x="430" y="16" width="52" height="52" rx="9" fill="#7AA89F" stroke="#7AA89F" stroke-width="0" />
              <text x="456" y="53" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="28" font-weight="700" text-anchor="middle">B</text>
              <text x="496" y="36" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">Etapa B</text>
              <text x="496" y="60" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Integración continua</text>
              <text x="430" y="100" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">Con el código en Azure Repos, cada</text>
              <text x="430" y="125" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">solicitud de integración compila</text>
              <text x="430" y="150" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">front-end y back-end, ejecuta</text>
              <text x="430" y="175" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">pruebas y revisa dependencias en</text>
              <text x="430" y="200" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">Azure Pipelines; la revisión humana</text>
              <text x="430" y="225" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">sigue siendo la aprobación.</text>
              <path d="M788 146 L824 146" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ci-b)" />
              <rect x="828" y="0" width="372" height="292" rx="8" fill="#F8FAFC" stroke="#DFBD76" stroke-width="1.6" />
              <rect x="844" y="16" width="52" height="52" rx="9" fill="#DFBD76" stroke="#DFBD76" stroke-width="0" />
              <text x="870" y="53" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="28" font-weight="700" text-anchor="middle">C</text>
              <text x="910" y="36" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">Etapa C</text>
              <text x="910" y="60" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Entrega continua</text>
              <text x="844" y="100" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">Empaquetado reproducible,</text>
              <text x="844" y="125" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">despliegue automático a QA y</text>
              <text x="844" y="150" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">aprobación humana para</text>
              <text x="844" y="175" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="18.5">preproducción y producción.</text>
              <rect x="0" y="312" width="1200" height="104" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.4" />
              <text x="16" y="338" fill="#7A4E00" font-family="Space Grotesk,sans-serif" font-size="17">Punto de partida: hoy no hay pipeline y la primera fase de la migración no refactoriza aplicaciones. La etapa C depende de la</text>
              <text x="16" y="361" fill="#7A4E00" font-family="Space Grotesk,sans-serif" font-size="17">segunda fase de la migración (contenedores, registro de imágenes y versionado), sobre la cual aún no hay decisión.</text>
              <text x="16" y="394" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">El alcance de las etapas B y C dentro del contrato se acuerda con infraestructura.</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Tres etapas de CI/CD</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>Etapa A, con el proceso actual:</strong> Validación de contratos y pruebas de la historia en el entorno de desarrollo antes de pedir la integración; el despliegue sigue siendo manual.</li>
                  <li><strong>Etapa B, integración continua:</strong> Con el código en Azure Repos, cada solicitud de integración compila front-end y back-end, ejecuta pruebas y revisa dependencias en Azure Pipelines; la revisión humana sigue siendo la aprobación.</li>
                  <li><strong>Etapa C, entrega continua:</strong> Empaquetado reproducible, despliegue automático a QA y aprobación humana para preproducción y producción.</li>
                  <li><strong>Punto de partida:</strong> hoy no hay pipeline y la primera fase de la migración no refactoriza aplicaciones.</li>
                  <li><strong>Dependencia:</strong> la etapa C depende de la segunda fase de la migración (contenedores, registro de imágenes y versionado), sobre la cual aún no hay decisión.</li>
                  <li><strong>Por acordar:</strong> el alcance de las etapas B y C dentro del contrato se acuerda con infraestructura.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Fuente: §4.6 — Verificación, integración y despliegue en tres etapas (sin tabla ni figura numerada en el informe)</figcaption>
            </figure>
          </article>

          <!-- Slide E2-11: Criterios de calidad (Tabla 4.4, 1/2) [c2-criterios] -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e2" data-item="c2-criterios">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Criterios de calidad: definición de terminado de una historia (1/2)</h2>
              <ul class="slide-list">
                <li>
                  <strong>La calidad se verifica por historia, no al final:</strong> una historia está terminada solo si cumple los diez criterios.
                </li>
                <li>
                  <strong>Los umbrales son una propuesta de la Universidad</strong> que ATENEA debe validar.
                </li>
                <li>
                  <strong>Cinco criterios de calidad:</strong> contrato válido, una prueba por escenario, sin cambios fuera del contrato, traza completa y aprobación de la líder del equipo.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.4vw,2.6vh),1.5rem);">
                  <caption>Tabla 4.4 — Definición de terminado de una historia (1/2): criterios de calidad, umbral propuesto, evidencia y quién los verifica</caption>
                  <thead>
                    <tr>
                      <th style="width:6%;font-size:0.82em;">N.º</th>
                      <th style="width:37%;font-size:0.82em;">Criterio</th>
                      <th style="width:18%;font-size:0.82em;">Umbral propuesto</th>
                      <th style="width:20%;font-size:0.82em;">Evidencia</th>
                      <th style="font-size:0.82em;">Verifica</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td colspan="5" data-label="Grupo" style="background:#EAF3F8;color:#1F536C;font-weight:700;letter-spacing:0.04em;text-transform:uppercase;">Calidad</td></tr>
                    <tr>
                      <td data-label="N.º"><strong>1</strong></td>
                      <td data-label="Criterio">El contrato de la historia es válido en modo estricto</td>
                      <td data-label="Umbral propuesto">0 errores</td>
                      <td data-label="Evidencia">Salida de la validación</td>
                      <td data-label="Verifica">Desarrollador</td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>2</strong></td>
                      <td data-label="Criterio">Cada escenario <em>Given/When/Then</em> tiene una prueba automatizada que pasa</td>
                      <td data-label="Umbral propuesto">100 % de los escenarios</td>
                      <td data-label="Evidencia">Reporte de pruebas</td>
                      <td data-label="Verifica">Desarrollador</td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>3</strong></td>
                      <td data-label="Criterio">No hay cambios fuera del contrato; lo que aparece pasa por control de cambios</td>
                      <td data-label="Umbral propuesto">0 archivos fuera de lo autorizado</td>
                      <td data-label="Evidencia">Diferencias de la rama y decisión registrada</td>
                      <td data-label="Verifica">Líder del equipo</td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>4</strong></td>
                      <td data-label="Criterio">La traza requisito, historia, contrato, código y prueba está completa</td>
                      <td data-label="Umbral propuesto">100 % de los requisitos de la historia</td>
                      <td data-label="Evidencia">Archivo de traza del repositorio</td>
                      <td data-label="Verifica">Arnés</td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>5</strong></td>
                      <td data-label="Criterio">La líder del equipo aprueba la integración a la rama protegida</td>
                      <td data-label="Umbral propuesto">1 aprobación registrada</td>
                      <td data-label="Evidencia">Solicitud de integración</td>
                      <td data-label="Verifica">Líder del equipo</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide E2-12: Criterios de seguridad y aceptación (Tabla 4.4, 2/2) [c2-criterios] -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e2" data-item="c2-criterios">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Criterios de seguridad y de aceptación: definición de terminado (2/2)</h2>
              <ul class="slide-list">
                <li>
                  <strong>Marco de seguridad:</strong> el flujo opera dentro de la Política de Seguridad y Privacidad y el Manual de Políticas de Seguridad de la Agencia, y no envía a ningún modelo información confidencial ni datos personales (cláusulas décima y décima primera).
                </li>
                <li>
                  <strong>Accesos y modelos:</strong> las autorizaciones de acceso y la habilitación de modelos y servicios las gestiona la Agencia (obligaciones 7 y 8).
                </li>
                <li>
                  <strong>Sin respuesta aún:</strong> las preguntas sobre análisis de vulnerabilidades del código y de las dependencias.
                </li>
                <li>
                  <strong>Sin restricciones específicas hoy</strong> para herramientas de IA: riesgo extremo RT-01; la Subgerencia de TIC debe adoptar la política.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.4vw,2.6vh),1.5rem);">
                  <caption>Tabla 4.4 — Definición de terminado de una historia (2/2): criterios de seguridad y de aceptación</caption>
                  <thead>
                    <tr>
                      <th style="width:6%;font-size:0.82em;">N.º</th>
                      <th style="width:37%;font-size:0.82em;">Criterio</th>
                      <th style="width:18%;font-size:0.82em;">Umbral propuesto</th>
                      <th style="width:20%;font-size:0.82em;">Evidencia</th>
                      <th style="font-size:0.82em;">Verifica</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td colspan="5" data-label="Grupo" style="background:#FFF2F2;color:#8E1B1B;font-weight:700;letter-spacing:0.04em;text-transform:uppercase;">Seguridad</td></tr>
                    <tr>
                      <td data-label="N.º"><strong>6</strong></td>
                      <td data-label="Criterio">La revisión de riesgo no deja hallazgos bloqueantes</td>
                      <td data-label="Umbral propuesto">0 bloqueantes</td>
                      <td data-label="Evidencia">Dictamen de revisión</td>
                      <td data-label="Verifica">Líder del equipo y seguridad</td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>7</strong></td>
                      <td data-label="Criterio">Las dependencias no tienen vulnerabilidades críticas ni altas conocidas</td>
                      <td data-label="Umbral propuesto">0 críticas y 0 altas</td>
                      <td data-label="Evidencia">Análisis de dependencias (etapa B)</td>
                      <td data-label="Verifica">Seguridad</td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>8</strong></td>
                      <td data-label="Criterio">No hay secretos ni credenciales en el código ni en el contexto enviado al modelo</td>
                      <td data-label="Umbral propuesto">0</td>
                      <td data-label="Evidencia">Revisión de la rama</td>
                      <td data-label="Verifica">Seguridad</td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>9</strong></td>
                      <td data-label="Criterio">Las pruebas y el contexto del modelo usan datos sintéticos, nunca datos personales reales</td>
                      <td data-label="Umbral propuesto">0 registros reales</td>
                      <td data-label="Evidencia">Revisión de datos de prueba</td>
                      <td data-label="Verifica">Líder del equipo</td>
                    </tr>
                    <tr><td colspan="5" data-label="Grupo" style="background:#EBF5ED;color:#1E5631;font-weight:700;letter-spacing:0.04em;text-transform:uppercase;">Aceptación</td></tr>
                    <tr>
                      <td data-label="N.º"><strong>10</strong></td>
                      <td data-label="Criterio">Negocio valida en preproducción y el acta queda firmada en el formato institucional, que hoy lleva seis firmas</td>
                      <td data-label="Umbral propuesto">Antes de producción</td>
                      <td data-label="Evidencia">Acta firmada</td>
                      <td data-label="Verifica">Líder de producto</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide E2-13: Brechas que cierra la metodología (Figura 4.2) [c2-brechas-cierra] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-brechas-cierra" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Del diagnóstico al cierre de brechas: cuatro conclusiones, cuatro resultados comprobables</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">De cada cierre resulta algo que se puede comprobar: historias con traza, código con una sola base, decisiones que siguen en las personas y documentación al día.</p>
              </div>
              <svg viewBox="0 0 1200 536" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figura 4.2: cuatro brechas del diagnóstico, las fases de la metodología que las cierran y el resultado de cada cierre">
              <defs>
              <marker id="br-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
              </defs>
              <text x="160.0" y="22" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">1. Diagnóstico (E1): brechas actuales</text>
              <text x="616.0" y="22" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">2. Metodología SDLC-IA con Aracne (E2)</text>
              <text x="1056.0" y="22" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">Brecha cerrada</text>
              <rect x="356" y="38" width="79" height="26" rx="13" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.2" />
              <text x="395.5" y="56" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Entender</text>
              <rect x="441" y="38" width="71" height="26" rx="13" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.2" />
              <text x="476.5" y="56" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Decidir</text>
              <rect x="518" y="38" width="102" height="26" rx="13" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.2" />
              <text x="569.0" y="56" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Descomponer</text>
              <rect x="626" y="38" width="79" height="26" rx="13" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.2" />
              <text x="665.5" y="56" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Traducir</text>
              <rect x="711" y="38" width="86" height="26" rx="13" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.2" />
              <text x="754.0" y="56" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Construir</text>
              <rect x="803" y="38" width="64" height="26" rx="13" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.2" />
              <text x="835.0" y="56" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" text-anchor="middle">Cerrar</text>
              <rect x="0" y="80" width="320" height="100" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.5" />
              <text x="14" y="107" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Requerimientos sin desglose.</text>
              <text x="14" y="130" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Actas extensas que no se</text>
              <text x="14" y="150" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">descomponen en historias ni</text>
              <text x="14" y="170" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">criterios, sin vínculo con el</text>
              <text x="14" y="190" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">código.</text>
              <rect x="356" y="80" width="520" height="100" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.5" />
              <text x="370" y="107" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Descomponer y Traducir.</text>
              <text x="370" y="130" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Épicas e historias con criterios de aceptación; un contrato</text>
              <text x="370" y="150" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">verificable por historia; traza requisito, historia,</text>
              <text x="370" y="170" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">contrato.</text>
              <rect x="912" y="80" width="288" height="100" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
              <text x="926" y="110" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">Historias estimables y traza</text>
              <text x="926" y="131" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">hasta el código; evidencia</text>
              <text x="926" y="152" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">para auditoría.</text>
              <path d="M320 130.0 L354 130.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#br-b)" />
              <path d="M876 130.0 L910 130.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#br-b)" />
              <rect x="0" y="194" width="320" height="100" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.5" />
              <text x="14" y="221" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Arquitectura sin estándar.</text>
              <text x="14" y="244" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Sin arquitecto ni documento; cada</text>
              <text x="14" y="264" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">desarrollador decide.</text>
              <rect x="356" y="194" width="520" height="100" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.5" />
              <text x="370" y="221" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Decidir y Construir.</text>
              <text x="370" y="244" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Arquitectura vinculante en el repositorio; Construir carga</text>
              <text x="370" y="264" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">las reglas y la arquitectura.</text>
              <rect x="912" y="194" width="288" height="100" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
              <text x="926" y="224" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">Código homogéneo bajo una sola</text>
              <text x="926" y="245" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">base.</text>
              <path d="M320 244.0 L354 244.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#br-b)" />
              <path d="M876 244.0 L910 244.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#br-b)" />
              <rect x="0" y="308" width="320" height="100" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.5" />
              <text x="14" y="335" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">IA usada como chat.</text>
              <text x="14" y="358" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Sin método ni política.</text>
              <rect x="356" y="308" width="520" height="100" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.5" />
              <text x="370" y="335" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Construir y Cerrar con agentes.</text>
              <text x="370" y="358" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Prueba por escenario, verificación contra el contrato y</text>
              <text x="370" y="378" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">puertas humanas.</text>
              <rect x="912" y="308" width="288" height="100" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
              <text x="926" y="338" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">Capacidad ampliada; las</text>
              <text x="926" y="359" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">decisiones siguen en las</text>
              <text x="926" y="380" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">personas.</text>
              <path d="M320 358.0 L354 358.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#br-b)" />
              <path d="M876 358.0 L910 358.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#br-b)" />
              <rect x="0" y="422" width="320" height="100" rx="8" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.5" />
              <text x="14" y="449" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Documentación dispersa.</text>
              <text x="14" y="472" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">SharePoint, Figma, correo y memoria</text>
              <text x="14" y="492" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">de las personas.</text>
              <rect x="356" y="422" width="520" height="100" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.5" />
              <text x="370" y="449" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Contexto, memoria y tablero.</text>
              <text x="370" y="472" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Contexto del proyecto, memoria y tablero en el repositorio;</text>
              <text x="370" y="492" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">épicas e historias en Azure Boards.</text>
              <rect x="912" y="422" width="288" height="100" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
              <text x="926" y="452" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">Documentación que se actualiza</text>
              <text x="926" y="473" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="600">con el trabajo.</text>
              <path d="M320 472.0 L354 472.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#br-b)" />
              <path d="M876 472.0 L910 472.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#br-b)" />
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">De cada brecha al resultado</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><span class="pill pill--partial">Brecha</span> <strong>Requerimientos sin desglose.</strong> Actas extensas que no se descomponen en historias ni criterios, sin vínculo con el código.<br><span class="pill pill--ok">Metodología</span> <strong>Descomponer y Traducir.</strong> Épicas e historias con criterios de aceptación; un contrato verificable por historia; traza requisito, historia, contrato.<br><span class="pill pill--ok">Resultado</span> Historias estimables y traza hasta el código; evidencia para auditoría.</li>
                  <li><span class="pill pill--partial">Brecha</span> <strong>Arquitectura sin estándar.</strong> Sin arquitecto ni documento; cada desarrollador decide.<br><span class="pill pill--ok">Metodología</span> <strong>Decidir y Construir.</strong> Arquitectura vinculante en el repositorio; Construir carga las reglas y la arquitectura.<br><span class="pill pill--ok">Resultado</span> Código homogéneo bajo una sola base.</li>
                  <li><span class="pill pill--partial">Brecha</span> <strong>IA usada como chat.</strong> Sin método ni política.<br><span class="pill pill--ok">Metodología</span> <strong>Construir y Cerrar con agentes.</strong> Prueba por escenario, verificación contra el contrato y puertas humanas.<br><span class="pill pill--ok">Resultado</span> Capacidad ampliada; las decisiones siguen en las personas.</li>
                  <li><span class="pill pill--partial">Brecha</span> <strong>Documentación dispersa.</strong> SharePoint, Figma, correo y memoria de las personas.<br><span class="pill pill--ok">Metodología</span> <strong>Contexto, memoria y tablero.</strong> Contexto del proyecto, memoria y tablero en el repositorio; épicas e historias en Azure Boards.<br><span class="pill pill--ok">Resultado</span> Documentación que se actualiza con el trabajo.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 4.2 — Brechas del diagnóstico de E1, fases de la metodología SDLC-IA que las cierran y resultado de cada cierre (ámbar: brecha; azul: metodología; verde: resultado)</figcaption>
            </figure>
          </article>

          <!-- Slide E2-14: Instalación y distribución (Figura 4.3 y Tabla 4.5) [c2-instalacion] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-instalacion" data-tone="amber">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Instalación y distribución de la metodología: repositorio privado o sandbox</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Por la cláusula vigésima cuarta la metodología pertenece a ATENEA y la Agencia decide quién la usa; cada opción la protege en un momento distinto.</p>
              </div>
              <svg viewBox="0 0 1200 560" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figura 4.3: dos opciones para distribuir la metodología, instalación local desde un repositorio privado o sandbox de ATENEA, con sus ventajas y desventajas">
              <defs>
              <marker id="ds-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
              <marker id="ds-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#B07A12" /></marker>
              </defs>
              <rect x="0" y="0" width="588" height="556" rx="10" fill="#FBFCFE" stroke="#2C6B87" stroke-width="1.6" stroke-dasharray="6,4" />
              <text x="16" y="28" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Opción 1. Instalación local desde un repositorio privado</text>
              <rect x="14" y="48.0" width="232" height="80" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
              <text x="130" y="67.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Repositorio privado de</text>
              <text x="130" y="85.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">ATENEA</text>
              <text x="130" y="102.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">acceso solo para quien la</text>
              <text x="130" y="118.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Agencia autorice</text>
              <path d="M130 128.0 L130 153.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ds-b)" />
              <text x="138" y="144.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">descarga</text>
              <rect x="14" y="153.0" width="232" height="80" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.5" />
              <text x="130" y="181.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Script de instalación</text>
              <text x="130" y="198.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">.sh en Linux y macOS, .ps1 en</text>
              <text x="130" y="214.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Windows</text>
              <path d="M130 233.0 L130 258.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ds-b)" />
              <text x="138" y="249.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">instala</text>
              <rect x="14" y="258.0" width="232" height="80" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.5" />
              <text x="130" y="294.2" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Equipo del desarrollador</text>
              <text x="130" y="311.2" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">metodología instalada</text>
              <path d="M130 338.0 L130 363.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ds-b)" />
              <rect x="14" y="363.0" width="232" height="80" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.5" />
              <text x="130" y="391.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Validación periódica</text>
              <text x="130" y="408.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">¿la persona sigue en la</text>
              <text x="130" y="424.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">organización?</text>
              <path d="M130 443.0 L130 468.0" stroke="#B07A12" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#ds-a)" />
              <text x="138" y="459.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">no</text>
              <rect x="14" y="468.0" width="232" height="80" rx="6" fill="#FFF7ED" stroke="#B07A12" stroke-width="1.5" />
              <text x="130" y="487.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Aviso a los</text>
              <text x="130" y="505.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">administradores de ATENEA</text>
              <text x="130" y="522.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">si alguien ajeno a la</text>
              <text x="130" y="538.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">organización la usa</text>
              <text x="266" y="60" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Ventajas</text>
              <text x="266" y="84" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">+</text>
              <text x="282" y="84" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">El desarrollador trabaja en su propio</text>
              <text x="282" y="101" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">entorno, sin latencia de red.</text>
              <text x="266" y="134" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">+</text>
              <text x="282" y="134" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">La instalación es repetible en Linux,</text>
              <text x="282" y="151" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">macOS y Windows.</text>
              <text x="266" y="184" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">+</text>
              <text x="282" y="184" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">ATENEA controla las versiones y decide</text>
              <text x="282" y="201" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">quién accede al repositorio.</text>
              <text x="266" y="234" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">+</text>
              <text x="282" y="234" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">No requiere infraestructura de cómputo</text>
              <text x="282" y="251" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">adicional.</text>
              <text x="266" y="294" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Desventajas</text>
              <text x="266" y="318" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">−</text>
              <text x="282" y="318" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Los archivos instalados quedan en el</text>
              <text x="282" y="335" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">equipo y pueden copiarse.</text>
              <text x="266" y="368" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">−</text>
              <text x="282" y="368" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">La validación detecta el uso indebido,</text>
              <text x="282" y="385" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">pero no lo impide.</text>
              <text x="266" y="418" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">−</text>
              <text x="282" y="418" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">La validación necesita conexión y el</text>
              <text x="282" y="435" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">script local puede modificarse.</text>
              <text x="266" y="468" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">−</text>
              <text x="282" y="468" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Hay que mantener dos scripts, uno por</text>
              <text x="282" y="485" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">sistema operativo.</text>
              <rect x="612" y="0" width="588" height="556" rx="10" fill="#FBFCFE" stroke="#1E5631" stroke-width="1.6" stroke-dasharray="6,4" />
              <text x="628" y="28" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Opción 2. Sandbox de ATENEA</text>
              <rect x="626" y="48.0" width="232" height="92" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.5" />
              <text x="742" y="98.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Desarrollador</text>
              <path d="M742 140.0 L742 184.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ds-b)" />
              <rect x="626" y="184.0" width="232" height="92" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.5" />
              <text x="742" y="217.2" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Credenciales</text>
              <text x="742" y="235.2" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">institucionales de ATENEA</text>
              <text x="742" y="252.2" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">inicia sesión</text>
              <path d="M742 276.0 L742 320.0" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ds-b)" />
              <text x="750" y="302.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">da acceso</text>
              <rect x="626" y="320.0" width="232" height="92" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
              <text x="742" y="346.8" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Sandbox de ATENEA</text>
              <text x="742" y="363.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">la metodología se usa dentro;</text>
              <text x="742" y="379.2" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">el código y los archivos no</text>
              <text x="742" y="394.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">salen de él</text>
              <path d="M742 412.0 L742 456.0" stroke="#B07A12" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#ds-a)" />
              <text x="750" y="438.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">revoca</text>
              <rect x="626" y="456.0" width="232" height="92" rx="6" fill="#FFF7ED" stroke="#B07A12" stroke-width="1.5" />
              <text x="742" y="490.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Retiro del equipo</text>
              <text x="742" y="507.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">se desactivan las credenciales</text>
              <text x="742" y="523.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">y se pierde el acceso</text>
              <text x="878" y="60" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Ventajas</text>
              <text x="878" y="84" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">+</text>
              <text x="894" y="84" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">La metodología y el código no salen de la</text>
              <text x="894" y="101" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">infraestructura de ATENEA.</text>
              <text x="878" y="134" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">+</text>
              <text x="894" y="134" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Al desactivar las credenciales, el acceso</text>
              <text x="894" y="151" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">se pierde de inmediato.</text>
              <text x="878" y="184" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">+</text>
              <text x="894" y="184" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Todo el equipo usa el mismo entorno y la</text>
              <text x="894" y="201" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">misma versión.</text>
              <text x="878" y="234" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">+</text>
              <text x="894" y="234" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">El uso queda registrado y puede auditarse</text>
              <text x="894" y="251" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">(cláusula vigésima novena).</text>
              <text x="878" y="294" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Desventajas</text>
              <text x="878" y="318" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">−</text>
              <text x="894" y="318" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">ATENEA debe aprovisionar y operar el</text>
              <text x="894" y="335" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">sandbox, con un costo recurrente.</text>
              <text x="878" y="368" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">−</text>
              <text x="894" y="368" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Sin conexión no se puede trabajar y la</text>
              <text x="894" y="385" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">red añade latencia.</text>
              <text x="878" y="418" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">−</text>
              <text x="894" y="418" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">El desarrollador adapta su flujo de</text>
              <text x="894" y="435" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">trabajo a un entorno remoto.</text>
              <text x="878" y="468" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">−</text>
              <text x="894" y="468" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Una falla del sandbox detiene a todo el</text>
              <text x="894" y="485" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">equipo.</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Dos opciones de distribución</p>
                <p style="margin:8px 0 2px;"><strong>Opción 1. Repositorio privado y script de instalación</strong></p><p style="margin:0 0 4px;">Repositorio privado de ATENEA → Script de instalación → Equipo del desarrollador → Validación periódica → Aviso a los administradores de ATENEA.</p><ul class="slide-list" style="margin:8px 0;">
                  <li><span class="pill pill--ok">Ventaja</span> El desarrollador trabaja en su propio entorno, sin latencia de red.</li>
                  <li><span class="pill pill--ok">Ventaja</span> La instalación es repetible en Linux, macOS y Windows.</li>
                  <li><span class="pill pill--ok">Ventaja</span> ATENEA controla las versiones y decide quién accede al repositorio.</li>
                  <li><span class="pill pill--ok">Ventaja</span> No requiere infraestructura de cómputo adicional.</li>
                  <li><span class="pill pill--partial">Desventaja</span> Los archivos instalados quedan en el equipo y pueden copiarse.</li>
                  <li><span class="pill pill--partial">Desventaja</span> La validación detecta el uso indebido, pero no lo impide.</li>
                  <li><span class="pill pill--partial">Desventaja</span> La validación necesita conexión y el script local puede modificarse.</li>
                  <li><span class="pill pill--partial">Desventaja</span> Hay que mantener dos scripts, uno por sistema operativo.</li>
                </ul><p style="margin:8px 0 2px;"><strong>Opción 2. Sandbox de ATENEA</strong></p><p style="margin:0 0 4px;">Desarrollador → Credenciales institucionales de ATENEA → Sandbox de ATENEA → Retiro del equipo.</p><ul class="slide-list" style="margin:8px 0;">
                  <li><span class="pill pill--ok">Ventaja</span> La metodología y el código no salen de la infraestructura de ATENEA.</li>
                  <li><span class="pill pill--ok">Ventaja</span> Al desactivar las credenciales, el acceso se pierde de inmediato.</li>
                  <li><span class="pill pill--ok">Ventaja</span> Todo el equipo usa el mismo entorno y la misma versión.</li>
                  <li><span class="pill pill--ok">Ventaja</span> El uso queda registrado y puede auditarse (cláusula vigésima novena).</li>
                  <li><span class="pill pill--partial">Desventaja</span> ATENEA debe aprovisionar y operar el sandbox, con un costo recurrente.</li>
                  <li><span class="pill pill--partial">Desventaja</span> Sin conexión no se puede trabajar y la red añade latencia.</li>
                  <li><span class="pill pill--partial">Desventaja</span> El desarrollador adapta su flujo de trabajo a un entorno remoto.</li>
                  <li><span class="pill pill--partial">Desventaja</span> Una falla del sandbox detiene a todo el equipo.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 4.3 — Opciones para distribuir la metodología al equipo de desarrollo: instalación local desde un repositorio privado de ATENEA, con validación periódica de la pertenencia a la organización, o uso dentro de un sandbox de la Agencia (ventajas y desventajas: Tabla 4.5)</figcaption>
            </figure>
          </article>

          <!-- Slide E2-15: Ruta de adopción (§4.8) -->
          <article class="slide" data-deck="e1-e4" data-module="e2" data-item="c2-ruta" data-caption-source="§4.8">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Ruta de adopción: cuatro pasos desde una demostración hasta otros módulos</h2>
              <ul class="slide-list">
                <li>
                  <strong>Se empieza con una demostración:</strong> un requerimiento real de ATENEA descompuesto con el flujo.
                </li>
                <li>
                  <strong>Luego se escribe el contexto</strong> del área del caso de uso con los documentos de arquitectura de la líder técnica.
                </li>
                <li>
                  <strong>Se acuerdan los límites del agente:</strong> qué se envía a un modelo y con qué cuentas y permisos opera.
                </li>
                <li>
                  <strong>Se extiende por porciones:</strong> primero una porción acotada del caso de uso y después otros módulos.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 372" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ruta de adopción en cuatro pasos">
              <defs>
              <marker id="ru-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
              </defs>
              <rect x="4" y="4" width="512" height="80" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.5" />
              <circle cx="38" cy="44" r="20" fill="#7FB4CA" />
              <text x="38" y="52" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700" text-anchor="middle">1</text>
              <text x="70" y="34" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">Con un requerimiento real de ATENEA, hacer un</text>
              <text x="70" y="53" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">ejercicio de descomposición como demostración.</text>
              <path d="M38 84 L38 96" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ru-b)" />
              <rect x="4" y="96" width="512" height="80" rx="8" fill="#F8FAFC" stroke="#7AA89F" stroke-width="1.5" />
              <circle cx="38" cy="136" r="20" fill="#7AA89F" />
              <text x="38" y="144" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700" text-anchor="middle">2</text>
              <text x="70" y="126" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">Escribir el contexto del área del caso de uso con los</text>
              <text x="70" y="145" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">documentos de arquitectura que la líder técnica se</text>
              <text x="70" y="164" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">comprometió a preparar.</text>
              <path d="M38 176 L38 188" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ru-b)" />
              <rect x="4" y="188" width="512" height="80" rx="8" fill="#F8FAFC" stroke="#B7CC85" stroke-width="1.5" />
              <circle cx="38" cy="228" r="20" fill="#B7CC85" />
              <text x="38" y="236" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700" text-anchor="middle">3</text>
              <text x="70" y="218" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">Acordar con ATENEA qué se envía a un modelo y con qué</text>
              <text x="70" y="237" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">cuentas y permisos opera el agente.</text>
              <path d="M38 268 L38 280" stroke="#2C6B87" stroke-width="1.6" marker-end="url(#ru-b)" />
              <rect x="4" y="280" width="512" height="80" rx="8" fill="#F8FAFC" stroke="#DFBD76" stroke-width="1.5" />
              <circle cx="38" cy="320" r="20" fill="#DFBD76" />
              <text x="38" y="328" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700" text-anchor="middle">4</text>
              <text x="70" y="310" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">Recorrer el ciclo completo en una porción acotada del</text>
              <text x="70" y="329" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">caso de uso y luego extender a otros módulos y</text>
              <text x="70" y="348" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15.5">automatizar el despliegue.</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Ruta de adopción</p>
                <ol class="slide-list" style="margin:8px 0;">
                  <li>Con un requerimiento real de ATENEA, hacer un ejercicio de descomposición como demostración.</li>
                  <li>Escribir el contexto del área del caso de uso con los documentos de arquitectura que la líder técnica se comprometió a preparar.</li>
                  <li>Acordar con ATENEA qué se envía a un modelo y con qué cuentas y permisos opera el agente.</li>
                  <li>Recorrer el ciclo completo en una porción acotada del caso de uso y luego extender a otros módulos y automatizar el despliegue.</li>
                </ol>
              </div>
              <figcaption class="fig-caption">Fuente: §4.8 — Ruta de adopción en cuatro pasos (sin tabla ni figura numerada en el informe)</figcaption>
            </figure>
          </article>

          <!-- ========================================================================= -->
          <!-- MÓDULO 4: E3 · Arquitectura y Arnés Institucional (Capítulo 5)             -->
          <!-- ========================================================================= -->

          <!-- Slide 18: Arquitectura End-to-End del Arnés Institucional (Diagrama / Figura 5.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e3">
            <div class="slide-content">
              <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
              <h2>Composición de la propuesta: integración institucional sin reemplazo</h2>
              <ul class="slide-list">
                <li>
                  <strong>Principio rector de integración:</strong> El arnés se acopla a las herramientas que ya existen en ATENEA (SharePoint, Figma, Azure Boards, Azure Repos) sin pretender sustituirlas.
                </li>
                <li>
                  <strong>Capa intermedia propia (Arnés LIA UNAL):</strong> Coordina las herramientas agénticas, mantiene las versiones de las piezas, entrega los comandos y garantiza la traza inmutable.
                </li>
                <li>
                  <strong>Modelos por tarea:</strong> Inferencia seleccionada técnicamente según la especialidad de cada agente (especificar, descomponer, construir o auditar), validada con los accesos de la entidad.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 360" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagrama de composición de la propuesta y arquitectura institucional del arnés agéntico">
                <!-- Capa Superior: Herramientas ATENEA -->
                <rect x="25" y="15" width="470" height="55" rx="8" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.3" />
                <text x="40" y="32" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="10" font-weight="700">HERRAMIENTAS EXISTENTES DE ATENEA</text>

                <rect x="35" y="38" width="140" height="24" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                <text x="105" y="54" text-anchor="middle" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="9">SharePoint (Gestor Doc)</text>

                <rect x="185" y="38" width="145" height="24" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                <text x="257" y="54" text-anchor="middle" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="9">Figma (Diseño UI/UX)</text>

                <rect x="340" y="38" width="145" height="24" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                <text x="412" y="54" text-anchor="middle" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="9">Azure Boards (Tickets)</text>

                <!-- Conexiones superiores hacia el arnés -->
                <path d="M105 62 V85" stroke="#4E93B0" stroke-width="1.3" />
                <path d="M257 62 V85" stroke="#4E93B0" stroke-width="1.3" />
                <path d="M412 62 V85" stroke="#4E93B0" stroke-width="1.3" />

                <!-- Capa Intermedia: Arnés LIA UNAL (Verde) -->
                <rect x="25" y="85" width="470" height="190" rx="10" fill="#F0F7F2" stroke="#1E5631" stroke-width="1.8" />
                <rect x="35" y="93" width="220" height="18" rx="4" fill="#1E5631" />
                <text x="145" y="106" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="9" font-weight="700">ARNÉS PRINCIPAL SDLC-IA &middot; LIA UNAL</text>

                <g font-family="Space Grotesk,sans-serif" font-size="8.5">
                  <!-- Entorno agéntico -->
                  <rect x="35" y="118" width="135" height="42" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="102" y="134" text-anchor="middle" fill="#1B2029" font-weight="700">Entorno Agéntico</text>
                  <text x="102" y="148" text-anchor="middle" fill="#5B6472">Claude Code / OpenCode CLI</text>

                  <!-- Modelos por tarea -->
                  <rect x="180" y="118" width="150" height="42" rx="5" fill="#FFF7ED" stroke="#DFBD76" />
                  <text x="255" y="134" text-anchor="middle" fill="#8A5A00" font-weight="700">Modelos por Tarea</text>
                  <text x="255" y="148" text-anchor="middle" fill="#5B6472">Definidos por UNAL / ATENEA</text>

                  <!-- Tablero de estado -->
                  <rect x="340" y="118" width="145" height="42" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="412" y="134" text-anchor="middle" fill="#1B2029" font-weight="700">Tablero de Estado</text>
                  <text x="412" y="148" text-anchor="middle" fill="#5B6472">Avance en tiempo real</text>

                  <!-- Gestor de specs -->
                  <rect x="35" y="168" width="135" height="42" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="102" y="184" text-anchor="middle" fill="#1B2029" font-weight="700">Gestor de Specs</text>
                  <text x="102" y="198" text-anchor="middle" fill="#5B6472">BMAD: PRD, Arq y CU</text>

                  <!-- Tejedor -->
                  <rect x="180" y="168" width="150" height="42" rx="5" fill="#F8FAFC" stroke="#1E5631" stroke-width="1.3" />
                  <text x="255" y="184" text-anchor="middle" fill="#1E5631" font-weight="700">Tejedor LIA UNAL</text>
                  <text x="255" y="198" text-anchor="middle" fill="#5B6472">Historia → Contrato OpenSpec</text>

                  <!-- Memoria -->
                  <rect x="340" y="168" width="145" height="42" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="412" y="184" text-anchor="middle" fill="#1B2029" font-weight="700">Memoria Persistente</text>
                  <text x="412" y="198" text-anchor="middle" fill="#5B6472">Engram + Grafo de Código</text>

                  <!-- Barra de comandos -->
                  <rect x="35" y="218" width="450" height="45" rx="6" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="260" y="235" text-anchor="middle" fill="#1E5631" font-weight="700">Catálogo de Comandos por Etapa:</text>
                  <text x="260" y="251" text-anchor="middle" fill="#5B6472">/sw:new (iniciar) &middot; /sw:adopt (adoptar) &middot; /sw:sprint (olas) &middot; /sw:build (construir) &middot; /sw:close (cerrar) &middot; /sw:status</text>
                </g>

                <!-- Conexiones inferiores hacia repositorios y despliegue -->
                <path d="M102 275 V295" stroke="#4E93B0" stroke-width="1.3" />
                <path d="M260 275 V295" stroke="#4E93B0" stroke-width="1.3" />
                <path d="M412 275 V295" stroke="#4E93B0" stroke-width="1.3" />

                <!-- Capa Inferior: Repositorios, CI/CD y Ambientes -->
                <rect x="25" y="295" width="470" height="50" rx="8" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.3" />
                <g font-family="Space Grotesk,sans-serif" font-size="8.5">
                  <rect x="35" y="307" width="140" height="26" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="105" y="323" text-anchor="middle" fill="#1B2029">Azure Repos (Código)</text>

                  <rect x="185" y="307" width="145" height="26" rx="4" fill="#FFFFFF" stroke="#DFBD76" />
                  <text x="257" y="323" text-anchor="middle" fill="#8A5A00">Azure Pipelines (CI/CD)</text>

                  <rect x="340" y="307" width="145" height="26" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="412" y="323" text-anchor="middle" fill="#1B2029">Ambientes QA / Pre / Prod</text>
                </g>
              </svg>
            </figure>
          </article>

          <!-- Slide 18: Componentes de la Propuesta Técnica (Tabla 5.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e3">
            <div class="slide-content">
              <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
              <h2>Matriz de componentes de la propuesta y estado de implementación</h2>
              <ul class="slide-list">
                <li>
                  <strong>Articulación modular:</strong> La solución integra desarrollos propios del LIA UNAL con piezas de terceros especializadas y herramientas preexistentes de ATENEA.
                </li>
                <li>
                  <strong>Núcleo LIA probado:</strong> El arnés principal, el tejedor determinista de contratos y el tablero de estado se encuentran implementados y evaluados funcionalmente.
                </li>
                <li>
                  <strong>Sujeto a decisiones de ATENEA:</strong> La forma de ejecución en terminal (Claude Code u OpenCode) y la habilitación de modelos e infraestructura se acuerdan con la Subgerencia de TIC.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table">
                  <caption>Tabla 5.1: Componentes de la propuesta, herramientas y estado de avance (tab:e3-componentes)</caption>
                  <thead>
                    <tr>
                      <th style="width:24%;">Componente</th>
                      <th>Función en el Sistema</th>
                      <th style="width:26%;">Herramienta</th>
                      <th style="width:18%;">Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Arnés principal</strong></td>
                      <td>Coordina herramientas, fija versiones, inyecta contexto y asegura traza.</td>
                      <td>Desarrollo LIA UNAL</td>
                      <td><span class="table-tag tag-green">Implementado</span></td>
                    </tr>
                    <tr>
                      <td><strong>Gestor de specs</strong></td>
                      <td>Elabora PRD, arquitectura, épicas e historias con criterios formales.</td>
                      <td>BMAD Integrado</td>
                      <td><span class="table-tag tag-green">Integrado</span></td>
                    </tr>
                    <tr>
                      <td><strong>Tejedor</strong></td>
                      <td>Convierte historia en contrato OpenSpec; calcula olas de trabajo.</td>
                      <td>Pieza propia LIA UNAL</td>
                      <td><span class="table-tag tag-green">Implementado</span></td>
                    </tr>
                    <tr>
                      <td><strong>Memoria persistente</strong></td>
                      <td>Decisiones, aprendizajes pasados y mapa semántico del código.</td>
                      <td>Engram + Graphify</td>
                      <td><span class="table-tag tag-green">Integrados</span></td>
                    </tr>
                    <tr>
                      <td><strong>Tablero de estado</strong></td>
                      <td>Visualización de avance por historia, contrato y cobertura.</td>
                      <td>Pieza propia LIA UNAL</td>
                      <td><span class="table-tag tag-green">Implementado</span></td>
                    </tr>
                    <tr>
                      <td><strong>Entorno agéntico</strong></td>
                      <td>Ejecuta comandos CLI: lectura de contexto, edición y tests.</td>
                      <td>Claude Code / OpenCode</td>
                      <td><span class="table-tag tag-amber">Por habilitar</span></td>
                    </tr>
                    <tr>
                      <td><strong>Modelos de IA</strong></td>
                      <td>Inferencia especializada por tarea (análisis, código, auditoría).</td>
                      <td>APIs / Modelos ATENEA</td>
                      <td><span class="table-tag tag-amber">Por definir</span></td>
                    </tr>
                    <tr>
                      <td><strong>Gestión documental</strong></td>
                      <td>Archivo formal de actas y evidencia de cumplimiento.</td>
                      <td>SharePoint ATENEA</td>
                      <td><span class="table-tag tag-blue">Existente</span></td>
                    </tr>
                    <tr>
                      <td><strong>Gestor repositorios</strong></td>
                      <td>Control de versiones, pull requests y ramas protegidas.</td>
                      <td>Azure Repos ATENEA</td>
                      <td><span class="table-tag tag-blue">Existente</span></td>
                    </tr>
                    <tr>
                      <td><strong>Integración/Entrega</strong></td>
                      <td>Compilación, ejecución de tests y despliegue por ambiente.</td>
                      <td>Azure Pipelines</td>
                      <td><span class="table-tag tag-amber">Por definir</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 20: Flujo Integral de Artefactos de Aracne (Diagrama de Flujo / Figura 6.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e4">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
              <h2>Flujo integral de artefactos de Aracne: de la idea a la línea base</h2>
              <ul class="slide-list">
                <li>
                  <strong>Tres fases metodológicas articuladas:</strong>
                  1. Especificación formal con BMAD (PRD y arquitectura);
                  2. Traducción determinista con OpenSpec y Tejedor LIA (Regla de frontera);
                  3. Construcción estricta SDD/ODD con pruebas automatizadas y cierre en línea base.
                </li>
                <li>
                  <strong>Regla de frontera:</strong> BMAD se detiene en la historia con criterios <em>Given/When/Then</em>; se podan deliberadamente las capacidades de escritura libre de código para obligar el paso por contratos verificables.
                </li>
                <li>
                  <strong>Gobernanza transversal:</strong> Control de cambios (`/sw:change`), gestión de defectos guiada por tests (`/sw:bug`) y memoria persistente (Engram).
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 360" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagrama de flujo integral de artefactos del arnés Aracne SDLC-AI">
                <!-- Fase 1: Especificación y Contratos -->
                <rect x="20" y="15" width="480" height="98" rx="8" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.3" />
                <rect x="30" y="22" width="260" height="18" rx="3" fill="#4E93B0" />
                <text x="160" y="35" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="9" font-weight="700">FASE 1: ESPECIFICACIÓN Y CONTRATOS (ENTENDER A TRADUCIR)</text>

                <g font-family="Space Grotesk,sans-serif" font-size="8.5">
                  <rect x="30" y="46" width="100" height="56" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="80" y="64" text-anchor="middle" fill="#1B2029" font-weight="700">Gestor Specs</text>
                  <text x="80" y="78" text-anchor="middle" fill="#5B6472">BMAD: PRD, Arq</text>
                  <text x="80" y="90" text-anchor="middle" fill="#5B6472">y prototipo UX</text>

                  <path d="M130 74 H145" stroke="#4E93B0" stroke-width="1.5" />

                  <rect x="145" y="46" width="105" height="56" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="197" y="64" text-anchor="middle" fill="#1B2029" font-weight="700">Historias Usuario</text>
                  <text x="197" y="78" text-anchor="middle" fill="#5B6472">Criterios formales</text>
                  <text x="197" y="90" text-anchor="middle" fill="#5B6472">Given/When/Then</text>

                  <path d="M250 74 H265" stroke="#1E5631" stroke-width="1.5" />

                  <rect x="265" y="46" width="110" height="56" rx="5" fill="#F0F7F2" stroke="#1E5631" stroke-width="1.3" />
                  <text x="320" y="64" text-anchor="middle" fill="#1E5631" font-weight="700">Tejedor (LIA UNAL)</text>
                  <text x="320" y="78" text-anchor="middle" fill="#5B6472">Historia → Contrato</text>
                  <text x="320" y="90" text-anchor="middle" fill="#5B6472">Registro de traza</text>

                  <path d="M375 74 H390" stroke="#4E93B0" stroke-width="1.5" />

                  <rect x="390" y="46" width="100" height="56" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="440" y="64" text-anchor="middle" fill="#1B2029" font-weight="700">OpenSpec</text>
                  <text x="440" y="78" text-anchor="middle" fill="#5B6472">Contrato ejecutable</text>
                  <text x="440" y="90" text-anchor="middle" fill="#5B6472">por cada historia</text>
                </g>

                <!-- Flecha vertical F1 -> F2 -->
                <path d="M440 102 V132" stroke="#1E5631" stroke-width="2" />
                <text x="445" y="122" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="8.5" font-weight="700">contrato formal</text>

                <!-- Fase 2: Construcción y Cierre Verificable -->
                <rect x="20" y="132" width="480" height="100" rx="8" fill="#F0F7F2" stroke="#1E5631" stroke-width="1.5" />
                <rect x="30" y="139" width="275" height="18" rx="3" fill="#1E5631" />
                <text x="167" y="152" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="9" font-weight="700">FASE 2: CONSTRUCCIÓN Y CIERRE VERIFICABLE (CONSTRUIR Y CERRAR)</text>

                <g font-family="Space Grotesk,sans-serif" font-size="8.5">
                  <rect x="390" y="163" width="100" height="56" rx="5" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.3" />
                  <text x="440" y="181" text-anchor="middle" fill="#1B2029" font-weight="700">Construir (/build)</text>
                  <text x="440" y="195" text-anchor="middle" fill="#1E5631" font-weight="600">Código + Tests</text>
                  <text x="440" y="207" text-anchor="middle" fill="#5B6472">1 test por escenario</text>

                  <path d="M390 191 H375" stroke="#1E5631" stroke-width="1.5" />

                  <rect x="265" y="163" width="110" height="56" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="320" y="181" text-anchor="middle" fill="#1E5631" font-weight="700">Cerrar (LIA UNAL)</text>
                  <text x="320" y="195" text-anchor="middle" fill="#5B6472">Validación estricta</text>
                  <text x="320" y="207" text-anchor="middle" fill="#5B6472">Archiva línea base</text>

                  <path d="M265 191 H250" stroke="#1E5631" stroke-width="1.5" />

                  <rect x="145" y="163" width="105" height="56" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="197" y="181" text-anchor="middle" fill="#1E5631" font-weight="700">Tablero (/status)</text>
                  <text x="197" y="195" text-anchor="middle" fill="#5B6472">Avance y cobertura</text>
                  <text x="197" y="207" text-anchor="middle" fill="#5B6472">Métricas en vivo</text>

                  <path d="M145 191 H130" stroke="#1E5631" stroke-width="1.5" stroke-dasharray="3,2" />

                  <rect x="30" y="163" width="100" height="56" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="80" y="181" text-anchor="middle" fill="#2C6B87" font-weight="700">Memoria (Engram)</text>
                  <text x="80" y="195" text-anchor="middle" fill="#5B6472">Registro decisiones</text>
                  <text x="80" y="207" text-anchor="middle" fill="#5B6472">Lecciones repo</text>
                </g>

                <!-- Fase 3: Gobernanza Transversal y Contexto de Código -->
                <rect x="20" y="250" width="480" height="95" rx="8" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.3" />
                <rect x="30" y="257" width="275" height="18" rx="3" fill="#4E93B0" />
                <text x="167" y="270" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="9" font-weight="700">FASE 3: GOBERNANZA TRANSVERSAL Y CONTEXTO CONTINUO</text>

                <g font-family="Space Grotesk,sans-serif" font-size="8.5">
                  <rect x="30" y="281" width="320" height="52" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="190" y="299" text-anchor="middle" fill="#1E5631" font-weight="700">Control de Cambios, Defectos e Incidencias (LIA UNAL)</text>
                  <text x="190" y="315" text-anchor="middle" fill="#5B6472">/sw:change (filtro de alcance) &middot; /sw:bug (corrección con tests) &middot; /sw:ticket (clasificación)</text>

                  <rect x="365" y="281" width="125" height="52" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="427" y="299" text-anchor="middle" fill="#2C6B87" font-weight="700">Mapa del Código</text>
                  <text x="427" y="315" text-anchor="middle" fill="#5B6472">Grafo AST real</text>
                  <text x="427" y="325" text-anchor="middle" fill="#5B6472">(Graphify)</text>
                </g>

                <!-- Bucle de cambio hacia atrás (rojo) -->
                <path d="M30 307 H12 V64 H30" stroke="#DFBD76" stroke-width="1.5" stroke-dasharray="3,2" />
                <text x="14" y="185" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="7.5" font-weight="700" transform="rotate(-90 14,185)">Cambio de alcance: regenera sólo lo afectado</text>
              </svg>
            </figure>
          </article>

          <!-- Slide 22: Sistema de Agentes Base de Aracne (Tabla 6.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e4">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
              <h2>Sistema de agentes base de Aracne: roles, artefactos y control humano</h2>
              <ul class="slide-list">
                <li>
                  <strong>Roles hiper-especializados:</strong> Cada agente opera con un ámbito funcional acotado, herramientas específicas y contratos formales de entrada y salida.
                </li>
                <li>
                  <strong>Control humano en cada compuerta:</strong> Ningún artefacto producido por un agente se integra sin la validación previa del responsable humano (PO, Diseñador, Líder Técnico o Subgerencia).
                </li>
                <li>
                  <strong>Superficies de edición acotadas:</strong> El constructor tiene prohibido modificar archivos fuera del contrato asignado, previniendo regresiones colaterales.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table">
                  <caption>Tabla 6.1: Agentes base de Aracne: rol, fase, insumos, salidas y control humano (tab:e4-agentes)</caption>
                  <thead>
                    <tr>
                      <th style="width:20%;">Agente y Rol</th>
                      <th style="width:12%;">Fase</th>
                      <th>Insumos y Disparador</th>
                      <th style="width:24%;">Artefacto de Salida</th>
                      <th style="width:20%;">Control Humano</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Analista CU</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">BMAD Analyst</span></td>
                      <td>Entender</td>
                      <td>Actas, entrevistas, tickets o código existente en el repositorio.</td>
                      <td>Brief de producto, contexto y preguntas de aclaración.</td>
                      <td>Valida intención, casos de uso y alcance.</td>
                    </tr>
                    <tr>
                      <td><strong>Product Manager</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">BMAD PM</span></td>
                      <td>Entender &rarr; Decidir</td>
                      <td>Brief validado, metas institucionales y restricciones técnicas.</td>
                      <td>PRD formal con requisitos numerados (FR/NFR).</td>
                      <td>Aprueba formalmente el PRD y priorización.</td>
                    </tr>
                    <tr>
                      <td><strong>Arquitecto</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">BMAD Architect</span></td>
                      <td>Decidir</td>
                      <td>PRD aprobado y stack tecnológico institucional.</td>
                      <td>Arquitectura vinculante (servicios, BD, integraciones).</td>
                      <td>Líder técnico y BD aprueban arquitectura.</td>
                    </tr>
                    <tr>
                      <td><strong>Diseñador Historias</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">BMAD Stories</span></td>
                      <td>Descomponer</td>
                      <td>PRD y arquitectura vinculante aprobados.</td>
                      <td>Épicas e historias con criterios Given/When/Then.</td>
                      <td>PO aprueba historias estimables y dependencias.</td>
                    </tr>
                    <tr>
                      <td><strong>Tejedor LIA</strong><br /><span style="font-size:0.68rem; color:var(--accent); font-weight:700;">LIA UNAL</span></td>
                      <td>Traducir</td>
                      <td>Historias aprobadas; invocado automáticamente.</td>
                      <td>Contratos OpenSpec verificables y plan de olas.</td>
                      <td>Desarrollador valida correspondencia.</td>
                    </tr>
                    <tr>
                      <td><strong>Constructor SDD</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">ODD Builder</span></td>
                      <td>Construir</td>
                      <td>Contrato OpenSpec asignado en una ola.</td>
                      <td>Código fuente + prueba unitaria por escenario.</td>
                      <td>Líder técnica revisa PR y aprueba merge.</td>
                    </tr>
                    <tr>
                      <td><strong>Auditor Calidad</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">Reviewer</span></td>
                      <td>Revisar</td>
                      <td>Pull Request con diff de código y pruebas.</td>
                      <td>Dictámenes multi-perspectiva (seguridad, calidad).</td>
                      <td>Líder técnica decide merge con base en reporte.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 23: Catálogo de Comandos CLI y Skills Operativas (Tabla 6.2) -->
          <article class="slide" data-deck="e1-e4" data-module="e4">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
              <h2>Catálogo de comandos CLI y skills operativas para el equipo técnico</h2>
              <ul class="slide-list">
                <li>
                  <strong>Interfaz de terminal estandarizada:</strong> Los comandos `/sw:*` unifican la experiencia del desarrollador sobre cualquier plataforma CLI (Claude Code u OpenCode).
                </li>
                <li>
                  <strong>Doctrina y reglas procedimentales:</strong> Las skills inyectan al modelo las restricciones organizacionales, la paleta cromática, los estándares de código y las reglas de seguridad.
                </li>
                <li>
                  <strong>Trazabilidad en tiempo real:</strong> El comando `/sw:status` genera el tablero interactivo de cobertura, estabilidad y tareas pendientes directamente en la terminal o navegador.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table dense">
                  <caption>Tabla 6.2: Catálogo de comandos CLI y skills por etapa (tab:e4-catalogo)</caption>
                  <thead>
                    <tr>
                      <th style="width:22%;">Comando / Skill</th>
                      <th style="width:18%;">Fase SDLC-IA</th>
                      <th>Disparador y Entrada</th>
                      <th style="width:28%;">Salida Generada</th>
                      <th style="width:17%;">Control Humano</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td><code>/sw:new</code></td><td>Entender &rarr; Traducir</td><td>Idea o servicio nuevo</td><td>PRD, arquitectura, historias y contratos</td><td>Aprueba artefactos</td></tr>
                    <tr><td><code>/sw:adopt</code></td><td>Entender &rarr; Traducir</td><td>Sistema existente; repo e insumos</td><td>Mapa del código, PRD acotado y base</td><td>Acuerda intervención</td></tr>
                    <tr><td><code>/sw:sprint</code></td><td>Descomponer</td><td>Contratos listos y dependencias</td><td>Olas de trabajo paralelo coordinadas</td><td>Asigna a desarrolladores</td></tr>
                    <tr><td><code>/sw:build</code></td><td>Construir</td><td>Contrato OpenSpec de una historia</td><td>Código + pruebas unitarias por escenario</td><td>Aprueba pull request</td></tr>
                    <tr><td><code>/sw:close</code></td><td>Cerrar</td><td>Historias con tareas verificadas</td><td>Línea base archivada y memoria Engram</td><td>Decide cierre historias</td></tr>
                    <tr><td><code>/sw:change</code></td><td>Transversal</td><td>Cambio solicitado en desarrollo</td><td>Filtro de alcance y regeneración acotada</td><td>Acepta o rechaza</td></tr>
                    <tr><td><code>/sw:bug</code></td><td>Transversal</td><td>Defecto detectado frente al contrato</td><td>Corrección guiada por test unitario</td><td>Aprueba corrección</td></tr>
                    <tr><td><code>/sw:ticket</code></td><td>Transversal</td><td>Incidencia Azure Boards / Mesa ayuda</td><td>Enrutamiento a cambio o a defecto</td><td>Confirma ruta</td></tr>
                    <tr><td><code>/sw:status</code></td><td>Transversal</td><td>Consulta de estado del proyecto</td><td>Tablero interactivo de avance y calidad</td><td>Prioriza actividades</td></tr>
                    <tr><td><code>/sw:doctor</code></td><td>Soporte</td><td>Verificación de salud del arnés</td><td>Preflight, versiones y coherencia de plan</td><td>Resuelve advertencias</td></tr>
                    <tr><td><strong>Skills Método</strong></td><td>Todas las fases</td><td>Invocación automática por comando</td><td>Reglas procedimentales institucionales</td><td>Gobernanza del flujo</td></tr>
                    <tr><td><strong>Skill Grafo AST</strong></td><td>Entender / Construir</td><td>Consulta de estructura o impacto</td><td>Respuestas deterministas sobre código</td><td>Consulta analítica</td></tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- ========================================================================= -->
          <!-- MÓDULO 6: Decisiones, Compromisos y Cierre (Capítulo 7)                   -->
          <!-- ========================================================================= -->

          <!-- Slide 24: Tres Decisiones Prioritarias de ATENEA -->
          <article class="slide" data-deck="e1-e4" data-module="e5">
            <div class="slide-content">
              <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1)</p>
              <h2>Tres decisiones prioritarias que corresponden a la Agencia ATENEA</h2>
              <ul class="slide-list">
                <li>
                  <strong>1. Selección formal del Caso de Uso (C3):</strong> Definir el proceso, la aplicación misional (Keycloak SSO o Creación de Terceros SICOR Posmedia) y el equipo técnico asignado para el piloto.
                </li>
                <li>
                  <strong>2. Habilitación de accesos institucionales:</strong> Gestionar permisos en el gestor documental, Figma, Azure Boards, Azure Repos y los modelos de IA autorizados por la política de la entidad.
                </li>
                <li>
                  <strong>3. Validación del Diagnóstico Institucional (E1):</strong> Emitir la conformidad formal sobre los hallazgos de capacidades técnicas, stack y puntos de fricción presentados en el informe.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 360" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Las tres decisiones prioritarias a cargo de ATENEA">
                <rect x="25" y="20" width="470" height="50" rx="8" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.3" />
                <text x="40" y="42" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">COMPROMISOS DECISIONALES DE LA AGENCIA ATENEA</text>
                <text x="40" y="58" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">Habilitadores críticos indispensables para iniciar la fase de construcción en Hito 2</text>

                <!-- Decisión 1 -->
                <rect x="25" y="85" width="470" height="74" rx="8" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.5" />
                <rect x="35" y="97" width="28" height="24" rx="4" fill="#1E5631" />
                <text x="49" y="113" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">D1</text>
                <text x="75" y="108" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">Caso de Uso Misional Institucional (C3)</text>
                <text x="75" y="126" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">Formalizar la selección entre el servicio unificado Keycloak o Terceros Posmedia,</text>
                <text x="75" y="142" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">definiendo el equipo de desarrollo contraparte y el proceso misional impactado.</text>

                <!-- Decisión 2 -->
                <rect x="25" y="172" width="470" height="74" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.3" />
                <rect x="35" y="184" width="28" height="24" rx="4" fill="#4E93B0" />
                <text x="49" y="200" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">D2</text>
                <text x="75" y="195" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">Accesos a Herramientas, Repositorios y Modelos de IA</text>
                <text x="75" y="213" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">Habilitar accesos del arnés a Azure Repos, Azure Boards, SharePoint y Figma,</text>
                <text x="75" y="229" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">e indicar el proveedor/modelo autorizado (Claude Teams, OpenAI o Foundry).</text>

                <!-- Decisión 3 -->
                <rect x="25" y="259" width="470" height="74" rx="8" fill="#FFFFFF" stroke="#DFBD76" stroke-width="1.3" />
                <rect x="35" y="271" width="28" height="24" rx="4" fill="#DFBD76" />
                <text x="49" y="287" text-anchor="middle" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">D3</text>
                <text x="75" y="282" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">Validación del Informe de Diagnóstico Institucional (E1)</text>
                <text x="75" y="300" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">Aprobación formal por parte de la supervisión técnica sobre los hallazgos de stack,</text>
                <text x="75" y="316" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">roles, deuda técnica en Angular 13 y los 10 puntos de fricción identificados.</text>
              </svg>
            </figure>
          </article>

          <!-- Slide 24: Matriz de Compromisos Abiertos (Tabla 7.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e5">
            <div class="slide-content">
              <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1)</p>
              <h2>Matriz de compromisos abiertos de las sesiones técnicas (Tabla 7.1)</h2>
              <ul class="slide-list">
                <li>
                  <strong>Trazabilidad de actas técnicas:</strong> Compromisos derivados de las reuniones técnicas del 7, 14 y 16 de octubre de 2026 (Acta 01 y grabaciones).
                </li>
                <li>
                  <strong>Habilitadores para el caso de uso:</strong> Se requiere recibir un requerimiento de ejemplo con su diseño validado y la estructura de carpetas de back-end y front-end de los proyectos.
                </li>
                <li>
                  <strong>Seguridad y migración:</strong> La entrega del reporte de seguridad y la definición de la fase de migración a Azure determinan la arquitectura del pipeline CI/CD.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table">
                  <caption>Tabla 7.1: Compromisos de las sesiones técnicas que condicionan E1 a E4 (tab:compromisos)</caption>
                  <thead>
                    <tr>
                      <th style="width:8%;">N.º</th>
                      <th>Compromiso Registrado</th>
                      <th style="width:22%;">Responsable</th>
                      <th style="width:14%;">Origen</th>
                      <th style="width:18%;">Estado al Corte</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>1</strong></td>
                      <td>Compartir un requerimiento de ejemplo real con su correspondiente diseño en Figma.</td>
                      <td>ATENEA</td>
                      <td>A4, R2</td>
                      <td><span class="table-tag tag-amber">Abierto</span></td>
                    </tr>
                    <tr>
                      <td><strong>2</strong></td>
                      <td>Enviar el informe formal de la reciente revisión de seguridad de las aplicaciones.</td>
                      <td>ATENEA</td>
                      <td>R2</td>
                      <td><span class="table-tag tag-amber">Abierto</span></td>
                    </tr>
                    <tr>
                      <td><strong>3</strong></td>
                      <td>Definir el estado y alcance de la migración de nube a Azure.</td>
                      <td>Subgerencia TIC</td>
                      <td>A4</td>
                      <td><span class="table-tag tag-blue">Parcial en R4</span></td>
                    </tr>
                    <tr>
                      <td><strong>4</strong></td>
                      <td>Definir y comunicar oficialmente el caso de uso institucional (C3).</td>
                      <td>ATENEA</td>
                      <td>R3</td>
                      <td><span class="table-tag tag-amber">Abierto</span></td>
                    </tr>
                    <tr>
                      <td><strong>5</strong></td>
                      <td>Enviar documento con información de proyectos y estructura de carpetas de front y back.</td>
                      <td>ATENEA</td>
                      <td>R3</td>
                      <td><span class="table-tag tag-amber">Abierto</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 25: Hoja de Ruta Contractual hacia el Hito 2 -->
          <article class="slide" data-deck="e1-e4" data-module="e5">
            <div class="slide-content">
              <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1)</p>
              <h2>Hoja de ruta: culminación del Hito 1 y transición hacia el Hito 2</h2>
              <ul class="slide-list">
                <li>
                  <strong>Cierre exitoso del Hito 1 (Semanas 1 a 13):</strong> Diagnóstico institucional consolidado (E1), Metodología SDLC-IA formalizada (E2), Arquitectura End-to-End especificada (E3) y Sistema de Agentes y Skills estructurado (E4).
                </li>
                <li>
                  <strong>Ruta operativa del Hito 2 (Semanas 14 a 22):</strong>
                  <strong>E5:</strong> Construcción, despliegue y validación del caso de uso en ambiente objetivo.
                  <strong>E6:</strong> Elaboración de manuales técnicos y operativos para independencia.
                  <strong>E7:</strong> Talleres de capacitación, transferencia tecnológica y guías de replicabilidad.
                  <strong>E8:</strong> Informe final, balance contractual y cierre de mutuo acuerdo.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 360" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hoja de ruta contractual y transición entre Hito 1 e Hito 2">
                <rect x="25" y="20" width="470" height="54" rx="8" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.3" />
                <text x="40" y="42" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">TRANSICIÓN CONTRACTUAL: HITO 1 → HITO 2 (SEMANAS 1 A 22)</text>
                <text x="40" y="58" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">Contrato Interadministrativo ATENEA-464-2026 &middot; $300.000.000 COP</text>

                <!-- Caja Hito 1 -->
                <rect x="25" y="90" width="225" height="230" rx="10" fill="#F0F7F2" stroke="#1E5631" stroke-width="1.8" />
                <rect x="35" y="100" width="205" height="22" rx="4" fill="#1E5631" />
                <text x="137" y="115" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="10" font-weight="700">HITO 1: C1–C4 / E1–E4 (50%)</text>

                <g font-family="Space Grotesk,sans-serif" font-size="9">
                  <rect x="35" y="132" width="205" height="38" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="45" y="148" fill="#1E5631" font-weight="700">E1 · Diagnóstico Institucional</text>
                  <text x="45" y="162" fill="#5B6472">Capacidades TI, roles y puntos fricción</text>

                  <rect x="35" y="178" width="205" height="38" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="45" y="194" fill="#1E5631" font-weight="700">E2 · Metodología SDLC-IA</text>
                  <text x="45" y="208" fill="#5B6472">6 fases y 5 compuertas humanas</text>

                  <rect x="35" y="224" width="205" height="38" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="45" y="240" fill="#1E5631" font-weight="700">E3 · Arquitectura End-to-End</text>
                  <text x="45" y="254" fill="#5B6472">Arnés LIA UNAL y caso de uso</text>

                  <rect x="35" y="270" width="205" height="38" rx="5" fill="#FFFFFF" stroke="#1E5631" />
                  <text x="45" y="286" fill="#1E5631" font-weight="700">E4 · Agentes y Skills</text>
                  <text x="45" y="300" fill="#5B6472">Comandos CLI y reglas OpenSpec</text>
                </g>

                <!-- Flecha de transición -->
                <path d="M250 205 H270" stroke="#1E5631" stroke-width="2.5" marker-end="url(#arrow-green)" />

                <!-- Caja Hito 2 -->
                <rect x="270" y="90" width="225" height="230" rx="10" fill="#F8FAFC" stroke="#4E93B0" stroke-width="1.8" />
                <rect x="280" y="100" width="205" height="22" rx="4" fill="#4E93B0" />
                <text x="382" y="115" text-anchor="middle" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="10" font-weight="700">HITO 2: C5–C8 / E5–E8 (50%)</text>

                <g font-family="Space Grotesk,sans-serif" font-size="9">
                  <rect x="280" y="132" width="205" height="38" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="290" y="148" fill="#2C6B87" font-weight="700">E5 · Despliegue y Piloto</text>
                  <text x="290" y="162" fill="#5B6472">Construcción y validación misional</text>

                  <rect x="280" y="178" width="205" height="38" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="290" y="194" fill="#2C6B87" font-weight="700">E6 · Documentación Operativa</text>
                  <text x="290" y="208" fill="#5B6472">Manuales de instalación y operación</text>

                  <rect x="280" y="224" width="205" height="38" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="290" y="240" fill="#2C6B87" font-weight="700">E7 · Workshop Transferencia</text>
                  <text x="290" y="254" fill="#5B6472">Capacitación y guías replicabilidad</text>

                  <rect x="280" y="270" width="205" height="38" rx="5" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="290" y="286" fill="#2C6B87" font-weight="700">E8 · Informe Final y Cierre</text>
                  <text x="290" y="300" fill="#5B6472">Matriz de verificación y balance</text>
                </g>

                <defs>
                  <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#1E5631" />
                  </marker>
                </defs>
                <text x="260" y="340" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="9.5">Hito 1 vence Semana 13 ($150M) &middot; Hito 2 vence Semana 22 ($150M) &middot; Liquidación a 4 meses</text>
              </svg>
            </figure>
          </article>
        </section>
      </main>

      <footer class="controls">
        <button class="btn" id="prev" aria-label="Diapositiva anterior">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path
              d="M15 18l-6-6 6-6"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </button>
        <span class="counter" id="counter" aria-live="polite">1 / 26</span>
        <button class="btn" id="next" aria-label="Diapositiva siguiente">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path
              d="M9 18l6-6-6-6"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </button>
      </footer>
    </div>

    <script src="assets/js/app.js?v=20261023_1"></script>
  </body>
</html>
'''
    return html

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    target = repo_root / "e1-e4.html"
    content = generate_e1_e4_html()
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ e1-e4.html generado exitosamente ({len(content)} bytes).")
