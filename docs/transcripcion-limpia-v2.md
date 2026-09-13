# Transcripción limpia v2

**Fecha:** 2026-08-16  
**Método:** depuración en español de Chile (filtro de muletillas) + contraste con minutas. Pipeline local: [`tools/transcript-ollama/`](../tools/transcript-ollama/README.md) (Ollama, sin APIs de pago).  
**Fuentes crudas:** `docs/erp-planificacion/agrosoft-levantamiento/fuentes/transcripcion*.md` (Reu1–Reu6).  
**Prioridad de verdad:** Reu6 > Reu5 > Reu4; **Agustín / María Jesús (MJ)** sobre opiniones de Carlos/Sergio en demo.

**Exclusión:** el concepto de mermas no aplica al negocio; no se documenta ni se propone.

**Leyenda de origen:** `Cliente` = Agustín/MJ/equipo Almahue · `Hipótesis` = Carlos/Sergio en demo · `Minuta` = decisión ya formalizada.

---

## 1. Identidad del producto y alcance

ERP agrícola (Agrosoft 3.0) para operación multi-empresa (Almahue SpA, logística, frutícola, etc.). No reemplazar Book (mano de obra). Maquinaria y niveles de almacenamiento: fuera de v1. AlmaWeb / Power BI son sistemas vecinos, no el ERP.

| ID | Tema | Valor de negocio | Origen | Estado |
|---|---|---|---|---|
| DEC-01 | Sin módulo Mano de Obra | Labores en Contratistas | Minuta Reu1 | Confirmado |
| DEC-02 | Sin solicitud de compra | Ir directo a OC | Minuta | Confirmado |
| DEC-03 | Aislamiento por empresa activa | Header aísla CC, bodegas, documentos | Cliente Reu6 | Confirmado |
| DEC-10 | Maquinaria | No usado en rubros | Minuta | Fuera v1 |

---

## 2. Administración, usuarios y permisos

Usuarios se administran **en el ERP** (no solo en ambiente de desarrollo). Un usuario puede tener varias empresas; la empresa del header es la que filtra datos. Super admin ve todas las empresas. Permisos por **rol** (lectura/escritura por módulo/pantalla); si hay diferencia por empresa, se crea **otro rol**.

SSO Microsoft: pedido de cliente (correos corporativos / baja de cuenta Entra). En código hay botón; credenciales IT pendientes. Hipótesis Devint: “como Google/Facebook”.

PIN de aprobación: no vive en el checkbox del rol (implementación antigua vista en demo). Queda ligado a **designación en reglas** + PIN de 4 dígitos del usuario.

| ID | Decisión | Origen | Estado |
|---|---|---|---|
| D1 Reu6 | Admin usuarios en ERP; multi-empresa | Cliente + minuta | Confirmado |
| D2 | Super admin aprueba cualquier pendiente (con aviso) | Cliente | Confirmado |
| D3 | Permisos por rol, no por empresa | Cliente | Confirmado |
| D5 | Quitar PIN del mantenedor de roles | Minuta (post demo) | Confirmado |
| D19 | SSO Microsoft | Cliente | Parcial (sin Tenant/Client ID) |

---

## 3. Aprobaciones

Reu4 hablaba de “una firma / pool de jefes”. Reu6 evoluciona a **cadena secuencial** por montos + línea de mando + suplencia de vacaciones. El solicitante **no elige** un aprobador ajeno al área.

Módulos con cadena: Compras (OC), Contratistas (proformas). Comercial (OV) está **reservado / parametrizable** (`comercialRequiereAprobacion`); no es el mismo flujo que factura.

| ID | Decisión | Origen | Estado |
|---|---|---|---|
| D4 Reu6 | Cadena automática por módulo/monto | Minuta | Confirmado (código grupos/escalas) |
| D6 | Organigrama + tope + suplencia | Cliente | Confirmado |
| Reu4 D2–D3 | Proforma aprobada sin edición; clave de reversa **por usuario** | MJ | Confirmado |

---

## 4. Compras

Cotización de **proveedor** (no de cliente). Convierte a **orden de compra**. OC: afecto/exento, CC por ítem, cuenta/elemento, proveedor del maestro. Libro de compras: asociar factura solo a OC **aprobadas y recepcionadas**. Matching 3 vías (OC–recepción–factura) es regla operativa.

