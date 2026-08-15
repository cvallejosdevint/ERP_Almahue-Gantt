# Veredicto final — Pipeline QA integral local (15/08/2026)

**Rol:** Encargado de proyecto (consolidado post-Olas A/B/C)  
**Audiencia:** Steering piloto Almahue

---

## Resumen ejecutivo

| Pregunta | Respuesta |
|---|---|
| ¿Piloto local validado? | **Sí — GO demo** con seed `demo-propuesta` y guion `DEMO-PROPUESTA-LOCAL.md` §4 |
| ¿Prod listo? | **No-Go** — H14 + E2E-008 pendientes |
| ¿Defectos P0/P1 abiertos? | **0** en alcance ejecutado |
| ¿Certificación 90 % plan v2? | **~75–80 %** trazable (HEREDADO + SKIP + opcional §4.1 parcial) |

**Veredicto global local:** **`PIPELINE_LOCAL_CERRADO`**

---

## Oleadas

| Oleada | Informe | Veredicto | Highlights |
|---|---|---|---|
| **A** | `integral-erp-ola-a` + retest | LISTO_OLA_B | Smoke, Emitir, OV aprobación, billing stub, match 3 vías |
| **B** | `integral-erp-ola-b` + TES-015 retest | LISTO_OLA_C | PAR, INV, CTR, CNT, TES, ADM, FIC |
| **C** | `integral-erp-ola-c` | PIPELINE_LOCAL_CERRADO | E2E-001–006 golden ALM-* |

Revisiones: `revision-ola-a-cierre.md`, `revision-ola-b-cierre.md`, `revision-ola-c.md`.

---

## Demo cliente — guion recomendado (15 min)

1. Inventario / bodegas Almahue  
2. Compras: `ALM-COT-001` → OC → aprobación Jorge PIN  
3. Ventas: OV → aprobación → stock → Emitir  
4. Factura `ALM-FAC-101` → stub DTE  
5. (Opcional) Centralización preview + tesorería pagos  

**Evitar:** prod remoto, E2E-007 greenfield, casos destructivos ADM/CNT-007.

---

## Pendientes (no bloquean demo local)

| ID | Tema | Dueño |
|---|---|---|
| **H14 / E2E-008** | Deploy prod + smoke | Devint + Cliente |
| **D4** | Narrativa flag `comercialRequiereAprobacion` en reunión | Cliente |
| **E2E-007** | Greenfield sin seed (P2) | Devint |
| **Opcional §4.1** | ~28 casos CMP/VEN/RBAC/BIL restantes | Devint |
| **Capturas** | Video/carpeta evidencias por caso P0 | Devint |

---

## Decisión steering

| Entorno | Go/No-Go |
|---|---|
| **Local demo** | **GO** |
| **Piloto prod** | **No-Go** |
| **Certificación integral 90 %** | **Pendiente** — opcional §4.1 + E2E-007 |

---

*Consolidado tras Olas A, B, C del 15/08/2026. Fuente canónica de estado: `qa/resultados/README.md`.*
