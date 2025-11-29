#!/usr/bin/env bash

# --- Usage ---
usage() {
    echo "Usage: $0 [-f]"
    echo "  -f    Force re-run even if STARTER_STARTED is already set"
    exit 1
}

# --- Parse flags ---
FORCE=0
while getopts ":f" opt; do
    case "$opt" in
        f) FORCE=1 ;;
        *) usage ;;
    esac
done

# --- Guard unless forced ---
if [[ -n "$STARTER_STARTED" && $FORCE -eq 0 ]]; then
    echo "starter.sh: already initialized (STARTER_STARTED set). Use -f to force."
    exit 0
fi

# --- Discover repo root (this script's directory) ---
# Resolve dir even if called through symlink
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- File paths (repo-relative) ---
COMPLETION_FILE="$SCRIPT_DIR/completions/persona_db-completion.bash"
VENV_ACTIVATE="$SCRIPT_DIR/venv/bin/activate"

# --- Check existence ---
if [[ ! -f "$COMPLETION_FILE" ]]; then
    echo "Missing: $COMPLETION_FILE"
    exit 1
fi

if [[ ! -f "$VENV_ACTIVATE" ]]; then
    echo "Missing: $VENV_ACTIVATE"
    exit 1
fi

# --- Source files ---
# shellcheck disable=SC1090
source "$COMPLETION_FILE"

# shellcheck disable=SC1090
source "$VENV_ACTIVATE"

# --- Mark environment started ---
export STARTER_STARTED=1
echo "starter.sh: environment initialized from $SCRIPT_DIR"

