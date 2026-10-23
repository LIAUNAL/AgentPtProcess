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

          <!-- Slide 12: Principios del Rediseño SDLC-IA -->
          <article class="slide" data-deck="e1-e4" data-module="e2">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Rediseño del ciclo de desarrollo: la IA ejecuta, las personas deciden</h2>
              <ul class="slide-list">
                <li>
                  <strong>Continuidad sin ruptura:</strong> El flujo parte de los artefactos que ATENEA ya utiliza (notas de levantamiento, diseño en Figma y requerimientos) y los dota de estructura determinista.
                </li>
                <li>
                  <strong>Cierre de las tres brechas críticas:</strong>
                  1. Desglose en historias estimables con criterios de aceptación;
                  2. Arquitectura decidida previamente y vinculante para todos;
                  3. Verificación continua por contrato y evidencia inmutable.
                </li>
                <li>
                  <strong>Seis fases secuenciales:</strong> Entender &rarr; Decidir &rarr; Descomponer &rarr; Traducir &rarr; Construir &rarr; Cerrar.
                </li>
                <li>
                  <strong>La verificación ocurre al construir:</strong> Cada historia se entrega con sus pruebas automatizadas y pasa por compuertas de aprobación humana obligatorias.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 360" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Principios metodológicos del flujo SDLC-IA y sus 6 fases">
                <rect x="25" y="18" width="470" height="58" rx="8" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.3" />
                <text x="40" y="42" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700">PRINCIPIO FUNDAMENTAL DEL REDISEÑO METODOLÓGICO</text>
                <text x="40" y="60" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">«La inteligencia artificial ejecuta; los profesionales humanos deciden»</text>

                <!-- 6 Cajas de Fases -->
                <g font-family="Space Grotesk,sans-serif">
                  <!-- Fase 1 -->
                  <rect x="25" y="95" width="145" height="105" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.3" />
                  <rect x="35" y="105" width="22" height="18" rx="3" fill="#7FB4CA" />
                  <text x="46" y="118" text-anchor="middle" fill="#06080F" font-size="9" font-weight="700">1</text>
                  <text x="65" y="118" fill="#1B2029" font-size="11" font-weight="700">Entender</text>
                  <text x="35" y="140" fill="#5B6472" font-size="9">• Notas de levantamiento</text>
                  <text x="35" y="156" fill="#5B6472" font-size="9">• Brief de producto</text>
                  <text x="35" y="172" fill="#5B6472" font-size="9">• Preguntas de aclaración</text>
                  <text x="35" y="188" fill="#2C6B87" font-size="8.5" font-weight="600">Comando: /sw:new</text>

                  <!-- Fase 2 -->
                  <rect x="187" y="95" width="145" height="105" rx="8" fill="#F8FAFC" stroke="#7AA89F" stroke-width="1.3" />
                  <rect x="197" y="105" width="22" height="18" rx="3" fill="#7AA89F" />
                  <text x="208" y="118" text-anchor="middle" fill="#06080F" font-size="9" font-weight="700">2</text>
                  <text x="227" y="118" fill="#1B2029" font-size="11" font-weight="700">Decidir</text>
                  <text x="197" y="140" fill="#5B6472" font-size="9">• Arquitectura vinculante</text>
                  <text x="197" y="156" fill="#5B6472" font-size="9">• Reglas del repositorio</text>
                  <text x="197" y="172" fill="#5B6472" font-size="9">• Puerta PO y Líder Tec.</text>
                  <text x="197" y="188" fill="#2C6B87" font-size="8.5" font-weight="600">Doc: architecture-base</text>

                  <!-- Fase 3 -->
                  <rect x="350" y="95" width="145" height="105" rx="8" fill="#F8FAFC" stroke="#B7CC85" stroke-width="1.3" />
                  <rect x="360" y="105" width="22" height="18" rx="3" fill="#B7CC85" />
                  <text x="371" y="118" text-anchor="middle" fill="#06080F" font-size="9" font-weight="700">3</text>
                  <text x="390" y="118" fill="#1B2029" font-size="11" font-weight="700">Descomponer</text>
                  <text x="360" y="140" fill="#5B6472" font-size="9">• Épicas e historias</text>
                  <text x="360" y="156" fill="#5B6472" font-size="9">• Criterios Given/When/Then</text>
                  <text x="360" y="172" fill="#5B6472" font-size="9">• Plan de olas paralelas</text>
                  <text x="360" y="188" fill="#2C6B87" font-size="8.5" font-weight="600">Comando: /sw:sprint</text>

                  <!-- Fase 4 -->
                  <rect x="25" y="215" width="145" height="105" rx="8" fill="#F8FAFC" stroke="#DFBD76" stroke-width="1.3" />
                  <rect x="35" y="225" width="22" height="18" rx="3" fill="#DFBD76" />
                  <text x="46" y="238" text-anchor="middle" fill="#06080F" font-size="9" font-weight="700">4</text>
                  <text x="65" y="238" fill="#1B2029" font-size="11" font-weight="700">Traducir</text>
                  <text x="35" y="260" fill="#5B6472" font-size="9">• Contratos OpenSpec</text>
                  <text x="35" y="276" fill="#5B6472" font-size="9">• Traducción determinista</text>
                  <text x="35" y="292" fill="#5B6472" font-size="9">• Traza requisito-código</text>
                  <text x="35" y="308" fill="#2C6B87" font-size="8.5" font-weight="600">Tejedor LIA UNAL</text>

                  <!-- Fase 5 -->
                  <rect x="187" y="215" width="145" height="105" rx="8" fill="#F8FAFC" stroke="#7AA89F" stroke-width="1.3" />
                  <rect x="197" y="225" width="22" height="18" rx="3" fill="#7AA89F" />
                  <text x="208" y="238" text-anchor="middle" fill="#06080F" font-size="9" font-weight="700">5</text>
                  <text x="227" y="238" fill="#1B2029" font-size="11" font-weight="700">Construir</text>
                  <text x="197" y="260" fill="#5B6472" font-size="9">• Construcción SDD/ODD</text>
                  <text x="197" y="276" fill="#5B6472" font-size="9">• Test por cada escenario</text>
                  <text x="197" y="292" fill="#5B6472" font-size="9">• Superficie acotada</text>
                  <text x="197" y="308" fill="#2C6B87" font-size="8.5" font-weight="600">Comando: /sw:build</text>

                  <!-- Fase 6 -->
                  <rect x="350" y="215" width="145" height="105" rx="8" fill="#F8FAFC" stroke="#4E93B0" stroke-width="1.3" />
                  <rect x="360" y="225" width="22" height="18" rx="3" fill="#4E93B0" />
                  <text x="371" y="238" text-anchor="middle" fill="#06080F" font-size="9" font-weight="700">6</text>
                  <text x="390" y="238" fill="#1B2029" font-size="11" font-weight="700">Cerrar</text>
                  <text x="360" y="260" fill="#5B6472" font-size="9">• Validación estricta</text>
                  <text x="360" y="276" fill="#5B6472" font-size="9">• Fijación de línea base</text>
                  <text x="360" y="292" fill="#5B6472" font-size="9">• Memoria y lecciones</text>
                  <text x="360" y="308" fill="#2C6B87" font-size="8.5" font-weight="600">Comando: /sw:close</text>
                </g>
                <text x="260" y="340" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="10">Control transversal: /sw:change (cambios) &middot; /sw:bug (defectos) &middot; /sw:status (tablero)</text>
              </svg>
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

          <!-- Slide 13: Flujo SDLC-IA por Etapas y Carriles (Diagrama de Flujo / Figura 4.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e2">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Flujo SDLC-IA por etapas y carriles de intervención técnica</h2>
              <ul class="slide-list">
                <li>
                  <strong>Aracne-SDLC-AI:</strong> arnés metodológico del LIA UNAL para ATENEA. Coordina agentes especializados y skills que reciben el contexto del proyecto, las restricciones de la organización y las reglas de cada etapa del SDLC-IA.
                </li>
                <li>
                  <strong>Cinco carriles institucionales:</strong> Negocio, PO/UX, Arnés Aracne (LIA UNAL), Desarrollo y Seguridad/Infraestructura.
                </li>
                <li>
                  <strong>Interacción agéntica guiada:</strong> En cada etapa, el arnés toma las salidas de la anterior, produce el artefacto estructurado correspondiente y somete el resultado a la decisión del rol responsable.
                </li>
                <li>
                  <strong>Trazabilidad integral:</strong> De la necesidad al PRD, del PRD a la historia, de la historia al contrato y del contrato al código con pruebas unitarias.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 650 372" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagrama de carriles del flujo SDLC-IA propuesto para ATENEA">
                <!-- Carriles de roles (Fondo) -->
                <!-- Carril 1: Negocio / Cliente -->
                <rect x="15" y="10" width="620" height="40" rx="4" fill="#EDF1F7" stroke="#BAC7D5" stroke-width="0.8" />
                <text x="25" y="34" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="9.5" font-weight="700">1. Negocio / Cliente</text>

                <!-- Carril 2: PO y Diseño UI/UX -->
                <rect x="15" y="54" width="620" height="42" rx="4" fill="#FFFFFF" stroke="#BAC7D5" stroke-width="0.8" />
                <text x="25" y="78" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="9.5" font-weight="700">2. PO y Diseño UX</text>

                <!-- Carril 3: Arnés de Agentes (LIA UNAL) -->
                <rect x="15" y="100" width="620" height="74" rx="6" fill="#F0F7F2" stroke="#1E5631" stroke-width="1.2" />
                <text x="25" y="134" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="9.5" font-weight="700">3. Arnés Aracne</text>
                <text x="25" y="147" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="8.5" font-weight="600">(LIA UNAL)</text>

                <!-- Carril 4: Líder Técnico / Devs -->
                <rect x="15" y="178" width="620" height="42" rx="4" fill="#FFFFFF" stroke="#BAC7D5" stroke-width="0.8" />
                <text x="25" y="202" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="9.5" font-weight="700">4. Líder Técnico / Dev</text>

                <!-- Carril 5: Infraestructura / QA -->
                <rect x="15" y="224" width="620" height="42" rx="4" fill="#EDF1F7" stroke="#BAC7D5" stroke-width="0.8" />
                <text x="25" y="249" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="9.5" font-weight="700">5. Infraestructura</text>

                <!-- Separador vertical sutil entre etiquetas de carril y columnas de fases -->
                <line x1="142" y1="10" x2="142" y2="266" stroke="#BAC7D5" stroke-width="0.8" stroke-dasharray="3,3" />

                <!-- Elementos Carril 1: Negocio -->
                <g font-family="Space Grotesk,sans-serif" font-size="8">
                  <rect x="152" y="16" width="72" height="28" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="188" y="28" text-anchor="middle" fill="#1B2029" font-weight="600">Plantea</text>
                  <text x="188" y="38" text-anchor="middle" fill="#5B6472">necesidad</text>

                  <rect x="232" y="16" width="72" height="28" rx="4" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.1" />
                  <text x="268" y="28" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta:</text>
                  <text x="268" y="38" text-anchor="middle" fill="#B71C1C" font-weight="600">Firma Acta</text>

                  <rect x="552" y="16" width="72" height="28" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="588" y="28" text-anchor="middle" fill="#1B2029" font-weight="600">Validación</text>
                  <text x="588" y="38" text-anchor="middle" fill="#5B6472">Pre-prod</text>
                </g>

                <!-- Elementos Carril 2: PO y Diseño UX -->
                <g font-family="Space Grotesk,sans-serif" font-size="8">
                  <rect x="152" y="60" width="72" height="30" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="188" y="73" text-anchor="middle" fill="#1B2029" font-weight="600">Notas reunión</text>
                  <text x="188" y="83" text-anchor="middle" fill="#5B6472">+ Figma</text>

                  <rect x="232" y="60" width="72" height="30" rx="4" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.1" />
                  <text x="268" y="73" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta PO:</text>
                  <text x="268" y="83" text-anchor="middle" fill="#B71C1C" font-weight="600">Aprueba Spec</text>

                  <rect x="312" y="60" width="72" height="30" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="348" y="73" text-anchor="middle" fill="#1B2029" font-weight="600">Ajusta</text>
                  <text x="348" y="83" text-anchor="middle" fill="#5B6472">historias</text>
                </g>

                <!-- Elementos Carril 3: Arnés de Agentes (LIA UNAL) -->
                <g font-family="Space Grotesk,sans-serif" font-size="8.5">
                  <!-- Fase 1: Entender -->
                  <rect x="152" y="108" width="72" height="58" rx="5" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.2" />
                  <text x="188" y="125" text-anchor="middle" font-weight="700" fill="#1E5631">Entender</text>
                  <text x="188" y="139" text-anchor="middle" fill="#5B6472">/sw:new</text>
                  <text x="188" y="151" text-anchor="middle" fill="#8A5A00" font-size="8">PRD &amp; dudas</text>

                  <path d="M224 137 H232" stroke="#1E5631" stroke-width="1.5" marker-end="url(#arrow-green-small)" />

                  <!-- Fase 2: Decidir -->
                  <rect x="232" y="108" width="72" height="58" rx="5" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.2" />
                  <text x="268" y="125" text-anchor="middle" font-weight="700" fill="#1E5631">Decidir</text>
                  <text x="268" y="139" text-anchor="middle" fill="#5B6472">BMAD Arq.</text>
                  <text x="268" y="151" text-anchor="middle" fill="#8A5A00" font-size="8">Spec formal</text>

                  <path d="M304 137 H312" stroke="#1E5631" stroke-width="1.5" marker-end="url(#arrow-green-small)" />

                  <!-- Fase 3: Descomponer -->
                  <rect x="312" y="108" width="72" height="58" rx="5" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.2" />
                  <text x="348" y="125" text-anchor="middle" font-weight="700" fill="#1E5631">Descomponer</text>
                  <text x="348" y="139" text-anchor="middle" fill="#5B6472">/sprint</text>
                  <text x="348" y="151" text-anchor="middle" fill="#8A5A00" font-size="8">Plan de olas</text>

                  <path d="M384 137 H392" stroke="#1E5631" stroke-width="1.5" marker-end="url(#arrow-green-small)" />

                  <!-- Fase 4: Traducir -->
                  <rect x="392" y="108" width="72" height="58" rx="5" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.2" />
                  <text x="428" y="125" text-anchor="middle" font-weight="700" fill="#1E5631">Traducir</text>
                  <text x="428" y="139" text-anchor="middle" fill="#5B6472">OpenSpec</text>
                  <text x="428" y="151" text-anchor="middle" fill="#8A5A00" font-size="8">Contrato BDD</text>

                  <path d="M464 137 H472" stroke="#1E5631" stroke-width="1.5" marker-end="url(#arrow-green-small)" />

                  <!-- Fase 5: Construir -->
                  <rect x="472" y="108" width="72" height="58" rx="5" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.2" />
                  <text x="508" y="125" text-anchor="middle" font-weight="700" fill="#1E5631">Construir</text>
                  <text x="508" y="139" text-anchor="middle" fill="#5B6472">/sw:build</text>
                  <text x="508" y="151" text-anchor="middle" fill="#1E5631" font-size="8" font-weight="600">TDD 1 a 1</text>

                  <path d="M544 137 H552" stroke="#1E5631" stroke-width="1.5" marker-end="url(#arrow-green-small)" />

                  <!-- Fase 6: Cerrar -->
                  <rect x="552" y="108" width="72" height="58" rx="5" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.2" />
                  <text x="588" y="125" text-anchor="middle" font-weight="700" fill="#1E5631">Cerrar</text>
                  <text x="588" y="139" text-anchor="middle" fill="#5B6472">/sw:close</text>
                  <text x="588" y="151" text-anchor="middle" fill="#2C6B87" font-size="8">Base &amp; Mem</text>
                </g>

                <!-- Elementos Carril 4: Líder Técnico / Devs -->
                <g font-family="Space Grotesk,sans-serif" font-size="8">
                  <rect x="232" y="184" width="72" height="30" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="268" y="197" text-anchor="middle" fill="#1B2029" font-weight="600">Decisiones</text>
                  <text x="268" y="207" text-anchor="middle" fill="#5B6472">técnicas &amp; BD</text>

                  <rect x="392" y="184" width="72" height="30" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="428" y="197" text-anchor="middle" fill="#1B2029" font-weight="600">Revisa</text>
                  <text x="428" y="207" text-anchor="middle" fill="#5B6472">contrato</text>

                  <rect x="472" y="184" width="72" height="30" rx="4" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.1" />
                  <text x="508" y="197" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta PR:</text>
                  <text x="508" y="207" text-anchor="middle" fill="#B71C1C" font-weight="600">Merge código</text>
                </g>

                <!-- Elementos Carril 5: Infraestructura / QA -->
                <g font-family="Space Grotesk,sans-serif" font-size="8">
                  <rect x="152" y="230" width="72" height="30" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="188" y="243" text-anchor="middle" fill="#1B2029" font-weight="600">Política uso IA</text>
                  <text x="188" y="253" text-anchor="middle" fill="#5B6472">(Subgerencia)</text>

                  <rect x="472" y="230" width="72" height="30" rx="4" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="508" y="243" text-anchor="middle" fill="#1B2029" font-weight="600">CI/CD Azure</text>
                  <text x="508" y="253" text-anchor="middle" fill="#5B6472">(Objetivo)</text>

                  <rect x="552" y="230" width="72" height="30" rx="4" fill="#FFF2F2" stroke="#B71C1C" stroke-width="1.1" />
                  <text x="588" y="243" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta:</text>
                  <text x="588" y="253" text-anchor="middle" fill="#B71C1C" font-weight="600">Deploy QA/Prod</text>
                </g>

                <!-- Flechas verticales de gobernanza humana -->
                <path d="M268 90 V108" stroke="#B71C1C" stroke-width="1.3" stroke-dasharray="3,2" marker-end="url(#arrow-red-small)" />
                <path d="M508 166 V184" stroke="#B71C1C" stroke-width="1.3" stroke-dasharray="3,2" marker-end="url(#arrow-red-small)" />
                <path d="M588 166 V230" stroke="#B71C1C" stroke-width="1.3" stroke-dasharray="3,2" marker-end="url(#arrow-red-small)" />

                <!-- Banners inferiores de contexto y gobierno -->
                <rect x="15" y="278" width="620" height="26" rx="5" fill="#FFFFFF" stroke="#1E5631" stroke-width="1" />
                <text x="325" y="295" text-anchor="middle" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="8.8" font-weight="700">Contexto del proyecto: Reglas y arquitectura vinculante &middot; Memoria persistente Engram &middot; Modelos BMAD</text>

                <rect x="15" y="309" width="620" height="26" rx="5" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1" />
                <text x="325" y="326" text-anchor="middle" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="8.8" font-weight="700">Gobierno transversal: /sw:status (seguimiento) &middot; /sw:change (cambios) &middot; /sw:bug (defectos)</text>

                <rect x="15" y="340" width="620" height="22" rx="4" fill="#EDF1F7" stroke="#BAC7D5" stroke-width="0.8" />
                <text x="325" y="355" text-anchor="middle" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="8.2" font-weight="600">Roles institucionales: LIA UNAL propone y acompaña el arnés &middot; Subgerencia TIC valida alcance, accesos y modelos</text>

                <defs>
                  <marker id="arrow-green-small" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#1E5631" />
                  </marker>
                  <marker id="arrow-red-small" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#B71C1C" />
                  </marker>
                </defs>
              </svg>
            </figure>
          </article>

          <!-- Slide 15: Intervención Agéntica por Etapa (Tabla 4.1) -->
          <article class="slide" data-deck="e1-e4" data-module="e2">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Intervención agéntica por etapa: brechas, flujos y decisiones humanas</h2>
              <ul class="slide-list">
                <li>
                  <strong>Mapeo biunívoco de responsabilidades:</strong> Cada etapa actual de ATENEA tiene una fase equivalente en el flujo SDLC-IA que resuelve su falencia diagnóstica específica.
                </li>
                <li>
                  <strong>Sustitución de ambigüedad por contratos:</strong> La etapa de traducción convierte historias Given/When/Then en contratos OpenSpec formalmente ejecutables.
                </li>
                <li>
                  <strong>Control humano permanente:</strong> El flujo no avanza a la siguiente fase sin la aprobación explícita del responsable humano asignado en cada compuerta.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table">
                  <caption>Tabla 4.1: Intervención agéntica por etapa: brecha, flujo, decisión y resultado (tab:e2-mapa)</caption>
                  <thead>
                    <tr>
                      <th style="width:14%;">Etapa / Fase</th>
                      <th style="width:20%;">Brecha que Atiende</th>
                      <th>Qué Hace el Flujo Agéntico</th>
                      <th style="width:22%;">Decisión Humana</th>
                      <th style="width:18%;">Resultado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Entender</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">Levantamiento</span></td>
                      <td>Requerimiento extenso sin estructura</td>
                      <td>Convierte notas y diseño en especificación numerada con supuestos y dudas.</td>
                      <td>Líder de producto fija intención y resuelve preguntas.</td>
                      <td><span class="table-tag tag-green">Especificación formal</span></td>
                    </tr>
                    <tr>
                      <td><strong>Decidir</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">Especificación</span></td>
                      <td>Decisiones técnicas sin registro</td>
                      <td>Redacta arquitectura y restricciones a partir de la especificación aprobada.</td>
                      <td>Líder técnico y BD aprueban arquitectura vinculante.</td>
                      <td><span class="table-tag tag-green">Arquitectura vinculante</span></td>
                    </tr>
                    <tr>
                      <td><strong>Descomponer</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">No existe hoy</span></td>
                      <td>Sin desglose ni criterios por unidad</td>
                      <td>Propone épicas e historias estimables con criterios y plan de olas paralelas.</td>
                      <td>Líder de producto aprueba historias y prioridades.</td>
                      <td><span class="table-tag tag-green">Historias y plan de olas</span></td>
                    </tr>
                    <tr>
                      <td><strong>Traducir</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">No existe hoy</span></td>
                      <td>Estándar dependiente de cada persona</td>
                      <td>Genera contrato verificable por historia deterministamente con traza completa.</td>
                      <td>Desarrollador revisa y valida el contrato formal.</td>
                      <td><span class="table-tag tag-green">Contratos OpenSpec</span></td>
                    </tr>
                    <tr>
                      <td><strong>Construir</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">Desarrollo</span></td>
                      <td>Código heterogéneo; calidad al final</td>
                      <td>Carga reglas y memoria; construye historia a la vez: código + test por escenario.</td>
                      <td>Líder técnico aprueba integración a ramas protegidas.</td>
                      <td><span class="table-tag tag-green">Código verificado</span></td>
                    </tr>
                    <tr>
                      <td><strong>Cerrar</strong><br /><span style="font-size:0.68rem; color:var(--subtext);">Compilados</span></td>
                      <td>Sin trazabilidad ni línea base</td>
                      <td>Valida contrato en modo estricto, archiva línea base y actualiza memoria.</td>
                      <td>Subgerencia / Líder autoriza despliegue en ambiente.</td>
                      <td><span class="table-tag tag-green">Línea base archivada</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 16: Piezas de Contexto del Proyecto (Tabla 4.2) -->
          <article class="slide" data-deck="e1-e4" data-module="e2">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Contexto institucional: las tres piezas que viven en el repositorio</h2>
              <ul class="slide-list">
                <li>
                  <strong>Soberanía de datos y código:</strong> Ninguna configuración ni memoria vive fuera del repositorio de ATENEA; se elimina la dependencia del equipo en máquinas individuales.
                </li>
                <li>
                  <strong>Reglas y negocio:</strong> Documento base de arquitectura (`architecture-base.md`) que establece versiones oficiales (Angular 13, Java 17, WildFly 34) y reglas que mandan sobre el agente.
                </li>
                <li>
                  <strong>Grafo AST del código real:</strong> Mapeo determinista de dependencias, clases y métodos para evitar alucinaciones durante la refactorización.
                </li>
                <li>
                  <strong>Memoria persistente:</strong> Registro de decisiones, lecciones aprendidas y causas de defectos pasados (Engram).
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table">
                  <caption>Tabla 4.2: Piezas de contexto, contenido, fases de uso y ubicación en el repositorio (tab:e2-contexto)</caption>
                  <thead>
                    <tr>
                      <th style="width:22%;">Pieza de Contexto</th>
                      <th>Contenido y Origen Fáctico</th>
                      <th style="width:24%;">Fases donde Interviene</th>
                      <th style="width:24%;">Dónde Vive en el Repo</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Reglas y negocio</strong></td>
                      <td>Reglas de negocio por sistema, glosario, convenciones del stack (Angular 13, Java 17, WildFly 34); obtenidas de actas y entrevistas.</td>
                      <td><span class="table-tag tag-green">Entender, Decidir, Construir</span></td>
                      <td><code>architecture-base.md</code> en la raíz del repositorio institucional.</td>
                    </tr>
                    <tr>
                      <td><strong>Arquitectura de código</strong></td>
                      <td>Módulos, integraciones, modelo de datos y decisiones técnicas registradas; ingeniería inversa asistida sobre código real.</td>
                      <td><span class="table-tag tag-green">Decidir, Construir, Control de Cambios</span></td>
                      <td>Documentos de arquitectura formal y grafo AST (Graphify).</td>
                    </tr>
                    <tr>
                      <td><strong>Memoria persistente</strong></td>
                      <td>Qué se hizo, por qué, qué pruebas fallaron y qué decisiones se tomaron; generada automáticamente por el flujo agéntico.</td>
                      <td><span class="table-tag tag-blue">Construir, Cerrar, Defectos</span></td>
                      <td>Base de memoria local persistente dentro del repositorio (Engram).</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 16: Gobernanza y Ruta de CI/CD hacia Azure -->
          <article class="slide" data-deck="e1-e4" data-module="e2">
            <div class="slide-content">
              <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
              <h2>Gobernanza: cinco puertas humanas y evolución de CI/CD hacia Azure</h2>
              <ul class="slide-list">
                <li>
                  <strong>Cinco compuertas de decisión humana indelegables:</strong>
                  <strong>P1 (PO):</strong> Aprobación de intención y preguntas del PRD.
                  <strong>P2 (Líder Técnico &amp; BD):</strong> Aprobación de arquitectura y modelo de datos.
                  <strong>P3 (PO):</strong> Aprobación de historias y olas de trabajo.
                  <strong>P4 (Líder Técnico):</strong> Revisión de código y merge de PR.
                  <strong>P5 (Subgerencia TIC):</strong> Aprobación de despliegue en ambiente.
                </li>
                <li>
                  <strong>Ruta de evolución CI/CD en 3 etapas:</strong>
                  <strong>Etapa A (Actual):</strong> Validación local de contratos y tests unitarios.
                  <strong>Etapa B (Integración Continua):</strong> Pipelines automáticos en Azure Repos/Pipelines.
                  <strong>Etapa C (Entrega Continua):</strong> Despliegue automático en QA y empaquetado reproducible.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 360" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Estructura de las 5 compuertas humanas de gobernanza y las 3 etapas de CI/CD">
                <!-- Bloque 5 Puertas -->
                <rect x="25" y="15" width="470" height="155" rx="8" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.3" />
                <text x="40" y="36" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">LAS 5 COMPUERTAS HUMANAS INDELEGABLES (GOBERNANZA)</text>

                <g font-family="Space Grotesk,sans-serif" font-size="9">
                  <rect x="35" y="48" width="85" height="110" rx="6" fill="#FFFFFF" stroke="#B71C1C" stroke-width="1.2" />
                  <text x="77" y="66" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta P1</text>
                  <text x="77" y="80" text-anchor="middle" fill="#1B2029" font-weight="600">Intención y CU</text>
                  <text x="77" y="98" text-anchor="middle" fill="#5B6472">Aprueba PRD</text>
                  <text x="77" y="110" text-anchor="middle" fill="#5B6472">y resuelve</text>
                  <text x="77" y="122" text-anchor="middle" fill="#5B6472">dudas de negocio</text>
                  <rect x="42" y="132" width="71" height="18" rx="3" fill="#FFF2F2" />
                  <text x="77" y="144" text-anchor="middle" fill="#B71C1C" font-weight="700">Rol: PO</text>

                  <rect x="127" y="48" width="85" height="110" rx="6" fill="#FFFFFF" stroke="#B71C1C" stroke-width="1.2" />
                  <text x="169" y="66" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta P2</text>
                  <text x="169" y="80" text-anchor="middle" fill="#1B2029" font-weight="600">Arquitectura</text>
                  <text x="169" y="98" text-anchor="middle" fill="#5B6472">Aprueba reglas,</text>
                  <text x="169" y="110" text-anchor="middle" fill="#5B6472">servicios y</text>
                  <text x="169" y="122" text-anchor="middle" fill="#5B6472">modelo de datos</text>
                  <rect x="134" y="132" width="71" height="18" rx="3" fill="#FFF2F2" />
                  <text x="169" y="144" text-anchor="middle" fill="#B71C1C" font-weight="700">Líder Tec / BD</text>

                  <rect x="219" y="48" width="85" height="110" rx="6" fill="#FFFFFF" stroke="#B71C1C" stroke-width="1.2" />
                  <text x="261" y="66" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta P3</text>
                  <text x="261" y="80" text-anchor="middle" fill="#1B2029" font-weight="600">Historias &amp; Olas</text>
                  <text x="261" y="98" text-anchor="middle" fill="#5B6472">Aprueba criterios</text>
                  <text x="261" y="110" text-anchor="middle" fill="#5B6472">de aceptación y</text>
                  <text x="261" y="122" text-anchor="middle" fill="#5B6472">plan de sprints</text>
                  <rect x="226" y="132" width="71" height="18" rx="3" fill="#FFF2F2" />
                  <text x="261" y="144" text-anchor="middle" fill="#B71C1C" font-weight="700">Rol: PO</text>

                  <rect x="311" y="48" width="85" height="110" rx="6" fill="#FFFFFF" stroke="#B71C1C" stroke-width="1.2" />
                  <text x="353" y="66" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta P4</text>
                  <text x="353" y="80" text-anchor="middle" fill="#1B2029" font-weight="600">Revisión PR</text>
                  <text x="353" y="98" text-anchor="middle" fill="#5B6472">Verifica código,</text>
                  <text x="353" y="110" text-anchor="middle" fill="#5B6472">tests unitarios</text>
                  <text x="353" y="122" text-anchor="middle" fill="#5B6472">y hace merge</text>
                  <rect x="318" y="132" width="71" height="18" rx="3" fill="#FFF2F2" />
                  <text x="353" y="144" text-anchor="middle" fill="#B71C1C" font-weight="700">Líder Técnica</text>

                  <rect x="403" y="48" width="82" height="110" rx="6" fill="#FFFFFF" stroke="#B71C1C" stroke-width="1.2" />
                  <text x="444" y="66" text-anchor="middle" fill="#B71C1C" font-weight="700">Puerta P5</text>
                  <text x="444" y="80" text-anchor="middle" fill="#1B2029" font-weight="600">Despliegue</text>
                  <text x="444" y="98" text-anchor="middle" fill="#5B6472">Autoriza pase</text>
                  <text x="444" y="110" text-anchor="middle" fill="#5B6472">a QA, preprod</text>
                  <text x="444" y="122" text-anchor="middle" fill="#5B6472">y producción</text>
                  <rect x="410" y="132" width="68" height="18" rx="3" fill="#FFF2F2" />
                  <text x="444" y="144" text-anchor="middle" fill="#B71C1C" font-weight="700">Subgerencia</text>
                </g>

                <!-- Bloque 3 Etapas de CI/CD -->
                <rect x="25" y="185" width="470" height="155" rx="8" fill="#F8FAFC" stroke="#1E5631" stroke-width="1.3" />
                <text x="40" y="206" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="11" font-weight="700">RUTA DE EVOLUCIÓN CI/CD HACIA AZURE</text>

                <g font-family="Space Grotesk,sans-serif" font-size="9">
                  <rect x="35" y="218" width="145" height="110" rx="6" fill="#FFFFFF" stroke="#4E93B0" />
                  <text x="107" y="236" text-anchor="middle" fill="#2C6B87" font-weight="700">ETAPA A: LOCAL</text>
                  <text x="107" y="252" text-anchor="middle" fill="#1B2029" font-weight="600">Validación de Contratos</text>
                  <text x="107" y="272" text-anchor="middle" fill="#5B6472">• Ejecución en dev</text>
                  <text x="107" y="288" text-anchor="middle" fill="#5B6472">• Tests antes de pedir merge</text>
                  <text x="107" y="304" text-anchor="middle" fill="#5B6472">• Despliegue manual actual</text>
                  <text x="107" y="320" text-anchor="middle" fill="#1E5631" font-weight="700">Estado: Inmediato</text>

                  <rect x="187" y="218" width="145" height="110" rx="6" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.3" />
                  <text x="260" y="236" text-anchor="middle" fill="#1E5631" font-weight="700">ETAPA B: CI</text>
                  <text x="260" y="252" text-anchor="middle" fill="#1B2029" font-weight="600">Integración Continua</text>
                  <text x="260" y="272" text-anchor="middle" fill="#5B6472">• Azure Repos + Pipelines</text>
                  <text x="260" y="288" text-anchor="middle" fill="#5B6472">• Compilación automática</text>
                  <text x="260" y="304" text-anchor="middle" fill="#5B6472">• Ejecución de pruebas en PR</text>
                  <text x="260" y="320" text-anchor="middle" fill="#1E5631" font-weight="700">Meta: Hito 1 / Hito 2</text>

                  <rect x="340" y="218" width="145" height="110" rx="6" fill="#FFFFFF" stroke="#DFBD76" />
                  <text x="412" y="236" text-anchor="middle" fill="#8A5A00" font-weight="700">ETAPA C: CD</text>
                  <text x="412" y="252" text-anchor="middle" fill="#1B2029" font-weight="600">Entrega Continua</text>
                  <text x="412" y="272" text-anchor="middle" fill="#5B6472">• Empaquetado reproducible</text>
                  <text x="412" y="288" text-anchor="middle" fill="#5B6472">• Deploy automático a QA</text>
                  <text x="412" y="304" text-anchor="middle" fill="#5B6472">• Aprobación para producción</text>
                  <text x="412" y="320" text-anchor="middle" fill="#8A5A00" font-weight="700">Sujeto a migración nube</text>
                </g>
              </svg>
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
