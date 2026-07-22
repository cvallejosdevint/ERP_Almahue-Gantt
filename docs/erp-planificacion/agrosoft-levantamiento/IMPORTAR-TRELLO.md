# Importar tarjetas a Trello (gratis y masivo)

## Sobre tu archivo `undefined - -.json`

Ese archivo **no es un export del tablero**: es HTML de la app de Trello (página web guardada con extensión `.json` por error). Por eso no sirve para importar.

Export JSON real (si lo necesitas después): en el tablero → menú `⋯` → **Imprimir y exportar** → **Exportar como JSON** (a veces requiere plan pago). **No lo necesitas** para crear tarjetas: usamos la API.

## Opción recomendada: API Trello (gratis)

La API REST de Trello es gratuita con API Key + Token personal. Ideal para ~40–60 tarjetas.

### 1. Credenciales (2 minutos)

1. Entra a [trello.com/power-ups/admin](https://trello.com/power-ups/admin) (o [trello.com/app-key](https://trello.com/app-key)).
2. Copia tu **API Key**.
3. Genera un **Token** (Authorize) y cópialo.
4. Abre tu tablero vacío. La URL es:
   `https://trello.com/b/XXXXXXXX/nombre-tablero`  
   → `XXXXXXXX` es el **Board ID** (también sirve el id largo).

### 2. Crear tablero vacío (manual, 10 s)

Crea un tablero, por ejemplo: **ERP Agrosoft 3.0 — Levantamiento**.  
(Puedes borrar las listas por defecto “Por hacer / En curso / Hecho” o dejarlas; el script crea las suyas.)

### 3. Primero: extraer lo que ya hay (~25 tarjetas)

Si el tablero **ya tiene tarjetas**, sácalas antes de importar (para ver duplicados / merge):

```powershell
cd E:\source\repos\Almahue\docs\erp-planificacion\agrosoft-levantamiento

$env:TRELLO_KEY = "TU_API_KEY"
$env:TRELLO_TOKEN = "TU_TOKEN"
$env:TRELLO_BOARD = "XXXXXXXX"

# O, si ya tienes el export JSON del tablero:
python extraer-trello.py --from-json "c:\Users\c\Downloads\wixKcrP0 - almahue-erp.json"
```

Genera `trello-snapshot.md`, `.csv` y `.json` en esta carpeta.

Tablero actual: [Almahue ERP](https://trello.com/b/wixKcrP0/almahue-erp) (`TRELLO_BOARD=wixKcrP0`) — workflow QA (Pendiente → … → En producción), no las listas del levantamiento Agrosoft.

### 4. Luego: importar el backlog canónico

```powershell
# Ver qué crearía (sin tocar Trello)
python importar-trello.py --dry-run

# Crear listas + tarjetas (no duplica si el título ya existe)
python importar-trello.py
```

El script:

- Crea las 8 listas de `trello-depurado.md`
- Crea tarjetas DEC/PEND + las de `matriz-trazabilidad.csv`
- Pone en la descripción: etiqueta, timestamps y link tl;dv
- **No duplica** si el título ya existe
- No sube PNG (eso se hace a mano o en un segundo paso); deja la ruta local en la descripción

### 5. Adjuntar capturas (opcional, después)

Las PNG están en `pantallas-legacy/`. Puedes arrastrarlas a cada tarjeta, o ampliar el script con `POST /cards/{id}/attachments` (también gratis vía API).

## Otras opciones gratis (más lentas)

| Método | Pros | Contras |
|---|---|---|
| **API + este script** | Rápido, repetible, gratis | Hay que generar key/token una vez |
| Copiar/pegar desde MD | Sin setup | Lento (~1 h) |
| Butler / automatizaciones Trello | Nativo | Límites en free; no importa CSV masivo bien |
| Power-Ups de import CSV | A veces fáciles | Muchos son de pago |

## Seguridad

- **No subas** key/token al git.
- El token da acceso a tus tableros: tratalo como contraseña.
- Si lo compartes por error, revócalo en la misma página de app-key.
