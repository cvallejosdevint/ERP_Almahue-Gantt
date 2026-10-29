with open('ERP/erp_front/src/types/domain.ts', 'r', encoding='utf-8') as f:
    text = f.read()

target = """export type EstadoProforma =
  | 'BORRADOR'
  | 'PENDIENTE_APROBACION'
  | 'DEFINITIVA'
  | 'ENVIADA_CONTRATISTA'
  | 'FACTURADA'
  | 'RECHAZADA';"""

replacement = """export type EstadoProforma =
  | 'BORRADOR'
  | 'PENDIENTE_APROBACION'
  | 'DEFINITIVA'
  | 'ENVIADA_CONTRATISTA'
  | 'FACTURADA'
  | 'RECHAZADA'
  | 'REVERSADA';"""

norm_text = text.replace('\r\n', '\n')
if target in norm_text:
    new_norm = norm_text.replace(target, replacement, 1)
    if '\r\n' in text:
        final_text = new_norm.replace('\n', '\r\n')
    else:
        final_text = new_norm
    with open('ERP/erp_front/src/types/domain.ts', 'w', encoding='utf-8') as f:
        f.write(final_text)
    print('domain.ts updated successfully!')
else:
    print('Target not found!')

