# Analisis: SMTP en BD + Monedas (Felipe, 8-9 oct 2026)

Fecha: 2026-10-09. Solo lectura sobre `origin`. Sin checkout a `feat/notificaciones-correo`, sin merge, sin commit.

Base local (coinciden con origin):

- Back `ERP/erp_back` `carlos-dev` = `09f870d`
- Front `ERP/erp_front` `carlos-dev` = `6fc3512`

Rango pedido (cambios NUEVOS de Felipe, no el merge previo de main):

- Back `9f056d6..0d37271` (3 commits)
- Front `0e653b4..c4a0443` (3 commits)

El merge-base de `origin/feat/notificaciones-correo` con `origin/carlos-dev` es el propio HEAD de `carlos-dev`. La rama feat esta adelante por historia extra (incluye `Integrar ... main` / cierre de saldo). **No mergear toda la rama**: reintroduce esa historia. Aplicar solo cherry-pick de los 6 commits de abajo.

---

## 1. Commits (autor FelipeCaves)

### Back (`ERP/erp_back`)

| Hash | Mensaje |
|---|---|
| `103c26f` | feat(notificaciones): agregar modelo y endpoints para config SMTP en BD |
| `df431af` | fix(notificaciones): corregir ruta de importacion de PrismaService |
| `0d37271` | fix(auth): sincronizar migraciones pendientes y tipo distribucionCc en compras |

Archivos (diff `9f056d6..0d37271`): `create-smtp-table.ts`, `polyfill.js`, `prisma/schema.prisma`, `schema.sql`, `scripts/apply-migraciones-pendientes.mjs`, `seed-demo.ts`, `admin.controller.ts`, `admin.service.ts`, `admin.dto.ts`, `compras.service.ts` (1 linea), `smtp-mail.provider.ts`.

### Front (`ERP/erp_front`)

| Hash | Mensaje |
|---|---|
| `20b0cc0` | feat(admin): agregar interfaz grafica para configurar SMTP |
| `952bff3` | refactor(monedas): remover columnas Sync BCCH y Foco Reporte a pedido del cliente |
| `c4a0443` | fix(smtp): corregir componentes y props en ConfiguracionSmtpPage |

Archivos: `App.tsx`, `Sidebar.tsx`, `ConfiguracionSmtpPage.tsx` (nuevo), `MonedasPage.tsx`, `services/api.ts`, `mock/api.ts`, `real/api.ts`.

---

## 2. Que cambia para el usuario

### Administracion > Configuracion de correos (NUEVO)

- Menu: **Administracion** > **Configuracion de correos**.
- Ruta real: `/admin/configuracion-correos`.
- Permiso de ruta: `admin:read` (mismo `ProtectedRoute` que Empresas / Usuarios / Roles). Escritura API: `admin:write`.
- Formulario: Host, Puerto (default 587), Usuario, Contrasena, Nombre remitente (opcional), Email remitente. Boton **Guardar Configuracion**.
- El dato queda por tenant (`empresaId`, unique). Un registro por empresa.
- Hoy el correo de notificaciones (modulo Notificaciones / cola) solo lee `.env` (`SMTP_HOST`, etc.). Con este cambio, si hay fila `activo=true` en BD, esa config gana; si no hay fila, cae a `.env`.
- **No** cubre `OutboundMailService` (PIN, otros envios legacy): ese servicio sigue leyendo solo `.env`. Pueden quedar dos SMTP distintos.

### Parametrizacion > Monedas (ajuste de grilla)

- Menu: **Parametrizacion** > **Monedas**.
- Ruta a fotografiar: `/catalogos/monedas`. `/parametrizacion/monedas` redirige a `/catalogos/monedas`.
- Se quitan de la **tabla** las columnas **Sync BCCH** y **Foco Reporte** (click para marcar moneda principal de reporteria).
- Quedan: Moneda, Nombre, Serie Banco Central, Tipo, Estado, Acciones.
- El modal de alta/edicion **sigue** mostrando el checkbox de sync BCCH (`sincronizarBCCH`). `toggleFocoMoneda` queda en el archivo aunque la columna desaparecio: el foco de reporteria ya no se cambia desde la grilla.

---

## 3. Que cambia tecnico

### Modelo Prisma (no se llama `SmtpConfig`)

