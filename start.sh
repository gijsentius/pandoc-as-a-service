#!/bin/sh

source venv/bin/activate
uvicorn service.main:app --host 0.0.0.0 --port 80