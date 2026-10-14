#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
clear 2>/dev/null || printf '\033c'
python3 xosint.py
