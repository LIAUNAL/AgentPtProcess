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
    <link rel="stylesheet" href="assets/css/styles.css?v=20261101_1" />
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
            <button class="rail-title" type="button" data-first="7">2 · Diagnóstico E1</button>
            <div class="rail-dots" id="dots-e1"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e2">
            <button class="rail-title" type="button" data-first="23">3 · Metodología E2</button>
            <div class="rail-dots" id="dots-e2"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e3">
            <button class="rail-title" type="button" data-first="39">4 · Arquitectura E3</button>
            <div class="rail-dots" id="dots-e3"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e4">
            <button class="rail-title" type="button" data-first="59">5 · Agentes y Skills E4</button>
            <div class="rail-dots" id="dots-e4"></div>
          </div>
          <div class="rail-module" data-deck="e1-e4" data-module="e5">
            <button class="rail-title" type="button" data-first="77">6 · Decisiones y Cierre</button>
            <div class="rail-dots" id="dots-e5"></div>
          </div>
        </nav>
      </div>

      <div class="stage-layout">
        <main class="viewport" id="viewport">
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
                Entregables E1 a E4: Diagnóstico institucional, Metodología SDLC-IA, Arquitectura End-to-End y Sistema de Agentes y Skills al 23 de octubre de 2026.
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
                <span>Bogotá D.C. &middot; Manizales, 23 de octubre de 2026</span>
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
                  <strong>Plazo:</strong> hasta cinco meses desde el acta de inicio (22 semanas).
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 0 520 340" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Estructura del contrato ATENEA-464-2026 y sus cuatro resultados esperados">
              <rect x="8" y="8" width="504" height="86" rx="10" fill="#EDF1F7" stroke="#2C6B87" stroke-width="1.5" />
              <text x="24" y="34" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">CONTRATO ATENEA-464-2026</text>
              <text x="24" y="58" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">ATENEA ↔ UNAL Sede Manizales</text>
              <text x="24" y="80" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">8 componentes · 22 semanas</text>
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
              <h2>Estado de los entregables E1 a E4 al corte</h2>
              <ul class="slide-list">
                <li>
                  <strong>Corte: 2 de noviembre de 2026.</strong> El informe se apoya en la minuta, el acta 01 del 7 de octubre, tres sesiones grabadas, las sesiones del 23 y del 30 de octubre, tres documentos de ATENEA y sus observaciones escritas del 1 de noviembre.
                </li>
                <li>
                  <strong>Hito 1:</strong> E1 a E4 integran el hito 1 del cronograma contractual.
                </li>
                <li>
                  <strong>E1:</strong> diagnóstico completo, listo para la validación de ATENEA.
                </li>
                <li>
                  <strong>E2 a E4:</strong> propuesta definida para el flujo, la arquitectura y el arnés de agentes; el caso de uso Campus 2600 en Hēma quedó definido el 30 de octubre.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <svg viewBox="0 -30 520 410" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Estado de los entregables E1 a E4 al 2 de noviembre de 2026">
              <text x="6" y="-10" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Corte: 2 de noviembre de 2026</text>
              <rect x="6" y="6" width="508" height="78" rx="9" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
              <rect x="6" y="6" width="112" height="78" rx="9" fill="#1E5631" />
              <rect x="100" y="6" width="18" height="78" fill="#1E5631" />
              <text x="62" y="44" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700" text-anchor="middle">E1</text>
              <text x="62" y="64" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Diagnóstico</text>
              <text x="134" y="51" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Diagnóstico completo para validación</text>
              <rect x="6" y="92" width="508" height="78" rx="9" fill="#FFF7ED" stroke="#8A5A00" stroke-width="1.5" />
              <rect x="6" y="92" width="112" height="78" rx="9" fill="#8A5A00" />
              <rect x="100" y="92" width="18" height="78" fill="#8A5A00" />
              <text x="62" y="130" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700" text-anchor="middle">E2</text>
              <text x="62" y="150" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">SDLC-IA</text>
              <text x="134" y="137" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Flujo propuesto por etapa</text>
              <rect x="6" y="178" width="508" height="110" rx="9" fill="#FFF7ED" stroke="#8A5A00" stroke-width="1.5" />
              <rect x="6" y="178" width="112" height="110" rx="9" fill="#8A5A00" />
              <rect x="100" y="178" width="18" height="110" fill="#8A5A00" />
              <text x="62" y="230" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700" text-anchor="middle">E3</text>
              <text x="62" y="250" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Arquitectura</text>
              <text x="134" y="204" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Composición definida por tipo</text>
              <text x="134" y="225" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">de componente</text>
              <text x="134" y="250" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="14">Caso Campus 2600 en Hēma definido el 30 de octubre;</text>
              <text x="134" y="270" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="14">primera reconstrucción: 7 épicas y 14 historias</text>
              <rect x="6" y="296" width="508" height="78" rx="9" fill="#FFF7ED" stroke="#8A5A00" stroke-width="1.5" />
              <rect x="6" y="296" width="112" height="78" rx="9" fill="#8A5A00" />
              <rect x="100" y="296" width="18" height="78" fill="#8A5A00" />
              <text x="62" y="334" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700" text-anchor="middle">E4</text>
              <text x="62" y="354" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Agentes y skills</text>
              <text x="134" y="331" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Arnés propuesto y probado</text>
              <text x="134" y="353" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">fuera de ATENEA</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Estado de E1 a E4 al 2 de noviembre de 2026</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>E1 Diagnóstico:</strong> <span class="pill pill--ok">Diagnóstico completo para validación</span></li>
                  <li><strong>E2 SDLC-IA:</strong> <span class="pill pill--partial">Flujo propuesto por etapa</span></li>
                  <li><strong>E3 Arquitectura:</strong> <span class="pill pill--partial">Composición definida por tipo de componente</span> Caso Campus 2600 en Hēma definido el 30 de octubre, con una primera reconstrucción de 7 épicas y 14 historias.</li>
                  <li><strong>E4 Agentes y skills:</strong> <span class="pill pill--partial">Arnés propuesto y probado fuera de ATENEA</span></li>
                </ul>
              </div>
              <figcaption class="fig-caption">Tabla 1.1. Estado de E1 a E4 al 2 de noviembre de 2026</figcaption>
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
                  <strong>Confidencialidad (décima):</strong> la información de ATENEA solo se almacena en sistemas que cumplan su seguridad.
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
                      <td data-label="Elemento"><strong>Supervisión (octava)</strong></td>
                      <td data-label="Condición en la minuta">Subgerente de Tecnologías de Información y Comunicaciones, o quien designe por escrito el ordenador del gasto.</td>
                    </tr>
                    <tr>
                      <td data-label="Elemento"><strong>Liquidación (decimosexta)</strong></td>
                      <td data-label="Condición en la minuta">De mutuo acuerdo dentro de los cuatro meses siguientes al vencimiento del plazo.</td>
                    </tr>
                    <tr>
                      <td data-label="Elemento"><strong>Ejecución (trigésima)</strong></td>
                      <td data-label="Condición en la minuta">Requiere acta de inicio; el perfeccionamiento se completa en SECOP II.</td>
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

          <!-- Slide 5: Entregables, componentes e hitos (Tablas 2.3 y 2.4) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e0">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">1 &middot; Marco Contractual y Alcance</p>
                <h2 style="margin-bottom:4px;">Entregables E1 a E8, componentes C1 a C8 e hitos</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">La correspondencia no es uno a uno: el cumplimiento se verifica por componente y cada hito agrupa cuatro.</p>
              </div>
              <svg viewBox="0 0 1200 540" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mapa entre entregables E1 a E8 y componentes C1 a C8, agrupados por hito contractual">
              <rect x="12" y="32.0" width="486" height="242.0" rx="10" fill="#F4FAF5" stroke="#1E5631" stroke-width="1.3" />
              <text x="26" y="52.0" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">HITO 1 · SEMANA 13</text>
              <rect x="12" y="274.0" width="486" height="242.0" rx="10" fill="#F2F7FA" stroke="#2C6B87" stroke-width="1.3" />
              <text x="26" y="294.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">HITO 2 · SEMANA 22</text>
              <rect x="702" y="32.0" width="486" height="242.0" rx="10" fill="#F4FAF5" stroke="#1E5631" stroke-width="1.3" />
              <text x="716" y="52.0" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">COMPONENTES C1 A C4 · HITO 1</text>
              <rect x="702" y="274.0" width="486" height="242.0" rx="10" fill="#F2F7FA" stroke="#2C6B87" stroke-width="1.3" />
              <text x="716" y="294.0" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" letter-spacing="1">COMPONENTES C5 A C8 · HITO 2</text>
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
              <text x="330" y="526" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">E4 cubre C4 (hito 1) y C5 (hito 2)</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Componentes, entregables e hitos</p>
                <p class="sched-sub">Hito 1 (semana 13)</p>
                <ul class="slide-list" style="margin:6px 0;">
                  <li><strong>C1</strong> Diagnóstico técnico, operativo y organizacional ← E1</li>
                  <li><strong>C2</strong> Definición de la metodología SDLC-IA ← E2</li>
                  <li><strong>C3</strong> Caso de uso institucional ← E1 y E3</li>
                  <li><strong>C4</strong> Agentes inteligentes ← E4</li>
                </ul>
                <p class="sched-sub">Hito 2 (semana 22)</p>
                <ul class="slide-list" style="margin:6px 0;">
                  <li><strong>C5</strong> Puesta en marcha de agentes y skills ← E4</li>
                  <li><strong>C6</strong> Ingeniería de pruebas y validación ← E5</li>
                  <li><strong>C7</strong> Despliegue en un proceso misional ← E5</li>
                  <li><strong>C8</strong> Documentación y transferencia ← E6, E7 y E8</li>
                </ul>
                <p class="sched-note">E4 cubre C4 (hito 1) y C5 (hito 2): para el hito 1 cuenta el documento de definición del sistema de agentes.</p>
              </div>
              <figcaption class="fig-caption">Tabla 2.4 — Entregables E1 a E8 y su relación con los componentes C1 a C8; hitos según la Tabla 2.3</figcaption>
            </figure>
          </article>

          <!-- Slide 6: Cronograma operativo (Figura 2.1) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e0">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">1 &middot; Marco Contractual y Alcance</p>
                <h2 style="margin-bottom:4px;">Cronograma operativo semanal y distribución de hitos</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El hito 1 vence en la semana 13; avance actual al 23 de octubre de 2026: E1 completo para validación y E2 a E4 con propuesta definida.</p>
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
                      <td data-label="Tipo">Plataforma de formación</td>
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
              <h2>Equipo y roles: concentración de funciones</h2>
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
                      <th style="width:34%;font-size:0.82em;">¿Qué hace hoy?</th>
                      <th style="font-size:0.82em;">Falencia</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Rol"><strong>Negocio o área cliente</strong></td>
                      <td data-label="Personas">Varias áreas (p. ej., Posmedia, Tesorería)</td>
                      <td data-label="¿Qué hace hoy?">Plantea la necesidad, aprueba el Figma de palabra y firma el acta</td>
                      <td data-label="Falencia">La firma llega semanas después y puede traer cambios</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Líder de producto (PO de facto)</strong></td>
                      <td data-label="Personas">4; el acta 01 registró 2 o 3</td>
                      <td data-label="¿Qué hace hoy?">Cada uno atiende un módulo: levanta con negocio, redacta el acta y gestiona firmas</td>
                      <td data-label="Falencia">Concentra levantamiento, especificación y aprobación sin apoyo para descomponer</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Diseño UI/UX</strong></td>
                      <td data-label="Personas">1</td>
                      <td data-label="¿Qué hace hoy?">Participa en las mesas, en forma virtual, y produce el Figma comentado</td>
                      <td data-label="Falencia">Es la única validación previa a construir</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Líder del equipo de desarrollo</strong></td>
                      <td data-label="Personas">1</td>
                      <td data-label="¿Qué hace hoy?">Revisa a mano cada cambio antes de integrarlo; define el enfoque técnico</td>
                      <td data-label="Falencia">Cuello de botella de revisión; sin reglas escritas contra las cuales revisar</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Base de datos</strong></td>
                      <td data-label="Personas">1</td>
                      <td data-label="¿Qué hace hoy?">Define con la líder el enfoque técnico de cada proyecto</td>
                      <td data-label="Falencia">Decisiones técnicas sin registro</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Desarrolladores</strong></td>
                      <td data-label="Personas">1 de front-end y 1 de back-end por módulo; 2 dedicados a SICORE CTeI</td>
                      <td data-label="¿Qué hace hoy?">Estiman, construyen y generan los compilados; desde 2027 se busca un perfil full stack</td>
                      <td data-label="Falencia">Cada quien estructura el código a su criterio</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Infraestructura</strong></td>
                      <td data-label="Personas">1</td>
                      <td data-label="¿Qué hace hoy?">Recibe los compilados, despliega y lidera la migración a Azure</td>
                      <td data-label="Falencia">Despliegue dependiente de una persona</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Seguridad</strong></td>
                      <td data-label="Personas">2</td>
                      <td data-label="¿Qué hace hoy?">Se vincularon a los sistemas de desarrollo este año</td>
                      <td data-label="Falencia">Primera revisión de seguridad de las aplicaciones, cerca de un mes antes del 7 de octubre</td>
                    </tr>
                    <tr>
                      <td data-label="Rol"><strong>Arquitecto de software</strong></td>
                      <td data-label="Personas"><span class="pill pill--risk">0 personas</span></td>
                      <td data-label="¿Qué hace hoy?">No aplica</td>
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

          <!-- Slide nueva S7: Historias de usuario de ejemplo (Tabla 3.3) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Dos historias de usuario reales: formato institucional, criterios en prosa</h2>
              <ul class="slide-list">
                <li>
                  <strong>Formato F1_P5_TIC:</strong> control de cambios, «como, quiero, para», criterios numerados en prosa y tabla de aprobaciones (A7, A8).
                </li>
                <li>
                  <strong>F-01 con matices:</strong> la de creación de terceros tiene alcance de épica; la de Talentos Excepcionales es del tamaño de una historia.
                </li>
                <li>
                  <strong>Lo que falta en ambas:</strong> criterios escritos como escenarios que se puedan convertir en pruebas.
                </li>
                <li>
                  <strong>Aprobada incompleta:</strong> la de terceros se firmó con partes remitidas a criterios futuros.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.2vw,2.14vh),1.5rem);">
                  <caption>Tabla 3.3 — Las dos historias de usuario de ejemplo enviadas por ATENEA, en el formato F1_P5_TIC</caption>
                  <thead>
                    <tr>
                      <th style="width:24%;font-size:0.82em;">Rasgo</th>
                      <th style="width:40%;font-size:0.82em;">Creación de terceros (A7)</th>
                      <th style="font-size:0.82em;">Talentos Excepcionales (A8)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Rasgo"><strong>Extensión y fechas</strong></td>
                      <td data-label="Creación de terceros (A7)">12 páginas; creada y aprobada el 14 de agosto de 2026</td>
                      <td data-label="Talentos Excepcionales (A8)">7 páginas; creada el 2 y aprobada el 6 de octubre de 2026</td>
                    </tr>
                    <tr>
                      <td data-label="Rasgo"><strong>Alcance</strong></td>
                      <td data-label="Creación de terceros (A7)">Validación del producto financiero en SICORE y creación de terceros en BOGDATA y SEVEN</td>
                      <td data-label="Talentos Excepcionales (A8)">Ajustes de textos, requisitos, filtros y acceso a una convocatoria cerrada</td>
                    </tr>
                    <tr>
                      <td data-label="Rasgo"><strong>Criterios de aceptación</strong></td>
                      <td data-label="Creación de terceros (A7)">4, con pestañas y estados, cargas masivas en Excel y correos por motivo de rechazo</td>
                      <td data-label="Talentos Excepcionales (A8)">5, sobre todo cambios de texto con capturas</td>
                    </tr>
                    <tr>
                      <td data-label="Rasgo"><strong>Lo que queda abierto</strong></td>
                      <td data-label="Creación de terceros (A7)">7 remisiones a criterios que «se detallarán»; 3 formatos por validar con el equipo de datos</td>
                      <td data-label="Talentos Excepcionales (A8)">La lista de participantes llega después, en Excel</td>
                    </tr>
                    <tr>
                      <td data-label="Rasgo"><strong>Aprobaciones</strong></td>
                      <td data-label="Creación de terceros (A7)">5 roles, el mismo día</td>
                      <td data-label="Talentos Excepcionales (A8)">3 roles</td>
                    </tr>
                  </tbody>
                </table>
              </div>
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
              <text x="790" y="433.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">Spring Boot 3</text>
              <rect x="995.0" y="382.0" width="200" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="1095" y="416.0" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Oracle Autonomous</text>
              <text x="1095" y="433.0" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">un esquema por ambiente</text>
              <rect x="675.0" y="490.0" width="230" height="76" rx="8" fill="#FFFFFF" stroke="#4E93B0" stroke-width="1.6" />
              <text x="790" y="515.5" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700" text-anchor="middle">Keycloak</text>
              <text x="790" y="532.5" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">SSO</text>
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
                  <li><strong>Clúster ATENEA en OCI (QA, preproducción y producción):</strong> Front-end Angular 13 en Docker → Back-end Java 17 con Spring Boot 3 → Oracle Autonomous con un esquema por ambiente; el back-end se autentica con Keycloak (SSO, en incorporación).</li>
                  <li><strong>Clientes y áreas</strong> acceden al front-end por HTTPS.</li>
                  <li><strong>Microsoft Azure:</strong> destino de la migración, fase 1, desde Oracle Cloud.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 3.2 — Elementos de infraestructura y desarrollo de ATENEA: el recuadro agrupa los tres ambientes del clúster en Oracle Cloud; Azure es el destino de la migración en curso</figcaption>
            </figure>
          </article>

          <!-- Slide 11: Stack tecnológico 1/2 (Tabla 3.4) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Stack de aplicación: tecnología y situación (1/2)</h2>
              <ul class="slide-list">
                <li>
                  <strong>Front-end con deuda:</strong> Angular 13 está fuera de soporte; ATENEA reconoce que debe subir a la versión 22 o 23.
                </li>
                <li>
                  <strong>Back-end vigente:</strong> Java 17 y Spring Boot 3 en Docker; la actualización a Java 21 está pendiente.
                </li>
                <li>
                  <strong>Código y documentación dispersos:</strong> Oracle Visual Builder en migración a Azure DevOps; actas en SharePoint y prototipos en Figma.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.2vw,2.14vh),1.5rem);">
                  <caption>Tabla 3.4 — Elementos de infraestructura y desarrollo, con su tecnología y su situación (parte 1 de 2)</caption>
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
                      <td data-label="Tecnología">Angular 13.3 con TypeScript 4.6 sobre Node, en contenedor Docker</td>
                      <td data-label="Observaciones">Fuera de soporte; ATENEA reconoce que debe subir a la versión 22 o 23</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Back-end</strong></td>
                      <td data-label="Tecnología">Java 17 con Spring Boot 3.3.5, empaquetado como .war; JPA sobre Oracle</td>
                      <td data-label="Observaciones">Actualización a Java 21 pendiente; el devcontainer del repositorio aún usa una imagen de Java 11</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Servidor de aplicaciones</strong></td>
                      <td data-label="Tecnología">En Docker sobre Linux Ubuntu</td>
                      <td data-label="Observaciones">Reemplazó a WebLogic a comienzos de 2026</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Base de datos</strong></td>
                      <td data-label="Tecnología">Oracle Autonomous; cuatro esquemas, tres oficiales (desarrollo o QA, preproducción, producción)</td>
                      <td data-label="Observaciones">Un servidor para producción y otro para los preproductivos; producto del Marketplace de Azure</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Identidad</strong></td>
                      <td data-label="Tecnología">Keycloak</td>
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

          <!-- Slide 12: Ambientes, nube, seguridad y despliegue 2/2 (Tabla 3.4) -->
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
                  <caption>Tabla 3.4 — Elementos de infraestructura y desarrollo, con su tecnología y su situación (parte 2 de 2)</caption>
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
                      <td data-label="Observaciones">Librerías desactualizadas y token de sesión en local storage; sin análisis de código ni de dependencias confirmado. El interceptor solo agrega el token a las peticiones POST y 12 rutas privadas se declaran sin guard en el enrutamiento raíz (por verificar)</td>
                    </tr>
                    <tr>
                      <td data-label="Capa o función"><strong>Pruebas</strong></td>
                      <td data-label="Tecnología">53 clases JUnit 5 con Mockito (43 de renovación); 236 archivos .spec.ts con Karma y Jasmine</td>
                      <td data-label="Observaciones">Sin CI no corren solas; validación manual en preproducción</td>
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

          <!-- Slide 13: Licencias y servicios de IA (Tabla 3.5) -->
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
                  <caption>Tabla 3.5 — Licencias y servicios de IA disponibles en ATENEA</caption>
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

          <!-- Slide nueva S7: Arquitectura actual de SICORE Posmedia (Tabla 3.6) -->
          <article class="slide" data-deck="e1-e4" data-module="e1">
            <div class="slide-content">
              <p class="slide-kicker">2 &middot; Diagnóstico ATENEA (E1)</p>
              <h2>Arquitectura actual de SICORE Posmedia: monolito en capas y SPA en Angular</h2>
              <ul class="slide-list">
                <li>
                  <strong>Diagnóstico de ATENEA (A9):</strong> descriptivo, sobre la rama master, enviado el 23 de octubre.
                </li>
                <li>
                  <strong>F-04 en cifras:</strong> varias convenciones conviven para lo mismo en los dos repositorios.
                </li>
                <li>
                  <strong>Arquitectura base:</strong> no parte de cero; falta decidir cuál variante es la norma.
                </li>
                <li>
                  <strong>Para el arnés:</strong> el .gitignore excluye CLAUDE.md y .claude/; esa regla debe ajustarse al instalar.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.72rem,min(1.2vw,2.14vh),1.5rem);">
                  <caption>Tabla 3.6 — Tamaño y organización de los repositorios de SICORE Posmedia al 23 de octubre de 2026</caption>
                  <thead>
                    <tr>
                      <th style="width:22%;font-size:0.82em;">Aspecto</th>
                      <th style="width:40%;font-size:0.82em;">sicore-api (back-end)</th>
                      <th style="font-size:0.82em;">sicore-web (front-end)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Aspecto"><strong>Código</strong></td>
                      <td data-label="sicore-api (back-end)">1254 archivos Java, unas 118 500 líneas</td>
                      <td data-label="sicore-web (front-end)">2794 archivos, unas 133 600 líneas de TypeScript</td>
                    </tr>
                    <tr>
                      <td data-label="Aspecto"><strong>Piezas</strong></td>
                      <td data-label="sicore-api (back-end)">77 controladores, 184 entidades, 179 repositorios; servicios: 57,3 % de los archivos</td>
                      <td data-label="sicore-web (front-end)">543 componentes, 107 módulos, 108 servicios</td>
                    </tr>
                    <tr>
                      <td data-label="Aspecto"><strong>Acceso a datos</strong></td>
                      <td data-label="sicore-api (back-end)">574 consultas SQL nativas, acopladas a Oracle</td>
                      <td data-label="sicore-web (front-end)">Estado en servicios y en local o session storage (139 archivos)</td>
                    </tr>
                    <tr>
                      <td data-label="Aspecto"><strong>Pruebas</strong></td>
                      <td data-label="sicore-api (back-end)">53 clases; 43 en renovación</td>
                      <td data-label="sicore-web (front-end)">236 archivos .spec.ts</td>
                    </tr>
                    <tr>
                      <td data-label="Aspecto"><strong>Convenciones</strong></td>
                      <td data-label="sicore-api (back-end)">Dos manejadores globales de excepciones; DTO en tres paquetes</td>
                      <td data-label="sicore-web (front-end)">Cinco patrones de carpetas; versiones paralelas de una funcionalidad</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide 14: Capacidades y brechas (Tabla 3.7) [c1-brechas] -->
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
                  <caption>Tabla 3.7 — Capacidades actuales y brechas de ATENEA en cada área de trabajo</caption>
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
                      <td data-label="Capacidad actual">Un desarrollador de front-end en Angular y uno de back-end en Java por módulo</td>
                      <td data-label="Brecha">Angular 13 fuera de soporte y actualización a Java 21 pendiente</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Revisión, pruebas y despliegue</strong></td>
                      <td data-label="Capacidad actual">Revisión manual de la líder del equipo y validación en preproducción</td>
                      <td data-label="Brecha">Sin CI/CD; pruebas concentradas en un módulo y sin ejecución automática; despliegue que depende de una persona</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Seguridad</strong></td>
                      <td data-label="Capacidad actual">Dos personas de seguridad vinculadas este año; WAF, Defender for Cloud y copias por ambiente</td>
                      <td data-label="Brecha">Primera revisión de seguridad de las aplicaciones en 2026; sin análisis de código ni de dependencias confirmado</td>
                    </tr>
                    <tr>
                      <td data-label="Área"><strong>Inteligencia artificial</strong></td>
                      <td data-label="Capacidad actual">Licencias de Claude, créditos en OpenRouter y acceso a ChatGPT con Codex</td>
                      <td data-label="Brecha">Uso como chat, sin método ni política, y con condiciones de datos por definir</td>
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

          <!-- Slide 15: Puntos de fricción (Tabla 3.8) -->
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
                  <caption>Tabla 3.8 — Puntos de fricción del acta 01 con el dato que los sustenta</caption>
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
                      <td data-label="Dato">Acta de 12 páginas: 4 criterios, 3 sistemas, 7 remisiones abiertas (A7)</td>
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
                      <td data-label="Dato">0 arquitectos; 5 patrones de carpetas en el front-end (A9)</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>F-05</strong></td>
                      <td data-label="Fricción">La calidad se valida al final</td>
                      <td data-label="Efecto">Defectos cerca de producción</td>
                      <td data-label="Dato">Validación en preproducción; 43 de 53 pruebas en un módulo (A9)</td>
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
              <div class="fit-grid" style="flex:1 1 auto;min-height:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));gap:14px;align-items:start;">
                <figure style="margin:0;display:flex;flex-direction:column;min-height:0;min-width:0;">
                  <svg style="flex:1 1 auto;min-height:0;" viewBox="0 0 520 372" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Línea base de madurez de nueve dimensiones: nivel actual de ATENEA frente al nivel objetivo al cierre del contrato, en una escala de 1 a 5">
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
                  <figcaption class="fig-caption">Tabla 3.9 — Línea base de madurez por dimensión (niveles CMMI 1 a 5) y nivel objetivo al cierre del contrato</figcaption>
                </figure>
                <figure style="margin:0;min-height:0;min-width:0;overflow:auto;">
                  <div class="data-table-wrapper">
                    <table class="data-table" style="font-size:clamp(0.72rem,min(0.98vw,1.75vh),1.5rem);">
                      <caption>Tabla 3.10 — Métricas DORA: situación actual y dato que debe aportar ATENEA</caption>
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

          <!-- Slide 18: Matriz de riesgos (Tabla 3.11) [c1-riesgos] -->
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
                  <caption>Tabla 3.11 — Matriz de riesgos técnicos, versión condensada (P: probabilidad; I: impacto; V = P + I); el informe añade tratamiento y responsable</caption>
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

          <!-- Slide 19: Inventario de datos (Tabla 3.12) [c1-datos] -->
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
                  <caption>Tabla 3.12 — Inventario de sistemas y fuentes de datos, con su clasificación y su uso permitido por los agentes de IA</caption>
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
                      <td data-label="Tecnología">Plataforma de formación</td>
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
                <h2 style="margin-bottom:4px;">Caso de uso priorizado: de tres candidatos a Campus 2600 en Hēma</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">La minuta encarga identificar y priorizar el caso de uso (obligación 5). ATENEA eligió Campus 2600 en Hēma el 23 de octubre y lo acotó a la primera transición el 30 de octubre (R5, R6).</p>
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
              <text x="720" y="109" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">de inconsistencias (A2)</text>
              <text x="720" y="126" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14"></text>
              <text x="720" y="143" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14"></text>
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
              <text x="30" y="516" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Elegido: Campus 2600 en Hēma el 23 de octubre (R5), acotado el 30 de octubre a la primera transición (R6).</text>
              </svg>
              <p class="fig-caption" style="margin:0;padding:2px 10px 0;font-size:clamp(0.78rem,0.95vw,0.95rem);">Círculo punteado: sin valorar; el informe propone los criterios, pero no puntúa a cada candidato.</p>
              <div class="mobile-alt">
                <p class="sched-title">Candidatos y criterios</p>
                <p class="sched-sub">ATENEA eligió Campus 2600 en Hēma (R5, R6).</p>
                <ol class="slide-list" style="margin:8px 0;">
                  <li><strong>Servicio unificado con Keycloak:</strong> usuarios, roles y permisos de SICORE Posmedia y SICORE CTeI; la líder del equipo lo consideró probable.</li>
                  <li><strong>Creación de terceros, SICORE Posmedia:</strong> recomendado en el análisis de inconsistencias.</li>
                  <li><strong>SICORE, HEMA o Academia Atenea:</strong> opción general planteada por ATENEA; de ella salió Campus 2600 en Hēma.</li>
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
              <figcaption class="fig-caption">Fuente: §5.4. Caso de uso institucional: tres candidatos y siete criterios de selección (sin tabla ni figura numerada en el informe)</figcaption>
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

          <!-- Slide E2-5.1: Fases y artefactos (1/2, Tabla 4.1) [c2-fases] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-fases">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Fases y artefactos (1/2): qué hace el flujo agéntico y qué decide la persona</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Cada etapa de ATENEA tiene un comando conectado al flujo; Descomponer y Traducir no existen hoy. Aquí, de entender a traducir.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.62rem,min(0.95vw,1.55vh),1.5rem);">
                  <caption>Tabla 4.1 — Intervención agéntica por etapa: brecha que atiende, función del flujo, decisión humana y resultado (1/2, texto condensado)</caption>
                  <thead>
                    <tr>
                      <th style="width:10%;font-size:0.82em;">Etapa actual</th>
                      <th style="width:9%;font-size:0.82em;">Fase</th>
                      <th style="width:12%;font-size:0.82em;">Brecha que atiende</th>
                      <th style="width:30%;font-size:0.82em;">¿Qué hace el flujo agéntico?</th>
                      <th style="width:21%;font-size:0.82em;">Decisión humana</th>
                      <th style="font-size:0.82em;">Resultado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Etapa actual">Levantamiento con el cliente</td>
                      <td data-label="Fase"><strong>Entender</strong></td>
                      <td data-label="Brecha que atiende">Requerimiento extenso sin estructura</td>
                      <td data-label="¿Qué hace el flujo agéntico?">Propone una especificación con requisitos numerados, supuestos marcados y preguntas de aclaración a partir de las notas y el diseño validado; en un sistema existente, acota el área de código</td>
                      <td data-label="Decisión humana">El líder de producto fija intención y alcance y resuelve las preguntas</td>
                      <td data-label="Resultado">Especificación de requisitos, para aprobación</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Especificación y validación de diseño</td>
                      <td data-label="Fase"><strong>Decidir</strong></td>
                      <td data-label="Brecha que atiende">Decisiones técnicas sin registro</td>
                      <td data-label="¿Qué hace el flujo agéntico?">Redacta la arquitectura y la experiencia: servicios a reutilizar, modelo de datos, integraciones y restricciones; contrasta la arquitectura declarada con la real</td>
                      <td data-label="Decisión humana">El líder de producto aprueba la especificación y sus criterios; la líder técnica y base de datos aprueban las decisiones técnicas</td>
                      <td data-label="Resultado">Especificación aprobada y arquitectura vinculante, en el repositorio</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">No existe</td>
                      <td data-label="Fase"><strong>Descomponer</strong></td>
                      <td data-label="Brecha que atiende">Sin desglose ni criterios por unidad</td>
                      <td data-label="¿Qué hace el flujo agéntico?">Propone épicas e historias que una persona puede terminar, con criterios de aceptación y los requisitos que cubren; calcula olas de trabajo paralelo según las dependencias</td>
                      <td data-label="Decisión humana">El líder de producto aprueba las historias; lo de bajo riesgo puede iniciarse con aprobación parcial explícita</td>
                      <td data-label="Resultado">Historias estimables y plan de olas; estimación por historia, no por requerimiento completo</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">No existe</td>
                      <td data-label="Fase"><strong>Traducir</strong></td>
                      <td data-label="Brecha que atiende">Estándar dependiente de cada persona</td>
                      <td data-label="¿Qué hace el flujo agéntico?">Genera, de forma determinista, un contrato verificable por historia con las reglas del proyecto y registra la traza requisito, historia y contrato</td>
                      <td data-label="Decisión humana">El desarrollador revisa el contrato; si está mal, se corrige la historia y se regenera</td>
                      <td data-label="Resultado">Contratos verificables; los escenarios son los casos de prueba</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- Slide E2-5.2: Fases y artefactos (2/2, Tabla 4.1) [c2-fases] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e2" data-item="c2-fases">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">3 &middot; Metodología SDLC-IA (E2)</p>
                <h2 style="margin-bottom:4px;">Fases y artefactos (2/2): qué hace el flujo agéntico y qué decide la persona</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">De construir a cerrar, más las dos filas que atraviesan todo el ciclo: seguimiento e incidentes y cambios.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.62rem,min(0.95vw,1.55vh),1.5rem);">
                  <caption>Tabla 4.1 — Intervención agéntica por etapa: brecha que atiende, función del flujo, decisión humana y resultado (2/2, texto condensado)</caption>
                  <thead>
                    <tr>
                      <th style="width:10%;font-size:0.82em;">Etapa actual</th>
                      <th style="width:9%;font-size:0.82em;">Fase</th>
                      <th style="width:12%;font-size:0.82em;">Brecha que atiende</th>
                      <th style="width:30%;font-size:0.82em;">¿Qué hace el flujo agéntico?</th>
                      <th style="width:21%;font-size:0.82em;">Decisión humana</th>
                      <th style="font-size:0.82em;">Resultado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Etapa actual">Desarrollo</td>
                      <td data-label="Fase"><strong>Construir</strong></td>
                      <td data-label="Brecha que atiende">Código heterogéneo; calidad validada al final</td>
                      <td data-label="¿Qué hace el flujo agéntico?">Carga reglas, arquitectura, memoria y grafo del código y construye una historia a la vez: código y una prueba por escenario; lo que aparezca fuera de la historia pasa por control de cambios</td>
                      <td data-label="Decisión humana">El desarrollador revisa y ajusta; la líder técnica aprueba la integración a ramas protegidas</td>
                      <td data-label="Resultado">Rama con código y pruebas verificadas antes de integrar</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Compilados a infraestructura</td>
                      <td data-label="Fase"><strong>Cerrar</strong></td>
                      <td data-label="Brecha que atiende">Sin traza ni línea base</td>
                      <td data-label="¿Qué hace el flujo agéntico?">Valida el contrato en modo estricto, lo archiva como línea base y actualiza la memoria del proyecto y el tablero</td>
                      <td data-label="Decisión humana">Infraestructura despliega en cada ambiente; negocio valida en preproducción</td>
                      <td data-label="Resultado">Traza especificación, código y pruebas; línea base para medir cambios</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Transversal · hoy: no existe</td>
                      <td data-label="Fase"><strong>Seguimiento</strong></td>
                      <td data-label="Brecha que atiende">Plazos sin sustento</td>
                      <td data-label="¿Qué hace el flujo agéntico?">Interpreta el tablero: requisitos, historias, contratos, tareas y esfuerzo por etapa; enruta incidencias</td>
                      <td data-label="Decisión humana">Prioridades y compromisos del líder de producto y la dirección</td>
                      <td data-label="Resultado">Avance real por historia</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa actual">Transversal</td>
                      <td data-label="Fase"><strong>Incidentes y cambios</strong></td>
                      <td data-label="Brecha que atiende">Cambios tardíos absorbidos por desarrollo</td>
                      <td data-label="¿Qué hace el flujo agéntico?">Clasifica el alcance de un cambio antes de tocar archivos y regenera solo lo afectado; corrige defectos sin abrir el alcance</td>
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
                <h2 style="margin-bottom:4px;">Organización del equipo</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El método reparte responsabilidades entre los roles que ATENEA ya tiene; ATENEA debe definir la dedicación de cada rol al designar su equipo (obligación 5 de la Agencia).</p>
              </div>
              <svg viewBox="0 0 1200 500" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tres responsabilidades que se formalizan y regla de trabajo entre la Universidad y ATENEA">
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
              <text x="632" y="200" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">Un desarrollador por equipo instala y actualiza el arnés y atiende sus</text>
              <text x="632" y="219" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15">diagnósticos.</text>
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
                  <li><strong>Referente del arnés:</strong> Un desarrollador por equipo instala y actualiza el arnés y atiende sus diagnósticos.</li>
                  <li><strong>Aprobación de historias:</strong> El líder de producto aprueba las historias y sus criterios antes de traducirlas a contratos; la firma del acta deja de llegar después de iniciada la construcción (RT-06).</li>
                  <li><strong>Regla de trabajo (14 de octubre):</strong> la Universidad propone la metodología y las herramientas y ATENEA valida. Durante el contrato la Universidad opera el arnés junto al equipo; al cierre, la operación queda en ATENEA (componente C8).</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Fuente: §4.3 — Tres responsabilidades que se formalizan (sin figura ni tabla numerada en el informe)</figcaption>
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
                  <strong>Siglas de los roles:</strong> <strong>PO</strong> líder de producto (<em>Product Owner</em>); <strong>UX</strong> diseño de experiencia de usuario (<em>User Experience</em>); <strong>LT</strong> líder del equipo (<em>Team Lead</em>); <strong>BD</strong> base de datos; <strong>Dev</strong> desarrolladores; <strong>Inf</strong> infraestructura; <strong>Seg</strong> seguridad; <strong>TIC</strong> Subgerencia de Tecnologías de la Información y las Comunicaciones; <strong>UN</strong> Universidad Nacional de Colombia durante el contrato.
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
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Líder de producto (Product Owner)">PO</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Diseño de experiencia de usuario (User Experience)">UX</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Líder del equipo (Team Lead)">LT</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Base de datos">BD</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Desarrolladores">Dev</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Infraestructura">Inf</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Seguridad">Seg</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Subgerencia de Tecnologías de la Información y las Comunicaciones">TIC</abbr></th>
                      <th style="width:8.3%;font-size:0.82em;text-align:center;"><abbr title="Universidad Nacional de Colombia durante el contrato">UN</abbr></th>
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
              <text x="16" y="142" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">stack; salen de la documentación de</text>
              <text x="16" y="164" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">requerimientos existente y de</text>
              <text x="16" y="186" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">entrevistas con el equipo.</text>
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
              <text x="422" y="120" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">y decisiones registradas; ingeniería</text>
              <text x="422" y="142" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">inversa asistida y validada por</text>
              <text x="422" y="164" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">el equipo.</text>
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
              <text x="828" y="98" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">¿Qué se hizo, por qué, qué falló y qué</text>
              <text x="828" y="120" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17">falta? La genera el flujo desde el</text>
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
                  <li><strong>Reglas y negocio.</strong> Reglas de cada sistema, glosario, normativa, convenciones y versiones del stack; salen de la documentación de requerimientos existente y de entrevistas con el equipo. <em>Fases:</em> Entender, Decidir, Construir. <em>¿Dónde vive?</em> Documento de arquitectura base del repositorio, que manda sobre los valores por defecto del agente.</li>
                  <li><strong>Arquitectura.</strong> Módulos, integraciones, modelo de datos y decisiones registradas; ingeniería inversa asistida y validada por el equipo. <em>Fases:</em> Decidir, Construir, cambios. <em>¿Dónde vive?</em> Arquitectura del proyecto y grafo del código, solo de código.</li>
                  <li><strong>Memoria.</strong> ¿Qué se hizo, por qué, qué falló y qué falta? La genera el flujo desde el primer caso de uso. <em>Fases:</em> Construir, Cerrar, cambios. <em>¿Dónde vive?</em> Memoria por proyecto dentro del repositorio.</li>
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
              <text x="14" y="130" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">Actas extensas sin historias,</text>
              <text x="14" y="150" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">sin criterios y sin vínculo</text>
              <text x="14" y="170" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16">con el código.</text>
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
                  <li><span class="pill pill--partial">Brecha</span> <strong>Requerimientos sin desglose.</strong> Actas extensas sin historias, sin criterios y sin vínculo con el código.<br><span class="pill pill--ok">Metodología</span> <strong>Descomponer y Traducir.</strong> Épicas e historias con criterios de aceptación; un contrato verificable por historia; traza requisito, historia, contrato.<br><span class="pill pill--ok">Resultado</span> Historias estimables y traza hasta el código; evidencia para auditoría.</li>
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

          <!-- E3-1: Composición de la propuesta (Figura 5.1) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Composición de la propuesta: integrarse con las herramientas de ATENEA, no sustituirlas</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El arnés de agentes de IA coordina las herramientas por etapa y entrega a cada una el artefacto que necesita; su forma de uso (línea de comandos, conexión a una plataforma existente o plataforma propia) se define con ATENEA durante el contrato.</p>
              </div>
              <svg viewBox="-6 -6 1212 572" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figura 5.1: composición de la propuesta con herramientas de ATENEA arriba y abajo y el arnés principal en el centro">
