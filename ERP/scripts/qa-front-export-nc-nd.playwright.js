/** QA front exportación: 6 facturas 110, 2 NC, 2 ND, 2 anulaciones. Usado por Playwright MCP. */
module.exports = async (page) => {
  page.setDefaultTimeout(180000);
  const log = [];
  const facturas = [];

  async function dismissPeriodo() {
    const btn = page.getByRole('button', { name: /Confirmar 20/i });
    if (await btn.isVisible({ timeout: 4000 }).catch(() => false)) {
      await page.getByLabel('Año').selectOption('2026').catch(() => {});
      await page.getByLabel('Mes contable').selectOption('09').catch(() => {});
      await page.getByRole('button', { name: /Confirmar 2026-09/i }).click().catch(async () => {
        await page.getByRole('button', { name: /Confirmar /i }).click();
      });
      await page.waitForTimeout(800);
    }
  }

  async function pickSearchable(labelRe, query) {
    const field = page.locator('div, label').filter({ hasText: labelRe }).first();
    await field.getByRole('button').first().click();
    const box = page.locator('[role="listbox"] input').last();
    await box.fill(query);
    await page.waitForTimeout(250);
    const opt = page.locator('[role="listbox"] [role="option"]').first();
    await opt.click();
  }

  async function loginAndEmpresa() {
    await page.goto('http://localhost:5174/login');
    await page.getByLabel('Email').fill('admin@almahue.local');
    await page.getByLabel('Contraseña').fill('Admin123!');
    await page.getByRole('button', { name: /Iniciar sesión/i }).click();
    await page.waitForURL((u) => !String(u).includes('/login'), { timeout: 30000 });
    await dismissPeriodo();
    const empBtn = page.getByRole('button').filter({ hasText: /empresa|EXPORT|SERVICES|Almahue/i }).first();
    await empBtn.click();
    await page.getByRole('button', { name: /EXPORT|77\.032\.638/i }).click();
    await dismissPeriodo();
  }

  async function emitFactura(idx, destQuery) {
    await page.goto('http://localhost:5174/comercial/ordenes-venta/nueva');
    await page.waitForTimeout(600);
    await page.getByLabel(/Indicador de venta/i).selectOption('EXPORTACION');
    await page.waitForTimeout(300);
    await pickSearchable(/Cliente/i, 'Pacific');
    await page.getByRole('button', { name: 'Siguiente' }).click();
    await pickSearchable(/Artículo|Artículo \/ servicio/i, 'Cereza');
    const cant = page.locator('input[type="number"]').first();
    await cant.fill('1');
    const precio = page.getByRole('spinbutton').nth(1);
    if (await precio.count()) {
      await precio.fill('20.25');
    } else {
      const inputs = page.locator('table input');
      await inputs.nth(1).fill('20.25').catch(() => {});
    }
    await page.getByRole('button', { name: 'Siguiente' }).click();
    await page.getByRole('button', { name: /Rellenar valores habituales/i }).click();
    await pickSearchable(/Puerto desembarque/i, destQuery);
    await page.getByRole('button', { name: /^Guardar$/ }).click();
    await page.waitForURL(/ordenes-venta/, { timeout: 60000 });
    await page.goto('http://localhost:5174/comercial/emitir');
    await page.waitForTimeout(800);
    await page.getByPlaceholder(/Buscar OV/i).fill('Pacific');
    await page.waitForTimeout(400);
    await page.getByRole('button', { name: 'Facturar' }).first().click();
    await page.waitForTimeout(800);
    const next = page.getByRole('button', { name: 'Siguiente' });
    if (await next.isEnabled()) await next.click();
    if (await next.isEnabled()) await next.click();
    await page.getByRole('button', { name: 'Emitir documento' }).click();
    await page.waitForURL(/libro/, { timeout: 180000 });
    const toast = await page.locator('[data-sonner-toast], li[data-sonner-toast]').first().textContent().catch(() => '');
    const url = page.url();
    facturas.push({ idx, destQuery, url, toast });
    log.push(`FAC ${idx} ${url} ${toast}`);
  }

  async function cierre(folioHint, tipo) {
    await page.goto('http://localhost:5174/comercial/libro');
    await page.waitForTimeout(800);
    if (folioHint) {
      const search = page.getByPlaceholder(/Buscar|Filtrar/i).first();
      if (await search.count()) await search.fill(folioHint);
    }
    await page.getByRole('button', { name: 'Cierre COMEX' }).first().click();
    await page.getByRole('button', { name: 'Continuar' }).click();
    await page.getByText(tipo === 'ND' ? 'ND (111)' : 'NC (112)').click();
    if (tipo === 'NC') {
      const qty = page.locator('dialog input[type="number"], [role="dialog"] input[type="number"]').first();
      if (await qty.count()) {
        await qty.fill('0.4');
      }
    } else {
      const price = page.locator('[role="dialog"] input[type="number"]').nth(1);
      if (await price.count()) {
        const v = Number(await price.inputValue()) || 20.25;
        await price.fill(String(v + 1));
      }
    }
    await page.getByRole('button', { name: /Emitir N/i }).click();
    await page.getByRole('button', { name: /Sí, emitir/i }).click();
    await page.waitForTimeout(2500);
    await page.waitForURL(/libro/, { timeout: 180000 });
    log.push(`CIERRE ${tipo} ${page.url()}`);
  }

  async function anular() {
    await page.goto('http://localhost:5174/comercial/libro');
    await page.waitForTimeout(800);
    await page.getByRole('button', { name: 'Anulación' }).first().click();
    await page.getByRole('button', { name: 'Continuar' }).click();
    await page.getByRole('button', { name: /Confirmar y emitir NC/i }).click();
    await page.waitForTimeout(2500);
    await page.waitForURL(/libro/, { timeout: 180000 });
    log.push(`ANULA ${page.url()}`);
  }

  try {
    await loginAndEmpresa();
    const dests = ['FILADELFIA', 'FILADELFIA', '180', '180', 'VALPARAISO', 'VALPARAISO'];
    for (let i = 0; i < 6; i++) {
      await emitFactura(i + 1, dests[i]);
    }
    await cierre(undefined, 'NC');
    await cierre(undefined, 'NC');
    await cierre(undefined, 'ND');
    await cierre(undefined, 'ND');
    await anular();
    await anular();
    return { ok: true, facturas, log };
  } catch (e) {
    return { ok: false, error: String(e), facturas, log, url: page.url() };
  }
};
