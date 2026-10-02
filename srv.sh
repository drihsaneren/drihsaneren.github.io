#!/bin/bash
# yerel sunucuyu başlat (yoksa), sonra verilen komutu çalıştır
curl -s -o /dev/null http://127.0.0.1:8765/ || { python3 -m http.server 8765 --directory "${REPO:-/home/claude/drihsaneren.github.io}" >/dev/null 2>&1 & sleep 1; }
cd "$(dirname "$0")" && "$@"
