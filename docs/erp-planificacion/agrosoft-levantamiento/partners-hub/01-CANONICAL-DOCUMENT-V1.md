# CanonicalDocument v1 — borrador de contrato

Contrato que emiten los ERPs hacia Partner Hub. Independiente de GoSocket u otros partners.

```json
{
  "schemaVersion": "1.0",
  "idempotencyKey": "almahue:EMP-1:doc-uuid:1",
  "source": {
    "erpId": "almahue",
    "empresaId": "EMP-1",
    "documentoId": "cm…"
  },
  "emisor": {
    "rut": "76.XXX.XXX-X",
    "razonSocial": "…",
    "giro": "…",
    "acteco": "…",
    "direccion": "…",
    "comuna": "…",
    "ciudad": "…",
    "sucursal": "Casa Matriz",
    "email": "opcional",
    "telefono": "opcional"
  },
  "receptor": {
    "rut": "…",
    "razonSocial": "…",
    "giro": "…",
    "direccion": "…",
    "comuna": "…",
    "ciudad": "…",
    "email": "recomendado Ley 21.713",
    "codigoInterno": "opcional"
  },
  "documento": {
    "tipoDte": 33,
    "fechaEmision": "2026-08-06",
    "fechaVencimiento": "2026-09-06",
    "formaPago": "2",
    "moneda": "CLP",
    "numeroInterno": "correlativo-o-id-erp",
    "referencia": { "tipo": "801", "folio": "OC-12", "fecha": "2026-08-01" }
  },
  "totales": {
    "neto": 100000,
    "exento": 0,
    "iva": 19000,
    "tasaIva": 19,
    "total": 119000
  },
  "lineas": [
    {
      "nro": 1,
      "descripcion": "…",
      "cantidad": 1,
      "unidad": "UN",
      "precio": 100000,
      "descuentoPct": 0,
      "montoNeto": 100000
    }
  ],
  "glosas": [],
  "indicadores": {
    "exportacion": false,
    "exento": false
  }
}
```

## Fuera de contrato (nunca al Hub)

- `cuentaContableId`, `centroCostoId`, asientos, usuarios, plantillas PDF internas del ERP.

## Respuesta Hub (mínima)

```json
{
  "emissionId": "…",
  "partner": "gosocket",
  "status": "ACCEPTED | REJECTED | PENDING",
  "folioOficial": "1234",
  "globalDocumentId": "…",
  "countryDocumentId": "…",
  "messages": [],
  "artifacts": { "pdfAvailable": false, "xmlAvailable": false }
}
```
