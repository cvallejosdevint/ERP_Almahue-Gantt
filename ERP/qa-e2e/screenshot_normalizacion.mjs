import { chromium } from 'playwright-core';
import path from 'path';

const brainDir = 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25';

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});

const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

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
  await page.keyboard.press('Escape');
  await page.waitForTimeout(500);

  // Click en el botón de edición de la tarjeta de Gerencia General
  // Es el botón de lápiz dentro de la tarjeta de Rango 1
  const btnEditGG = page.locator('div:has-text("RANGO 1") button[title*="Configurar"]').first();
  await btnEditGG.click();
  await page.waitForTimeout(800);

  // Tomar captura del modal
  await page.screenshot({
    path: path.join(brainDir, 'despues-normalizacion-modal-regla.png'),
  });
  console.log('Saved despues-normalizacion-modal-regla.png');

  console.log('Done.');
} catch (err) {
  console.error('Error:', err);
} finally {
  await browser.close();
}
