/** Speech de cada hoja: prerrequisitos reales de la muestra y proceso ya guardado. */

const pin = (x, y, t, d) => ({ x, y, t, d });
const st = (mod, cls, title, img, pins) => ({
  mod,
  cls,
  title,
  img,
  alt: title,
  pins: Array.isArray(pins[0]) ? pins.map((p) => pin(...p)) : pins,
});

const emp = pin(30.07, 43.65, 'ALMAHUE EXPORT', 'Empresa activa de la muestra. Comprador. Periodo 2026-10 abierto.');
const almEmp = pin(30.07, 37.29, 'ALM SERVICES', 'Emisor sandbox RUT 77.032.639-7. Espejo proveedor/contratista en Export.');
const per = pin(21.73, 41.46, '2026-10', 'Periodo abierto. Sin esto no hay asiento, DTE contable ni cierre CTR.');
const prov = pin(36.68, 42.4, 'ALM SERVICES', 'Proveedor guardado en el maestro de Export. RUT 77.032.639-7.');
const oc = pin(21.91, 56.54, 'OC-2026-0001', 'Se armó la OC, se envió a aprobación, Felipe firmó con PIN 4821 y quedó RECEPCIONADA. Neto 100000.');
const ocFac = pin(77.98, 56.54, 'Factura 64', 'DTE ALM folio oficial 64, asociado a esta OC.');
const libro64 = pin(19.72, 103.64, 'Factura 64', 'Se sincronizó el inbox, se asoció a OC-2026-0001 y se contabilizó. Asiento 20260003. Queda bajo el corte de la foto.');
const libroOc = pin(35.96, 105.21, 'OC-2026-0001', 'OC de servicio de la muestra. Neto 100000.');
const libro65 = pin(19.72, 95.09, 'Factura 65', 'DTE 33 ALM > Export. Se aceptó en GoSocket, se asoció a OC-2026-0002 y se contabilizó. Asiento 20260006.');
const libroOc2 = pin(35.96, 96.66, 'OC-2026-0002', 'OC INSUMOS madre. Recibió la guía 52 folio 57 y la factura 65.');
const libro61 = pin(19.72, 67.2, 'Factura 61', 'Sandbox 33. Se armó OC-2026-0003 SERVICIO (neto 9500), se firmó con PIN 4821 y se asoció.');
const libroOc3 = pin(35.96, 68.78, 'OC-2026-0003', 'OC SERVICIO de regularización. Factura 61 ya no queda sin OC.');
const libro62 = pin(19.72, 76.46, 'Factura 62', 'Sandbox 33. OC-2026-0004 SERVICIO neto 20000, PIN 4821 y asociada.');
const libroOc4 = pin(35.96, 78.04, 'OC-2026-0004', 'OC SERVICIO de regularización de la factura 62.');
const libro63 = pin(19.72, 85.72, 'Factura 63', 'Sandbox 33. OC-2026-0005 SERVICIO neto 30000, PIN 4821 y asociada.');
const libroOc5 = pin(35.96, 87.3, 'OC-2026-0005', 'OC SERVICIO de regularización de la factura 63.');
const cierreBod = pin(84.22, 28.54, 'CERRADO', 'Bodega 2026-10 cerrada. Asiento 20260007. El periodo contable sigue ABIERTO.');
const cierreSal = pin(26.81, 98.13, 'Salida venta', '66250 al asiento de cierre. Las entradas 64 y 65 ya estaban en COMPRAS (20260003 y 20260006).');
const asiCtr = pin(20.79, 55.42, '20260005', 'Cierre CTR 2026-10. Tipo CIERRE, origen TRASPASO-CTR:2026-10. PF-00001 por 9600.');
const asiCompra = pin(20.79, 66.35, '20260003', 'Libro de compras. Tipo COMPRAS. Registro factura 64. 119000.');
const asiVenta = pin(20.79, 84.48, '20260001', 'Venta Export. Tipo VENTAS. Folio 93. 55335.');
const asiRec = pin(20.79, 93.33, '20260004', 'Recepción OC-2026-0001. Tipo COMPRAS. 100000.');
const asiCierreBod = pin(20.79, 44.48, '20260007', 'Cierre de bodega 2026-10. Tipo CIERRE, origen CIERRE-BODEGA:2026-10. 66250.');
const asi = asiCompra;
const detCtrCta = pin(13.55, 56.49, '6-1-01-01-002', 'MANO DE OBRA CONTRATISTA. Debe 9600. Packing cereza export / Seleccion y embalaje cereza.');
const detCtrGlo = pin(42.7, 56.49, 'PF-00001', 'Haber 2-1-08-02-003 FACT X RECIBIR CONTRATISTAS. Mismo 9600. Tipo CIERRE, no COMPRAS ni MANUAL.');
const detCompraCta = pin(13.71, 50.87, '6-1-01-01-001', 'MANO DE OBRA PROPIA 100000. Sigue IVA credito 19000 y haber PROVEEDORES 119000.');
const detCompraGlo = pin(44.43, 50.87, 'Factura 64', 'Lineas del DTE ALM ya contabilizado en el libro.');
const detVentaCta = pin(16.6, 56.49, '1-1-04-01-001', 'CLIENTES 55335. Haber ingreso venta 46500 e IVA debito 8835.');
const detVentaGlo = pin(48.45, 56.49, 'Muestra venta Export', 'Asiento al contabilizar el folio 93. Emitir no asienta.');
const detRecCta = pin(15.09, 50.87, '6-1-01-01-002', 'MANO DE OBRA CONTRATISTA 100000. Haber FACT X RECIBIR SERVICIOS 2-1-08-02-004.');
const detRecGlo = pin(42.05, 50.87, 'Recepción OC-2026-0001', 'Asiento de confirmar la recepción. Distinto del cierre CTR 20260005.');
const ctrCierre = pin(50.97, 32.5, '20260005', 'Se ejecutó Traspasar y cerrar sobre PF-00001. Mes cerrado. Asiento 20260005.');

const CONTA = {
  ctr: {
    list: asiCtr,
    listT: 'Listado: asiento 20260005 del cierre CTR',
    img: 'despues-conta-asiento-detalle-ctr.png',
    pins: [detCtrCta, detCtrGlo],
    detT: 'Detalle: cuentas de las lineas del cierre',
  },
  compra: {
    list: asiCompra,
    listT: 'Listado: asiento 20260003 compra 64',
    img: 'despues-conta-asiento-detalle-compra.png',
    pins: [detCompraCta, detCompraGlo],
    detT: 'Detalle: cuentas de la factura 64',
  },
  venta: {
    list: asiVenta,
    listT: 'Listado: asiento 20260001 venta 93',
    img: 'despues-conta-asiento-detalle-venta.png',
    pins: [detVentaCta, detVentaGlo],
    detT: 'Detalle: cuentas de la venta Export',
  },
  recepcion: {
    list: asiRec,
    listT: 'Listado: asiento 20260004 recepción OC',
    img: 'despues-conta-asiento-detalle-recepcion.png',
    pins: [detRecCta, detRecGlo],
    detT: 'Detalle: cuentas de la recepción OC',
  },
  bodega: {
    list: pin(20.79, 44.48, '20260007', 'Cierre de bodega 2026-10. Tipo CIERRE, origen CIERRE-BODEGA:2026-10. Salidas de venta 66250.'),
    listT: 'Listado: asiento 20260007 cierre de bodega',
    img: 'despues-conta-asiento-detalle-cierre-bodega.png',
    pins: [
      pin(14.93, 50.87, '6-2-02-01-003', 'AJUSTES DE INVENTARIO 66250. Debe de las SALIDA_VENTA del mes.'),
      pin(41.79, 50.87, 'Cierre bodega 2026-10', 'Haber EXISTENCIA INSUMOS 1-1-08-01-003 mismo 66250. Periodo contable sigue ABIERTO.'),
    ],
    detT: 'Detalle: cuentas del cierre de bodega',
  },
  insumos: {
    list: pin(20.79, 102.6, '20260006', 'Factura 65 de la OC INSUMOS 0002. Tipo COMPRAS. 11305. Queda bajo el corte de la foto del listado.'),
    listT: 'Listado: asiento 20260006 compra 65',
    img: 'despues-conta-asiento-detalle-insumos.png',
    pins: [
      pin(13.27, 50.87, '1-1-08-01-003', 'EXISTENCIA INSUMOS 9500. Sigue IVA credito 1805 y haber PROVEEDORES 11305.'),
      pin(42.7, 50.87, 'Factura 65', 'Asiento al contabilizar la OC madre. La guia 57 no asienta sola.'),
    ],
    detT: 'Detalle: cuentas de la factura 65',
  },
};

