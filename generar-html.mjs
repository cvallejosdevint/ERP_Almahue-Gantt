import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { stepsFor, granSteps } from './pasos-recorrido.mjs';

const dir = path.dirname(fileURLToPath(import.meta.url));
const plantilla = fs.readFileSync(
  path.resolve(dir, '../../../.cursor/skills/almahue-antes-despues/plantilla-recorrido.html'),
  'utf8',
);

const hojas = [
  { slug: 'panel', grupo: 'Inicio', label: 'Panel operativo', ruta: '/', img: 'despues-panel.png', cls: 'param' },
  { slug: 'admin-empresas', grupo: 'Administración', label: 'Empresas', ruta: '/admin/empresas', img: 'despues-admin-empresas.png', cls: 'param' },
  { slug: 'admin-plantilla', grupo: 'Administración', label: 'Plantilla documentos', ruta: '/admin/plantilla-documentos', img: 'despues-admin-plantilla.png', cls: 'param' },
  { slug: 'admin-usuarios', grupo: 'Administración', label: 'Usuarios', ruta: '/admin/usuarios', img: 'despues-admin-usuarios.png', cls: 'param' },
  { slug: 'admin-roles', grupo: 'Administración', label: 'Roles y permisos', ruta: '/admin/roles', img: 'despues-admin-roles.png', cls: 'param' },
  { slug: 'admin-aprobaciones', grupo: 'Administración', label: 'Reglas de aprobación', ruta: '/admin/aprobaciones', img: 'despues-admin-aprobaciones.png', cls: 'param' },
  { slug: 'admin-correos', grupo: 'Administración', label: 'Configuración de correos', ruta: '/admin/configuracion-correos', img: 'despues-admin-correos.png', cls: 'param' },
  { slug: 'param-monedas', grupo: 'Parametrización', label: 'Monedas', ruta: '/catalogos/monedas', img: 'despues-param-monedas.png', cls: 'param' },
  { slug: 'param-unidades', grupo: 'Parametrización', label: 'Unidades de medida', ruta: '/catalogos/unidades', img: 'despues-param-unidades.png', cls: 'param' },
  { slug: 'param-cc', grupo: 'Parametrización', label: 'Centros de costo', ruta: '/catalogos/centros-costo', img: 'despues-param-cc.png', cls: 'param' },
  { slug: 'param-elementos', grupo: 'Parametrización', label: 'Elementos de costo', ruta: '/catalogos/elementos-costo', img: 'despues-param-elementos.png', cls: 'param' },
  { slug: 'param-areas', grupo: 'Parametrización', label: 'Áreas de negocio', ruta: '/catalogos/areas-negocio', img: 'despues-param-areas.png', cls: 'param' },
  { slug: 'param-conceptos', grupo: 'Parametrización', label: 'Conceptos', ruta: '/catalogos/conceptos-flujo', img: 'despues-param-conceptos.png', cls: 'param' },
  { slug: 'param-codigos', grupo: 'Parametrización', label: 'Códigos financieros', ruta: '/catalogos/codigos-financieros', img: 'despues-param-codigos.png', cls: 'param' },
  { slug: 'param-tipos-doc', grupo: 'Parametrización', label: 'Tipos de documento', ruta: '/catalogos/tipos-documento', img: 'despues-param-tipos-doc.png', cls: 'param' },
  { slug: 'param-plan-cuentas', grupo: 'Parametrización', label: 'Plan de cuentas', ruta: '/catalogos/plan-cuentas', img: 'despues-param-plan-cuentas.png', cls: 'param' },
  { slug: 'param-indicadores', grupo: 'Parametrización', label: 'Indicadores BC', ruta: '/catalogos/indicadores-bc', img: 'despues-param-indicadores.png', cls: 'param' },
  { slug: 'param-proveedores', grupo: 'Parametrización', label: 'Proveedores', ruta: '/catalogos/proveedores', img: 'despues-param-proveedores.png', cls: 'param' },
  { slug: 'param-contratista', grupo: 'Parametrización', label: 'Contratista', ruta: '/catalogos/contratista', img: 'despues-param-contratista.png', cls: 'param' },
  { slug: 'param-af', grupo: 'Parametrización', label: 'Activo fijo', ruta: '/catalogos/activo-fijo', img: 'despues-param-af.png', cls: 'param' },
  { slug: 'ctr-listado', grupo: 'Contratistas', label: 'Listado', ruta: '/contratistas', img: 'despues-ctr-listado.png', cls: 'compras' },
  { slug: 'ctr-ingreso', grupo: 'Contratistas', label: 'Ingreso diario', ruta: '/contratistas/ingreso-diario', img: 'despues-ctr-ingreso.png', cls: 'compras' },
  { slug: 'ctr-proformas', grupo: 'Contratistas', label: 'Proformas y facturas', ruta: '/contratistas/proformas', img: 'despues-ctr-proformas.png', cls: 'compras' },
  { slug: 'ctr-aprobaciones', grupo: 'Contratistas', label: 'Aprobaciones', ruta: '/contratistas/aprobaciones', img: 'despues-ctr-aprobaciones.png', cls: 'compras' },
  { slug: 'ctr-auditoria', grupo: 'Contratistas', label: 'Auditoría', ruta: '/contratistas/auditoria', img: 'despues-ctr-auditoria.png', cls: 'compras' },
  { slug: 'ctr-traspaso', grupo: 'Contratistas', label: 'Traspaso contable y cierre de mes', ruta: '/contratistas/traspaso', img: 'despues-ctr-traspaso.png', cls: 'conta' },
  { slug: 'ctr-rep-ingresos', grupo: 'Contratistas', label: 'Reporte ingresos', ruta: '/contratistas/reporte-ingresos', img: 'despues-ctr-rep-ingresos.png', cls: 'compras' },
  { slug: 'ctr-rep-cc', grupo: 'Contratistas', label: 'Labores por centro de costo', ruta: '/contratistas/reporte-ccosto-labor', img: 'despues-ctr-rep-cc.png', cls: 'compras' },
  { slug: 'ctr-rep-prod', grupo: 'Contratistas', label: 'Control de producción', ruta: '/contratistas/reporte-produccion', img: 'despues-ctr-rep-prod.png', cls: 'compras' },
  { slug: 'ventas-ov', grupo: 'Ventas', label: 'Órdenes de venta', ruta: '/comercial/ordenes-venta', img: 'despues-ventas-ov.png', cls: 'ventas' },
  { slug: 'ventas-emitir', grupo: 'Ventas', label: 'Emitir DTE', ruta: '/comercial/emitir', img: 'despues-ventas-emitir.png', cls: 'ventas' },
  { slug: 'ventas-libro', grupo: 'Ventas', label: 'Libro de ventas', ruta: '/comercial/libro', img: 'despues-ventas-libro.png', cls: 'ventas' },
  { slug: 'ventas-clientes', grupo: 'Ventas', label: 'Clientes', ruta: '/comercial/clientes', img: 'despues-ventas-clientes.png', cls: 'ventas' },
  { slug: 'ventas-rep-sii', grupo: 'Ventas', label: 'Libro de ventas SII', ruta: '/comercial/reporte-libro-sii', img: 'despues-ventas-rep-sii.png', cls: 'ventas' },
  { slug: 'ventas-rep-cliente', grupo: 'Ventas', label: 'Ventas por cliente y producto', ruta: '/comercial/reporte-cliente-producto', img: 'despues-ventas-rep-cliente.png', cls: 'ventas' },
  { slug: 'compras-ordenes', grupo: 'Compras', label: 'Órdenes de compra', ruta: '/compras/ordenes', img: 'despues-compras-ordenes.png', cls: 'compras' },
  { slug: 'compras-aprobaciones', grupo: 'Compras', label: 'Aprobaciones', ruta: '/compras/aprobaciones', img: 'despues-compras-aprobaciones.png', cls: 'compras' },
  { slug: 'compras-libro', grupo: 'Compras', label: 'Libro de compras', ruta: '/compras/registro', img: 'despues-compras-libro.png', cls: 'compras' },
  { slug: 'compras-rep-pend', grupo: 'Compras', label: 'OC pendientes de recepción', ruta: '/compras/reporte-oc-pendientes', img: 'despues-compras-rep-pend.png', cls: 'compras' },
  { slug: 'compras-rep-depto', grupo: 'Compras', label: 'OC por depto y usuario', ruta: '/compras/reporte-oc-depto', img: 'despues-compras-rep-depto.png', cls: 'compras' },
  { slug: 'insumos-maestro', grupo: 'Insumos / Bodega', label: 'Maestro artículos', ruta: '/insumos/maestro', img: 'despues-insumos-maestro.png', cls: 'compras' },
  { slug: 'insumos-bodegas', grupo: 'Insumos / Bodega', label: 'Bodegas', ruta: '/insumos/bodegas', img: 'despues-insumos-bodegas.png', cls: 'compras' },
  { slug: 'insumos-stock', grupo: 'Insumos / Bodega', label: 'Stock por bodega / producto', ruta: '/insumos/stock', img: 'despues-insumos-stock.png', cls: 'compras' },
  { slug: 'insumos-movimientos', grupo: 'Insumos / Bodega', label: 'Movimientos / NC', ruta: '/insumos/movimientos', img: 'despues-insumos-movimientos.png', cls: 'compras' },
  { slug: 'insumos-cierre', grupo: 'Insumos / Bodega', label: 'Cierre de bodega', ruta: '/insumos/cierre', img: 'despues-insumos-cierre.png', cls: 'compras' },
  { slug: 'insumos-ordenes', grupo: 'Insumos / Bodega', label: 'Órdenes de insumos', ruta: '/insumos/ordenes', img: 'despues-insumos-ordenes.png', cls: 'compras' },
  { slug: 'insumos-aprobaciones', grupo: 'Insumos / Bodega', label: 'Aprobaciones', ruta: '/insumos/aprobaciones', img: 'despues-insumos-aprobaciones.png', cls: 'compras' },
  { slug: 'insumos-guias', grupo: 'Insumos / Bodega', label: 'Libro de guías', ruta: '/insumos/guias-recibidas', img: 'despues-insumos-guias.png', cls: 'compras' },
  { slug: 'af-maestro', grupo: 'Activo fijo', label: 'Maestro', ruta: '/activo-fijo/maestro', img: 'despues-af-maestro.png', cls: 'conta' },
  { slug: 'af-traspaso', grupo: 'Activo fijo', label: 'Traspaso contable', ruta: '/activo-fijo/traspaso', img: 'despues-af-traspaso.png', cls: 'conta' },
  { slug: 'af-reportes', grupo: 'Activo fijo', label: 'Reportes', ruta: '/activo-fijo/reportes', img: 'despues-af-reportes.png', cls: 'conta' },
  { slug: 'conta-periodos', grupo: 'Contabilidad', label: 'Períodos contables', ruta: '/contabilidad/periodos', img: 'despues-conta-periodos.png', cls: 'conta' },
  { slug: 'conta-asientos', grupo: 'Contabilidad', label: 'Comprobantes / asientos', ruta: '/contabilidad/asientos', img: 'despues-conta-asientos.png', cls: 'conta' },
  { slug: 'conta-honorarios', grupo: 'Contabilidad', label: 'Factores honorarios', ruta: '/contabilidad/honorarios', img: 'despues-conta-honorarios.png', cls: 'conta' },
  { slug: 'conta-presupuestos', grupo: 'Contabilidad', label: 'Presupuestos', ruta: '/presupuestos', img: 'despues-conta-presupuestos.png', cls: 'conta' },
  { slug: 'conta-diario', grupo: 'Contabilidad', label: 'Libro diario', ruta: '/contabilidad/libro-diario', img: 'despues-conta-diario.png', cls: 'conta' },
  { slug: 'conta-mayor', grupo: 'Contabilidad', label: 'Libro mayor', ruta: '/contabilidad/mayor', img: 'despues-conta-mayor.png', cls: 'conta' },
  { slug: 'conta-balance', grupo: 'Contabilidad', label: 'Balance de 8 columnas', ruta: '/contabilidad/balance-8-columnas', img: 'despues-conta-balance.png', cls: 'conta' },
  { slug: 'conta-er', grupo: 'Contabilidad', label: 'Estado de resultados', ruta: '/contabilidad/estado-resultados', img: 'despues-conta-er.png', cls: 'conta' },
  { slug: 'conta-situacion', grupo: 'Contabilidad', label: 'Situación financiera', ruta: '/contabilidad/situacion-financiera', img: 'despues-conta-situacion.png', cls: 'conta' },
  { slug: 'teso-cartolas', grupo: 'Tesorería', label: 'Cartolas', ruta: '/tesoreria/cartolas', img: 'despues-teso-cartolas.png', cls: 'teso' },
  { slug: 'teso-conciliacion', grupo: 'Tesorería', label: 'Conciliación', ruta: '/tesoreria/conciliacion', img: 'despues-teso-conciliacion.png', cls: 'teso' },
  { slug: 'teso-flujo', grupo: 'Tesorería', label: 'Flujo de caja', ruta: '/tesoreria/flujo-caja', img: 'despues-teso-flujo.png', cls: 'teso' },
  { slug: 'teso-pagos', grupo: 'Tesorería', label: 'Pagos', ruta: '/tesoreria/pagos', img: 'despues-teso-pagos.png', cls: 'teso' },
  { slug: 'teso-nominas', grupo: 'Tesorería', label: 'Nómina semanal', ruta: '/tesoreria/nominas', img: 'despues-teso-nominas.png', cls: 'teso' },
  { slug: 'teso-cc', grupo: 'Tesorería', label: 'Estado de cuenta', ruta: '/tesoreria/cuentas-corrientes', img: 'despues-teso-cc.png', cls: 'teso' },
];

