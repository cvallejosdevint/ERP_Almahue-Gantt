# Diagrama de flujo de negocio — Almahue ERP (entrega)

**Fecha:** 2026-07-30  
**Alcance:** circuitos operativos Demo OFF (sin GoSocket productivo).

## Vista general

```mermaid
flowchart TB
  subgraph ADMIN["A · Administración"]
    EMP[Empresas] --> USR[Usuarios]
    USR --> ROL[Roles / permisos]
    ROL --> PLT[Plantilla documentos]
    ROL --> WFR[Reglas aprobación]
  end

  subgraph PARAM["B · Parametrización"]
    MON[Monedas / UM / Tipos doc] --> CC[Centros costo]
    CC --> PC[Plan cuentas]
    PC --> EL[Elementos costo]
    EL --> PROV[Proveedores]
    PROV --> PER[Periodos contables]
    PER --> SII[Config SII]
  end

  subgraph VENTAS["C · Ventas"]
    CLI[Clientes] --> COT[Cotización + líneas]
    COT --> EMI[Emitir]
    EMI --> CONV[Convertir NP / Factura]
    CONV --> LIBV[Libro comercial]
    LIBV --> CONTV[Contabilizar]
    CONTV --> NC[Nota crédito]
  end

  subgraph COMPRAS["D · Compras"]
    OC[OC + jefe] --> AP[Aprobar / Rechazar]
    AP --> REC[Recepción + TC]
    REC --> REG[Registro factura compra]
  end

  subgraph CTR["E · Contratistas"]
    ING[Ingreso diario] --> ASO[Asociación labores]
    ASO --> PRF[Proforma]
    PRF --> APR[Aprobar supervisor]
    APR --> FAC[Factura N:1]
    FAC --> TRA[Traspaso / cierre mes]
  end

  subgraph BOD["F · Insumos"]
    ART[Artículos] --> BODG[Bodegas]
    BODG --> MOV[Movimientos / NC]
  end

  subgraph CONTA["G · Contabilidad"]
    ASI[Asientos] --> LD[Libro diario / Mayor]
    LD --> CEN[Centralización masiva]
    PER -.->|periodo abierto| ASI
    PER -.->|periodo abierto| CEN
  end

  subgraph TES["H · Tesorería"]
    CAR[Cartola import] --> CMC[Contabilizar mov]
    CMC --> CAL[Calzar pago]
    CAL --> ANT[Anticipos]
    ANT --> CCT[Cuentas corrientes]
    CAR --> CONC[Conciliación]
  end

  ADMIN --> PARAM
  PARAM --> VENTAS
  PARAM --> COMPRAS
  PARAM --> CTR
  PARAM --> BOD
  VENTAS --> CONTA
  COMPRAS --> CONTA
  CTR --> CONTA
  CONTA --> TES
  COMPRAS --> TES
```

## Decisiones críticas (ramas)

| Nodo | Rama feliz | Excepción esperada |
|---|---|---|
| OC | Aprobar → recepción | Rechazar; solo jefe; sin aprobador |
| Cotización | Emitir → convertir | Anular; no editar FACTURADO |
| Proforma | Definitiva + nombre aprobador | Pendiente aprobación |
| Periodo | Contabilizar si ABIERTO | Bloquear si CERRADO |
| Cartola | Contabilizar → calzar ACTIVO | No duplicar calce; cerrar cartola |
| Centralización | Preview → confirmar | Omitir ya centralizado |

## Cobertura QA previa (TC01–41)

Suite `qa-pruebas-flujo-completo-2026-07-29`: **41/41 PASS** en happy paths principales.  
**No cubre de forma explícita** muchas excepciones (rechazo OC, NC, cartola cierre, anular asiento, etc.) — ver matriz EX del subagente excepciones.
