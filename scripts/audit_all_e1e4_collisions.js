const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://localhost:8000/', { waitUntil: 'domcontentloaded' });
  await page.click('.hub-card[data-deck="e1-e4"]');
  await page.waitForTimeout(400);

  const total = await page.evaluate(() => document.querySelectorAll('.slide[data-deck="e1-e4"]').length);
  console.log(`Auditing ALL ${total} slides in E1-E4 for SVG & Table text overlaps...\n`);

  for (let idx = 0; idx < total; idx++) {
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
    }, idx);

    await page.waitForTimeout(100);

    const issues = await page.evaluate((idx) => {
      const s = document.querySelector('.slide.is-active');
      const title = s.querySelector('h2')?.innerText?.replace(/\n/g, ' ');
      const svg = s.querySelector('svg');
      const table = s.querySelector('.data-table');
      const wrapper = s.querySelector('.data-table-wrapper');
      const content = s.querySelector('.slide-content');

      const found = [];

      // Check content vertical overflow
      if (content && content.scrollHeight - content.clientHeight > 2) {
        found.push({
          type: 'CONTENT_OVERFLOW_Y',
          detail: `Content diff: ${content.scrollHeight - content.clientHeight}px`
        });
      }

      // Check table wrapper vertical overflow
      if (wrapper && wrapper.scrollHeight - wrapper.clientHeight > 2) {
        found.push({
          type: 'TABLE_WRAPPER_OVERFLOW_Y',
          detail: `Table wrapper diff: ${wrapper.scrollHeight - wrapper.clientHeight}px (table: ${table?.clientHeight}px, wrapper: ${wrapper.clientHeight}px)`
        });
      }

      // Check SVG overlaps
      if (svg) {
        const texts = Array.from(svg.querySelectorAll('text')).map(t => ({
          text: t.textContent.trim(),
          r: t.getBoundingClientRect()
        })).filter(t => t.r.width > 0 && t.r.height > 0);

        for (let i = 0; i < texts.length; i++) {
          for (let j = i + 1; j < texts.length; j++) {
            const t1 = texts[i];
            const t2 = texts[j];
            const ox = Math.max(0, Math.min(t1.r.right, t2.r.right) - Math.max(t1.r.left, t2.r.left));
            const oy = Math.max(0, Math.min(t1.r.bottom, t2.r.bottom) - Math.max(t1.r.top, t2.r.top));
            if (ox > 5 && oy > 4) {
              found.push({
                type: 'SVG_TEXT_OVERLAP',
                detail: `"${t1.text}" overlaps "${t2.text}" by ${ox.toFixed(1)}px x ${oy.toFixed(1)}px`
              });
            }
          }
        }

        // Check text spilling out of SVG
        const svgR = svg.getBoundingClientRect();
        texts.forEach(t => {
          if (t.r.right > svgR.right + 2) {
            found.push({
              type: 'SVG_TEXT_SPILL_RIGHT',
              detail: `"${t.text}" spills right by ${(t.r.right - svgR.right).toFixed(1)}px`
            });
          }
          if (t.r.left < svgR.left - 2) {
            found.push({
              type: 'SVG_TEXT_SPILL_LEFT',
              detail: `"${t.text}" spills left by ${(svgR.left - t.r.left).toFixed(1)}px`
            });
          }
        });
      }

      return { idx, title, found };
    }, idx);

    if (issues.found.length > 0) {
      console.log(`[Slide ${idx}] "${issues.title}":`);
      issues.found.forEach(f => console.log(`   * [${f.type}] ${f.detail}`));
    }
  }

  await browser.close();
})();
