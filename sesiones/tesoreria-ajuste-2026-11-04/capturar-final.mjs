import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const dir = path.dirname(fileURLToPath(import.meta.url));
function boxStr(b) {
  if (!b) return null;
  return [Math.round(b.x), Math.round(b.y), Math.round(b.width), Math.round(b.height)].join(',');
}
function pinPct(b, vp) {
  if (!b || !vp) return null;
  return {
    x: +(((b.x + b.width / 2) / vp.width) * 100).toFixed(2),
    y: +(((b.y + b.height / 2) / vp.height) * 100).toFixed(2),
  };
}

async function forceDemo(page) {
  await page.evaluate(() => {
    localStorage.setItem('almahue-erp-demo-mode', 'true');
    localStorage.setItem('almahue-erp-selected-empresa', 'EMP-1');
    localStorage.setItem('almahue-erp-periodo-contable', JSON.stringify({
      temporada: '2026', mesContable: '08', mesRemuneracion: '08', codigo: '2026-08',
    }));
    localStorage.setItem('almahue-erp-periodo-prompted', '1');
  });
}

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
await page.setViewportSize({ width: 1536, height: 960 });

await page.goto('http://localhost:5174/login', { waitUntil: 'domcontentloaded' });
await forceDemo(page);
await page.locator('input[type="email"], input[name="email"]').first().fill('admin@almahue.local');
await page.locator('input[type="password"]').fill('Admin123!');
await page.getByRole('button', { name: /Entrar con clave/i }).click();
await page.waitForTimeout(2500);
const confirmar = page.getByRole('button', { name: /Confirmar 2026/i });
if (await confirmar.count()) {
  await confirmar.first().click();
  await page.waitForTimeout(600);
}
await forceDemo(page);
await page.reload({ waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1200);

const out = {};

// ===== 1) Estado de cuenta: antes (sin modal) + despues (modal) =====
await page.goto('http://localhost:5174/tesoreria/cuentas-corrientes', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1800);
await page.screenshot({ path: path.join(dir, 'antes-estado-cuenta.png'), fullPage: false });
await page.getByRole('button', { name: 'Registrar ajuste' }).click();
await page.waitForTimeout(600);
await page.screenshot({ path: path.join(dir, 'despues-estado-cuenta-ajuste.png'), fullPage: false });
{
  const vp = page.viewportSize();
  out['estado-cuenta-ajuste'] = {};
  for (const [key, loc] of [
    ['btnAjuste', page.getByRole('button', { name: 'Registrar ajuste' })],
    ['tituloModal', page.getByRole('heading', { name: 'Ajuste estado de cuenta' })],
    ['tipo', page.locator('label').filter({ hasText: /^Tipo$/ })],
    ['debe', page.locator('label').filter({ hasText: /^Debe$/ })],
    ['haber', page.locator('label').filter({ hasText: /^Haber$/ })],
    ['glosa', page.locator('label').filter({ hasText: /^Glosa$/ })],
    ['guardar', page.getByRole('button', { name: 'Guardar' }).last()],
  ]) {
    const b = await loc.first().boundingBox().catch(() => null);
    out['estado-cuenta-ajuste'][key] = { boxStr: boxStr(b), pin: pinPct(b, vp) };
  }
}
await page.keyboard.press('Escape');
await page.waitForTimeout(400);

// ===== 2) Pagos TC: antes listado; despues editar MOSTOS o nuevo anticipo productor =====
await page.goto('http://localhost:5174/tesoreria/pagos', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2000);
await page.screenshot({ path: path.join(dir, 'antes-pagos-tc.png'), fullPage: false });

// Prefer edit MOSTOS
const search = page.getByPlaceholder(/Buscar/i);
if (await search.count()) {
  await search.fill('MOSTOS');
  await page.waitForTimeout(900);
}
let mode = 'nuevo';
const row = page.locator('tr').filter({ hasText: /MOSTOS/i }).first();
if (await row.count()) {
  await row.getByRole('button', { name: /Editar/i }).click();
  await page.waitForTimeout(900);
  // Si abre ficha solo lectura, Editar dentro del modal
  const modal = page.locator('.fixed.inset-0.z-50, [role=dialog]').last();
  const editarFicha = modal.getByRole('button', { name: /^Editar$|^Editar pago$/i });
  if (await editarFicha.count()) {
    await editarFicha.first().click({ force: true });
    await page.waitForTimeout(600);
  }
  mode = 'editar-mostos';
} else {
  await page.getByRole('button', { name: /Nuevo pago/i }).click();
  await page.waitForTimeout(700);
  // Custom Select: click Tipo combobox then option
  const tipoLabel = page.locator('label').filter({ hasText: /^Tipo$/ });
  const tipoTrigger = tipoLabel.locator('button, [role=combobox], [data-state]').first();
  if (await tipoTrigger.count()) {
    await tipoTrigger.click();
  } else {
    // click near the value text
    await page.getByText('Pago / cobro total').first().click();
  }
  await page.waitForTimeout(300);
  await page.getByRole('option', { name: /Anticipo productor/i }).click();
  await page.waitForTimeout(600);
  mode = 'nuevo-anticipo-productor';
}

// scroll to TC / historial
const anchor = page.getByText(/TC aplicado|Historial de tipo de cambio|Equivalente USD/i).first();
if (await anchor.count()) await anchor.scrollIntoViewIfNeeded();
await page.waitForTimeout(500);
await page.screenshot({ path: path.join(dir, 'despues-pagos-tc.png'), fullPage: false });

{
  const vp = page.viewportSize();
  out['pagos-tc'] = {};
  for (const [key, loc] of [
    ['tipo', page.locator('label').filter({ hasText: /^Tipo$/ })],
    ['monto', page.locator('label').filter({ hasText: /^Monto/ })],
    ['tc', page.locator('label').filter({ hasText: /TC aplicado/i })],
    ['equiv', page.getByText(/Equivalente USD/i)],
    ['historial', page.getByText(/Historial de tipo de cambio/i)],
    ['accion', page.getByRole('button', { name: /Crear|Guardar|Actualizar/i }).last()],
  ]) {
    const b = await loc.first().boundingBox().catch(() => null);
    out['pagos-tc'][key] = { boxStr: boxStr(b), pin: pinPct(b, vp) };
  }
  out['pagos-tc-mode'] = mode;
}

fs.writeFileSync(path.join(dir, 'measurements.json'), JSON.stringify(out, null, 2));
console.log(JSON.stringify(out, null, 2));
await browser.close();
