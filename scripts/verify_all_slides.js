const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(`Console error: ${msg.text()}`);
  });
  page.on('pageerror', err => errors.push(`Page error: ${err.message}`));

  const screenshotsDir = path.join(__dirname, 'screenshots');
  if (!fs.existsSync(screenshotsDir)) fs.mkdirSync(screenshotsDir);

  console.log('--- Testing Hub ---');
  await page.goto('http://localhost:8000/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(screenshotsDir, '00_hub.png') });

  console.log('--- Testing Kick-off Deck ---');
  await page.click('.hub-card[data-deck="kickoff"]');
  await page.waitForTimeout(400);

  let kickoffSlideCount = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.slide')).filter(s => (s.dataset.deck || 'kickoff') === 'kickoff').length;
  });
  console.log(`Kick-off active with ${kickoffSlideCount} slides.`);

  // Verify first 5 slides and last slide of Kick-off
  await page.screenshot({ path: path.join(screenshotsDir, 'kickoff_slide_01.png') });
  for (let i = 2; i <= 5; i++) {
    await page.keyboard.press('ArrowRight');
    await page.waitForTimeout(200);
    await page.screenshot({ path: path.join(screenshotsDir, `kickoff_slide_${String(i).padStart(2, '0')}.png`) });
  }

  console.log('--- Returning to Hub via Selector button ---');
  await page.click('#deck-selector-btn');
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(screenshotsDir, '01_hub_return.png') });

  console.log('--- Testing E1-E4 Deck ---');
  await page.click('.hub-card[data-deck="e1-e4"]');
  await page.waitForTimeout(400);

  let e1e4SlideCount = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.slide')).filter(s => s.dataset.deck === 'e1-e4').length;
  });
  console.log(`E1-E4 active with ${e1e4SlideCount} slides.`);

  const slideIssues = [];

  // Step through EVERY slide of E1-E4 (all 26 slides)
  for (let i = 0; i < e1e4SlideCount; i++) {
    const slideInfo = await page.evaluate((idx) => {
      const active = document.querySelector('.slide.is-active');
      if (!active) return { error: 'No active slide' };
      const s = window.getComputedStyle(active);
      const title = active.querySelector('h1, h2')?.innerText?.trim();
      const kicker = active.querySelector('.slide-kicker')?.innerText?.trim();
      const fig = active.querySelector('.slide-figure');
      const table = active.querySelector('.data-table');
      const svg = active.querySelector('svg');

      return {
        idx,
        kicker,
        title,
        width: parseFloat(s.width),
        height: parseFloat(s.height),
        hasFigure: !!fig,
        figWidth: fig ? parseFloat(window.getComputedStyle(fig).width) : 0,
        figHeight: fig ? parseFloat(window.getComputedStyle(fig).height) : 0,
        hasTable: !!table,
        hasSvg: !!svg,
        isCover: active.classList.contains('is-cover')
      };
    }, i);

    if (slideInfo.error) {
      slideIssues.push(`Slide ${i}: ${slideInfo.error}`);
    } else {
      if (slideInfo.width < 500) {
        slideIssues.push(`Slide ${i} (${slideInfo.title}): width too narrow (${slideInfo.width}px)`);
      }
      if (slideInfo.hasFigure && slideInfo.figWidth < 200) {
        slideIssues.push(`Slide ${i} (${slideInfo.title}): figure width too narrow (${slideInfo.figWidth}px)`);
      }
    }

    if (i < 10 || i === e1e4SlideCount - 1 || slideInfo.hasTable) {
      await page.screenshot({ path: path.join(screenshotsDir, `e1e4_slide_${String(i).padStart(2, '0')}.png`) });
    }

    if (i < e1e4SlideCount - 1) {
      await page.keyboard.press('ArrowRight');
      await page.waitForTimeout(150);
    }
  }

  console.log('--- Summary ---');
  console.log('Console/Page errors:', errors);
  console.log('Slide layout issues:', slideIssues);

  await browser.close();
  console.log('Done verification!');
})();
