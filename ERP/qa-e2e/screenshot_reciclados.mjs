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

  // 1. Organigrama con conectores intermedios + y botones + Persona
  await page.screenshot({
    path: 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25/despues-botones-intermedios-organigrama.png',
  });
  console.log('1. Organigrama capturado OK');

  // 2. Click en botón "+ Persona"
  const plusPersonaBtn = await page.$('button:has-text("+ Persona")');
  if (plusPersonaBtn) {
    await plusPersonaBtn.click();
    await page.waitForTimeout(800);
    await page.screenshot({
      path: 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25/despues-modal-asignacion-rapida-persona.png',
    });
    console.log('2. Modal Asignación Rápida capturado OK');

    // Cerrar modal de asignación rápida con Escape
    await page.keyboard.press('Escape');
    await page.waitForTimeout(1000);
  }

  // 3. Click en configurar eslabón (para mostrar PIN y Suplente)
  const editBtns = await page.$$('button[title*="Configurar nombre"]');
  if (editBtns.length > 1) {
    await editBtns[1].click();
    await page.waitForTimeout(1000);
    await page.screenshot({
      path: 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25/despues-modal-configuracion-pin-suplente.png',
    });
    console.log('3. Modal Configuración PIN y Suplente capturado OK');
  }
} catch (e) {
  console.error('Error:', e);
} finally {
  await browser.close();
  console.log('Finalizado.');
}