function contaItems(kind, n0) {
  const k = CONTA[kind];
  return [
    st('Recepción', 'conta', `${n0}. ${k.listT}`, 'despues-conta-asientos.png', [k.list]),
    st('Recepción', 'conta', `${n0 + 1}. ${k.detT}`, k.img, k.pins),
  ];
}

function kindFor(slug) {
  if (String(slug).startsWith('ctr-') || slug === 'param-contratista') return 'ctr';
  if (String(slug).startsWith('ventas-')) return 'venta';
  if (slug === 'compras-aprobaciones' || slug === 'compras-rep-pend') return 'recepcion';
  if (slug === 'insumos-guias' || slug === 'insumos-ordenes' || slug === 'insumos-movimientos') return 'insumos';
  if (slug === 'insumos-cierre' || slug === 'insumos-stock') return 'bodega';
  if (String(slug).startsWith('conta-')) return 'ctr';
  return 'compra';
}

function withContaItems(slug, steps) {
  const lastImg = steps[steps.length - 1]?.img || '';
  if (lastImg.includes('asiento-detalle')) return steps;
  const kind = kindFor(slug);
  const n = steps.length + 1;
  const k = CONTA[kind];
  if (lastImg === 'despues-conta-asientos.png') {
    return [
      ...steps,
      st('Recepción', 'conta', `${n}. ${k.detT}`, k.img, k.pins),
    ];
  }
  return [...steps, ...contaItems(kind, n)];
}
const afNom = pin(25.43, 55.81, 'Equipo packing', 'Se dio de alta el activo contra la factura 64. Neto 50000. Guardar en maestro AF.');
const af64 = pin(53.92, 55.81, 'Factura 64', 'Mismo folio del DTE ya contabilizado.');
const mov64 = pin(80.1, 50.4, 'Factura 64', 'Se guardó ENTRADA_PROVEEDOR con facturaRef 64. Arriba hay dos SALIDA VENTA (OV 10007260 y OV 1000).');
const mov65 = pin(80.1, 39.38, '65', 'ENTRADA_PROVEEDOR de la guía 57. facturaRef 65 al contabilizar la OC madre. 1 pallet x 9500.');
const ovCli = pin(35.32, 56.35, 'Pacific Fruit', 'OV 10007260. Se guardó, se validó stock y se facturó. Sin cadena OV (D4). La fila 1000 es otra OV facturada sin DTE: no es la muestra.');
const ov93 = pin(84.41, 56.35, 'FACTURA 93', 'Se convirtió la OV 10007260, se emitió al sandbox y se contabilizó. Folio oficial 93, asiento 20260001.');
const guia56 = pin(27.33, 56.35, '0000056', 'Guía tipo 52 folio 56 del inbox ALM, 17-10-2026. Estado Pendiente. Quedó fuera del camino bueno.');
const guia57 = pin(25.95, 59.87, '57', 'Guía tipo 52 folio SII 57 emitida desde ALM en el front. Recepcionada sobre OC-2026-0002.');
const guiaAlm = pin(32.22, 59.87, 'ALM SERVICES', 'Emisor de la guía 57 y de la factura 65. RUT 77.032.639-7.');
const guiaFac = pin(69.74, 59.87, '65', 'Factura 33 asociada a la misma OC. El asiento nace de esta factura, no de la guía.');
const guiaAsi = pin(75, 59.87, '20260006', 'Asiento COMPRAS de la factura 65. EXISTENCIA INSUMOS 9500 + IVA 1805 / PROVEEDORES 11305.');
const ocIns = pin(21.68, 60.7, 'OC-2026-0002', 'OC INSUMOS. Admin firmó con PIN 4821, se recepcionó la guía 57 y quedó CONTABILIZADA.');
const ocInsFac = pin(78.37, 60.7, 'Factura 65', 'Misma factura del libro de compras y del movimiento de bodega.');
const ocInsVacio = pin(31.9, 28.49, 'ÓRDENES 0', '2026-10 no tiene OC origen INSUMOS. La muestra es OC SERVICIO 0001 en Compras. Las guías no tienen madre.');
const afPer = pin(24.51, 25.42, '2026-10', 'Periodo de la sesión. El equipo packing inicia depreciación el 01-11-2026: octubre no arma asiento AF.');
const lv93 = pin(20.8, 65.63, '93', 'Libro de ventas: resultado de Emitir + Contabilizar. Cliente Pacific Fruit.');
const lvCli = pin(50.82, 65.63, 'Pacific Fruit', 'Mismo cliente de la OV guardada.');
const ing = pin(82.93, 58.94, 'PF-00001', 'Se guardó el ingreso diario (8 horas, 2026-10) y se asoció a la proforma.');
const pf = pin(20.87, 58.52, 'PF-00001', 'Se armó con los ingresos, se guardó y se pasó a DEFINITIVA.');
const pagoAlm = pin(33.65, 39.35, 'ALM SERVICES', 'Se registró el pago TEF calzado a folio 64. Estado PENDIENTE: no hay cartola.');
const pago64 = pin(78.87, 39.35, '64', 'Mismo folio del DTE ALM ya contabilizado.');
const ccAlm = pin(34.48, 47.29, 'ALM SERVICES', 'Saldo proveedor -238000: asientos 20260002 y 20260003 (ambos Registro compra 64) mas el pago PENDIENTE que no baja la deuda hasta cartola.');
const nom64 = pin(22.27, 79.87, '64', 'La nómina lee el compromiso del pago guardado.');
const nomAlm = pin(31.79, 79.87, 'ALM SERVICES', 'Mismo proveedor de la factura 64.');
const ctrAlm = pin(42.51, 39.38, 'ALM SERVICES', 'Contratista maestro, espejo del proveedor. Se usa en ingreso y proforma.');
const panelPf = pin(62.82, 87.77, 'PF-00001', 'El panel muestra la proforma ya guardada.');
const repPf = pin(55.13, 70.29, 'PF-00001', 'El reporte lee el ingreso y la proforma de la muestra.');
const deptoOc = pin(83.84, 55.6, 'OC-2026-0001', 'La reportería lee la OC guardada y la factura 64.');

function empPer(extra = []) {
  return [
    st('Pre requisitos', 'param', '1. Empresa Export y ALM', 'despues-admin-empresas.png', [almEmp, emp]),
    st('Pre requisitos', 'param', '2. Periodo 2026-10 abierto', 'despues-conta-periodos.png', [per]),
    ...extra,
  ];
}

