# Reunion presencial cliente 26/10/2026

**Tipo:** revision contabilidad, parametrizacion, carga masiva, plan de cuentas, OC y presupuesto (presencial).
**Fuentes:**

| Tramo | Medio | Transcripcion | Cobertura |
|---|---|---|---|
| Manana / primera parte | `26-10-2026 12.33.m4a` (01:24:40) | [`transcripcion-2026-10-26-presencial.md`](../transcripciones/transcripcion-2026-10-26-presencial.md) | Parcial: ASR empieza en sala (resultado del ejercicio). Cierre ~almuerzo; final es charla no operativa. |
| Tarde | `26-10-2026 15.20.m4a` | **Pendiente** (archivo corrupto en PC) | No disponible hasta re-copiar desde el celular. |

**Sala (por contexto y apuntes):** Maria Jesus / MJ, equipo Almahue (Carlos en demo). ASR no separa speakers; se marca **MJ** cuando el contenido es regla de negocio / Agrosoft.

**Apuntes del consultor (escritorio):** `revision en cliente.txt` (misma fecha).

---

## 1. Reportes y cierre de periodo

1. **Resultado del ejercicio vs resultado acumulado (MJ, `[00:19]`-`[02:03]`):** El estado de resultados de un mes (ej. enero) muestra solo ese mes. El resultado del ejercicio de diciembre **pasa el 31/12** al estado de situacion financiera como **resultado acumulado**. En reportes debe verse ambos; si falta el resultado del ejercicio en situacion financiera, no cuadra.
2. **Reporteria contable:** Falta cerrar modulo de reporteria mas alla de lo ya visto (`[06:23]`).
3. **Balance 8 columnas / estado de resultados / libro mayor (apuntes consultor, no reforzado en audio 1):** Balance y estado de resultados solo **ano en curso** (cuentas cambian de temporada). Situacion financiera puede traer anos anteriores. Libro mayor si puede cruzar anos con saldo. Filtros mes/ano en diario y mayor; opcion **todos** = solo ano actual. Ancho del selector **todas las cuentas** en mayor.

## 2. Carga masiva de comprobantes (Agrosoft)

4. **Formato restrictivo preferido (MJ, `[08:47]`-`[09:12]`):** Prefieren plantilla fija que obligue campos (ej. centro de costo). Si falta dato obligatorio, **no cargar la linea** y reporte de rechazos (ej. 300 de 1800).
5. **Vista Agrosoft demostrada (`[09:42]`-`[16:57]`):** Correlativo = numero de lineas del comprobante; **tipo** (ej. traspaso desde contabilidad); fecha; TC; cuenta; campos opcionales segun parametrizacion de cuenta (planta, CC, area, auxiliar, referencia, vencimiento, montos CLP/USD, glosa). Validaciones: periodo vs fecha, debe=haber CLP y USD; si falla, **no carga nada** del archivo.
6. **Mapeo Excel flexible (Carlos, `[07:09]`-`[08:43]`):** Propuesta de mapear columnas del Excel en configuracion. MJ acepta soporte futuro pero **prioriza formato unico** para no saltarse obligatorios.
7. **Configuracion de columnas (MJ, `[10:44]`-`[11:46]`):** Formulario donde marcan obligatorios y vinculan columna Excel (ej. periodo en columna P); una vez definido, permanece.
8. **Carga historica:** MJ ofrece cruzar archivos / plantilla con todas las cuentas (`[21:18]`). Validar data con **Mario** (apuntes consultor).

## 3. Plan de cuentas y dimensiones (N:N)

9. **Asociacion por cuenta (`[22:15]`-`[25:59]`):** Cada cuenta imputable puede tener **N** centros de costo, **N** elementos y **N** areas. UI tipo tres listas con agregar/quitar. Al usar la cuenta, solo se ofrecen los ligados. **Aprobado** en sala.
10. **Centro vs elemento (MJ):** Centro mas transversal (ej. cerezas); elemento mas por departamento / detalle operacion (DUS, certificados, etc.). **No** ligar elemento al centro de forma rigida (`[30:18]`-`[31:22]`).
11. **Columna contador en mantenedores (`[29:17]`-`[29:59]`):** En CC, elemento y area, columna con **cantidad de cuentas** asociadas; al clic, detalle. Vista principal desde la cuenta; contador es utilidad inversa.
12. **Export plan de cuentas (`[18:10]`-`[18:51]`):** Niveles 1-5 como Agrosoft; filtros por tipo (activo, pasivo, etc.).
13. **Area de negocio:** MJ indica que el Excel actual puede estar mal parametrizado (`[20:03]`); revisar con archivo que enviara.

