#!/usr/bin/env bash
# Configura .env del ERP y del intermediario SIN imprimir secretos.
# Uso en el host: sudo bash /tmp/bootstrap-billing-prod.sh
set -eu

ERP_ENV=/opt/almahue_erp/.env
GW_DIR=/opt/billing_gateway
GW_ENV="$GW_DIR/.env"
LOCAL_ENV=/tmp/billing.env.local
TENANTS_SRC="$GW_DIR/src/registry/tenants.local.example.json"
TENANTS_DST="$GW_DIR/src/registry/tenants.local.json"

if [[ ! -f "$ERP_ENV" ]]; then
  echo "Falta $ERP_ENV" >&2
  exit 1
fi
if [[ ! -f "$LOCAL_ENV" ]]; then
  echo "Falta $LOCAL_ENV (subir .env local del gateway, luego borrar)" >&2
  exit 1
fi

umask 077
KEY="$(openssl rand -base64 48 | tr -d '\n')"
if [[ ${#KEY} -lt 32 ]]; then
  echo "No se pudo generar API key" >&2
  exit 1
fi

mkdir -p "$GW_DIR/src/registry"

if grep -q '^BILLING_GATEWAY_ENABLED=' "$ERP_ENV"; then
  sed -i \
    -e 's/^BILLING_GATEWAY_ENABLED=.*/BILLING_GATEWAY_ENABLED=true/' \
    -e 's/^BILLING_STUB_INLINE=.*/BILLING_STUB_INLINE=false/' \
    -e 's|^BILLING_GATEWAY_URL=.*|BILLING_GATEWAY_URL=http://almahue_billing_gateway:3040|' \
    "$ERP_ENV"
  if grep -q '^BILLING_GATEWAY_API_KEY=' "$ERP_ENV"; then
    sed -i "s|^BILLING_GATEWAY_API_KEY=.*|BILLING_GATEWAY_API_KEY=${KEY}|" "$ERP_ENV"
  else
    printf '\nBILLING_GATEWAY_API_KEY=%s\n' "$KEY" >> "$ERP_ENV"
  fi
else
  cat >> "$ERP_ENV" <<EOF

BILLING_GATEWAY_ENABLED=true
BILLING_STUB_INLINE=false
BILLING_GATEWAY_URL=http://almahue_billing_gateway:3040
BILLING_GATEWAY_API_KEY=${KEY}
EOF
fi

{
  echo "PORT=3040"
  echo "BILLING_HOST_PORT=3040"
  echo "BILLING_BIND_HOST=0.0.0.0"
  echo "BILLING_STORE_PATH=/app/data/emissions.sqlite"
  echo "BILLING_CORS_ORIGINS="
  echo "BILLING_API_KEYS=${KEY}@almahue"
  echo "DEFAULT_CONNECTION_MODE=sandbox"
  grep -E '^GOSOCKET_' "$LOCAL_ENV" || true
} > "$GW_ENV"
chmod 600 "$GW_ENV"

if [[ -f "$TENANTS_SRC" ]]; then
  cp "$TENANTS_SRC" "$TENANTS_DST"
fi
chmod 600 "$TENANTS_DST" 2>/dev/null || true

shred -u "$LOCAL_ENV" 2>/dev/null || rm -f "$LOCAL_ENV"

echo "billing-env: ok (key rotada, GOSOCKET copiado, tenants.local listo)"
