INSERT INTO erp."ActivoFijoIpc" ("id", "empresaId", "periodoYm", "valor", "createdAt", "updatedAt")
VALUES
  ('ipc-emp1-2026-09', 'EMP-1', '2026-09', 0.500000, NOW(), NOW()),
  ('ipc-emp1-2026-10', 'EMP-1', '2026-10', 0.800000, NOW(), NOW()),
  ('ipc-emp2-2026-09', 'EMP-2', '2026-09', 0.500000, NOW(), NOW()),
  ('ipc-emp2-2026-10', 'EMP-2', '2026-10', 0.800000, NOW(), NOW()),
  ('ipc-emp3-2026-09', 'EMP-3', '2026-09', 0.500000, NOW(), NOW()),
  ('ipc-emp3-2026-10', 'EMP-3', '2026-10', 0.800000, NOW(), NOW())
ON CONFLICT ("empresaId", "periodoYm") DO UPDATE SET "valor" = EXCLUDED."valor", "updatedAt" = NOW();
