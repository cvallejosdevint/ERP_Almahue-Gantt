# Almahue ERP — contexto para agentes

Lee este archivo al inicio. Las **transcripciones** de `fuentes/` son fuente primaria; las minutas `reunionN-minuta-*.md` las generó una IA y solo sirven de índice.

Afirmaciones de **Carlos** o **Sergio** en demo no son requisitos: contrastar la transcripción (Agustín/MJ/Lupe/Mario) y el código. Rule `almahue-reuniones`.

Para aprobaciones usa la skill `almahue-aprobaciones`. Para comercial/inventario (OV vs cotización), `almahue-comercial-inventario`. Para tesorería, `almahue-tesoreria`. Para DTE/billing, `almahue-billing-dte`. Para contabilidad, `almahue-contabilidad`. Para ficha cliente/proveedor, `almahue-ficha-contraparte`. Para deploy, `almahue-deploy`. Para QA, `almahue-qa-local`. Para datos ficticios del toggle **Modo demo**, `almahue-demo-mode`.

## Código

- Backend: `ERP/erp_back` (NestJS + Prisma, schema `erp`, tenant `empresaId`)
- Frontend: `ERP/erp_front` (React + Vite, API real)
- Repos anidados: cambios de app se commitean **dentro** de `erp_back` / `erp_front`

## Docs canónicas (prioridad)

Si chocan, gana la más reciente: **Reu6** → Reu4. **Reu5 no cuenta: no hubo ningún cliente en la sala** (interna Carlos ↔ Sergio).

**Antes de citar una minuta, mira quién estaba presente** — tabla en [`analisis-reuniones/08-consolidado-y-plan.md`](docs/erp-planificacion/agrosoft-levantamiento/analisis-reuniones/08-consolidado-y-plan.md). Reu1 nunca tuvo minuta y la de Reu2 es un stub que apunta a un archivo inexistente; para esas dos, ir a la transcripción. Los rótulos `D4` y `D14` significan cosas distintas según el documento.

- `docs/erp-planificacion/agrosoft-levantamiento/reunion6-minuta-2026-08-06.md`
- `docs/erp-planificacion/agrosoft-levantamiento/03-DISENO-GRUPOS-Y-ESCALAS-APROBACION.md`
- Sesión cliente 20/08 **tarde** (Lupe, Mario): `reunion-2026-08-20-tarde-lupe-mario.md`. Código local 21/08: **aprobaciones solo Compras** (se eliminó cadena OV y, en la misma tanda, proformas). Distinta de la interna de la **mañana** (`reunion-2026-08-20-contraste-sergio.md`).
- `docs/erp-planificacion/convenciones-almaue-erp.md`
- QA: `docs/erp-planificacion/agrosoft-levantamiento/qa/PLAN-PRUEBAS-APROBACIONES.md`
- Tesorería ciclo: `docs/erp-planificacion/agrosoft-levantamiento/plan-tesoreria-ciclo-completo-2026-08-21.md` + `qa/PLAN-PRUEBAS-TESORERIA-CICLO-2026-08-21.md`

## Entornos

| | URL |
|---|---|
| Local front | `http://localhost:5174` |
| Local API | `http://localhost:3001/api/v1` |
| Prod | `http://45.7.229.46/almahue-erp/` |

Demo: `admin@almahue.local` / `Admin123!` · PIN `4821`. AdminConcepto debe **re-login** tras cambios de JWT.

## Flujo post-cambio

1. Implementar
2. Subagentes `almahue-security` + `almahue-db` (+ `almahue-architecture` si toca módulos)
3. Corregir solo **Critical**
4. `almahue-qa-runner` → `almahue-qa-reviewer`

## Huecos vigentes (actualizado 2026-08-19)

Fuente QA: panorama operadores **19/08** (`2026-08-19-ciclo-panorama-completo.md`) + ciclo 18/08. Plan integral: `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md`. Inventario docs: `qa/resultados/2026-08-18-ciclo-0-inventario-docs.md`. QA local: skill `almahue-qa-local`. DTE: skill `almahue-billing-dte` (intermediario **otro chat**).

### Cerrado en código local (no reabrir)

