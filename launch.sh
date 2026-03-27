#!/bin/bash
# Jarves Launcher - Run from anywhere

JARVES_DIR="/home/rudran/Projects/Code/jarves"
cd "$JARVES_DIR"
source venv/bin/activate
python3 jarves.py "$@"
