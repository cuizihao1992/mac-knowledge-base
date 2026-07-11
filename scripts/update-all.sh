#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if [ -x "$ROOT_DIR/.venv/bin/python" ]; then
  PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
fi

run_step() {
  local title="$1"
  shift
  printf '\n==> %s\n' "$title"
  "$@"
}

run_step "Extract CETC project assets" "$PYTHON_BIN" scripts/extract-cetc-assets.py
run_step "Extract high-value CETC assets" "$PYTHON_BIN" scripts/deep-extract-cetc-assets.py
run_step "Refresh CETC cleanup command plan" "$PYTHON_BIN" scripts/plan-cetc-cleanup.py
run_step "Build website data" "$PYTHON_BIN" scripts/build-site.py
run_step "Build AI corpus" "$PYTHON_BIN" scripts/build-corpus.py
run_step "Build local vector index" "$PYTHON_BIN" scripts/build-vector-index.py

run_step "Check Python scripts" "$PYTHON_BIN" -m py_compile scripts/*.py
run_step "Check frontend JavaScript" node --check docs/app.js
run_step "Check website JSON" "$PYTHON_BIN" -c "import json; json.load(open('docs/data.json'))"
run_step "Check corpus manifest" "$PYTHON_BIN" -c "import json; json.load(open('data/manifest.json'))"
run_step "Check vector manifest" "$PYTHON_BIN" -c "import json; json.load(open('data/vector-index/manifest.json'))"

rm -rf scripts/__pycache__

printf '\nDone. Review changes with:\n  git status --short\n  git diff --stat\n'
