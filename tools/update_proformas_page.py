path = 'ERP/erp_front/src/features/contratistas/ProformasContratistaNivel1Page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target_label = """function estadoProformaLabel(estado: ProformaContratista['estado']): string {
  if (estado === 'ENVIADA_CONTRATISTA') return 'Notificada contratista';
  return estado.replaceAll('_', ' ');
}"""

replacement_label = """function estadoProformaLabel(estado: ProformaContratista['estado']): string {
  if (estado === 'ENVIADA_CONTRATISTA') return 'Notificada contratista';
  if (estado === 'REVERSADA') return 'Reversada';
  return estado.replaceAll('_', ' ');
}"""

target_badge = """function estadoBadge(estado: ProformaContratista['estado']) {
  const tone =
    estado === 'FACTURADA' ? 'success'
      : estado === 'ENVIADA_CONTRATISTA' ? 'success'
        : estado === 'DEFINITIVA' ? 'warning'
          : estado === 'RECHAZADA' ? 'danger'
            : 'muted';
  return <Badge tone={tone}>{estadoProformaLabel(estado)}</Badge>;
}"""

replacement_badge = """function estadoBadge(estado: ProformaContratista['estado']) {
  const tone =
    estado === 'FACTURADA' ? 'success'
      : estado === 'ENVIADA_CONTRATISTA' ? 'success'
        : estado === 'DEFINITIVA' ? 'warning'
          : estado === 'REVERSADA' ? 'warning'
            : estado === 'RECHAZADA' ? 'danger'
              : 'muted';
  return <Badge tone={tone}>{estadoProformaLabel(estado)}</Badge>;
}"""

target_filtro_state = "const [estadoFiltro, setEstadoFiltro] = useState<'TODOS' | 'PENDIENTES' | 'FACTURADAS'>('TODOS');"
replacement_filtro_state = "const [estadoFiltro, setEstadoFiltro] = useState<'TODOS' | 'PENDIENTES' | 'FACTURADAS' | 'REVERSADA'>('TODOS');"

target_filtro_select = """        toolbarExtra={(
          <Select className="max-w-[220px]" value={estadoFiltro} onChange={(e) => setEstadoFiltro(e.target.value as typeof estadoFiltro)}>
            <option value="TODOS">Todas</option>
            <option value="PENDIENTES">Pendientes de facturar</option>
            <option value="FACTURADAS">Facturadas</option>
          </Select>
        )}"""

replacement_filtro_select = """        toolbarExtra={(
          <Select className="max-w-[220px]" value={estadoFiltro} onChange={(e) => setEstadoFiltro(e.target.value as typeof estadoFiltro)}>
            <option value="TODOS">Todas</option>
            <option value="PENDIENTES">Pendientes de facturar</option>
            <option value="FACTURADAS">Facturadas</option>
            <option value="REVERSADA">Reversadas</option>
          </Select>
        )}"""

target_extra_actions = 'if (canFinalize && row.estado === "BORRADOR") {'
replacement_extra_actions = 'if (canFinalize && (row.estado === "BORRADOR" || row.estado === "REVERSADA")) {'

norm_content = content.replace('\r\n', '\n')

def apply_rep(text, t, r, name):
    norm_t = t.replace('\r\n', '\n')
    norm_r = r.replace('\r\n', '\n')
    if norm_t not in text:
        raise ValueError(f"Target not found: {name}")
    print(f"Applied: {name}")
    return text.replace(norm_t, norm_r)

norm_content = apply_rep(norm_content, target_label, replacement_label, "estadoProformaLabel")
norm_content = apply_rep(norm_content, target_badge, replacement_badge, "estadoBadge")
norm_content = apply_rep(norm_content, target_filtro_state, replacement_filtro_state, "estadoFiltro state")
norm_content = apply_rep(norm_content, target_filtro_select, replacement_filtro_select, "estadoFiltro select")
norm_content = apply_rep(norm_content, target_extra_actions, replacement_extra_actions, "extraActions canFinalize")

with open(path, 'w', encoding='utf-8') as f:
    f.write(norm_content.replace('\n', '\r\n'))

print("ALL CHANGES APPLIED TO ProformasContratistaNivel1Page.tsx")

