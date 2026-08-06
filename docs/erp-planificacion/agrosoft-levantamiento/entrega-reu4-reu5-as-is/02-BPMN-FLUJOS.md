# BPMN — Flujos de negocio con gateways (Reu4 → Reu5)

**Fecha:** 2026-08-06  
**Notación:** Mermaid estilo BPMN. Diamantes = **XOR** (una rama) o **AND** (paralelo).  
**Cobertura AS-IS:** Sí · Parcial · No · Diferido

---

## 1. Emisión de ventas (ancla GoSocket)

```mermaid
flowchart TD
  start([Inicio: emitir documento]) --> gwTipo{XOR tipo}
  gwTipo -->|FACTURA_NC| wizard[Wizard Emitir]
  gwTipo -->|COTIZACION| cotiz[Mantenedor cotizaciones]
  wizard --> draft[Guardar BORRADOR]
  draft --> preview[Preview marca agua BORRADOR]
  preview --> gwReady{XOR listo para emitir?}
  gwReady -->|No| edit[Editar borrador]
  edit --> gwReady
  gwReady -->|Si Grabar y contabilizar| gwPeriodo{XOR periodo ABIERTO?}
  gwPeriodo -->|No| block[Bloqueo: abrir periodo]
  gwPeriodo -->|Si| asiento[Generar asiento ERP]
  asiento --> gwGs{XOR GoSocket integrado?}
  gwGs -->|No AS-IS| local[EMITIDO local folio provisorio]
  gwGs -->|Si TO-BE| gs[Enviar DTE GoSocket]
  gs --> pdf[PDF timbrado + folio CAF]
  local --> libro[Libro ventas]
  pdf --> libro
  cotiz --> gwConv{XOR convertir a}
  gwConv -->|NP| np[NP BORRADOR]
  gwConv -->|FACTURA| draft
  np --> gwNpFact{XOR facturar NP?}
  gwNpFact -->|Si| draft
  gwNpFact -->|No| park[Queda en bandeja NP]
```

| Gateway | Ramas | Cobertura AS-IS |
|---|---|---|
| XOR tipo | Factura/NC vs Cotización | Sí |
| XOR listo | Seguir editando vs Grabar+contabilizar | Sí |
| XOR periodo | Abierto vs cerrado | Sí |
| XOR GoSocket | Local vs DTE | **Diferido** / rama local Sí |
| XOR convertir | NP vs Factura | Parcial (pierde campos) |
| XOR facturar NP | Sí vs No | **Parcial** (API Sí, UI No) |

---

## 2. Corrección de venta: reverso vs NC

```mermaid
flowchart TD
  doc[Factura CONTABILIZADA] --> gwCorr{XOR tipo correccion}
  gwCorr -->|Solo imputacion CC_cuenta| rev[Reverso contable]
  rev --> editImp[Editar cuenta/CC]
  editImp --> recontab[Re-contabilizar]
  gwCorr -->|Anular o corregir monto tributario| nc[Emitir NC]
  nc --> gwNc{XOR tipo NC}
  gwNc -->|Anulacion total| ncTot[NC monto = factura]
  gwNc -->|Correccion monto_texto| ncParc[NC precargada]
  ncTot --> libroNC[Libro ventas NC resta]
  ncParc --> libroNC
```

| Gateway | Cobertura |
|---|---|
| XOR reverso vs NC | Sí (flujos separados) |
| XOR NC total vs parcial | Parcial |

---

## 3. Compras: OC → PIN → recepción → factura

```mermaid
flowchart TD
  oc[OC BORRADOR] --> emit[Emitir OC]
  emit --> gwApr{XOR requiere aprobacion?}
  gwApr -->|No| ok[APROBADO]
  gwApr -->|Si| pin[Solicitar + PIN aprobador]
  pin --> gwPin{XOR resultado PIN}
  gwPin -->|Aprobado| ok
  gwPin -->|Rechazado| rech[RECHAZADO / re-emitir]
  ok --> rec[Recepcion]
  rec --> gwRec{XOR confirmar recepcion?}
  gwRec -->|Borrador| rec
  gwRec -->|Confirmada| reg[Registro factura compra]
  reg --> gwAfecto{XOR afecto OC vs factura}
  gwAfecto -->|Mismatch| alert[Alerta usuario]
  alert --> gwForce{XOR continuar?}
  gwForce -->|Si| asientoC[Asiento compra]
  gwForce -->|No| fix[Corregir datos]
  gwAfecto -->|OK| asientoC
```

