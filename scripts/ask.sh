#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if [ -x "$ROOT_DIR/.venv/bin/python" ]; then
  PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
fi

if [ -f "$ENV_FILE" ]; then
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
fi

QUERY="${1:-}"
if [ -z "$QUERY" ]; then
  echo "Usage: ./scripts/ask.sh \"你的问题\" [provider]" >&2
  echo "Providers: none, deepseek, openai, openai-compatible" >&2
  exit 1
fi

shift || true
PROVIDER="${KB_PROVIDER:-none}"
if [ "$#" -gt 0 ]; then
  case "$1" in
    none|deepseek|openai|openai-compatible)
      PROVIDER="$1"
      shift || true
      ;;
  esac
fi

case "$PROVIDER" in
  none)
    exec "$PYTHON_BIN" "$ROOT_DIR/scripts/ask-kb.py" "$QUERY" --provider none "$@"
    ;;
  deepseek)
    exec "$PYTHON_BIN" "$ROOT_DIR/scripts/ask-kb.py" "$QUERY" --provider deepseek "$@"
    ;;
  openai)
    exec "$PYTHON_BIN" "$ROOT_DIR/scripts/ask-kb.py" "$QUERY" --provider openai "$@"
    ;;
  openai-compatible)
    if [ -z "${KB_BASE_URL:-}" ] || [ -z "${KB_MODEL:-}" ]; then
      echo "openai-compatible requires KB_BASE_URL and KB_MODEL in .env" >&2
      exit 1
    fi
    exec "$PYTHON_BIN" "$ROOT_DIR/scripts/ask-kb.py" "$QUERY" \
      --provider openai-compatible \
      --base-url "$KB_BASE_URL" \
      --model "$KB_MODEL" \
      "$@"
    ;;
  *)
    echo "Unknown provider: $PROVIDER" >&2
    exit 1
    ;;
esac