const STEPS = {
  panel: [
    ...empPer(),
    st('Proceso de Inicio > Panel operativo', 'param', '3. Avisos de lo ya guardado', 'despues-panel.png', [panelPf]),
    st('En paralelo', 'compras', '4. OC y factura de la muestra', 'despues-compras-ordenes.png', [oc, ocFac]),
    st('Recepción', 'compras', '5. Proforma DEFINITIVA', 'despues-ctr-proformas.png', [pf]),
  ],

  'admin-empresas': [
    st('Pre requisitos', 'param', '1. Login holding', 'despues-admin-usuarios.png', [pin(28, 18, 'Usuarios', 'Operadores demo123 / PIN 4821. Admin admin@almahue.local. Se conservaron en el wipe transaccional.')]),
    st('Proceso de Administración > Empresas', 'param', '2. Export y ALM guardadas', 'despues-admin-empresas.png', [almEmp, emp]),
    st('En paralelo', 'param', '3. Periodo de cada una', 'despues-conta-periodos.png', [per]),
    st('Recepción', 'compras', '4. La OC usa Export', 'despues-compras-ordenes.png', [oc]),
  ],
  'admin-plantilla': [
    ...empPer(),
    st('Proceso de Administración > Plantilla documentos', 'param', '3. Logo y firma ya guardados', 'despues-admin-plantilla.png', [pin(28, 18, 'Plantilla', 'La plantilla de COMPRAS/VENTAS se usa al notificar OC o factura. Quedó cargada en el maestro.')]),
    st('En paralelo', 'param', '4. Correos', 'despues-admin-correos.png', [pin(28, 18, 'SMTP', 'H9 externo. El PIN de OC se avisó a Felipe con esta config.')]),
    st('Recepción', 'compras', '5. OC enviada', 'despues-compras-ordenes.png', [oc]),
  ],
  'admin-usuarios': [
    ...empPer(),
    st('Proceso de Administración > Usuarios', 'param', '3. Operadores de la muestra', 'despues-admin-usuarios.png', [pin(28, 18, 'Usuarios', 'Valentina, Elena, Felipe. Password demo123. PIN 4821. Se usaron para armar OC, OV y firmar.')]),
    st('En paralelo', 'param', '4. Roles', 'despues-admin-roles.png', [pin(28, 18, 'Roles', 'compras:write, comercial:write, contratistas:write. Admin ROL-1 con * arma cadena OC sin estar en la escala.')]),
    st('Recepción', 'compras', '5. Firma de OC', 'despues-compras-aprobaciones.png', [pin(28, 18, 'Bandeja', 'Felipe firmó OC-2026-0001. Ya no hay pendiente.')]),
  ],
  'admin-roles': [
    ...empPer(),
    st('Proceso de Administración > Roles y permisos', 'param', '3. Permisos que se usaron', 'despues-admin-roles.png', [pin(28, 18, 'Roles', 'Sin compras:write no se guarda OC. Sin contratistas:write no se guarda ingreso ni proforma.')]),
    st('En paralelo', 'param', '4. Usuarios', 'despues-admin-usuarios.png', [pin(28, 18, 'Usuarios', 'Los operadores de la muestra ya tienen el rol.')]),
    st('Recepción', 'compras', '5. Cadena OC', 'despues-admin-aprobaciones.png', [pin(28, 22, 'Escala', 'Solo Compras. D4: sin cadena OV ni PIN de proformas.')]),
  ],
  'admin-aprobaciones': [
    ...empPer(),
    st('Proceso de Administración > Reglas de aprobación', 'param', '3. Escala Compras guardada', 'despues-admin-aprobaciones.png', [pin(28, 22, 'Grupos y escalas', 'Se usó para enviar OC-2026-0001. Felipe PIN 4821. Admin no figura en la escala.')]),
    st('En paralelo', 'compras', '4. Bandeja OC', 'despues-compras-aprobaciones.png', [pin(28, 18, 'Bandeja', 'La OC ya salió: está RECEPCIONADA.')]),
    st('Recepción', 'compras', '5. OC-2026-0001', 'despues-compras-ordenes.png', [oc]),
  ],
  'admin-correos': [
    ...empPer(),
    st('Proceso de Administración > Configuración de correos', 'param', '3. Avisos de PIN y OC', 'despues-admin-correos.png', [pin(28, 18, 'Correos', 'Plantilla COMPRAS. El envío de OC y el PIN usan esto. SMTP H9 externo.')]),
    st('En paralelo', 'compras', '4. OC enviada', 'despues-compras-ordenes.png', [oc]),
    st('Recepción', 'param', '5. Plantilla', 'despues-admin-plantilla.png', [pin(28, 18, 'Plantilla', 'Logo y firma que viajan en el mail.')]),
  ],

  'param-monedas': empPer([
    st('Proceso de Parametrización > Monedas', 'param', '3. CLP de la muestra', 'despues-param-monedas.png', [pin(28, 18, 'CLP', 'OC, proforma, pago y DTE 64 van en CLP. Maestro conservado.')]),
    st('En paralelo', 'param', '4. Indicadores BC', 'despues-param-indicadores.png', [pin(28, 18, 'TC', 'Si hubiera USD, la escala OC convierte con el TC del día.')]),
    st('Recepción', 'compras', '5. OC en CLP', 'despues-compras-ordenes.png', [oc]),
  ]),
  'param-unidades': empPer([
    st('Proceso de Parametrización > Unidades de medida', 'param', '3. Unidades del maestro', 'despues-param-unidades.png', [pin(28, 18, 'Unidades', 'Las usa el ingreso CTR (jornada) y el insumo de la OV. Maestro conservado.')]),
    st('En paralelo', 'compras', '4. Ingreso diario', 'despues-ctr-ingreso.png', [ing]),
    st('Recepción', 'ventas', '5. OV de producto', 'despues-ventas-ov.png', [ovCli]),
  ]),
  'param-cc': empPer([
    st('Proceso de Parametrización > Centros de costo', 'param', '3. CC de la muestra', 'despues-param-cc.png', [pin(28, 18, 'Centros', 'El ingreso CTR y las lineas de OC/OV llevan CC si la cuenta lo pide. Maestro conservado.')]),
    st('En paralelo', 'compras', '4. Ingreso con CC', 'despues-ctr-ingreso.png', [ing]),
    st('Recepción', 'compras', '5. Reportería labores por CC', 'despues-ctr-rep-cc.png', [pin(28, 18, 'Labores por CC', 'Lee el ingreso guardado de 2026-10.')]),
  ]),
  'param-elementos': empPer([
    st('Proceso de Parametrización > Elementos de costo', 'param', '3. Elemento en linea OC', 'despues-param-elementos.png', [pin(28, 18, 'Elementos', 'Si la cuenta exige elemento, la linea de OC/recepción lo manda. Maestro conservado.')]),
    st('En paralelo', 'compras', '4. OC-2026-0001', 'despues-compras-ordenes.png', [oc]),
    st('Recepción', 'compras', '5. Recepción confirmada', 'despues-compras-libro.png', [libro64]),
  ]),
  'param-areas': empPer([
    st('Proceso de Parametrización > Áreas de negocio', 'param', '3. Área si la cuenta lo pide', 'despues-param-areas.png', [pin(28, 18, 'Áreas', 'Dimensión del asiento de ventas/compras. Maestro conservado.')]),
    st('En paralelo', 'conta', '4. Asientos de la muestra', 'despues-conta-asientos.png', [asi]),
    st('Recepción', 'ventas', '5. Libro 93', 'despues-ventas-libro.png', [lv93]),
  ]),
  'param-conceptos': empPer([
    st('Proceso de Parametrización > Conceptos', 'param', '3. Conceptos de flujo', 'despues-param-conceptos.png', [pin(28, 18, 'Conceptos', 'Los usa flujo de caja cuando hay cartola contabilizada. En la muestra no hay Excel de banco.')]),
    st('En paralelo', 'teso', '4. Flujo', 'despues-teso-flujo.png', [pin(28, 18, 'Flujo', 'Vacío de cartola. El pago 64 no crea asiento banco.')]),
    st('Recepción', 'teso', '5. Pago 64', 'despues-teso-pagos.png', [pagoAlm, pago64]),
  ]),
  'param-codigos': empPer([
    st('Proceso de Parametrización > Códigos financieros', 'param', '3. Catálogo T2', 'despues-param-codigos.png', [pin(28, 18, 'Códigos', 'Al contabilizar un movimiento de cartola 1:1. La muestra no importó cartola.')]),
    st('En paralelo', 'teso', '4. Cartolas', 'despues-teso-cartolas.png', [pin(28, 18, 'Import-only', 'Sin archivo no hay código financiero en flujo.')]),
    st('Recepción', 'teso', '5. Pago sin cartola', 'despues-teso-pagos.png', [pago64]),
  ]),
  'param-tipos-doc': empPer([
    st('Proceso de Parametrización > Tipos de documento', 'param', '3. FACTURA / OC / OV', 'despues-param-tipos-doc.png', [pin(28, 18, 'Tipos', 'La muestra usó OC, FACTURA, OV. No hay cotización ni NP (D11).')]),
    st('En paralelo', 'compras', '4. OC guardada', 'despues-compras-ordenes.png', [oc]),
    st('Recepción', 'ventas', '5. Factura 93', 'despues-ventas-libro.png', [lv93]),
  ]),
  'param-plan-cuentas': empPer([
    st('Proceso de Parametrización > Plan de cuentas', 'param', '3. Cuentas imputables', 'despues-param-plan-cuentas.png', [pin(30.67, 14.69, 'Plan', 'Se usaron para contabilizar compra 64, recepción OC y venta 93. Padres no imputables.')]),
    st('En paralelo', 'conta', '4. Asientos resultantes', 'despues-conta-asientos.png', [asi]),
    st('Recepción', 'compras', '5. Libro 64', 'despues-compras-libro.png', [libro64]),
  ]),
  'param-indicadores': empPer([
    st('Proceso de Parametrización > Indicadores BC', 'param', '3. TC del día', 'despues-param-indicadores.png', [pin(28, 18, 'Indicadores', 'La OC en moneda extranjera convierte a CLP para la escala. La muestra fue CLP.')]),
    st('En paralelo', 'compras', '4. OC CLP', 'despues-compras-ordenes.png', [oc]),
    st('Recepción', 'teso', '5. Pago CLP', 'despues-teso-pagos.png', [pago64]),
  ]),
  'param-proveedores': empPer([
    st('Proceso de Parametrización > Proveedores', 'param', '3. ALM SERVICES guardado', 'despues-param-proveedores.png', [prov]),
    st('En paralelo', 'compras', '4. OC al proveedor', 'despues-compras-ordenes.png', [oc, ocFac]),
    st('Recepción', 'teso', '5. Pago al mismo RUT', 'despues-teso-pagos.png', [pagoAlm, pago64]),
  ]),
  'param-contratista': empPer([
    st('Proceso de Parametrización > Contratista', 'param', '3. Maestro + tarifas', 'despues-param-contratista.png', [pin(28, 18, 'Maestro CTR', 'Labor, actividad, tarifa y CC. Se conservaron. Sin esto no se guarda ingreso diario.')]),
    st('En paralelo', 'compras', '4. Listado operativo', 'despues-ctr-listado.png', [ctrAlm]),
    st('Recepción', 'compras', '5. Ingreso y PF-00001', 'despues-ctr-ingreso.png', [ing]),
  ]),
  'param-af': empPer([
    st('Proceso de Parametrización > Activo fijo', 'param', '3. Familias packing', 'despues-param-af.png', [pin(28, 18, 'Familias', 'EQP / packing. Se usaron al dar de alta el equipo de 50000.')]),
    st('En paralelo', 'conta', '4. Maestro AF', 'despues-af-maestro.png', [afNom, af64]),
    st('Recepción', 'compras', '5. Factura 64', 'despues-compras-libro.png', [libro64]),
  ]),

  'ctr-listado': [
    ...empPer([
      st('Pre requisitos', 'param', '3. Maestro contratista', 'despues-param-contratista.png', [pin(28, 18, 'Maestro', 'Tarifas y labores de Export. Se conservaron.')]),
    ]),
    st('Proceso de Contratistas > Listado', 'compras', '4. ALM SERVICES operativo', 'despues-ctr-listado.png', [ctrAlm]),
    st('En paralelo', 'compras', '5. Ingreso diario ya guardado', 'despues-ctr-ingreso.png', [ing]),
    st('Recepción', 'compras', '6. PF-00001', 'despues-ctr-proformas.png', [pf]),
  ],
  'ctr-ingreso': [
    ...empPer([
      st('Pre requisitos', 'param', '3. Contratista y tarifa', 'despues-param-contratista.png', [pin(28, 18, 'Tarifa', 'Sin tarifario vigente el ingreso pide precio y motivo. En la muestra se guardó jornada de 8 horas.')]),
      st('Pre requisitos', 'compras', '4. Ficha operativa', 'despues-ctr-listado.png', [ctrAlm]),
    ]),
    st('Proceso de Contratistas > Ingreso diario', 'compras', '5. Se guardó la jornada', 'despues-ctr-ingreso.png', [ing]),
    st('En paralelo', 'compras', '6. Con eso se armó la proforma', 'despues-ctr-proformas.png', [pf]),
    st('Recepción', 'compras', '7. Reportería de ingresos', 'despues-ctr-rep-ingresos.png', [repPf]),
  ],
  'ctr-proformas': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Ingresos diarios guardados', 'despues-ctr-ingreso.png', [ing]),
    ]),
    st('Proceso de Contratistas > Proformas y facturas', 'compras', '4. Se guardó PF-00001 y quedó DEFINITIVA', 'despues-ctr-proformas.png', [pf]),
    st('En paralelo', 'compras', '5. D4: sin bandeja PIN', 'despues-ctr-aprobaciones.png', [pin(28, 18, 'Sin cadena', 'La cadena de PIN es solo OC. PF-00001 no espera firma acá.')]),
    st('Recepción', 'conta', '6. Cierre ya ejecutado: asiento 20260005', 'despues-ctr-traspaso.png', [ctrCierre]),
  ],
  'ctr-aprobaciones': [
    ...empPer([
      st('Pre requisitos', 'param', '3. Alcance D4', 'despues-admin-aprobaciones.png', [pin(28, 22, 'Solo Compras', 'No hay escala de proformas ni de OV.')]),
      st('Pre requisitos', 'compras', '4. PF-00001 ya DEFINITIVA', 'despues-ctr-proformas.png', [pf]),
    ]),
    st('Proceso de Contratistas > Aprobaciones', 'compras', '5. Bandeja vacía a propósito', 'despues-ctr-aprobaciones.png', [pin(28, 18, 'Sin pendientes', 'El proceso de la muestra no deja PIN acá. El dato está en Proformas.')]),
    st('En paralelo', 'compras', '6. Ingreso origen', 'despues-ctr-ingreso.png', [ing]),
    st('Recepción', 'conta', '7. Siguiente: traspaso', 'despues-ctr-traspaso.png', [pin(28, 18, 'Cierre', 'El mes se cierra con las DEFINITIVAS, no con esta bandeja.')]),
  ],
  'ctr-auditoria': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Ingreso y proforma guardados', 'despues-ctr-ingreso.png', [ing]),
      st('Pre requisitos', 'compras', '4. PF-00001 DEFINITIVA', 'despues-ctr-proformas.png', [pf]),
    ]),
    st('Proceso de Contratistas > Auditoría', 'compras', '5. Trazas de lo guardado', 'despues-ctr-auditoria.png', [pin(28, 18, 'Auditoría', 'CREAR ingreso, CREAR proforma, DEFINITIVA. Periodo 2026-10.')]),
    st('En paralelo', 'conta', '6. Traspaso', 'despues-ctr-traspaso.png', [pin(28, 18, 'Cierre', 'El cierre de mes deja otra traza cuando se ejecuta.')]),
    st('Recepción', 'compras', '7. Reportería', 'despues-ctr-rep-ingresos.png', [repPf]),
  ],
  'ctr-traspaso': [
    ...empPer([
      st('Pre requisitos', 'param', '3. Maestro y cuentas de contrato', 'despues-param-contratista.png', [pin(28, 18, 'Tipo de contrato', 'Debe / haber / administración. Sin esto el cierre no arma asiento.')]),
      st('Pre requisitos', 'compras', '4. Se guardaron los ingresos diarios', 'despues-ctr-ingreso.png', [ing]),
      st('Pre requisitos', 'compras', '5. Se armó y se guardó PF-00001 DEFINITIVA', 'despues-ctr-proformas.png', [pf]),
    ]),
    st('Proceso de Contratistas > Traspaso contable y cierre de mes', 'conta', '6. Cierre ejecutado: asiento 20260005', 'despues-ctr-traspaso.png', [ctrCierre]),
    st('En paralelo', 'compras', '7. Reportería del mismo mes', 'despues-ctr-rep-ingresos.png', [repPf]),
    st('Recepción', 'conta', '8. Listado: asiento 20260005 del cierre CTR', 'despues-conta-asientos.png', [asiCtr]),
  ],
  'ctr-rep-ingresos': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Ingreso guardado', 'despues-ctr-ingreso.png', [ing]),
      st('Pre requisitos', 'compras', '4. PF-00001 DEFINITIVA', 'despues-ctr-proformas.png', [pf]),
    ]),
    st('Proceso de Contratistas > Reporte ingresos', 'compras', '5. Lee PF-00001', 'despues-ctr-rep-ingresos.png', [repPf]),
    st('En paralelo', 'compras', '6. Labores por CC', 'despues-ctr-rep-cc.png', [pin(28, 18, 'Mismo mes', 'Mismo ingreso 2026-10.')]),
    st('Recepción', 'conta', '7. Traspaso', 'despues-ctr-traspaso.png', [pin(28, 18, 'Cierre', 'El reporte no asienta. El cierre sí.')]),
  ],
  'ctr-rep-cc': [
    ...empPer([
      st('Pre requisitos', 'param', '3. Centros de costo', 'despues-param-cc.png', [pin(28, 18, 'CC', 'El ingreso se guardó con CC.')]),
      st('Pre requisitos', 'compras', '4. Ingreso 8 horas', 'despues-ctr-ingreso.png', [ing]),
    ]),
    st('Proceso de Contratistas > Labores por centro de costo', 'compras', '5. Corte 2026-10', 'despues-ctr-rep-cc.png', [pin(28, 18, 'Labores por CC', 'Si el corte no muestra fila, el CC del ingreso no entra en el agrupado. El dato fuente es PF-00001.')]),
    st('En paralelo', 'compras', '6. Control de producción', 'despues-ctr-rep-prod.png', [pin(28, 18, 'Producción', 'Misma jornada.')]),
    st('Recepción', 'compras', '7. Proforma', 'despues-ctr-proformas.png', [pf]),
  ],
  'ctr-rep-prod': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Ingreso diario', 'despues-ctr-ingreso.png', [ing]),
      st('Pre requisitos', 'compras', '4. PF-00001', 'despues-ctr-proformas.png', [pf]),
    ]),
    st('Proceso de Contratistas > Control de producción', 'compras', '5. Jornada de la muestra', 'despues-ctr-rep-prod.png', [pin(28, 18, 'Producción', 'Lee cantidad/trato del ingreso 2026-10.')]),
    st('En paralelo', 'compras', '6. Reporte ingresos', 'despues-ctr-rep-ingresos.png', [repPf]),
    st('Recepción', 'conta', '7. Cierre de mes', 'despues-ctr-traspaso.png', [pin(28, 18, 'Traspaso', 'La producción no asienta; el cierre sí.')]),
  ],

  'ventas-ov': [
    ...empPer([
      st('Pre requisitos', 'ventas', '3. Cliente Pacific Fruit', 'despues-ventas-clientes.png', [pin(28, 18, 'Cliente', 'Ficha guardada en Export. Sin cotización (D11).')]),
      st('Pre requisitos', 'compras', '4. Artículo y bodega', 'despues-insumos-maestro.png', [pin(28, 18, 'Maestro', 'Insumo inventariable. Precio de venta no bajo precio de compra (D16).')]),
    ]),
    st('Proceso de Ventas > Órdenes de venta', 'ventas', '5. Se guardó la OV 10007260 y se confirmó stock', 'despues-ventas-ov.png', [ovCli, ov93]),
    st('En paralelo', 'ventas', '6. Se emitió y se contabilizó 93', 'despues-ventas-libro.png', [lv93, lvCli]),
    st('Recepción', 'conta', '7. Listado: asiento 20260001 venta 93', 'despues-conta-asientos.png', [asiVenta]),
  ],
  'ventas-emitir': [
    ...empPer([
      st('Pre requisitos', 'ventas', '3. OV CONFIRMADA', 'despues-ventas-ov.png', [ovCli]),
    ]),
    st('Proceso de Ventas > Emitir DTE', 'ventas', '4. Se eligió la OV y se emitió al sandbox', 'despues-ventas-emitir.png', [pin(27.05, 12.92, 'Emitir', 'FACTURA/NC/ND/GUIA. Folio oficial Export 93. ALM emitió el 64 hacia Export. El DTE queda EMITIDO; las cuentas van en Libro.')]),
    st('En paralelo', 'ventas', '5. Libro con folio 93', 'despues-ventas-libro.png', [lv93]),
    st('Recepción', 'conta', '6. Listado: asiento 20260001 venta 93', 'despues-conta-asientos.png', [asiVenta]),
  ],
  'ventas-libro': [
    ...empPer([
      st('Pre requisitos', 'ventas', '3. OV guardada', 'despues-ventas-ov.png', [ovCli, ov93]),
      st('Pre requisitos', 'ventas', '4. DTE emitido', 'despues-ventas-emitir.png', [pin(27.05, 12.92, 'Emitir', 'Sin emisión no hay fila EMITIDO en el libro.')]),
    ]),
    st('Proceso de Ventas > Libro de ventas', 'ventas', '5. Se asignó cuenta por ítem y se contabilizó 93', 'despues-ventas-libro.png', [lv93, lvCli]),
    st('En paralelo', 'compras', '6. Stock de la OV', 'despues-insumos-stock.png', [pin(28, 18, 'Stock', 'La OV de producto movió bodega al confirmar.')]),
    st('Recepción', 'conta', '7. Listado: asiento 20260001 venta 93', 'despues-conta-asientos.png', [asiVenta]),
  ],
  'ventas-clientes': [
    ...empPer(),
    st('Proceso de Ventas > Clientes', 'ventas', '3. Pacific Fruit guardado', 'despues-ventas-clientes.png', [pin(28, 18, 'Clientes', 'Receptor de la factura 93. ALM usa a Export como cliente al emitir el 64.')]),
    st('En paralelo', 'ventas', '4. OV a ese cliente', 'despues-ventas-ov.png', [ovCli]),
    st('Recepción', 'ventas', '5. Libro 93', 'despues-ventas-libro.png', [lvCli]),
  ],
  'ventas-rep-sii': [
    ...empPer([
      st('Pre requisitos', 'ventas', '3. Factura 93 contabilizada', 'despues-ventas-libro.png', [lv93]),
    ]),
    st('Proceso de Ventas > Libro de ventas SII', 'ventas', '4. Corte 2026-10', 'despues-ventas-rep-sii.png', [pin(28, 18, 'Libro SII', 'Debe leer folio 93. Si la grilla no lo muestra, el filtro de periodo/tipo no calza.')]),
    st('En paralelo', 'ventas', '5. Por cliente y producto', 'despues-ventas-rep-cliente.png', [pin(28, 18, 'Pacific', 'Misma OV e insumo.')]),
    st('Recepción', 'conta', '6. Listado: asiento 20260001 venta 93', 'despues-conta-asientos.png', [asiVenta]),
  ],
  'ventas-rep-cliente': [
    ...empPer([
      st('Pre requisitos', 'ventas', '3. OV y factura 93', 'despues-ventas-ov.png', [ovCli, ov93]),
    ]),
    st('Proceso de Ventas > Ventas por cliente y producto', 'ventas', '4. Pacific + artículo', 'despues-ventas-rep-cliente.png', [pin(28, 18, 'Cliente-producto', 'Lee la OV confirmada y el DTE 93.')]),
    st('En paralelo', 'ventas', '5. Libro SII', 'despues-ventas-rep-sii.png', [pin(28, 18, 'SII', 'Mismo folio 93.')]),
    st('Recepción', 'ventas', '6. Libro de ventas', 'despues-ventas-libro.png', [lv93]),
  ],

  'compras-ordenes': [
    ...empPer([
      st('Pre requisitos', 'param', '3. Proveedor ALM', 'despues-param-proveedores.png', [prov]),
      st('Pre requisitos', 'param', '4. Escala Compras y PIN 4821', 'despues-admin-aprobaciones.png', [pin(28, 22, 'Escala', 'Felipe firma. Admin arma cadena sin estar en el nodo.')]),
    ]),
    st('Proceso de Compras > Órdenes de compra', 'compras', '5. Se guardó, se envió y se recepcionó OC-2026-0001', 'despues-compras-ordenes.png', [oc, ocFac]),
    st('En paralelo', 'compras', '6. Bandeja: ya firmada', 'despues-compras-aprobaciones.png', [pin(28, 18, 'Bandeja', 'PIN usado. La OC no vuelve a pendiente.')]),
    st('Recepción', 'compras', '7. Libro factura 64 contabilizada', 'despues-compras-libro.png', [libro64, libroOc]),
  ],
  'compras-aprobaciones': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. OC enviada a aprobación', 'despues-compras-ordenes.png', [oc]),
    ]),
    st('Proceso de Compras > Aprobaciones', 'compras', '4. Se firmó con PIN 4821', 'despues-compras-aprobaciones.png', [pin(28, 18, 'Bandeja', 'Resultado: OC RECEPCIONADA. No queda fila pendiente.')]),
    st('En paralelo', 'compras', '5. Recepción y libro', 'despues-compras-libro.png', [libro64]),
    st('Recepción', 'conta', '6. Listado: asiento 20260004 recepción OC', 'despues-conta-asientos.png', [asiRec]),
  ],
  'compras-libro': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. OC-2026-0001 RECEPCIONADA', 'despues-compras-ordenes.png', [oc, ocFac]),
      st('Pre requisitos', 'ventas', '4. DTE ALM folio 64 emitido', 'despues-ventas-emitir.png', [pin(27.05, 12.92, 'Emitir en ALM', 'ALM emitió la factura a Export. Folio oficial 64.')]),
    ]),
    st('Proceso de Compras > Libro de compras', 'compras', '5. Facturas 61-63 con OC y 64/65 contabilizadas', 'despues-compras-libro.png', [libro61, libroOc3, libro62, libroOc4, libro63, libroOc5, libro65, libroOc2]),
    st('En paralelo', 'conta', '6. Activo packing 50000', 'despues-af-maestro.png', [afNom, af64]),
    st('Recepción', 'teso', '7. Deuda lista para pagar', 'despues-teso-pagos.png', [pagoAlm, pago64]),
  ],
  'compras-rep-pend': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. OC-2026-0001 ya RECEPCIONADA', 'despues-compras-ordenes.png', [oc]),
    ]),
    st('Proceso de Compras > OC pendientes de recepción', 'compras', '4. Lista vacía porque ya se recepcionó', 'despues-compras-rep-pend.png', [pin(28, 18, 'Pendientes', 'El reporte muestra saldo por recibir. La muestra no deja OC abierta. No se inventó OC INSUMOS madre.')]),
    st('En paralelo', 'compras', '5. OC por depto', 'despues-compras-rep-depto.png', [deptoOc]),
    st('Recepción', 'compras', '6. Libro 64', 'despues-compras-libro.png', [libro64]),
  ],
  'compras-rep-depto': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. OC guardada', 'despues-compras-ordenes.png', [oc, ocFac]),
    ]),
    st('Proceso de Compras > OC por depto y usuario', 'compras', '4. Lee OC-2026-0001 y factura 64', 'despues-compras-rep-depto.png', [deptoOc]),
    st('En paralelo', 'compras', '5. Pendientes de recepción', 'despues-compras-rep-pend.png', [pin(28, 18, 'Saldo', 'Cero: ya RECEPCIONADA.')]),
    st('Recepción', 'compras', '6. Libro', 'despues-compras-libro.png', [libroOc]),
  ],

  'insumos-maestro': empPer([
    st('Proceso de Insumos / Bodega > Maestro artículos', 'compras', '3. Artículos conservados', 'despues-insumos-maestro.png', [pin(28, 18, 'Maestro', 'Se usó el inventariable en la OV (D16 piso precio compra) y el movimiento factura 64.')]),
    st('En paralelo', 'ventas', '4. OV de producto', 'despues-ventas-ov.png', [ovCli]),
    st('Recepción', 'compras', '5. Entrada 64', 'despues-insumos-movimientos.png', [mov64]),
  ]),
  'insumos-bodegas': empPer([
    st('Proceso de Insumos / Bodega > Bodegas', 'compras', '3. Bodega de la OV y del movimiento', 'despues-insumos-bodegas.png', [pin(28, 18, 'Bodegas', 'La OV confirmada descuenta stock. La entrada 64 suma.')]),
    st('En paralelo', 'compras', '4. Stock', 'despues-insumos-stock.png', [pin(28, 18, 'Stock', 'Resultado de confirmar OV + guardar entrada.')]),
    st('Recepción', 'ventas', '5. OV 93', 'despues-ventas-ov.png', [ovCli]),
  ]),
  'insumos-stock': empPer([
    st('Pre requisitos', 'compras', '3. Entrada factura 64 guardada', 'despues-insumos-movimientos.png', [mov64]),
    st('Pre requisitos', 'ventas', '4. OV confirmada', 'despues-ventas-ov.png', [ovCli]),
    st('Proceso de Insumos / Bodega > Stock por bodega / producto', 'compras', '5. Saldo después de guardar esos movimientos', 'despues-insumos-stock.png', [pin(28, 18, 'Stock', 'Maestro inicial 1000 más entrada 64 menos salida de venta.')]),
    st('Recepción', 'compras', '6. Cierre de bodega', 'despues-insumos-cierre.png', [cierreBod, cierreSal]),
  ]),
  'insumos-movimientos': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Factura 65 en libro', 'despues-compras-libro.png', [libro65, libroOc2]),
      st('Pre requisitos', 'compras', '4. Guía 57 recepcionada', 'despues-insumos-guias.png', [guia57, guiaFac]),
    ]),
    st('Proceso de Insumos / Bodega > Movimientos / NC', 'compras', '5. ENTRADA_PROVEEDOR de la guía 57 con factura 65', 'despues-insumos-movimientos.png', [mov65]),
    st('En paralelo', 'compras', '6. OC INSUMOS contabilizada', 'despues-insumos-ordenes.png', [ocIns, ocInsFac]),
    st('Recepción', 'compras', '7. El asiento es de la factura, no del movimiento', 'despues-compras-libro.png', [libro65]),
  ],
  'insumos-cierre': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Movimientos del mes', 'despues-insumos-movimientos.png', [mov64]),
      st('Pre requisitos', 'compras', '4. Stock', 'despues-insumos-stock.png', [pin(28, 18, 'Saldo', 'Hay que tener las entradas/salidas guardadas antes de cerrar.')]),
    ]),
    st('Proceso de Insumos / Bodega > Cierre de bodega', 'compras', '5. Cierre 2026-10 ejecutado: asiento 20260007', 'despues-insumos-cierre.png', [cierreBod, cierreSal]),
    st('En paralelo', 'param', '6. Periodo contable', 'despues-conta-periodos.png', [per]),
    st('Recepción', 'conta', '7. Listado: asiento 20260007 cierre de bodega', 'despues-conta-asientos.png', [asiCierreBod]),
  ],
  'insumos-ordenes': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Proveedor ALM y escala', 'despues-param-proveedores.png', [prov]),
    ]),
    st('Proceso de Insumos / Bodega > Órdenes de insumos', 'compras', '4. OC-2026-0002 CONTABILIZADA', 'despues-insumos-ordenes.png', [ocIns, ocInsFac]),
    st('En paralelo', 'compras', '5. Guía 57 y factura 65', 'despues-insumos-guias.png', [guia57, guiaFac, guiaAsi]),
    st('Recepción', 'compras', '6. Libro de compras', 'despues-compras-libro.png', [libro65, libroOc2]),
  ],
  'insumos-aprobaciones': [
    ...empPer([
      st('Pre requisitos', 'param', '3. Escala Insumos', 'despues-admin-aprobaciones.png', [pin(28, 22, 'Insumos', 'Cadena distinta a Compras. La muestra no envió OC INSUMOS.')]),
    ]),
    st('Proceso de Insumos / Bodega > Aprobaciones', 'compras', '4. Bandeja vacía', 'despues-insumos-aprobaciones.png', [pin(28, 18, 'Bandeja', 'OC-2026-0001 usó la cadena Compras, no esta.')]),
    st('En paralelo', 'compras', '5. Bandeja Compras', 'despues-compras-aprobaciones.png', [pin(28, 18, 'Compras', 'Ahí se firmó 0001.')]),
    st('Recepción', 'compras', '6. OC de la muestra', 'despues-compras-ordenes.png', [oc]),
  ],
  'insumos-guias': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. OC INSUMOS 0002 aprobada', 'despues-insumos-ordenes.png', [ocIns]),
    ]),
    st('Proceso de Insumos / Bodega > Libro de guías', 'compras', '4. Guía 57 recepcionada, factura 65, asiento 20260006', 'despues-insumos-guias.png', [guia57, guiaFac, guiaAsi]),
    st('En paralelo', 'compras', '5. Movimiento con facturaRef 65', 'despues-insumos-movimientos.png', [mov65]),
    st('Recepción', 'compras', '6. Libro de compras', 'despues-compras-libro.png', [libro65, libroOc2]),
  ],

  'af-maestro': [
    ...empPer([
      st('Pre requisitos', 'param', '3. Familias packing', 'despues-param-af.png', [pin(28, 18, 'Param AF', 'Familia EQP, ubicación PACK, CC.')]),
      st('Pre requisitos', 'compras', '4. Factura 64 contabilizada', 'despues-compras-libro.png', [libro64]),
    ]),
    st('Proceso de Activo fijo > Maestro', 'conta', '5. Se guardó Equipo packing 50000', 'despues-af-maestro.png', [afNom, af64]),
    st('En paralelo', 'conta', '6. Traspaso AF', 'despues-af-traspaso.png', [pin(28, 18, 'Traspaso', 'El alta no asienta. El traspaso de depreciación sí, cuando se ejecute.')]),
    st('Recepción', 'conta', '7. Reportes AF', 'despues-af-reportes.png', [pin(28, 18, 'Reportes', 'Leen el activo guardado contra folio 64.')]),
  ],
  'af-traspaso': [
    ...empPer([
      st('Pre requisitos', 'conta', '3. Activo packing guardado', 'despues-af-maestro.png', [afNom, af64]),
      st('Pre requisitos', 'param', '4. Cuentas de depreciación', 'despues-param-af.png', [pin(28, 18, 'Cuentas AF', 'Parametrización de familia/subfamilia.')]),
    ]),
    st('Proceso de Activo fijo > Traspaso contable', 'conta', '5. Simular octubre: sin cuota (inicio 01-11)', 'despues-af-traspaso.png', [afPer]),
    st('En paralelo', 'conta', '6. Reportes', 'despues-af-reportes.png', [pin(28, 18, 'Reportes', 'Mismo activo.')]),
    st('Recepción', 'conta', '7. Comprobantes', 'despues-conta-asientos.png', [asi]),
  ],
  'af-reportes': [
    ...empPer([
      st('Pre requisitos', 'conta', '3. Equipo packing', 'despues-af-maestro.png', [afNom, af64]),
    ]),
    st('Proceso de Activo fijo > Reportes', 'conta', '4. Lee factura 64 y neto 50000', 'despues-af-reportes.png', [pin(28, 18, 'Reportes', 'Alta de la muestra. Sin asiento propio.')]),
    st('En paralelo', 'conta', '5. Traspaso', 'despues-af-traspaso.png', [pin(28, 18, 'Traspaso', 'Depreciación cuando corra el mes.')]),
    st('Recepción', 'compras', '6. Libro 64', 'despues-compras-libro.png', [libro64]),
  ],

  'conta-periodos': [
    st('Pre requisitos', 'param', '1. Empresas del holding', 'despues-admin-empresas.png', [almEmp, emp]),
    st('Proceso de Contabilidad > Períodos contables', 'conta', '2. Se dejó 2026-10 abierto', 'despues-conta-periodos.png', [per]),
    st('En paralelo', 'compras', '3. Todo el flujo usa ese mes', 'despues-compras-ordenes.png', [oc]),
    st('Recepción', 'conta', '4. Asientos del mes', 'despues-conta-asientos.png', [asi]),
  ],
  'conta-asientos': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Compra 64 contabilizada', 'despues-compras-libro.png', [libro64]),
      st('Pre requisitos', 'ventas', '4. Venta 93 contabilizada', 'despues-ventas-libro.png', [lv93]),
    ]),
    st('Proceso de Contabilidad > Comprobantes / asientos', 'conta', '5. Listado: 20260005 CIERRE, 20260003 COMPRAS, 20260001 VENTAS, 20260004 recepción', 'despues-conta-asientos.png', [asiCtr, asiCompra]),
    st('En paralelo', 'conta', '6. Mayor', 'despues-conta-mayor.png', [pin(28, 18, 'Mayor', 'Mismos comprobantes.')]),
    st('Recepción', 'conta', '7. Detalle: cuentas de las lineas del cierre', 'despues-conta-asiento-detalle-ctr.png', CONTA.ctr.pins),
  ],
  'conta-honorarios': empPer([
    st('Proceso de Contabilidad > Factores honorarios', 'conta', '3. Factores del mes', 'despues-conta-honorarios.png', [pin(28, 18, 'Honorarios', 'No hay boleta de honorarios en la cadena ALM 64 / Export 93.')]),
    st('En paralelo', 'conta', '4. Asientos de la muestra', 'despues-conta-asientos.png', [asi]),
    st('Recepción', 'compras', '5. Libro compras', 'despues-compras-libro.png', [libro64]),
  ]),
  'conta-presupuestos': empPer([
    st('Proceso de Contabilidad > Presupuestos', 'conta', '3. Presupuesto vs gasto real', 'despues-conta-presupuestos.png', [pin(28, 18, 'Presupuestos', 'El gasto real de la muestra es la OC 0001 / asiento 20260003 y la PF-00001.')]),
    st('En paralelo', 'conta', '4. Estado de resultados', 'despues-conta-er.png', [pin(28, 18, 'ER', 'Lee los asientos 2026-10.')]),
    st('Recepción', 'conta', '5. Asientos', 'despues-conta-asientos.png', [asi]),
  ]),
  'conta-diario': [
    ...empPer([
      st('Pre requisitos', 'conta', '3. Asientos ya creados', 'despues-conta-asientos.png', [asi]),
    ]),
    st('Proceso de Contabilidad > Libro diario', 'conta', '4. Compra 64, recepción, venta 93', 'despues-conta-diario.png', [pin(28, 18, 'Diario', 'Mismos números 20260001 / 20260003 / 20260004.')]),
    st('En paralelo', 'conta', '5. Mayor', 'despues-conta-mayor.png', [pin(28, 18, 'Mayor', 'Por cuenta.')]),
    st('Recepción', 'conta', '6. Balance', 'despues-conta-balance.png', [pin(28, 18, '8 columnas', 'Totales del mes.')]),
  ],
  'conta-mayor': [
    ...empPer([
      st('Pre requisitos', 'conta', '3. Asientos 2026-10', 'despues-conta-asientos.png', [asi]),
    ]),
    st('Proceso de Contabilidad > Libro mayor', 'conta', '4. Cuentas movidas por 64 y 93', 'despues-conta-mayor.png', [pin(28, 18, 'Mayor', 'Proveedores, ingresos, IVA, clientes.')]),
    st('En paralelo', 'conta', '5. Diario', 'despues-conta-diario.png', [pin(28, 18, 'Diario', 'Misma fuente.')]),
    st('Recepción', 'teso', '6. CC ALM', 'despues-teso-cc.png', [ccAlm]),
  ],
  'conta-balance': [
    ...empPer([
      st('Pre requisitos', 'conta', '3. Asientos del mes', 'despues-conta-asientos.png', [asi]),
    ]),
    st('Proceso de Contabilidad > Balance de 8 columnas', 'conta', '4. Totales 2026-10', 'despues-conta-balance.png', [pin(28, 18, 'Balance', 'Incluye compra 64 y venta 93.')]),
    st('En paralelo', 'conta', '5. Situación financiera', 'despues-conta-situacion.png', [pin(28, 18, 'Situación', 'Misma base.')]),
    st('Recepción', 'conta', '6. Estado de resultados', 'despues-conta-er.png', [pin(28, 18, 'ER', 'Ingresos 93 y gastos de OC/CTR.')]),
  ],
  'conta-er': [
    ...empPer([
      st('Pre requisitos', 'conta', '3. Venta 93 y compra 64', 'despues-conta-asientos.png', [asi]),
    ]),
    st('Proceso de Contabilidad > Estado de resultados', 'conta', '4. Resultado octubre', 'despues-conta-er.png', [pin(28, 18, 'ER', 'Ingreso factura 93, gasto OC 0001 / PF-00001 si el cierre CTR asienta.')]),
    st('En paralelo', 'conta', '5. Balance', 'despues-conta-balance.png', [pin(28, 18, 'Balance', 'Otra vista del mismo mes.')]),
    st('Recepción', 'ventas', '6. Libro 93', 'despues-ventas-libro.png', [lv93]),
  ],
  'conta-situacion': [
    ...empPer([
      st('Pre requisitos', 'conta', '3. Asientos y CC', 'despues-conta-asientos.png', [asi]),
    ]),
    st('Proceso de Contabilidad > Situación financiera', 'conta', '4. Activo / pasivo octubre', 'despues-conta-situacion.png', [pin(28, 18, 'Situación', 'Incluye proveedores de 64, clientes de 93 y el AF packing 50000 (sin asiento de alta).')]),
    st('En paralelo', 'conta', '5. AF maestro', 'despues-af-maestro.png', [afNom]),
    st('Recepción', 'teso', '6. Estado de cuenta', 'despues-teso-cc.png', [ccAlm]),
  ],

  'teso-cartolas': [
    ...empPer([
      st('Pre requisitos', 'teso', '3. Pago 64 ya registrado', 'despues-teso-pagos.png', [pagoAlm, pago64]),
    ]),
    st('Proceso de Tesorería > Cartolas', 'teso', '4. Import-only, sin Excel en la muestra', 'despues-teso-cartolas.png', [pin(28, 18, 'Cartolas', 'No se fingió archivo banco. El pago queda PENDIENTE hasta calzar un movimiento importado.')]),
    st('En paralelo', 'teso', '5. Conciliación y flujo', 'despues-teso-conciliacion.png', [pin(28, 18, 'Conciliación', 'Vacía sin cartola. No inventa movimientos.')]),
    st('Recepción', 'teso', '6. Nómina igual lista el 64', 'despues-teso-nominas.png', [nom64, nomAlm]),
  ],
  'teso-conciliacion': [
    ...empPer([
      st('Pre requisitos', 'teso', '3. Cartola (no hay)', 'despues-teso-cartolas.png', [pin(28, 18, 'Sin import', 'La conciliación resume cartolas. Sin archivo no hay líneas.')]),
      st('Pre requisitos', 'teso', '4. Pago 64', 'despues-teso-pagos.png', [pago64]),
    ]),
    st('Proceso de Tesorería > Conciliación', 'teso', '5. Resumen vacío a propósito', 'despues-teso-conciliacion.png', [pin(28, 18, 'Conciliación', 'Cuando se importe la cartola, el calce 1:1 es con el pago folio 64.')]),
    st('En paralelo', 'teso', '6. Flujo', 'despues-teso-flujo.png', [pin(28, 18, 'Flujo', 'Se nutre de cartola CONTABILIZADO.')]),
    st('Recepción', 'teso', '7. CC', 'despues-teso-cc.png', [ccAlm]),
  ],
  'teso-flujo': [
    ...empPer([
      st('Pre requisitos', 'teso', '3. Sin cartola contabilizada', 'despues-teso-cartolas.png', [pin(28, 18, 'Cartola', 'El flujo no usa el pago suelto; usa cartola + apertura.')]),
    ]),
    st('Proceso de Tesorería > Flujo de caja', 'teso', '4. Banco / moneda', 'despues-teso-flujo.png', [pin(28, 18, 'Flujo', 'Queda sin movimientos de banco. El speech es ese: el pago 64 está en Pagos y Nómina, no acá.')]),
    st('En paralelo', 'teso', '5. Pagos', 'despues-teso-pagos.png', [pagoAlm]),
    st('Recepción', 'teso', '6. Nómina', 'despues-teso-nominas.png', [nom64]),
  ],
  'teso-pagos': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Factura 64 contabilizada (aging)', 'despues-compras-libro.png', [libro64]),
      st('Pre requisitos', 'param', '4. Proveedor ALM', 'despues-param-proveedores.png', [prov]),
    ]),
    st('Proceso de Tesorería > Pagos', 'teso', '5. Se guardó el pago TEF calce 64', 'despues-teso-pagos.png', [pagoAlm, pago64]),
    st('En paralelo', 'teso', '6. CC y nómina usan ese pago', 'despues-teso-cc.png', [ccAlm]),
    st('Recepción', 'conta', '7. Listado: asiento 20260003 compra 64', 'despues-conta-asientos.png', [asiCompra]),
  ],
  'teso-nominas': [
    ...empPer([
      st('Pre requisitos', 'teso', '3. Pago folio 64 guardado', 'despues-teso-pagos.png', [pago64]),
    ]),
    st('Proceso de Tesorería > Nómina semanal', 'teso', '4. Compromiso 64 / ALM', 'despues-teso-nominas.png', [nom64, nomAlm]),
    st('En paralelo', 'teso', '5. Estado de cuenta', 'despues-teso-cc.png', [ccAlm]),
    st('Recepción', 'teso', '6. Cartola sigue sin Excel', 'despues-teso-cartolas.png', [pin(28, 18, 'Import-only', 'Aplazar semana no muta el DTE 64.')]),
  ],
  'teso-cc': [
    ...empPer([
      st('Pre requisitos', 'compras', '3. Compra 64 contabilizada', 'despues-compras-libro.png', [libro64]),
      st('Pre requisitos', 'teso', '4. Pago guardado', 'despues-teso-pagos.png', [pagoAlm, pago64]),
    ]),
    st('Proceso de Tesorería > Estado de cuenta', 'teso', '5. ALM: deuda y calce 64', 'despues-teso-cc.png', [ccAlm]),
    st('En paralelo', 'teso', '6. Nómina', 'despues-teso-nominas.png', [nom64]),
    st('Recepción', 'conta', '7. Mayor de proveedores', 'despues-conta-mayor.png', [pin(28, 18, 'Mayor', 'Misma deuda 20260003.')]),
  ],
};