function writeRecorrido(h) {
  const steps = stepsFor(h);
  const html = plantilla
    .replace('<title>Recorrido</title>', `<title>${h.grupo} · ${h.label}</title>`)
    .replace('<h1>De dónde sale el dato.</h1>', `<h1><a href="index.html" style="color:inherit;text-decoration:none">Manual cliente</a> · De dónde sale el dato.</h1>`)
    .replace(/const steps = \[[\s\S]*?\];/, `const steps = ${JSON.stringify(steps, null, 6)};`);
  fs.writeFileSync(path.join(dir, `recorrido-${h.slug}.html`), html, 'utf8');
}

hojas.forEach(writeRecorrido);

{
  const html = plantilla
    .replace('<title>Recorrido</title>', '<title>Gran recorrido · muestra ALM Export</title>')
    .replace('<h1>De dónde sale el dato.</h1>', '<h1><a href="index.html" style="color:inherit;text-decoration:none">Manual cliente</a> · Gran recorrido.</h1>')
    .replace(/const steps = \[[\s\S]*?\];/, `const steps = ${JSON.stringify(granSteps, null, 6)};`);
  fs.writeFileSync(path.join(dir, 'recorrido.html'), html, 'utf8');
}

const grupos = [];
for (const h of hojas) {
  if (!grupos.includes(h.grupo)) grupos.push(h.grupo);
}

