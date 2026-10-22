const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  await page.goto('http://localhost:8000/', { waitUntil: 'domcontentloaded' });
  await page.click('.hub-card[data-deck="e1-e4"]');
  await page.waitForTimeout(400);

  const outDir = path.join(__dirname, 'audit_slides');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);

  // We want to inspect slides 1, 2, 8, 9, 13, 14, 21, 22
  const targetIndices = [1, 2, 8, 9, 13, 14, 21, 22];

  const results = {};

  for (let idx = 0; idx < 26; idx++) {
    if (targetIndices.includes(idx)) {
      const info = await page.evaluate((idx) => {
        const active = document.querySelector('.slide.is-active');
        if (!active) return { error: 'No active slide' };
        const title = active.querySelector('h1, h2')?.innerText?.replace(/\n/g, ' ')?.trim();
        const kicker = active.querySelector('.slide-kicker')?.innerText?.trim();
        const content = active.querySelector('.slide-content');
        const figure = active.querySelector('.slide-figure');
        const table = active.querySelector('.data-table');
        const svg = active.querySelector('svg');

        // Check text overflow in content
        const cScrollHeight = content?.scrollHeight || 0;
        const cClientHeight = content?.clientHeight || 0;
        const cScrollWidth = content?.scrollWidth || 0;
        const cClientWidth = content?.clientWidth || 0;

        // Check table overflow
        const tableScroll = active.querySelector('.table-scroll');
        const tScrollWidth = table?.scrollWidth || 0;
        const tClientWidth = table?.clientWidth || 0;

        // Check SVG text collisions / overlaps if SVG exists
        const svgCollisions = [];
        if (svg) {
          const texts = Array.from(svg.querySelectorAll('text'));
          for (let i = 0; i < texts.length; i++) {
            const r1 = texts[i].getBoundingClientRect();
            if (r1.width === 0 || r1.height === 0) continue;
            for (let j = i + 1; j < texts.length; j++) {
              const r2 = texts[j].getBoundingClientRect();
              if (r2.width === 0 || r2.height === 0) continue;
              // Check collision with small margin tolerance
              const overlapX = Math.max(0, Math.min(r1.right, r2.right) - Math.max(r1.left, r2.left));
              const overlapY = Math.max(0, Math.min(r1.bottom, r2.bottom) - Math.max(r1.top, r2.top));
              const area = overlapX * overlapY;
              if (area > 15 && overlapX > 5 && overlapY > 4) {
                svgCollisions.push({
                  text1: texts[i].textContent.trim(),
                  text2: texts[j].textContent.trim(),
                  overlapX,
                  overlapY,
                  area
                });
              }
            }
          }
        }

        // Check HTML elements overlap inside content
        const pTags = Array.from(active.querySelectorAll('p, li, td, th'));
        const htmlCollisions = [];
        for (let i = 0; i < pTags.length; i++) {
          const r1 = pTags[i].getBoundingClientRect();
          if (r1.width === 0 || r1.height === 0) continue;
          for (let j = i + 1; j < pTags.length; j++) {
            // Ignore ancestors
            if (pTags[i].contains(pTags[j]) || pTags[j].contains(pTags[i])) continue;
            const r2 = pTags[j].getBoundingClientRect();
            const overlapX = Math.max(0, Math.min(r1.right, r2.right) - Math.max(r1.left, r2.left));
            const overlapY = Math.max(0, Math.min(r1.bottom, r2.bottom) - Math.max(r1.top, r2.top));
            if (overlapX > 20 && overlapY > 8) {
              htmlCollisions.push({
                el1: pTags[i].textContent.slice(0, 30),
                el2: pTags[j].textContent.slice(0, 30),
                overlapX,
                overlapY
              });
            }
          }
        }

        return {
          idx,
          title,
          kicker,
          hasSvg: !!svg,
          hasTable: !!table,
          contentOverflowY: cScrollHeight - cClientHeight,
          contentOverflowX: cScrollWidth - cClientWidth,
          svgCollisions,
          htmlCollisions,
          tableScrollable: !!tableScroll
        };
      }, idx);

      results[idx] = info;
      await page.screenshot({ path: path.join(outDir, `slide_${String(idx).padStart(2, '0')}.png`) });
    }

    if (idx < 25) {
      await page.keyboard.press('ArrowRight');
      await page.waitForTimeout(150);
    }
  }

  console.log(JSON.stringify(results, null, 2));
  await browser.close();
})();