<defs><marker id="f51-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker><marker id="f51-r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#B71C1C" /></marker><marker id="f51-g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#1E5631" /></marker></defs>
<rect x="20" y="0" width="360" height="62" rx="7" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.6" />
<text x="200.0" y="25" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Gestor documental</text>
<text x="200.0" y="46" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">de ATENEA</text>
<rect x="420" y="0" width="360" height="62" rx="7" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.6" />
<text x="600.0" y="25" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Herramienta de diseño</text>
<text x="600.0" y="46" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">de ATENEA</text>
<rect x="820" y="0" width="360" height="62" rx="7" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.6" />
<text x="1000.0" y="25" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Requisitos y tickets</text>
<text x="1000.0" y="46" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">sistema de ATENEA</text>
<path d="M200.0 64 V106" stroke="#2C6B87" stroke-width="1.8" marker-end="url(#f51-b)" />
<text x="210.0" y="90" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14">especificaciones aprobadas</text>
<path d="M600.0 64 V106" stroke="#2C6B87" stroke-width="1.8" marker-end="url(#f51-b)" />
<text x="610.0" y="90" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14">diseño validado</text>
<path d="M1000.0 64 V106" stroke="#2C6B87" stroke-width="1.8" marker-start="url(#f51-b)" marker-end="url(#f51-b)" />
<text x="1010.0" y="90" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14">integración</text>
<rect x="0" y="108" width="1200" height="270" rx="10" fill="#F0F7F2" stroke="#1E5631" stroke-width="2" />
<rect x="14" y="116" width="520" height="26" rx="5" fill="#1E5631" stroke="#1E5631" stroke-width="0" />
<text x="26" y="135" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Arnés principal para el ciclo de desarrollo (LIA UNAL)</text>
<rect x="20" y="150" width="360" height="76" rx="7" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.6" />
<text x="200.0" y="175" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Entorno agéntico</text>
<text x="200.0" y="196" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">integrable con CLI como Claude Code u</text>
<text x="200.0" y="213" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">OpenCode</text>
<rect x="420" y="150" width="360" height="76" rx="7" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.6" />
<text x="600.0" y="175" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Modelos</text>
<text x="600.0" y="196" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">definidos por tarea; validados con los</text>
<text x="600.0" y="213" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">accesos de ATENEA</text>
<rect x="820" y="150" width="360" height="76" rx="7" fill="#E3F0E7" stroke="#1E5631" stroke-width="1.6" />
<text x="1000.0" y="175" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Tablero de estado</text>
<text x="1000.0" y="196" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">avance por historia y etapa</text>
<rect x="20" y="238" width="360" height="62" rx="7" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.6" />
<text x="200.0" y="263" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Gestor de especificaciones</text>
<text x="200.0" y="284" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">PRD, historias y contratos</text>
<rect x="420" y="238" width="360" height="62" rx="7" fill="#E3F0E7" stroke="#1E5631" stroke-width="1.6" />
<text x="600.0" y="263" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Tejedor</text>
<text x="600.0" y="284" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">historia → contrato verificable; traza</text>
<rect x="820" y="238" width="360" height="62" rx="7" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.6" />
<text x="1000.0" y="263" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Memoria persistente</text>
<text x="1000.0" y="284" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">decisiones y mapa del código</text>
<rect x="20" y="316" width="1160" height="48" rx="7" fill="#E3F0E7" stroke="#1E5631" stroke-width="1.6" />
<text x="600" y="346" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">Comandos por etapa: entender, decidir, descomponer, traducir, construir, cerrar, cambios y estado</text>
<path d="M380 184 H416" stroke="#1E5631" stroke-width="1.8" marker-end="url(#f51-g)" />
<path d="M380 264 H416" stroke="#1E5631" stroke-width="1.8" marker-end="url(#f51-g)" />
<path d="M780 264 H816" stroke="#1E5631" stroke-width="1.8" marker-end="url(#f51-g)" />
<path d="M200.0 376 V438" stroke="#2C6B87" stroke-width="1.8" marker-end="url(#f51-b)" />
<text x="210.0" y="412" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14">código y pruebas por historia</text>
<rect x="20" y="440" width="360" height="62" rx="7" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.6" />
<text x="200.0" y="465" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Gestor de repositorios</text>
<text x="200.0" y="486" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">de ATENEA</text>
<rect x="420" y="440" width="360" height="62" rx="7" fill="#FFF7ED" stroke="#DFBD76" stroke-width="1.6" />
<text x="600.0" y="465" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Integración y entrega</text>
<text x="600.0" y="486" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">CI/CD de ATENEA (por definir)</text>
<rect x="820" y="440" width="360" height="62" rx="7" fill="#EDF1F7" stroke="#4E93B0" stroke-width="1.6" />
<text x="1000.0" y="465" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">Ambientes de ATENEA</text>
<text x="1000.0" y="486" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">QA, preproducción y producción</text>
<path d="M380 471 H416" stroke="#2C6B87" stroke-width="1.8" marker-end="url(#f51-b)" />
<path d="M780 471 H816" stroke="#2C6B87" stroke-width="1.8" marker-end="url(#f51-b)" />
<path d="M200.0 504 V528 H1000.0 V506" stroke="#B71C1C" stroke-width="1.8" stroke-dasharray="6,4" marker-end="url(#f51-r)" />
<text x="600" y="550" fill="#B71C1C" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700" text-anchor="middle">hoy: compilados entregados a mano a infraestructura</text>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Composición de la propuesta</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>Herramientas de ATENEA, por función:</strong> gestor documental, herramienta de diseño y sistema de requerimientos o tickets (arriba); gestor de repositorios, integración y entrega y ambientes (abajo).</li>
                  <li><strong>Arnés principal (LIA UNAL):</strong> entorno agéntico, modelos, tablero de estado, gestor de especificaciones, tejedor, memoria persistente y los comandos por etapa.</li>
                  <li><strong>Por decidir (ámbar):</strong> los modelos, que ATENEA definirá y a los que puede limitarse la herramienta de código (§5.3), y la integración y entrega (CI/CD).</li>
                  <li><strong>Entrega:</strong> hoy los compilados se entregan a mano a infraestructura.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 5.1 — Composición de la propuesta: arnés de agentes de IA como marco institucional de ATENEA. Verde: arnés principal; azul: herramientas de ATENEA o de terceros integradas; ámbar: por decidir</figcaption>
            </figure>
          </article>

          <!-- E3-2: Matriz de componentes 1/2 (Tabla 5.1) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Matriz de componentes (1/2): las siete piezas del arnés y su estado</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Verde: implementado o integrado; ámbar: por confirmar o en migración; gris: por definir o por construir. Las piezas propias del LIA UNAL están implementadas; entorno agéntico y modelos dependen de ATENEA.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.2vw,2.0vh),1.5rem);">
                  <caption>Tabla 5.1 — Componentes de la propuesta (1/2): función, herramienta que la cumple y estado</caption>
                  <thead>
                    <tr>
                      <th style="width:17%;font-size:0.82em;">Componente</th>
                      <th style="width:30%;font-size:0.82em;">Función</th>
                      <th style="width:29%;font-size:0.82em;">Herramienta</th>
                      <th style="font-size:0.82em;">Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Componente"><strong>Arnés principal</strong></td>
                      <td data-label="Función">Coordina las herramientas agénticas por etapa, fija las versiones de sus piezas, entrega los comandos al entorno agéntico y mantiene la traza</td>
                      <td data-label="Herramienta">Desarrollo del LIA UNAL</td>
                      <td data-label="Estado"><span class="pill pill--ok">Implementado</span> y probado fuera de ATENEA (capítulo 6); forma de uso por definir</td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Gestor de especificaciones</strong></td>
                      <td data-label="Función">PRD, arquitectura, épicas, historias, contratos y criterios de aceptación</td>
                      <td data-label="Herramienta">Componente de planeación y especificación de terceros, integrado al arnés</td>
                      <td data-label="Estado"><span class="pill pill--ok">Integrado</span> versión fijada por el arnés</td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Tejedor</strong></td>
                      <td data-label="Función">Convierte cada historia en un contrato verificable y registra la traza requisito, historia y contrato; calcula olas de trabajo</td>
                      <td data-label="Herramienta">Pieza propia del arnés</td>
                      <td data-label="Estado"><span class="pill pill--ok">Implementado</span></td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Memoria persistente</strong></td>
                      <td data-label="Función">Decisiones, aprendizajes y mapa del código, por proyecto y dentro del repositorio</td>
                      <td data-label="Herramienta">Componentes de memoria y de grafo de código de terceros, integrados</td>
                      <td data-label="Estado"><span class="pill pill--ok">Integrados</span> versiones fijadas</td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Tablero de estado</strong></td>
                      <td data-label="Función">Avance por requisito, historia, contrato y etapa</td>
                      <td data-label="Herramienta">Pieza propia del arnés</td>
                      <td data-label="Estado"><span class="pill pill--ok">Implementado</span></td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Entorno agéntico</strong></td>
                      <td data-label="Función">Ejecuta los comandos: lee, edita, prueba</td>
                      <td data-label="Herramienta">Integrable con entornos de línea de comandos como Claude Code u OpenCode</td>
                      <td data-label="Estado"><span class="pill pill--partial">Por confirmar</span> habilitación en ATENEA</td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Modelos</strong></td>
                      <td data-label="Función">Inferencia para el agente</td>
                      <td data-label="Herramienta">Modelo definido por la Universidad para la tarea de cada agente y validado con los accesos actuales de ATENEA; licencias, APIs y modelos como servicio los habilita la Agencia</td>
                      <td data-label="Estado"><span class="pill pill--todo">Por definir y habilitar</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-3: Matriz de componentes 2/2 (Tabla 5.1) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Matriz de componentes (2/2): las seis herramientas de ATENEA que el arnés integra</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El principio es integrarse con la herramienta que ya cumple cada función en la entidad: dos existen, otras dos existen y están en migración; la integración con requisitos y tickets está por construir y la integración y entrega, por definir.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.2vw,2.0vh),1.5rem);">
                  <caption>Tabla 5.1 — Componentes de la propuesta (2/2): función, herramienta que la cumple y estado</caption>
                  <thead>
                    <tr>
                      <th style="width:17%;font-size:0.82em;">Componente</th>
                      <th style="width:30%;font-size:0.82em;">Función</th>
                      <th style="width:29%;font-size:0.82em;">Herramienta</th>
                      <th style="font-size:0.82em;">Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Componente"><strong>Gestión documental</strong></td>
                      <td data-label="Función">Especificaciones aprobadas y evidencia</td>
                      <td data-label="Herramienta">Gestor documental de ATENEA</td>
                      <td data-label="Estado"><span class="pill pill--ok">Existente</span></td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Diseño</strong></td>
                      <td data-label="Función">Prototipos validados con el cliente</td>
                      <td data-label="Herramienta">Herramienta de diseño de ATENEA</td>
                      <td data-label="Estado"><span class="pill pill--ok">Existente</span></td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Requisitos y tickets</strong></td>
                      <td data-label="Función">Épicas, historias y tareas; estado del trabajo</td>
                      <td data-label="Herramienta">Sistema de gestión de requerimientos o tickets de ATENEA</td>
                      <td data-label="Estado"><span class="pill pill--todo">Por construir</span> integración</td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Repositorio de código</strong></td>
                      <td data-label="Función">Ramas, revisiones e integración</td>
                      <td data-label="Herramienta">Gestor de repositorios de ATENEA</td>
                      <td data-label="Estado"><span class="pill pill--partial">En migración</span> existente</td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Integración y entrega</strong></td>
                      <td data-label="Función">Compilación, pruebas y despliegue por ambiente</td>
                      <td data-label="Herramienta">Orquestador de <abbr title="Integración y entrega continuas">CI/CD</abbr> de ATENEA</td>
                      <td data-label="Estado"><span class="pill pill--todo">Por definir</span></td>
                    </tr>
                    <tr>
                      <td data-label="Componente"><strong>Ambientes</strong></td>
                      <td data-label="Función">QA, preproducción y producción</td>
                      <td data-label="Herramienta">Clúster de ATENEA</td>
                      <td data-label="Estado"><span class="pill pill--partial">En migración de nube</span> existentes</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-4: Caso de uso institucional (§5.4) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Caso de uso institucional: Campus 2600 en Hēma, primera transición (§5.4)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;">El caso es el <strong>banco de pruebas</strong> de Aracne-SDLC-AI y de la metodología SDLC-IA: sobre un desarrollo real de ATENEA se recorre el ciclo completo, de las historias de usuario al despliegue. En él conviven tres planos: lo que Hēma tiene hoy en operación, lo que muestra el prototipo de Campus 2600 y lo que entra en el alcance del contrato.</p>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><strong>Selección:</strong> el 23 de octubre de 2026 se escogió una necesidad priorizada por la dirección, representada en un prototipo visual con datos simulados (R5); el 30 de octubre se precisó: módulo Campus 2600 de la plataforma Hēma, del sistema <abbr title="Sistema de Información Core">SICORE</abbr> <abbr title="Ciencia, Tecnología e Innovación">CTeI</abbr>, limitado a los requerimientos ya definidos de la primera transición (R6).</p>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><strong>Alcance:</strong> sin los temas presupuestales, de monetización o aún no aprobados por el área funcional; el motor de emparejamiento de la segunda transición queda fuera. De Campus solo existe un prototipo interactivo, sin repositorio ni desarrollo. <strong>Insumos:</strong> grabación y transcripción del 30 de octubre, prototipo en Angular y acceso a la plataforma de interoperabilidad, que se pedirá por correo formal.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.2vw,2.0vh),1.5rem);">
                  <caption>Fuente: §5.4. Los siete criterios de la Universidad aplicados al módulo Campus 2600</caption>
                  <thead>
                    <tr>
                      <th style="width:26%;font-size:0.82em;">Criterio</th>
                      <th style="font-size:0.82em;">Cómo lo cumple Campus 2600</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Criterio"><strong>1. Valor institucional</strong></td>
                      <td data-label="Cómo lo cumple Campus 2600">Gestiona la asignación y la ejecución de servicios especializados que dos integradores prestan a emprendimientos y empresas de Bogotá</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio"><strong>2. Viabilidad en plazo y equipo</strong></td>
                      <td data-label="Cómo lo cumple Campus 2600">El prototipo interactivo contiene reglas de negocio ya definidas y John actúa como usuario funcional (R5, R6)</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio"><strong>3. Especificación y diseño</strong></td>
                      <td data-label="Cómo lo cumple Campus 2600">El prototipo muestra pantallas, flujo de navegación y formularios de postulación; no hay historias de usuario de Campus</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio"><strong>4. Verificabilidad y pruebas</strong></td>
                      <td data-label="Cómo lo cumple Campus 2600">Prerrequisitos por etapa, votación de los jurados, circuito de firmas y cálculo de brechas permiten contratos verificables y pruebas automatizadas</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio"><strong>5. Protección de datos</strong></td>
                      <td data-label="Cómo lo cumple Campus 2600">El prototipo usa datos simulados; los agentes no necesitan datos personales reales</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio"><strong>6. Aislamiento de la migración</strong></td>
                      <td data-label="Cómo lo cumple Campus 2600">Sus reglas funcionales no dependen de la migración de la infraestructura base</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio"><strong>7. Ciclo completo</strong></td>
                      <td data-label="Cómo lo cumple Campus 2600">Va de la postulación de la entidad a los informes de avance de los integradores, que el gestor valida o devuelve</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-4a: Hēma hoy (§5.4.1, Figura 5.3) -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <div class="slide-content">
              <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3) &middot; Caso de uso</p>
              <h2>Hēma hoy: plataforma sombrilla con cuatro estrategias (§5.4.1)</h2>
              <ul class="slide-list">
                <li><strong>Hēma</strong> mapea y articula a los actores de ciencia, tecnología e innovación de Bogotá, y la lidera ATENEA (R6).</li>
                <li>Reúne <strong>cuatro estrategias</strong>: Ecosistema caracteriza a las entidades y alimenta el directorio de actores; BankPro acompaña a los investigadores en sus postulaciones; las otras dos son Internacionalización y Campus 2600.</li>
                <li>Comparte <strong>servicios</strong> que cada vertical reutiliza: identidad, datos y <abbr title="Interfaces de programación de aplicaciones">API</abbr>, analítica y convocatorias (A12, A13).</li>
                <li>En la <strong>versión 2.1.5 de pruebas</strong> funcionan la biblioteca de recursos, los formularios de caracterización, BankPro, los catálogos paramétricos, la administración de usuarios, estrategias y roles, y los reportes de diligenciamiento (P9).</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <img data-src="assets/images/caso-uso/20-hema-real-bankpro.webp" width="1600" height="888" decoding="async" loading="lazy" alt="Hēma versión 2.1.5 en el ambiente de pruebas: módulo BankPro con el buscador de convocatorias y el acompañamiento en seis pasos" />
              <figcaption class="fig-caption">Figura 5.3. Hēma versión 2.1.5, ambiente de pruebas; datos de identificación ocultos. Módulo BankPro, cuyo componente de convocatorias compartirá Campus 2600</figcaption>
            </figure>
          </article>

          <!-- E3-4b: Campus 2600 dentro de Hēma (§5.4.2, Figuras 5.4 a 5.6) -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <div class="slide-content">
              <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3) &middot; Caso de uso</p>
              <h2>Campus 2600 dentro de Hēma: una estrategia registrada, sin pantallas de su proceso (§5.4.2)</h2>
              <ul class="slide-list">
                <li><strong>Campus 2600</strong> es una convocatoria interna de ATENEA dirigida a tres tipologías de actores, con un presupuesto para cada una (R6).</li>
                <li>Los servicios a los beneficiarios los prestan dos integradores, <strong>Ceiba y Connect</strong>, que tienen los convenios con las entidades oferentes.</li>
                <li>Comparte con BankPro el <strong>componente de convocatorias</strong>; la diferencia es que las de BankPro son de terceros.</li>
                <li>En Hēma 2.1.5 figura como <strong>estrategia activa</strong> con sus roles, pero no hay pantallas de postulación, evaluación, diagnóstico ni hoja de ruta. Su proceso solo existe en un prototipo en Angular.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div style="flex:1 1 auto;min-height:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:8px;align-content:start;">
                <figure style="margin:0;min-width:0;display:flex;flex-direction:column;gap:4px;">
                  <img data-src="assets/images/caso-uso/21-hema-real-estrategias.webp" width="1600" height="888" decoding="async" loading="lazy" style="height:auto;" alt="Hēma versión 2.1.5, Estrategias y roles: Campus 2600, Ecosistema CTeI, BankPro e Internacionalización aparecen activas" />
                  <figcaption class="fig-caption">Figura 5.4. Hēma versión 2.1.5, ambiente de pruebas; datos de identificación ocultos. Estrategias y roles</figcaption>
                </figure>
                <figure style="margin:0;min-width:0;display:flex;flex-direction:column;gap:4px;">
                  <img data-src="assets/images/caso-uso/08-hema-convocatoria-campus2600.webp" width="1600" height="900" decoding="async" loading="lazy" style="height:auto;" alt="Prototipo de Campus 2600: convocatoria con las tipologías EBCT, EAI y MiPymes y sus topes" />
                  <figcaption class="fig-caption">Figura 5.5. Prototipo de referencia, con datos simulados. Convocatoria y tipologías</figcaption>
                </figure>
                <figure style="margin:0;min-width:0;display:flex;flex-direction:column;gap:4px;">
                  <img data-src="assets/images/caso-uso/07-hema-directorio-actores.webp" width="1600" height="900" decoding="async" loading="lazy" style="height:auto;" alt="Prototipo de Campus 2600: directorio de actores y oferta de servicios especializados" />
                  <figcaption class="fig-caption">Figura 5.6. Prototipo de referencia, con datos simulados. Directorio de actores y servicios</figcaption>
                </figure>
              </div>
            </figure>
          </article>

          <!-- E3-4c: Lo que hay que construir (§5.4.2, Figuras 5.8 a 5.11) -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <div class="slide-content">
              <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3) &middot; Caso de uso</p>
              <h2>Lo que hay que construir: el proceso que hoy solo está en el prototipo (§5.4.2)</h2>
              <ul class="slide-list">
                <li><strong>Sin desarrollar</strong> están la postulación en dos operaciones, la evaluación técnica con panel de jurados, la formalización, el autodiagnóstico y el diagnóstico, la hoja de ruta con su circuito de firmas y el plan de trabajo con los informes de avance (R6).</li>
                <li>Además de las entidades, en un caso específico puede postularse una <strong>persona natural</strong>.</li>
                <li>En la hoja de ruta, <strong>cada rol ve una parte</strong>: el postulante no ve el valor de los servicios, el financiero de ATENEA los ve todos con su valor y cada integrador solo los suyos.</li>
                <li>Una entidad puede tener <strong>varias hojas de ruta parciales</strong> cuando una brecha es prerrequisito de otras, y cada una se formula sobre la <strong>versión aprobada del directorio</strong> en ese momento.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div style="flex:1 1 auto;min-height:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:8px;align-content:start;">
                <figure style="margin:0;min-width:0;display:flex;flex-direction:column;gap:4px;">
                  <img data-src="assets/images/caso-uso/11-hema-mesa-calificacion.webp" width="1600" height="900" decoding="async" loading="lazy" style="height:auto;" alt="Prototipo de Campus 2600: mesa de calificación técnica y verificación de antecedentes legales" />
                  <figcaption class="fig-caption">Figura 5.8. Mesa de calificación técnica</figcaption>
                </figure>
                <figure style="margin:0;min-width:0;display:flex;flex-direction:column;gap:4px;">
                  <img data-src="assets/images/caso-uso/13-hema-diagnostico-brechas.webp" width="1600" height="900" decoding="async" loading="lazy" style="height:auto;" alt="Prototipo de Campus 2600: diagnóstico de brechas con el cálculo del Delta y la criticidad" />
                  <figcaption class="fig-caption">Figura 5.9. Diagnóstico de brechas</figcaption>
                </figure>
                <figure style="margin:0;min-width:0;display:flex;flex-direction:column;gap:4px;">
                  <img data-src="assets/images/caso-uso/14-hema-hoja-ruta-presupuesto.webp" width="1600" height="900" decoding="async" loading="lazy" style="height:auto;" alt="Prototipo de Campus 2600: hoja de ruta con control de topes y asignación de integradores" />
                  <figcaption class="fig-caption">Figura 5.10. Hoja de ruta y topes</figcaption>
                </figure>
                <figure style="margin:0;min-width:0;display:flex;flex-direction:column;gap:4px;">
                  <img data-src="assets/images/caso-uso/16-hema-firmas-hash.webp" width="1600" height="900" decoding="async" loading="lazy" style="height:auto;" alt="Prototipo de Campus 2600: circuito de firmas con hash y compuertas de devolución" />
                  <figcaption class="fig-caption">Figura 5.11. Circuito de firmas con hash</figcaption>
                </figure>
              </div>
              <figcaption class="fig-caption">Figuras 5.8 a 5.11. Prototipo de referencia, con datos simulados</figcaption>
            </figure>
          </article>

          <!-- E3-4d: Delimitación y solicitudes (§5.4.3, Tablas 5.2 y 5.3) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3) &middot; Caso de uso</p>
                <h2 style="margin-bottom:4px;">Delimitación del caso y solicitudes a ATENEA (§5.4.3)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;">El alcance abarca lo ya definido para Campus, sin los temas presupuestales, de monetización o aún no aprobados por el área funcional (R6). Queda abierto el control de topes, que quien presentó el prototipo señaló como el mayor cuello de botella del módulo. Las solicitudes irán por correo formal a Ronald.</p>
              </div>
              <div style="flex:1 1 auto;min-height:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:10px;">
                <div class="data-table-wrapper" style="min-height:0;height:auto;">
                  <table class="data-table" style="font-size:clamp(0.64rem,min(1.05vw,1.9vh),1.4rem);">
                    <caption>Tabla 5.2. Delimitación del caso Campus 2600: parte del proceso y situación (las seis partes «Dentro» se presentaron en el prototipo, R6)</caption>
                    <thead>
                      <tr>
                        <th style="width:70%;font-size:0.82em;">Parte del proceso</th>
                        <th style="font-size:0.82em;">Situación</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td data-label="Parte del proceso">Directorio de actores y servicios de Campus, con versiones aprobadas</td><td data-label="Situación"><span class="pill pill--ok">Dentro</span></td></tr>
                      <tr><td data-label="Parte del proceso">Postulación en dos operaciones con revisión del gestor</td><td data-label="Situación"><span class="pill pill--ok">Dentro</span></td></tr>
                      <tr><td data-label="Parte del proceso">Evaluación técnica, panel de jurados y <abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr> en paralelo</td><td data-label="Situación"><span class="pill pill--ok">Dentro</span></td></tr>
                      <tr><td data-label="Parte del proceso">Formalización, autodiagnóstico, diagnóstico y cálculo de Δ</td><td data-label="Situación"><span class="pill pill--ok">Dentro</span></td></tr>
                      <tr><td data-label="Parte del proceso">Hoja de ruta, hojas parciales, visibilidad por rol y firmas con hash</td><td data-label="Situación"><span class="pill pill--ok">Dentro</span></td></tr>
                      <tr><td data-label="Parte del proceso">Plan de trabajo e informes de avance de los integradores</td><td data-label="Situación"><span class="pill pill--ok">Dentro</span></td></tr>
                      <tr><td data-label="Parte del proceso">Control de topes por tipología y del reparto entre integradores (solicitud 1)</td><td data-label="Situación"><span class="pill pill--partial">Por confirmar</span></td></tr>
                      <tr><td data-label="Parte del proceso">Otros temas presupuestales y monetización: sin definición del área funcional</td><td data-label="Situación"><span class="pill pill--todo">Fuera</span></td></tr>
                      <tr><td data-label="Parte del proceso">Integración con sistemas financieros externos: interfaces simuladas verificables</td><td data-label="Situación"><span class="pill pill--todo">Fuera</span></td></tr>
                      <tr><td data-label="Parte del proceso">Motor de emparejamiento de oferta y demanda: segunda transición de Hēma</td><td data-label="Situación"><span class="pill pill--todo">Fuera</span></td></tr>
                    </tbody>
                  </table>
                </div>
                <div class="data-table-wrapper" style="min-height:0;height:auto;">
                  <table class="data-table" style="font-size:clamp(0.64rem,min(1.05vw,1.9vh),1.4rem);">
                    <caption>Tabla 5.3. Solicitudes a ATENEA para cerrar la delimitación del caso Campus 2600 (texto condensado)</caption>
                    <thead>
                      <tr>
                        <th style="width:6%;font-size:0.82em;">N.º</th>
                        <th style="width:52%;font-size:0.82em;">Qué se necesita de ATENEA</th>
                        <th style="font-size:0.82em;">Para qué</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td data-label="N.º"><strong>1</strong></td><td data-label="Qué se necesita">Decidir si el control de topes por tipología y del reparto entre Ceiba y Connect entra en el caso</td><td data-label="Para qué">Incluir o retirar las historias de hoja de ruta que dependen de esas reglas</td></tr>
                      <tr><td data-label="N.º"><strong>2</strong></td><td data-label="Qué se necesita">Validar las 14 historias reconstruidas por la Universidad</td><td data-label="Para qué">Fijar el alcance que se implementará en los componentes 5 y 6</td></tr>
                      <tr><td data-label="N.º"><strong>3</strong></td><td data-label="Qué se necesita">Entregar el prototipo de Campus en Angular, como código o con acceso</td><td data-label="Para qué">Tomar de primera mano las reglas ya acordadas</td></tr>
                      <tr><td data-label="N.º"><strong>4</strong></td><td data-label="Qué se necesita">Indicar las reglas de postulación de una persona natural</td><td data-label="Para qué">Ajustar la historia de postulación y sus criterios</td></tr>
                      <tr><td data-label="N.º"><strong>5</strong></td><td data-label="Qué se necesita">Compartir los catálogos de Ceiba y Connect y la plantilla de variables de Ecosistema</td><td data-label="Para qué">Diseñar la carga masiva del directorio y sus versiones</td></tr>
                      <tr><td data-label="N.º"><strong>6</strong></td><td data-label="Qué se necesita">Dar acceso a la carpeta de SharePoint <em>Nuevas historias de usuario</em> que enlaza la arquitectura empresarial (A11)</td><td data-label="Para qué">Reutilizar el componente de convocatorias sin duplicarlo</td></tr>
                      <tr><td data-label="N.º"><strong>7</strong></td><td data-label="Qué se necesita">Confirmar si Campus se integrará sobre el ambiente de pruebas de Hēma consultado (P9)</td><td data-label="Para qué">Preparar el entorno de integración del caso</td></tr>
                      <tr><td data-label="N.º"><strong>8</strong></td><td data-label="Qué se necesita">Definir cómo se incorporan los cambios que surjan de la validación con el área funcional</td><td data-label="Para qué">Mantener alineadas las historias</td></tr>
                      <tr><td data-label="N.º"><strong>9</strong></td><td data-label="Qué se necesita">Validar los candidatos del estudio de referentes que aplican a Campus 2600 (Tabla 5.5)</td><td data-label="Para qué">Decidir si entran como historias del caso o quedan para Hēma</td></tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </figure>
          </article>

          <!-- E3-4e: Qué hace el agente CTeI (§6.10, Tabla 6.7) -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e3" data-tone="emerald" data-caption-source="§6.10">
            <div class="slide-content">
              <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3) &middot; Referentes CTeI</p>
              <h2>El agente de investigación CTeI: un estudio de referentes antes del brief</h2>
              <ul class="slide-list">
                <li><strong><code>aracne-ctei-scout</code></strong> prepara estudios de base tecnológica sobre plataformas, software, patentes y artículos de los mercados local, nacional, latinoamericano e internacional.</li>
                <li>Corre en la fase <strong>Entender</strong> de <code>/sw:new</code>, antes del brief de producto. Deja un <code>research-brief.md</code> con requisitos, épicas e historias candidatas, que el equipo de requerimientos de ATENEA acepta o descarta.</li>
                <li>Es <strong>opcional</strong>: está construido, no hace parte del paquete 0.9.0 y entra en la versión siguiente del arnés.</li>
                <li>Los datos del panorama se exploran en el tablero público <a href="https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion" target="_blank" rel="noopener" style="overflow-wrap:anywhere;">https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion</a>.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.68rem,min(1.15vw,2.1vh),1.5rem);">
                  <caption>Fuente: §6.10 y Tabla 6.7. El agente de investigación CTeI y su servidor MCP</caption>
                  <thead>
                    <tr><th style="width:24%;">Pieza</th><th>Qué es</th></tr>
                  </thead>
                  <tbody>
                    <tr><td data-label="Pieza"><strong>Dónde entra</strong></td><td data-label="Qué es">Antes del brief de producto (<code>bmad-product-brief</code>); alimenta el <abbr title="Product Requirements Document (documento de requisitos de producto)">PRD</abbr>, las épicas y las historias</td></tr>
                    <tr><td data-label="Pieza"><strong>Servidor <abbr title="Model Context Protocol">MCP</abbr></strong></td><td data-label="Qué es"><code>ctei-landscape</code>, paquete 0.1.0 en un repositorio público (P10); sin versión fijada todavía</td></tr>
                    <tr><td data-label="Pieza"><strong>Siete herramientas</strong></td><td data-label="Qué es"><code>search_landscape</code> (por tipo y por alcance), <code>get_entry</code>, <code>related_entries</code>, <code>actor_service_matrix</code>, <code>coverage_gaps</code>, <code>taxonomy</code> y <code>export_to_insumos</code></td></tr>
                    <tr><td data-label="Pieza"><strong>Instalar el agente</strong></td><td data-label="Qué es"><code style="overflow-wrap:anywhere;">aracne-sdlc-ai init --only research</code></td></tr>
                    <tr><td data-label="Pieza"><strong>Instalar el MCP</strong></td><td data-label="Qué es"><code style="overflow-wrap:anywhere;">uvx --from git+https://github.com/LIAUNAL/panoramaPlataformasCTeI ctei-landscape-mcp</code></td></tr>
                    <tr><td data-label="Pieza"><strong>Ficha CT000</strong></td><td data-label="Qué es">Resume la conceptualización vigente de Hēma; es privada, se queda con ATENEA y el servidor la lee desde <code>CTEI_REFERENCE_PATH</code></td></tr>
                    <tr><td data-label="Pieza"><strong>Trazabilidad</strong></td><td data-label="Qué es">Cada afirmación que llega al PRD o a una historia cita el identificador de su ficha</td></tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-4f: La campaña de referentes (§5.4.4) -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e3" data-tone="emerald" data-caption-source="§5.4.4">
            <div class="slide-content">
              <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3) &middot; Referentes CTeI</p>
              <h2>La campaña de referentes: 121 fichas en cinco corridas (§5.4.4)</h2>
              <ul class="slide-list">
                <li>La reunión del 30 de octubre dejó una <strong>pregunta para el caso</strong> (R7): ¿qué actores, servicios o interacciones tienen otras plataformas CTeI que Hēma no contempla?</li>
                <li>El <strong>1 de noviembre de 2026</strong> el laboratorio hizo cinco corridas de búsqueda que dejaron 121 fichas: 35 plataformas, 34 patentes, 19 artículos, 8 programas de software y 25 de otros tipos (P10).</li>
                <li>Por <strong>alcance</strong>, 9 son de Bogotá, 19 nacionales, 33 de América Latina y 60 internacionales.</li>
                <li>Tiene <strong>límites</strong>: la mayoría de las patentes son de China, Estados Unidos y Europa, y no hay fichas de software latinoamericano.</li>
                <li>Tablero público: <a href="https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion" target="_blank" rel="noopener" style="overflow-wrap:anywhere;">https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion</a></li>
              </ul>
            </div>
            <figure class="slide-figure">
              <img data-src="assets/images/caso-uso/panorama-ctei-constelacion.webp" width="1600" height="1100" decoding="async" loading="lazy" alt="Tablero público del panorama de plataformas CTeI en la pestaña Constelación 3D: cada referente es un sistema con sus planetas de alcance, tipo, tema, clúster, actor, interacción y servicio" />
              <figcaption class="fig-caption">Fuente: §5.4.4. Tablero público del panorama CTeI, vista Constelación 3D (captura del 3 de noviembre de 2026)</figcaption>
            </figure>
          </article>

          <!-- E3-4g: Clústeres y Campus 2600 (§5.4.4, Tabla 5.4) -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e3" data-tone="emerald">
            <div class="slide-content">
              <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3) &middot; Referentes CTeI</p>
              <h2>Seis clústeres temáticos y su relación con Campus 2600 (§5.4.4)</h2>
              <ul class="slide-list">
                <li>Las 121 fichas se agrupan en <strong>seis clústeres</strong>, ordenados por número de fichas.</li>
                <li>La columna de relación con Campus 2600 es una <strong>lectura de la Universidad</strong>.</li>
                <li>El panorama incluye la convocatoria pública del caso como ficha <strong>CT101</strong>, «2600 Campus: convocatoria 2600 Generación Llega Alto», y a uno de sus integradores como <strong>CT100</strong>, «Connect Bogotá Región».</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.68rem,min(1.15vw,2.1vh),1.5rem);">
                  <caption>Tabla 5.4. Clústeres temáticos del panorama CTeI y su relación con Campus 2600. Panorama: <a href="https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion" target="_blank" rel="noopener" style="overflow-wrap:anywhere;">https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion</a></caption>
                  <thead>
                    <tr><th style="width:44%;">Clúster</th><th style="width:10%;">Fichas</th><th>Relación con Campus 2600</th></tr>
                  </thead>
                  <tbody>
                    <tr><td data-label="Clúster"><strong>C06.</strong> Registro de actores, perfiles de investigadores y sistemas <abbr title="Current Research Information System (sistema de información de investigación)">CRIS</abbr></td><td data-label="Fichas">38</td><td data-label="Relación">Directorio de actores y servicios</td></tr>
                    <tr><td data-label="Clúster"><strong>C02.</strong> Emparejamiento de oferta y demanda y transferencia tecnológica</td><td data-label="Fichas">36</td><td data-label="Relación">Servicios de los integradores; el motor de emparejamiento queda fuera del caso (Tabla 5.2)</td></tr>
                    <tr><td data-label="Clúster"><strong>C05.</strong> Observatorios, indicadores y ciencia abierta</td><td data-label="Fichas">18</td><td data-label="Relación">Reportes</td></tr>
                    <tr><td data-label="Clúster"><strong>C01.</strong> Agencias de financiación de la innovación empresarial</td><td data-label="Fichas">12</td><td data-label="Relación">Convocatoria y postulación</td></tr>
                    <tr><td data-label="Clúster"><strong>C03.</strong> Emprendimiento, incubación y aceleración</td><td data-label="Fichas">11</td><td data-label="Relación">Beneficiarios (<abbr title="Empresas de Base Científica y Tecnológica">EBCT</abbr>, <abbr title="Empresas de Alto Impacto">EAI</abbr> y MiPymes)</td></tr>
                    <tr><td data-label="Clúster"><strong>C04.</strong> Infraestructura compartida y gobernanza territorial</td><td data-label="Fichas">6</td><td data-label="Relación">Laboratorios ofrecidos como servicio</td></tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-4h: Brechas y candidatos (§5.4.4, Tabla 5.5) -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-tone="amber">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3) &middot; Referentes CTeI</p>
                <h2 style="margin-bottom:4px;">Brechas frente a CT000 y candidatos a requisito para Campus 2600 (§5.4.4)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;">La herramienta <code>coverage_gaps</code> comparó las etiquetas de las 121 fichas con la ficha privada CT000 y encontró <strong>33 brechas</strong>: 12 actores, 13 servicios y 8 interacciones que el panorama tiene y CT000 no (A14). «Una brecha no es un requisito»: puede desaparecer si Hēma ya cubre el tema en Ecosistema o en BankPro, y cada candidato pasa por el equipo de requerimientos de ATENEA. Cinco de los diez candidatos aplican a Campus 2600: 1, 2, 4, 8 y 10.</p>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><code>aracne-ctei-scout</code> aún no ha corrido sobre Campus, así que el caso no tiene todavía un <code>research-brief.md</code>; la campaña y la comparación se hicieron con las herramientas del servidor <code>ctei-landscape</code> llamadas directamente.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.64rem,min(1.1vw,1.9vh),1.4rem);">
                  <caption>Tabla 5.5. Candidatos a requisito del estudio de referentes CTeI para validar con ATENEA. Panorama: <a href="https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion" target="_blank" rel="noopener" style="overflow-wrap:anywhere;">https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion</a></caption>
                  <thead>
                    <tr>
                      <th style="width:5%;font-size:0.82em;">N.º</th>
                      <th style="width:57%;font-size:0.82em;">Candidato</th>
                      <th style="width:22%;font-size:0.82em;">Fichas que lo respaldan</th>
                      <th style="font-size:0.82em;">¿Aplica a Campus 2600?</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td data-label="N.º"><strong>1</strong></td><td data-label="Candidato">Oficinas de transferencia, centros de desarrollo tecnológico y parques como actores con perfil propio en el directorio</td><td data-label="Fichas">CT119, CT118, CT110, CT204</td><td data-label="¿Aplica?"><span class="pill pill--ok">Sí</span></td></tr>
                    <tr><td data-label="N.º"><strong>2</strong></td><td data-label="Candidato">Reconocimiento o certificación de actores en el directorio, enlazado con el de Minciencias</td><td data-label="Fichas">CT110, CT109, CT202</td><td data-label="¿Aplica?"><span class="pill pill--ok">Sí</span></td></tr>
                    <tr><td data-label="N.º"><strong>3</strong></td><td data-label="Candidato">Perfil del investigador interoperable con CvLAC, GrupLAC y ORCID</td><td data-label="Fichas">CT108, CT200, CT320, CT318, CT501</td><td data-label="¿Aplica?">No directamente</td></tr>
                    <tr><td data-label="N.º"><strong>4</strong></td><td data-label="Candidato">Red de expertos y búsqueda de evaluadores a partir de perfiles, para el panel de jurados y el panel de expertos del diagnóstico</td><td data-label="Fichas">CT301, CT405, CT406, CT515</td><td data-label="¿Aplica?"><span class="pill pill--ok">Sí</span></td></tr>
                    <tr><td data-label="N.º"><strong>5</strong></td><td data-label="Candidato">Observatorio e indicadores públicos del sistema de Bogotá con datos abiertos</td><td data-label="Fichas">CT112, CT117, CT107, CT207</td><td data-label="¿Aplica?">No directamente</td></tr>
                    <tr><td data-label="N.º"><strong>6</strong></td><td data-label="Candidato">Retos de innovación abierta para articular oferta y demanda</td><td data-label="Fichas">CT116, CT100, CT315, CT314</td><td data-label="¿Aplica?">No directamente</td></tr>
                    <tr><td data-label="N.º"><strong>7</strong></td><td data-label="Candidato">Vitrina de resultados y licenciamiento de tecnologías</td><td data-label="Fichas">CT303, CT312, CT313, CT216</td><td data-label="¿Aplica?">No directamente</td></tr>
                    <tr><td data-label="N.º"><strong>8</strong></td><td data-label="Candidato">Inversionistas y fondos de capital como actores del directorio, ligados al servicio de levantar capital de la ruta de Campus</td><td data-label="Fichas">CT102, CT204, CT208, CT212</td><td data-label="¿Aplica?"><span class="pill pill--ok">Sí</span></td></tr>
                    <tr><td data-label="N.º"><strong>9</strong></td><td data-label="Candidato">Eventos y relacionamiento dentro de la plataforma</td><td data-label="Fichas">CT100, CT302</td><td data-label="¿Aplica?">No directamente</td></tr>
                    <tr><td data-label="N.º"><strong>10</strong></td><td data-label="Candidato">Cofinanciación entre varios actores y consorcios como modalidad de postulación</td><td data-label="Fichas">CT104, CT202, CT203, CT212</td><td data-label="¿Aplica?"><span class="pill pill--ok">Sí</span></td></tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-5: Proceso misional destino (Tabla 5.6) [c3-proceso] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-item="c3-proceso" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Proceso misional destino: seis etapas de Campus 2600 en Hēma (§5.5)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><strong>Integradores:</strong> CEIBA y CONNECT (Connect Bogotá) prestan los servicios del directorio, hoy en catálogos de Excel; la bolsa se reparte 60&nbsp;% para Ceiba y 40&nbsp;% para Connect (R6). <strong>Prototipo:</strong> convocatoria de un año prorrogable con tres tipologías (<abbr title="Empresas de Base Científica y Tecnológica">EBCT</abbr> hasta $120.000.000, <abbr title="Empresas de Alto Impacto">EAI</abbr> hasta $50.000.000 y MiPymes hasta $25.000.000 COP); los topes se describen porque el prototipo los muestra, y su inclusión en el caso queda por confirmar con ATENEA (Tabla 5.3).</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.2vw,2.0vh),1.5rem);">
                  <caption>Tabla 5.6. Etapas del proceso misional de Campus 2600 en Hēma: etapa, actores, insumo y resultado</caption>
                  <thead>
                    <tr>
                      <th style="width:15%;font-size:0.82em;">Etapa</th>
                      <th style="width:20%;font-size:0.82em;">Actores</th>
                      <th style="width:30%;font-size:0.82em;">Insumos</th>
                      <th style="font-size:0.82em;">Resultados</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Etapa"><strong>1. Directorio y catálogo</strong></td>
                      <td data-label="Actores">Gestor Hēma e integradores</td>
                      <td data-label="Insumos">Caracterización de actores; catálogos de los integradores, hoy en Excel, cargados con una plantilla de las variables de Ecosistema</td>
                      <td data-label="Resultados">Catálogo de servicios Campus en una versión aprobada</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa"><strong>2. Postulación técnica</strong></td>
                      <td data-label="Actores">Emprendimiento o spin-off y gestor de Campus</td>
                      <td data-label="Insumos">Operación primaria, con documentos habilitantes, y secundaria, con foco estratégico, antecedentes legales y <abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr></td>
                      <td data-label="Resultados">Radicado (ejemplo: RAD-OP1-2024-00145); el gestor aprueba, pide subsanación o rechaza cada etapa</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa"><strong>3. Calificación y filtro</strong></td>
                      <td data-label="Actores">Evaluación técnica y panel de tres jurados</td>
                      <td data-label="Insumos">Expediente y criterios técnicos; documentos <abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr> gestionados en paralelo</td>
                      <td data-label="Resultados">Puntaje con mínimo exigido (ejemplo del prototipo: 87/100); cada criterio con al menos dos votos de tres; formalización con <abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr> cumplido</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa"><strong>4. Diagnóstico de brechas</strong></td>
                      <td data-label="Actores">Entidad, gestor y, si se requiere, panel de expertos</td>
                      <td data-label="Insumos">Autodiagnóstico de la entidad y diagnóstico del gestor</td>
                      <td data-label="Resultados">Diferencia (Δ) con el promedio de las evaluaciones; brechas, criticidad y servicios propuestos</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa"><strong>5. Hoja de ruta y firmas</strong></td>
                      <td data-label="Actores">Gestor, financiero, emprendedor, integradores, gerente y supervisor del convenio</td>
                      <td data-label="Insumos">Brechas, versión aprobada del catálogo y presupuesto de la tipología, repartido 60&nbsp;% Ceiba y 40&nbsp;% Connect</td>
                      <td data-label="Resultados">Hoja de ruta firmada por hash y congelada; si alguien la rechaza, vuelve a la etapa de ficha</td>
                    </tr>
                    <tr>
                      <td data-label="Etapa"><strong>6. Ejecución y cierre</strong></td>
                      <td data-label="Actores">Integrador asignado (Ceiba o Connect) y gestor</td>
                      <td data-label="Insumos">Hoja de ruta congelada</td>
                      <td data-label="Resultados">Plan de trabajo revisado por el gestor e informes de avance que el gestor valida o devuelve</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-6: Requisitos (Tabla 5.7) [c3-requisitos] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-item="c3-requisitos" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Requisitos: seis no funcionales y doce funcionales del caso (§5.6)</h2>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.6rem,min(1.05vw,1.7vh),1.3rem);line-height:1.2;">
                  <caption>Tabla 5.7. Requisitos del caso de uso Campus 2600: identificador, descripción y origen</caption>
                  <thead>
                    <tr>
                      <th style="width:8%;font-size:0.82em;">ID</th>
                      <th style="font-size:0.82em;">Requisito</th>
                      <th style="width:15%;font-size:0.82em;">Origen</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="ID"><strong>RNF-01</strong></td>
                      <td data-label="Requisito">Integración en la plataforma existente: SICORE usa Angular 13, Java 17 con Spring Boot 3 y persistencia relacional</td>
                      <td data-label="Origen">A5, R2; R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RNF-02</strong></td>
                      <td data-label="Requisito">Ningún dato confidencial o societario sensible llega a los prompts; las pruebas usan datos sintéticos</td>
                      <td data-label="Origen">Tabla 3.12 (A1)</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RNF-03</strong></td>
                      <td data-label="Requisito">Segregación <abbr title="Control de acceso basado en roles">RBAC</abbr>: el postulante no ve los valores, el financiero ve todo y cada integrador ve solo sus servicios</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RNF-04</strong></td>
                      <td data-label="Requisito">Cada firma de la hoja de ruta se registra con un hash (SHA-256 en la pantalla del prototipo)</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RNF-05</strong></td>
                      <td data-label="Requisito">Trazabilidad auditable ante la Contraloría Distrital entre postulación, diagnóstico, firmas y desembolsos</td>
                      <td data-label="Origen">Requerimiento (A2)</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RNF-06</strong></td>
                      <td data-label="Requisito">Validación de topes y transiciones de estado en menos de 500 milisegundos</td>
                      <td data-label="Origen">UNAL; por validar</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-01</strong></td>
                      <td data-label="Requisito">Carga masiva del catálogo con la plantilla de Ecosistema, filtro Campus y versión aprobada por acta (ACTA-CAT-2026-002 en el prototipo)</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-02</strong></td>
                      <td data-label="Requisito">Postulación en operación primaria y secundaria (<abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr>); el gestor aprueba, pide subsanación o rechaza; sin prerrequisitos no se continúa</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-03</strong></td>
                      <td data-label="Requisito">Puntaje con mínimo exigido y panel de tres jurados, cada criterio con dos votos de tres; <abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr> en paralelo, requisito para la formalización</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-04</strong></td>
                      <td data-label="Requisito">Autodiagnóstico, diagnóstico del gestor con posible panel de expertos y Δ con el promedio de las evaluaciones</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-05</strong></td>
                      <td data-label="Requisito">Matriz de criticidad: brechas con su criticidad y los servicios propuestos del catálogo</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-06</strong></td>
                      <td data-label="Requisito">El costo total de los servicios no excede el techo de la tipología ($120M, $50M, $25M)</td>
                      <td data-label="Origen">R6; por confirmar</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-07</strong></td>
                      <td data-label="Requisito">Hojas de ruta parciales cuando la solución de una brecha condiciona las demás</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-08</strong></td>
                      <td data-label="Requisito">Firmas por hash del financiero, el emprendedor, los integradores, el gerente y el supervisor, que hoy van por correo</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-09</strong></td>
                      <td data-label="Requisito">Si algún firmante la rechaza, la hoja de ruta regresa a la etapa de ficha</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-10</strong></td>
                      <td data-label="Requisito">Hoja de ruta inmutable tras la última firma, vinculada a la versión del catálogo activo</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-11</strong></td>
                      <td data-label="Requisito">Plan de trabajo de los integradores con validación obligatoria del gestor de Campus</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                    <tr>
                      <td data-label="ID"><strong>RF-12</strong></td>
                      <td data-label="Requisito">Informes de avance que el gestor valida o devuelve</td>
                      <td data-label="Origen">R6</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-7: Historias de usuario (Tabla 5.8) [c3-historias] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-item="c3-historias" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Historias de usuario: 7 épicas y 14 historias reconstruidas, ocho de muestra (§5.7)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><strong>Reconstrucción:</strong> la Universidad la hizo con la grabación y el prototipo; queda pendiente de validación con ATENEA (R6). El arnés generó 14 contratos OpenSpec, uno por historia, y el plan de sprint los ordenó en tres olas de 7, 5 y 2 según el orden de las historias dentro de cada épica; las dependencias entre épicas todavía no se detectan. <strong>Por resolver al validar:</strong> HU-03 rechaza de forma automática por SARLAFT, que la sesión trató como requisito paralelo, y HU-08 devuelve a borrador, cuando en la sesión la hoja regresa a la etapa de ficha.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.6rem,min(1.05vw,1.8vh),1.3rem);">
                  <caption>Tabla 5.8. Historias de usuario del caso Campus 2600 con criterios de aceptación</caption>
                  <thead>
                    <tr>
                      <th style="width:8%;font-size:0.82em;">Historia</th>
                      <th style="width:20%;font-size:0.82em;">Nombre y rol</th>
                      <th style="font-size:0.82em;">Criterios Given/When/Then</th>
                      <th style="width:24%;font-size:0.82em;">Prueba automatizada</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Historia"><strong>HU-01</strong></td>
                      <td data-label="Nombre y rol">Versionamiento de catálogo (gestor Hēma)</td>
                      <td data-label="Criterios Given/When/Then"><em>Given</em> una carga masiva de servicios, <em>When</em> el gestor aprueba el acta, <em>Then</em> sube la versión y se marcan los servicios Campus activos</td>
                      <td data-label="Prueba automatizada">Servicio: la versión anterior del catálogo es inmutable</td>
                    </tr>
                    <tr>
                      <td data-label="Historia"><strong>HU-02</strong></td>
                      <td data-label="Nombre y rol">Postulación técnica (emprendedor)</td>
                      <td data-label="Criterios Given/When/Then"><em>Given</em> una tipología válida, <em>When</em> se envía el formulario con soportes, <em>Then</em> se genera el radicado y el estado pasa a POSTULADO</td>
                      <td data-label="Prueba automatizada">Integración: radicado unívoco y validación de esquema</td>
                    </tr>
                    <tr>
                      <td data-label="Historia"><strong>HU-03</strong></td>
                      <td data-label="Nombre y rol">Calificación <abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr> (mesa evaluadora)</td>
                      <td data-label="Criterios Given/When/Then"><em>Given</em> un reporte en listas restrictivas, <em>When</em> se procesa la validación, <em>Then</em> el expediente queda en RECHAZADO_SARLAFT</td>
                      <td data-label="Prueba automatizada">Unitaria: rechazo sin avance a diagnóstico</td>
                    </tr>
                    <tr>
                      <td data-label="Historia"><strong>HU-04</strong></td>
                      <td data-label="Nombre y rol">Cálculo de brechas (panel de expertos)</td>
                      <td data-label="Criterios Given/When/Then"><em>Given</em> el autodiagnóstico y las calificaciones, <em>When</em> se cierra la evaluación, <em>Then</em> se calcula el Δ y se clasifican las brechas</td>
                      <td data-label="Prueba automatizada">Algorítmica: promedio ponderado y delta</td>
                    </tr>
                    <tr>
                      <td data-label="Historia"><strong>HU-05</strong></td>
                      <td data-label="Nombre y rol">Control presupuestal (gestor Hēma)</td>
                      <td data-label="Criterios Given/When/Then"><em>Given</em> EBCT con tope de $120.000.000, <em>When</em> los servicios suman $135.000.000, <em>Then</em> la API rechaza la transacción por exceso</td>
                      <td data-label="Prueba automatizada">Contrato de API: límite financiero en el backend</td>
                    </tr>
                    <tr>
                      <td data-label="Historia"><strong>HU-06</strong></td>
                      <td data-label="Nombre y rol">Segregación de costos (integrador CEIBA)</td>
                      <td data-label="Criterios Given/When/Then"><em>Given</em> un usuario con rol CEIBA, <em>When</em> consulta la hoja de ruta, <em>Then</em> solo recibe sus servicios y ningún dato de CONNECT</td>
                      <td data-label="Prueba automatizada">Seguridad: <abbr title="Objeto de transferencia de datos">DTO</abbr> filtrado por contexto</td>
                    </tr>
                    <tr>
                      <td data-label="Historia"><strong>HU-07</strong></td>
                      <td data-label="Nombre y rol">Firma digital con hash (supervisor)</td>
                      <td data-label="Criterios Given/When/Then"><em>Given</em> las aprobaciones previas, <em>When</em> el supervisor firma, <em>Then</em> se genera el hash SHA-256 y la hoja queda congelada</td>
                      <td data-label="Prueba automatizada">Integridad: hash y bloqueo de edición</td>
                    </tr>
                    <tr>
                      <td data-label="Historia"><strong>HU-08</strong></td>
                      <td data-label="Nombre y rol">Devolución de firmas (emprendedor)</td>
                      <td data-label="Criterios Given/When/Then"><em>Given</em> una hoja en circuito de firmas, <em>When</em> el emprendedor marca desacuerdo, <em>Then</em> se invalidan las firmas y vuelve a borrador</td>
                      <td data-label="Prueba automatizada">Máquina de estados: reinicio tras la objeción</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-8: Arquitectura de agentes del caso (Tabla 5.9) [c3-arquitectura-agentes] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-item="c3-arquitectura-agentes" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Arquitectura de agentes del caso: siete fases, la primera opcional, cada una con su decisión humana (§5.8)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;"><span class="pill pill--ok">Establecido</span> El arnés no tiene identidad propia: actúa con los permisos de la cuenta de la persona en la herramienta agéntica y en el repositorio; los controles combinan las restricciones del comando con la cuenta institucional.</p>
              </div>
              <svg viewBox="-6 -6 1212 620" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tabla 5.9: siete fases del caso, la primera opcional, con agentes y comandos, controles y decisión humana de cada una">
