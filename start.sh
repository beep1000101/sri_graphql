#!/bin/bash
set -e  # exit on error

python database/database_seed.py

exec flask run --host=0.0.0.0
