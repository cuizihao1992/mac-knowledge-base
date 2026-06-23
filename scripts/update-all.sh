#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

run_step() {
  local title="$1"
  shift
  printf '\n==> %s\n' "$title"
  "$@"
}

run_step "Extract CETC project assets" python3 scripts/extract-cetc-assets.py
run_step "Extract high-value CETC assets" python3 scripts/deep-extract-cetc-assets.py
run_step "Refresh CETC cleanup command plan" python3 scripts/plan-cetc-cleanup.py
run_step "Build website data" python3 scripts/build-site.py
run_step "Build AI corpus" python3 scripts/build-corpus.py
run_step "Build local vector index" python3 scripts/build-vector-index.py

run_step "Check Python scripts" python3 -m py_compile scripts/*.py
run_step "Check frontend JavaScript" node --check docs/app.js
run_step "Check website JSON" bash -c "python3 -m json.tool docs/data.json >/dev/null"
run_step "Check corpus manifest" bash -c "python3 -m json.tool data/manifest.json >/dev/null"
run_step "Check vector manifest" bash -c "python3 -m json.tool data/vector-index/manifest.json >/dev/null"

rm -rf scripts/__pycache__

printf '\nDone. Review changes with:\n  git status --short\n  git diff --stat\n'
