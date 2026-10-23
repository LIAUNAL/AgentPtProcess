// ==========================================================================
// Deck Engine · LIA UNAL (Multi-Deck Support: Kick-off & E1-E4)
// ==========================================================================

const DECK_CONFIG = {
  kickoff: {
    id: "kickoff",
    name: "Kick-off: Propuesta SDLC-IA",
    kicker: "Propuesta de Entendimiento",
    runningTitle:
      'Agentes de <abbr title="Inteligencia Artificial">IA</abbr> en el ciclo de vida del desarrollo. Propuesta. <abbr title="Departamento de Ingeniería Electrónica y de Computadores (UNAL Manizales)">DIEEC</abbr>-<abbr title="Universidad Nacional de Colombia">UNAL</abbr>-Manizales.',
    badge: "Kick-off Inicial",
    storageKey: "deck-slide-kickoff"
  },
  "e1-e4": {
    id: "e1-e4",
    name: "Informe Técnico E1–E4",
    kicker: "Contrato ATENEA-464-2026",
    runningTitle:
      'Informe Técnico E1–E4 &middot; Contrato ATENEA-464-2026 &middot; <abbr title="Universidad Nacional de Colombia">UNAL</abbr> Manizales / Agencia ATENEA.',
    badge: "Hito 1 · Oct 2026",
    storageKey: "deck-slide-e1-e4"
  }
};

let currentDeck = "kickoff";
let slides = [];
let railModules = [];
let railTitles = [];
let current = 0;
let cleanupTimer = null;
let lastModule = null;
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

const counter = document.getElementById("counter");
const prevBtn = document.getElementById("prev");
const nextBtn = document.getElementById("next");
const deckApp = document.querySelector(".deck-app");
const modeBadge = document.getElementById("mode-badge");
const runningTitleEl = document.querySelector(".running-title");
const selectorBtn = document.getElementById("deck-selector-btn");
const selectorName = document.getElementById("deck-current-name");
const deckModal = document.getElementById("deck-panel-modal");
const deckCloseBtn = document.getElementById("deck-modal-close");
const deckCards = Array.from(document.querySelectorAll(".deck-card"));

const modeMap = {
  0: "normal",
  1: "command",
  2: "insert",
  3: "visual",
  4: "replace",
  5: "terminal",
  6: "normal",
  7: "command",
  8: "insert",
  9: "visual",
  10: "replace",
  11: "terminal"
};

function pad(value) {
  return String(value).padStart(2, "0");
}

function cleanupTransitionClasses(slide) {
  if (!slide) return;
  slide.classList.remove(
    "is-entering",
    "is-leaving",
    "from-next",
    "from-prev",
    "to-next",
    "to-prev"
  );
}

function buildDots() {
  // Limpiar contenedores de dots del deck activo
  railModules.forEach((mod) => {
    const modId = mod.dataset.module;
    const container = document.getElementById(`dots-${modId}`);
    if (container) container.innerHTML = "";
  });

  const moduleMap = {};
  slides.forEach((slide, idx) => {
    const mod = slide.dataset.module;
    if (!moduleMap[mod]) moduleMap[mod] = [];
    moduleMap[mod].push(idx);
  });

  Object.entries(moduleMap).forEach(([mod, indices]) => {
    const container = document.getElementById(`dots-${mod}`);
    if (!container) return;
    indices.forEach((slideIdx) => {
      const pip = document.createElement("button");
      pip.className = "rail-pip";
      pip.dataset.slide = slideIdx;
      pip.setAttribute("aria-label", `Slide ${slideIdx + 1}`);
      pip.addEventListener("click", () => render(slideIdx));
      container.appendChild(pip);
    });
  });
}

