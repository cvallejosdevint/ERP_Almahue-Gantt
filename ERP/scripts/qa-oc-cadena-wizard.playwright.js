async (page) => {
  page.setDefaultTimeout(25000);
  const FRONT = 'http://localhost:5174';
  const API = 'http://localhost:3001/api/v1';
  const PISO = 500000;
  const results = [];
  const log = [];

  const toastText = async () => {
    const t = page.locator('[data-sonner-toast]').first();
    if (await t.isVisible({ timeout: 4000 }).catch(() => false)) {
      return ((await t.innerText()) || '').replace(/\s+/g, ' ').trim();
    }
    return '';
  };

  const dismissPeriodo = async () => {
    const later = page.getByRole('button', { name: /Más tarde/i });
    if (await later.isVisible({ timeout: 2500 }).catch(() => false)) {
      await later.click();
      await page.waitForTimeout(400);
      return;
    }
    const conf = page.getByRole('button', { name: /Confirmar 2026-09/i });
    if (await conf.isVisible({ timeout: 1500 }).catch(() => false)) {
      await conf.click();
      await page.waitForTimeout(400);
    }
  };

  const login = async (email, password) => {
    await page.evaluate(() => { localStorage.clear(); sessionStorage.clear(); });
    await page.goto(FRONT + '/login');
    await page.locator('input[type="email"]').waitFor({ state: 'visible', timeout: 20000 });
    await page.locator('input[type="email"]').fill(email);
    await page.locator('input[type="password"]').fill(password);
    await page.getByRole('button', { name: /Entrar con clave/i }).click();
    await page.waitForURL((u) => !String(u).includes('/login'), { timeout: 30000 });
    await dismissPeriodo();
    const emp = page.getByRole('button').filter({ hasText: /EXPORT|SERVICES|Almahue|empresa/i }).first();
    if (await emp.isVisible({ timeout: 3000 }).catch(() => false)) {
      const txt = (await emp.innerText()) || '';
      if (!/EXPORT/i.test(txt)) {
        await emp.click();
        const opt = page.getByRole('button', { name: /EXPORT|77\.032\.638/i }).first();
        if (await opt.isVisible({ timeout: 3000 }).catch(() => false)) await opt.click();
        await dismissPeriodo();
      }
    }
  };

  const expandTotales = async () => {
    const enviar = page.getByRole('button', { name: /Enviar a aprobación|Guardar borrador/ });
    if (await enviar.first().isVisible({ timeout: 1500 }).catch(() => false)) return;
    const exp = page.getByTitle('Expandir panel');
    if (await exp.isVisible({ timeout: 1500 }).catch(() => false)) await exp.click();
  };

  const fillOc = async ({ neto, moneda = 'CLP', descripcion }) => {
    await page.goto(FRONT + '/compras/ordenes/nueva');
    await page.waitForTimeout(700);
    await expandTotales();
    await page.getByRole('button', { name: /Buscar proveedor/i }).click();
    const box = page.locator('[role="listbox"] input').last();
    if (await box.isVisible({ timeout: 2000 }).catch(() => false)) await box.fill('a');
    await page.waitForTimeout(350);
    const opt = page.locator('[role="listbox"] [role="option"]').first();
    if (!(await opt.isVisible({ timeout: 4000 }).catch(() => false))) {
      throw new Error('Sin proveedores en el combo');
    }
    await opt.click();
    const monedaSel = page.locator('select').filter({ has: page.locator('option[value="CLP"]') }).first();
    if (await monedaSel.count()) await monedaSel.selectOption(moneda).catch(() => {});
    await page.getByRole('button', { name: /2\. Ítems/i }).click();
    await page.waitForTimeout(400);
    const row = page.locator('.rounded.border').filter({ hasText: 'Descripción' }).first();
    await row.getByRole('textbox').first().fill(descripcion);
    const cc = row.locator('select').nth(0);
    const cta = row.locator('select').nth(1);
    const ccVal = await cc.locator('option').nth(1).getAttribute('value');
    const ctaVal = await cta.locator('option').nth(1).getAttribute('value');
    if (ccVal) await cc.selectOption(ccVal);
    if (ctaVal) await cta.selectOption(ctaVal);
    await row.locator('input[type="number"]').fill('1');
    const precioBox = row.getByRole('textbox').nth(1);
    await precioBox.click();
    await precioBox.fill(String(neto));
    await page.waitForTimeout(900);
  };

  const cadenaPanel = async () => {
    const box = page.locator('h3', { hasText: 'Cadena de aprobación' }).locator('xpath=..');
    return ((await box.innerText().catch(() => '')) || '').replace(/\s+/g, ' ').trim();
  };

  const runCase = async (id, { neto, moneda, modo, esperado }) => {
    const rec = { id, neto, moneda, modo, esperado, resultado: 'BLOCKED', toast: '', cadena: '', url: '', nota: '' };
    try {
      await fillOc({
        neto,
        moneda,
        descripcion: id + ' neto ' + neto + ' ' + moneda,
      });
      rec.cadena = await cadenaPanel();
      rec.url = page.url();
      const enviar = page.getByRole('button', { name: 'Enviar a aprobación' });
      const borrador = page.getByRole('button', { name: 'Guardar borrador' }).last();
      rec.enviarDisabled = await enviar.isDisabled().catch(() => null);
      if (modo === 'borrador') {
        await borrador.click();
        rec.toast = await toastText();
        rec.url = page.url();
        rec.resultado = /Borrador guardado/i.test(rec.toast) || /ordenes/i.test(rec.url)
          ? 'PASS'
          : 'FAIL';
        rec.nota = 'Guardar borrador no debe pedir cadena';
      } else {
        const before = page.url();
        if (rec.enviarDisabled) {
          rec.toast = rec.cadena;
          rec.resultado = esperado === 'bloquea' ? 'PASS' : 'FAIL';
          rec.nota = 'Botón Enviar deshabilitado';
        } else {
          await enviar.click();
          rec.toast = await toastText();
          await page.waitForTimeout(800);
          rec.url = page.url();
          const moved = rec.url !== before && /ordenes/i.test(rec.url) && !/nueva/i.test(rec.url);
          const waitToast = /Espere a que se calcule/i.test(rec.toast);
          const sent = /enviada a aprobación|APROBADO|aprobada/i.test(rec.toast) || moved;
          if (esperado === 'bloquea') rec.resultado = waitToast || !sent ? 'PASS' : 'FAIL';
          else if (esperado === 'auto_aprobado' || esperado === 'pendiente') rec.resultado = sent ? 'PASS' : (waitToast ? 'FAIL' : 'FAIL');
          else rec.resultado = sent ? 'PASS' : 'FAIL';
          rec.nota = waitToast
            ? 'Toast de espera con preview distinto de ok (sintoma Jose)'
            : sent
              ? 'El wizard persistió la OC'
              : 'No se persistió';
        }
      }
    } catch (e) {
      rec.resultado = 'BLOCKED';
      rec.nota = String(e && e.message ? e.message : e);
    }
    results.push(rec);
    log.push(id + ' ' + rec.resultado + ' ' + rec.toast);
  };

  const sessionAuth = async () => page.evaluate(() => {
    const raw = localStorage.getItem('erp.session') || localStorage.getItem('almahue.session') || '';
    try {
      const s = JSON.parse(raw);
      return { token: s.accessToken || s.token || s.access_token || '', empresaId: s.empresaId || s.user?.empresaId || '' };
    } catch {
      return { token: '', empresaId: '' };
    }
  });

  const apiJson = async (method, path, body) => {
    const auth = await sessionAuth();
    return page.evaluate(async ({ method, url, token, empresaId, body }) => {
      const headers = { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' };
      if (empresaId) headers['x-empresa-id'] = empresaId;
      const res = await fetch(url, { method, headers, body: body ? JSON.stringify(body) : undefined });
      const text = await res.text();
      let data = text;
      try { data = JSON.parse(text); } catch {}
      return { status: res.status, data };
    }, { method, url: API + path, token: auth.token, empresaId: auth.empresaId, body });
  };

  let pisoNodo = null;
  try {
    await login('admin@almahue.local', 'Admin123!');
    const escalas = await apiJson('GET', '/escalas-aprobacion');
    const list = Array.isArray(escalas.data) ? escalas.data : (escalas.data?.items || []);
    const compras = list.filter((n) => /compra/i.test(String(n.modulo || n.grupoModulo || n.tipo || '')) || n.grupoNombre);
    const nodo = list.find((n) => n.montoMax === PISO || n.montoMax === 500000)
      || list.find((n) => n.montoMax != null)
      || list[0];
    if (nodo) {
      pisoNodo = {
        id: nodo.id,
        montoMax: nodo.montoMax,
        grupoId: nodo.grupoId,
        escalaAUsuarioId: nodo.escalaAUsuarioId,
        escalaAId: nodo.escalaAId,
        logica: nodo.logica,
        snapshot: nodo,
      };
    }
    log.push('escalas ' + list.length + ' nodoPiso=' + (pisoNodo ? pisoNodo.id + ':' + pisoNodo.montoMax : 'ninguno'));
  } catch (e) {
    log.push('admin escalas BLOCKED ' + e.message);
  }

  await login('erojas@almahuexport.cl', 'demo123');

  await runCase('T1-CLP-bajo', { neto: 100000, moneda: 'CLP', modo: 'enviar', esperado: 'auto_aprobado' });
  await runCase('T1-CLP-igual', { neto: 500000, moneda: 'CLP', modo: 'enviar', esperado: 'pendiente' });
  await runCase('T1-CLP-alto', { neto: 2500000, moneda: 'CLP', modo: 'enviar', esperado: 'pendiente' });

  await runCase('T2-BOR-bajo', { neto: 50000, moneda: 'CLP', modo: 'borrador', esperado: 'borrador' });
  await runCase('T2-BOR-igual', { neto: 500000, moneda: 'CLP', modo: 'borrador', esperado: 'borrador' });
  await runCase('T2-BOR-alto', { neto: 9000000, moneda: 'CLP', modo: 'borrador', esperado: 'borrador' });

  await runCase('T3-USD-bajo', { neto: 50, moneda: 'USD', modo: 'enviar', esperado: 'auto_aprobado' });
  await runCase('T3-USD-medio', { neto: 520, moneda: 'USD', modo: 'enviar', esperado: 'pendiente' });
  await runCase('T3-USD-alto', { neto: 4000, moneda: 'USD', modo: 'enviar', esperado: 'pendiente' });

  if (pisoNodo && pisoNodo.id) {
    await login('admin@almahue.local', 'Admin123!');
    const bodyNull = { ...pisoNodo.snapshot, montoMax: null };
    const cleared = await apiJson('PUT', '/escalas-aprobacion/' + pisoNodo.id, bodyNull);
    log.push('clear piso HTTP ' + cleared.status);
    await login('erojas@almahuexport.cl', 'demo123');
    await runCase('T4-SINMONTO-bajo', { neto: 100000, moneda: 'CLP', modo: 'enviar', esperado: 'pendiente' });
    await runCase('T4-SINMONTO-igual', { neto: 500000, moneda: 'CLP', modo: 'enviar', esperado: 'pendiente' });
    await runCase('T4-SINMONTO-alto', { neto: 2500000, moneda: 'CLP', modo: 'enviar', esperado: 'pendiente' });
    await login('admin@almahue.local', 'Admin123!');
    const restored = await apiJson('PUT', '/escalas-aprobacion/' + pisoNodo.id, { ...pisoNodo.snapshot, montoMax: pisoNodo.montoMax ?? PISO });
    log.push('restore piso HTTP ' + restored.status);
  } else {
    ['T4-SINMONTO-bajo', 'T4-SINMONTO-igual', 'T4-SINMONTO-alto'].forEach((id) => {
      results.push({ id, resultado: 'BLOCKED', nota: 'No se encontró el nodo de 500.000 para vaciar el monto' });
    });
  }

  const pass = results.filter((r) => r.resultado === 'PASS').length;
  const fail = results.filter((r) => r.resultado === 'FAIL').length;
  const blocked = results.filter((r) => r.resultado === 'BLOCKED').length;
  return { dump: 'ERP/backups/almahue-erp-20261008-105736.dump', pisoNodo, pass, fail, blocked, results, log };
}
