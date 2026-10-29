path = 'ERP/erp_front/src/features/contratistas/proforma-editable.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "const PRE_APROBACION = new Set<ProformaContratista['estado']>(['BORRADOR', 'PENDIENTE_APROBACION']);"
replacement = "const PRE_APROBACION = new Set<ProformaContratista['estado']>(['BORRADOR', 'PENDIENTE_APROBACION', 'REVERSADA']);"

norm_content = content.replace('\r\n', '\n')
norm_target = target.replace('\r\n', '\n')

if norm_target in norm_content:
    new_norm = norm_content.replace(norm_target, replacement.replace('\r\n', '\n'))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_norm.replace('\n', '\r\n'))
    print("SUCCESS: proforma-editable.ts updated")
else:
    print("ERROR: Target not found")

