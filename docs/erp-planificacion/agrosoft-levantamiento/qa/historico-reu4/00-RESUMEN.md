> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; menú Cotizaciones/NP y usuarios `qa.*@`.

# QA Reu4 — 2026-07-31 (stack local)

## Entorno validado

| Pieza | URL / config |
|--------|----------------|
| Front Vite | `http://127.0.0.1:5174` |
| API Nest | `http://127.0.0.1:3001/api/v1` |
| Proxy front → back | `VITE_DEV_API_PROXY=http://localhost:3001` |
| `VITE_API_URL` | `/api/v1` (mismo origen) |
| Postgres | `localhost:5433` / DB `almahue` / schema `erp` |
| Login | `admin@almahue.local` / `Admin123!` · PIN aprobación `4821` |
| Aprobador QA | `qa.aprobador@almahue.local` / `QaTest123!` · PIN `4821` |
| Modo UI | **MODO REAL** (`localStorage almahue-erp-demo-mode=false`) |

**No se usó deploy publicado.** Las instancias previas en :3001/:5174/:5175 se mataron y se levantó Nest (`npm run start:dev`) + Vite (`npx vite --port 5174 --host 127.0.0.1`) de nuevo.

Health (proxy y directo) responden el mismo payload Nest local:

```json
{"status":"ok","service":"erp_back","version":"0.0.1","apiPrefix":"/api/v1","db":"ok"}
```

## Resultados

| Capa | Resultado |
|------|-----------|
| Unitarios back (`npm test`) | **12 suites / 57 tests PASS** |
| GETs únicos de `real/api.ts` vía proxy `:5174` | **52/52 OK** (sin 404/5xx) |
| Smoke UI MODO REAL | Páginas Reu4 llaman `/api/v1/...` y pintan datos de BD |
| Cumplimiento Reu4 (minuta+transcripción) | Ver [`06-MATRIZ-CUMPLIMIENTO-REU4.md`](./06-MATRIZ-CUMPLIMIENTO-REU4.md) + capturas en [`capturas-cumplimiento/`](./capturas-cumplimiento/) |
| Propuesta cobranza R4-18 | [`propuesta-modulo-cobranza.md`](../../docs/erp-planificacion/agrosoft-levantamiento/propuesta-modulo-cobranza.md) |

## Smoke UI (APIs observadas en Network)

| Ruta UI | APIs usadas (ejemplo) | Evidencia |
|---------|------------------------|-----------|
| `/catalogos/centros-costo` | `centros-costo`, `empresas` | Tabla real (DAGGEN ALM…), sin columna Empresa |
| `/comercial/libro` | `documentos`, `cuentas`, `centros-costo` | Totales RCV; sin “Nuevo documento” / “Emitir DTE” en libro |
| `/comercial/emitir` | `clientes`, `cuentas`, `centros-costo` | Wizard emitir en MODO REAL |
| `/contabilidad/balance-8-columnas` | `balance-8-columnas?periodo=2026-07` | Menú Balance de 8 columnas |
| `/tesoreria/cuentas-corrientes` | `cuentas-corrientes?soloConSaldo=1` | Label “Estado de cuenta” |
| `/tesoreria/aging` | `documentos-aging` | Nóminas/aging con sync |
| `/contratistas/proformas` | `proformas-contratista`, `workflows` | UI con acción Reversar/clave |
| `/compras/registro` | `registros-compra`, `ordenes-compra`, `proveedores` | Fila real `OC-2026-001` / `FACT-FIX30-001-EDIT` |

## Cómo reproducir

```powershell
# 1) Matar huérfanos
Get-NetTCPConnection -LocalPort 3001,5174,5175 -State Listen -ErrorAction SilentlyContinue |
  ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }

# 2) Back
cd E:\source\repos\Almahue\ERP\erp_back
npm run start:dev

# 3) Front (otra consola)
cd E:\source\repos\Almahue\ERP\erp_front
npx vite --port 5174 --host 127.0.0.1

# 4) Abrir http://127.0.0.1:5174 → login → botón "Modo real"
```