<defs><marker id="f55-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker></defs>
<text x="46" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">FASE DEL CASO</text>
<text x="250" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">AGENTES Y COMANDOS</text>
<text x="590" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">CONTROLES</text>
<text x="950" y="20" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700" letter-spacing="1">DECISIÓN HUMANA</text>
<rect x="0" y="34" width="1200" height="74" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.4" stroke-dasharray="7,4" />
<circle cx="24" cy="71.0" r="15" fill="#FFFFFF" stroke="#7FB4CA" stroke-width="2" stroke-dasharray="4,3" />
<text x="24" y="77.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">1</text>
<text x="48" y="60" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Estudio de</text>
<text x="48" y="80" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">referentes</text>
<text x="48" y="99" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="15" font-style="italic">(opcional)</text>
<text x="250" y="58" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">aracne-ctei-scout con</text>
<text x="250" y="77" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">ctei-landscape</text>
<text x="590" y="58" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Cada afirmación del research-brief.md</text>
<text x="590" y="77" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">de Campus, construido sobre la</text>
<text x="590" y="96" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">campaña existente, cita su ficha</text>
<text x="950" y="58" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">El equipo de requerimientos de</text>
<text x="950" y="77" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">ATENEA acepta o descarta cada</text>
<text x="950" y="96" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">candidato</text>
<path d="M24 88.0 V134.0" stroke="#2C6B87" stroke-width="2" stroke-dasharray="5,4" marker-end="url(#f55-b)" />
<g transform="translate(0,82)">
<rect x="0" y="34" width="1200" height="74" rx="6" fill="#F8FAFC" stroke="#D6DEE8" stroke-width="1.2" />
<circle cx="24" cy="71.0" r="15" fill="#7FB4CA" />
<text x="24" y="77.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">2</text>
<text x="48" y="64" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Adopción del área</text>
<text x="250" y="58" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">/sw:adopt y analista de BMAD, con</text>
<text x="250" y="77" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">graphify</text>
<text x="590" y="58" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Lee esquemas de datos y pantallas</text>
<text x="590" y="77" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">sin modificar repositorios</text>
<text x="950" y="58" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">Acordar qué parte del sistema</text>
<text x="950" y="77" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">entra al método</text>
<rect x="0" y="116" width="1200" height="74" rx="6" fill="#FFFFFF" stroke="#D6DEE8" stroke-width="1.2" />
<circle cx="24" cy="153.0" r="15" fill="#7FB4CA" />
<text x="24" y="159.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">3</text>
<text x="48" y="146" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Producto y</text>
<text x="48" y="167" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">arquitectura</text>
<text x="250" y="140" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Agentes de producto, experiencia y</text>
<text x="250" y="159" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">arquitectura de BMAD</text>
<text x="590" y="140" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">La arquitectura base del área manda</text>
<text x="590" y="159" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">sobre los agentes</text>
<text x="950" y="140" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">El líder de producto aprueba</text>
<text x="950" y="159" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">el PRD; la líder del equipo,</text>
<text x="950" y="178" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">la arquitectura</text>
<rect x="0" y="198" width="1200" height="74" rx="6" fill="#F8FAFC" stroke="#D6DEE8" stroke-width="1.2" />
<circle cx="24" cy="235.0" r="15" fill="#7FB4CA" />
<text x="24" y="241.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">4</text>
<text x="48" y="228" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Historias y</text>
<text x="48" y="249" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">contratos</text>
<text x="250" y="222" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Agente de historias y aracne-weaver</text>
<text x="250" y="241" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">con el puente en modo estricto</text>
<text x="590" y="222" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Contratos validados y traza en</text>
<text x="590" y="241" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">trace.json</text>
<text x="950" y="222" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">El líder de producto aprueba</text>
<text x="950" y="241" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">las historias</text>
<rect x="0" y="280" width="1200" height="74" rx="6" fill="#FFFFFF" stroke="#D6DEE8" stroke-width="1.2" />
<circle cx="24" cy="317.0" r="15" fill="#7FB4CA" />
<text x="24" y="323.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">5</text>
<text x="48" y="310" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Olas</text>
<text x="250" y="304" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">aracne-sprint-planner con /sw:sprint</text>
<text x="590" y="304" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Olas según el orden de las historias</text>
<text x="590" y="323" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">en cada épica; sin tocar código</text>
<text x="950" y="304" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">La líder del equipo aprueba</text>
<text x="950" y="323" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">el reparto</text>
<rect x="0" y="362" width="1200" height="74" rx="6" fill="#F8FAFC" stroke="#D6DEE8" stroke-width="1.2" />
<circle cx="24" cy="399.0" r="15" fill="#7FB4CA" />
<text x="24" y="405.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">6</text>
<text x="48" y="392" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Construcción y</text>
<text x="48" y="413" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">revisión</text>
<text x="250" y="386" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">aracne-builder, aracne-validator,</text>
<text x="250" y="405" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">revisores review-* y aracne-cicd</text>
<text x="590" y="386" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Un contrato a la vez; la terminal de</text>
<text x="590" y="405" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">/sw:build se acota a equipos y cuentas</text>
<text x="590" y="424" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">institucionales (Tabla 6.4)</text>
<text x="950" y="386" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">La líder del equipo aprueba</text>
<text x="950" y="405" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">la integración a la rama</text>
<text x="950" y="424" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">protegida</text>
<rect x="0" y="444" width="1200" height="74" rx="6" fill="#FFFFFF" stroke="#D6DEE8" stroke-width="1.2" />
<circle cx="24" cy="481.0" r="15" fill="#7FB4CA" />
<text x="24" y="487.0" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700" text-anchor="middle">7</text>
<text x="48" y="474" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Cierre y</text>
<text x="48" y="495" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">operación</text>
<text x="250" y="468" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">aracne-closer, aracne-status,</text>
<text x="250" y="487" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">aracne-ticket y aracne-change</text>
<text x="590" y="468" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">/sw:status solo lee; los cambios pasan</text>
<text x="590" y="487" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">por control de alcance</text>
<text x="950" y="468" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">Decidir qué historias se</text>
<text x="950" y="487" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="15">cierran y qué vuelve al flujo</text>
<path d="M24 88.0 V134.0" stroke="#2C6B87" stroke-width="2" marker-end="url(#f55-b)" />
<path d="M24 170.0 V216.0" stroke="#2C6B87" stroke-width="2" marker-end="url(#f55-b)" />
<path d="M24 252.0 V298.0" stroke="#2C6B87" stroke-width="2" marker-end="url(#f55-b)" />
<path d="M24 334.0 V380.0" stroke="#2C6B87" stroke-width="2" marker-end="url(#f55-b)" />
<path d="M24 416.0 V462.0" stroke="#2C6B87" stroke-width="2" marker-end="url(#f55-b)" />
</g>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Siete fases del caso, la primera opcional</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>1. Estudio de referentes (opcional).</strong> <em>Agentes y comandos:</em> aracne-ctei-scout con ctei-landscape. <em>Controles:</em> Cada afirmación del research-brief.md de Campus, construido sobre la campaña existente, cita su ficha. <em>Decisión humana:</em> El equipo de requerimientos de ATENEA acepta o descarta cada candidato.</li>
                  <li><strong>2. Adopción del área.</strong> <em>Agentes y comandos:</em> /sw:adopt y analista de BMAD, con graphify. <em>Controles:</em> Lee esquemas de datos y pantallas sin modificar repositorios. <em>Decisión humana:</em> Acordar qué parte del sistema entra al método.</li>
                  <li><strong>3. Producto y arquitectura.</strong> <em>Agentes y comandos:</em> Agentes de producto, experiencia y arquitectura de BMAD. <em>Controles:</em> La arquitectura base del área manda sobre los agentes. <em>Decisión humana:</em> El líder de producto aprueba el PRD; la líder del equipo, la arquitectura.</li>
                  <li><strong>4. Historias y contratos.</strong> <em>Agentes y comandos:</em> Agente de historias y aracne-weaver con el puente en modo estricto. <em>Controles:</em> Contratos validados y traza en trace.json. <em>Decisión humana:</em> El líder de producto aprueba las historias.</li>
                  <li><strong>5. Olas.</strong> <em>Agentes y comandos:</em> aracne-sprint-planner con /sw:sprint. <em>Controles:</em> Olas según el orden de las historias en cada épica, sin tocar código. <em>Decisión humana:</em> La líder del equipo aprueba el reparto.</li>
                  <li><strong>6. Construcción y revisión.</strong> <em>Agentes y comandos:</em> aracne-builder, aracne-validator, revisores review-* y aracne-cicd. <em>Controles:</em> Un contrato a la vez; la terminal de /sw:build se acota a equipos y cuentas institucionales (Tabla 6.4). <em>Decisión humana:</em> La líder del equipo aprueba la integración a la rama protegida.</li>
                  <li><strong>7. Cierre y operación.</strong> <em>Agentes y comandos:</em> aracne-closer, aracne-status, aracne-ticket y aracne-change. <em>Controles:</em> /sw:status solo lee; los cambios pasan por control de alcance. <em>Decisión humana:</em> Decidir qué historias se cierran y qué vuelve al flujo.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Tabla 5.9. Arquitectura de agentes del caso: fase, agentes y comandos, controles y decisión humana</figcaption>
            </figure>
          </article>

          <!-- E3-9: Flujos (Tabla 5.10) [c3-flujos] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-item="c3-flujos" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Flujos del caso: el principal y seis de excepción y contingencia (§5.9)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><strong>Cambios del 30 de octubre:</strong> la subsanación la decide el gestor en cada etapa; los documentos SARLAFT se gestionan en paralelo y condicionan la formalización; una hoja de ruta rechazada regresa a la etapa de ficha.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.2vw,2.0vh),1.5rem);">
                  <caption>Tabla 5.10. Flujos del caso Campus 2600: tipo de flujo, descripción y resultado</caption>
                  <thead>
                    <tr>
                      <th style="width:16%;font-size:0.82em;">Flujo</th>
                      <th style="width:30%;font-size:0.82em;">Descripción</th>
                      <th style="width:27%;font-size:0.82em;">Mecanismo</th>
                      <th style="font-size:0.82em;">Resultado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Flujo"><strong>Flujo principal</strong></td>
                      <td data-label="Descripción">De la postulación a los informes de avance validados por el gestor</td>
                      <td data-label="Mecanismo">Secuencia estándar en seis etapas (Tabla 5.6)</td>
                      <td data-label="Resultado">Hoja de ruta ejecutada con seguimiento del gestor</td>
                    </tr>
                    <tr>
                      <td data-label="Flujo"><strong>Subsanación</strong></td>
                      <td data-label="Descripción">Documentos habilitantes o de la operación secundaria incompletos</td>
                      <td data-label="Mecanismo">El gestor aprueba, pide subsanación o rechaza</td>
                      <td data-label="Resultado">Sin los prerrequisitos no se continúa</td>
                    </tr>
                    <tr>
                      <td data-label="Flujo"><strong>Excepción <abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr></strong></td>
                      <td data-label="Descripción">Documentos SARLAFT incompletos o con hallazgos</td>
                      <td data-label="Mecanismo">Gestión en paralelo a la evaluación técnica</td>
                      <td data-label="Resultado">Sin formalización mientras no se cumplan</td>
                    </tr>
                    <tr>
                      <td data-label="Flujo"><strong>Excepción presupuestal</strong></td>
                      <td data-label="Descripción">Servicios que superan el tope de la tipología (tema por confirmar)</td>
                      <td data-label="Mecanismo">Validación síncrona en el formulario de hoja de ruta</td>
                      <td data-label="Resultado">Bloqueo con indicación de excedente y ajuste</td>
                    </tr>
                    <tr>
                      <td data-label="Flujo"><strong>Hojas parciales</strong></td>
                      <td data-label="Descripción">La solución de una brecha condiciona las demás</td>
                      <td data-label="Mecanismo">Partición de la hoja de ruta en fases consecutivas</td>
                      <td data-label="Resultado">Emisión de hojas de ruta parciales</td>
                    </tr>
                    <tr>
                      <td data-label="Flujo"><strong>Objeción en firmas</strong></td>
                      <td data-label="Descripción">Rechazo de cualquier firmante de la hoja de ruta</td>
                      <td data-label="Mecanismo">Regreso a la etapa de ficha</td>
                      <td data-label="Resultado">Nueva concertación y nuevo circuito de firmas</td>
                    </tr>
                    <tr>
                      <td data-label="Flujo"><strong>Catálogo dinámico</strong></td>
                      <td data-label="Descripción">Actualización del catálogo de servicios durante el proceso</td>
                      <td data-label="Mecanismo">Versionamiento por acta institucional</td>
                      <td data-label="Resultado">Protección de hojas previas y consulta del nuevo catálogo</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-10: Integraciones (Tabla 5.11) [c3-integraciones] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-item="c3-integraciones" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Integraciones: siete sistemas de ATENEA con los que se articula el caso (§5.10)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><strong>Pendientes:</strong> la estructura de Azure se revisa con GoToCloud el martes 3 de noviembre de 2026, a las 4 p.&nbsp;m.; la ubicación de la wiki de Azure DevOps se define en la siguiente reunión; el motor de emparejamiento queda para la segunda transición.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.2vw,2.0vh),1.5rem);">
                  <caption>Tabla 5.11. Integraciones del caso Campus 2600 con el ecosistema de ATENEA</caption>
                  <thead>
                    <tr>
                      <th style="width:17%;font-size:0.82em;">Sistema</th>
                      <th style="width:30%;font-size:0.82em;">Función en el caso</th>
                      <th style="width:24%;font-size:0.82em;">Protocolo e interfaz</th>
                      <th style="font-size:0.82em;">Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Sistema"><strong>Azure Repos y Pipelines</strong></td>
                      <td data-label="Función en el caso">Control de versiones, compilación continua y despliegue del código</td>
                      <td data-label="Protocolo e interfaz">Git sobre HTTPS y agentes de Azure DevOps</td>
                      <td data-label="Estado"><span class="pill pill--partial">En migración</span> estructura de Azure en revisión con GoToCloud el 3 de noviembre de 2026</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema"><strong>Wiki del proyecto en Azure DevOps</strong></td>
                      <td data-label="Función en el caso">Posible ubicación central de los artefactos y los requerimientos</td>
                      <td data-label="Protocolo e interfaz">Wiki de Azure DevOps</td>
                      <td data-label="Estado"><span class="pill pill--todo">Planteada</span> ubicación definitiva en la siguiente reunión</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema"><strong>Persistencia relacional</strong></td>
                      <td data-label="Función en el caso">Tablas de postulación, catálogos, hojas de ruta y planes de trabajo</td>
                      <td data-label="Protocolo e interfaz">Oracle Autonomous vía <abbr title="Jakarta Persistence API">JPA</abbr></td>
                      <td data-label="Estado"><span class="pill pill--ok">Existente</span> en SICORE</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema"><strong>Base de datos de grafos</strong></td>
                      <td data-label="Función en el caso">Motor de emparejamiento entre oferta y demanda de servicios</td>
                      <td data-label="Protocolo e interfaz">Base de datos de grafos y modelo semántico</td>
                      <td data-label="Estado"><span class="pill pill--todo">Fuera del caso</span> segunda transición de Hēma</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema"><strong>Autenticación institucional</strong></td>
                      <td data-label="Función en el caso">Identidades y roles con Keycloak, conectado al Directorio Activo o a un directorio interno de la entidad</td>
                      <td data-label="Protocolo e interfaz"><abbr title="OpenID Connect">OIDC</abbr> / <abbr title="JSON Web Token">JWT</abbr> con mapeo de roles <abbr title="Control de acceso basado en roles">RBAC</abbr></td>
                      <td data-label="Estado"><span class="pill pill--partial">En incorporación</span> integración con el directorio por concretar con GoToCloud y Microsoft</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema"><strong>Servicio de firmas hash</strong></td>
                      <td data-label="Función en el caso">Huellas SHA-256 para hojas de ruta congeladas</td>
                      <td data-label="Protocolo e interfaz">API interna de firma con almacenamiento inmutable</td>
                      <td data-label="Estado"><span class="pill pill--todo">Mostrado en el prototipo</span> sin desarrollo</td>
                    </tr>
                    <tr>
                      <td data-label="Sistema"><strong>Gestor documental</strong></td>
                      <td data-label="Función en el caso">Archivo formal de actas de catálogo (ACTA-CAT) y resoluciones</td>
                      <td data-label="Protocolo e interfaz">Conexión documental para soportes oficiales</td>
                      <td data-label="Estado"><span class="pill pill--ok">Existente</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-11: Datos (Tabla 5.12) [c3-datos] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-item="c3-datos" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Datos y modelo de seguridad: qué puede llegar al modelo de IA (§5.11)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><strong>Entidades:</strong> CONVOCATORIA, TIPOLOGIA, POSTULACION, ACTOR, CATALOGO_SERVICIO, ACTA_CATALOGO, EVALUACION_MESA, DIAGNOSTICO, HOJA_RUTA, HOJA_RUTA_SERVICIO, FIRMA_HASH, PLAN_TRABAJO e INFORME_AVANCE. Vienen de la reconstrucción de la Universidad y se contrastarán con la plataforma desplegada cuando ATENEA dé el acceso. <strong>Regla:</strong> los agentes solo reciben el esquema relacional y las definiciones de <abbr title="Objeto de transferencia de datos">DTO</abbr>, nunca los datos societarios ni los antecedentes reales.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.2vw,2.0vh),1.5rem);">
                  <caption>Tabla 5.12. Clasificación y tratamiento de datos del caso Campus 2600</caption>
                  <thead>
                    <tr>
                      <th style="width:20%;font-size:0.82em;">Entidad o dato</th>
                      <th style="width:18%;font-size:0.82em;">Clasificación</th>
                      <th style="width:32%;font-size:0.82em;">Restricción de seguridad</th>
                      <th style="font-size:0.82em;">¿Llega al modelo de IA?</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Entidad o dato"><strong>Antecedentes y <abbr title="Sistema de Administración del Riesgo de Lavado de Activos y de la Financiación del Terrorismo">SARLAFT</abbr></strong></td>
                      <td data-label="Clasificación">Confidencial</td>
                      <td data-label="Restricción de seguridad">Almacenamiento cifrado con acceso restringido a evaluadores</td>
                      <td data-label="¿Llega al modelo de IA?"><span class="pill pill--risk">No</span> solo el estado booleano de cumplimiento</td>
                    </tr>
                    <tr>
                      <td data-label="Entidad o dato"><strong>Tarifas de integradores</strong></td>
                      <td data-label="Clasificación">Confidencial comercial</td>
                      <td data-label="Restricción de seguridad">Ocultas para postulantes; aislamiento entre Ceiba y Connect</td>
                      <td data-label="¿Llega al modelo de IA?"><span class="pill pill--risk">No</span> solo rangos sintéticos en pruebas</td>
                    </tr>
                    <tr>
                      <td data-label="Entidad o dato"><strong>Soportes de postulación</strong></td>
                      <td data-label="Clasificación">Privada / institucional</td>
                      <td data-label="Restricción de seguridad">Servidor de archivos seguro</td>
                      <td data-label="¿Llega al modelo de IA?"><span class="pill pill--risk">No</span></td>
                    </tr>
                    <tr>
                      <td data-label="Entidad o dato"><strong>Estructura del catálogo</strong></td>
                      <td data-label="Clasificación">Pública institucional</td>
                      <td data-label="Restricción de seguridad">Accesible a todos los roles autenticados</td>
                      <td data-label="¿Llega al modelo de IA?"><span class="pill pill--ok">Sí</span> esquemas y nombres de servicio</td>
                    </tr>
                    <tr>
                      <td data-label="Entidad o dato"><strong>Huella de firma hash</strong></td>
                      <td data-label="Clasificación">Pública institucional</td>
                      <td data-label="Restricción de seguridad">Verificable públicamente para no repudio</td>
                      <td data-label="¿Llega al modelo de IA?"><span class="pill pill--ok">Sí</span> cadenas hash SHA-256</td>
                    </tr>
                    <tr>
                      <td data-label="Entidad o dato"><strong>Juego de pruebas sintéticas</strong></td>
                      <td data-label="Clasificación">Abierta de ingeniería</td>
                      <td data-label="Restricción de seguridad">Diseñado para validación automatizada de reglas</td>
                      <td data-label="¿Llega al modelo de IA?"><span class="pill pill--ok">Sí</span> con anonimización completa</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E3-12: Criterios de aceptación (Tabla 5.13) [c3-aceptacion] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e3" data-item="c3-aceptacion" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">4 &middot; Arquitectura del Arnés (E3)</p>
                <h2 style="margin-bottom:4px;">Criterios de aceptación: por historia y de punta a punta (§5.12)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;margin-bottom:2px;"><strong>Dos niveles:</strong> por historia, con pruebas automatizadas generadas en el flujo SDLC-IA, y de punta a punta, con la supervisión de ATENEA. La ingeniería de pruebas del caso es el componente C6.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.2vw,2.0vh),1.5rem);">
                  <caption>Tabla 5.13. Criterios de aceptación del caso Campus 2600: nivel, criterio y validación</caption>
                  <thead>
                    <tr>
                      <th style="width:44%;font-size:0.82em;">Criterio de aceptación</th>
                      <th style="width:30%;font-size:0.82em;">Evidencia técnica</th>
                      <th style="font-size:0.82em;">Valida</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td colspan="3" data-label="Nivel" style="background:#EAF3F8;color:#1F536C;font-weight:700;letter-spacing:0.04em;text-transform:uppercase;">Por historia</td></tr>
                    <tr>
                      <td data-label="Criterio de aceptación">Cada escenario <em>Given/When/Then</em> tiene una prueba unitaria o de integración que pasa al 100&nbsp;%</td>
                      <td data-label="Evidencia técnica">Reporte de ejecución de pruebas en el pipeline</td>
                      <td data-label="Valida">Desarrollador y agente validador</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio de aceptación">El control presupuestal rechaza en el backend, de forma determinística, los intentos de desbordamiento</td>
                      <td data-label="Evidencia técnica">Caso de prueba automatizado con aserción de error</td>
                      <td data-label="Valida">Agente de pruebas y líder técnico</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio de aceptación">Las consultas por perfil filtran las tarifas y los datos de integradores competidores</td>
                      <td data-label="Evidencia técnica">Pruebas de integración con perfiles de seguridad</td>
                      <td data-label="Valida">Auditor de seguridad y líder técnico</td>
                    </tr>
                    <tr><td colspan="3" data-label="Nivel" style="background:#EAF3F8;color:#1F536C;font-weight:700;letter-spacing:0.04em;text-transform:uppercase;">De punta a punta</td></tr>
                    <tr>
                      <td data-label="Criterio de aceptación">El circuito de postulación, diagnóstico y firmas se ejecuta sin errores en <abbr title="Ambiente de aseguramiento de la calidad">QA</abbr></td>
                      <td data-label="Evidencia técnica">Bitácora de despliegue y ejecución en Azure</td>
                      <td data-label="Valida">Equipo de infraestructura</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio de aceptación">La hoja de ruta genera un hash inmutable y se congela sin admitir modificaciones</td>
                      <td data-label="Evidencia técnica">Prueba de integridad de datos y reporte de verificación</td>
                      <td data-label="Valida">Supervisor del convenio y negocio</td>
                    </tr>
                    <tr>
                      <td data-label="Criterio de aceptación">El flujo completo queda registrado en la traza institucional trace.json</td>
                      <td data-label="Evidencia técnica">Archivo de trazabilidad validado</td>
                      <td data-label="Valida">Subgerencia de TIC de ATENEA</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>


          <!-- E4-1: Flujo integral de artefactos (Figura 6.1) [c4-arquitectura] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e4" data-item="c4-arquitectura" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
                <h2 style="margin-bottom:4px;">Flujo integral de artefactos de Aracne: de la idea a la línea base</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Tres enfoques: <abbr title="Breakthrough Method for Agile AI-Driven Development">BMAD</abbr> (de la concepción a la historia), <abbr title="Desarrollo Dirigido por Especificación">SDD</abbr> con OpenSpec (de la historia al contrato) y <abbr title="Desarrollo Orgánico y Acotado">ODD</abbr> (construcción contra el contrato). <strong>Regla de frontera:</strong> <abbr title="Breakthrough Method for Agile AI-Driven Development">BMAD</abbr> se detiene en la historia con criterios <em>Given/When/Then</em>; desde ahí el control pasa al Tejedor LIA y al constructor.</p>
              </div>
              <svg viewBox="-12 -6 1218 590" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figura 6.1: flujo integral de artefactos del arnés Aracne en tres fases, con el bucle de cambio de alcance">
