#!/usr/bin/env bash
# build.sh para Render
# Exit on error
set -o errexit

echo "=== INICIANDO DESPLIEGUE EN RENDER ==="

echo "1. Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

echo "2. Aplicando migraciones..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "3. Recolectando archivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "4. Verificando superusuario..."
python manage.py shell << EOF
from django.contrib.auth.models import User
import os

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'✅ Superusuario {username} creado')
else:
    print('ℹ️ Superusuario ya existe')
EOF

echo "=== ✅ DESPLIEGUE COMPLETADO ==="