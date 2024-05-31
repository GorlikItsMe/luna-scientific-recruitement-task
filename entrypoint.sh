#!/bin/bash

echo "[setup] (1/3) Migrating..."
python manage.py migrate

echo "[setup] (2/3) Collecting static files..."
python manage.py collectstatic --noinput

echo "[setup] (3/3) Starting gunicorn server..."
gunicorn core.wsgi:application --access-logfile - --workers 4 --bind 0.0.0.0:8000 --timeout 30000
