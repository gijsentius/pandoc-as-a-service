#!/bin/sh

set -e
source venv/bin/activate
# uvicorn service.main:app --host 0.0.0.0 --port 80
uvicorn service.main:app --reload
