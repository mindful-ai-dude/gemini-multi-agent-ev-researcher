#!/bin/bash
# Script to run the Next.js frontend (webui) from anywhere in the project

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_ROOT/webui"

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
  echo "[INFO] Installing frontend dependencies with pnpm..."
  pnpm install
fi

# Start the Next.js dev server
echo "[INFO] Starting frontend (Next.js) at http://localhost:3000"
pnpm dev
