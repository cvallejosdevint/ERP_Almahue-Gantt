<!--
Tono Trello (Almahue ERP) — alinear con mocks tempranos + export Market:
- Lenguaje de negocio/usuario: qué hace la pantalla, para quién, qué se puede hacer.
- Evitar en textos visibles: rutas (/tesoreria/...), seed, mock store, API, fixtures,
  nombres de archivos de repo, jerga de implementación.
- Códigos R2-Cxx / DEC / PEND: solo en el índice de seguimiento (como C-01 en Reu 1),
  no en el cuerpo principal de pantallas Mock.
- Estructura: Actualización arriba + registro/legacy abajo. No borrar comentarios.
-->

**Reunión 2 - Registro demo**

**Fecha:** 23/07/2026
**Objetivo:** Cerrar Ventas + Tesorería; rediseñar Contratistas con referencia AgroSmart; alinear roles, Trello y GoSocket.

---

**CONTRATISTAS (rediseño UX)**

- **R2-C01** Ingreso diario labores (estilo AgroSmart)
  [Ingreso diario labores (contratistas)](https://trello.com/c/kD5faLBC)
  _Pantalla nueva_
- **R2-C02** Precio editable en control diario (sin tarifario rígido previo)
  [Ingreso diario labores (contratistas)](https://trello.com/c/kD5faLBC) · Tarifas de contratista
- **R2-C03** Actividad filtrada por labor seleccionada
  Tarifas de contratista · [Ingreso diario labores (contratistas)](https://trello.com/c/kD5faLBC)
- **R2-C04** Asociación masiva labores → proforma / factura (calce monto)
  [Asociación labores a proforma/factura](https://trello.com/c/TbhPZfMp)
  _Pantalla nueva_
- **R2-C05** N proformas → 1 factura + periodo multi-mes
  Proformas y facturas (contratistas)
  _pedido cerrado como diseño_
- **R2-C06** Cierre mes: asiento facturas por recibir vs costo MO contratada
  Traspaso contable y cierre de mes (contratistas)

**VENTAS / LIBRO**

- **R2-V01** Reutilizar datos al reversar documento (nuevo folio + asientos)
  Libro comercial
- **R2-V02** Confirmación antes de grabar documento proveniente de reversa
  Libro comercial
- **R2-V03** Eliminar utilidad de «Guardar»; solo «Grabar y contabilizar»
  Libro comercial
- **R2-V04** Búsqueda de clientes robusta
  Libro comercial · Clientes

**TESORERÍA**

- **R2-T01** Carga cartola Excel + PDF
  [Carga cartola bancaria](https://trello.com/c/8wHl30Q3)
  _Pantalla nueva (o ampliar Conciliación)_
- **R2-T02** Conciliación diaria/semanal desde cartola (fuente oficial)
  Conciliación bancaria
- **R2-T03** Link directo al asiento cuando hay diferencia
  Conciliación bancaria
- **R2-T04** Reversa selectiva de movimientos (no solo mes completo)
  Conciliación bancaria
- **R2-T05** Anticipos productores — calce parcial sin traspaso manual confuso
  Pagos · [Anticipos productores](https://trello.com/c/iMCx4eXp)
  _Pantalla/flujo nuevo o ampliación Pagos_
- **R2-T06** Diferencia TC bidireccional (CLP↔USD)
  Pagos
- **R2-T07** Control por cobrar/pagar y atraso >90 días (roadmap)
  Pagos · Flujo de caja
  _opcional / fase siguiente_

**ROLES Y PERMISOS**

- **R2-R01** Perfiles Digitador contratistas / Analista / Admin
  Roles y permisos
- **R2-R02** Marcas de lectura/escritura por pantalla
  Roles y permisos
- **R2-R03** Digitador: solo procesos diarios del módulo asignado + empresas visibles
  Roles y permisos · Usuarios

**CATÁLOGOS E INDICADORES**

- **R2-K01** Actualizar Banco Central (automático o manual + hora)
  Monedas · Indicadores Banco Central
- **R2-K02** Centros de costo: contacto encargado + lista de Mario
  Centros de costo
  _PEND-06_
- **R2-K03** Elementos de costo — lista actualizada Mario
  Plan de cuentas
  _PEND-06_

**INTEGRACIONES / PROCESO**

- **R2-G01** GoSocket ~01/09 independiente del ERP; libro compras diferible
  Facturación electrónica (GoSocket)
- **R2-G02** Feedback asíncrono Trello + reunión semanal martes
  _(proceso — esta tarjeta)_

---

**PANTALLAS NUEVAS (Reunión 2 · MockUp + Solicitudes reunión 2 + Fuera Gantt F1 · Reunión 2)**

1. Ingreso diario labores (contratistas) — [Ingreso diario labores (contratistas)](https://trello.com/c/kD5faLBC)
2. Asociación labores a proforma/factura — [Asociación labores a proforma/factura](https://trello.com/c/TbhPZfMp)
3. Carga cartola bancaria (PDF/Excel) — [Carga cartola bancaria](https://trello.com/c/8wHl30Q3)
4. Anticipos productores (calce parcial) — [Anticipos productores](https://trello.com/c/iMCx4eXp)

---

**CORRECCIONES SOBRE PANTALLAS EXISTENTES** _(etiqueta Solicitudes reunión 2 — comentario nuevo; no reemplaza Reu 1)_

- Tarifas de contratista — R2-C02, R2-C03
- Proformas y facturas (contratistas) — R2-C05
- Traspaso contable y cierre de mes — R2-C06
- Libro comercial — R2-V01…V04
- Conciliación bancaria — R2-T02…T04
- Pagos — R2-T05, R2-T06
- Roles y permisos — R2-R01…R03
- Monedas / Indicadores Banco Central — R2-K01
- Centros de costo — R2-K02
- Facturación electrónica (GoSocket) — R2-G01
- Bodegas — niveles de bodega fuera de alcance v1; sin pantalla nueva

---

**DECISIONES FIRMES (DEC-11 a DEC-15)**

- **DEC-11** Contratistas tipo AgroSmart (ingreso diario + asociación masiva)
- **DEC-12** Niveles de almacenamiento fuera de alcance v1
- **DEC-13** Roles Digitador contratistas / Analista / Admin
- **DEC-14** GoSocket 01/09 independiente del ERP
- **DEC-15** Feedback Trello + reunión semanal martes

**PENDIENTES CLIENTE**

- **PEND-01** Afecto/Exento — regla borde
- **PEND-02** Pedido cerrado: varias proformas a una factura / multi-mes
- **PEND-03** → fuera de alcance v1 (niveles de bodega)
- **PEND-04** AlmaWeb / dashboards (Mario, agosto)
- **PEND-05** Cartola Excel+PDF (Agustín)
- **PEND-06** Lista CC + elementos de costo (Mario)

**COMPROMISOS / ACCIONES**

1. Agustín: Excel + PDF cartola
2. Mario: CC + elementos de costo
3. Carlos: link Trello + capturas actualizadas (lunes)
4. Sergio: coordinar GoSocket vs ERP básico
5. Equipo: roles Digitador / Analista / Admin
6. Martes: reunión planificación semanal

**FUERA DE ALCANCE REUNIÓN 2** _(no abrir ahora)_

- Dashboard ejecutivo / Power BI (Mario agosto)
- Maquinaria
- Niveles de almacenamiento
- Integración ERP↔GoSocket libro compras online en septiembre (diferible)
