const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.type(), msg.text()));
  page.on('pageerror', err => console.error('BROWSER ERROR:', err.message));

  console.log('1. Loading http://localhost:8000/ ...');
  await page.goto('http://localhost:8000/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(__dirname, 'test_hub.png') });
  console.log('Screenshot saved: test_hub.png');

  // Check visibility of Hub vs Deck
  const isHubVisible = await page.$eval('#deck-hub-view', el => window.getComputedStyle(el).display);
  const isDeckVisible = await page.$eval('.deck-app', el => window.getComputedStyle(el).display);
  console.log('Hub display:', isHubVisible, '| Deck display:', isDeckVisible);

  console.log('2. Clicking Kick-off card...');
  await page.click('.hub-card[data-deck="kickoff"]');
  await page.waitForTimeout(600);
  await page.screenshot({ path: path.join(__dirname, 'test_kickoff.png') });
  console.log('Screenshot saved: test_kickoff.png');

  const deckAppStyles = await page.$eval('.deck-app', el => {
    const s = window.getComputedStyle(el);
    return {
      display: s.display,
      gridTemplateRows: s.gridTemplateRows,
      gridTemplateColumns: s.gridTemplateColumns,
      flexDirection: s.flexDirection,
      width: s.width,
      height: s.height
    };
  });
  console.log('Deck App styles after opening Kickoff:', deckAppStyles);

  console.log('3. Returning to Hub...');
  await page.click('#deck-selector-btn');
  await page.waitForTimeout(400);

  console.log('4. Clicking E1-E4 card...');
  await page.click('.hub-card[data-deck="e1-e4"]');
  await page.waitForTimeout(600);
  await page.screenshot({ path: path.join(__dirname, 'test_e1_e4.png') });
  console.log('Screenshot saved: test_e1_e4.png');

  // Check active slide in E1-E4
  const activeSlideInfo = await page.evaluate(() => {
    const active = document.querySelector('.slide.is-active');
    if (!active) return null;
    const s = window.getComputedStyle(active);
    return {
      id: active.id,
      dataset: active.dataset,
      display: s.display,
      visibility: s.visibility,
      opacity: s.opacity,
      width: s.width,
      height: s.height,
      content: active.querySelector('.slide-content')?.innerText?.slice(0, 80)
    };
  });
  console.log('Active slide in E1-E4:', activeSlideInfo);

  // Navigate forward in E1-E4 to test next slide
  console.log('5. Navigating to Slide 2 in E1-E4...');
  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(500);
  await page.screenshot({ path: path.join(__dirname, 'test_e1_e4_slide2.png') });
  console.log('Screenshot saved: test_e1_e4_slide2.png');

  const slide2Info = await page.evaluate(() => {
    const active = document.querySelector('.slide.is-active');
    if (!active) return null;
    const s = window.getComputedStyle(active);
    const fig = active.querySelector('.slide-figure');
    return {
      id: active.id,
      display: s.display,
      gridTemplateColumns: s.gridTemplateColumns,
      title: active.querySelector('h2')?.innerText,
      hasFigure: !!fig,
      figureDisplay: fig ? window.getComputedStyle(fig).display : null,
      figureWidth: fig ? window.getComputedStyle(fig).width : null,
      figureHeight: fig ? window.getComputedStyle(fig).height : null
    };
  });
  console.log('Slide 2 in E1-E4:', slide2Info);

  await browser.close();
  console.log('Done!');
})();
