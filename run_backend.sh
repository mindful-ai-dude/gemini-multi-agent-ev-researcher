#!/bin/bash
# Script to run the FastAPI backend from anywhere in the project

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$SCRIPT_DIR"

cd "$SCRIPT_DIR"

# Always use the conda env Python (Python 3.12)
PYTHON_BIN="/usr/local/Caskroom/miniconda/base/envs/elv_research/bin/python"
echo "[INFO] Using Python at $PYTHON_BIN"
$PYTHON_BIN -m uvicorn backend.main:app --reload
