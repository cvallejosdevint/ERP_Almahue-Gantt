# Matriz de riesgos

**Fecha:** 2026-08-16 · ERP Almahue (piloto stub, pre-GoSocket).  
**Actualización:** refactor relacional inventario + flete canónico desplegado en **local** y cubierto con tests unitarios (insumos, stock-bodega, canonical, comercial-ov) sobre el código y semilla del piloto.

| ID | Tipo | Riesgo | Impacto | Prob. | Estado | Mitigación |
|---|---|---|---|---|---|---|
| R1 | Técnico | Integración GoSocket se trata como “ya está” por demo | Alto (folios SII, legal) | Media | Abierto | Stub obligatorio; no emitir SII sin credenciales; proyecto billing aparte |
| R2 | Técnico | Canonical DTE manda flete como recargo SII (D17) | Bajo | Baja | **Mitigado** | `canonical-builder` serializa flete como **línea de detalle** (`tipoLinea` FLETE / RECARGO→FLETE). Stub local; test `emite flete como línea de detalle, no como recargo SII`. Revalidar solo si se reabre HTTP partner. |
| R3 | Técnico | Concurrencia: dos OV sobre el mismo stock | Alto | Media | Abierto | Confirmación transaccional por `(empresaId, insumoId, bodegaId)`; test de carrera |
| R4 | Técnico | Movimientos de bodega por **nombre** no por id | Bajo | Baja | **Mitigado** | U1/U2 cerrados: `bodegaId`/`insumoId` obligatorios; `resolveBodegaId` solo por id+tenant. Migración `20260816220000_movimiento_bodega_fks`. UI movimientos envía FKs. Probar de nuevo tras `prisma migrate deploy` local con seed. |
| R5 | Técnico | Dos modelos de guía (`GuiaDespacho` vs doc GUIA) | Medio | Media | Abierto | Una verdad de folio |
| R6 | Técnico | JWT AdminConcepto sin re-login | Medio | Alta | Abierto | Documentar + QA BD-APB-03; no “ya asigné y no veo” |
| R7 | Técnico | Tenant leak entre empresas | Alto | Baja (si guards) | Abierto | Filtro `empresaId` en todo query; BD-TEN-01 |
| R8 | Técnico | Flag `comercialRequiereAprobacion=false` en piloto vs narrativa demo | Medio | Alta | Abierto | Decisión explícita de reunión; no SKIP silencioso |
| R9 | Operativo | Prod sin migrate OV/stock (H14) | Alto | Alta | Abierto | No demo OV en `45.7.229.46` hasta deploy; incluir migrate de FKs bodega |
| R10 | Operativo | Excel MJ (plan cuentas, cartola, AlmaWeb) no llega | Medio | Media | Abierto | Piloto con seed; no bloquear stub DTE |
| R11 | Operativo | SMTP ausente (PIN por correo) | Bajo | Alta | Abierto | PIN en perfil; H9 diferido |
| R12 | Operativo | Usuarios compartidos / empresa activa incorrecta | Medio | Media | Abierto | Header visible; capacitación; no compartir login |
| R13 | Operativo | Hipótesis Carlos/Sergio tomadas como requisito | Alto | Media | Abierto | Rule reuniones: minuta + código |
| R14 | Seguridad | Secretos en git (`.env`, JWT, dumps) | Alto | Baja | Abierto | `.gitignore`; no commit `ERP/.deploy/` |
| R15 | Datos | Modo demo vs API real | Medio | Media | Abierto | Evidencia QA solo MODO REAL |

No se mitiga “mermas”: el concepto no forma parte del negocio.
