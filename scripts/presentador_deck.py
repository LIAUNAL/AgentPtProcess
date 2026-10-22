#!/usr/bin/env python3
"""
Auditor y validador de presentaciones para el Agent Presentador.
Verifica la integridad de diapositivas, navegación, accesibilidad y consistencia de decks.
"""

import sys
import os
import re
from pathlib import Path

def validate_html(file_path):
    print(f"\n🔍 Auditando: {file_path}")
    if not os.path.exists(file_path):
        print(f"❌ Error: Archivo {file_path} no existe.")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    warnings = []

    # 1. Contar slides
    slides = re.findall(r'<article[^>]*class=["\'][^"\']*slide[^"\']*["\'][^>]*>', content)
    print(f"  📊 Diapositivas detectadas: {len(slides)}")
    if len(slides) == 0:
        errors.append("No se detectaron diapositivas (<article class='slide...'>).")

    # 2. Revisar SVG role y aria-label
    svgs = re.findall(r'<svg\b([^>]*)>', content)
    svg_without_label = 0
    for svg_attrs in svgs:
        # Ignore small icon SVGs in buttons or decorative sub-svgs
        if 'viewBox="0 0 24 24"' in svg_attrs or 'viewBox="0 0 20 20"' in svg_attrs or 'aria-hidden="true"' in svg_attrs:
            continue
        if 'aria-label=' not in svg_attrs and 'role="img"' not in svg_attrs:
            svg_without_label += 1

    if svg_without_label > 0:
        warnings.append(f"{svg_without_label} diagramas SVG no tienen aria-label o role='img' explícito.")

    # 3. Revisar imágenes existentes
    base_dir = os.path.dirname(os.path.abspath(file_path))
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for src in img_srcs:
        # Resolve relative to base_dir
        img_path = os.path.normpath(os.path.join(base_dir, src))
        if not os.path.exists(img_path):
            errors.append(f"Imagen referenciada no encontrada en disco: {src}")

    # 4. Revisar módulos de rail y contenedores de dots
    rail_modules = re.findall(r'data-module=["\']([^"\']+)["\']', content)
    dot_containers = re.findall(r'id=["\']dots-([^"\']+)["\']', content)
    print(f"  🏷️  Módulos encontrados: {set(rail_modules)}")
    print(f"  🔘 Contenedores de dots: {set(dot_containers)}")

    # 5. Revisar etiquetas de cierre básicas
    for tag in ["main", "nav", "footer", "body", "html"]:
        opens = len(re.findall(rf'<{tag}\b', content))
        closes = len(re.findall(rf'</{tag}>', content))
        if opens != closes:
            errors.append(f"Desbalance en etiquetas <{tag}>: {opens} abiertas vs {closes} cerradas.")

    # Reporte
    if warnings:
        for w in warnings:
            print(f"  ⚠️  Aviso: {w}")
    if errors:
        for e in errors:
            print(f"  ❌ Error: {e}")
        return False
    else:
        print("  ✅ Todo en orden. Validación estructural aprobada.")
        return True

def main():
    repo_root = Path(__file__).resolve().parent.parent
    files_to_check = [
        repo_root / "index.html",
        repo_root / "kickoff.html",
        repo_root / "e1-e4.html"
    ]

    all_passed = True
    for f in files_to_check:
        if f.exists():
            if not validate_html(f):
                all_passed = False
        else:
            print(f"ℹ️ Archivo {f.name} aún no existe.")

    if not all_passed:
        sys.exit(1)
    else:
        print("\n✨ Auditoría de presentaciones completada con éxito.\n")

if __name__ == "__main__":
    main()
