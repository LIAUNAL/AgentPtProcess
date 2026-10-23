#!/usr/bin/env python3
"""Audit the E1-E4 deck (e1-e4.html) with Playwright.

Checks: coverage manifest, rail navigation, projector layout (incl. table text >= 12px), mobile rules.

Usage:
    python3 scripts/audit_e1e4_deck.py [--only coverage|rail|layout|mobile] [--shots DIR] [--target index|standalone]

Exit code is non-zero when any check fails.
"""
import argparse
import re
import socket
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent

# Required item ids per module: every id needs a slide with a captioned figure.
MANIFEST = {
    "e1": ["c1-madurez", "c1-brechas", "c1-datos", "c1-riesgos", "c1-caso-uso"],
    "e2": ["c2-fases", "c2-roles", "c2-criterios", "c2-control-humano",
           "c2-organizacion", "c2-instalacion", "c2-brechas-cierra"],
    "e3": ["c3-proceso", "c3-requisitos", "c3-historias", "c3-arquitectura-agentes",
           "c3-flujos", "c3-integraciones", "c3-datos", "c3-aceptacion"],
    "e4": ["c4-arquitectura", "c4-catalogo", "c4-instalacion", "c4-flujos-interaccion",
           "c4-control-humano", "c4-seguridad", "c4-trazabilidad"],
}
# Unnumbered informe sources (no table or figure) cite their section: "Fuente: §N.M".
CAPTION_RE = re.compile(r"^((Figura|Tabla) \d+\.\d+|Fuente: §\d+\.\d+)")

DESKTOP_VIEWPORTS = [(1920, 1080), (1366, 768), (1280, 720)]
MOBILE_PROFILES = {
    "iphone13": "iPhone 13",
    "pixel7": "Pixel 7",
    "ipad": "iPad (gen 7)",
    "landscape-844x390": None,  # custom
}

MIN_SVG_TEXT_PX = 11
MIN_TABLE_TEXT_PX = 12  # td computed size at projector viewports
MIN_TAP_PX = 44
MIN_DOT_PX = 32


class Report:
    """Collects failures per check and prints a concise summary."""

    def __init__(self):
        self.results = {}

    def add(self, check, msg):
        self.results.setdefault(check, []).append(msg)

    def touch(self, check):
        self.results.setdefault(check, [])

    def print(self):
        failed = False
        for check, msgs in self.results.items():
            if msgs:
                failed = True
                print(f"[FAIL] {check}: {len(msgs)} problem(s)")
                for m in msgs:
                    print(f"   - {m}")
            else:
                print(f"[PASS] {check}")
        return not failed


# ---------------------------------------------------------------- helpers
def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def start_server():
    port = free_port()
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    for _ in range(50):
        try:
            socket.create_connection(("127.0.0.1", port), 0.2).close()
            return proc, port
        except OSError:
            time.sleep(0.1)
    proc.kill()
    raise RuntimeError("http.server did not start")


# Page under audit for layout and mobile checks; --target switches between the
# standalone file and the live entry point (index.html with the deck selector).
TARGETS = {"standalone": "e1-e4.html", "index": "index.html?deck=e1-e4"}
TARGET = TARGETS["index"]


def open_deck(browser, base, url, **ctx_kwargs):
    ctx = browser.new_context(**ctx_kwargs)
    page = ctx.new_page()
    page.goto(f"{base}/{url}", wait_until="load")
    page.wait_for_function("typeof slides !== 'undefined' && slides.length > 0")
    return ctx, page


def slide_count(page):
    return page.evaluate("slides.length")


def go_to(page, idx):
    page.evaluate(f"render({idx}, {{animate:false}})")
    page.wait_for_timeout(30)


def slide_label(page, idx):
    return page.evaluate(
        "(i) => { const s = slides[i]; const h = s.querySelector('h2');"
        " return `#${i} [${s.dataset.module}] ${(h ? h.textContent : '').replace(/\\s+/g, ' ').trim().slice(0, 50)}`; }",
        idx,
    )


