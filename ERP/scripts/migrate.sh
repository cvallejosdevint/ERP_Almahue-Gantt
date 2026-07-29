#!/usr/bin/env bash
# Aplica migraciones Prisma contra DATABASE_URL del .env / entorno.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi

: "${DATABASE_URL:?Define DATABASE_URL (en .env o entorno)}"

echo "==> prisma migrate deploy (schema erp)"
docker compose run --rm --no-deps \
  -e DATABASE_URL="$DATABASE_URL" \
  api npx prisma migrate deploy

echo "OK"