## 4. Presupuesto y responsabilidad por area

14. **Imputacion obligatoria (`[24:37]`-`[28:51]`):** Sin CC/elemento correctos el presupuesto no sirve. Meta 2026: cada area define cuenta y elemento al aprobar OC (hoy solo aprueban monto). Ejemplo VINs confeccion vs arriendo.
15. **Alerta presupuesto (apuntes):** Parametro de **porcentaje** de alerta visible en totalizados (no hablado en audio 1).
16. **CC por departamento con totalizados arriba (apuntes):** No detallado en audio 1.

## 5. Orden de compra

17. **Orden de campos (`[44:04]`-`[44:13]`):** **Cuenta contable**, luego **centro de costo**, luego **elemento**. Sin cuenta, CC y elemento bloqueados.
18. **Lineas vs multiples dimensiones:** MJ prefiere **varias lineas** con misma cuenta y distinto CC/elemento, no un solo renglon con N centros (`[47:25]`-`[47:47]`). Carlos: opcion **+** o duplicar linea; detalle agrupable al exportar.
19. **Division por monto (`[35:06]`-`[35:17]`):** Casos raros (software 50% TI / 50% contabilidad); puede ir por monto segun factura.
20. **Solicitar CC/elemento no listado (`[44:13]`-`[45:24]`):** Si no esta en lista de la cuenta, **solicitud al administrador** con motivo y trazabilidad (usuario, cuenta). No agregar libre en OC.
21. **Vista detalle OC (`[48:50]`-`[55:29]`):** Ver detalle en sistema estilo **flujo de caja** / arbol (cuenta y debajo CC/elemento). MJ quiere CC visible en vista principal, no solo en segunda hoja.
22. **PDF al proveedor (`[51:11]`-`[55:45]`):** Export oficial **sin** dimensiones contables; detalle contable solo en ERP. Opcion exportar con detalle para uso interno si aplica.
23. **Nace en OC (`[31:46]`):** Ideal imputar en OC; hoy a veces se corrige en factura.

## 6. Comprobantes manuales (apuntes + parcial audio)

24. **Tipos origen (apuntes):** apertura, egresos, ingresos, proveedores, traspasos, ventas. Correlativo con nomenclatura de tipo; tipo manual al crear; automatico si viene de otro modulo. **Implementado en UI** (deploy 26/10) segun trabajo previo.
25. **Nuevo comprobante contabilizado al guardar (apuntes):** No confirmado en audio 1.
26. **Detalle asiento 3 columnas, RC adjunto, editar glosa, motivo cierre/apertura, TC manual + aviso admin (apuntes):** No detallado en audio 1.

## 7. Parametrizacion general (apuntes; pendiente audio tarde)

27. **Bancos:** Varias cuentas por banco, cada una con moneda.
28. **Historial de parametrizaciones:** Revisar; no funciona.
29. **Usuarios dos empresas:** Corregido selector (ok en apuntes).
30. **Boleta de honorarios:** Registro y recepcion; no emision; tipo documento en proveedores.
31. **Nota de cobro:** Rendicion de gastos; compras + contabilidad; facturas electronicas.
32. **OPB / embarcador:** Intermediario que paga facturas export/import; Almahue ingresa detalle.

## 8. Tesoreria / cartola (audio 1 tarde reunión)

33. **Cartola y formato banco (`[01:02:43]`-`[01:09:29]`):** Lupe confirma descarga **directa del banco**. Limitaciones de acceso ejecutivo Banco Chile; validar formato con operacion.

## 9. Pendientes de evidencia

- Transcribir `15.20.m4a` cuando el archivo sea valido.
- Archivos Excel / carga masiva que MJ ofrecio enviar.
- Confirmar en audio tarde: honorarios, OPB, bancos, historial, comprobante contabilizado, filtros mayor/balance.

---

## Referencias

- Transcripcion manana: [`../transcripciones/transcripcion-2026-10-26-presencial.md`](../transcripciones/transcripcion-2026-10-26-presencial.md)
- Contraste con apuntes: [`../../requerimientos/contraste-minuta-revision-cliente-2026-10-26.md`](../../requerimientos/contraste-minuta-revision-cliente-2026-10-26.md)