# ---------------------------------------------------------------- checks
def check_coverage(page, report):
    check = "coverage"
    report.touch(check)
    data = page.evaluate(
        """() => Array.from(document.querySelectorAll('.slide[data-deck=e1-e4], .slide'))
            .filter((s, i, a) => a.indexOf(s) === i)
            .map((s) => {
              const cap = s.querySelector('figure figcaption, figure caption, .data-table caption');
              return {
                items: (s.dataset.item || '').split(/\\s+/).filter(Boolean),
                module: s.dataset.module,
                hasFigure: !!s.querySelector('figure svg, figure table'),
                caption: cap ? cap.textContent.trim().replace(/\\s+/g, ' ') : null,
              };
            })"""
    )
    for module, ids in MANIFEST.items():
        for item in ids:
            slides_for = [d for d in data if item in d["items"]]
            if not slides_for:
                report.add(check, f"{item}: no slide with data-item")
                continue
            ok = [d for d in slides_for if d["hasFigure"] and d["caption"]
                  and CAPTION_RE.match(d["caption"]) and d["module"] == module]
            if ok:
                continue
            d = slides_for[0]
            if d["module"] != module:
                report.add(check, f"{item}: slide has data-module={d['module']}, expected {module}")
            elif not d["hasFigure"]:
                report.add(check, f"{item}: slide lacks figure with svg/table")
            else:
                report.add(check, f"{item}: caption missing or malformed ({d['caption']!r})")


def check_rail(browser, base, report):
    check = "rail"
    report.touch(check)
    ctx, page = open_deck(browser, base, "e1-e4.html", viewport={"width": 1366, "height": 768})
    titles = page.evaluate(
        """() => railTitles.map((t) => ({
            text: t.textContent.trim(),
            module: t.closest('.rail-module').dataset.module }))"""
    )
    for i, t in enumerate(titles):
        expected = page.evaluate(
            "(m) => slides.findIndex((s) => s.dataset.module === m)", t["module"])
        go_to(page, slide_count(page) - 1 if expected == 0 else 0)
        page.evaluate("(i) => railTitles[i].click()", i)
        page.wait_for_timeout(60)
        got = page.evaluate("current")
        if expected < 0:
            report.add(check, f"'{t['text']}': no slide with data-module={t['module']}")
        elif got != expected:
            report.add(check, f"'{t['text']}' ({t['module']}): landed on {got}, expected {expected}")
    ctx.close()
    # Smoke: the assembled index loads the same deck with the same slide count.
    ctx, page = open_deck(browser, base, "index.html?deck=e1-e4", viewport={"width": 1366, "height": 768})
    n_index = slide_count(page)
    ctx.close()
    ctx, page = open_deck(browser, base, "e1-e4.html", viewport={"width": 1366, "height": 768})
    n_std = slide_count(page)
    ctx.close()
    if n_index != n_std:
        report.add(check, f"index.html?deck=e1-e4 has {n_index} slides, e1-e4.html has {n_std}")


