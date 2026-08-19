# Plan de pruebas v1 (E2E con stubs GoSocket)

> **Histórico (corte stub, 2026-08-16).** No usar como H11 vigente ni como estado de OC (`cotiz→OC` = `BORRADOR`, no `EMITIDO`). Plan vigente: `qa/PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md`. Billing HTTP + fail-closed CAF: `qa/resultados/2026-08-19-billing-errores-*.md`.

**Fecha:** 2026-08-16  
**Entorno:** local front `http://localhost:5174` · API `http://localhost:3001/api/v1` · `BILLING_STUB_INLINE`.  
**Complementa:** `docs/erp-planificacion/agrosoft-levantamiento/qa/PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` (215 casos). Este v1 es el **recorte core** para piloto pre-integración.

Usuarios seed típicos: `admin@almahue.local` / `Admin123!` · PIN demo `4821`. AdminConcepto: **re-login** tras cambiar JWT.

Sin pruebas de mermas.

---

## 1. Estrategia

| Capa | Qué cubre | Qué no |
|---|---|---|
| Stub DTE | Folio local, print HTML, error/timeout inyectado | SII, XML partner, timbraje |
| Golden path | Compras→OC→recepción; OV→stock→factura stub | Temporada puente, COMEX profundo |
| RBAC | digitador / aprobador / solo lectura / AdminConcepto | SMTP PIN |
| Datos | Tenant `empresaId`; no ver la otra sociedad | Carga Acepta |

Evidencia: `qa/resultados/` (gitignored). Sin JWT en informes.

---

## 2. Casos core (golden paths)

| ID | Flujo | Pasos | Esperado | Rol |
|---|---|---|---|---|
| GP-CMP-01 | Cotización → OC | Alta cotización proveedor; convertir a OC; emitir | OC `EMITIDO` con `proveedorId`; no genera factura venta | Compras write |
| GP-CMP-02 | OC → aprobación → recepción | Solicitar cadena; PIN; recepción confirmada | Bandeja avanza; recepción `CONFIRMADO` | Solicitante + aprobador |
| GP-CMP-03 | Libro compras | Registrar factura vs OC recepcionada | `matchOk`; OC no recepcionada no asociable | Compras |
| GP-INV-01 | Entrada bodega | Movimiento `ENTRADA_PROVEEDOR` confirmado | Stock por bodega sube (idealmente vía `StockInsumoBodega`) | Insumos write |
| GP-VEN-01 | OV producto | Wizard OV; splits bodega; guardar borrador | `ORDEN_VENTA` BORRADOR; sin salida stock | Ventas write |
| GP-VEN-02 | Confirmar OV | Confirmar (o aprobar si flag on) | `SALIDA_VENTA`; saldo no negativo | Ventas / aprobador OV |
| GP-VEN-03 | Factura desde OV | Emitir FACTURA; stub billing | Copia qty/desc; precio editable; **sin** segundo movimiento stock | Ventas |
| GP-VEN-04 | NC inventariable | NC sobre factura; contabilizar | Movimiento `DEVOLUCION_NC` positivo | Ventas |
| GP-FIC-01 | Lookup RUT | `GET /comercial/lookup-rut` | Sociedad/cliente/proveedor del **mismo** tenant | Cualquiera con permiso |

---

## 3. Casos de borde

| ID | Escenario | Esperado |
|---|---|---|
| BD-STUB-01 | Stub timeout / 5xx al emitir | Toast error; documento no queda “emitido SII”; se puede reintentar |
| BD-STUB-02 | Stub OK pero sin XML partner | Print local; no fallar por XML ausente |
| BD-APB-01 | OC sobre tope / sin saldo de facultad | Cadena exige siguiente nodo; no auto-aprueba |
| BD-APB-02 | PIN incorrecto | No cambia estado; no filtra el PIN en logs |
| BD-APB-03 | AdminConcepto sin re-login | 403 en config; tras login nuevo, acceso |
| BD-VEN-01 | Venta sobre stock | API 400; sin movimiento |
| BD-VEN-02 | Precio bajo costo (D16 BLOQUEAR) | Bloqueo; no hay excepción de negocio |
| BD-VEN-03 | Servicio `inventariable=false` | Confirmar OV **sin** salida bodega |
| BD-VEN-04 | Flete `tipoLinea=FLETE` | Línea extra; stub no la manda como recargo SII (si canonical listo: FAIL si recargo) |
| BD-TEN-01 | Empresa A vs B en header | Listados no cruzan documentos |
| BD-RBAC-01 | Solo lectura | GET ok; POST/PUT 403 |
| BD-LEG-01 | URL `/comercial/cotizaciones` | Redirect a Compras; no NP |

---

## 4. Reglas de negocio a validar

| Regla | Dónde |
|---|---|
| Cotización ≠ OV | Menú + `tipo` documento |
| Stock al confirmar OV, no al facturar | Movimientos vs estado factura |
| Afecto OC vs factura | Alerta mismatch registro compra |
| Proforma contratista aprobada inmutable | Fuera de este recorte; plan aprobaciones |
| Periodo cerrado | No emitir / no asiento (si se toca contabilidad en la corrida) |

---

## 5. Matriz de roles (mínima)

| Acción | Digitador compras | Aprobador OC | Digitador ventas | AdminConcepto | Admin |
|---|---|---|---|---|---|
| Crear OC | Sí | Lectura | No | No (salvo módulo) | Sí |
| Aprobar OC (PIN) | No | Sí (si nodo) | No | Según JWT módulos | Super |
| Confirmar OV | No | No | Sí (si no hay cadena) | — | Sí |
| Config grupos/escalas | No | No | No | Sí (re-login) | `admin:*` |
| Emitir factura stub | No | No | Sí | — | Sí |

---

## 6. Criterio de salida piloto (stubs)

- GP-CMP-01–03, GP-VEN-01–03 y BD-STUB-01 en **PASS**.  
- BD-VEN-01 y BD-TEN-01 en **PASS**.  
- GoSocket real = **fuera**; no FAIL de producto.  
- Prod `45.7.229.46` = **BLOCKED** hasta migrate H14.
