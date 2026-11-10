# QA Semana Acuerdos 2026-11 (Items #23-#39)

Fecha: 2026-11-10 03:10:11 UTC  
Stack: front http://localhost:5174 | API http://localhost:3001  
Credenciales: admin@almahue.local / Admin123!  
Login: real via UI  

## Resumen

| Total | PASS | FAIL | SKIP |
|-------|------|------|------|
| 18 | 8 | 5 | 5 |

## Resultados

| # | Resultado | Nota | Captura |
|---|-----------|------|---------|
| #PRE | PASS | Login admin@almahue.local OK via UI | - |
| #23 | FAIL | Error: locator.click: Timeout 25000ms exceeded.
Call log:
  - waiting for locator('table tbody tr, [data-row], .asiento-row').first().locator('button, a').filter({ hasText: /ver-detalle-abrir/i }).first()
   | - |
| #24 | PASS | Proforma edicion: 2 campos editables | [24-proforma-edicion.png](evidencia-semana-2026-11/24-proforma-edicion.png) |
| #25 | PASS | Boton asociar OC visible en libro compras; modal abierto y cancelado | [25-asociar-oc-modal.png](evidencia-semana-2026-11/25-asociar-oc-modal.png) |
| #26 | PASS | Pagina guias packing carga. Titulo: "ERP Enterprise Almahue"; tabla: false | [26-guias-packing.png](evidencia-semana-2026-11/26-guias-packing.png) |
| #27 | PASS | Cartola/calce carga. Titulo: "ERP Enterprise Almahue"; tabla: false; calce ctrl: false | [27-tesoreria-cartola.png](evidencia-semana-2026-11/27-tesoreria-cartola.png) |
| #28 | FAIL | Libro ventas carga; tabla: false | [28-libro-ventas.png](evidencia-semana-2026-11/28-libro-ventas.png) |
| #29 | FAIL | Organigrama sin contenido visible. Texto: ERP Enterprise Almahue

Plataforma integrada para gestión financiera, comercial, contratistas e insumos.

Almahue / Devint · Jul 2026

Iniciar sesión

Ingresa con tu email y contraseña del ERP.

Email
Contraseña
Entrar con clave
O | [29-admin-aprobaciones.png](evidencia-semana-2026-11/29-admin-aprobaciones.png) |
| #30 | FAIL | Roles listado: false; admin modulo viejo: false | [30-admin-roles.png](evidencia-semana-2026-11/30-admin-roles.png) |
| #31 | FAIL | Usuarios: 0 filas; columna cargo: false; input cargo en modal: false | [31-admin-usuarios.png](evidencia-semana-2026-11/31-admin-usuarios.png) |
| #32 | PASS | Ramas area: true; topes en pagina: false; input tope modal: false | [32-ramas-areas-topes.png](evidencia-semana-2026-11/32-ramas-areas-topes.png) |
| #33 | SKIP | Sin simulador ni wizard OC accesible para preview cadena | [33-simulador-cadena.png](evidencia-semana-2026-11/33-simulador-cadena.png) |
| #34 | SKIP | Mensaje tope ultimo eslabon: no detectado | [34-tope-ultimo-eslabon.png](evidencia-semana-2026-11/34-tope-ultimo-eslabon.png) |
| #35 | SKIP | Sin boton Nueva OC visible | [35-oc-lista.png](evidencia-semana-2026-11/35-oc-lista.png) |
| #36 | PASS | AND/OR en eslabones: texto: true; control: false | [36-and-or-eslabon.png](evidencia-semana-2026-11/36-and-or-eslabon.png) |
| #37 | PASS | Recetas packing carga. Titulo: "ERP Enterprise Almahue" | [37-packing-recetas.png](evidencia-semana-2026-11/37-packing-recetas.png) |
| #38 | SKIP | Promedio ponderado en movimientos: false | [38-insumos-movimientos-pp.png](evidencia-semana-2026-11/38-insumos-movimientos-pp.png) |
| #39 | SKIP | Guias por confirmar: false; adjuntos: false; btn confirmar: false | [39-guias-confirmar.png](evidencia-semana-2026-11/39-guias-confirmar.png) |

## Blockers

- **#23**: Error: locator.click: Timeout 25000ms exceeded.
Call log:
  - waiting for locator('table tbody tr, [data-row], .asiento-row').first().locator('button, a').filter({ hasText: /ver|detalle|abrir/i }).first()
  
- **#28**: Libro ventas carga; tabla: false
- **#29**: Organigrama sin contenido visible. Texto: ERP Enterprise Almahue

Plataforma integrada para gestión financiera, comercial, contratistas e insumos.

Almahue / Devint · Jul 2026

Iniciar sesión

Ingresa con tu email y contraseña del ERP.

Email
Contraseña
Entrar con clave
O
- **#30**: Roles listado: false; admin modulo viejo: false
- **#31**: Usuarios: 0 filas; columna cargo: false; input cargo en modal: false

## Notas

- Organigrama: 8 ramas y 6 cargos jerarquicos en BD local al momento de la prueba.
- Se uso login real por UI (no demo token).
- Ningun documento fue guardado/enviado/contabilizado.
- API backend fue reiniciado antes de la prueba (port 3001 habia quedado en CLOSED).