<defs>
<marker id="a61b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
<marker id="a61g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#1E5631" /></marker>
<marker id="a61a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#B07A12" /></marker>
<marker id="a61k" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#5B6472" /></marker>
</defs>
<rect x="40" y="0" width="1160" height="178" rx="10" fill="#EDF1F7" stroke="#2C6B87" stroke-width="1.4" stroke-dasharray="7,5" />
<rect x="52" y="9" width="470" height="26" rx="4" fill="#2C6B87" />
<text x="62" y="27" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Fase de especificación y contratos (Entender a Traducir)</text>
<rect x="56" y="50" width="236" height="112" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="174" y="83.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Gestor de</text>
<text x="174" y="104.7" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">especificaciones</text>
<text x="174" y="123.3" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">BMAD: PRD, arquitectura y</text>
<text x="174" y="141.3" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">prototipos de interfaz UX</text>
<rect x="356" y="50" width="236" height="112" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="474" y="85.2" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Historias de usuario</text>
<text x="474" y="103.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">épicas y criterios de</text>
<text x="474" y="121.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">aceptación en formato</text>
<text x="474" y="139.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">Given/When/Then</text>
<rect x="656" y="50" width="236" height="112" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="774" y="85.2" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Tejedor (Arnés LIA)</text>
<text x="774" y="103.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">conversión historia a</text>
<text x="774" y="121.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">contrato verificable y</text>
<text x="774" y="139.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">registro de traza</text>
<rect x="956" y="50" width="236" height="112" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="1074" y="94.2" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Contratos (OpenSpec)</text>
<text x="1074" y="112.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">especificación ejecutable y</text>
<text x="1074" y="130.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">formal por cada historia</text>
<path d="M294 106 H353" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a61b)" />
<path d="M594 106 H653" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a61b)" />
<path d="M894 106 H953" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a61b)" />
<rect x="40" y="214" width="1160" height="178" rx="10" fill="#F0F7F2" stroke="#1E5631" stroke-width="1.4" stroke-dasharray="7,5" />
<rect x="52" y="223" width="505" height="26" rx="4" fill="#1E5631" />
<text x="62" y="241" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Fase de construcción y cierre verificable (Construir y Cerrar)</text>
<rect x="56" y="264" width="236" height="112" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="174" y="308.2" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Memoria persistente</text>
<text x="174" y="326.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">Engram: decisiones de diseño</text>
<text x="174" y="344.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">y lecciones por proyecto</text>
<rect x="356" y="264" width="236" height="112" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="474" y="299.2" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Tablero de estado</text>
<text x="474" y="317.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">avance, estabilidad y</text>
<text x="474" y="335.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">métricas del proyecto en</text>
<text x="474" y="353.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">tiempo real</text>
<rect x="656" y="264" width="236" height="112" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="774" y="308.2" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Cerrar (Arnés LIA)</text>
<text x="774" y="326.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">validación, archivado y</text>
<text x="774" y="344.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">fijación de línea base</text>
<rect x="956" y="264" width="236" height="112" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="1074" y="308.2" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Construir (Entorno)</text>
<text x="1074" y="326.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">código y pruebas unitarias</text>
<text x="1074" y="344.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">automatizadas por escenario</text>
<path d="M954 320 H895" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a61b)" />
<path d="M654 320 H595" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a61b)" />
<path d="M294 320 H353" stroke="#2C6B87" stroke-width="2.2" fill="none" stroke-dasharray="6,4" marker-end="url(#a61b)" />
<text x="924" y="298" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">código</text>
<text x="924" y="312" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">+ pruebas</text>
<text x="624" y="298" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">línea</text>
<text x="624" y="312" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">base</text>
<text x="324" y="312" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="11.5" text-anchor="middle">decisiones</text>
<rect x="40" y="428" width="1160" height="150" rx="10" fill="#EDF1F7" stroke="#2C6B87" stroke-width="1.4" stroke-dasharray="7,5" />
<rect x="52" y="437" width="480" height="26" rx="4" fill="#2C6B87" />
<text x="62" y="455" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Gobernanza transversal y contexto de código (Soporte continuo)</text>
<rect x="56" y="468" width="836" height="96" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="474" y="513.1" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Control de cambios, defectos e incidencias (Arnés LIA)</text>
<text x="474" y="531.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">/sw:change (control de alcance) · /sw:bug (correcciones) · /sw:ticket (enrutamiento)</text>
<rect x="956" y="468" width="236" height="96" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="1074" y="495.2" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700" text-anchor="middle">Mapa del código</text>
<text x="1074" y="513.8" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">graphify: análisis de</text>
<text x="1074" y="531.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">impacto y dependencias en</text>
<text x="1074" y="549.7" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">grafo AST</text>
<path d="M1074 162 V262" stroke="#1E5631" stroke-width="2.2" fill="none" marker-end="url(#a61g)" />
<text x="1084" y="202" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">contrato formal</text>
<path d="M1074 466 V379" stroke="#2C6B87" stroke-width="2" fill="none" stroke-dasharray="6,4" marker-end="url(#a61b)" />
<text x="1084" y="414" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13">grafo AST</text>
<path d="M954 516 H895" stroke="#2C6B87" stroke-width="2" fill="none" stroke-dasharray="6,4" marker-end="url(#a61b)" />
<path d="M562 378 V466" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a61b)" marker-start="url(#a61b)" />
<rect x="330" y="184" width="540" height="24" rx="5" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1" fill-opacity="1" />
<text x="600" y="201" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="13" text-anchor="middle">traza requisito–contrato · plan de olas de trabajo paralelo</text>
<path d="M56 516 H14 V106 H53" stroke="#B07A12" stroke-width="2.2" fill="none" stroke-dasharray="7,5" marker-end="url(#a61a)" />
<text x="8" y="316" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" text-anchor="middle" transform="rotate(-90 8,316)">cambio de alcance: vuelve a planeación; regenera solo lo afectado</text>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Tres fases del flujo de artefactos</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>1. Especificación y contratos (Entender a Traducir).</strong> Gestor de especificaciones (BMAD: PRD, arquitectura y prototipos UX) &rarr; historias de usuario con criterios <em>Given/When/Then</em> &rarr; Tejedor (Arnés LIA): conversión historia a contrato verificable y registro de traza &rarr; contratos (OpenSpec), uno por historia. Anotación: traza requisito&ndash;contrato y plan de olas de trabajo paralelo.</li>
                  <li><strong>2. Construcción y cierre verificable (Construir y Cerrar).</strong> Del contrato formal a construir (código y pruebas unitarias por escenario) &rarr; cerrar (validación, archivado y línea base) &rarr; tablero de estado (avance, estabilidad y métricas). La memoria persistente (Engram) aporta decisiones al tablero.</li>
                  <li><strong>3. Gobernanza transversal y contexto de código (Soporte continuo).</strong> Control de cambios, defectos e incidencias (<code>/sw:change</code>, <code>/sw:bug</code>, <code>/sw:ticket</code>) y mapa del código con graphify (grafo AST) para el análisis de impacto. Un cambio de alcance vuelve a planeación y regenera solo lo afectado.</li>
                </ul>
                <p class="sched-note">Verde: componentes propios del LIA UNAL; azul: piezas y herramientas integradas.</p>
              </div>
              <figcaption class="fig-caption">Figura 6.1 — Flujo de artefactos del arnés de agentes de IA. Verde: componentes propios desarrollados por el LIA UNAL; azul: piezas y herramientas integradas</figcaption>
            </figure>
          </article>

          <!-- E4-2: Agentes base 1/2 (Tabla 6.1) [c4-arquitectura] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e4" data-item="c4-arquitectura" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
                <h2 style="margin-bottom:4px;">Agentes base de Aracne (1/2): de entender el requerimiento a construirlo</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Dieciséis agentes base, cada uno con un rol delimitado y una supervisión humana obligatoria; diez de ellos son subagentes <code>aracne-*</code> propios y los de planeación son agentes de <abbr title="Breakthrough Method for Agile AI-Driven Development">BMAD</abbr>. Se suman dos agentes opcionales de investigación, construidos después del paquete congelado, que entran en la versión siguiente.</p>
              </div>
              <svg viewBox="0 -2 1200 594" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tabla 6.1 (1/2): diez agentes, de entender a construir, ocho base y dos opcionales, con su identificador, lo que producen y el control humano">
<rect x="0" y="2" width="18" height="18" rx="3" fill="#EBF5ED" stroke="#1E5631" stroke-width="2" />
<text x="26" y="17" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Subagente propio aracne-*</text>
<rect x="255.8" y="2" width="18" height="18" rx="3" fill="#FFFFFF" stroke="#2C6B87" stroke-width="2" />
<text x="281.8" y="17" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Agente o skill de BMAD</text>
<rect x="490" y="2" width="18" height="18" rx="3" fill="#FFFFFF" stroke="#1E5631" stroke-width="2" stroke-dasharray="4,3" />
<text x="516" y="17" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Opcional: construido después del paquete 0.9.0, entra en la versión siguiente</text>
<rect x="0" y="36" width="228" height="268" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<rect x="0" y="36" width="228" height="28" rx="8" fill="#2C6B87" />
<rect x="0" y="50" width="228" height="14" rx="0" fill="#2C6B87" />
<text x="10" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Entender</text>
<text x="218" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">1</text>
<text x="10" y="89" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Analista de</text>
<text x="10" y="109" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Requerimientos y CU</text>
<text x="10" y="129" fill="#2C6B87" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">bmad-agent-analyst</text>
<text x="10" y="157" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="10" y="176" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Brief de producto o de</text>
<text x="10" y="194" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">adopción</text>
<text x="10" y="216" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="10" y="235" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Valida casos de uso,</text>
<text x="10" y="253" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">intención y alcance</text>
<text x="10" y="271" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">pactado</text>
<rect x="243" y="36" width="228" height="268" rx="8" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.8" stroke-dasharray="7,4" />
<rect x="243" y="36" width="228" height="28" rx="8" fill="#1E5631" />
<rect x="243" y="50" width="228" height="14" rx="0" fill="#1E5631" />
<text x="253" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Entender</text>
<text x="461" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">2</text>
<text x="253" y="89" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Investigador CTeI</text>
<text x="253" y="109" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14.5" font-style="italic">(opcional)</text>
<text x="253" y="129" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">aracne-ctei-scout</text>
<text x="253" y="157" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="253" y="176" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">research-brief.md con</text>
<text x="253" y="194" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">requisitos, épicas e</text>
<text x="253" y="212" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">historias candidatas</text>
<text x="253" y="234" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="253" y="253" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Requerimientos acepta o</text>
<text x="253" y="271" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">descarta cada candidato</text>
<rect x="486" y="36" width="228" height="268" rx="8" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.8" stroke-dasharray="7,4" />
<rect x="486" y="36" width="228" height="28" rx="8" fill="#1E5631" />
<rect x="486" y="50" width="228" height="14" rx="0" fill="#1E5631" />
<text x="496" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Entender a Construir</text>
<text x="704" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">3</text>
<text x="496" y="89" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Consultor de</text>
<text x="496" y="109" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Portafolio <tspan fill="#5B6472" font-size="14.5" font-weight="400" font-style="italic">(opcional)</tspan></text>
<text x="496" y="129" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">aracne-portfolio</text>
<text x="496" y="157" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="496" y="176" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Productos y componentes</text>
<text x="496" y="194" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">de ATENEA para reutilizar</text>
<text x="496" y="216" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="496" y="235" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Decide qué se reutiliza</text>
<rect x="729" y="36" width="228" height="268" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<rect x="729" y="36" width="228" height="28" rx="8" fill="#2C6B87" />
<rect x="729" y="50" width="228" height="14" rx="0" fill="#2C6B87" />
<text x="739" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Entender a Decidir</text>
<text x="947" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">4</text>
<text x="739" y="89" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Product Manager (PM)</text>
<text x="739" y="109" fill="#2C6B87" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">bmad-agent-pm</text>
<text x="739" y="137" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="739" y="156" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">PRD con FR y NFR</text>
<text x="739" y="174" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">numerados</text>
<text x="739" y="196" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="739" y="215" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Aprueba el PRD y la</text>
<text x="739" y="233" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">priorización de requisitos</text>
<rect x="972" y="36" width="228" height="268" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<rect x="972" y="36" width="228" height="28" rx="8" fill="#2C6B87" />
<rect x="972" y="50" width="228" height="14" rx="0" fill="#2C6B87" />
<text x="982" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Decidir</text>
<text x="1190" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">5</text>
<text x="982" y="89" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Diseñador UX/UI</text>
<text x="982" y="109" fill="#2C6B87" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">bmad-agent-ux-designer</text>
<text x="982" y="137" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="982" y="156" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">DESIGN.md y</text>
<text x="982" y="174" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">especificaciones UX-DR</text>
<text x="982" y="196" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="982" y="215" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Aprueba el diseño de</text>
<text x="982" y="233" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">interacción, las pantallas</text>
<text x="982" y="251" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">y los contratos visuales</text>
<rect x="0" y="322" width="228" height="268" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<rect x="0" y="322" width="228" height="28" rx="8" fill="#2C6B87" />
<rect x="0" y="336" width="228" height="14" rx="0" fill="#2C6B87" />
<text x="10" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Decidir</text>
<text x="218" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">6</text>
<text x="10" y="375" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Arquitecto de</text>
<text x="10" y="395" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Software</text>
<text x="10" y="415" fill="#2C6B87" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">bmad-agent-architect</text>
<text x="10" y="443" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="10" y="462" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">ARCHITECTURE-SPINE.md</text>
<text x="10" y="480" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">y límites modulares</text>
<text x="10" y="502" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="10" y="521" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Aprueba componentes,</text>
<text x="10" y="539" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">patrones, modelo de datos</text>
<text x="10" y="557" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">y contratos</text>
<rect x="243" y="322" width="228" height="268" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<rect x="243" y="322" width="228" height="28" rx="8" fill="#2C6B87" />
<rect x="243" y="336" width="228" height="14" rx="0" fill="#2C6B87" />
<text x="253" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Descomponer</text>
<text x="461" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">7</text>
<text x="253" y="375" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Descompositor de</text>
<text x="253" y="395" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Historias</text>
<text x="253" y="415" fill="#2C6B87" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">skill de BMAD</text>
<text x="253" y="443" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="253" y="462" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Épicas e historias</text>
<text x="253" y="480" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Given/When/Then</text>
<text x="253" y="502" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="253" y="521" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Aprueba el desglose de</text>
<text x="253" y="539" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">historias antes de</text>
<text x="253" y="557" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">compilar contratos</text>
<rect x="486" y="322" width="228" height="268" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="486" y="322" width="228" height="28" rx="8" fill="#1E5631" />
<rect x="486" y="336" width="228" height="14" rx="0" fill="#1E5631" />
<text x="496" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Traducir</text>
<text x="704" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">8</text>
<text x="496" y="375" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Tejedor de</text>
<text x="496" y="395" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Especificaciones</text>
<text x="496" y="415" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">aracne-weaver</text>
<text x="496" y="443" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="496" y="462" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Contratos OpenSpec y</text>
<text x="496" y="480" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">trace.json</text>
<text x="496" y="502" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="496" y="521" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Inspecciona los contratos;</text>
<text x="496" y="539" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">si hay inconsistencias,</text>
<text x="496" y="557" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">ajusta la historia</text>
<rect x="729" y="322" width="228" height="268" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="729" y="322" width="228" height="28" rx="8" fill="#1E5631" />
<rect x="729" y="336" width="228" height="14" rx="0" fill="#1E5631" />
<text x="739" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Descomponer a Construir</text>
<text x="947" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">9</text>
<text x="739" y="375" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Planificador de Olas</text>
<text x="739" y="395" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">aracne-sprint-planner</text>
<text x="739" y="423" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="739" y="442" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">sprint-plan.md: olas de</text>
<text x="739" y="460" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">trabajo paralelo</text>
<text x="739" y="482" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="739" y="501" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Asigna historias (un</text>
<text x="739" y="519" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">change por persona) y</text>
<text x="739" y="537" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">valida dependencias</text>
<rect x="972" y="322" width="228" height="268" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="972" y="322" width="228" height="28" rx="8" fill="#1E5631" />
<rect x="972" y="336" width="228" height="14" rx="0" fill="#1E5631" />
<text x="982" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700">Construir</text>
<text x="1190" y="342" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="13.5" font-weight="700" text-anchor="end">10</text>
<text x="982" y="375" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">Constructor SDD-ODD</text>
<text x="982" y="395" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13" font-weight="700">aracne-builder</text>
<text x="982" y="423" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="982" y="442" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Código y una prueba por</text>
<text x="982" y="460" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">escenario</text>
<text x="982" y="482" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="982" y="501" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">Supervisa la codificación;</text>
<text x="982" y="519" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">valida que no haya código</text>
<text x="982" y="537" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14">fuera de la spec</text>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Agentes 1 a 10 de 18: dieciséis base y dos opcionales</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>1. Analista de Requerimientos y CU</strong> (<code>bmad-agent-analyst</code>). <em>Fase:</em> Entender. <em>Produce:</em> Brief de producto o de adopción. <em>Control humano:</em> Valida casos de uso, intención y alcance pactado.</li>
                  <li><strong>2. Investigador CTeI, opcional</strong> (<code>aracne-ctei-scout</code>). <em>Fase:</em> Entender. <em>Produce:</em> research-brief.md con requisitos, épicas e historias candidatas. <em>Control humano:</em> El equipo de requerimientos acepta o descarta cada candidato.</li>
                  <li><strong>3. Consultor de Portafolio, opcional</strong> (<code>aracne-portfolio</code>). <em>Fase:</em> Entender a Construir. <em>Produce:</em> Productos y componentes de ATENEA relacionados, candidatos a reutilización. <em>Control humano:</em> Decide qué se reutiliza.</li>
                  <li><strong>4. Product Manager (PM)</strong> (<code>bmad-agent-pm</code>). <em>Fase:</em> Entender a Decidir. <em>Produce:</em> PRD con FR y NFR numerados. <em>Control humano:</em> Aprueba el PRD y la priorización de requisitos.</li>
                  <li><strong>5. Diseñador UX/UI</strong> (<code>bmad-agent-ux-designer</code>). <em>Fase:</em> Decidir. <em>Produce:</em> DESIGN.md y especificaciones UX-DR. <em>Control humano:</em> Aprueba el diseño de interacción, las pantallas y los contratos visuales.</li>
                  <li><strong>6. Arquitecto de Software</strong> (<code>bmad-agent-architect</code>). <em>Fase:</em> Decidir. <em>Produce:</em> ARCHITECTURE-SPINE.md y límites modulares. <em>Control humano:</em> Aprueba componentes, patrones, modelo de datos y contratos.</li>
                  <li><strong>7. Descompositor de Historias</strong> (skill de BMAD). <em>Fase:</em> Descomponer. <em>Produce:</em> Épicas e historias Given/When/Then. <em>Control humano:</em> Aprueba el desglose de historias antes de compilar contratos.</li>
                  <li><strong>8. Tejedor de Especificaciones</strong> (<code>aracne-weaver</code>). <em>Fase:</em> Traducir. <em>Produce:</em> Contratos OpenSpec y trace.json. <em>Control humano:</em> Inspecciona los contratos; si hay inconsistencias, ajusta la historia.</li>
                  <li><strong>9. Planificador de Olas</strong> (<code>aracne-sprint-planner</code>). <em>Fase:</em> Descomponer a Construir. <em>Produce:</em> sprint-plan.md: olas de trabajo paralelo. <em>Control humano:</em> Asigna historias (un change por persona) y valida dependencias.</li>
                  <li><strong>10. Constructor SDD-ODD</strong> (<code>aracne-builder</code>). <em>Fase:</em> Construir. <em>Produce:</em> Código y una prueba por escenario. <em>Control humano:</em> Supervisa la codificación; valida que no haya código fuera de la spec.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Tabla 6.1. Agentes base del arnés (1/2): rol, fase, artefacto de salida y supervisión humana, de Entender a Construir, con los dos opcionales</figcaption>
            </figure>
          </article>

          <!-- E4-3: Agentes base 2/2 (Tabla 6.1) [c4-arquitectura] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e4" data-item="c4-arquitectura" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
                <h2 style="margin-bottom:4px;">Agentes base de Aracne (2/2): verificar, revisar, integrar, cerrar y operar</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Los revisores vienen de Gentle-AI. En la versión 0.9.0 <code>aracne-cicd</code> abre la solicitud de integración con la CLI de GitHub; en Azure DevOps ese paso debe adaptarse.</p>
              </div>
              <svg viewBox="0 -2 1200 556" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tabla 6.1 (2/2): ocho agentes base, de verificar a operar, con su identificador, lo que producen y el control humano">
<rect x="0" y="2" width="18" height="18" rx="3" fill="#EBF5ED" stroke="#1E5631" stroke-width="2" />
<text x="26" y="17" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Subagente propio aracne-*</text>
<rect x="255.8" y="2" width="18" height="18" rx="3" fill="#FFF7ED" stroke="#B07A12" stroke-width="2" />
<text x="281.8" y="17" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Revisores de Gentle-AI</text>
<rect x="0" y="36" width="285" height="248" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="0" y="36" width="285" height="28" rx="8" fill="#1E5631" />
<rect x="0" y="50" width="285" height="14" rx="0" fill="#1E5631" />
<text x="12" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Verificar</text>
<text x="273" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="end">11</text>
<text x="12" y="91" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Verificador de Contratos y</text>
<text x="12" y="112" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">QA</text>
<text x="12" y="133" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">aracne-validator</text>
<text x="12" y="163" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="12" y="183" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Validación estricta, pruebas E2E</text>
<text x="12" y="201" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">e impacto en el grafo</text>
<text x="12" y="219" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="12" y="239" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">Exige el 100 % de pruebas en</text>
<text x="12" y="257" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">verde antes de autorizar el</text>
<text x="12" y="275" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">cierre</text>
<rect x="305" y="36" width="285" height="248" rx="8" fill="#FFF7ED" stroke="#B07A12" stroke-width="1.8" />
<rect x="305" y="36" width="285" height="28" rx="8" fill="#B07A12" />
<rect x="305" y="50" width="285" height="14" rx="0" fill="#B07A12" />
<text x="317" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Revisar</text>
<text x="578" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="end">12</text>
<text x="317" y="91" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Revisores</text>
<text x="317" y="112" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Multi-Perspectiva</text>
<text x="317" y="133" fill="#B07A12" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">review-* (Gentle-AI)</text>
<text x="317" y="163" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="317" y="183" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Dictámenes de riesgo y</text>
<text x="317" y="201" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">fiabilidad, y veredicto</text>
<text x="317" y="219" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="317" y="239" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">La líder técnica aprueba la</text>
<text x="317" y="257" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">calidad según los dictámenes</text>
<rect x="610" y="36" width="285" height="248" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="610" y="36" width="285" height="28" rx="8" fill="#1E5631" />
<rect x="610" y="50" width="285" height="14" rx="0" fill="#1E5631" />
<text x="622" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Integrar y Entregar</text>
<text x="883" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="end">13</text>
<text x="622" y="91" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Operador CI/CD e</text>
<text x="622" y="112" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Integración</text>
<text x="622" y="133" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">aracne-cicd</text>
<text x="622" y="163" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="622" y="183" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Commits atómicos y PR con traza</text>
<text x="622" y="201" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="622" y="221" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">Autoriza el merge a ramas</text>
<text x="622" y="239" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">protegidas y el despliegue</text>
<rect x="915" y="36" width="285" height="248" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="915" y="36" width="285" height="28" rx="8" fill="#1E5631" />
<rect x="915" y="50" width="285" height="14" rx="0" fill="#1E5631" />
<text x="927" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Cerrar</text>
<text x="1188" y="56" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="end">14</text>
<text x="927" y="91" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Cierre y Línea Base</text>
<text x="927" y="112" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">aracne-closer</text>
<text x="927" y="142" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="927" y="162" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Contrato archivado en archive/ y</text>
<text x="927" y="180" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">specs/</text>
<text x="927" y="198" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="927" y="218" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">Ratifica el cierre de la historia</text>
<text x="927" y="236" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">y su ingreso a la línea base</text>
<rect x="0" y="302" width="285" height="248" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="0" y="302" width="285" height="28" rx="8" fill="#1E5631" />
<rect x="0" y="316" width="285" height="14" rx="0" fill="#1E5631" />
<text x="12" y="322" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Transversal</text>
<text x="273" y="322" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="end">15</text>
<text x="12" y="357" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Clasificador de</text>
<text x="12" y="378" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Incidencias</text>
<text x="12" y="399" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">aracne-ticket</text>
<text x="12" y="429" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="12" y="449" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Enrutamiento: defecto a</text>
<text x="12" y="467" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">corrección, requerimiento a</text>
<text x="12" y="485" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">cambio</text>
<text x="12" y="503" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="12" y="523" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">Confirma la clasificación y</text>
<text x="12" y="541" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">autoriza abrir el flujo</text>
<rect x="305" y="302" width="285" height="248" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="305" y="302" width="285" height="28" rx="8" fill="#1E5631" />
<rect x="305" y="316" width="285" height="14" rx="0" fill="#1E5631" />
<text x="317" y="322" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Transversal</text>
<text x="578" y="322" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="end">16</text>
<text x="317" y="357" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Control de Cambios y</text>
<text x="317" y="378" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Alcance</text>
<text x="317" y="399" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">aracne-change</text>
<text x="317" y="429" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="317" y="449" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Clasificación de alcance y</text>
<text x="317" y="467" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">regeneración acotada</text>
<text x="317" y="485" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="317" y="505" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">Decide si amplía el alcance o</text>
<text x="317" y="523" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">remite a una nueva épica</text>
<rect x="610" y="302" width="285" height="248" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="610" y="302" width="285" height="28" rx="8" fill="#1E5631" />
<rect x="610" y="316" width="285" height="14" rx="0" fill="#1E5631" />
<text x="622" y="322" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Transversal</text>
<text x="883" y="322" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="end">17</text>
<text x="622" y="357" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Observabilidad y Estado</text>
<text x="622" y="378" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">aracne-status</text>
<text x="622" y="408" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="622" y="428" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Tablero web dashboard.html,</text>
<text x="622" y="446" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">inestabilidad y cobertura</text>
<text x="622" y="464" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="622" y="484" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">Dirección y líderes monitorean</text>
<text x="622" y="502" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">avance real y riesgos</text>
<rect x="915" y="302" width="285" height="248" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<rect x="915" y="302" width="285" height="28" rx="8" fill="#1E5631" />
<rect x="915" y="316" width="285" height="14" rx="0" fill="#1E5631" />
<text x="927" y="322" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700">Soporte</text>
<text x="1188" y="322" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="end">18</text>
<text x="927" y="357" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Salud del Entorno y</text>
<text x="927" y="378" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Diagnóstico</text>
<text x="927" y="399" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">aracne-doctor</text>
<text x="927" y="429" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Produce</text>
<text x="927" y="449" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Diagnóstico de preflight y</text>
<text x="927" y="467" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">detección de deriva</text>
<text x="927" y="485" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700">Control humano</text>
<text x="927" y="505" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">Ejecuta acciones correctivas ante</text>
<text x="927" y="523" fill="#1F536C" font-family="Space Grotesk,sans-serif" font-size="14.5">faltantes</text>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Agentes 11 a 18 de 18: los ocho base restantes</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>11. Verificador de Contratos y QA</strong> (<code>aracne-validator</code>). <em>Fase:</em> Verificar. <em>Produce:</em> Validación estricta, pruebas E2E e impacto en el grafo. <em>Control humano:</em> Exige el 100 % de pruebas en verde antes de autorizar el cierre.</li>
                  <li><strong>12. Revisores Multi-Perspectiva</strong> (review-* (Gentle-AI)). <em>Fase:</em> Revisar. <em>Produce:</em> Dictámenes de riesgo y fiabilidad, y veredicto. <em>Control humano:</em> La líder técnica aprueba la calidad según los dictámenes.</li>
                  <li><strong>13. Operador CI/CD e Integración</strong> (<code>aracne-cicd</code>). <em>Fase:</em> Integrar y Entregar. <em>Produce:</em> Commits atómicos y PR con traza. <em>Control humano:</em> Autoriza el merge a ramas protegidas y el despliegue.</li>
                  <li><strong>14. Cierre y Línea Base</strong> (<code>aracne-closer</code>). <em>Fase:</em> Cerrar. <em>Produce:</em> Contrato archivado en archive/ y specs/. <em>Control humano:</em> Ratifica el cierre de la historia y su ingreso a la línea base.</li>
                  <li><strong>15. Clasificador de Incidencias</strong> (<code>aracne-ticket</code>). <em>Fase:</em> Transversal. <em>Produce:</em> Enrutamiento: defecto a corrección, requerimiento a cambio. <em>Control humano:</em> Confirma la clasificación y autoriza abrir el flujo.</li>
                  <li><strong>16. Control de Cambios y Alcance</strong> (<code>aracne-change</code>). <em>Fase:</em> Transversal. <em>Produce:</em> Clasificación de alcance y regeneración acotada. <em>Control humano:</em> Decide si amplía el alcance o remite a una nueva épica.</li>
                  <li><strong>17. Observabilidad y Estado</strong> (<code>aracne-status</code>). <em>Fase:</em> Transversal. <em>Produce:</em> Tablero web dashboard.html, inestabilidad y cobertura. <em>Control humano:</em> Dirección y líderes monitorean avance real y riesgos.</li>
                  <li><strong>18. Salud del Entorno y Diagnóstico</strong> (<code>aracne-doctor</code>). <em>Fase:</em> Soporte. <em>Produce:</em> Diagnóstico de preflight y detección de deriva. <em>Control humano:</em> Ejecuta acciones correctivas ante faltantes.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Tabla 6.1. Agentes base del arnés (2/2): rol, fase, artefacto de salida y supervisión humana, de Verificar a Soporte</figcaption>
            </figure>
          </article>

          <!-- E4-4: Catálogo 1/2 (Tabla 6.2) [c4-catalogo] -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-catalogo">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
              <h2>Catálogo de comandos (1/2): del arranque al cierre y al control de cambios</h2>
              <ul class="slide-list">
                <li>
                  <strong>Once comandos <code>/sw:*</code>:</strong> el agente principal ejecuta cada uno como orquestador e invoca a los subagentes; en OpenCode se escriben <code>/sw-*</code>.
                </li>
                <li>
                  <strong>Cuatro familias de skills</strong> (método, planeación, mapa del código y revisión) completan el catálogo en la lámina siguiente.
                </li>
                <li>
                  <strong>Control humano en cada fila:</strong> el arnés propone; la persona aprueba, asigna o decide.
                </li>
                <li>
                  <strong>Versión 0.9.0:</strong> el anexo C define cada comando, subagente y skill.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.68rem,min(1.15vw,2.05vh),1.5rem);">
                  <caption>Tabla 6.2. Comandos y skills por etapa (1/2): disparador, fase, salida y control humano, del arranque al control de cambios (texto condensado)</caption>
                  <thead>
                    <tr>
                      <th style="width:30%;font-size:0.82em;">Comando o skill</th>
                      <th style="width:14%;font-size:0.82em;">Fase</th>
                      <th style="width:33%;font-size:0.82em;">Salida</th>
                      <th style="font-size:0.82em;">Control humano</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:new</code><br /><span style="font-size:0.84em;color:var(--subtext);">Proyecto o servicio nuevo; idea o requerimiento</span></span></td>
                      <td data-label="Fase"><strong>Entender a Traducir</strong></td>
                      <td data-label="Salida">Estudio CTeI opcional antes del brief; brief, PRD, arquitectura, UX, épicas, historias y contratos; no escribe código</td>
                      <td data-label="Control humano">Aprueba PRD, arquitectura e historias</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:adopt</code><br /><span style="font-size:0.84em;color:var(--subtext);">Sistema en operación; repositorio e insumos</span></span></td>
                      <td data-label="Fase"><strong>Entender a Traducir</strong></td>
                      <td data-label="Salida">Alcance acordado, mapa del código, PRD del área y línea base acotada</td>
                      <td data-label="Control humano">Acuerda el área; se detiene sin acuerdo</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:sprint</code><br /><span style="font-size:0.84em;color:var(--subtext);">Contratos listos y grafo de dependencias</span></span></td>
                      <td data-label="Fase"><strong>Descomponer</strong></td>
                      <td data-label="Salida">Olas de trabajo paralelo por dependencias técnicas reales</td>
                      <td data-label="Control humano">Asigna historias a desarrolladores</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:build</code><br /><span style="font-size:0.84em;color:var(--subtext);">Un contrato OpenSpec asignado</span></span></td>
                      <td data-label="Fase"><strong>Construir</strong></td>
                      <td data-label="Salida">Código, una prueba por escenario y tareas marcadas en tasks.md</td>
                      <td data-label="Control humano">Revisa y aprueba la integración</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:close</code><br /><span style="font-size:0.84em;color:var(--subtext);">Historias con tareas terminadas</span></span></td>
                      <td data-label="Fase"><strong>Cerrar</strong></td>
                      <td data-label="Salida">Contrato validado y archivado como línea base del sistema</td>
                      <td data-label="Control humano">Decide qué historias se cierran</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:change</code><br /><span style="font-size:0.84em;color:var(--subtext);">Requerimiento a mitad del desarrollo</span></span></td>
                      <td data-label="Fase"><strong>Transversal</strong></td>
                      <td data-label="Salida">Clasificación de alcance, documento fuente actualizado y regeneración acotada</td>
                      <td data-label="Control humano">Acepta o rechaza el cambio de alcance</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:bug</code><br /><span style="font-size:0.84em;color:var(--subtext);">Defecto frente a un contrato vigente</span></span></td>
                      <td data-label="Fase"><strong>Transversal</strong></td>
                      <td data-label="Salida">Corrección guiada por test, sin alterar el contrato ni el alcance</td>
                      <td data-label="Control humano">Revisa y aprueba la corrección</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:ticket</code><br /><span style="font-size:0.84em;color:var(--subtext);">Incidencia del sistema de tickets de ATENEA</span></span></td>
                      <td data-label="Fase"><strong>Transversal</strong></td>
                      <td data-label="Salida">Clasificación formal y enrutamiento a cambio o defecto; no resuelve</td>
                      <td data-label="Control humano">Confirma la ruta de resolución</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E4-5: Catálogo 2/2 (Tabla 6.2) [c4-catalogo] -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-catalogo">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
              <h2>Catálogo de comandos y skills (2/2): estado, soporte y cuatro familias de skills</h2>
              <ul class="slide-list">
                <li>
                  <strong>Estado y soporte:</strong> <code>/sw:status</code> da el tablero; <code>/sw:sync</code> actualiza las herramientas fijadas y <code>/sw:doctor</code> revisa la salud del arnés.
                </li>
                <li>
                  <strong>Skills:</strong> son doctrina del flujo y consulta del código; solo las de planeación y revisión llevan una decisión humana.
                </li>
                <li>
                  <strong>Pruebas:</strong> con el paquete congelado 0.9.0 pasaron los 241 casos de la suite. Desde una ruta con espacios fallan 21; la corrección ya está en el repositorio del arnés y sale en la versión siguiente.
                </li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.64rem,min(1.05vw,1.9vh),1.4rem);">
                  <caption>Tabla 6.2. Comandos y skills por etapa (2/2): comandos de estado y soporte, la instalación opcional de investigación y las cuatro familias de skills (texto condensado)</caption>
                  <thead>
                    <tr>
                      <th style="width:30%;font-size:0.82em;">Comando o skill</th>
                      <th style="width:14%;font-size:0.82em;">Fase</th>
                      <th style="width:33%;font-size:0.82em;">Salida</th>
                      <th style="font-size:0.82em;">Control humano</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:status</code><br /><span style="font-size:0.84em;color:var(--subtext);">Solicitud de estado del proyecto</span></span></td>
                      <td data-label="Fase"><strong>Transversal</strong></td>
                      <td data-label="Salida">Tablero interactivo; lectura de avance, inestabilidad y pendientes</td>
                      <td data-label="Control humano">Usa el tablero para priorizar</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:sync</code><br /><span style="font-size:0.84em;color:var(--subtext);">Diferencias con las versiones fijadas</span></span></td>
                      <td data-label="Fase"><strong>Soporte</strong></td>
                      <td data-label="Salida">Actualización controlada de las herramientas de versión fija</td>
                      <td data-label="Control humano">Autoriza la actualización</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>/sw:doctor</code><br /><span style="font-size:0.84em;color:var(--subtext);">Verificación de salud del arnés</span></span></td>
                      <td data-label="Fase"><strong>Soporte</strong></td>
                      <td data-label="Salida">Estado de instalación, preflight y coherencia entre plan y contratos</td>
                      <td data-label="Control humano">Resuelve lo faltante</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><code>aracne-sdlc-ai init --only research</code><br /><span style="font-size:0.84em;color:var(--subtext);">Instalación opcional, fuera del paquete 0.9.0</span></span></td>
                      <td data-label="Fase"><strong>Soporte</strong></td>
                      <td data-label="Salida">Agentes <code>aracne-ctei-scout</code> y <code>aracne-portfolio</code> con sus servidores MCP</td>
                      <td data-label="Control humano">Decide si los instala</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><strong>Skill de método</strong><br /><span style="font-size:0.84em;color:var(--subtext);">Arrancar, adoptar, procesar requerimientos o tickets, planear y construir</span></span></td>
                      <td data-label="Fase"><strong>Todas</strong></td>
                      <td data-label="Salida">Reglas procedimentales del método para el agente activo</td>
                      <td data-label="Control humano">Ninguno propio (doctrina del flujo)</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><strong>Skills de planeación</strong><br /><span style="font-size:0.84em;color:var(--subtext);">Invocadas durante la concepción o la adopción</span></span></td>
                      <td data-label="Fase"><strong>Entender a Descomponer</strong></td>
                      <td data-label="Salida">PRD, arquitectura, contratos UX, épicas e historias de usuario</td>
                      <td data-label="Control humano">Aprueba cada artefacto generado</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><strong>Skill del mapa del código</strong><br /><span style="font-size:0.84em;color:var(--subtext);">Consulta de estructura, rutas o dependencias</span></span></td>
                      <td data-label="Fase"><strong>Entender y Construir</strong></td>
                      <td data-label="Salida">Respuestas precisas sobre el grafo AST del código real</td>
                      <td data-label="Control humano">Ninguno propio (consulta determinista)</td>
                    </tr>
                    <tr>
                      <td data-label="Comando o skill"><span><strong>Skills de revisión</strong><br /><span style="font-size:0.84em;color:var(--subtext);">Auditoría estática previa a la integración</span></span></td>
                      <td data-label="Fase"><strong>Revisar y Cerrar</strong></td>
                      <td data-label="Salida">Dictámenes multi-perspectiva y veredicto de calidad</td>
                      <td data-label="Control humano">Decide si aprueba la integración</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E4-6: Instalación y estructura (Figura 6.2) [c4-instalacion] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e4" data-item="c4-instalacion" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
                <h2 style="margin-bottom:4px;">Instalación y estructura del proyecto: un comando y dos plataformas</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Versión Aracne-SDLC-AI 0.9.0. Las dos plataformas comparten <code>.aracne-sdlc-ai/</code>; cambia dónde guarda cada una sus piezas. <strong>Versiones fijadas:</strong> BMAD 6.11.0, OpenSpec 1.10.0, graphify 0.8.37 y Gentle-AI 4.1.1. <strong>Plataformas:</strong> Linux y macOS; en Windows, solo dentro de <abbr title="Windows Subsystem for Linux 2">WSL2</abbr>. El zip 0.9.0 se instala desde una ruta sin espacios.</p>
              </div>
              <svg viewBox="0 0 1200 548" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figura 6.2: estructura de carpetas de un proyecto con Aracne, parte común y diferencias entre Claude Code y OpenCode">