LAYOUT_JS = """(MIN_TD) => {
  const slide = slides[current];
  const out = [];
  const vw = innerWidth, vh = innerHeight;
  const roots = slide.querySelectorAll('.slide-content, .slide-figure');
  const seen = new Set();
  roots.forEach((root) => {
    [root, ...root.querySelectorAll('*')].forEach((el) => {
      if (seen.has(el)) return;
      seen.add(el);
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || el.closest('svg') && el.tagName !== 'svg') return;
      const clipY = ['hidden', 'clip', 'auto', 'scroll'].includes(cs.overflowY);
      const clipX = ['hidden', 'clip', 'auto', 'scroll'].includes(cs.overflowX);
      const label = el.tagName.toLowerCase() + (el.className && el.className.baseVal === undefined ? '.' + String(el.className).trim().split(/\\s+/).join('.') : '');
      if (clipY && el.scrollHeight > el.clientHeight + 2 && el.clientHeight > 0)
        out.push(`clipped-y ${label} (${el.scrollHeight}>${el.clientHeight})`);
      const scrollX = el.classList.contains('is-scroll-x') || (el.closest('.is-scroll-x') !== null);
      if (clipX && !scrollX && el.scrollWidth > el.clientWidth + 2 && el.clientWidth > 0)
        out.push(`clipped-x ${label} (${el.scrollWidth}>${el.clientWidth})`);
    });
  });
  // Table body text must stay legible when projected.
  const minTd = Math.min(...Array.from(slide.querySelectorAll('.data-table td'))
    .filter((td) => td.getBoundingClientRect().width > 0)
    .map((td) => parseFloat(getComputedStyle(td).fontSize)));
  if (minTd < MIN_TD) out.push(`table text ${minTd.toFixed(1)}px < ${MIN_TD}px`);
  // Captions must be visible inside the viewport.
  slide.querySelectorAll('figcaption, figure caption').forEach((c) => {
    const r = c.getBoundingClientRect();
    const cs = getComputedStyle(c);
    if (cs.display === 'none' || cs.visibility === 'hidden' || r.height === 0)
      out.push('caption hidden');
    else if (r.bottom > vh + 1 || r.top < -1 || r.right > vw + 1 || r.left < -1)
      out.push(`caption outside viewport (${Math.round(r.top)}-${Math.round(r.bottom)} of ${vh})`);
  });
  // Overlapping SVG <text> boxes.
  slide.querySelectorAll('svg').forEach((svg) => {
    const sr = svg.getBoundingClientRect();
    if (sr.width === 0) return;
    const texts = Array.from(svg.querySelectorAll('text'))
      .filter((t) => !t.closest('[data-allow-overlap]'))
      .map((t) => ({ t, r: t.getBoundingClientRect() }))
      .filter((o) => o.r.width > 0 && o.r.height > 0);
    for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
      const a = texts[i].r, b = texts[j].r;
      const w = Math.min(a.right, b.right) - Math.max(a.left, b.left);
      const h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
      if (w <= 0 || h <= 0) continue;
      const small = Math.min(a.width * a.height, b.width * b.height);
      if (w * h > 0.2 * small)
        out.push(`svg text overlap: "${texts[i].t.textContent.trim().slice(0, 24)}" / "${texts[j].t.textContent.trim().slice(0, 24)}"`);
    }
  });
  return out;
}"""


def check_layout(browser, base, report, shots):
    check = "layout"
    report.touch(check)
    for w, h in DESKTOP_VIEWPORTS:
        ctx, page = open_deck(browser, base, TARGET, viewport={"width": w, "height": h})
        for i in range(slide_count(page)):
            go_to(page, i)
            for problem in page.evaluate(LAYOUT_JS, MIN_TABLE_TEXT_PX):
                report.add(check, f"{w}x{h} {slide_label(page, i)}: {problem}")
            save_shot(page, shots, f"{w}x{h}", i)
        ctx.close()


MOBILE_SLIDE_JS = """(minText) => {
  const slide = slides[current];
  const out = [];
  if (document.documentElement.scrollWidth > innerWidth + 1)
    out.push(`page scrolls horizontally (${document.documentElement.scrollWidth}>${innerWidth})`);
  const altVisible = Array.from(slide.querySelectorAll('.mobile-alt, .schedule-mobile'))
    .some((e) => e.getBoundingClientRect().height > 0 && getComputedStyle(e).display !== 'none');
  slide.querySelectorAll('svg').forEach((svg) => {
    const r = svg.getBoundingClientRect();
    if (r.width === 0 || getComputedStyle(svg).display === 'none' || altVisible) return;
    const scale = svg.getScreenCTM() ? svg.getScreenCTM().a : 1;
    let min = Infinity, which = '';
    svg.querySelectorAll('text').forEach((t) => {
      const px = parseFloat(getComputedStyle(t).fontSize) * scale;
      if (px < min) { min = px; which = t.textContent.trim().slice(0, 24); }
    });
    if (min < minText) out.push(`svg text ${min.toFixed(1)}px < ${minText}px ("${which}")`);
  });
  if (innerWidth <= 560) {
    slide.querySelectorAll('table').forEach((tb) => {
      if (tb.closest('.is-scroll-x') || tb.classList.contains('is-scroll-x')) return;
      if (tb.getBoundingClientRect().width === 0) return;
      const missing = Array.from(tb.querySelectorAll('tbody td')).filter((td) => !td.dataset.label).length;
      if (missing) out.push(`table without is-scroll-x has ${missing} td without data-label`);
    });
  }
  return out;
}"""