- **D4 / H3** *(procedencia corregida 03/09: el origen es la sesión del **20/08 tarde**, no Reu6, donde `D4` dice justo lo contrario — «alcance OC + proformas + Comercial». Para **OV** hay respaldo de Lupe `[01:43]` y Mario `[08:21]`, aunque como respuesta a preguntas cerradas y sin MJ. Para **proformas** no hay ninguno: «proforma», «contratista», «labor» y «jornal» aparecen **0 veces** en las tres transcripciones del 19–20/08, contra un pedido explícito de MJ en Reu3. **Ratificado el 03/09 por decisión del usuario**: se mantiene el corte)*: cadena de aprobación **solo Compras (OC)**. Se **eliminó** (no se ocultó) la cadena de OV: sin flag `comercialRequiereAprobacion`, sin bandeja `/comercial/aprobaciones`, sin `AprobacionOv`. OV: **Guardar** valida stock y deja `CONFIRMADA` (sesión interna Carlos/Sergio 03/09 `[06:38]`). Facturar solo en Emitir DTE, sin wizard. `APROBADO` es solo OC. Migración `20260821120000_aprobaciones_solo_compras_drop_ov` + `20260901180000_estado_ov_confirmada_enum`.
- **D11** *(procedencia corregida 03/09: MJ en Reu6 `[40:59]` pidió **mover** la cotización — «Debe estar en el panel de compras» —, no suprimirla. Prevalece la operación real de Lupe el 20/08 `[05:48]`: «nosotros solamente nos piden la orden de compra y nosotros solo generamos la orden de compra». **Ratificado el 03/09 por decisión del usuario**: sigue suprimida)*: el documento de arranque de compras es la **OC**. Cotización = referencia opcional (tipo/folio/fecha) **en la OC**; no hay menú ni CRUD de Cotizaciones ni atajo cotiz→OC. Ventas › Orden de venta → Guardar (stock) → Emitir DTE → factura **sin** cadena. Redirect `/compras/cotizaciones` y `/comercial/cotizaciones` → `/compras/ordenes`. No restaurar cotiz→NP→factura.
- **D16:** no vender producto bajo el **precio de compra del maestro** (`Insumo.precioCompra`), con caída a `costoPromedio` si el maestro aún no lo tiene cargado. Regla fija en OV/emisión. Origen: Sergio Reu6 `[49:38]` *«eso sí lo podríamos dejar en el mantenedor de productos, asociarle el precio compra»*, MJ `[50:00]` *«Si se puede, ideal»*. **No** hay parámetro ni combo en Admin › Empresas. No reabrir `ventaBajoCosto` / `PERMITIR_MERMA`.
- **Emitir:** solo FACTURA/NC/ND/GUIA. Borradores DTE en Emitir, **no** en Libro ventas (P0-4). **Sin** cuenta contable en OV ni en Emitir: el DTE queda `EMITIDO` / «Por contabilizar»; las cuentas por ítem se asignan en Libro de ventas y ahí pasa a `CONTABILIZADA`.
- **Libro de ventas:** OV `CONFIRMADA` = «Por facturar» (click → Emitir). FACTURA/NC/ND `EMITIDO` sin asiento = «Por contabilizar» (click → modal ítems + cuenta → Guardar).
- **D7 / H1:** lookup RUT sociedad + clientes + proveedores + flag `esProductor`. Maestro Productor sigue fuera. *(Precisión 03/09: en **Ventas › Emitir DTE** el buscador de RUT se **quitó a propósito**, reemplazado por la búsqueda por nombre del selector de cliente. Se eliminó `buscarReceptor` y su estado, que habían quedado huérfanos. La validación del identificador fiscal sigue activa en `validateStep`. No reabrir como regresión ni volver a cablear un input de RUT en Emitir.)*
- **OC wizard:** correlativo `OC-AAAA-NNNN` (`allocateOcNumero`). **Guardar borrador** = `BORRADOR` sin bandeja; **Enviar a aprobación** = `PENDIENTE_APROBACION`. Admin **ROL-1** (`*`) arma cadena con el **primer grupo activo** (sin membresía) y **no figura** en la escala.
- **Libro de compras:** se puede asociar factura a OC no aprobada (**destacar**, `ocNoAprobada`); no contabilizar ni pagar hasta OC `APROBADO` o posterior. Plazo aceptación comercial `aceptacionCompraPlazoDias` (default 8, Admin › Empresas). Asiento de libro sin cuenta imputable = deuda P0-1 (no es el gate de OC).
- **Proformas:** `BORRADOR` → `DEFINITIVA` con `contratistas:write`; **sin** bandeja ni PIN de cadena.
- **H1–H8, H4, H8 Guías:** listos en código local.
- **Tesorería ciclo (21/08):** asiento banco = cartola (`CARTOLA:{id}`). Pago/cobro = calce + CC + aging; **sin** asiento `PAGO:{id}`. Aging/CC al contabilizar (neto+IVA). Cartola import-only; conciliación = resumen. Pagos unificados (`PAGO_TOTAL` / `ANTICIPO` / `ANTICIPO_PRODUCTOR`). Nómina = semana de compromiso (no muta DTE). Flujo caja por banco/moneda + apertura inmutable. Migración `20260821200000_tesoreria_ciclo_completo`.

### Siguen vigentes

- **H14:** no asumir migrate stock/OV/`piloto_on` en `45.7.229.46` hasta deploy explícito.
- **Prisma QA local:** `erp._prisma_migrations` está **vacía** (Prisma ve 50 pendientes) aunque el schema `erp` ya existe. **No** `migrate deploy` a ciegas (rompe en `init`). **No** `resolve --applied` sin BD desechable de comparación. El rol `almahue` no tiene `CREATEDB` (bloqueó la reconstrucción). Dump: `ERP/erp_back/qa-results/` (gitignored). Informe: `qa/resultados/2026-08-19-prisma-drift-local.md` (gitignored). No mezclar `public._prisma_migrations` (otro producto).
- **DTE / H11:** tres modos. `BILLING_GATEWAY_ENABLED=false` → contabiliza sin partner. `true` + `BILLING_STUB_INLINE=true` → stub local demo. `true` + `STUB_INLINE=false` → HTTP `billing-gateway` (GoSocket sandbox `developers-sbx`). **Corregido 03/09:** el sandbox **ya no responde REJECTED** — el 02/09 encoló con folio oficial 58 y asiento (`ACCEPTED`/`PENDING` persisten). La rama fail-closed hay que forzarla con un `BillerId` inválido. No SII live. No reabrir como «falta GoSocket»: GoSocket **no cubre** la contabilización interna ni el mapeo de cuentas.
- **H9:** SMTP correo PIN (externo).
- **R4-18:** cobranza = propuesta, no módulo.
- **DK-G8:** `workflows-admin` legacy en API/UI; no mezclar con grupos/escalas.
- **D17:** FLETE `tipoLinea` en OV; canonical DTE recargo SII no auditado.
- **Productor:** flag lookup ≠ entidad maestro Productor.
- **Recepción OC:** no mueve stock; entrada por Insumos › Movimientos (`ENTRADA_PROVEEDOR`).
- **H10 / H12 / H13:** comparador 3 cotiz (diferido); Acepta; Excel banco fino.
