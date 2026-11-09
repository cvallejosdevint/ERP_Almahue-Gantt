import { chromium } from 'playwright-core';

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});

const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });

try {
  await page.goto('http://127.0.0.1:5174/login', { waitUntil: 'networkidle' });

  // Login
  const emailInput = await page.$('input[type="email"]');
  if (emailInput) {
    await page.fill('input[type="email"]', 'admin@almahue.local');
    await page.fill('input[type="password"]', 'Admin123!');
    await page.click('button:has-text("Entrar con clave")');
    await page.waitForTimeout(1500);
  }

  await page.goto('http://127.0.0.1:5174/admin/aprobaciones', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  // Cerrar modal de periodo contable si aparece
  const modalPeriodoBtn = await page.$('button:has-text("Confirmar"), button:has-text("Más tarde")');
  if (modalPeriodoBtn) {
    await modalPeriodoBtn.click();
    await page.waitForTimeout(1000);
  }

  // Scroll en el contenedor principal hacia abajo para ver el estrato de Jefaturas
  await page.evaluate(() => {
    const containers = Array.from(document.querySelectorAll('*')).filter(
      (el) => el.scrollHeight > el.clientHeight && getComputedStyle(el).overflowY.includes('auto')
    );
    for (const c of containers) {
      c.scrollBy(0, 420);
    }
    window.scrollBy(0, 420);
  });
  await page.waitForTimeout(600);

  // 1. Captura de la tarjeta AND de Packing corregida (sin etiqueta redundante, 1 sola línea)
  await page.screenshot({
    path: 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25/despues-and-limpio-una-linea.png',
  });
  console.log('1. Captura normal OK');

  // 2. Con zoom o ancho reducido para validar que NO se parte en 2 líneas
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.waitForTimeout(500);
  await page.screenshot({
    path: 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25/despues-and-zoom-una-linea.png',
  });
  console.log('2. Captura con zoom OK');
} catch (e) {
  console.error('Error:', e);
} finally {
  await browser.close();
  console.log('Finalizado.');
}