const index = `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <title>Manual cliente Almahue ERP</title>
  <style>
    :root { --bg: #f4f1ea; --ink: #1c1917; --muted: #57534e; --line: #e7e5e4; --card: #fff; --side: #1c1917; }
    * { box-sizing: border-box; }
    body { margin: 0; font: 15px/1.35 "Segoe UI", sans-serif; background: var(--bg); color: var(--ink); display: grid; grid-template-columns: 280px 1fr; min-height: 100vh; }
    aside { background: var(--side); color: #f5f5f4; padding: 16px 12px; overflow: auto; }
    aside h1 { font-size: 1rem; margin: 0 8px 12px; }
    aside p { margin: 0 8px 16px; color: #a8a29e; font-size: 13px; }
    .g { margin: 0 0 10px; }
    .g strong { display: block; font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: #a8a29e; padding: 8px; }
    .g a { display: block; color: #fafaf9; text-decoration: none; padding: 6px 8px; border-radius: 8px; }
    .g a:hover { background: #292524; }
    .g a.dest { background: #292524; color: #fde68a; }
    main { padding: 24px 32px; }
    main h2 { margin: 0 0 8px; }
    .nota { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 12px 16px; }
  </style>
</head>
<body>
  <aside>
    <h1>Almahue ERP</h1>
    <p>Manual y speech 21/10/2026. Empresa Export. Datos nuevos. DTE ALM 61-65, cierre bodega 20260007.</p>
    <div class="g"><strong>Presentacion</strong><a class="dest" href="recorrido.html">Gran recorrido (26 pasos)</a></div>
    ${grupos.map((g) => `<div class="g"><strong>${g}</strong>${hojas.filter((h) => h.grupo === g).map((h) => `<a href="recorrido-${h.slug}.html">${h.label}</a>`).join('')}</div>`).join('')}
  </aside>
  <main>
    <h2>Como usarlo en la presentacion</h2>
    <div class="nota">
      <p><a href="recorrido.html">Gran recorrido</a>: 26 pasos con Siguiente. Cadena ya guardada: OC-2026-0001 a 0005, DTE ALM 61-65, DTE Export 93, PF-00001, cierre CTR 20260005, cierre bodega 20260007, pago folio 64. Pins sobre PNG 1536x960.</p>
      <p>Cada submodulo cuenta el proceso completo y termina con el comprobante en el listado mas el detalle de las lineas (cuentas, debe y haber). Menú vuelve al indice.</p>
      <p>Las fotos no pulsan Guardar, Emitir, Contabilizar ni Pagar: el speech usa lo que ya quedo en la muestra, incluido el cierre de bodega 2026-10. Bitacora: <a href="gaps.md">gaps.md</a>.</p>
    </div>
  </main>
</body>
</html>
`;
fs.writeFileSync(path.join(dir, 'index.html'), index, 'utf8');
console.log('hojas', hojas.length);
