// npm install --no-save playwright
// npx playwright install chromium
// node scripts/export-slides.cjs [output directory]
// Optional: CHROME_EXECUTABLE=/path/to/chromium
const { chromium } = require('playwright');
const fs = require('node:fs/promises');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

(async () => {
  const root = path.resolve(__dirname, '..');
  const output = path.resolve(process.argv[2] || path.join(root, 'exports'));
  const launch = { headless: true };
  if (process.env.CHROME_EXECUTABLE) launch.executablePath = process.env.CHROME_EXECUTABLE;
  if (process.env.CHROME_EXECUTABLE) launch.args = ['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage'];
  const browser = await chromium.launch(launch);
  const page = await browser.newPage({ viewport: { width: 1200, height: 1600 }, deviceScaleFactor: 1 });
  const failures = [];
  const errors = [];
  page.on('pageerror', err => errors.push(err.message));
  await page.goto(pathToFileURL(path.join(root, 'carousel-ai-edge21.html')).href);
  await page.evaluate(() => document.fonts.ready);
  await page.addStyleTag({ content: 'body{padding:0!important} .toolbar,.slide-label,.export-note{display:none!important} main{display:block!important;max-width:none!important}.preview-row{margin:0!important}.slide-wrapper{width:1080px!important;height:var(--height)!important}.slide{transform:none!important}.slide-canvas:before,.slide-canvas:after{display:none!important}' });
  const layerChecks = await page.evaluate(() => {
    const findings = [];
    for (const slide of document.querySelectorAll('.slide')) {
      const frame = slide.querySelector('.slide-canvas').getBoundingClientRect();
      for (const el of slide.querySelectorAll('.editable')) {
        const b = el.getBoundingClientRect();
        const range = document.createRange(); range.selectNodeContents(el);
        const text = range.getBoundingClientRect();
        if (text.right > b.right + 2 || text.left < b.left - 2) findings.push(slide.id + ': text exceeds box: ' + el.textContent);
        if (b.left < frame.left+90 || b.right > frame.right-90 || b.top < frame.top+180 || b.bottom > frame.top+1260) findings.push(slide.id + ': outside shared text area: ' + el.textContent);
      }
    }
    return findings;
  });
  failures.push(...layerChecks);
  for (const ratio of ['3x4', '4x5']) {
    await fs.mkdir(path.join(output, ratio), { recursive: true });
    await page.evaluate(r => document.body.classList.toggle('ratio45', r==='4x5'), ratio);
    for (let i=1; i<=10; i++) {
      const id = String(i).padStart(2,'0');
      const el = page.locator('#slide-'+id);
      const b = await el.boundingBox();
      const height = ratio==='3x4' ? 1440 : 1350;
      if (b.width !== 1080 || b.height !== height) failures.push(`${id}/${ratio}: wrong export dimensions`);
      await el.screenshot({ path: path.join(output,ratio,`edge21-${id}.png`), animations:'disabled' });
    }
  }
  await page.evaluate(()=>document.body.classList.remove('ratio45'));
  await page.pdf({path:path.join(output,'Edge21-Carousel-Review.pdf'),printBackground:true,preferCSSPageSize:true});
  await page.reload();
  await page.evaluate(() => document.fonts.ready);
  await page.getByRole('button',{name:'Show guides'}).click();
  if (!await page.locator('body').evaluate(x=>x.classList.contains('guides'))) failures.push('Guide toggle failed');
  await page.getByRole('button',{name:'Edit copy'}).click();
  if (await page.locator('[contenteditable="true"]').count()!==await page.locator('.editable').count()) failures.push('Edit toggle failed');
  const dlPromise=page.waitForEvent('download');
  await page.getByRole('button',{name:'Save template'}).click();
  const download=await dlPromise;
  const saved=path.join(output,'qa-saved-template.html'); await download.saveAs(saved);
  await page.goto(pathToFileURL(saved).href);
  if (await page.locator('.slide').count()!==10) failures.push('Saved template lost slides');
  if (await page.locator('body').evaluate(x=>x.classList.contains('editing')||x.classList.contains('guides'))) failures.push('Saved template retained editing overlays');
  await fs.unlink(saved);
  await browser.close();
  const report={slides:10,formats:['1080x1440','1080x1350'],font_loading:'embedded',failures,console_errors:errors};
  await fs.writeFile(path.join(output,'qa-report.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify(report,null,2));
  if(failures.length||errors.length) process.exitCode=1;
})().catch(err=>{console.error(err);process.exit(1)});
