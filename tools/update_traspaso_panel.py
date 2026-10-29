path = 'ERP/erp_front/src/features/contratistas/TraspasoContratistasResumenPanel.tsx'
with open(path, 'rb') as f:
    text = f.read().decode('utf-8').replace('\r\n', '\n')

target = """          <div className="mb-3 flex flex-wrap gap-x-4 gap-y-1 text-xs text-[var(--color-muted)]">"""

replacement = """          {/* Matriz 2x2 Cierre Contratistas vs Cierre Contable */}
          <div className="mb-3 rounded-md border border-[var(--color-border)] bg-[var(--color-surface-2)] px-3 py-2 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div>
              <span className="text-xs font-semibold text-[var(--color-text)]">
                {!traspasoHecho && !periodoContableCerrado && 'Caso 1: Contratistas Abierto · Contabilidad Abierta'}
                {traspasoHecho && !periodoContableCerrado && 'Caso 2: Contratistas Centralizado · Contabilidad Abierta'}
                {!traspasoHecho && periodoContableCerrado && 'Caso 3: Contratistas Abierto · Contabilidad Cerrada'}
                {traspasoHecho && periodoContableCerrado && 'Caso 4: Contratistas Cerrado · Contabilidad Cerrada (Cierre Total)'}
              </span>
              <p className="text-[11px] text-[var(--color-muted)]">
                {!traspasoHecho && !periodoContableCerrado && 'Operación normal activa. Se permiten reversas directas con clave manteniendo ítems asociados.'}
                {traspasoHecho && !periodoContableCerrado && 'Módulo centralizado con asiento. Se permite reapertura del módulo para corregir y re-traspasar.'}
                {!traspasoHecho && periodoContableCerrado && 'Período contable cerrado. Bloqueo de centralización directa; requiere diferir a período abierto.'}
                {traspasoHecho && periodoContableCerrado && 'Asiento de centralización inmutable. Correcciones solo vía Comprobante de Ajuste con PIN de regla de aprobación.'}
              </p>
            </div>
            <span className="self-start sm:self-auto text-[10px] font-bold px-2 py-0.5 rounded bg-[var(--color-surface)] border border-[var(--color-border)] tabular-nums">
              {!traspasoHecho && !periodoContableCerrado && 'CASO 1 / 4'}
              {traspasoHecho && !periodoContableCerrado && 'CASO 2 / 4'}
              {!traspasoHecho && periodoContableCerrado && 'CASO 3 / 4'}
              {traspasoHecho && periodoContableCerrado && 'CASO 4 / 4'}
            </span>
          </div>

          <div className="mb-3 flex flex-wrap gap-x-4 gap-y-1 text-xs text-[var(--color-muted)]">"""

if target in text:
    text = text.replace(target, replacement)
    print("TraspasoContratistasResumenPanel updated with 2x2 matrix banner")
else:
    print("ERROR: target not found")

with open(path, 'wb') as f:
    f.write(text.replace('\n', '\r\n').encode('utf-8'))

print("DONE")
