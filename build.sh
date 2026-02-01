#!/usr/bin/env bash
set -o errexit

echo "=== INICIANDO BUILD ==="
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

echo "=== INSTALANDO DEPENDENCIAS ==="
pip install --upgrade pip
echo "Requirements.txt contenido:"
cat requirements.txt
pip install -r requirements.txt

echo "=== VERIFICANDO INSTALACIONES ==="
pip list | grep -i gunicorn || echo "GUNICORN NO INSTALADO"
pip list | grep -i django || echo "DJANGO NO INSTALADO"

echo "=== APLICANDO MIGRACIONES ==="
python manage.py migrate --noinput

echo "=== COLECTANDO STATIC FILES ==="
python manage.py collectstatic --noinput

echo "=== BUILD COMPLETADO ==="