function updateChrome() {
  const pips = Array.from(document.querySelectorAll(".rail-pip"));
  pips.forEach((pip) => {
    pip.classList.toggle("is-active", Number(pip.dataset.slide) === current);
  });

  const currentModule = slides[current]?.dataset.module;
  const moduleChanged = currentModule !== lastModule;
  railModules.forEach((mod) => {
    const isActive = mod.dataset.module === currentModule;
    mod.classList.toggle("is-active-module", isActive);
    if (isActive && moduleChanged) {
      mod.scrollIntoView({ block: "nearest", inline: "center", behavior: "smooth" });
    }
  });
  lastModule = currentModule;

  if (counter) {
    counter.textContent = `${pad(current + 1)} / ${pad(slides.length)}`;
  }

  if (prevBtn) prevBtn.disabled = current === 0;
  if (nextBtn) nextBtn.disabled = current === slides.length - 1;

  const tone = slides[current]?.dataset.tone;
  const moduleIdx = Number(currentModule);
  const mode = modeMap[moduleIdx] || "normal";

  if (deckApp) {
    deckApp.className = deckApp.className
      .replace(/tone-\w+/g, "")
      .replace(/mode-\w+/g, "")
      .replace(/\s+/g, " ")
      .trim();

    if (tone) deckApp.classList.add(`tone-${tone}`);
    deckApp.classList.add(`mode-${mode}`);
  }

  if (modeBadge) {
    modeBadge.textContent = mode.toUpperCase();
  }
}

function render(index, options = {}) {
  if (slides.length === 0) return;
  const { animate = true } = options;
  const next = Math.max(0, Math.min(index, slides.length - 1));

  if (next === current && slides[current]?.classList.contains("is-active")) {
    updateChrome();
    return;
  }

  const previous = current;
  current = next;

  const config = DECK_CONFIG[currentDeck];
  if (config) {
    try {
      localStorage.setItem(config.storageKey, current);
    } catch (_) {}
  }

  if (cleanupTimer) {
    window.clearTimeout(cleanupTimer);
    cleanupTimer = null;
  }

  const currentSlide = slides[current];
  const previousSlide = slides[previous];

  slides.forEach((slide, idx) => {
    if (idx !== current && idx !== previous) {
      cleanupTransitionClasses(slide);
      slide.classList.remove("is-active");
    }
  });

  cleanupTransitionClasses(previousSlide);
  cleanupTransitionClasses(currentSlide);

  if (!animate || reduceMotion.matches || !previousSlide) {
    if (previousSlide) previousSlide.classList.remove("is-active");
    if (currentSlide) currentSlide.classList.add("is-active");
    updateChrome();
    return;
  }

  const direction = next > previous ? "next" : "prev";

  previousSlide.classList.remove("is-active");
  previousSlide.classList.add("is-leaving", direction === "next" ? "to-next" : "to-prev");

  currentSlide.classList.add(
    "is-active",
    "is-entering",
    direction === "next" ? "from-next" : "from-prev"
  );

  cleanupTimer = window.setTimeout(() => {
    slides.forEach((slide) => {
      cleanupTransitionClasses(slide);
      if (slide !== slides[current]) slide.classList.remove("is-active");
    });
    cleanupTimer = null;
  }, 440);

  updateChrome();
}

