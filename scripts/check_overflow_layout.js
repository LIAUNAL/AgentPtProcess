const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function runCheck(viewport = { width: 1440, height: 900 }) {
  console.log(`\n==================================================`);
  console.log(`Starting Layout & Overflow Audit at ${viewport.width}x${viewport.height}`);
  console.log(`==================================================\n`);

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(`[Console Error] ${msg.text()}`);
  });
  page.on('pageerror', err => errors.push(`[Page Error] ${err.message}`));

  await page.goto('http://localhost:8000/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  const findings = [];

  // Helper to audit the currently active slide
  async function auditActiveSlide(deckName, slideIdx) {
    const result = await page.evaluate(({ deckName, slideIdx }) => {
      const activeSlide = document.querySelector('.slide.is-active');
      if (!activeSlide) return { error: `No active slide found for index ${slideIdx}` };

      const issues = [];
      const slideRect = activeSlide.getBoundingClientRect();
      const slideComputed = window.getComputedStyle(activeSlide);
      const title = activeSlide.querySelector('h1, h2')?.innerText?.replace(/\n/g, ' ')?.trim() || 'Untitled';
      const kicker = activeSlide.querySelector('.slide-kicker')?.innerText?.trim() || '';

      // 1. Check if the slide itself overflows its parent viewport
      const viewportEl = activeSlide.closest('.deck-viewport');
      if (viewportEl) {
        const vRect = viewportEl.getBoundingClientRect();
        if (slideRect.bottom > vRect.bottom + 5) {
          issues.push({
            type: 'SLIDE_OVERFLOW_VIEWPORT',
            detail: `Slide bottom (${slideRect.bottom.toFixed(1)}px) exceeds viewport bottom (${vRect.bottom.toFixed(1)}px) by ${(slideRect.bottom - vRect.bottom).toFixed(1)}px`
          });
        }
      }

      // 2. Check all text & card containers inside the slide for overflow
      const candidates = activeSlide.querySelectorAll(
        '.slide-content, .slide-figure, .slide-header, .cover-team, .cover-members, ' +
        '.metric-card, .deliverable-card, .status-card, .takeaway-block, ' +
        '.prose, blockquote, .cover-body, .cover-aside, .data-table, .table-scroll'
      );

      candidates.forEach(el => {
        const cs = window.getComputedStyle(el);
        const overflowY = cs.overflowY;
        const overflowX = cs.overflowX;

        // If it's a scrollable container (like .table-scroll or .figure-scroll), horizontal scroll is intentional
        const isScrollableTable = el.classList.contains('table-scroll') || el.classList.contains('figure-scroll') || el.classList.contains('data-table');
        
        // Vertical overflow check
        if (!isScrollableTable && el.clientHeight > 0 && el.scrollHeight - el.clientHeight > 8) {
          // Check if overflow is hidden (clipping) or visible (spilling)
          issues.push({
            type: 'VERTICAL_OVERFLOW',
            tag: el.className || el.tagName,
            detail: `Height: ${el.clientHeight}px, ScrollHeight: ${el.scrollHeight}px (diff: ${el.scrollHeight - el.clientHeight}px), overflowY: ${overflowY}`
          });
        }

        // Horizontal overflow check
        if (!isScrollableTable && el.clientWidth > 0 && el.scrollWidth - el.clientWidth > 10) {
          issues.push({
            type: 'HORIZONTAL_OVERFLOW',
            tag: el.className || el.tagName,
            detail: `Width: ${el.clientWidth}px, ScrollWidth: ${el.scrollWidth}px (diff: ${el.scrollWidth - el.clientWidth}px), overflowX: ${overflowX}`
          });
        }
      });

      // 3. Check for text truncation / collisions in lists or headers
      const headings = activeSlide.querySelectorAll('h1, h2, h3');
      headings.forEach(h => {
        if (h.scrollWidth > h.clientWidth + 5) {
          issues.push({
            type: 'HEADING_OVERFLOW',
            text: h.innerText.slice(0, 40),
            detail: `Heading scrollWidth (${h.scrollWidth}px) > clientWidth (${h.clientWidth}px)`
          });
        }
      });

      return {
        deckName,
        slideIdx,
        title,
        kicker,
        slideWidth: slideRect.width,
        slideHeight: slideRect.height,
        issues
      };
    }, { deckName, slideIdx });

    return result;
  }

  // --- Audit Kick-off ---
  console.log(`Auditing Kick-off Deck...`);
  await page.click('.hub-card[data-deck="kickoff"]');
  await page.waitForTimeout(400);

  const kickoffCount = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.slide')).filter(s => (s.dataset.deck || 'kickoff') === 'kickoff').length;
  });

  console.log(`Kick-off total slides: ${kickoffCount}`);

  for (let i = 0; i < kickoffCount; i++) {
    const report = await auditActiveSlide('Kick-off', i);
    if (report.issues && report.issues.length > 0) {
      findings.push(report);
    }
    if (i < kickoffCount - 1) {
      await page.keyboard.press('ArrowRight');
      await page.waitForTimeout(100);
    }
  }

  // --- Return to Hub ---
  await page.click('#deck-selector-btn');
  await page.waitForTimeout(300);

  // --- Audit E1-E4 ---
  console.log(`Auditing E1-E4 Deck...`);
  await page.click('.hub-card[data-deck="e1-e4"]');
  await page.waitForTimeout(400);

  const e1e4Count = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.slide')).filter(s => s.dataset.deck === 'e1-e4').length;
  });

  console.log(`E1-E4 total slides: ${e1e4Count}`);

  for (let i = 0; i < e1e4Count; i++) {
    const report = await auditActiveSlide('E1-E4', i);
    if (report.issues && report.issues.length > 0) {
      findings.push(report);
    }
    if (i < e1e4Count - 1) {
      await page.keyboard.press('ArrowRight');
      await page.waitForTimeout(100);
    }
  }

  await browser.close();

  console.log(`\nAudit completed for ${viewport.width}x${viewport.height}:`);
  console.log(`Total issues found: ${findings.length}`);
  if (findings.length > 0) {
    findings.forEach(f => {
      console.log(`\n[${f.deckName}] Slide ${f.slideIdx}: "${f.title}" (${f.slideWidth}x${f.slideHeight})`);
      f.issues.forEach(iss => console.log(`  - [${iss.type}] ${iss.tag || ''}: ${iss.detail || iss.text}`));
    });
  } else {
    console.log(`  ✓ Perfect layout! No text overflows, no clipping, no viewport breaches.`);
  }

  return findings;
}

(async () => {
  // Test standard laptop resolution
  const f1 = await runCheck({ width: 1440, height: 900 });
  // Test standard 1080p full HD display
  const f2 = await runCheck({ width: 1920, height: 1080 });
  // Test lower resolution (1280x800) to see if small screens overflow
  const f3 = await runCheck({ width: 1280, height: 800 });
})();
