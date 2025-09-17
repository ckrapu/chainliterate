#!/usr/bin/env bash
set -euo pipefail

awslocal s3api \
  create-bucket --bucket chainliterate-data-layer \
  --create-bucket-configuration LocationConstraint=us-east-2 \
  --region us-east-2

tmp_cors_file="$(mktemp /tmp/chainliterate-cors.XXXXXX.json)"
cat >"${tmp_cors_file}" <<'JSON'
{"CORSRules":[{"AllowedHeaders":["*"],"AllowedMethods":["GET","POST","PUT"],"AllowedOrigins":["*"],"ExposeHeaders":["ETag"]}]}
JSON

awslocal s3api put-bucket-cors \
  --bucket chainliterate-data-layer \
  --cors-configuration file://"${tmp_cors_file}"

rm -f "${tmp_cors_file}"
