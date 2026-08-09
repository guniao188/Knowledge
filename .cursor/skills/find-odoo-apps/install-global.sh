#!/usr/bin/env bash
# Install find-odoo-apps into the user-global Cursor skills directory.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_ROOT="${HOME}/.cursor/skills"
TARGET="${TARGET_ROOT}/find-odoo-apps"

if [[ ! -f "${SCRIPT_DIR}/SKILL.md" ]]; then
  echo "error: SKILL.md not found next to this script: ${SCRIPT_DIR}" >&2
  exit 1
fi

mkdir -p "${TARGET_ROOT}"
rm -rf "${TARGET}"
mkdir -p "${TARGET}"
# Copy skill contents; skip the installer itself from being required at runtime
cp -R "${SCRIPT_DIR}/." "${TARGET}/"

echo "Installed global skill:"
echo "  ${TARGET}/SKILL.md"
echo
echo "Next: fully quit and restart Cursor, then check Customize → Skills for find-odoo-apps"
echo "Try in any project: /find-odoo-apps"