<rect x="0" y="0" width="330" height="44" rx="7" fill="#1B2029" />
<text x="165" y="29" fill="#FFFFFF" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="19" font-weight="700" text-anchor="middle">npx aracne-sdlc-ai init</text>
<text x="350" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">Monta el arnés dentro del repositorio del caso: todo lo que el método produce queda versionado</text>
<text x="350" y="39" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15">junto al código.</text>
<rect x="0" y="62" width="392" height="474" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.6" />
<rect x="0" y="62" width="392" height="34" rx="8" fill="#2C6B87" />
<rect x="0" y="80" width="392" height="16" rx="0" fill="#2C6B87" />
<text x="14" y="85" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700">Común a las dos plataformas</text>
<text x="14" y="122" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">proyecto/</text>
<text x="28" y="144" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">docs/architecture-base.md</text>
<text x="242.5" y="144" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">reglas del proyecto</text>
<text x="28" y="166" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">.aracne-sdlc-ai/</text>
<text x="42" y="188" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">config.json</text>
<text x="143.1" y="188" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">idioma</text>
<text x="42" y="210" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">bmad/planning-artifacts/</text>
<text x="56" y="232" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">prd, arquitectura, UX</text>
<text x="56" y="254" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">epics.md</text>
<text x="132.8" y="254" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">historias G/W/T</text>
<text x="42" y="276" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">openspec/</text>
<text x="56" y="298" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">changes/eNsM-*/</text>
<text x="189.5" y="298" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">contratos</text>
<text x="56" y="320" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">changes/archive/</text>
<text x="56" y="342" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">specs/</text>
<text x="116.6" y="342" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">línea base</text>
<text x="42" y="364" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">trace.json</text>
<text x="135" y="364" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">traza</text>
<text x="42" y="386" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">sprint-plan.md</text>
<text x="167.4" y="386" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">olas</text>
<text x="42" y="408" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">changelog.jsonl</text>
<text x="175.5" y="408" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">bitácora</text>
<text x="42" y="430" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">bin/engram, engram/</text>
<text x="207.9" y="430" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">memoria</text>
<text x="42" y="452" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">dashboard.html</text>
<text x="167.4" y="452" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">tablero</text>
<text x="28" y="474" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">_bmad/</text>
<text x="88.6" y="474" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">instalación de BMAD</text>
<text x="28" y="496" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">graphify-out/graph.json</text>
<text x="226.3" y="496" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">mapa del código</text>
<text x="28" y="518" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">.gitignore, .graphifyignore</text>
<rect x="404" y="62" width="392" height="474" rx="8" fill="#FFFFFF" stroke="#1E5631" stroke-width="1.6" />
<rect x="404" y="62" width="392" height="34" rx="8" fill="#1E5631" />
<rect x="404" y="80" width="392" height="16" rx="0" fill="#1E5631" />
<text x="418" y="85" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700">Claude Code</text>
<text x="418" y="122" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">proyecto/</text>
<text x="432" y="144" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">.claude/</text>
<text x="446" y="166" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">commands/sw/*.md</text>
<text x="587.6" y="166" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">11 comandos /sw:*</text>
<text x="446" y="188" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">agents/aracne-*.md</text>
<text x="603.8" y="188" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">10 subagentes</text>
<text x="446" y="210" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">agents/review-*.md, jd-*.md</text>
<text x="676.7" y="210" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">8 de Gentle-AI</text>
<text x="446" y="232" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">skills/aracne-sdlc-ai/</text>
<text x="636.2" y="232" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">método</text>
<text x="446" y="254" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">skills/bmad-*/</text>
<text x="571.4" y="254" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">planeación</text>
<text x="446" y="276" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">skills/graphify/</text>
<text x="446" y="298" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">skills/judgment-day, work-unit-commits,</text>
<text x="446" y="320" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">branch-pr, chained-pr/</text>
<text x="446" y="342" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">settings.json</text>
<text x="563.3" y="342" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">hooks de graphify</text>
<text x="432" y="364" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">CLAUDE.md</text>
<text x="432" y="386" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">.mcp.json</text>
<text x="516.9" y="386" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">servidor Engram</text>
<rect x="808" y="62" width="392" height="474" rx="8" fill="#FFFFFF" stroke="#B07A12" stroke-width="1.6" />
<rect x="808" y="62" width="392" height="34" rx="8" fill="#B07A12" />
<rect x="808" y="80" width="392" height="16" rx="0" fill="#B07A12" />
<text x="822" y="85" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700">OpenCode</text>
<text x="822" y="122" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">proyecto/</text>
<text x="836" y="144" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">.opencode/</text>
<text x="850" y="166" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">commands/sw-*.md</text>
<text x="991.6" y="166" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">11 comandos /sw-*</text>
<text x="850" y="188" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">agents/aracne-*.md</text>
<text x="1007.8" y="188" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">10 subagentes</text>
<text x="850" y="210" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">skills/graphify/</text>
<text x="836" y="232" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">.agents/skills/</text>
<text x="969.5" y="232" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">método y planeación</text>
<text x="836" y="254" fill="#1F536C" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5" font-weight="700">.config/opencode/skills/</text>
<text x="1042.4" y="254" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">skills de Gentle-AI</text>
<text x="836" y="276" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">AGENTS.md</text>
<text x="836" y="298" fill="#1B2029" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13.5">opencode.json</text>
<text x="953.3" y="298" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12.5" font-style="italic">servidor Engram</text>
<rect x="418" y="418" width="364" height="104" rx="6" fill="#EBF5ED" />
<text x="430" y="440" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13.5">Claude Code lee comandos, subagentes y skills</text>
<text x="430" y="458" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13.5">de .claude/ y la memoria de .mcp.json.</text>
<text x="430" y="476" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13.5">Se invoca con /sw:build.</text>
<rect x="822" y="376" width="364" height="146" rx="6" fill="#FFF7ED" />
<text x="834" y="398" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13.5">OpenCode lee .opencode/ y .agents/skills/; la</text>
<text x="834" y="416" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13.5">memoria, de opencode.json.</text>
<text x="834" y="438" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13.5">Se invoca con /sw-build.</text>
<text x="834" y="460" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13.5">Gentle-AI registra sus revisores en la</text>
<text x="834" y="478" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13.5">configuración global del usuario.</text>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Instalación: <code>npx aracne-sdlc-ai init</code></p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>Común a las dos plataformas.</strong> <code>docs/architecture-base.md</code> (reglas del proyecto); <code>.aracne-sdlc-ai/</code> con <code>config.json</code>, artefactos de BMAD (<code>epics.md</code>), <code>openspec/</code> (<code>changes/</code>, <code>archive/</code>, <code>specs/</code> como línea base), <code>trace.json</code>, <code>sprint-plan.md</code>, <code>changelog.jsonl</code>, memoria Engram y <code>dashboard.html</code>; <code>_bmad/</code> (instalación de BMAD); <code>graphify-out/graph.json</code> (mapa del código); <code>.gitignore</code> y <code>.graphifyignore</code>.</li>
                  <li><strong>Claude Code.</strong> <code>.claude/commands/sw/*.md</code> (11 comandos <code>/sw:*</code>), <code>agents/aracne-*.md</code> (10 subagentes), <code>agents/review-*.md</code> y <code>jd-*.md</code> (8 de Gentle-AI), <code>skills/</code> (método, planeación, graphify, judgment-day, work-unit-commits, branch-pr y chained-pr), <code>settings.json</code> (hooks de graphify), <code>CLAUDE.md</code> y <code>.mcp.json</code> (servidor Engram).</li>
                  <li><strong>OpenCode.</strong> <code>.opencode/commands/sw-*.md</code> (11 comandos <code>/sw-*</code>), <code>agents/aracne-*.md</code>, <code>skills/graphify/</code>; <code>.agents/skills/</code> (método y planeación), <code>.config/opencode/skills/</code> (skills de Gentle-AI), <code>AGENTS.md</code> y <code>opencode.json</code> (servidor Engram).</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 6.2 — Estructura de un proyecto con Aracne-SDLC-AI 0.9.0: la parte común y lo que cambia entre Claude Code y OpenCode</figcaption>
            </figure>
          </article>

          <!-- E4-7: Flujos de interacción (Figura 6.3) [c4-flujos-interaccion] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e4" data-item="c4-flujos-interaccion" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
                <h2 style="margin-bottom:4px;">Flujos de interacción entre agentes: una historia, de la idea a la línea base</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El agente principal orquesta cada comando: carga el contexto, invoca a los subagentes y devuelve el resultado a la persona. Los subagentes trabajan con contexto y herramientas acotados.</p>
              </div>
              <svg viewBox="-4 -4 1208 606" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figura 6.3: diagrama de secuencia entre diez participantes, en seis fases y con tres puertas humanas">
<defs>
<marker id="a63b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
<marker id="a63k" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#5B6472" /></marker>
</defs>
<rect x="0" y="58" width="1200" height="114" rx="0" fill="#F4F6F9" />
<line x1="0" y1="172" x2="1200" y2="172" stroke="#FFFFFF" stroke-width="2" />
<text x="8" y="111.5" fill="#1F2D4D" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Entender</text>
<text x="8" y="127.5" fill="#1F2D4D" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">y Decidir</text>
<rect x="0" y="172" width="1200" height="62" rx="0" fill="#F4F6F9" />
<line x1="0" y1="234" x2="1200" y2="234" stroke="#FFFFFF" stroke-width="2" />
<text x="8" y="207.5" fill="#1F2D4D" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Traducir</text>
<rect x="0" y="234" width="1200" height="88" rx="0" fill="#F4F6F9" />
<line x1="0" y1="322" x2="1200" y2="322" stroke="#FFFFFF" stroke-width="2" />
<text x="8" y="282.5" fill="#1F2D4D" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Descomponer</text>
<rect x="0" y="322" width="1200" height="114" rx="0" fill="#F4F6F9" />
<line x1="0" y1="436" x2="1200" y2="436" stroke="#FFFFFF" stroke-width="2" />
<text x="8" y="375.5" fill="#1F2D4D" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Construir</text>
<text x="8" y="391.5" fill="#1F2D4D" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">y verificar</text>
<rect x="0" y="436" width="1200" height="62" rx="0" fill="#F4F6F9" />
<line x1="0" y1="498" x2="1200" y2="498" stroke="#FFFFFF" stroke-width="2" />
<text x="8" y="471.5" fill="#1F2D4D" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Integrar</text>
<rect x="0" y="498" width="1200" height="62" rx="0" fill="#F4F6F9" />
<line x1="0" y1="560" x2="1200" y2="560" stroke="#FFFFFF" stroke-width="2" />
<text x="8" y="533.5" fill="#1F2D4D" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Cerrar</text>
<line x1="140" y1="46" x2="140" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="248" y1="46" x2="248" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="356" y1="46" x2="356" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="464" y1="46" x2="464" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="572" y1="46" x2="572" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="680" y1="46" x2="680" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="788" y1="46" x2="788" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="896" y1="46" x2="896" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="1004" y1="46" x2="1004" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<line x1="1112" y1="46" x2="1112" y2="560" stroke="#9AA5B4" stroke-width="1" stroke-dasharray="4,4" />
<path d="M140 86 H248" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="77.6" y="67" width="232.8" height="16" rx="3" fill="#F4F6F9" />
<text x="194" y="80" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">/sw:new: idea y arquitectura base</text>
<path d="M248 112 H356" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="202.5" y="93" width="199" height="16" rx="3" fill="#F4F6F9" />
<text x="302" y="106" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">brief, PRD, UX, arquitectura</text>
<path d="M356 138 H248" stroke="#5B6472" stroke-width="1.6" fill="none" stroke-dasharray="6,4" marker-end="url(#a63k)" />
<rect x="216" y="119" width="172" height="16" rx="3" fill="#F4F6F9" />
<text x="302" y="132" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">épicas e historias G/W/T</text>
<path d="M248 164 H151" stroke="#5B6472" stroke-width="1.6" fill="none" stroke-dasharray="6,4" marker-end="url(#a63k)" />
<rect x="158" y="145" width="165.2" height="16" rx="3" fill="#F4F6F9" />
<text x="240.6" y="158" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">aprobar PRD e historias</text>
<circle cx="140" cy="164" r="7.5" fill="#B42318" />
<path d="M248 200 H464" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="293.6" y="181" width="124.8" height="16" rx="3" fill="#F4F6F9" />
<text x="356" y="194" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">epics.md aprobado</text>
<path d="M464 226 H248" stroke="#5B6472" stroke-width="1.6" fill="none" stroke-dasharray="6,4" marker-end="url(#a63k)" />
<rect x="280.1" y="207" width="151.8" height="16" rx="3" fill="#F4F6F9" />
<text x="356" y="220" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">contratos, trace.json</text>
<path d="M140 262 H248" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="155.2" y="243" width="77.5" height="16" rx="3" fill="#F4F6F9" />
<text x="194" y="256" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">/sw:sprint</text>
<path d="M248 288 H572" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="357.8" y="269" width="104.5" height="16" rx="3" fill="#F4F6F9" />
<text x="410" y="282" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">olas y reparto</text>
<path d="M572 314 H151" stroke="#5B6472" stroke-width="1.6" fill="none" stroke-dasharray="6,4" marker-end="url(#a63k)" />
<rect x="290.2" y="295" width="131.5" height="16" rx="3" fill="#F4F6F9" />
<text x="356" y="308" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">aprobar el reparto</text>
<circle cx="140" cy="314" r="7.5" fill="#B42318" />
<path d="M140 350 H248" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="141.8" y="331" width="104.5" height="16" rx="3" fill="#F4F6F9" />
<text x="194" y="344" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">/sw:build eNsM</text>
<path d="M248 376 H680" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="421.9" y="357" width="84.2" height="16" rx="3" fill="#F4F6F9" />
<text x="464" y="370" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">un contrato</text>
<path d="M680 402 H788" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="675" y="383" width="118" height="16" rx="3" fill="#F4F6F9" />
<text x="734" y="396" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">código y pruebas</text>
<path d="M788 428 H896" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="806.6" y="409" width="70.8" height="16" rx="3" fill="#F4F6F9" />
<text x="842" y="422" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">veredicto</text>
<path d="M896 464 H1004" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="911.2" y="445" width="77.5" height="16" rx="3" fill="#F4F6F9" />
<text x="950" y="458" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">dictámenes</text>
<path d="M1004 490 H151" stroke="#5B6472" stroke-width="1.6" fill="none" stroke-dasharray="6,4" marker-end="url(#a63k)" />
<rect x="371.2" y="471" width="401.5" height="16" rx="3" fill="#F4F6F9" />
<text x="572" y="484" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">commits y PR con traza; la persona autoriza la integración</text>
<circle cx="140" cy="490" r="7.5" fill="#B42318" />
<path d="M140 526 H248" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="158.6" y="507" width="70.8" height="16" rx="3" fill="#F4F6F9" />
<text x="194" y="520" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">/sw:close</text>
<path d="M248 552 H1112" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<rect x="580.5" y="533" width="199" height="16" rx="3" fill="#F4F6F9" />
<text x="680" y="546" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" text-anchor="middle">validar y archivar en specs/</text>
<rect x="88" y="0" width="104" height="46" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.6" />
<text x="140" y="28" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">Persona</text>
<rect x="196" y="0" width="104" height="46" rx="6" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.6" />
<text x="248" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">Orquestador</text>
<text x="248" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">/sw:*</text>
<rect x="304" y="0" width="104" height="46" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.6" />
<text x="356" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">Agentes</text>
<text x="356" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">BMAD</text>
<rect x="412" y="0" width="104" height="46" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="464" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">aracne-</text>
<text x="464" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">weaver</text>
<rect x="520" y="0" width="104" height="46" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="572" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">aracne-</text>
<text x="572" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">sprint-planner</text>
<rect x="628" y="0" width="104" height="46" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="680" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">aracne-</text>
<text x="680" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">builder</text>
<rect x="736" y="0" width="104" height="46" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="788" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">aracne-</text>
<text x="788" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">validator</text>
<rect x="844" y="0" width="104" height="46" rx="6" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.6" />
<text x="896" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">Revisores</text>
<text x="896" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">Gentle-AI</text>
<rect x="952" y="0" width="104" height="46" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="1004" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">aracne-</text>
<text x="1004" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">cicd</text>
<rect x="1060" y="0" width="104" height="46" rx="6" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="1112" y="19" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">aracne-</text>
<text x="1112" y="35" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" text-anchor="middle">closer</text>
<circle cx="10" cy="583" r="7.5" fill="#B42318" />
<text x="24" y="588" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Puerta humana: aprobar historias, el reparto e integración (merge)</text>
<rect x="500" y="573" width="16" height="16" rx="3" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.5" />
<text x="524" y="588" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Subagente propio de Aracne</text>
<path d="M740 582 H774" stroke="#2C6B87" stroke-width="1.8" fill="none" marker-end="url(#a63b)" />
<text x="782" y="588" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Invocación</text>
<path d="M880 582 H914" stroke="#5B6472" stroke-width="1.6" fill="none" stroke-dasharray="6,4" marker-end="url(#a63k)" />
<text x="922" y="588" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13">Respuesta al llamador</text>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Una historia, de la idea a la línea base</p>
                <p class="sched-h">Entender y Decidir</p>
                <ol class="slide-list" style="margin:4px 0 8px;" start="1">
                  <li><strong>Persona</strong> invoca a <strong>Orquestador</strong>: /sw:new: idea y arquitectura base</li>
                  <li><strong>Orquestador</strong> invoca a <strong>Agentes BMAD</strong>: brief, PRD, UX, arquitectura</li>
                  <li><strong>Agentes BMAD</strong> responde a <strong>Orquestador</strong>: épicas e historias G/W/T</li>
                  <li><strong>Orquestador</strong> responde a <strong>Persona</strong>: aprobar PRD e historias <span class="pill pill--risk">Puerta humana</span></li>
                </ol>
                <p class="sched-h">Traducir</p>
                <ol class="slide-list" style="margin:4px 0 8px;" start="5">
                  <li><strong>Orquestador</strong> invoca a <strong>aracne-weaver</strong>: epics.md aprobado</li>
                  <li><strong>aracne-weaver</strong> responde a <strong>Orquestador</strong>: contratos, trace.json</li>
                </ol>
                <p class="sched-h">Descomponer</p>
                <ol class="slide-list" style="margin:4px 0 8px;" start="7">
                  <li><strong>Persona</strong> invoca a <strong>Orquestador</strong>: /sw:sprint</li>
                  <li><strong>Orquestador</strong> invoca a <strong>aracne-sprint-planner</strong>: olas y reparto</li>
                  <li><strong>aracne-sprint-planner</strong> responde a <strong>Persona</strong>: aprobar el reparto <span class="pill pill--risk">Puerta humana</span></li>
                </ol>
                <p class="sched-h">Construir y verificar</p>
                <ol class="slide-list" style="margin:4px 0 8px;" start="10">
                  <li><strong>Persona</strong> invoca a <strong>Orquestador</strong>: /sw:build eNsM</li>
                  <li><strong>Orquestador</strong> invoca a <strong>aracne-builder</strong>: un contrato</li>
                  <li><strong>aracne-builder</strong> invoca a <strong>aracne-validator</strong>: código y pruebas</li>
                  <li><strong>aracne-validator</strong> invoca a <strong>Revisores Gentle-AI</strong>: veredicto</li>
                </ol>
                <p class="sched-h">Integrar</p>
                <ol class="slide-list" style="margin:4px 0 8px;" start="14">
                  <li><strong>Revisores Gentle-AI</strong> invoca a <strong>aracne-cicd</strong>: dictámenes</li>
                  <li><strong>aracne-cicd</strong> responde a <strong>Persona</strong>: commits y PR con traza; la persona autoriza la integración <span class="pill pill--risk">Puerta humana</span></li>
                </ol>
                <p class="sched-h">Cerrar</p>
                <ol class="slide-list" style="margin:4px 0 8px;" start="16">
                  <li><strong>Persona</strong> invoca a <strong>Orquestador</strong>: /sw:close</li>
                  <li><strong>Orquestador</strong> invoca a <strong>aracne-closer</strong>: validar y archivar en specs/</li>
                </ol>
              </div>
              <figcaption class="fig-caption">Figura 6.3 — Interacción entre agentes para una historia, de la idea a la línea base. Verde: subagentes propios de Aracne; flechas continuas: invocaciones; discontinuas: respuestas</figcaption>
            </figure>
          </article>

          <!-- E4-8: Control humano y ejemplo (Figura 6.4) [c4-control-humano] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e4" data-item="c4-control-humano" data-tone="rose">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
                <h2 style="margin-bottom:4px;">Puntos de control humano y ejemplo de punta a punta: del requerimiento a la puesta en marcha</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Caso Campus 2600 en Hēma: los pasos 4 a 6 ya corrieron sobre la reconstrucción de la Universidad (14 historias, 14 contratos, 3 olas); el resto es ilustrativo. Aracne llega hasta la solicitud de integración y la línea base; el despliegue lo ejecuta el pipeline de ATENEA con autorización humana.</p>
              </div>
              <svg viewBox="-4 -4 1208 536" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figura 6.4: recorrido ideal de los pasos 0 a 13, con siete puertas humanas, y las tres puertas del capítulo 6">
<defs>
<marker id="a64b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
<marker id="a64k" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#5B6472" /></marker>
</defs>
<rect x="0" y="16" width="150" height="104" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="75" y="64" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#1E5631" font-size="17">0</tspan> init y doctor</text>
<text x="75" y="82.8" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">en el repositorio</text>
<rect x="175" y="16" width="150" height="104" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="250" y="64" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#2C6B87" font-size="17">1</tspan> Arquitectura</text>
<text x="250" y="82.8" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">base del área</text>
<rect x="350" y="16" width="150" height="104" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="425" y="64" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#1E5631" font-size="17">2</tspan> /sw:adopt con el</text>
<text x="425" y="82.8" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">grabación y prototipo</text>
<rect x="525" y="16" width="150" height="104" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="600" y="54.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#1E5631" font-size="17">3</tspan> PRD, UX y</text>
<text x="600" y="73.4" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">arquitectura</text>
<text x="600" y="92.3" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">(BMAD)</text>
<rect x="700" y="16" width="150" height="104" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="775" y="64" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#1E5631" font-size="17">4</tspan> Épicas e</text>
<text x="775" y="82.8" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">historias G/W/T</text>
<rect x="875" y="16" width="150" height="104" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="950" y="54.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#1E5631" font-size="17">5</tspan> Contratos y</text>
<text x="950" y="73.4" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">traza</text>
<text x="950" y="92.3" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">(aracne-weaver)</text>
<rect x="1050" y="16" width="150" height="104" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="1125" y="64" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#1E5631" font-size="17">6</tspan> Olas de trabajo</text>
<text x="1125" y="82.8" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">(/sw:sprint)</text>
<rect x="1050" y="176" width="150" height="104" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="1125" y="214.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#1E5631" font-size="17">7</tspan> /sw:build:</text>
<text x="1125" y="233.4" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">pruebas, código,</text>
<text x="1125" y="252.3" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">revisión, PR</text>
<rect x="875" y="176" width="150" height="104" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.8" stroke-dasharray="7,4" />
<text x="950" y="214.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#2C6B87" font-size="17">8</tspan> Integración</text>
<text x="950" y="233.4" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">continua (Azure</text>
<text x="950" y="252.3" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">Pipelines)</text>
<rect x="700" y="176" width="150" height="104" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="775" y="224" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#1E5631" font-size="17">9</tspan> /sw:close:</text>
<text x="775" y="242.8" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">línea base</text>
<rect x="525" y="176" width="150" height="104" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.8" stroke-dasharray="7,4" />
<text x="600" y="224" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#2C6B87" font-size="17">10</tspan> Despliegue</text>
<text x="600" y="242.8" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">a QA</text>
<rect x="350" y="176" width="150" height="104" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="425" y="214.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#2C6B87" font-size="17">11</tspan> Validación en</text>
<text x="425" y="233.4" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">preproducción</text>
<text x="425" y="252.3" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">y firma</text>
<rect x="175" y="176" width="150" height="104" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.8" stroke-dasharray="7,4" />
<text x="250" y="214.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#2C6B87" font-size="17">12</tspan> Despliegue a</text>
<text x="250" y="233.4" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">producción</text>
<text x="250" y="252.3" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">autorizado</text>
<rect x="0" y="176" width="150" height="104" rx="8" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.8" />
<text x="75" y="214.6" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle"><tspan font-weight="700" fill="#2C6B87" font-size="17">13</tspan> Puesta en</text>
<text x="75" y="233.4" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">marcha y</text>
<text x="75" y="252.3" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5" text-anchor="middle">operación</text>
<path d="M152 68 H171" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M327 68 H346" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M502 68 H521" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M677 68 H696" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M852 68 H871" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M1027 68 H1046" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M1048 228 H1029" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M873 228 H854" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M698 228 H679" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M523 228 H504" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M348 228 H329" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M173 228 H154" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<path d="M1125 122 V174" stroke="#2C6B87" stroke-width="2" fill="none" marker-end="url(#a64b)" />
<circle cx="496" cy="20" r="8" fill="#B42318" stroke="#FFFFFF" stroke-width="1.5" />
<circle cx="671" cy="20" r="8" fill="#B42318" stroke="#FFFFFF" stroke-width="1.5" />
<circle cx="846" cy="20" r="8" fill="#B42318" stroke="#FFFFFF" stroke-width="1.5" />
<circle cx="1196" cy="20" r="8" fill="#B42318" stroke="#FFFFFF" stroke-width="1.5" />
<circle cx="1196" cy="180" r="8" fill="#B42318" stroke="#FFFFFF" stroke-width="1.5" />
<circle cx="496" cy="180" r="8" fill="#B42318" stroke="#FFFFFF" stroke-width="1.5" />
<circle cx="321" cy="180" r="8" fill="#B42318" stroke="#FFFFFF" stroke-width="1.5" />
<path d="M75 282 V312 H1125 V283" stroke="#5B6472" stroke-width="1.8" fill="none" stroke-dasharray="6,4" marker-end="url(#a64k)" />
<rect x="250" y="316" width="700" height="22" rx="3" fill="#FFFFFF" />
<text x="600" y="332" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14" text-anchor="middle">cambios (/sw:change), defectos (/sw:bug) e incidencias (/sw:ticket) vuelven al flujo</text>
<text x="0" y="372" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700">Las tres puertas humanas que no se delegan (§6.6)</text>
<rect x="0" y="384" width="388" height="106" rx="8" fill="#FFF7ED" stroke="#B07A12" stroke-width="1.6" />
<circle cx="26" cy="412" r="14" fill="#B42318" />
<text x="26" y="418" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">1</text>
<text x="50" y="418" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700">Aprobar el PRD y las historias</text>
<text x="14" y="446" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">Antes de que aracne-weaver las traduzca a</text>
<text x="14" y="464" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">contratos.</text>
<rect x="406" y="384" width="388" height="106" rx="8" fill="#FFF7ED" stroke="#B07A12" stroke-width="1.6" />
<circle cx="432" cy="412" r="14" fill="#B42318" />
<text x="432" y="418" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">2</text>
<text x="456" y="418" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700">Aprobar el reparto de las olas</text>
<text x="420" y="446" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">Un contrato por persona, según las</text>
<text x="420" y="464" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">dependencias.</text>
<rect x="812" y="384" width="388" height="106" rx="8" fill="#FFF7ED" stroke="#B07A12" stroke-width="1.6" />
<circle cx="838" cy="412" r="14" fill="#B42318" />
<text x="838" y="418" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700" text-anchor="middle">3</text>
<text x="862" y="418" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="16.5" font-weight="700">Autorizar la integración</text>
<text x="826" y="446" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">aracne-cicd nunca hace merge ni push a ramas</text>
<text x="826" y="464" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">protegidas, ni despliega sin autorización</text>
<text x="826" y="482" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="14">humana explícita.</text>
<rect x="0" y="507" width="22" height="18" rx="4" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="30" y="522" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Arnés</text>
<rect x="100" y="507" width="22" height="18" rx="4" fill="#FFFFFF" stroke="#2C6B87" stroke-width="1.6" />
<text x="130" y="522" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Persona</text>
<rect x="214" y="507" width="22" height="18" rx="4" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.6" stroke-dasharray="7,4" />
<text x="244" y="522" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Azure DevOps</text>
<circle cx="376" cy="516" r="7.5" fill="#B42318" />
<text x="390" y="522" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">Puerta humana (siete en el recorrido: pasos 2, 3, 4, 6, 7, 11 y 12)</text>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Recorrido ideal: pasos 0 a 13</p>
                <ol class="slide-list" start="0" style="margin:8px 0;">
                  <li><strong>0.</strong> init y doctor en el repositorio <em>(Arnés)</em></li>
                  <li><strong>1.</strong> Arquitectura base del área <em>(Persona)</em></li>
                  <li><strong>2.</strong> /sw:adopt con la grabación y el prototipo <em>(Arnés)</em> <span class="pill pill--risk">Puerta humana</span></li>
                  <li><strong>3.</strong> PRD, UX y arquitectura (BMAD) <em>(Arnés)</em> <span class="pill pill--risk">Puerta humana</span></li>
                  <li><strong>4.</strong> Épicas e historias G/W/T <em>(Arnés)</em> <span class="pill pill--risk">Puerta humana</span></li>
                  <li><strong>5.</strong> Contratos y traza (aracne-weaver) <em>(Arnés)</em></li>
                  <li><strong>6.</strong> Olas de trabajo (/sw:sprint) <em>(Arnés)</em> <span class="pill pill--risk">Puerta humana</span></li>
                  <li><strong>7.</strong> /sw:build: pruebas, código, revisión, PR <em>(Arnés)</em> <span class="pill pill--risk">Puerta humana</span></li>
                  <li><strong>8.</strong> Integración continua (Azure Pipelines) <em>(Azure DevOps)</em></li>
                  <li><strong>9.</strong> /sw:close: línea base <em>(Arnés)</em></li>
                  <li><strong>10.</strong> Despliegue a QA <em>(Azure DevOps)</em></li>
                  <li><strong>11.</strong> Validación en preproducción y firma <em>(Persona)</em> <span class="pill pill--risk">Puerta humana</span></li>
                  <li><strong>12.</strong> Despliegue a producción autorizado <em>(Azure DevOps)</em> <span class="pill pill--risk">Puerta humana</span></li>
                  <li><strong>13.</strong> Puesta en marcha y operación <em>(Persona)</em></li>
                </ol>
                <p class="sched-note">Tras la puesta en marcha, los cambios (<code>/sw:change</code>), defectos (<code>/sw:bug</code>) e incidencias (<code>/sw:ticket</code>) vuelven al flujo.</p>
                <p class="sched-title">Tres puertas humanas que no se delegan (&sect;6.6)</p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong>1. Aprobar el PRD y las historias</strong>, antes de que <code>aracne-weaver</code> las traduzca a contratos.</li>
                  <li><strong>2. Aprobar el reparto de las olas</strong>, un contrato por persona.</li>
                  <li><strong>3. Autorizar la integración.</strong> <code>aracne-cicd</code> nunca hace <em>merge</em> ni <em>push</em> a ramas protegidas, ni despliega sin autorización humana explícita.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Figura 6.4 — Recorrido ideal de un módulo con Aracne, de la instalación a la puesta en marcha. Verde: arnés; blanco: personas; azul discontinuo: Azure DevOps; puntos rojos: puertas humanas</figcaption>
            </figure>
          </article>

          <!-- E4-9: Seguridad (Tabla 6.4) [c4-seguridad] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e4" data-item="c4-seguridad">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
                <h2 style="margin-bottom:4px;">Criterios de seguridad: ocho riesgos <abbr title="Open Worldwide Application Security Project">OWASP</abbr> contra los controles del arnés</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;"><span class="pill pill--risk">Pendiente</span> <code>/sw:build</code> y <code>/sw:bug</code> permiten la terminal sin restricción: hay que acotarla antes de usarlos en ATENEA. El arnés no tiene identidad propia: actúa con los permisos de la cuenta de la persona.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.66rem,min(1.12vw,2.05vh),1.5rem);">
                  <caption>Tabla 6.4 — Criterios de seguridad del sistema de agentes: riesgo, control en el arnés 0.9.0 y adaptación pendiente</caption>
                  <thead>
                    <tr>
                      <th style="width:19%;font-size:0.82em;">Riesgo</th>
                      <th style="width:44%;font-size:0.82em;">Control en el arnés 0.9.0</th>
                      <th style="font-size:0.82em;">Pendiente para ATENEA</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Riesgo"><strong>Abuso de herramientas y acciones no autorizadas</strong></td>
                      <td data-label="Control en el arnés 0.9.0"><span>Cada comando declara las herramientas que puede usar: <code>/sw:status</code> solo lee; <code>/sw:sprint</code> y <code>/sw:close</code> no escriben archivos</span></td>
                      <td data-label="Pendiente para ATENEA"><span><span class="pill pill--risk">Terminal sin restricción</span> <code>/sw:build</code> y <code>/sw:bug</code>: acotarla y ejecutarlos solo en equipos y cuentas institucionales</span></td>
                    </tr>
                    <tr>
                      <td data-label="Riesgo"><strong>Desviación del objetivo y código fuera de especificación</strong></td>
                      <td data-label="Control en el arnés 0.9.0"><span>Regla de frontera: se podan las skills de BMAD que escriben código sin contrato; el constructor trabaja un contrato a la vez y lo demás pasa por <code>/sw:change</code></span></td>
                      <td data-label="Pendiente para ATENEA"><span><span class="pill pill--ok">Ninguno</span></span></td>
                    </tr>
                    <tr>
                      <td data-label="Riesgo"><strong>Cadena de suministro</strong></td>
                      <td data-label="Control en el arnés 0.9.0"><span>Versiones fijadas en un solo archivo (BMAD 6.11.0, OpenSpec 1.10.0, graphify 0.8.37, Gentle-AI 4.1.1); el paquete no tiene dependencias npm; instalar desde Homebrew es una decisión explícita del usuario</span></td>
                      <td data-label="Pendiente para ATENEA"><span>Revisión de esas versiones por seguridad antes de instalar</span></td>
                    </tr>
                    <tr>
                      <td data-label="Riesgo"><strong>Fuga de datos a terceros</strong></td>
                      <td data-label="Control en el arnés 0.9.0"><span>La telemetría de OpenSpec se desactiva en cada ejecución</span></td>
                      <td data-label="Pendiente para ATENEA"><span>Condiciones de datos del proveedor del modelo (anexo D)</span></td>
                    </tr>
                    <tr>
                      <td data-label="Riesgo"><strong>Servidores MCP no confiables</strong></td>
                      <td data-label="Control en el arnés 0.9.0"><span>Un único servidor MCP, la memoria local Engram, con el perfil de herramientas del agente</span></td>
                      <td data-label="Pendiente para ATENEA"><span>Lista de servidores MCP permitidos por la Subgerencia de TIC</span></td>
                    </tr>
                    <tr>
                      <td data-label="Riesgo"><strong>Secretos y credenciales</strong></td>
                      <td data-label="Control en el arnés 0.9.0"><span>El arnés no maneja secretos; la plantilla de arquitectura base deja la sección para que el proyecto la defina</span></td>
                      <td data-label="Pendiente para ATENEA"><span>Definir la regla en la arquitectura base y aplicar el criterio 8 (Tabla 4.4)</span></td>
                    </tr>
                    <tr>
                      <td data-label="Riesgo"><strong>Integración sin revisión</strong></td>
                      <td data-label="Control en el arnés 0.9.0"><span>Revisión en cuatro perspectivas (riesgo, fiabilidad, resiliencia y legibilidad) y aprobación humana de la integración</span></td>
                      <td data-label="Pendiente para ATENEA"><span>Proteger las ramas en Azure DevOps</span></td>
                    </tr>
                    <tr>
                      <td data-label="Riesgo"><strong>Datos personales en el contexto del modelo</strong></td>
                      <td data-label="Control en el arnés 0.9.0"><span>Las pruebas se escriben por escenario sobre datos de ejemplo</span></td>
                      <td data-label="Pendiente para ATENEA"><span>Aplicar el inventario (Tabla 3.12) y los criterios 8 y 9</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E4-10: Trazabilidad (§6.9) [c4-trazabilidad] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e4" data-item="c4-trazabilidad" data-caption-source="§6.9" data-tone="emerald">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">5 &middot; Agentes y Skills (E4)</p>
                <h2 style="margin-bottom:4px;">Trazabilidad: dos archivos del repositorio enlazan el requisito con el código</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Responde a una necesidad del diagnóstico: hoy no hay vínculo entre el acta y las tareas, y ante la Contraloría se entrega la estimación desglosada.</p>
              </div>
              <svg viewBox="-4 -4 1208 500" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cadena de trazabilidad del requisito a la integración, con trace.json, changelog.jsonl y el estado de la verificación">
<defs>
<marker id="a69b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker>
</defs>
<rect x="0" y="8" width="170" height="62" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="85" y="47" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700" text-anchor="middle">Requisito</text>
<path d="M173 39 H202" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a69b)" />
<rect x="206" y="8" width="170" height="62" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="291" y="47" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700" text-anchor="middle">Historia</text>
<path d="M379 39 H408" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a69b)" />
<rect x="412" y="8" width="170" height="62" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.8" />
<text x="497" y="47" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700" text-anchor="middle">Contrato</text>
<path d="M585 39 H614" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a69b)" />
<rect x="618" y="8" width="170" height="62" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.8" />
<text x="703" y="47" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700" text-anchor="middle">Código</text>
<path d="M791 39 H820" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a69b)" />
<rect x="824" y="8" width="170" height="62" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.8" />
<text x="909" y="47" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700" text-anchor="middle">Prueba</text>
<path d="M997 39 H1026" stroke="#2C6B87" stroke-width="2.2" fill="none" marker-end="url(#a69b)" />
<rect x="1030" y="8" width="170" height="62" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.8" />
<text x="1115" y="47" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700" text-anchor="middle">Integración</text>
<path d="M2 82 V92 H576 V82" stroke="#1E5631" stroke-width="2" fill="none" />
<text x="289" y="114" fill="#1E5631" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="middle">Los dos archivos del arnés cubren los primeros eslabones</text>
<path d="M624 82 V92 H1198 V82" stroke="#2C6B87" stroke-width="2" fill="none" />
<text x="911" y="114" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="14.5" font-weight="700" text-anchor="middle">El historial de Git y la solicitud de integración, los últimos</text>
<rect x="0" y="132" width="578" height="132" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="14" y="158" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="17" font-weight="700">trace.json</text>
<text x="14" y="182" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Mapa de traza. Por contrato: épica e historia de origen, requisitos</text>
<text x="14" y="201" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">que cubre, origen de cada atribución, capacidad, revisión y número de</text>
<text x="14" y="220" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">escenarios.</text>
<text x="14" y="243" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Determinista: el mismo archivo de historias produce el mismo mapa.</text>
<rect x="0" y="276" width="578" height="146" rx="8" fill="#EBF5ED" stroke="#1E5631" stroke-width="1.6" />
<text x="14" y="302" fill="#1E5631" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="17" font-weight="700">changelog.jsonl</text>
<text x="14" y="326" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Bitácora de corridas. Cada corrida del puente añade una línea con</text>
<text x="14" y="345" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">fecha, archivo de origen, huella SHA-256 abreviada, opciones y</text>
<text x="14" y="364" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">contratos producidos.</text>
<text x="14" y="387" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Solo se añaden líneas; no se reescriben.</text>
<rect x="622" y="132" width="578" height="132" rx="8" fill="#EAF3F8" stroke="#2C6B87" stroke-width="1.6" />
<text x="636" y="158" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Git y solicitud de integración</text>
<text x="636" y="182" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">La PR de aracne-cicd lleva la traza y los commits atómicos.</text>
<text x="636" y="205" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Dos pruebas protegen la cadena: una evita la pérdida de entradas del</text>
<text x="636" y="224" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">mapa en una corrida parcial y otra verifica que cada corrida deja una</text>
<text x="636" y="243" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">línea en la bitácora.</text>
<rect x="622" y="276" width="578" height="146" rx="8" fill="#FFF7ED" stroke="#B07A12" stroke-width="1.6" />
<text x="636" y="302" fill="#B07A12" font-family="Space Grotesk,sans-serif" font-size="17" font-weight="700">Estado de la verificación</text>
<text x="636" y="326" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">241 casos de la suite pasaron con el paquete congelado 0.9.0;</text>
<text x="636" y="345" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">desde una ruta con espacios fallan 21 (corrección en la versión siguiente).</text>
<text x="636" y="372" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">Probado fuera de ATENEA; falta instalarlo y adaptarlo a las</text>
<text x="636" y="391" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14.5">condiciones de ATENEA.</text>
<rect x="0" y="434" width="1200" height="50" rx="8" fill="#FFFFFF" stroke="#B07A12" stroke-width="1.4" stroke-dasharray="6,4" />
<text x="14" y="455" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">La traza es versionada y verificable, pero no inmutable: vive en el repositorio y su protección depende de las ramas protegidas y de los</text>
<text x="14" y="474" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">permisos del gestor de repositorios.</text>
</svg>
              <div class="mobile-alt">
                <p class="sched-title">Cadena de trazabilidad</p>
                <p style="margin:6px 0;"><strong>Requisito &rarr; historia &rarr; contrato &rarr; c&oacute;digo &rarr; prueba &rarr; integraci&oacute;n.</strong></p>
                <ul class="slide-list" style="margin:8px 0;">
                  <li><strong><code>trace.json</code> (mapa de traza).</strong> Por contrato: &eacute;pica e historia de origen, requisitos que cubre, origen de cada atribuci&oacute;n, capacidad, revisi&oacute;n y n&uacute;mero de escenarios. Es determinista: el mismo archivo de historias produce el mismo mapa.</li>
                  <li><strong><code>changelog.jsonl</code> (bit&aacute;cora de corridas).</strong> Cada corrida del puente a&ntilde;ade una l&iacute;nea con fecha, archivo de origen, huella SHA-256 abreviada, opciones y contratos producidos. Solo se a&ntilde;aden l&iacute;neas.</li>
                  <li><strong>Git y solicitud de integraci&oacute;n.</strong> Cubren los &uacute;ltimos eslabones; la PR de <code>aracne-cicd</code> lleva la traza.</li>
                  <li><strong>Estado.</strong> <span class="pill pill--ok">241 casos pasan</span> con el paquete congelado 0.9.0 (desde una ruta con espacios fallan 21, corregido para la versión siguiente); <span class="pill pill--partial">Probado fuera de ATENEA</span> falta instalarlo y adaptarlo.</li>
                  <li><strong>L&iacute;mite.</strong> La traza es versionada y verificable, pero no inmutable: su protecci&oacute;n depende de las ramas protegidas y de los permisos del gestor de repositorios.</li>
                </ul>
              </div>
              <figcaption class="fig-caption">Fuente: §6.9 — Cadena de trazabilidad con trace.json y changelog.jsonl, y estado de la verificación (sin figura ni tabla numerada en el informe)</figcaption>
            </figure>
          </article>

          <!-- ========================================================================= -->
          <!-- E4 · Plataforma Aracne propuesta a ATENEA (mockups de concepto, §4.10)     -->
          <!-- ========================================================================= -->

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-plataforma" data-tone="blue" data-caption-source="§4.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Plataforma propuesta</p>
              <h2>Aracne como plataforma de la entidad: una propuesta de concepto</h2>
              <ul class="slide-list">
                <li><strong>Mockups para discutir:</strong> las pantallas que siguen muestran el concepto propuesto a <abbr title="Agencia Distrital para la Educación Superior, la Ciencia y la Tecnología">ATENEA</abbr>; no son software construido.</li>
                <li><strong>Hoy:</strong> el método se instala en el equipo de cada desarrollador, y el contexto y las decisiones del proyecto quedan en esa máquina.</li>
                <li><strong>Propuesta:</strong> un servidor de la entidad en contenedores sobre Azure, con interfaz web, roles desde <abbr title="Microsoft Entra ID, directorio de identidades de la entidad">Entra ID</abbr> y un punto de acceso <abbr title="Model Context Protocol">MCP</abbr> al que se conecta cada desarrollador.</li>
                <li><strong>Tres bandas:</strong> la máquina del desarrollador, el servidor de la entidad y Azure DevOps con Entra ID.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <img data-src="assets/images/aracne-mockup-01-mapa-como-se-conecta-todo.webp" width="1600" height="1059" decoding="async" loading="lazy" alt="Mockup del mapa de conexiones: la máquina del desarrollador con Claude Code u OpenCode, el servidor de la entidad con interfaz web, API, punto de acceso MCP, agentes propios y base de datos, y Azure DevOps con Azure Repos y Entra ID" />
              <figcaption class="fig-caption">Fuente: §4.10. Mockup de concepto: cómo se conectan la máquina del desarrollador, el servidor de la entidad y Azure DevOps</figcaption>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-plataforma" data-tone="blue" data-caption-source="§4.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Plataforma propuesta</p>
              <h2>Lo propio de ATENEA vive en el servidor; el desarrollador instala solo lo general</h2>
              <ul class="slide-list">
                <li><strong>Agentes propios:</strong> hechos a la medida de la entidad, corren en el servidor y se usan desde el chat de cada proyecto.</li>
                <li><strong>Paquete general:</strong> trae los comandos y agentes de traducir, construir y cerrar, sin conocimiento de la entidad.</li>
                <li><strong>Retiro:</strong> al salir del grupo de Entra ID, la persona pierde en el mismo momento el chat, la conexión <abbr title="Model Context Protocol">MCP</abbr> y el acceso al depósito de paquetes.</li>
                <li><strong>Sin editor de prompts:</strong> cada pieza tiene versión, pasa pruebas y se publica.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.68rem,min(1.2vw,2.2vh),1.5rem);">
                  <caption>Fuente: §4.10. Qué es propio de la entidad y qué es general en la plataforma propuesta</caption>
                  <thead>
                    <tr><th>Pieza</th><th>Dónde vive</th><th>Qué contiene</th></tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Pieza"><strong>Agentes propios de ATENEA</strong></td>
                      <td data-label="Dónde vive">Servidor de la entidad; se usan desde el chat del proyecto</td>
                      <td data-label="Qué contiene">Levantar requerimientos, brief, <abbr title="Product Requirements Document (documento de requisitos de producto)">PRD</abbr>, arquitectura y <abbr title="Experiencia de usuario">UX</abbr>, épicas e historias</td>
                    </tr>
                    <tr>
                      <td data-label="Pieza"><strong>Paquete general de construcción</strong></td>
                      <td data-label="Dónde vive">Equipo del desarrollador, desde el depósito de paquetes de ATENEA</td>
                      <td data-label="Qué contiene">Especificador y planificador, constructor y verificador, revisores de código y seguridad, operador de integración, cierre, estado y doctor</td>
                    </tr>
                    <tr>
                      <td data-label="Pieza"><strong>Artefactos del proyecto</strong></td>
                      <td data-label="Dónde vive">Carpeta <code>docs</code> del repositorio en Azure Repos</td>
                      <td data-label="Qué contiene">Brief, PRD, arquitectura, épicas, historias y tablero de estado, cada uno por commit</td>
                    </tr>
                    <tr>
                      <td data-label="Pieza"><strong>Contexto y memoria del proyecto</strong></td>
                      <td data-label="Dónde vive">Servidor de la entidad y repositorio</td>
                      <td data-label="Qué contiene">Lo que se queda en la entidad cuando una persona sale del proyecto</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-plataforma" data-tone="blue" data-caption-source="§4.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Plataforma propuesta</p>
              <h2>Inicio y Proyectos: el tablero general y un proyecto con nombre, repositorio y personas</h2>
              <ul class="slide-list">
                <li><strong>Inicio:</strong> cuatro cifras arriba, el estado del desarrollo por proyecto, las novedades y los agentes llamados en el día.</li>
                <li><strong>Etapa según los artefactos:</strong> la marcan los archivos que existen en el repositorio; el avance, las pruebas y las solicitudes de integración los reporta Claude Code por <abbr title="Model Context Protocol">MCP</abbr>.</li>
                <li><strong>Nuevo proyecto:</strong> pide el nombre, el enlace del repositorio en Azure Repos y las personas con su rol. Nada más.</li>
                <li><strong>Permiso acotado:</strong> el servidor lee y hace commit solo en la carpeta <code>docs</code> del repositorio.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div style="flex:1 1 auto;min-height:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));grid-template-rows:minmax(0,1fr);gap:8px;">
                <img data-src="assets/images/aracne-mockup-02-inicio-tablero-general.webp" width="1600" height="1695" decoding="async" loading="lazy" style="min-height:0;object-fit:cover;object-position:top center;" alt="Mockup de Inicio: cifras generales, estado del desarrollo por proyecto, novedades y agentes llamados hoy" />
                <img data-src="assets/images/aracne-mockup-03-proyectos-y-nuevo-proyecto.webp" width="1600" height="1059" decoding="async" loading="lazy" style="min-height:0;object-fit:cover;object-position:top center;" alt="Mockup de Proyectos: tabla de proyectos y panel de nuevo proyecto con nombre, repositorio y personas con rol" />
              </div>
              <figcaption class="fig-caption">Fuente: §4.10. Mockups de Inicio y de Proyectos (vistas parciales)</figcaption>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-plataforma" data-tone="blue" data-caption-source="§4.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Plataforma propuesta</p>
              <h2>Dentro de un proyecto: del chat con los agentes propios a épicas e historias</h2>
              <ul class="slide-list">
                <li><strong>Chat de requerimientos:</strong> la persona sube transcripciones y actas, y el agente pregunta lo que falta.</li>
                <li><strong>Artefactos por commit:</strong> brief, <abbr title="Product Requirements Document (documento de requisitos de producto)">PRD</abbr> y arquitectura quedan como archivos en <code>docs</code>; cada tarjeta muestra la versión y el commit.</li>
                <li><strong>Descomponer:</strong> el agente de historias divide el PRD en épicas e historias y las escribe en <code>docs/epicas</code> y <code>docs/historias</code>.</li>
                <li><strong>Revisión humana:</strong> la líder técnica marca las historias listas; el desarrollador las recibe con el clone y Claude Code las toma por <abbr title="Model Context Protocol">MCP</abbr>.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div style="flex:1 1 auto;min-height:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));grid-template-rows:minmax(0,1fr);gap:8px;">
                <img data-src="assets/images/aracne-mockup-04-proyecto-chat-y-artefactos.webp" width="1600" height="1271" decoding="async" loading="lazy" style="min-height:0;object-fit:cover;object-position:top center;" alt="Mockup de un proyecto: chat con los agentes propios, árbol de artefactos del repositorio y ficha del PRD" />
                <img data-src="assets/images/aracne-mockup-05-proyecto-descomponer-epicas-historias.webp" width="1600" height="1389" decoding="async" loading="lazy" style="min-height:0;object-fit:cover;object-position:top center;" alt="Mockup de la descomposición del PRD en épicas e historias escritas como archivos, con la ficha de una historia" />
              </div>
              <figcaption class="fig-caption">Fuente: §4.10. Mockups de un proyecto: chat y artefactos, y descomposición en épicas e historias (vistas parciales)</figcaption>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-plataforma" data-tone="blue" data-caption-source="§4.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Plataforma propuesta</p>
              <h2>Flujo agéntico y estado: qué agente entró en cada etapa y dónde va cada requisito</h2>
              <ul class="slide-list">
                <li><strong>Seis etapas:</strong> Entender, Decidir, Descomponer, Traducir, Construir y Cerrar, cada una con sus agentes, llamadas, entradas y salidas.</li>
                <li><strong>Dos lugares:</strong> las etapas 1 a 3 corren en el chat con los agentes propios; las 4 a 6, en Claude Code con el paquete general.</li>
                <li><strong>Decisiones de personas:</strong> la revisión de historias y la aprobación de solicitudes de integración se marcan aparte.</li>
                <li><strong>Estado:</strong> es el tablero que genera el comando de estado del arnés; enlaza requisito, épica, historia y contrato, y muestra la construcción en curso.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div style="flex:1 1 auto;min-height:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));grid-template-rows:minmax(0,1fr);gap:8px;">
                <img data-src="assets/images/aracne-mockup-06-proyecto-flujo-agentico.webp" width="1600" height="2071" decoding="async" loading="lazy" style="min-height:0;object-fit:cover;object-position:top center;" alt="Mockup del flujo agéntico: seis etapas con sus agentes, número de llamadas, entradas y salidas" />
                <img data-src="assets/images/aracne-mockup-07-proyecto-estado-y-flujo-de-requerimientos.webp" width="1600" height="1812" decoding="async" loading="lazy" style="min-height:0;object-fit:cover;object-position:top center;" alt="Mockup del estado de un proyecto: descomposición del PRD al código y flujo de requerimientos de requisito a contrato" />
              </div>
              <figcaption class="fig-caption">Fuente: §4.10. Mockups del flujo agéntico y del estado de un proyecto (vistas parciales)</figcaption>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-plataforma" data-tone="blue" data-caption-source="§4.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Plataforma propuesta</p>
              <h2>Administración: los roles son grupos del Directorio Activo u otro directorio de la entidad y los permisos son fijos por rol</h2>
              <ul class="slide-list">
                <li><strong>Cinco roles:</strong> administrador, requerimientos, líder técnica, desarrollador y consultor de la Universidad.</li>
                <li><strong>Matriz fija:</strong> dice qué puede hacer cada rol y no se edita por persona; solo la líder técnica aprueba integraciones a ramas protegidas.</li>
                <li><strong>Auditoría de seguridad:</strong> accesos rechazados, sesiones <abbr title="Model Context Protocol">MCP</abbr> activas, commits fuera de <code>docs</code> y cada llamada con su cuenta y resultado.</li>
                <li><strong>Arneses e integraciones:</strong> versión de los agentes propios y del paquete general; conexión con el Directorio Activo u otro directorio de la entidad, Azure Repos, los modelos con clave corporativa y el punto de acceso MCP.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <img data-src="assets/images/aracne-mockup-08-administracion.webp" width="1600" height="2565" decoding="async" loading="lazy" style="min-height:0;object-fit:cover;object-position:top center;" alt="Mockup de Administración: matriz de permisos por rol, lista de personas, auditoría de seguridad, arneses e integraciones" />
              <figcaption class="fig-caption">Fuente: §4.10. Mockup de Administración: personas y roles, auditoría, arneses e integraciones (vista parcial)</figcaption>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-plataforma" data-tone="purple" data-caption-source="§4.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Plataforma propuesta</p>
              <h2>Un proyecto de principio a fin: seis etapas y lo que cada una deja en el repositorio</h2>
              <ul class="slide-list">
                <li><strong>En la web:</strong> entender, decidir y descomponer ocurren en el chat, con el rol de requerimientos y la revisión de la líder técnica.</li>
                <li><strong>En Claude Code:</strong> traducir, construir y cerrar los hace el desarrollador; la líder técnica aprueba las integraciones.</li>
                <li><strong>Un solo lugar de verdad:</strong> cada etapa deja archivos en el repositorio y la siguiente los lee.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.68rem,min(1.2vw,2.2vh),1.5rem);">
                  <caption>Fuente: §4.10. Flujo de un proyecto en la plataforma propuesta</caption>
                  <thead>
                    <tr><th>Etapa</th><th>Quién</th><th>Dónde</th><th>Qué queda en el repositorio</th></tr>
                  </thead>
                  <tbody>
                    <tr><td data-label="Etapa"><strong>1 &middot; Entender</strong></td><td data-label="Quién">Requerimientos</td><td data-label="Dónde">Chat en la web</td><td data-label="Repositorio"><code>docs/brief.md</code></td></tr>
                    <tr><td data-label="Etapa"><strong>2 &middot; Decidir</strong></td><td data-label="Quién">Requerimientos y líder técnica</td><td data-label="Dónde">Chat en la web</td><td data-label="Repositorio"><code>docs/prd.md</code>, <code>docs/arquitectura.md</code>, <code>docs/ux.md</code></td></tr>
                    <tr><td data-label="Etapa"><strong>3 &middot; Descomponer</strong></td><td data-label="Quién">Requerimientos; revisa la líder técnica</td><td data-label="Dónde">Chat en la web</td><td data-label="Repositorio"><code>docs/epicas/</code>, <code>docs/historias/</code></td></tr>
                    <tr><td data-label="Etapa"><strong>4 &middot; Traducir</strong></td><td data-label="Quién">Desarrollador</td><td data-label="Dónde">Claude Code</td><td data-label="Repositorio"><code>openspec/</code> y orden de trabajo</td></tr>
                    <tr><td data-label="Etapa"><strong>5 &middot; Construir</strong></td><td data-label="Quién">Desarrollador; aprueba la líder técnica</td><td data-label="Dónde">Claude Code</td><td data-label="Repositorio">Ramas por historia, solicitudes de integración y evidencia por MCP</td></tr>
                    <tr><td data-label="Etapa"><strong>6 &middot; Cerrar</strong></td><td data-label="Quién">Desarrollador</td><td data-label="Dónde">Claude Code</td><td data-label="Repositorio">Contratos archivados y <code>docs/status/dashboard.html</code></td></tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-plataforma" data-tone="rose" data-caption-source="§4.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Plataforma propuesta</p>
              <h2>¿Qué validar con ATENEA antes de construir la plataforma?</h2>
              <ul class="slide-list">
                <li><strong>Es una propuesta:</strong> el alcance de los agentes, los permisos y el orden de construcción se acuerdan con la entidad.</li>
                <li><strong>Orden sugerido:</strong> primero el servidor con roles, proyectos y chat; luego el <abbr title="Model Context Protocol">MCP</abbr> con el paquete general; al final el tablero de estado y el flujo agéntico.</li>
                <li><strong>Piloto:</strong> un proyecto real recorre las seis etapas para medir llamadas, tiempos y decisiones de personas.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.68rem,min(1.2vw,2.2vh),1.5rem);">
                  <caption>Fuente: §4.10. Puntos de la plataforma propuesta que se validan con ATENEA</caption>
                  <thead>
                    <tr><th>Punto</th><th>Qué se valida</th></tr>
                  </thead>
                  <tbody>
                    <tr><td data-label="Punto"><strong>1 &middot; Alcance de los agentes propios</strong></td><td data-label="Qué se valida">Cuáles se hacen a la medida de ATENEA y con qué fuentes: transcripciones, actas, normativa y formatos propios</td></tr>
                    <tr><td data-label="Punto"><strong>2 &middot; Permisos sobre el repositorio</strong></td><td data-label="Qué se valida">Que una identidad de servicio escriba solo en la carpeta <code>docs</code>, y cómo se protegen las ramas</td></tr>
                    <tr><td data-label="Punto"><strong>3 &middot; Modelos y claves</strong></td><td data-label="Qué se valida">Clave corporativa en Key Vault, proveedor del modelo y consumo esperado por proyecto; ninguna clave en equipos de desarrolladores</td></tr>
                    <tr><td data-label="Punto"><strong>4 &middot; Roles y grupos de Entra ID</strong></td><td data-label="Qué se valida">Los cinco grupos, quién administra la pertenencia y la configuración gestionada de Claude Code por Intune</td></tr>
                    <tr><td data-label="Punto"><strong>5 &middot; Primer proyecto piloto</strong></td><td data-label="Qué se valida">Un proyecto real para recorrer las seis etapas de punta a punta</td></tr>
                    <tr><td data-label="Punto"><strong>6 &middot; Orden de construcción</strong></td><td data-label="Qué se valida">Servidor con roles, proyectos y chat; después MCP y paquete general; al final tablero de estado y flujo agéntico</td></tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-extensiones" data-tone="green" data-caption-source="§6.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Agentes de investigación</p>
              <h2>Dos agentes nuevos con su servidor MCP: panorama CTeI y productos de ATENEA</h2>
              <ul class="slide-list">
                <li><strong>Solicitud del 30 de octubre:</strong> ATENEA pidió investigar plataformas de ciencia, tecnología e innovación de otros países para encontrar actores, servicios o interacciones que Hēma no contempla.</li>
                <li><strong>Propuesta de la Universidad:</strong> un segundo agente organiza la arquitectura, el diseño y el código de los productos que ATENEA ya tiene, para reutilizar y decidir mejor.</li>
                <li><strong>Estado:</strong> los dos están construidos y son de instalación opcional; no hacen parte de la versión 0.9.0 y entran en la versión siguiente.</li>
              </ul>
            </div>
            <figure class="slide-figure" style="display:flex;flex-direction:column;gap:6px;">
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.68rem,min(1.2vw,2.2vh),1.5rem);">
                  <caption>Tabla 6.7. Agentes y servidores MCP de investigación, construidos y de instalación opcional, fuera del paquete 0.9.0</caption>
                  <thead>
                    <tr><th>Agente y MCP</th><th>Dónde entra</th><th>Qué entrega</th><th>Origen y estado</th></tr>
                  </thead>
                  <tbody>
                    <tr><td data-label="Agente y MCP"><code>aracne-ctei-scout</code> con <code>ctei-landscape</code></td><td data-label="Dónde entra">Antes del <em>brief</em> de producto</td><td data-label="Qué entrega">Estudio de base tecnológica (plataformas, software, patentes y artículos; Bogotá, Colombia, Latinoamérica y el mundo), <code>research-brief.md</code> y requisitos, épicas e historias candidatas</td><td data-label="Origen y estado">Solicitud de ATENEA (R7); construido, opcional</td></tr>
                    <tr><td data-label="Agente y MCP"><code>aracne-portfolio</code> con <code>atenea-portfolio</code></td><td data-label="Dónde entra"><em>Brief</em>, arquitectura, <code>/sw:adopt</code>, <code>/sw:change</code> y <code>/sw:build</code>, solo como consulta</td><td data-label="Qué entrega">Grafo de productos y componentes, candidatos de reutilización y documentación de código curada al estilo de context7; privado por la confidencialidad del contrato</td><td data-label="Origen y estado">Propuesta de la Universidad; construido, opcional</td></tr>
                  </tbody>
                </table>
              </div>
              <ul class="slide-list" style="flex:0 0 auto;margin:6px 4px 0;font-size:clamp(0.8rem,1vw,1rem);">
                <li>Los dos agentes se instalan con <code>aracne-sdlc-ai init --only research</code>.</li>
                <li>El servidor <code>ctei-landscape</code> es público y se instala con <code style="overflow-wrap:anywhere;">uvx --from git+https://github.com/LIAUNAL/panoramaPlataformasCTeI ctei-landscape-mcp</code>.</li>
                <li>Sus datos se exploran en <a href="https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion" target="_blank" rel="noopener" style="overflow-wrap:anywhere;">https://liaunal.github.io/panoramaPlataformasCTeI/#constelacion</a>.</li>
              </ul>
            </figure>
          </article>

          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e4" data-item="c4-extensiones" data-tone="green" data-caption-source="§6.10">
            <div class="slide-content">
              <p class="slide-kicker">5 &middot; Agentes y Skills (E4) &middot; Agentes de investigación</p>
              <h2>Se construyeron como el banco de proyectos del laboratorio</h2>
              <ul class="slide-list">
                <li><strong>Referencia:</strong> el banco <code>bancoProyectosPapersLIA</code> ya alimenta la redacción de artículos y propuestas con fichas, clústeres y un servidor MCP.</li>
                <li><strong>Trazabilidad:</strong> cada afirmación que llega al PRD o a una historia cita el identificador de su ficha.</li>
                <li><strong>Visualización:</strong> un tablero estático muestra el trabajo de los agentes, con pruebas de calidad visual y de memoria.</li>
              </ul>
            </div>
            <figure class="slide-figure">
              <div class="data-table-wrapper">
                <table class="data-table" style="font-size:clamp(0.68rem,min(1.2vw,2.2vh),1.5rem);">
                  <caption>Fuente: §6.10. Piezas del banco del laboratorio que se reutilizaron</caption>
                  <thead>
                    <tr><th>Pieza</th><th>Cómo se usa en los dos agentes</th></tr>
                  </thead>
                  <tbody>
                    <tr><td data-label="Pieza"><strong>Fichas Markdown</strong></td><td data-label="Uso">Una por producto o por referente CTeI, con campos fijos</td></tr>
                    <tr><td data-label="Pieza"><strong>Una sola fuente JSON</strong></td><td data-label="Uso">Taxonomía, clústeres estables y relaciones con los cinco ítems más parecidos</td></tr>
                    <tr><td data-label="Pieza"><strong>Servidor MCP</strong></td><td data-label="Uso">Búsqueda sobre SQLite FTS5 que se reindexa al cambiar la fuente; <code>export_to_insumos</code> copia fichas a los insumos de <code>/sw:adopt</code></td></tr>
                    <tr><td data-label="Pieza"><strong>Tablero</strong></td><td data-label="Uso">Constelación 3D, clústeres, buscador, línea de tiempo y un mapa por alcance territorial</td></tr>
                    <tr><td data-label="Pieza"><strong>Pruebas</strong></td><td data-label="Uso">Playwright para la calidad visual y el consumo de memoria</td></tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- ========================================================================= -->
          <!-- MÓDULO 6: Decisiones, Compromisos y Cierre (Capítulo 7)                   -->
          <!-- ========================================================================= -->

          <!-- E5-1: Tres decisiones de ATENEA (§7.1) [c-cierre-decisiones] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e5" data-item="cierre-decisiones" data-caption-source="§7.1">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1)</p>
                <h2 style="margin-bottom:4px;">Estado de las tres decisiones y cierre de Hito 1</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Resolución integral de las observaciones de supervisión para habilitar la radicación de la Factura 1 (ventana 1–15 de noviembre).</p>
              </div>
              <svg viewBox="-4 0 1208 350" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Estado de las tres decisiones de ATENEA: caso de uso seleccionado con 14 historias reconstruidas por validar, entorno en Azure en curso y siete observaciones resueltas">
<rect x="0" y="10" width="372" height="330" rx="12" fill="#FFFFFF" stroke="#1E5631" stroke-width="2" />
<rect x="0" y="10" width="372" height="62" rx="12" fill="#1E5631" />
<rect x="0" y="50" width="372" height="22" fill="#1E5631" />
<text x="20" y="50" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700">1 · Caso seleccionado</text>
<text x="20" y="112" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Campus 2600 en Hēma</text>
<text x="20" y="148" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">✓ 7 épicas y 14 historias</text>
<text x="38" y="173" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">reconstruidas por la Universidad</text>
<text x="20" y="198" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">✓ 14 contratos y prueba de humo</text>
<text x="20" y="223" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">→ Validación con ATENEA</text>
<rect x="414" y="10" width="372" height="330" rx="12" fill="#FFFFFF" stroke="#4E93B0" stroke-width="2" />
<rect x="414" y="10" width="372" height="62" rx="12" fill="#4E93B0" />
<rect x="414" y="50" width="372" height="22" fill="#4E93B0" />
<text x="434" y="50" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700">2 · Entorno y accesos</text>
<text x="434" y="112" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">Entorno agéntico en Azure</text>
<text x="434" y="148" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">✓ VPN y Hēma QA recibidos</text>
<text x="434" y="173" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">✓ Flujo centralizado (Directorio Activo</text>
<text x="452" y="198" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">u otro directorio de la entidad)</text>
<text x="434" y="223" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">✓ Requisitos mínimos propuestos</text>
<text x="434" y="248" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">→ GoToCloud: martes 3-nov, 4 p. m.</text>
<rect x="828" y="10" width="372" height="330" rx="12" fill="#FFFFFF" stroke="#1E5631" stroke-width="2" />
<rect x="828" y="10" width="372" height="62" rx="12" fill="#1E5631" />
<rect x="828" y="50" width="372" height="22" fill="#1E5631" />
<text x="848" y="50" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="24" font-weight="700">3 · Diagnóstico y carta</text>
<text x="848" y="112" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="19" font-weight="700">7 observaciones resueltas</text>
<text x="848" y="148" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">✓ Carta formal de respuestas</text>
<text x="848" y="173" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">✓ Aracne 0.9.0 (241 pruebas)</text>
<text x="848" y="198" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">✓ Zip congelado con SHA-256</text>
<text x="848" y="223" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="16">→ Visto bueno y Factura 1</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Estado de las decisiones</p>
                <ol class="slide-list" style="margin:8px 0;">
                  <li><strong>Campus 2600 en Hēma (C3):</strong> seleccionado; 7 épicas y 14 historias reconstruidas por la Universidad a partir de la grabación y el prototipo, pendientes de validación con ATENEA; 14 contratos OpenSpec y prueba de humo del arnés.</li>
                  <li><strong>Entorno en Azure:</strong> VPN y Hēma recibidos; requisitos técnicos mínimos propuestos para la reunión con GoToCloud del martes 3 de noviembre a las 4 p. m.</li>
                  <li><strong>Diagnóstico y carta:</strong> 7 observaciones resueltas con la versión 0.9.0 (241 pruebas) para radicar la Factura 1 ($150M).</li>
                </ol>
              </div>
              <figcaption class="fig-caption">Fuente: §7.1 y Carta de Respuestas a Observaciones de ATENEA (1 de noviembre de 2026)</figcaption>
            </figure>
          </article>

          <!-- E5-2: Información pendiente (1/2) [cierre-pendientes] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e5" data-item="cierre-pendientes">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1)</p>
                <h2 style="margin-bottom:4px;">Información pendiente para cerrar C1 a C4 y C7 (1/2)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Lo que falta depende de información que solo tiene ATENEA; el informe marca cada dato como pendiente en lugar de suponerlo. Componentes C1 y C3.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.7rem,min(1.2vw,2.25vh),1.55rem);">
                  <caption>Tabla 7.1. Información que debe aportar ATENEA para cerrar los componentes C1 a C4 y C7 (1/2)</caption>
                  <thead>
                    <tr>
                      <th style="width:9%;font-size:0.82em;">Comp.</th>
                      <th style="width:48%;font-size:0.82em;">Información</th>
                      <th style="width:28%;font-size:0.82em;">¿Dónde se usa?</th>
                      <th style="font-size:0.82em;">Origen</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Comp."><strong>C1</strong></td>
                      <td data-label="Información"><span>Validación de la línea base de madurez y datos de despliegues, fallos y tiempos de recuperación</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tablas 3.7 y 3.8</span></td>
                      <td data-label="Origen"><span>R3, A4</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C1</strong></td>
                      <td data-label="Información"><span>Validación de la probabilidad, el impacto y los responsables de los riesgos técnicos</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tabla 3.11</span></td>
                      <td data-label="Origen"><span>A6</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C1</strong></td>
                      <td data-label="Información"><span>Responsable y volumen de cada fuente de datos, y si QA usa datos reales</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tabla 3.12</span></td>
                      <td data-label="Origen"><span>A1</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C1, C3</strong></td>
                      <td data-label="Información"><span>Selección del caso de uso y acta y diseño del módulo elegido</span></td>
                      <td data-label="¿Dónde se usa?"><span>Secciones 5.4 a 5.12 y anexo E</span></td>
                      <td data-label="Origen"><span>R2, R3</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C3</strong></td>
                      <td data-label="Información"><span>Proceso actual de la liquidación de apoyos económicos, con usuarios y volumen</span></td>
                      <td data-label="¿Dónde se usa?"><span>Sección 5.5 (Tabla 5.2)</span></td>
                      <td data-label="Origen"><span>A6</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C3</strong></td>
                      <td data-label="Información"><span>Protocolo, autenticación y responsable de cada integración</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tabla 5.7</span></td>
                      <td data-label="Origen"><span>A6</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E5-3: Información pendiente (2/2) [cierre-pendientes] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e5" data-item="cierre-pendientes">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1)</p>
                <h2 style="margin-bottom:4px;">Información pendiente para cerrar C1 a C4 y C7 (2/2)</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Lo que falta depende de información que solo tiene ATENEA; el informe marca cada dato como pendiente en lugar de suponerlo. Componentes C3, C2 y C4.</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.7rem,min(1.2vw,2.25vh),1.55rem);">
                  <caption>Tabla 7.1. Información que debe aportar ATENEA para cerrar los componentes C1 a C4 y C7 (2/2)</caption>
                  <thead>
                    <tr>
                      <th style="width:9%;font-size:0.82em;">Comp.</th>
                      <th style="width:48%;font-size:0.82em;">Información</th>
                      <th style="width:28%;font-size:0.82em;">¿Dónde se usa?</th>
                      <th style="font-size:0.82em;">Origen</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="Comp."><strong>C3</strong></td>
                      <td data-label="Información"><span>Entidades y columnas del módulo para el juego de datos sintéticos</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tabla 5.8</span></td>
                      <td data-label="Origen"><span>A6</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C2</strong></td>
                      <td data-label="Información"><span>Designación del equipo y dedicación de cada rol</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tabla 4.2</span></td>
                      <td data-label="Origen"><span>A5</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C2</strong></td>
                      <td data-label="Información"><span>Validación de los umbrales de calidad y seguridad y adopción de la política de uso de IA</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tabla 4.4 y anexo D</span></td>
                      <td data-label="Origen"><span>R4</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C2, C4</strong></td>
                      <td data-label="Información"><span>Informe de la revisión de seguridad de las aplicaciones</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tablas 3.9 y 6.4</span></td>
                      <td data-label="Origen"><span>R2</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C4</strong></td>
                      <td data-label="Información"><span>Lista de servidores MCP y herramientas permitidas, y protección de ramas en Azure DevOps</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tabla 6.4</span></td>
                      <td data-label="Origen"><span>R4</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C4</strong></td>
                      <td data-label="Información"><span>Aprobación de los servidores MCP de investigación (<code>ctei-landscape</code> y <code>atenea-portfolio</code>), una vez la Universidad fije su versión con una etiqueta</span></td>
                      <td data-label="¿Dónde se usa?"><span>Tabla 6.6</span></td>
                      <td data-label="Origen"><span>A10</span></td>
                    </tr>
                    <tr>
                      <td data-label="Comp."><strong>C4</strong></td>
                      <td data-label="Información"><span>Validación de la ficha de referencia de Hēma (CT000) que usa el agente de investigación CTeI</span></td>
                      <td data-label="¿Dónde se usa?"><span>Sección 6.10</span></td>
                      <td data-label="Origen"><span>R7</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E5-4: Compromisos registrados (Tabla 7.2) [cierre-compromisos] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e5" data-item="cierre-compromisos">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1)</p>
                <h2 style="margin-bottom:4px;">Compromisos registrados: cinco, todos con ATENEA o su Subgerencia de TIC</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">Compromisos de las sesiones que afectan a E1 a E4, con su responsable y su estado al corte. <span class="pill pill--todo">Abierto</span> dos, <span class="pill pill--partial">Parcial en R4</span> uno, <span class="pill pill--ok">Recibido</span> dos (23 de octubre).</p>
              </div>
              <div class="data-table-wrapper" style="flex:1 1 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.78rem,min(1.3vw,2.5vh),1.65rem);">
                  <caption>Tabla 7.2 — Compromisos de las sesiones que afectan a E1 a E4: responsable, origen y estado al corte</caption>
                  <thead>
                    <tr>
                      <th style="width:6%;font-size:0.82em;">N.º</th>
                      <th style="width:46%;font-size:0.82em;">Compromiso</th>
                      <th style="width:18%;font-size:0.82em;">Responsable</th>
                      <th style="width:12%;font-size:0.82em;">Origen</th>
                      <th style="font-size:0.82em;">Estado al corte</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="N.º"><strong>1</strong></td>
                      <td data-label="Compromiso"><span>Compartir un requerimiento de ejemplo con su diseño</span></td>
                      <td data-label="Responsable"><span>ATENEA</span></td>
                      <td data-label="Origen"><span>A4, R2</span></td>
                      <td data-label="Estado al corte"><span><span class="pill pill--ok" style="font-size:0.72em;">Recibido</span> 23-oct: dos historias de usuario (A7, A8); Figma solo como enlace</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>2</strong></td>
                      <td data-label="Compromiso"><span>Enviar el informe de la revisión de seguridad</span></td>
                      <td data-label="Responsable"><span>ATENEA</span></td>
                      <td data-label="Origen"><span>R2</span></td>
                      <td data-label="Estado al corte"><span><span class="pill pill--todo" style="font-size:0.72em;">Abierto</span></span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>3</strong></td>
                      <td data-label="Compromiso"><span>Definir el estado de la migración</span></td>
                      <td data-label="Responsable"><span>Subgerencia de TIC</span></td>
                      <td data-label="Origen"><span>A4</span></td>
                      <td data-label="Estado al corte"><span><span class="pill pill--partial" style="font-size:0.72em;">Parcial en R4</span></span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>4</strong></td>
                      <td data-label="Compromiso"><span>Definir el caso de uso institucional (C3)</span></td>
                      <td data-label="Responsable"><span>ATENEA</span></td>
                      <td data-label="Origen"><span>R3</span></td>
                      <td data-label="Estado al corte"><span><span class="pill pill--todo" style="font-size:0.72em;">Abierto</span> se definirá la semana del 26-oct, con la transcripción de la reunión del 23</span></td>
                    </tr>
                    <tr>
                      <td data-label="N.º"><strong>5</strong></td>
                      <td data-label="Compromiso"><span>Enviar un documento con la información actual de los proyectos y la estructura de carpetas de back-end y front-end, para entender la arquitectura de los desarrollos</span></td>
                      <td data-label="Responsable"><span>ATENEA</span></td>
                      <td data-label="Origen"><span>R3</span></td>
                      <td data-label="Estado al corte"><span><span class="pill pill--ok" style="font-size:0.72em;">Recibido</span> 23-oct (A9)</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </figure>
          </article>

          <!-- E5-5: Hoja de ruta Hito 1 a Hito 2 (Figura 2.1 y §4.8) [cierre-ruta] -->
          <article class="slide is-figure-full" data-deck="e1-e4" data-module="e5" data-item="cierre-ruta" data-caption-source="Figura 2.1 y §4.8">
            <figure class="slide-figure">
              <div class="fig-head" style="flex:0 0 auto;padding:4px 10px 2px;">
                <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1)</p>
                <h2 style="margin-bottom:4px;">Hoja de ruta: del cierre del Hito 1 al Hito 2</h2>
                <p style="font-size:clamp(0.86rem,1.05vw,1rem);line-height:1.4;">El Hito 1 cierra C1 a C4 en la semana 13; el Hito 2 cubre C5 a C8 y vence en la semana 22. Cuatro pasos de adopción preparan el paso a otros módulos.</p>
              </div>
              <svg viewBox="-4 -4 1208 516" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hoja de ruta: el Hito 1 va de la semana 1 a la 13 y cierra C1 a C4; el Hito 2 va de la semana 14 a la 22 y cubre C5 a C8; debajo, los cuatro pasos de la ruta de adopción">
<defs><marker id="rm-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#2C6B87" /></marker></defs>
<text x="271.4" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S1</text>
<text x="314.1" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S2</text>
<text x="356.8" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S3</text>
<text x="399.5" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S4</text>
<text x="442.3" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S5</text>
<text x="485.0" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S6</text>
<text x="527.7" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S7</text>
<text x="570.5" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S8</text>
<text x="613.2" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S9</text>
<text x="655.9" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S10</text>
<text x="698.6" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S11</text>
<text x="741.4" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S12</text>
<text x="784.1" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S13</text>
<text x="826.8" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S14</text>
<text x="869.5" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S15</text>
<text x="912.3" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S16</text>
<text x="955.0" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S17</text>
<text x="997.7" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S18</text>
<text x="1040.5" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S19</text>
<text x="1083.2" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S20</text>
<text x="1125.9" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S21</text>
<text x="1168.6" y="16" text-anchor="middle" fill="#5B6472" font-family="Space Grotesk,sans-serif" font-size="12">S22</text>
<rect x="251.0" y="26" width="553.5" height="26" rx="4" fill="#1E5631" />
<text x="260.0" y="45" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Hito 1 · C1 a C4 · semana 13</text>
<rect x="806.5" y="26" width="382.5" height="26" rx="4" fill="#5B6472" />
<text x="815.5" y="45" fill="#FFFFFF" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Hito 2 · C5 a C8 · E5 a E8 · semana 22</text>
<text x="8" y="76" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E1 · Diagnóstico</text>
<rect x="251.0" y="60" width="83.5" height="22" rx="4" fill="#9DB7C9" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="258.0" y="76" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A2</text>
<text x="8" y="105" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E2 · Metodología SDLC-IA</text>
<rect x="293.7" y="89" width="40.7" height="22" rx="4" fill="#7FB4CA" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="300.7" y="105" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A3</text>
<text x="8" y="134" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E3 · Caso de uso y arquitectura</text>
<rect x="293.7" y="118" width="83.5" height="22" rx="4" fill="#7FB4CA" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="300.7" y="134" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A4</text>
<text x="8" y="163" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E4 · Agentes y arneses</text>
<rect x="336.5" y="147" width="83.5" height="22" rx="4" fill="#B7CC85" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="343.5" y="163" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A6 · A7</text>
<text x="8" y="192" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E4 · Integración en flujos</text>
<rect x="421.9" y="176" width="126.2" height="22" rx="4" fill="#B7CC85" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="428.9" y="192" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A9</text>
<text x="8" y="221" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E4 · Puesta en marcha</text>
<rect x="507.4" y="205" width="126.2" height="22" rx="4" fill="#9DBB66" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="514.4" y="221" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A10</text>
<text x="8" y="250" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E5 · Ingeniería de pruebas</text>
<rect x="421.9" y="234" width="83.5" height="22" rx="4" fill="#7AA89F" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="428.9" y="250" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A8</text>
<text x="8" y="279" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E5 · Despliegue piloto</text>
<rect x="635.5" y="263" width="126.2" height="22" rx="4" fill="#7AA89F" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="642.5" y="279" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A12</text>
<text x="8" y="308" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E5 · Validación y ajustes</text>
<rect x="678.3" y="292" width="126.2" height="22" rx="4" fill="#5E9488" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="685.3" y="308" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A13</text>
<text x="8" y="337" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="14">E7 · Workshop 1</text>
<rect x="550.1" y="321" width="40.7" height="22" rx="4" fill="#DFBD76" stroke="#2C6B87" stroke-opacity="0.6" />
<text x="557.1" y="337" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">A11</text>
<text x="8" y="366" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="14" font-weight="700">Hito 2 · A14 a A20</text>
<rect x="806.5" y="350" width="382.5" height="22" rx="4" fill="#BAC7D5" stroke="#5B6472" stroke-opacity="0.6" />
<text x="813.5" y="366" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">Ampliación, documentación, talleres y cierre</text>
<line x1="805.5" y1="26" x2="805.5" y2="382" stroke="#1E5631" stroke-width="2.5" stroke-dasharray="5,4" />
<line x1="1190.0" y1="26" x2="1190.0" y2="382" stroke="#8A5A00" stroke-width="2.5" stroke-dasharray="5,4" />
<text x="799.5" y="398" text-anchor="end" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">H1c · hito 1 contractual</text>
<text x="1184.0" y="398" text-anchor="end" fill="#8A5A00" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="700">H2 · hito 2 contractual</text>
<text x="8" y="422" fill="#2C6B87" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Ruta de adopción (§4.8)</text>
<rect x="0" y="434" width="282" height="68" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.5" />
<circle cx="26" cy="468" r="16" fill="#7FB4CA" />
<text x="26" y="474" text-anchor="middle" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">1</text>
<text x="52" y="460" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Demostración</text>
<text x="52" y="479" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="13">con un requerimiento</text>
<text x="52" y="494" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="13">real de ATENEA</text>
<path d="M284 468 L304 468" stroke="#2C6B87" stroke-width="1.8" marker-end="url(#rm-b)" />
<rect x="306" y="434" width="282" height="68" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.5" />
<circle cx="332" cy="468" r="16" fill="#7FB4CA" />
<text x="332" y="474" text-anchor="middle" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">2</text>
<text x="358" y="460" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Contexto del área</text>
<text x="358" y="479" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="13">con los documentos de</text>
<text x="358" y="494" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="13">arquitectura</text>
<path d="M590 468 L610 468" stroke="#2C6B87" stroke-width="1.8" marker-end="url(#rm-b)" />
<rect x="612" y="434" width="282" height="68" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.5" />
<circle cx="638" cy="468" r="16" fill="#7FB4CA" />
<text x="638" y="474" text-anchor="middle" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">3</text>
<text x="664" y="460" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Límites del agente</text>
<text x="664" y="479" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="13">qué se envía a un modelo</text>
<text x="664" y="494" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="13">y con qué permisos</text>
<path d="M896 468 L916 468" stroke="#2C6B87" stroke-width="1.8" marker-end="url(#rm-b)" />
<rect x="918" y="434" width="282" height="68" rx="8" fill="#F8FAFC" stroke="#7FB4CA" stroke-width="1.5" />
<circle cx="944" cy="468" r="16" fill="#7FB4CA" />
<text x="944" y="474" text-anchor="middle" fill="#06080F" font-family="Space Grotesk,sans-serif" font-size="16" font-weight="700">4</text>
<text x="970" y="460" fill="#1B2029" font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700">Porción acotada</text>
<text x="970" y="479" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="13">del caso de uso y luego</text>
<text x="970" y="494" fill="#454F61" font-family="Space Grotesk,sans-serif" font-size="13">otros módulos</text>
              </svg>
              <div class="mobile-alt">
                <p class="sched-title">Hoja de ruta S1 a S22</p>
                <p class="sched-h">Hito 1 · C1 a C4 · E1 a E4 · semana 13</p>
                <ul class="slide-list" style="margin:6px 0;">
                  <li><strong>E1</strong> Diagnóstico (A2) · S1-S2</li>
                  <li><strong>E2</strong> Metodología SDLC-IA (A3) · S2</li>
                  <li><strong>E3</strong> Caso de uso y arquitectura (A4) · S2-S3</li>
                  <li><strong>E4</strong> Agentes, skills e integración (A6, A7, A9, A10) · S3-S9</li>
                  <li>También corren en el Hito 1 las actividades de <strong>E5</strong> (A8, A12, A13) y <strong>E7</strong> (A11)</li>
                </ul>
                <p class="sched-h">Hito 2 · C5 a C8 · E5 a E8 · semana 22</p>
                <ul class="slide-list" style="margin:6px 0;">
                  <li><strong>A14 a A20</strong> Ampliación, documentación, talleres y cierre · S14-S22</li>
                </ul>
                <p class="sched-h">Ruta de adopción (§4.8)</p>
                <ol class="slide-list" style="margin:6px 0;">
                  <li>Demostración con un requerimiento real de ATENEA.</li>
                  <li>Contexto del área con los documentos de arquitectura.</li>
                  <li>Límites del agente: qué se envía a un modelo y con qué permisos.</li>
                  <li>Porción acotada del caso de uso y luego otros módulos.</li>
                </ol>
              </div>
              <figcaption class="fig-caption">Fuente: Figura 2.1 y §4.8 — Hito 1 (S1 a S13) y Hito 2 (S14 a S22) con la ruta de adopción (el informe no tiene una sección de próximos pasos)</figcaption>
            </figure>
          </article>

          <!-- E5-6: Instalación de Aracne y Aegis (paquete de entrega) [cierre-instalacion] -->
          <article class="slide is-figure-wide" data-deck="e1-e4" data-module="e5" data-item="cierre-instalacion" data-tone="emerald">
            <div class="slide-content">
              <p class="slide-kicker">6 &middot; Decisiones y Cierre (Hito 1) &middot; Paquete de instalación</p>
              <h2>Instalación de Aracne y Aegis</h2>
              <ul class="slide-list">
                <li><strong>Aracne:</strong> guía a un asistente de inteligencia artificial para construir software en orden: planear, construir y revisar.</li>
                <li><strong>Aegis:</strong> da a cada persona su cuenta y un saldo mensual para usar la inteligencia artificial.</li>
                <li><strong>Verificación:</strong> cada paquete trae su huella SHA-256 para comprobar que llegó completo.</li>
              </ul>
            </div>
            <figure class="slide-figure" style="display:flex;flex-direction:column;gap:6px;">
              <div class="data-table-wrapper" style="flex:0 0 auto;min-height:0;height:auto;">
                <table class="data-table" style="font-size:clamp(0.9rem,min(1.7vw,3vh),1.5rem);">
                  <caption>La entrega tiene dos partes: el servidor y los computadores de las personas usuarias</caption>
                  <thead>
                    <tr><th>Parte</th><th>Qué incluye</th><th>Dónde se instala</th></tr>
                  </thead>
                  <tbody>
                    <tr><td data-label="Parte"><strong>1. Servidor Aegis</strong></td><td data-label="Qué incluye">Una guía en Word y un paquete para instalar Aegis con Docker</td><td data-label="Dónde se instala">Servidor Linux</td></tr>
                    <tr><td data-label="Parte"><strong>2. Computadores con Windows</strong></td><td data-label="Qué incluye">Un tutorial paso a paso con capturas reales, pensado para personas sin experiencia técnica, y el paquete de Aracne</td><td data-label="Dónde se instala">Computadores con Windows</td></tr>
                  </tbody>
                </table>
              </div>
              <ul class="slide-list" style="flex:0 0 auto;margin:10px 4px 0;font-size:clamp(0.9rem,1.3vw,1.2rem);">
                <li><strong>Descarga:</strong> <a href="https://drive.google.com/drive/folders/1vQbMZurvoBqzIMZMAEAUgQ_FEePQgrtj?usp=sharing" target="_blank" rel="noopener" style="overflow-wrap:anywhere;">https://drive.google.com/drive/folders/1vQbMZurvoBqzIMZMAEAUgQ_FEePQgrtj?usp=sharing</a></li>
              </ul>
            </figure>
          </article>
        </main>
      </div>

      <footer class="deck-controls">
        <p class="running-title">
          Informe Técnico E1–E4 · Contrato ATENEA-464-2026 · <abbr title="Universidad Nacional de Colombia">UNAL</abbr> Manizales / Agencia ATENEA.
        </p>
        <img
          class="controls-logo controls-logo-unal"
          src="assets/images/escudo_unal.png"
          alt="Universidad Nacional de Colombia"
        />
        <img
          class="controls-logo"
          src="assets/images/logo_labIA.png"
          alt="Laboratorio de Inteligencia Artificial UNAL"
        />
        <button type="button" id="prev" class="ghost" aria-label="Diapositiva anterior" title="Anterior">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
            <path d="M15 5 L8 12 L15 19" />
          </svg>
        </button>
        <span id="counter" aria-live="polite">01 / 74</span>
        <button type="button" id="next" class="solid" aria-label="Diapositiva siguiente" title="Siguiente">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
            <path d="M9 5 L16 12 L9 19" />
          </svg>
        </button>
      </footer>
    </div>

    <script src="assets/js/app.js?v=20261101_1"></script>
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
