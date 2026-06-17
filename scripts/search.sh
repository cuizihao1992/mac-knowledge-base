#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -eq 0 ]; then
  echo "Usage: ./scripts/search.sh <keyword>"
  exit 1
fi

if command -v rg >/dev/null 2>&1; then
  rg --line-number --heading --smart-case "$*" .
else
  grep -RIn "$*" .
fi