CONTROLS_JS = """([minBtn, minDot]) => {
  const out = [];
  const vis = (e) => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && !e.closest('[hidden]'); };
  const dots = new Set(document.querySelectorAll('.rail-dots button, .rail-pip'));
  const sel = '.rail-title, .deck-selector-btn, button';
  document.querySelectorAll(sel).forEach((e) => {
    if (!vis(e) || e.closest('.slide') || e.closest('#deck-panel-modal')) return;
    const r = e.getBoundingClientRect();
    const name = (e.className || e.tagName) + ' "' + (e.textContent || e.getAttribute('aria-label') || '').trim().slice(0, 20) + '"';
    if (dots.has(e)) {
      if (r.width < minDot || r.height < minDot)
        out.push(`dot ${Math.round(r.width)}x${Math.round(r.height)} < ${minDot}px: ${name}`);
    } else if (r.height < minBtn) {
      out.push(`control height ${Math.round(r.height)} < ${minBtn}px: ${name}`);
    }
  });
  return out;
}"""


def mobile_context_kwargs(pw, name, profile):
    if profile is None:  # landscape phone
        return dict(viewport={"width": 844, "height": 390}, has_touch=True, is_mobile=True,
                    device_scale_factor=2)
    dev = pw.devices.get(profile)
    if dev is None:
        print(f"  (device '{profile}' unavailable, using iPhone 13)")
        dev = pw.devices["iPhone 13"]
    return dict(dev)


def check_mobile(pw, browser, base, report, shots):
    check = "mobile"
    report.touch(check)
    for name, profile in MOBILE_PROFILES.items():
        kwargs = mobile_context_kwargs(pw, name, profile)
        kwargs["has_touch"] = True
        ctx, page = open_deck(browser, base, TARGET, **kwargs)
        w = page.evaluate("innerWidth")
        tag = f"{name} {w}px"
        for problem in page.evaluate(CONTROLS_JS, [MIN_TAP_PX, MIN_DOT_PX]):
            report.add(check, f"{tag} chrome: {problem}")
        for i in range(slide_count(page)):
            go_to(page, i)
            for problem in page.evaluate(MOBILE_SLIDE_JS, MIN_SVG_TEXT_PX):
                report.add(check, f"{tag} {slide_label(page, i)}: {problem}")
            save_shot(page, shots, name, i)
        ctx.close()


def save_shot(page, shots, tag, idx):
    if not shots:
        return
    out = Path(shots)
    out.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(out / f"{tag}-{idx:02d}.png"))


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--only", choices=["coverage", "rail", "layout", "mobile"])
    ap.add_argument("--shots", help="directory for per-slide PNG screenshots")
    ap.add_argument("--target", choices=sorted(TARGETS), default="index",
                    help="page used by the layout and mobile checks")
    args = ap.parse_args()
    global TARGET
    TARGET = TARGETS[args.target]
    wanted = lambda n: args.only in (None, n)

    report = Report()
    server, port = start_server()
    base = f"http://127.0.0.1:{port}"
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            if wanted("coverage"):
                ctx, page = open_deck(browser, base, "e1-e4.html", viewport={"width": 1366, "height": 768})
                check_coverage(page, report)
                ctx.close()
            if wanted("rail"):
                check_rail(browser, base, report)
            if wanted("layout"):
                check_layout(browser, base, report, args.shots)
            if wanted("mobile"):
                check_mobile(pw, browser, base, report, args.shots)
            browser.close()
    finally:
        server.kill()
    sys.exit(0 if report.print() else 1)


if __name__ == "__main__":
    main()
