#!/usr/bin/env bash

alembic upgrade head
python3 app/main.py
