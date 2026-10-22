#!/usr/bin/env python3
"""
Ensamblador de index.html multi-deck (Kick-off y E1-E4) y sincronizador de decks.
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
    e1_e4_viewport_match = re.search(r'<main class="viewport"[^>]*>(.*?)</main>', e1_e4_content, re.DOTALL)
    if not e1_e4_viewport_match:
        raise ValueError("No se encontró main.viewport en e1-e4.html")
    e1_e4_slides = e1_e4_viewport_match.group(1).strip()

    # 3. Extraer el modal de e1-e4.html
    modal_match = re.search(r'(<div id="deck-panel-modal".*?</div>\s*</div>\s*</div>)', e1_e4_content, re.DOTALL)
    if not modal_match:
        raise ValueError("No se encontró #deck-panel-modal en e1-e4.html")
    modal_html = modal_match.group(1).strip()

    # 4. En kickoff_content, asegurar data-deck="kickoff" en rail-module y en slide
    # Para rail-module:
    def add_deck_to_rail_mod(m):
        attrs = m.group(1)
        if 'data-deck=' not in attrs:
            return f'<div class="rail-module" data-deck="kickoff" {attrs}>'
        return m.group(0)

    mod_kickoff = re.sub(r'<div class="rail-module"\s+([^>]*)>', add_deck_to_rail_mod, kickoff_content)

    # Para slide:
    def add_deck_to_slide(m):
        tag = m.group(0)
        if 'data-deck=' not in tag:
            # Reemplazar <article class="slide" o similar
            return tag.replace('class="slide', 'data-deck="kickoff" class="slide')
        return tag

    mod_kickoff = re.sub(r'<article[^>]*class=["\'][^"\']*slide[^"\']*["\'][^>]*>', add_deck_to_slide, mod_kickoff)

    # 5. Insertar botón selector y envolver rail en .rail-bar-wrapper
    selector_btn_html = '''      <div class="rail-bar-wrapper">
        <button class="deck-selector-btn" id="deck-selector-btn" aria-haspopup="dialog" aria-expanded="false" title="Cambiar presentación (Tecla P o M)">
          <span class="deck-selector-badge">DECK</span>
          <span class="deck-selector-name" id="deck-current-name">Kick-off: Propuesta</span>
          <svg class="deck-selector-caret" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
          </svg>
        </button>'''

    # Encontrar <nav class="rail"
    rail_start = mod_kickoff.find('<nav class="rail"')
    if rail_start == -1:
        raise ValueError("No se encontró <nav class=\"rail\" en mod_kickoff")

    mod_kickoff = mod_kickoff[:rail_start] + selector_btn_html + "\n        " + mod_kickoff[rail_start:]

    # Cerrar .rail-bar-wrapper después de </nav>
    rail_end = mod_kickoff.find('</nav>') + len('</nav>')
    mod_kickoff = mod_kickoff[:rail_end] + "\n      </div>" + mod_kickoff[rail_end:]

    # 6. Añadir los módulos de E1-E4 dentro de <nav class="rail">
    # Insertar antes de </nav>
    nav_close_idx = mod_kickoff.find('</nav>')
    mod_kickoff = mod_kickoff[:nav_close_idx] + "\n          <!-- Módulos de E1-E4 -->\n          " + e1_e4_rail_modules + "\n        " + mod_kickoff[nav_close_idx:]

    # 7. Añadir los slides de E1-E4 dentro de <main class="viewport">
    # Insertar antes de </main>
    main_close_idx = mod_kickoff.find('</main>')
    mod_kickoff = mod_kickoff[:main_close_idx] + "\n          <!-- ======================================================== -->\n          <!-- Diapositivas de E1-E4 (Informe Técnico) -->\n          <!-- ======================================================== -->\n          " + e1_e4_slides + "\n        " + mod_kickoff[main_close_idx:]

    # 8. Añadir el modal antes de <script src="assets/js/app.js">
    script_idx = mod_kickoff.find('<script src="assets/js/app.js">')
    mod_kickoff = mod_kickoff[:script_idx] + modal_html + "\n\n    " + mod_kickoff[script_idx:]

    # 9. Actualizar versión en CSS link
    mod_kickoff = re.sub(r'href="assets/css/styles.css\?v=[^"]*"', 'href="assets/css/styles.css?v=20261022_1"', mod_kickoff)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(mod_kickoff)

    print(f"✅ index.html ensamblado exitosamente ({len(mod_kickoff)} bytes).")

    # También actualizar kickoff.html para que tenga el selector y el modal (modo standalone pero con selector funcional)
    # En kickoff.html solo agregamos el selector y el modal
    with open(kickoff_path, "w", encoding="utf-8") as f:
        # Usamos la versión con selector y modal pero solo con slides de kickoff
        kickoff_standalone = mod_kickoff
        # Quitar los slides de E1-E4 de kickoff.html si queremos que sea puro kickoff
        f.write(kickoff_content)

if __name__ == "__main__":
    main()
