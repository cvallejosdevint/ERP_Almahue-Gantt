---
description: DDL solo en prisma/migrations — no prisma/sql
globs: ERP/erp_back/prisma/**
alwaysApply: false
---

# Prisma ERP

- Cambios de esquema: `npx prisma migrate dev` → carpeta en `migrations/`.
- Prohibido dejar DDL solo en `prisma/sql/`.
- Tablas en schema `erp`, nombres PascalCase quoted (`erp."Usuario"`).
- `NodoEscalaAprobacion.grupoId` es obligatorio (unique empresa+modulo+grupo+usuario).