Modelo **`ConfiguracionSmtp`** en schema `erp`:

- `id`, `empresaId` (unique + FK `Empresa` cascade), `host`, `port`, `user`, `password` (texto plano), `fromName?`, `fromEmail`, `activo` (default true), timestamps.
- Relacion en `Empresa`: `configuracionesSmtp ConfiguracionSmtp[]`.

**No hay carpeta en `prisma/migrations/` para esta tabla.** El schema Prisma cambia; el historial de migraciones de Prisma no. Eso choca con la regla del repo (schema solo via `prisma/migrations/`) y con el hueco conocido: `erp._prisma_migrations` vacia, **no** `prisma migrate deploy` a ciegas.

DDL ad hoc (fuera de migraciones):

- `schema.sql` en la **raiz** de `erp_back` (solo CREATE de `erp."ConfiguracionSmtp"` + unique + FK).
- `create-smtp-table.ts` en la **raiz**: mismo DDL via `$executeRawUnsafe`. Usa `new PrismaClient()` **sin** adapter pg. En Prisma 7 del proyecto (`@prisma/adapter-pg`) ese script puede fallar al arrancar.

`polyfill.js` (raiz): parche de `util.styleText`. **Ninguna referencia** en package.json ni imports del commit. Ruido.

`seed-demo.ts` (raiz, en el commit de SMTP): **no siembra SMTP**. Crea o reusa primera empresa, proveedor, usuario `demo@almahue.local` con `passwordHash: 'dummy'`, y un `registroCompra` COMPTABILIZADA con `gosocketGlobalDocumentId` dummy. Riesgo si alguien lo corre contra la BD local de Almahue.

### Endpoints

`AdminController` es `@Controller()` (sin prefijo `admin`). Con el global prefix de la API:

- `GET /api/v1/config-correo` - `admin:read` - filtra por `user.empresaId`.
- `PUT /api/v1/config-correo` - `admin:write` - upsert por `empresaId`. Fuerza `activo: true`. No hay campo `activo` en el DTO ni en la UI.

Front real: `http.get('config-correo')` / `http.put('config-correo', input)` (mismo estilo que el resto). Mock: `localStorage` clave `demoSmtpConfig`.

GET y PUT **devuelven `password` en claro**. La pantalla carga esa contrasena en el input.

### Mailer: BD vs `.env`

`SmtpMailProvider` (Notificaciones):

1. `prisma.configuracionSmtp.findFirst({ where: { activo: true } })` - **sin `empresaId`**. Si hay mas de un tenant con SMTP activo, toma uno cualquiera (orden no definido).
2. Si no hay fila: `.env` (`SMTP_HOST` obligatorio para fallback; `SMTP_PORT` default 1025; `SMTP_USER` / `SMTP_PASS`; `SMTP_SECURE` o puerto 465; `SMTP_FROM`).
3. El transporter ya no se arma en el constructor; se arma en cada `sendEmail`.
4. `df431af` corrige el import a `src/prisma/prisma.service.ts` (`../../../../prisma/prisma.service`). El module ya importa `PrismaModule`.

`OutboundMailService` **no se toca**: sigue `.env` y cachea transporter.

### `0d37271` (no es SMTP)

- `compras.service.ts`: al crear la OC hija de cierre de saldo, `distribucionCc: (distHija ?? oc.distribucionCc) as Prisma.InputJsonValue`. El blob padre de este commit **es identico** a `origin/carlos-dev` (`6e0cf77`). Es un cast de tipos sobre el codigo de Jose; no cambia el negocio.
- `scripts/apply-migraciones-pendientes.mjs`: el script local de carlos-dev solo tenia `precioCompra` e `IF EXISTS` drop de `ConfigContableSii`. El commit mete DDL extra (idempotente con IF NOT EXISTS) de:
  - `LibroComprasSyncMeta`
  - columnas OC `ocPadreId`, `cerradaAt`, `cierreSaldoMotivo` + FK
  - columnas match/validacion en `RegistroCompra`
  - enum `TipoGrupoAprobacion` + columna `tipo` en `GrupoAprobacion`
  - `DelegacionAprobacion.grupoIds`
  - flags empresa `permiteDevolucionProveedor` / `recibeInsumosConGuia` **con UPDATE por RUT** (77.032.639-7 vs 77.032.638-9)
  - tabla `GuiaInsumoRecibida` + FKs
  - drop `ConfigContableSii`

