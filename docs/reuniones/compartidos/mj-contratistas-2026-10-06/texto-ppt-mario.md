# Texto de Compras_Almahue_ Flujo.pptx

## Diapositiva 1

ERP ALMAHUE · MODELO CONCEPTUAL Maestro de Proveedores y Compras Diagramas de flujo funcionales para revisión del equipo Versión 1.2 · asientos por definir · septiembre 2026 Proveedor Orden de compra Recepción Factura Pago

## Diapositiva 2

00 Vista general del proceso Cinco etapas desde el alta del proveedor hasta el pago. Cada OC queda trazada en la base de datos auxiliar. ERP Almahue · Compras v1.2 1 Proveedor Maestro administrado por admin o jefe de contabilidad. Días de pago de la lista o digitados en la OC. 2 Orden de compra Tipo Compra: insumos, servicios o activo fijo. Aprobación según monto (X, Y, Z). 3 Recepción Con guía o con factura. Parcial crea OC hija  (solo insumos). 4 Factura Se reconoce por N° de guía o de factura. Validación de monto y cantidad. 5 Pago Línea NETO + línea IVA pendientes de pago. Tesorería registra el pago. Si hay alerta en recepción o factura:  el usuario creador modifica la OC (vuelve a aprobación) o rechaza la factura (reclamo en Gosocket; la OC conserva su saldo). modificación

## Diapositiva 3

01 Maestro de proveedores y días de pago El maestro lo administra solo el admin o el jefe de contabilidad. En la OC, el usuario puede digitar otro plazo. ERP Almahue · Compras v1.2 MAESTRO · ADMIN O JEFE DE CONTABILIDAD ORDEN DE COMPRA · USUARIO Admin o jefe de contabilidad Crea o edita proveedor: RUT, contacto, cuenta, moneda y días de la lista ¿Datos completos y RUT único? Proveedor activo Corregir datos o rechazar duplicado Lista de días de pago Usuario crea OC y elige proveedor Precarga condiciones del proveedor ¿Días de pago? Usa un plazo de la lista Digita otro número: se usa en esta OC Admin revisa: ¿se agrega a la lista? Sí No Lista Digita Sí Plazo digitado:  solo un número de días; se usa de inmediato.    IVA por defecto:  CLP, día 10 del mes siguiente.    Proveedor extranjero:  OC exenta de IVA. Estado en BD auxiliar Alerta o rechazo Impacto contable Integración / otro módulo

## Diapositiva 4

02 Tipo de compra, aprobación y modificaciones Toda OC declara su tipo de compra. El mismo circuito aplica a una OC nueva y a cualquier modificación. ERP Almahue · Compras v1.2 Solicitud de modificación Nueva OC:  Se  selecciona  el  tipo  de compra y días de pago OC pendiente de aprobación Monto a CLP; TC del día si es USD o YUAN ¿Monto vs límites del usuario? Aprobación automática Jefatura directa Jefatura directa Gerente de área Jefatura directa Gerente de área Gerente general ¿Aprobada? OC aprobada, recepción pendiente Rechazo con motivo, notificado Creador o jefatura directa corrige ≤ X X a Y Y a Z > Z Sí No Límites X, Y y Z:  por usuario, en el módulo de cadenas.    Secuencial:  un rechazo corta la cadena.    Editar o modificar:  solo el creador y su jefatura  directa . Los  tipo  de  compra  son : INSUMO, SERVICIOS, ACTIVO FIJO

## Diapositiva 5

03 Recepción: guía o factura y OC hijas La recepción se compara con el saldo de la OC. Toda alerta impide guardar el paso. ERP Almahue · Compras v1.2 OC aprobada, recepción pendiente Usuario creador registra la recepción ¿Recepción vs saldo de la OC? Mayor: alerta, no se guarda; pedir modificación de OC ¿Tipo de compra? Servicios o activo fijo: solo recepción completa; no se guarda OC hija automática, autorizada; rebaja saldo ¿Documento de recepción? Guía: registra N° de guía; queda Factura pendiente Factura: registra N° de factura; pasa a validación Mayor Menor Igual Insumos Guía OC hijas:  solo en insumos.    Con factura:  no existe el paso de facturas por recibir.    Asiento de recepción:  según tipo de compra, pendiente de definir. Estado en BD auxiliar Alerta o rechazo Impacto contable Integración / otro módulo