function initDeck(deckId) {
  if (!DECK_CONFIG[deckId]) deckId = "kickoff";
  currentDeck = deckId;

  // Actualizar atributo global del deck
  if (deckApp) {
    deckApp.setAttribute("data-active-deck", currentDeck);
  }

  // Filtrar slides del deck activo
  const allSlides = Array.from(document.querySelectorAll(".slide"));
  allSlides.forEach((s) => {
    const sDeck = s.dataset.deck || "kickoff";
    if (sDeck === currentDeck) {
      s.style.display = "";
    } else {
      s.style.display = "none";
      s.classList.remove("is-active", "is-entering", "is-leaving");
    }
  });

  slides = allSlides.filter((s) => (s.dataset.deck || "kickoff") === currentDeck);

  // Filtrar módulos del rail
  const allModules = Array.from(document.querySelectorAll(".rail-module"));
  allModules.forEach((m) => {
    const mDeck = m.dataset.deck || "kickoff";
    m.style.display = mDeck === currentDeck ? "" : "none";
  });

  railModules = allModules.filter((m) => (m.dataset.deck || "kickoff") === currentDeck);

  // Recalcular listener de títulos del rail
  railTitles = Array.from(document.querySelectorAll(".rail-title")).filter((t) => {
    const p = t.closest(".rail-module");
    return p && (p.dataset.deck || "kickoff") === currentDeck;
  });

  railTitles.forEach((title) => {
    title.onclick = () => {
      // El destino se calcula del primer slide del deck activo cuyo data-module
      // coincide con el módulo del rail; data-first queda solo como respaldo.
      const moduleId = title.closest(".rail-module")?.dataset.module;
      let target = slides.findIndex((s) => s.dataset.module === moduleId);
      if (target < 0) target = Number(title.dataset.first);
      if (Number.isFinite(target) && target >= 0) render(target);
    };
  });

  // Reconstruir dots
  buildDots();

  // Actualizar metadatos y controles
  const config = DECK_CONFIG[currentDeck];
  if (selectorName) selectorName.textContent = config.name;
  if (runningTitleEl) runningTitleEl.innerHTML = config.runningTitle;

  // Actualizar tarjetas en el modal
  deckCards.forEach((c) => {
    const isAct = c.dataset.deck === currentDeck;
    c.classList.toggle("is-active-deck", isAct);
    const btn = c.querySelector(".deck-card-btn");
    if (btn) btn.textContent = isAct ? "Presentación activa ✓" : "Cargar presentación";
  });

  // Guardar preferencia y actualizar URL sin recargar
  try {
    localStorage.setItem("active-deck", currentDeck);
    const url = new URL(window.location);
    url.searchParams.set("deck", currentDeck);
    window.history.replaceState({}, "", url);
  } catch (_) {}

  // Cargar slide guardado para este deck
  const saved = Number(localStorage.getItem(config.storageKey)) || 0;
  current = 0;
  render(Math.min(saved, Math.max(0, slides.length - 1)), { animate: false });
}

// --------------------------------------------------------------------------
// Hub Selector de Presentaciones (Landing View)
// --------------------------------------------------------------------------
const deckHubView = document.getElementById("deck-hub-view");
const hubCards = Array.from(document.querySelectorAll(".hub-card, .hub-card-btn"));

function showHub(pushState = true) {
  if (!deckHubView) return;
  document.body.classList.add("view-hub");
  document.body.classList.remove("view-deck");
  if (pushState) {
    try {
      const url = new URL(window.location);
      url.searchParams.delete("deck");
      window.history.pushState({}, "", url.pathname + (url.search || ""));
    } catch (_) {}
  }
}

function openDeck(deckId, pushState = true) {
  if (deckHubView) {
    document.body.classList.remove("view-hub");
    document.body.classList.add("view-deck");
  }
  initDeck(deckId);
  if (pushState) {
    try {
      const url = new URL(window.location);
      url.searchParams.set("deck", deckId);
      window.history.pushState({}, "", url);
    } catch (_) {}
  }
}

if (deckHubView) {
  hubCards.forEach((el) => {
    el.addEventListener("click", (e) => {
      const card = el.closest("[data-deck]");
      const targetDeck = card ? card.dataset.deck : null;
      if (targetDeck) {
        e.preventDefault();
        openDeck(targetDeck);
      }
    });
  });
}

// Popstate (navegación con botón atrás/adelante del navegador)
window.addEventListener("popstate", () => {
  if (!deckHubView) return;
  const p = new URLSearchParams(window.location.search);
  const d = p.get("deck");
  if (d && DECK_CONFIG[d]) {
    openDeck(d, false);
  } else {
    showHub(false);
  }
});

