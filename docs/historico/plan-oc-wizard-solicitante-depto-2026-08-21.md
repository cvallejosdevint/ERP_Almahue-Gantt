# Contrato — wizard OC: Solicitante / Departamento / Siguiente (21/08)

**Síntoma.** Digitador (p. ej. QA Solicitante AND) no puede pulsar **Siguiente**. Los campos Solicitante y Departamento parecen obligatorios y vacíos; Departamento admite texto basura.

**Causa real de Siguiente gris.** El wizard deshabilita Siguiente si falla *cualquier* catálogo (`proveedores` **o** `cuentas` **o** `centros-costo` **o** `elementos-costo`). `GET elementos-costo` exige solo `contabilidad:read`. El rol SOL tiene `compras:write` y **no** contabilidad → **403**. El banner de error se oculta (403 “silencioso”). El usuario cree que faltan Solicitante/Departamento.

**Causa de producto (campos).** Copia del Agrosoft (Reu1 / MJ): en el sistema viejo se elegían departamento + persona + jefe. En Almahue el solicitante **es quien está logueado** y el “departamento” de aprobaciones **es el grupo Compras**. Los textos libres no mueven la cadena.

## Qué hacer

1. **Solicitante:** solo lectura = nombre de sesión. Se persiste ese texto + `creadoPorId` (ya existe).
2. **Departamento:** solo lectura = nombre del grupo Compras (`previewCadena.grupo.nombre`). Si no hay grupo, el aviso de siempre (Admin › Grupos). No campo libre.
3. **Siguiente (paso 1):** solo exige proveedor. No bloquear por 403 de elementos/cuentas.
4. **GET `/elementos-costo`:** mismo criterio que cuentas — permitir `compras:read` / `compras:write` (imputación OC paso 3). Sin abrir asientos ni plan de cuentas write.
5. Si el paso 3 no puede cargar cuenta/elemento: mensaje visible, no botón gris mudo en el paso 1.

No reset BD. No tesorería. No OV.
