# Gestión de proyecto — ERP Almahue

**Fecha:** 2026-08-16 · Documento de título / capstone (ingeniería de software).  
**Producto:** ERP agrícola en estabilización (piloto local con stubs DTE).

---

## 1. Alcance

**Incluye:** multi-empresa (tenant `empresaId`), administración de usuarios/roles, compras (cotización→OC→recepción→registro), ventas (OV→stock→factura stub), insumos/bodega, contratistas (proformas), contabilidad y tesorería en base, aprobaciones por grupos/escalas, ficha cliente/proveedor, billing stub.

**Excluye v1:** mano de obra (Book), maquinaria, niveles de almacenamiento, emisión SII real, SMTP, cobranza como módulo, maestro productor, traspaso gastos próxima temporada, cotización de cliente en Ventas.

---

## 2. Objetivos

1. Dejar un **piloto operable** en local (y exploración en host) sin depender de GoSocket.  
2. Unificar el flujo documental **D11**: Compras cotiza; Ventas vende con OV.  
3. Aislar datos por empresa activa y permisos `modulo:read/write`.  
4. Dejar la integración DTE como **proyecto siguiente**, con contratos de stub ya ejercitados.

---

## 3. Metodología

- Levantamiento: reuniones semanales + minutas (Reu6 > Reu5 > Reu4).  
- Requisitos: Agustín / MJ; Carlos/Sergio en demo = hipótesis.  
- Entrega incremental: código en `ERP/erp_back` y `ERP/erp_front` (repos anidados).  
- Calidad: plan integral v2 + recorte [`plan-de-pruebas-v1.md`](plan-de-pruebas-v1.md); informes en `qa/resultados/` no versionados.  
- Esquema: solo `prisma/migrations/`.  
- Agentes/skills: convenciones en [`reglas-y-skills-sistema.md`](reglas-y-skills-sistema.md).

Fases de entorno: **local stub** → **piloto host con datos de prueba** → **prod con migrate explícito (H14)** → **GoSocket**.

---

## 4. Stakeholders

| Rol | Personas | Interés |
|---|---|---|
| Producto / operación | Agustín, María Jesús (MJ) | Flujos reales, organigrama, Excel maestros |
| Control de gestión | Mario | CC, plan cuentas, AlmaWeb/BI (vecino) |
| Proveedor DTE | Pablo / GoSocket | Credenciales; no bloquean piloto stub |
| Desarrollo | Devint (Carlos, Sergio) | Implementación; no fuente de requisitos |
| IT Almahue | — | SSO Entra, SMTP, red |

---

## 5. Entregables de esta auditoría documental

| Fase | Archivos |
|---|---|
| 0 | `tools/transcript-ollama/`, skill `almahue-transcript-local` |
| 1 | `transcripcion-limpia-v2.md`, `matriz-asis-tobe.md` |
| 2 | `auditoria-integridad-datos.md` |
| 3 | `plan-de-pruebas-v1.md` |
| 4 | este archivo + riesgos + arquitectura + reglas |
