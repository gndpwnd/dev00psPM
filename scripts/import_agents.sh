#!/bin/bash

N8N_URL=${N8N_URL:-http://n8n:5678}
AUTH_USER=${N8N_BASIC_AUTH_USER:-admin}
AUTH_PASS=${N8N_BASIC_AUTH_PASSWORD:-adminpass}

echo "Importing agent workflows..."

for file in ./agents/*.json; do
  echo "Importing $file..."
  curl -s -u "$AUTH_USER:$AUTH_PASS" \
    -X POST "$N8N_URL/rest/workflows" \
    -H "Content-Type: application/json" \
    -d @"$file"
done

echo "Done importing workflows."