## Diapositiva 6

04 Llegada y asociación de la factura La factura referencia la OC madre; el sistema la reconoce por N° de guía o de factura. ERP Almahue · Compras v1.2 Llega factura ¿Origen? ¿Referencia a la OC madre? Contabilidad asigna la OC Carga manual: usuario indica OC, monto y TC ¿Recepción confirmada y pendiente de factura? Factura en espera de recepción ¿N° de guía o de factura coincide con la recepción? Factura pendiente: Contabilidad asigna las OC hijas Factura asociada: pasa a validaciones Gosocket No Sí Manual No Sí Sí No Una factura puede cubrir varias OC hijas , pero no una OC hija en partes.      Si no hay reconocimiento automático , la factura espera la asignación de Contabilidad. Estado en BD auxiliar Alerta o rechazo Impacto contable Integración / otro módulo

## Diapositiva 7

05 Validaciones de la factura y alertas Si hay alerta, la factura no se asocia y queda pendiente hasta que el usuario creador decida. ERP Almahue · Compras v1.2 Factura asociada a sus recepciones u OC hijas ¿Cubre completas las OC hijas asociadas? ¿Monto y cantidad coinciden? Factura validada Alerta: no se asocia, queda pendiente ¿Qué decide el usuario creador? Modificar la OC: vuelve a aprobación Rechazar: reclamo en Gosocket; la OC conserva su saldo Sí Sí No No PUNTOS CRÍTICOS No se permite facturar una OC hija en partes. Por ahora no se valida el tipo de cambio. El registro en CLP, USD y YUAN no cambia. Estado en BD auxiliar Alerta o rechazo Impacto contable Integración / otro módulo

## Diapositiva 8

06 Registro contable y paso a  pago   ( PENDIENTE) La OC hija ya existe desde la recepción: la factura solo se asocia, se registra y genera las líneas por pagar. ERP Almahue · Compras v1.2 Factura validada Registro en CLP, USD y YUAN Asiento de factura según tipo de compra: por definir Fechas de pago NETO: factura + días IVA: día 10 mes sig. Pendiente de pago: línea NETO + línea IVA Tesorería registra el pago Pagada PUNTOS CRÍTICOS Una línea NETO y una línea IVA por cada OC u OC hija facturada. Recepción con factura: no pasa por facturas por recibir. OC exenta de IVA: solo línea NETO. Estado en BD auxiliar Alerta o rechazo Impacto contable Integración / otro módulo

## Diapositiva 9

07 Cierre de una OC con saldo Si el saldo restante no se recibirá, la OC madre se ajusta a lo recibido y se cierra. ERP Almahue · Compras v1.2 OC madre con saldo que no se recibirá Usuario solicita ajustar la OC a lo recibido Aprobación según el nuevo monto ¿Recibido = monto de la OC? OC cerrada OC sigue abierta con saldo Sí No PUNTOS CRÍTICOS La modificación puede ser positiva o negativa. Pasa por la cadena que corresponda al nuevo monto. Se cierra cuando lo recibido en sus OC hijas iguala el monto modificado. Estado en BD auxiliar Alerta o rechazo Impacto contable Integración / otro módulo

## Diapositiva 10

