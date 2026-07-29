#!/usr/bin/env bash
# Construye imágenes Docker del ERP (api + web).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

API_TAG="${ERP_API_IMAGE:-almahue-erp-api:local}"
WEB_TAG="${ERP_WEB_IMAGE:-almahue-erp-web:local}"
VITE_API_URL="${VITE_API_URL:-/api/v1}"
VITE_APP_TITLE="${VITE_APP_TITLE:-Almahue ERP v1}"

echo "==> Building $API_TAG"
docker build -t "$API_TAG" ./erp_back

echo "==> Building $WEB_TAG (VITE_API_URL=$VITE_API_URL)"
docker build \
  --build-arg "VITE_API_URL=$VITE_API_URL" \
  --build-arg "VITE_APP_TITLE=$VITE_APP_TITLE" \
  -t "$WEB_TAG" \
  ./erp_front

echo "OK. Imágenes: $API_TAG , $WEB_TAG"
