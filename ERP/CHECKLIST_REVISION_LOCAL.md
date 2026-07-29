# Checklist revisión local — ERP Almahue

## Cómo levantar

```bash
# Backend (puerto 3001)
cd ERP/erp_back
cp .env.example .env   # si aún no existe
npx prisma migrate deploy
npx prisma db seed
npm run start:dev

# Frontend (puerto 5173 típico Vite)
cd ERP/erp_front
npm run dev
```

- API: http://localhost:3001/api/v1  
- Swagger: http://localhost:3001/api/docs  
- App: http://localhost:5173  

## Credenciales seed

| Usuario | Password | Rol |
|---------|----------|-----|
| `admin@almahue.local` | `Admin123!` | Administrador (`*`) |
| `cperez@almahue.cl` | `demo123` | Analista (lectura) |
| `jsanchez@almahue.cl` | `demo123` | Digitador contratistas |
| `atorres@almahue.cl` | `demo123` | Contador |

Empresa activa por defecto: **Almahue SpA** (`EMP-1`). Usar header/selector `X-Empresa-Id`.

## Pantallas a revisar (modo real)

Marcar al validar contra API real (no demo).

### Admin / catálogos
- [ ] http://localhost:5173/admin/empresas
- [ ] http://localhost:5173/admin/usuarios
- [ ] http://localhost:5173/admin/roles
- [ ] http://localhost:5173/catalogos/monedas
- [ ] http://localhost:5173/catalogos/unidades
- [ ] http://localhost:5173/catalogos/tipos-documento
- [ ] http://localhost:5173/catalogos/centros-costo

### Contratistas (Oleada 2)
- [ ] http://localhost:5173/contratistas
- [ ] http://localhost:5173/contratistas/ingreso-diario
- [ ] http://localhost:5173/contratistas/asociacion
- [ ] http://localhost:5173/contratistas/tarifas
- [ ] http://localhost:5173/contratistas/proformas
- [ ] http://localhost:5173/contratistas/traspaso

### Compras (Oleada 3)
- [ ] http://localhost:5173/compras/ordenes
- [ ] http://localhost:5173/compras/aprobaciones
- [ ] http://localhost:5173/compras/recepciones
- [ ] http://localhost:5173/compras/registro

### Insumos (Oleada 4)
- [ ] http://localhost:5173/insumos/maestro
- [ ] http://localhost:5173/insumos/bodegas
- [ ] http://localhost:5173/insumos/movimientos

### Contabilidad (Oleada 5)
- [ ] http://localhost:5173/contabilidad/plan-cuentas
- [ ] http://localhost:5173/contabilidad/elementos-costo
- [ ] http://localhost:5173/contabilidad/honorarios
- [ ] http://localhost:5173/contabilidad/indicadores-bc
- [ ] http://localhost:5173/contabilidad/asientos
- [ ] http://localhost:5173/contabilidad/reportes

### Tesorería (Oleada 6)
- [ ] http://localhost:5173/tesoreria/flujo-caja
- [ ] http://localhost:5173/tesoreria/pagos
- [ ] http://localhost:5173/tesoreria/cartolas
- [ ] http://localhost:5173/tesoreria/nominas
- [ ] http://localhost:5173/tesoreria/anticipos
- [ ] http://localhost:5173/tesoreria/conciliacion

### Comercial + GoSocket (Oleada 7)
- [ ] http://localhost:5173/comercial/clientes
- [ ] http://localhost:5173/comercial/libro
- [ ] http://localhost:5173/integraciones/gosocket

### Dashboard
- [ ] http://localhost:5173/

## Smoke mínimo sugerido

1. Login admin → KPIs dashboard con datos.
2. Crear ingreso labor diario → asociar a proforma DEFINITIVA.
3. Crear/editar OC con distribución CC → ver aprobación pendiente.
4. Contabilizar movimiento de cartola seed → asiento en Contabilidad.
5. Reversar documento comercial FAC-1001 → cadena asientos.
6. GoSocket: listar DTEs seed (sync local si `GOSOCKET_API_URL` vacío).
