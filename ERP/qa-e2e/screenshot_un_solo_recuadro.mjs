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

  // Scroll en el contenedor principal hacia abajo para ver el estrato de Jefaturas y el recuadro único
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

  // 1. Organigrama con paralelos OR y AND en UN SOLO RECUADRO (mostrando chips y +2)
  await page.screenshot({
    path: 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25/despues-paralelos-un-solo-recuadro.png',
  });
  console.log('1. Organigrama un solo recuadro capturado OK');

  // 2. Click en el badge "+2" para abrir la configuración del eslabón y ver la lista completa
  const plusTwoBadge = await page.$('button:has-text("+2")');
  if (plusTwoBadge) {
    await plusTwoBadge.click();
    await page.waitForTimeout(1000);
    await page.screenshot({
      path: 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25/despues-modal-todos-los-usuarios.png',
    });
    console.log('2. Modal ver todos los usuarios capturado OK');
  } else {
    // Si no encuentra +2, hacer click en el botón editar del eslabón
    const editBtns = await page.$$('button[title*="Configurar nombre"]');
    if (editBtns.length > 1) {
      await editBtns[1].click();
      await page.waitForTimeout(1000);
      await page.screenshot({
        path: 'C:/Users/c/.gemini/antigravity/brain/32ce2313-769c-4630-956e-d3cffea0fb25/despues-modal-todos-los-usuarios.png',
      });
      console.log('2. Modal alternativo capturado OK');
    }
  }
} catch (e) {
  console.error('Error:', e);
} finally {
  await browser.close();
  console.log('Finalizado.');
}
