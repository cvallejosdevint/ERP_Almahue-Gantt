# Validación PDF Enterprise vs Gantt v3

Fecha: 2026-07-10  
Fuentes: `ERP-Contable-Financiero-Enterprise.pdf`, `Modulo-Comercial-Documento-Tecnico-Enterprise.pdf`  
Plan: `tools/erp_gantt_tasks.py` (**85 tareas**, 298 persona-día)

## Resumen ejecutivo

| Categoría | Estado |
|-----------|--------|
| Módulos funcionales v1 (PDF) | **Cubierto** (10 dominios + transversales) |
| Roadmap 5 fases (PDF global) | **Alineado** F0–F7 |
| Módulo comercial (PDF detallado) | **Mayormente cubierto** — 4 gaps funcionales |
| GoSocket / DTE | **Cubierto** |
| DevOps / QA enterprise | **Parcial** — faltan tareas explícitas |
| Stack técnico (MUI, Redux, TypeORM) | **Desviación documentada** — no bloquea planificación funcional |
| Auditoría transversal | **Gap** — implícito, sin tarea dedicada |

**Conclusión:** El plan cubre el alcance funcional principal. Tras esta validación se agregan **8 tareas** para cerrar gaps explícitos del PDF (auditoría, notas crédito, email/import, hardening QA, observabilidad).

---

## 1. PDF Global — Módulos funcionales

| Requisito PDF | Tarea(s) Gantt | Estado |
|---------------|----------------|--------|
| Administración & Seguridad (usuarios, roles, RBAC, empresas) | DEF-CORE, CORE-*, MOCK-CORE | OK |
| Sucursales multiempresa | DEF-CORE (parcial), CAT | **Parcial** → DEF-SUCURSALES |
| JWT + refresh + sesiones | CORE-BACK | OK (blacklist Redis: ver stack) |
| Contratistas & Insumos | DEF-INSUMOS, INS-*, MOCK-INSUMOS | OK |
| Contratos comerciales contratistas | INS-BACK (nombre genérico) | **Parcial** → ampliar INS-BACK |
| Comercial & Facturación | DEF-COM, COM-*, MOCK-COM-* | OK |
| GoSocket PFE (no motor SII propio) | DEF-GOSOCKET, INT-GOSOCKET-SPIKE, INT-* | OK |
| Contabilidad (plan cuentas, asientos, CC) | DEF-CONT, CONT-* | OK |
| Tesorería (flujo caja, pagos, conciliación) | DEF-TES, TES-* | OK |
| Presupuestos & seguimiento | DEF-PRES, PRES-* | OK |
| Dashboard ejecutivo KPIs | DEF-REP, REP-*, MOCK-REP, MOCK-COM-DASH | OK |
| Workflow aprobaciones | DEF-WF, WF-* | OK |
| Reportes PDF/Excel/CSV | REP-BACK | OK |
| Auditoría / trazabilidad total | — | **Gap** → DEF-AUDIT, AUDIT-BACK |
| CI/CD Docker NGINX | INF-02, INF-07, DEP-01 | OK |
| Monitoreo, logs JSON, DR/BCP | DEP-01 (parcial) | **Parcial** → INF-OBS |
| Performance / pruebas carga | QA-02 (parcial) | **Parcial** → QA-LOAD, QA-SEC |

---

## 2. PDF Global — Roadmap oficial

| Fase PDF | Contenido | Fase Gantt |
|----------|-----------|------------|
| Fase 1 — Base | Docker, JWT, Admin, CI/CD | F2 |
| Fase 2 — Core Financiero | Contab, Tesorería, Presupuestos, Contratistas/Insumos | F3 |
| Fase 3 — Comercial & DTE | Comercial, GoSocket, Workflow | F4 + F5 + F6 |
| Fase 4 — Inteligencia | Dashboard, reportes, export | F7 REP-* |
| Fase 5 — Hardening | Performance, carga, seguridad, UAT | F7 QA-* + nuevas |

---

## 3. PDF Módulo Comercial — Detalle

| Requisito PDF | Tarea(s) Gantt | Estado |
|---------------|----------------|--------|
| Clientes (CRUD, crédito, listas precio, import Excel) | DEF-COM, COM-BACK, MOCK-COM-CLI | **Parcial** import → COM-BACK |
| Prospectos / leads / conversión | DEF-COM, COM-BACK, MOCK-COM-CLI | OK |
| Cotizaciones (versionado, vigencia, estados) | COM-BACK, MOCK-COM-LIBRO | OK |
| Envío cotización email + PDF | — | **Gap** → COM-EMAIL |
| Órdenes / NP / conversiones | COM-BACK, MOCK-COM-LIBRO | OK |
| Notas de crédito | — | **Gap** → incluido en COM-NC |
| Motor común `commercial_documents` | DEF-COM, COM-BACK | OK |
| Libro Comercial (filtros, acciones, export) | COM-FRONT, MOCK-COM-LIBRO | OK |
| Workflow por monto/tipo/escalamiento | DEF-WF, WF-* | OK |
| APIs `/api/v1/customers`, `/documents`, `/convert`, `/invoice` | DEF-API, COM-BACK, INT-BACK | OK |
| ElectronicInvoiceProvider / GoSocket | DEF-GOSOCKET, INT-* | OK |
| Resiliencia (retry, circuit breaker, timeout) | INT-BACK | OK |
| Dashboard KPIs comercial | MOCK-COM-DASH, COM-FRONT | OK |
| Contabilización al cierre flujo comercial | INT-CONT-BACK | OK |
| RBAC roles (Admin, Supervisor, Vendedor, Lectura) | DEF-CORE, CORE-BACK | OK |
| audit_logs inmutable | — | **Gap** → AUDIT-BACK |
| Integration log / email log | — | **Gap** → AUDIT-BACK |
| QA: Jest 80%, Supertest, k6, OWASP ZAP | QA-01 (parcial) | **Parcial** → QA-LOAD, QA-SEC |
| Validación UX wireframes (doc pendiente) | F1 mockups + FB-ACTA | OK |

---

## 4. Desviaciones de stack (no son omisiones funcionales)

| PDF especifica | Plan Almahue | Acción |
|--------------|--------------|--------|
| Material UI + Redux + React Query | Tailwind + Vite + axios | Registrar en DEF-ALCANCE / acta stack |
| TypeORM | Prisma | DEF-PRISMA + acta ORM |
| Redis blacklist tokens | No explícito | Ampliar CORE-BACK o DEF-SEC |
| API Gateway / microservicios | Modular monolith | DEF-ARQ documenta decisión |

---

## 5. Tareas agregadas post-validación

Ver `erp_gantt_tasks.py` v3.1:

- `DEF-SUCURSALES` — sucursales multiempresa
- `DEF-AUDIT` — spec auditoría transversal
- `DEF-SEC` — hardening OWASP, rate limit, helmet
- `AUDIT-BACK` — audit_logs + integration/email logs
- `COM-EMAIL` — envío cotización PDF por correo
- `COM-NC` — notas de crédito en motor documentos
- `INF-OBS` — logs JSON, health checks, métricas
- `QA-LOAD` / `QA-SEC` — k6 + OWASP ZAP en pipeline

---

## 6. Fuera de alcance v1 (explícito en plan)

| Ítem | Motivo |
|------|--------|
| Producción / MRP | No en PDF Enterprise v1 — DEF-ALCANCE fase 2 |
| RRHH / Nómina | No en PDF Enterprise v1 |
| Integración SII directa | Reemplazada por GoSocket |
| Mobile | Fuera de scope proyecto |