Productores **fuera** del menú Compras como listado mezclado; flag `esProductor` en ficha.

Tres cotizaciones comparativas: ideal futuro, **no** proceso actual (H10 diferido).

| ID | Decisión | Origen | Estado |
|---|---|---|---|
| D11 flujo | Cotización Compras → OC | MJ/Agustín + código | Confirmado |
| Reu4 D4 | OC ligada a factura solo si aprobada + recepcionada | MJ | Confirmado |
| H10 | Cotizaciones comparativas | Hipótesis / futuro | Diferido |

---

## 5. Ventas / comercial

MJ: **ventas no cotizan**. Agustín: hace falta un documento previo a la factura (orden / proforma comercial). Decisión de producto: menú **Orden de venta** (no cotización de cliente en Ventas).

OV: línea producto (catálogo + bodega + stock) o servicio (sin stock). El movimiento de inventario ocurre al **confirmar** la OV, no al facturar. La factura copia cantidad y descripción; **precio editable**. Stock vendible = saldo positivo real (no tránsito). Multi-bodega: no vender sobre stock. Flete = **línea adicional**, no recargo SII en el detalle.

No restaurar cotización → nota de pedido → factura (eso apareció en UI Reu5 y quedó obsoleto).

Emitir documento: FACTURA / NC / ND / GUÍA. Libro de ventas = consulta de emitidos/contabilizados (sin botón emitir).

| ID | Decisión | Origen | Estado |
|---|---|---|---|
| D11–D15 Reu6 | OV, stock, multi-bodega | MJ + Agustín | Confirmado |
| D16 | No vender bajo costo (parametrizable, default bloquear) | Minuta | Confirmado (sin excepciones de negocio inventadas) |
| D17 | Flete como línea | Minuta | Confirmado |
| Reu4 D5–D8 | Guías ≠ libro ventas; emisión en pantalla dedicada | MJ | Confirmado |

---

## 6. Contrapartes (ficha única)

Bases **separadas** cliente vs proveedor. Consulta RUT unificada (sociedad, cliente, proveedor; productor como flag, **no** maestro propio). Ficha: bancos (N cuentas/monedas), contactos, direcciones de despacho.

---

## 7. Insumos / bodega

Maestro de artículos (familia, UM, inventariable, cuenta de centralización). Bodegas por empresa. Movimientos: entrada proveedor, traslado, salida, devolución/NC. Carga masiva tipo AlmaWeb = depende de Excel MJ (proyecto vecino). NC inventariable reingresa bodega.

`Insumo.stock` global es legado de lectura; el saldo de venta es **por bodega**.

---

## 8. Contabilidad y tesorería (alcance, no demo completa Reu6)

Plan de cuentas con flags CC / elemento / área; **inactivar** en vez de borrar si hay movimiento. Periodos en Contabilidad. Cartola Excel → conciliar (plantilla fina MJ pendiente). Estado de cuenta por RUT (compras+ventas). Contabilidad electrónica SII = segunda etapa.

---

## 9. Facturación electrónica (DTE)

GoSocket es proveedor **independiente** del ERP. Credenciales y docs oficiales pendientes. El ERP opera con **stub local** (PDF/print, sin SII real). Carga masiva histórica: MJ ↔ Acepta (externo).

Hipótesis Devint en Reu6: “ya tenemos documentación para iniciar”. No tratarlo como go-live.

---

## 10. Diferidos explícitos

| Tema | Quién | Nota |
|---|---|---|
| Traspaso gastos próxima temporada | Producto + MJ | No bloquea piloto |
| SMTP / correo al cambiar PIN | Infra Almahue | H9 |
| Excel cartolas finas | MJ | H13 |
| Cobranza módulo | Propuesta | Fuera piloto |
| Exportación / COMEX profundo | Manual MJ | Campos en documento; UI parcial |
| Deploy prod migrate OV/stock | Operación | H14 |

---

## 11. Cómo leer a Carlos y Sergio

En las transcripciones aparecen frases del tipo “ya está”, “lo podemos incorporar”, “esto no hay que considerarlo”. Se registran como **hipótesis** hasta que consten en minuta de MJ/Agustín o en código + prueba. Ejemplos: SSO “listo como Google”; cotización de ventas; PIN en el rol; emisión SII inminente.
