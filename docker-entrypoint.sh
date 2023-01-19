#!/usr/bin/env bash

lsof -i tcp:5432
alembic upgrade head
python3 app/main.py