async (page) => {
  const dir = 'E:/source/repos/Almahue/docs/sesiones/manual-cliente-2026-10-21';
  await page.setViewportSize({ width: 1536, height: 960 });

  const shot = async (name) => {
    await page.waitForTimeout(900);
    await page.screenshot({ path: `${dir}/${name}`, fullPage: false });
  };
  const pct = (box, vp) => ({
    x: +(((box.x + box.width / 2) / vp.width) * 100).toFixed(2),
    y: +(((box.y + box.height / 2) / vp.height) * 100).toFixed(2),
  });

  await page.goto('http://localhost:5174/contratistas/traspaso', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1800);
  await shot('despues-ctr-traspaso.png');

  await page.goto('http://localhost:5174/contabilidad/asientos', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1800);
  await shot('despues-conta-asientos.png');

  const vp = () => page.viewportSize();
  const pins = {};
  for (const n of ['20260005', '20260003', '20260001', '20260004']) {
    const cell = page.getByText(n, { exact: true }).first();
    const box = await cell.boundingBox();
    pins[`list${n}`] = box ? pct(box, vp()) : null;
  }

  const detalle = async (numero, file) => {
    const row = page.locator('tr').filter({ hasText: numero }).first();
    await row.getByRole('button', { name: 'Ver' }).click();
    await page.waitForTimeout(900);
    await shot(file);
    const cuenta = page.locator('[data-comprobante-cuenta]').first();
    const glosa = page.locator('[data-comprobante-glosa]').first();
    const cuentaBox = await cuenta.boundingBox();
    const glosaBox = await glosa.boundingBox();
    const out = {
      cuenta: cuentaBox ? pct(cuentaBox, vp()) : null,
      glosa: glosaBox ? pct(glosaBox, vp()) : null,
    };
    await page.getByRole('button', { name: 'Cerrar' }).last().click();
    await page.waitForTimeout(500);
    return out;
  };

  pins.detCtr = await detalle('20260005', 'despues-conta-asiento-detalle-ctr.png');
  pins.detCompra = await detalle('20260003', 'despues-conta-asiento-detalle-compra.png');
  pins.detVenta = await detalle('20260001', 'despues-conta-asiento-detalle-venta.png');
  pins.detRecepcion = await detalle('20260004', 'despues-conta-asiento-detalle-recepcion.png');
  return pins;
}
