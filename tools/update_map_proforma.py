path = 'ERP/erp_back/src/modules/contratistas/contratistas.service.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """  estado:
    | 'BORRADOR'
    | 'PENDIENTE_APROBACION'
    | 'DEFINITIVA'
    | 'ENVIADA_CONTRATISTA'
    | 'FACTURADA'
    | 'RECHAZADA';"""

replacement = """  estado:
    | 'BORRADOR'
    | 'PENDIENTE_APROBACION'
    | 'DEFINITIVA'
    | 'ENVIADA_CONTRATISTA'
    | 'FACTURADA'
    | 'RECHAZADA'
    | 'REVERSADA';"""

norm_content = content.replace('\r\n', '\n')
norm_target = target.replace('\r\n', '\n')

if norm_target in norm_content:
    norm_content = norm_content.replace(norm_target, replacement.replace('\r\n', '\n'))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(norm_content.replace('\n', '\r\n'))
    print("SUCCESS: mapProforma estado updated")
else:
    print("ERROR: Target not found")

