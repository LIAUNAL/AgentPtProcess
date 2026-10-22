const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://localhost:8000/', { waitUntil: 'domcontentloaded' });
  await page.click('.hub-card[data-deck="e1-e4"]');
  await page.waitForTimeout(400);

  const outDir = path.join(__dirname, 'detailed_audit');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);

  const indices = [1, 2, 8, 9, 13, 14, 21, 22];

  for (const idx of indices) {
    // Navigate to slide idx
    await page.evaluate((targetIdx) => {
      const slides = Array.from(document.querySelectorAll('.slide[data-deck="e1-e4"]'));
      slides.forEach((s, i) => {
        if (i === targetIdx) {
          s.classList.add('is-active');
          s.style.display = '';
        } else {
          s.classList.remove('is-active');
          s.style.display = 'none';
        }
      });
      // trigger render logic if needed
    }, idx);

    await page.waitForTimeout(150);

    const report = await page.evaluate((idx) => {
      const active = document.querySelector('.slide.is-active');
      const title = active.querySelector('h2')?.innerText?.replace(/\n/g, ' ');
      const content = active.querySelector('.slide-content');
      const figure = active.querySelector('.slide-figure');
      const svg = active.querySelector('svg');
      const table = active.querySelector('.data-table');
      const tableWrapper = active.querySelector('.data-table-wrapper');

      // 1. Text content overflows
      const contentOverflow = {
        clientHeight: content?.clientHeight,
        scrollHeight: content?.scrollHeight,
        diffY: (content?.scrollHeight || 0) - (content?.clientHeight || 0),
        clientWidth: content?.clientWidth,
        scrollWidth: content?.scrollWidth,
        diffX: (content?.scrollWidth || 0) - (content?.clientWidth || 0)
      };

      // 2. Table overflows
      let tableOverflow = null;
      if (table) {
        tableOverflow = {
          wrapperHeight: tableWrapper?.clientHeight,
          wrapperScrollHeight: tableWrapper?.scrollHeight,
          wrapperDiffY: (tableWrapper?.scrollHeight || 0) - (tableWrapper?.clientHeight || 0),
          wrapperWidth: tableWrapper?.clientWidth,
          wrapperScrollWidth: tableWrapper?.scrollWidth,
          wrapperDiffX: (tableWrapper?.scrollWidth || 0) - (tableWrapper?.clientWidth || 0),
          tableHeight: table.clientHeight,
          tableWidth: table.clientWidth
        };
      }

      // 3. SVG text collisions & out-of-bounds
      let svgIssues = [];
      if (svg) {
        const svgRect = svg.getBoundingClientRect();
        const texts = Array.from(svg.querySelectorAll('text')).map(t => {
          const r = t.getBoundingClientRect();
          return {
            el: t,
            text: t.textContent.trim(),
            rect: r,
            relX: r.left - svgRect.left,
            relY: r.top - svgRect.top,
            relRight: r.right - svgRect.left,
            relBottom: r.bottom - svgRect.top
          };
        });

        // Out-of-bounds text
        texts.forEach(t => {
          if (t.rect.width > 0) {
            if (t.relRight > svgRect.width + 2) {
              svgIssues.push({
                type: 'TEXT_OUT_OF_SVG_RIGHT',
                text: t.text,
                diff: t.relRight - svgRect.width
              });
            }
            if (t.relX < -2) {
              svgIssues.push({
                type: 'TEXT_OUT_OF_SVG_LEFT',
                text: t.text,
                diff: -t.relX
              });
            }
          }
        });

        // Text-Text collisions
        for (let i = 0; i < texts.length; i++) {
          for (let j = i + 1; j < texts.length; j++) {
            const t1 = texts[i];
            const t2 = texts[j];
            if (t1.rect.width === 0 || t2.rect.width === 0) continue;

            const overlapX = Math.max(0, Math.min(t1.rect.right, t2.rect.right) - Math.max(t1.rect.left, t2.rect.left));
            const overlapY = Math.max(0, Math.min(t1.rect.bottom, t2.rect.bottom) - Math.max(t1.rect.top, t2.rect.top));

            if (overlapX > 4 && overlapY > 4) {
              svgIssues.push({
                type: 'TEXT_COLLISION',
                text1: t1.text,
                text2: t2.text,
                overlapX,
                overlapY
              });
            }
          }
        }

        // Rect-Text boundary checks: does text spill outside its enclosing box?
        const rects = Array.from(svg.querySelectorAll('rect')).map(r => r.getBoundingClientRect());
        // For each text, check if it was supposed to be inside a box but spills outside
      }

      return {
        idx,
        title,
        contentOverflow,
        tableOverflow,
        svgIssues
      };
    }, idx);

    await page.screenshot({ path: path.join(outDir, `slide_${String(idx).padStart(2, '0')}.png`) });
    console.log(`=== Slide Index ${idx}: "${report.title}" ===`);
    console.log('Content Overflow:', report.contentOverflow);
    if (report.tableOverflow) console.log('Table Overflow:', report.tableOverflow);
    if (report.svgIssues.length > 0) console.log('SVG Issues:', report.svgIssues);
    console.log('--------------------------------------------------\n');
  }

  await browser.close();
})();