08 Registro en CLP, USD y YUAN Se aplica al llegar la factura. NETO e IVA tienen el mismo tratamiento. La factura nacional siempre llega en CLP. ERP Almahue · Compras v1.2 Moneda de la OC CLP USD YUAN CLP Monto de la factura TC del día de la factura TC del día de la factura USD Monto de la factura USD de la OC · TC generado TC del día de la factura YUAN Monto de la factura TC del día de la factura YUAN de la OC · TC generado Factura manual Monto y TC ingresados por el usuario; la tercera moneda con TC del día de la factura TC generado = CLP de la factura / monto de la OC (u OC hija) en su moneda. Garantiza que los USD o YUAN registrados sean exactamente los de la OC. Conviene guardarlo junto al registro para trazabilidad.

## Diapositiva 11

09 Estados de la OC en la base auxiliar Cada OC recorre cinco estados; Tesorería es el único que marca una línea como pagada. ERP Almahue · Compras v1.2 ESTADO 1 OC pendiente de aprobación Al enviar la OC o una modificación. ESTADO 2 OC aprobada, recepción pendiente Espera la recepción con guía o con factura. ESTADO 3 Factura pendiente Recepción con guía registrada. Aquí quedan facturas por asignar o con alerta. ESTADO 4 Pendiente de pago Factura validada: línea NETO + línea IVA. ESTADO 5 Pagada Pago registrado por Tesorería. Alerta El paso no se guarda: el registro sigue en su estado pendiente. Recepción con factura Pasa de Estado 2 a Pendiente de pago al validarse la factura. Recepción parcial Solo insumos: se crea una OC hija autorizada; la OC madre conserva el saldo.

## Diapositiva 12

10 Campos de la base de datos auxiliar Un registro por OC (u OC hija), separado en NETO e IVA. ERP Almahue · Compras v1.2 # Campo Contenido Se completa en 0 Estado Uno de los cinco estados del proceso Cada cambio 1 Fecha creación OC Fecha en que se crea la OC Creación de OC 1a Tipo de compra Insumos, servicios o activo fijo Creación de OC 2 Número OC OC madre o hija (100, 100.1…) Creación / recepción parcial 2a Documento de recepción N° de guía o N° de factura Recepción 3 Fecha documento Fecha de la factura Factura 4 Número documento Folio de la factura Factura 5 Fecha de pago NETO: factura + días · IVA: día 10 mes siguiente Factura 6 Proveedor Desde el maestro Creación de OC 7 Ítem Descripción de la compra Creación de OC 8 A pagar NETO o IVA Factura 9 Moneda de pago Según condición de la OC Creación de OC 10–12 Registro CLP / USD / YUAN Según reglas de monedas Factura

## Diapositiva 13

11 Reglas clave para desarrollo Lo que el sistema debe garantizar, más allá del flujo. ERP Almahue · Compras v1.2 Tipo de compra Insumos, servicios o activo fijo: define los asientos y habilita OC hijas solo en insumos. Alertas sin guardado Toda alerta impide guardar el paso; el registro queda en estado pendiente. Reconocimiento por guía La factura se asocia por N° de guía o de factura; si no calza, asigna Contabilidad. Saldo de la OC Total de la OC menos lo recibido en sus OC hijas. Una recepción mayor genera alerta. Permisos de edición Solo el creador y su jefatura directa editan la OC o piden modificarla. Días de pago En la OC: de la lista o digitados; el admin decide si el plazo entra a la lista.

## Diapositiva 14

12 Relación con otros módulos Compras recibe datos de tres fuentes y alimenta a Contabilidad y Tesorería. ERP Almahue · Compras v1.2 Compras Maestro de proveedores Cadenas de aprobación Tipo de cambio del día Gosocket Contabilidad BD auxiliar Tesorería condiciones de pago límites por usuario TC aprobación y registro factura reclamo recepción y factura asignación de OC movimientos pendiente de pago pago Estado en BD auxiliar Alerta o rechazo Impacto contable Integración / otro módulo

## Diapositiva 15

Próximos pasos 1 Revisión con el equipo Validar reglas, estados y responsables de cada paso. 2 Asientos Definir los asientos por tipo de compra y por documento de recepción. 3 Siguiente módulo Tesorería (pago de lo pendiente) o Insumos (recepción de inventario).
