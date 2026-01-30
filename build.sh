#!/usr/bin/env bash
set -o errexit

echo "=== INICIANDO DESPLIEGUE ==="

pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear

echo "=== DESPLIEGUE COMPLETADO ==="