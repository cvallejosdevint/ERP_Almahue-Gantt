-- Identidad real de las dos sociedades + mes actual septiembre.
-- Correr DESPUÉS de migrate (columnas gosocketNroResolucion / gosocketActeco).
-- No borra catálogos, usuarios, grupos ni documentos. IDs siguen EMP-1 / EMP-2.

SET search_path TO erp;

UPDATE "Empresa"
SET
  rut = '77.032.638-9',
  "razonSocial" = 'ALMAHUE EXPORT SPA',
  giro = 'Exportacion de fruta fresca y servicios de packing',
  direccion = 'Camino Fundo El Maiten 1200',
  comuna = 'San Fernando',
  ciudad = 'San Fernando',
  "gosocketBillerId" = 'd159916d-4977-499f-a52e-70550fc379ee',
  "gosocketNroResolucion" = '0',
  "gosocketFechaResolucion" = '2024-10-11',
  "gosocketActeco" = '461001',
  activa = true
WHERE id = 'EMP-1';

UPDATE "Empresa"
SET
  rut = '77.032.639-7',
  "razonSocial" = 'ALM SERVICES SPA',
  giro = 'Servicios logisticos, transporte y soporte operacional',
  "gosocketBillerId" = 'd23bdecb-0776-433b-aaf2-ab4e11e76501',
  "gosocketNroResolucion" = '0',
  "gosocketFechaResolucion" = '2020-02-14',
  activa = true
WHERE id = 'EMP-2';

UPDATE "Empresa" SET activa = false WHERE id = 'EMP-3';

UPDATE "PeriodoContable" SET activo = false WHERE "empresaId" IN ('EMP-1', 'EMP-2');

INSERT INTO "PeriodoContable" (
  id, "empresaId", codigo, anio, mes, "fechaDesde", "fechaHasta", estado, activo, "createdAt", "updatedAt"
)
VALUES
  (
    'PER-EMP1-2026-09', 'EMP-1', '2026-09', 2026, 9,
    TIMESTAMPTZ '2026-09-01 00:00:00+00', TIMESTAMPTZ '2026-09-30 23:59:59+00',
    'ABIERTO', true, NOW(), NOW()
  ),
  (
    'PER-EMP2-2026-09', 'EMP-2', '2026-09', 2026, 9,
    TIMESTAMPTZ '2026-09-01 00:00:00+00', TIMESTAMPTZ '2026-09-30 23:59:59+00',
    'ABIERTO', true, NOW(), NOW()
  )
ON CONFLICT ("empresaId", codigo) DO UPDATE
SET estado = 'ABIERTO', activo = true, "updatedAt" = NOW();
