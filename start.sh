#!/bin/bash
set -e

python database/database_seed.py

exec flask run --host=0.0.0.0
