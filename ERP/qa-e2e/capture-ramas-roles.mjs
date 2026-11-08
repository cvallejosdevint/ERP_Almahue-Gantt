import { chromium } from 'playwright-core';
import { mkdir } from 'node:fs/promises';

const out = 'E:/source/repos/Almahue/docs/sesiones/acuerdos-sala-2026-11-06';
await mkdir(out, { recursive: true });

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});
const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
page.setDefaultTimeout(20000);

async function masTarde() {
  const btn = page.getByRole('button', { name: 'Más tarde', exact: true });
  if (await btn.count() && await btn.first().isVisible().catch(() => false)) {
    await btn.first().click().catch(() => {});
    await page.waitForTimeout(200);
  }
}

// 1. Inicializar sesión y modo demo
await page.goto('http://127.0.0.1:5174/', { waitUntil: 'domcontentloaded' });
await page.evaluate(() => {
  localStorage.setItem('almahue-erp-demo-mode', 'true');
  localStorage.setItem('almahue-erp-empresa-id', 'EMP-1');
  localStorage.setItem('almahue-erp-periodo-contable', '2026-08');
  localStorage.setItem('erp.session', JSON.stringify({
    id: 'U-1',
    nombre: 'Admin Almahue',
    email: 'admin@almahue.local',
    rolId: 'ROL-1',
    rolNombre: 'Administrador General',
    empresaId: 'EMP-1',
    empresaNombre: 'ALMAHUE EXPORT SPA',
    permisos: ['*'],
    token: 'demo-token',
  }));
});

// 2. Navegar a /admin/aprobaciones (Esquema de Ramas Dinámicas con Nivel de Rama)
console.log('Navegando a /admin/aprobaciones...');
await page.goto('http://127.0.0.1:5174/admin/aprobaciones', { waitUntil: 'networkidle' });
await page.waitForTimeout(1000);
await masTarde();

// Clic en el botón "Evaluar Ruta de Aprobación" del simulador
const btnEvaluar = page.getByRole('button', { name: /Evaluar Ruta de Aprobación/i });
if (await btnEvaluar.count()) {
  await btnEvaluar.click().catch(() => {});
  await page.waitForTimeout(800);
}

// Tomar captura de la vista Esquema de Ramas con ramas dinámicas ordenadas por su nivel
await page.screenshot({ path: `${out}/despues-esquema-ramas-aprobacion.png` });
console.log('Captura despues-esquema-ramas-aprobacion.png guardada exitosamente');

// Abrir modal de Nueva Rama
const btnNuevaRama = page.getByRole('button', { name: /\+ Nueva Rama/i });
if (await btnNuevaRama.count()) {
  await btnNuevaRama.click().catch(() => {});
  await page.waitForTimeout(600);
  await page.screenshot({ path: `${out}/despues-modal-nueva-rama.png` });
  console.log('Captura despues-modal-nueva-rama.png guardada exitosamente');

  // Cerrar modal
  const btnCancelarRama = page.getByRole('button', { name: /Cancelar/i });
  if (await btnCancelarRama.count()) {
    await btnCancelarRama.click().catch(() => {});
    await page.waitForTimeout(300);
  }
}

// Abrir modal de configuración de un eslabón (ej. Jefatura de Riego)
const editButtons = page.locator('button[title*="Configurar nombre"]');
if (await editButtons.count()) {
  await editButtons.nth(2).click().catch(() => {});
  await page.waitForTimeout(600);
  await page.screenshot({ path: `${out}/despues-eslabon-configurar-modal.png` });
  console.log('Captura despues-eslabon-configurar-modal.png guardada exitosamente');

  // Cerrar modal
  const btnCancelar = page.getByRole('button', { name: /Cancelar/i });
  if (await btnCancelar.count()) {
    await btnCancelar.click().catch(() => {});
    await page.waitForTimeout(300);
  }
}

// 3. Navegar a /admin/usuarios
console.log('Navegando a /admin/usuarios...');
await page.goto('http://127.0.0.1:5174/admin/usuarios', { waitUntil: 'networkidle' });
await page.waitForTimeout(1000);
await masTarde();

// Tomar captura de la tabla de usuarios con la columna de Cargo y Jefatura
await page.screenshot({ path: `${out}/despues-usuarios-cargo-arbol.png` });
console.log('Captura despues-usuarios-cargo-arbol.png guardada exitosamente');

// Abrir modal de edición del primer usuario
const editButtonsUsuarios = page.locator('button[title*="Editar"], button:has(svg.lucide-pencil), button:has(svg.lucide-edit-2), button:has(svg.lucide-edit)');
if (await editButtonsUsuarios.count()) {
  await editButtonsUsuarios.first().click().catch(() => {});
  await page.waitForTimeout(700);
  await page.screenshot({ path: `${out}/despues-modal-editar-usuario.png` });
  console.log('Captura despues-modal-editar-usuario.png guardada exitosamente');

  // Cerrar modal
  const btnCancelar = page.getByRole('button', { name: /Cancelar/i });
  if (await btnCancelar.count()) {
    await btnCancelar.click().catch(() => {});
    await page.waitForTimeout(300);
  }
}

// 4. Navegar a /admin/organigrama
console.log('Navegando a /admin/organigrama...');
await page.goto('http://127.0.0.1:5174/admin/organigrama', { waitUntil: 'networkidle' });
await page.waitForTimeout(1000);
await masTarde();

await page.screenshot({ path: `${out}/despues-organigrama-jerarquia.png` });
console.log('Captura despues-organigrama-jerarquia.png guardada exitosamente');

await browser.close();
console.log('Todas las capturas Playwright generadas con resolución 1536x960.');