**Ese script no crea `ConfiguracionSmtp`.** Correrlo no alcanza para SMTP. Correrlo si aplica (o re-aplica) DDL de cierre de saldo / libro / grupos / guias y **reescribe flags de empresa por RUT**.

---

## 4. Riesgos

### Critical

1. **Secretos SMTP en BD y en API.** Password en texto plano, GET/PUT la exponen a cualquier `admin:read` / `admin:write`. Logs de Prisma/Nest pueden filtrarla. No hay cifrado ni campo omitido en respuesta.
2. **Mailer sin tenant.** `findFirst({ activo: true })` puede enviar con el SMTP de otra empresa. Viola el filtro `empresaId`.
3. **No usar `prisma migrate deploy`.** No hay migracion Prisma de `ConfiguracionSmtp`. Deploy a ciegas sigue prohibido (`erp._prisma_migrations` vacia).
4. **`scripts/apply-migraciones-pendientes.mjs` no es el camino SMTP** y, si se corre entero, mezcla DDL de Jose + UPDATE de flags por RUT. No es `migrate deploy`, pero muta schema y datos. No correrlo "por las dudas" al traer SMTP.
5. **`seed-demo.ts`.** Usuario dummy, empresa `EMP-DEMO` / RUT 77.777.777-7, factura contabilizada. No ejecutarlo en la BD de trabajo.

### High

6. Tabla SMTP solo via `schema.sql` / `create-smtp-table.ts` en raiz, fuera de `prisma/migrations/`. Tras cherry-pick hay que `prisma generate` y crear la tabla a mano. Si no: el back no arranca o pega al consultar `configuracionSmtp`.
7. `create-smtp-table.ts` sin adapter Prisma 7: puede no servir en local. Preferir SQL (`schema.sql`) contra la BD, no el ts.
8. Dos canales de correo: UI nueva no configura PIN/`OutboundMailService`. El usuario puede creer que "Configuracion de correos" cubre todo el ERP.
9. Working tree local back: `compras.service.ts` ya tiene diff sucio vs `origin/carlos-dev` (no es el commit de Felipe). Cherry-pick de `0d37271` sobre working tree sucio **si** choca. Hay que stash o descartar lo local de ese archivo antes.

### Medium

10. GET pinta la password en el form; PUT siempre `activo: true` (no se puede apagar desde UI).
11. Menu SMTP sin `allowAdminConcepto` propio (el padre Administracion si lo tiene). Ruta exige `admin:read`. Verificar AdminConcepto vs ROL-1.
12. Monedas: se pidio quitar columnas; el modal sigue con Sync BCCH; foco reporteria queda en API/modelo sin control en grilla.
13. `schema.sql` y scripts sueltos en raiz ensucian el paquete y se pueden copiar a prod por error.
14. `polyfill.js` muerto.
15. Tras generate, hay que reiniciar el API. Front: ruta nueva no esta en catalogo de pantallas (no se toco seed de pantallas).

### Low / conflicto Jose

16. Cast `distribucionCc` en cierre de saldo: en `origin/carlos-dev` limpio el hunk aplica. No cambia comportamiento. Si TypeScript local ya compilaba, el commit es ruido en el archivo de Jose.
17. Cherry-pick **no** deberia listar conflictos de contenido en limpio: los blobs padre de `103c26f` / `0d37271` **coinciden** con `origin/carlos-dev` (schema, admin.controller, smtp-mail.provider, apply-script, compras).

Archivos de conflicto **esperados solo si el arbol no esta limpio**:

- Back: `src/modules/compras/compras.service.ts` (working tree local ya modificado).
- Front: `src/features/admin/ConfiguracionSmtpPage.tsx` si se aplica `c4a0443` **antes** de `20b0cc0` (el archivo no existe). Orden: crear pagina, luego el fix.

Si alguien mergea toda `feat/notificaciones-correo` en vez de cherry-pick: reaparecen commits de main / notificaciones / cierre de saldo (back ~11 commits unicos, front ~9). Evitar.

---

## 5. Pantallas a fotografiar (antes / despues)

