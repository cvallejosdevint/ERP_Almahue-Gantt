# Contraste: apuntes `revision en cliente.txt` vs reunion 26/10/2026

**Objetivo:** alinear tus notas del escritorio con lo que dice la transcripcion disponible (audio `12.33`) y marcar huecos hasta tener el audio `15.20`.

| Documento | Ruta |
|---|---|
| Apuntes consultor | `C:\Users\c\Desktop\revision en cliente.txt` |
| Minuta consolidada | [`docs/reuniones/minutas/reunion-2026-10-26-presencial.md`](../reuniones/minutas/reunion-2026-10-26-presencial.md) |
| Transcripcion audio 1 | [`docs/reuniones/transcripciones/transcripcion-2026-10-26-presencial.md`](../reuniones/transcripciones/transcripcion-2026-10-26-presencial.md) |
| Transcripcion audio 2 | Pendiente (archivo corrupto) |

Leyenda: **OK** = coincide; **+TX** = refuerzo en transcripcion; **SOLO apuntes** = no aparece en audio 1; **MATIZ** = mismo tema, distinto enfasis; **COD** = ya tocado en codigo local (referencia rapida).

---

## Parametrizacion

| # | Apunte consultor | Evidencia reunion / minuta | Estado |
|---|---|---|---|
| P1 | Plan de cuentas: N CC, N elementos, N areas por cuenta | MJ aprueba UI tres listas y filtro al usar cuenta `[24:53]`-`[25:59]` | Falta BD/UI plan (0 vinculos en prod hoy) |
| P2 | Columna cantidad de cuentas en CC, elemento, area | MJ pide contador + detalle `[29:17]`-`[29:59]` | No implementado |
| P3 | Usuarios: dos empresas en selector | Apunte (ok) | **COD** EmpresaSelector prod 26/10 |
| P4 | Bancos: varias cuentas, moneda cada una | **SOLO apuntes** (posible audio tarde) | Revisar modulo parametrizacion bancos |
| P5 | Historial parametrizaciones roto | **SOLO apuntes** | Bug a investigar |
| P6 | Honorarios: registro/recepcion, no emision; tipo en proveedor | **SOLO apuntes** | Sin evidencia TX1 |
| P7 | Nota de cobro = rendicion; compras + contabilidad | **SOLO apuntes** | Sin evidencia TX1 |
| P8 | OPB embarcador, facturas export/import | **SOLO apuntes** | Sin evidencia TX1 |

## Contabilidad

| # | Apunte consultor | Evidencia reunion / minuta | Estado |
|---|---|---|---|
| C1 | TC en pesos al contabilizar | **SOLO apuntes** (TX1 habla TC en carga masiva CLP/USD) | MATIZ |
| C2 | Motivo cierre/apertura periodo | **SOLO apuntes** | PeriodoContableEvento existe en schema; validar UI |
| C3 | Correlativo con nomenclatura de tipo | TX1 carga masiva: correlativo + tipo `[09:59]` | **MATIZ** manual OC/asientos distinto |
| C4 | Detalle asiento 3 columnas; botones glosa | **SOLO apuntes** | |
| C5 | Adjuntar RC en comprobante | **SOLO apuntes** | |
| C6 | Tipos: apertura, egresos, ingresos, proveedores, traspasos, ventas | Apuntes; traspaso citado en Agrosoft `[10:03]` | **COD** combo nuevo comprobante 26/10 |
| C7 | Correlativo: pide tipo si manual; auto si origen | **SOLO apuntes** | |
| C8 | Carga masiva vista Agrosoft | TX1 extenso `[09:42]`-`[16:57]` | Parcial / distinto en ERP |
| C9 | Nuevo comprobante -> contabilizado directo | **SOLO apuntes** | Hoy permite Pendiente |
| C10 | TC faltante: ingreso manual + aviso admin | **SOLO apuntes** | Parcial aviso TC en otros modulos |
| C11 | CC por departamento + totalizados | **SOLO apuntes** | |
| C12 | Presupuesto: alerta % en totalizados | TX1 presupuesto e imputacion `[24:37]`-`[28:51]`; % no dicho | Falta alerta % |
| C13 | Libro mayor/diario filtros mes/ano; todos = ano actual | **SOLO apuntes** | |
| C14 | Ancho campo todas las cuentas mayor | **SOLO apuntes** | |
| C15 | Balance 8 col y EERR solo ano actual | **SOLO apuntes** | |
| C16 | Mayor puede ano a ano | **SOLO apuntes** | |
| C17 | Situacion financiera anos anteriores | **SOLO apuntes** | |
| C18 | Utilidad ejercicio desde EERR al 31/12 a situacion financiera | **+TX** MJ `[00:19]`-`[02:03]` | **Hueco reportes** |
| C19 | Validar resultado ejercicio vs acumulado en reporteria | **+TX** mismo bloque MJ | Accion reportes |
| C20 | Data historica con Mario | Apuntes + oferta MJ archivos `[21:18]` | Operativo |

## Orden de compra

| # | Apunte consultor | Evidencia reunion / minuta | Estado |
|---|---|---|---|
| O1 | Orden item: cuenta, CC, elemento | MJ `[44:04]`-`[44:13]` | **COD** orden columnas 26/10; falta bloqueo sin cuenta |
| O2 | Solicitar al admin CC/elemento no asociado | MJ `[44:13]`-`[45:24]` | No implementado |
| O3 | CC/elemento por linea; multiples lineas | MJ prefiere lineas `[47:25]`; software 50/50 `[33:42]` | **MATIZ** vs boton + en misma linea |
| O4 | Ver detalle estilo flujo de caja | MJ `[55:17]`-`[55:29]`, estado cuenta `[49:41]` | No implementado |
| O5 | PDF proveedor sin dimensiones | MJ `[51:11]`-`[55:45]` | No implementado |

---

## Resumen ejecutivo

1. **Audio manana (`12.33`)** cubre fuerte: **reportes (resultado ejercicio/acumulado)**, **carga masiva Agrosoft**, **plan N:N**, **presupuesto/imputacion**, **OC (orden campos, lineas, solicitud admin, detalle, PDF)** y un tramo de **cartola**.
2. **Tus apuntes** agregan bloques que **no salen en audio 1**: honorarios, nota de cobro, OPB, bancos multi-cuenta, historial parametros, comprobante auto-contabilizado, RC, 3 columnas asiento, filtros mayor/balance, alerta % presupuesto. Es probable que esten en **`15.20.m4a`** o en otra parte de la reunion no grabada.
3. **Audio tarde:** no transcrito; hay que **re-copiar** el M4A desde el celular (ver README en `medios/whisper-local/2026-10-26-presencial-tarde/`).
4. **Ya en codigo (26/10):** tipos de comprobante nuevos; selector dos empresas; OC elemento habilitado con catalogo (prod sin N:N en BD aun).

## Siguiente paso sugerido (antes de codificar)

1. Reenviar `15.20.m4a` valido y completar transcripcion tarde.
2. Cruzar de nuevo este contraste (marcar filas SOLO apuntes que pasen a OK).
3. Priorizar con MJ: **N:N plan de cuentas en prod**, **carga masiva**, **reportes resultado ejercicio**, **OC solicitud admin + detalle + PDF**.