export function stepsFor(h) {
  const base = STEPS[h.slug] || [
    st('Pre requisitos', 'param', '1. Empresa y periodo 2026-10', 'despues-admin-empresas.png', [almEmp, emp]),
    st(`Proceso de ${h.grupo} > ${h.label}`, h.cls, `2. ${h.label}`, h.img, [pin(28, 14, h.label, 'Pantalla de la muestra. Cadena OC-2026-0001, DTE 64, DTE 93, PF-00001, pago 64.')]),
  ];
  return withContaItems(h.slug, base);
}

export const granSteps = [
  st('Pre requisitos', 'param', '1. Empresas del holding', 'despues-admin-empresas.png', [almEmp, emp]),
  st('Pre requisitos', 'param', '2. Periodo 2026-10 abierto', 'despues-conta-periodos.png', [per]),
  st('Pre requisitos', 'param', '3. Proveedor ALM guardado', 'despues-param-proveedores.png', [prov]),
  st('Pre requisitos', 'param', '4. Escala Compras y PIN 4821', 'despues-admin-aprobaciones.png', [pin(28, 22, 'Reglas', 'Felipe firma OC. Sin cadena OV ni PIN de proformas (D4).')]),
  st('Proceso de Compras > Órdenes de compra', 'compras', '5. Se guardó y se recepcionó OC-2026-0001', 'despues-compras-ordenes.png', [oc, ocFac]),
  st('Proceso de Compras > Libro de compras', 'compras', '6. Facturas 61-63 con OC; 64 y 65 contabilizadas', 'despues-compras-libro.png', [libro61, libroOc3, libro65, libroOc2]),
  st('Proceso de Insumos / Bodega > Órdenes de insumos', 'compras', '7. OC-2026-0002 INSUMOS CONTABILIZADA', 'despues-insumos-ordenes.png', [ocIns, ocInsFac]),
  st('Proceso de Insumos / Bodega > Libro de guías', 'compras', '8. Guía 57 recepcionada con factura 65', 'despues-insumos-guias.png', [guia57, guiaFac, guiaAsi]),
  st('En paralelo', 'compras', '9. Movimiento ENTRADA con facturaRef 65', 'despues-insumos-movimientos.png', [mov65]),
  st('Recepción', 'conta', '10. Asiento 20260006 compra 65', 'despues-conta-asientos.png', [CONTA.insumos.list]),
  st('Recepción', 'conta', '11. Detalle existencia insumos 65', 'despues-conta-asiento-detalle-insumos.png', CONTA.insumos.pins),
  st('En paralelo', 'conta', '12. Se dio de alta el packing 50000', 'despues-af-maestro.png', [afNom, af64]),
  st('En paralelo', 'compras', '13. Entrada bodega factura 64', 'despues-insumos-movimientos.png', [mov64]),
  st('Proceso de Insumos / Bodega > Cierre de bodega', 'compras', '14. Cierre 2026-10 ejecutado: asiento 20260007', 'despues-insumos-cierre.png', [cierreBod, cierreSal]),
  st('Recepción', 'conta', '15. Listado: asiento 20260007 cierre de bodega', 'despues-conta-asientos.png', [asiCierreBod]),
  st('Recepción', 'conta', '16. Detalle: cuentas del cierre de bodega', 'despues-conta-asiento-detalle-cierre-bodega.png', CONTA.bodega.pins),
  st('Proceso de Ventas > Órdenes de venta', 'ventas', '17. Se guardó la OV y salió folio 93', 'despues-ventas-ov.png', [ovCli, ov93]),
  st('Proceso de Ventas > Libro de ventas', 'ventas', '18. Se contabilizó 93', 'despues-ventas-libro.png', [lv93, lvCli]),
  st('Proceso de Contratistas > Ingreso diario', 'compras', '19. Se guardó la jornada', 'despues-ctr-ingreso.png', [ing]),
  st('Proceso de Contratistas > Proformas y facturas', 'compras', '20. Se armó PF-00001 DEFINITIVA', 'despues-ctr-proformas.png', [pf]),
  st('Proceso de Contratistas > Traspaso y cierre', 'conta', '21. Cierre CTR ejecutado: asiento 20260005', 'despues-ctr-traspaso.png', [ctrCierre]),
  st('Proceso de Tesorería > Pagos', 'teso', '22. Se guardó el pago folio 64', 'despues-teso-pagos.png', [pagoAlm, pago64]),
  st('Proceso de Tesorería > Estado de cuenta', 'teso', '23. CC con esa deuda y ese pago', 'despues-teso-cc.png', [ccAlm]),
  st('En paralelo', 'teso', '24. Nómina 64 (sin cartola)', 'despues-teso-nominas.png', [nom64, nomAlm]),
  st('Recepción', 'conta', '25. Listado: asiento 20260005 del cierre CTR', 'despues-conta-asientos.png', [asiCtr, asiCompra]),
  st('Recepción', 'conta', '26. Detalle: cuentas de las lineas del cierre CTR', 'despues-conta-asiento-detalle-ctr.png', [detCtrCta, detCtrGlo]),
];
