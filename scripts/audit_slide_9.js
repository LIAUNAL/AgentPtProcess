const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://localhost:8000/', { waitUntil: 'domcontentloaded' });
  await page.click('.hub-card[data-deck="e1-e4"]');
  await page.waitForTimeout(400);

  // Navigate to slide 9
  await page.evaluate(() => {
    const slides = Array.from(document.querySelectorAll('.slide[data-deck="e1-e4"]'));
    slides.forEach((s, i) => {
      if (i === 9) {
        s.classList.add('is-active');
        s.style.display = '';
      } else {
        s.classList.remove('is-active');
        s.style.display = 'none';
      }
    });
  });
  await page.waitForTimeout(200);

  const findings = await page.evaluate(() => {
    const s = document.querySelector('.slide.is-active');
    const svg = s.querySelector('svg');
    const svgRect = svg.getBoundingClientRect();

    const texts = Array.from(svg.querySelectorAll('text')).map(t => {
      const r = t.getBoundingClientRect();
      return {
        text: t.textContent.trim(),
        r,
        top: r.top,
        bottom: r.bottom,
        left: r.left,
        right: r.right,
        width: r.width,
        height: r.height
      };
    });

    const rects = Array.from(svg.querySelectorAll('rect')).map(rc => {
      const r = rc.getBoundingClientRect();
      return {
        id: rc.id || rc.getAttribute('fill') || rc.getAttribute('stroke'),
        r,
        top: r.top,
        bottom: r.bottom,
        left: r.left,
        right: r.right,
        width: r.width,
        height: r.height
      };
    });

    // Check which texts are outside their intended rects or colliding
    const overlaps = [];
    texts.forEach(t => {
      // Find enclosing or nearest rect
      rects.forEach(rc => {
        // If text overlaps rect boundary
        const isHorizNear = Math.abs(t.left - rc.left) < 15 || Math.abs(t.right - rc.right) < 15;
        const isVertInside = t.top >= rc.top - 5 && t.bottom <= rc.bottom + 5;
        if (isVertInside) {
          if (t.right > rc.right) {
            overlaps.push({
              text: t.text,
              issue: `Text spills out of rect by ${(t.right - rc.right).toFixed(1)}px (text right: ${t.right.toFixed(1)}, rect right: ${rc.right.toFixed(1)})`
            });
          }
          if (t.left < rc.left) {
            overlaps.push({
              text: t.text,
              issue: `Text spills out of rect left by ${(rc.left - t.left).toFixed(1)}px`
            });
          }
        }
      });
    });

    return { svgRect, texts, rects, overlaps };
  });

  console.log('Slide 9 SVG Audit:');
  console.log('Overlaps/Spills:', findings.overlaps);
  await browser.close();
})();