Usar Playwright a ventana completa (menu + contenido). No guardar SMTP real ni documentos.

| # | Cuando | Menu | Ruta exacta | Que debe verse |
|---|---|---|---|---|
| 1 | ANTES | Administracion (abierto) | p.ej. `/admin/usuarios` o `/admin/roles` | Hijos: Empresas, Plantilla documentos, Usuarios, Roles y permisos, Reglas de aprobacion. **Sin** "Configuracion de correos". |
| 2 | ANTES | Parametrizacion > Monedas | `/catalogos/monedas` | Grilla con columnas Sync BCCH y Foco Reporte. |
| 3 | DESPUES | Administracion > Configuracion de correos | `/admin/configuracion-correos` | Formulario SMTP vacio o con datos de prueba (no capturar password real). Item nuevo en el menu. |
| 4 | DESPUES | Parametrizacion > Monedas | `/catalogos/monedas` | Sin Sync BCCH ni Foco Reporte. Resto igual. Optional: abrir "Nueva moneda" y anotar que Sync BCCH sigue en el modal. |

`/parametrizacion/monedas` no es la pantalla viva (redirect).

---

## 6. Como aplicar en local sin romper `carlos-dev`

No: checkout de `feat/notificaciones-correo`, no merge, no `prisma migrate deploy`, no `seed-demo.ts`, no correr el apply-script entero "para SMTP".

Previo: `git status` limpio en cada nested repo. En back, stash o revertir el diff local de `compras.service.ts`.

### Back (cwd `ERP/erp_back`, branch `carlos-dev`)

```text
git cherry-pick 103c26f df431af 0d37271
```

Orden obligatorio: el fix de import (`df431af`) va encima del feat SMTP. El tercero es el de compras + apply-script.

Si se quiere **cero toque** al cierre de saldo de Jose, alternativa (no es el 3+3 literal): cherry-pick solo `103c26f` `df431af` y, de `0d37271`, no traer el script ni compras. SMTP no depende de ese commit.

Despues del cherry-pick SMTP:

1. `npx prisma generate` (o el script del package) para que exista `prisma.configuracionSmtp`.
2. Crear la tabla con SQL de `schema.sql` contra el schema `erp` (psql / cliente). No `migrate deploy`.
3. No commitear `.env`. No hace falta poner SMTP en `.env` si se va a probar la UI (BD gana).
4. Reiniciar API `:3001`.

### Front (cwd `ERP/erp_front`, branch `carlos-dev`)

```text
git cherry-pick 20b0cc0 952bff3 c4a0443
```

`c4a0443` exige que `ConfiguracionSmtpPage.tsx` ya exista (`20b0cc0`). `952bff3` (Monedas) es independiente; puede ir en medio o al final.

### Si hay conflicto

En limpio vs `origin/carlos-dev`: no se espera. Si aparece:

| Archivo | Por que |
|---|---|
| `src/modules/compras/compras.service.ts` | Working tree sucio o cherry-pick sobre otro HEAD. Resolver dejando el cast `as Prisma.InputJsonValue` sin revertir `ocPadreId` / cierre de saldo. |
| `scripts/apply-migraciones-pendientes.mjs` | Si el script local ya se edito. Preferir no ampliar el script en el mismo PR que SMTP. |
| `src/features/admin/ConfiguracionSmtpPage.tsx` | `c4a0443` sin `20b0cc0`. Abortar y respetar el orden. |
| `prisma/schema.prisma` / `admin.controller.ts` | Solo si `carlos-dev` local no es `09f870d`. |

Abortar cherry-pick: `git cherry-pick --abort` (no reset duro salvo pedido explicito).

---

## 7. Veredicto para aplicar

- Producto: pantalla Admin SMTP + quitar dos columnas de Monedas. Pedido de cliente en Monedas esta a medias (modal y foco).
- Tecnico SMTP usable en local con cherry-pick 5 commits de producto (`103c26f`, `df431af`, `20b0cc0`, `c4a0443`, `952bff3`) + DDL manual de `ConfiguracionSmtp` + `prisma generate`.
- `0d37271` es ajeno a SMTP; el apply-script es el mayor riesgo operativo junto a secretos y falta de `empresaId` en el mailer.
- No mergear `origin/feat/notificaciones-correo`.
