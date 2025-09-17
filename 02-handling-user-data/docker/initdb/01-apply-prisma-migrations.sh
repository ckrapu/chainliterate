#!/usr/bin/env bash
set -euo pipefail

echo "[initdb] Applying Prisma migrations"

DB_NAME="${POSTGRES_DB:-postgres}"
DB_USER="${POSTGRES_USER:-postgres}"

if [ -d "/prisma/migrations" ]; then
  shopt -s nullglob
  for migration in /prisma/migrations/*/migration.sql; do
    echo "[initdb] Running migration: ${migration}"
    psql -v ON_ERROR_STOP=1 --username "${DB_USER}" --dbname "${DB_NAME}" -f "${migration}"
  done
  shopt -u nullglob
  echo "[initdb] Prisma migrations applied"
else
  echo "[initdb] No Prisma migrations directory found; skipping"
fi

