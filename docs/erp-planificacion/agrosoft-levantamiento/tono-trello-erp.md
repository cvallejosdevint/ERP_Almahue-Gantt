# Tono Trello — Almahue ERP

Aplica a **Reunión 1 y Reunión 2** (índices + pantallas Mock).

Referencias: export Market (`IGkpfaoD - almahue-market.json`) + mocks tempranos del board ERP (`backups/trello-wixKcrP0-2026-07-22_1401.json`).

## Reglas

1. **Negocio primero.** Qué hace la pantalla, para quién, qué se puede hacer.
2. **Sin jerga de implementación** en descripciones/comentarios visibles: rutas (`/tesoreria/...`), `seed`, mock store, API, fixtures, paths de repo, ASP.NET, etc.
3. **Bullets cortos** en español natural (estilo Observaciones Market / mocks tempranos).
4. **Códigos de seguimiento** (C-xx / P-xx / R2 / DEC / PEND): en el **índice** o en una cabecera/registro breve; no saturar el cuerpo principal de cada Mock.
5. **Estructura:** Actualización arriba + registro/legacy abajo. No borrar comentarios; si un Update quedó técnico, editar ese Update o añadir uno nuevo claro.

## Ejemplo antes / después (pantalla Mock)

**Antes (técnico):**
> Mock ERP demo en `/contratistas/ingreso-diario`.  
> **Ruta:** `/contratistas/ingreso-diario` · R2-C01 / DEC-11

**Después (negocio):**
> Pantalla de ingreso diario de labores de contratista. El digitador registra, día a día, la mano de obra por empresa, fecha, centro de costo o cuartel, labor y tipo de pago, pudiendo ajustar el precio según la situación del día.  
> Para quién: digitadores de contratistas.  
> Qué se puede hacer: registrar varias labores del día; editar precio al ingreso; dejar listo para asociar a proforma o factura.

**Antes (Reu1, stub):**
> **Fuera Gantt F1** · Reunión 1 · P-07

**Después (Reu1, negocio):**
> Pantalla de recepción de orden de compra. Aquí se confirma lo recibido y se aplica el tipo de cambio efectivo.  
> Para quién: quien recepciona compras.  
> Qué se puede hacer: recepcionar una OC; ver el TC; dejar lista la factura.

## Scripts

- `suavizar-tono-trello-reu1.py` — índice Reu1 + mocks etiqueta Solicitudes reunión 1 (Gantt F1 + pantallas nuevas).
- `suavizar-tono-trello-reu2.py` — reescribe índice + N1–N4.
- `crear-pantallas-nuevas-reunion2-trello.py` / `crear-tarjeta-reunion2-trello.py` — generan textos en este tono.
- `crear-tarjeta-reunion1-indice.py` / `reunion1-registro-trello-template.md` — índice Reu1 (códigos C/P/I/K en el registro).
