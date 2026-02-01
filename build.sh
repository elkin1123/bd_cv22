#!/usr/bin/env bash

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario automáticamente
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_elkin.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'admin'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email='elkinjoshuadelgadolesp68@gmail.com',
        password='Admin123456!'
    )
    print(f'✅ Usuario {username} creado')
"

# Colectar archivos estáticos
python manage.py collectstatic --noinput