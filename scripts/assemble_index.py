#!/usr/bin/env python3
"""
Ensamblador de index.html multi-deck (Kick-off y E1-E4) con Hub Selector de Presentaciones como vista inicial.
"""

import re
from pathlib import Path

def main():
    repo_root = Path(__file__).resolve().parent.parent
    kickoff_path = repo_root / "kickoff.html"
    e1_e4_path = repo_root / "e1-e4.html"
    index_path = repo_root / "index.html"

    with open(kickoff_path, "r", encoding="utf-8") as f:
        kickoff_content = f.read()

    with open(e1_e4_path, "r", encoding="utf-8") as f:
        e1_e4_content = f.read()

    # 1. Extraer los módulos de rail de E1-E4
    e1_e4_rail_match = re.search(r'<nav class="rail"[^>]*>(.*?)</nav>', e1_e4_content, re.DOTALL)
    if not e1_e4_rail_match:
        raise ValueError("No se encontró nav.rail en e1-e4.html")
    e1_e4_rail_modules = e1_e4_rail_match.group(1).strip()

    # 2. Extraer los slides de E1-E4
    e1_e4_viewport_match = re.search(r'<main class="(?:deck-)?viewport"[^>]*>\s*<section class="stage"[^>]*>(.*?)</section>\s*</main>', e1_e4_content, re.DOTALL)
    if not e1_e4_viewport_match:
        # Fallback sin stage
        e1_e4_viewport_match = re.search(r'<main class="(?:deck-)?viewport"[^>]*>(.*?)</main>', e1_e4_content, re.DOTALL)
        if not e1_e4_viewport_match:
            raise ValueError("No se encontró main.viewport ni main.deck-viewport en e1-e4.html")
    e1_e4_slides = e1_e4_viewport_match.group(1).strip()

    # 3. En kickoff_content, asegurar data-deck="kickoff" en rail-module y en slide
    def add_deck_to_rail_mod(m):
        attrs = m.group(1)
        if 'data-deck=' not in attrs:
            return f'<div class="rail-module" data-deck="kickoff" {attrs}>'
        return m.group(0)

    mod_kickoff = re.sub(r'<div class="rail-module"\s+([^>]*)>', add_deck_to_rail_mod, kickoff_content)

    def add_deck_to_slide(m):
        tag = m.group(0)
        if 'data-deck=' not in tag:
            return tag.replace('class="slide', 'data-deck="kickoff" class="slide')
        return tag

    mod_kickoff = re.sub(r'<article[^>]*class=["\'][^"\']*slide[^"\']*["\'][^>]*>', add_deck_to_slide, mod_kickoff)

    # 4. Asegurar que <body class="view-hub"> sea la clase inicial en index.html
    mod_kickoff = re.sub(r'<body[^>]*>', '<body class="view-hub">', mod_kickoff)

    # 5. Insertar botón selector y envolver rail en .rail-bar-wrapper
    selector_btn_html = '''      <div class="rail-bar-wrapper">
        <button class="deck-selector-btn" id="deck-selector-btn" aria-haspopup="dialog" aria-expanded="false" title="Cambiar presentación (Tecla P o M)">
          <span class="deck-selector-badge">DECK</span>
          <span class="deck-selector-name" id="deck-current-name">Kick-off: Propuesta</span>
          <span class="deck-selector-switch" style="font-size:0.75rem; color:var(--accent); font-weight:700; margin-left:6px;">← Selector</span>
        </button>'''

    rail_start = mod_kickoff.find('<nav class="rail"')
    if rail_start == -1:
        raise ValueError("No se encontró <nav class=\"rail\" en mod_kickoff")

    mod_kickoff = mod_kickoff[:rail_start] + selector_btn_html + "\n        " + mod_kickoff[rail_start:]

    rail_end = mod_kickoff.find('</nav>') + len('</nav>')
    mod_kickoff = mod_kickoff[:rail_end] + "\n      </div>" + mod_kickoff[rail_end:]

    # 6. Añadir los módulos de E1-E4 dentro de <nav class="rail">
    nav_close_idx = mod_kickoff.find('</nav>')
    mod_kickoff = mod_kickoff[:nav_close_idx] + "\n          <!-- Módulos de E1-E4 -->\n          " + e1_e4_rail_modules + "\n        " + mod_kickoff[nav_close_idx:]

    # 7. Añadir los slides de E1-E4 dentro de <section class="stage"> o <main class="viewport">
    stage_close_idx = mod_kickoff.find('</section>')
    if stage_close_idx != -1:
        insert_idx = stage_close_idx
    else:
        insert_idx = mod_kickoff.find('</main>')

    mod_kickoff = mod_kickoff[:insert_idx] + "\n          <!-- ======================================================== -->\n          <!-- Diapositivas de E1-E4 (Informe Técnico) -->\n          <!-- ======================================================== -->\n          " + e1_e4_slides + "\n        " + mod_kickoff[insert_idx:]

    # 8. Insertar el Hub Selector de Presentaciones justo antes de </main> o después de .deck-app
    hub_view_html = '''
    <!-- ====================================================================== -->
    <!-- Pantalla de Selección de Presentación (Landing Hub View)               -->
    <!-- ====================================================================== -->
    <div id="deck-hub-view" class="deck-hub-view">
      <div class="hub-container">
        <header class="hub-header">
          <div class="hub-logos">
            <img class="hub-logo" src="assets/images/escudo_unal.png" alt="Universidad Nacional de Colombia" />
            <img class="hub-logo" src="assets/images/logo_labIA.png" alt="Laboratorio de Inteligencia Artificial" />
            <img class="hub-logo" src="assets/images/logo-atenea.png" alt="Agencia Distrital ATENEA" />
          </div>
          <p class="hub-kicker">LABORATORIO DE INTELIGENCIA ARTIFICIAL &middot; UNAL MANIZALES &middot; CONTRATO ATENEA-464-2026</p>
          <h1 class="hub-title">Sistema de Presentaciones Técnicas e Institucionales</h1>
          <p class="hub-subtitle">Selecciona la presentación que deseas consultar o proyectar:</p>
        </header>

        <div class="hub-cards-grid">
          <!-- Tarjeta 1: Kick-off -->
          <div class="hub-card" data-deck="kickoff">
            <div class="hub-card-header">
              <span class="hub-card-tag tag-blue">PROPUESTA INICIAL</span>
              <span class="hub-card-meta">45 Diapositivas &middot; 6 Módulos</span>
            </div>
            <div>
              <h2 class="hub-card-title">Kick-off: Propuesta SDLC-IA</h2>
              <p class="hub-card-desc">Adopción conceptual y técnica de agentes de IA en el ciclo de vida del software: motivación, evolución de roles, evidencia empírica industrial (SWE-bench), arnés metodológico y arquitectura SpecWeaver.</p>
            </div>
            <ul class="hub-card-pills">
              <li>Minuta Contractual</li>
              <li>Motivación &amp; Perfiles</li>
              <li>Chat vs Agente</li>
              <li>SWE-bench</li>
              <li>SpecWeaver</li>
            </ul>
            <button class="hub-card-btn" type="button" data-deck="kickoff">
              <span>Iniciar Presentación Kick-off</span>
              <span>&rarr;</span>
            </button>
          </div>

          <!-- Tarjeta 2: E1-E4 -->
          <div class="hub-card" data-deck="e1-e4">
            <div class="hub-card-header">
              <span class="hub-card-tag">HITO 1 CONTRACTUAL</span>
              <span class="hub-card-meta">64 Diapositivas &middot; 6 Módulos</span>
            </div>
            <div>
              <h2 class="hub-card-title">Informe Técnico E1–E4: Avance de Hito 1</h2>
              <p class="hub-card-desc">Avance del Hito 1 alineado con el informe técnico (corte al 23 de octubre de 2026): diagnóstico de E1 (madurez, DORA, riesgos y datos), metodología SDLC-IA con 7 puntos de control humano (E2), los ocho elementos del caso de uso y la arquitectura del arnés (E3), Aracne-SDLC-AI 0.9.0 con agentes, comandos, instalación, seguridad y trazabilidad (E4), y las decisiones, la información pendiente y los compromisos de ATENEA. Funciona también en el celular.</p>
            </div>
            <ul class="hub-card-pills">
              <li>Contrato &amp; Alcance</li>
              <li>C1 · E1 Diagnóstico</li>
              <li>C2 · E2 Metodología SDLC-IA</li>
              <li>C3 · E3 Arquitectura y caso de uso</li>
              <li>C4 · E4 Aracne-SDLC-AI 0.9.0</li>
              <li>Decisiones &amp; Cierre</li>
            </ul>
            <button class="hub-card-btn" type="button" data-deck="e1-e4">
              <span>Iniciar Presentación E1–E4</span>
              <span>&rarr;</span>
            </button>
          </div>
        </div>

        <footer class="hub-footer">
          <div>
            <span>Acceso directo por URL: <code>?deck=e1-e4</code> | <code>?deck=kickoff</code></span>
          </div>
          <div>
            <span>Atajos en presentación: <kbd>→</kbd> <kbd>Espacio</kbd> avanzar &middot; <kbd>←</kbd> retroceder &middot; <kbd>P</kbd> / <kbd>M</kbd> selector &middot; <kbd>F</kbd> pantalla completa</span>
          </div>
        </footer>
      </div>
    </div>
'''

    # Insertar el Hub Selector de Presentaciones justo después de <div class="ambient"></div>
    ambient_idx = mod_kickoff.find('<div class="ambient"></div>')
    if ambient_idx != -1:
        insert_hub_idx = ambient_idx + len('<div class="ambient"></div>')
        mod_kickoff = mod_kickoff[:insert_hub_idx] + "\n" + hub_view_html + "\n" + mod_kickoff[insert_hub_idx:]
    else:
        script_idx = mod_kickoff.find('<script src="assets/js/app.js"')
        mod_kickoff = mod_kickoff[:script_idx] + hub_view_html + "\n\n    " + mod_kickoff[script_idx:]

    # 9. Actualizar versión en CSS link
    mod_kickoff = re.sub(r'src="assets/js/app.js[^"]*"', 'src="assets/js/app.js?v=20261023_4"', mod_kickoff)
    mod_kickoff = re.sub(r'href="assets/css/styles.css\?v=[^"]*"', 'href="assets/css/styles.css?v=20261023_4"', mod_kickoff)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(mod_kickoff)

    print(f"✅ index.html ensamblado exitosamente ({len(mod_kickoff)} bytes).")

if __name__ == "__main__":
    main()
