#!/bin/bash
set -e  # exit on error

tree
export PYTHONPATH=/app
chmod +x database/database_seed.py
python database/database_seed.py

exec flask run --host=0.0.0.0