// --------------------------------------------------------------------------
// Modal y Panel de Control
// --------------------------------------------------------------------------
function toggleDeckModal(force) {
  if (deckHubView) {
    showHub();
    return;
  }
  if (!deckModal) return;
  const isOpen = force !== undefined ? force : !deckModal.classList.contains("is-open");
  deckModal.classList.toggle("is-open", isOpen);
  deckModal.setAttribute("aria-hidden", !isOpen);
  if (selectorBtn) selectorBtn.setAttribute("aria-expanded", isOpen);
}

if (selectorBtn) {
  selectorBtn.addEventListener("click", () => {
    if (deckHubView) {
      showHub();
    } else {
      toggleDeckModal();
    }
  });
}
if (deckCloseBtn) {
  deckCloseBtn.addEventListener("click", () => toggleDeckModal(false));
}
if (deckModal) {
  const backdrop = deckModal.querySelector(".deck-modal-backdrop");
  if (backdrop) backdrop.addEventListener("click", () => toggleDeckModal(false));
}

deckCards.forEach((card) => {
  card.addEventListener("click", (e) => {
    const targetDeck = card.dataset.deck;
    if (targetDeck) {
      openDeck(targetDeck);
      toggleDeckModal(false);
    }
  });
});

// --------------------------------------------------------------------------
// Navegación por botones y teclado
// --------------------------------------------------------------------------
if (prevBtn) prevBtn.addEventListener("click", () => render(current - 1));
if (nextBtn) nextBtn.addEventListener("click", () => render(current + 1));

window.addEventListener("keydown", (event) => {
  const opts = { animate: !event.repeat };
  if (event.key === "ArrowRight" || event.key === "PageDown" || event.key === " ") {
    event.preventDefault();
    render(current + 1, opts);
  }
  if (event.key === "ArrowLeft" || event.key === "PageUp") {
    event.preventDefault();
    render(current - 1, opts);
  }
  if (event.key === "Home") render(0);
  if (event.key === "End") render(slides.length - 1);
  if (event.key.toLowerCase() === "f") {
    document.body.classList.toggle("focus-mode");
  }
  if (event.key.toLowerCase() === "p" || event.key.toLowerCase() === "m") {
    if (deckHubView) {
      if (document.body.classList.contains("view-hub")) {
        openDeck(currentDeck || "e1-e4");
      } else {
        showHub();
      }
    } else {
      toggleDeckModal();
    }
  }
  if (event.key === "Escape") {
    if (deckModal?.classList.contains("is-open")) {
      toggleDeckModal(false);
    } else if (deckHubView && document.body.classList.contains("view-deck")) {
      showHub();
    }
  }
});

// --------------------------------------------------------------------------
// Gestos táctiles
// --------------------------------------------------------------------------
let touchStartX = 0;
window.addEventListener("touchstart", (event) => {
  touchStartX = event.changedTouches[0].screenX;
});
window.addEventListener("touchend", (event) => {
  const touchEndX = event.changedTouches[0].screenX;
  const delta = touchEndX - touchStartX;
  if (Math.abs(delta) < 40) return;
  if (delta < 0) render(current + 1);
  if (delta > 0) render(current - 1);
});

// --------------------------------------------------------------------------
// Inicialización al cargar la página
// --------------------------------------------------------------------------
function initApp() {
  const params = new URLSearchParams(window.location.search);
  const deckParam = params.get("deck");
  if (deckHubView) {
    if (deckParam && DECK_CONFIG[deckParam]) {
      openDeck(deckParam, false);
    } else {
      // Al iniciar, SOLO debe verse el panel selector de presentaciones
      showHub(false);
    }
  } else {
    const initialDeck = deckParam || (document.querySelector("[data-deck='e1-e4']") ? "e1-e4" : "kickoff");
    initDeck(initialDeck);
  }
}

let appInitialized = false;
function safeInit() {
  if (appInitialized) return;
  appInitialized = true;
  initApp();
}

document.addEventListener("DOMContentLoaded", safeInit);
if (document.readyState === "interactive" || document.readyState === "complete") {
  safeInit();
}