| Gateway | Cobertura |
|---|---|
| XOR aprobación / PIN | Sí |
| XOR recepción | Sí |
| XOR afecto/exento | Sí (alerta, no bloqueo duro) |

---

## 4. Contratistas: ingreso → proforma → factura N:1 → traspaso

```mermaid
flowchart TD
  ing[Ingreso diario labores] --> asoc[Asociar a labores/CC]
  asoc --> pf[Proforma BORRADOR]
  pf --> gwDef{XOR pasar a definitiva?}
  gwDef -->|Directo si sin jefes| def[DEFINITIVA]
  gwDef -->|Hay regla jefes| sol[Solicitar aprobacion + elegir aprobador]
  sol --> pinP[PIN]
  pinP --> gwPinP{XOR}
  gwPinP -->|OK| def
  gwPinP -->|Rechazo| pf
  def --> gwFact{XOR facturar}
  gwFact -->|1 o N proformas| fac[Factura N:1 interna]
  fac --> tras[Traspaso cierre periodo header]
  tras --> asientoT[Asiento cierre]
  def --> gwRev{XOR reversar?}
  gwRev -->|Si + clave| pf
```

| Gateway | Cobertura |
|---|---|
| XOR definitiva / cola PIN | Sí |
| XOR factura N:1 | Sí |
| XOR reverso | Sí |
| GoSocket factura proveedor | Diferido |

---

## 5. Contabilidad: periodos

```mermaid
flowchart TD
  p[Periodo] --> gwEst{XOR estado}
  gwEst -->|ABIERTO| trabajo[Contabilizar docs/asientos]
  gwEst -->|CERRADO| block2[Bloqueo contabilizacion]
  block2 --> gwRe{XOR reabrir?}
  gwRe -->|Si| motivo[Motivo obligatorio]
  motivo --> hist[Evento REABRIR en historial]
  hist --> trabajo
  trabajo --> gwCerrar{XOR cerrar mes?}
  gwCerrar -->|Si| cerrar[CERRAR + evento]
```

| Gateway | Cobertura |
|---|---|
| XOR abierto/cerrado | Sí |
| XOR reabrir + motivo | Sí |
| Historial quién/cuándo | Sí |

---

## 6. Tesorería: cartola → pago → conciliación

```mermaid
flowchart TD
  imp[Importar cartola] --> movs[Movimientos PENDIENTE]
  movs --> gwPath{XOR camino}
  gwPath -->|Contabilizar mov| asientoB[Asiento banco]
  gwPath -->|Crear pago| pago[Pago + calce movId]
  pago --> asientoB
  asientoB --> conc[Conciliacion]
  conc --> gwConc{XOR}
  gwConc -->|Conciliar| okC[Conciliado]
  gwConc -->|Desconciliar| movs
  libroV[Libro ventas Registrar pago] --> gwBridge{XOR bridge UI?}
  gwBridge -->|TO-BE navigate| pago
  gwBridge -->|AS-IS stub| toast[Toast sin navegacion]
```

| Gateway | Cobertura |
|---|---|
| XOR cartola/pago | Sí |
| XOR conciliar | Sí |
| XOR bridge libro→pago | **Parcial / No** (stub) |

---

## 7. Resumen de cobertura de casuísticas

| Flujo | Gateways cubiertos | Huecos |
|---|---|---|
| Emisión ventas | Borrador, periodo, reverso/NC | GoSocket DTE; NP→Factura UI |
| Compras | PIN, recepción, afecto | Ingestión compras GoSocket |
| Contratistas | PIN, N:1, traspaso | Factura proveedor electrónica |
| Periodos | Cerrar/reabrir+motivo | — |
| Tesorería | Cartola/pago/conciliación | Bridge desde libros; Excel finas |

**Conclusión BPMN:** la lógica piloto cubre las casuísticas **operativas sin SII**. Las ramas TO-BE de GoSocket y los dead-ends UI (NP, bridge pago, stubs mail) son los gaps de cobertura real pendientes de cierre de código / integración.
