# Crea build.sh para Render
echo '#!/usr/bin/env bash
# Script de construcción para Render

set -o errexit

echo "🚀 Iniciando despliegue en Render..."

# 1. Actualizar pip
echo "📦 Actualizando pip..."
pip install --upgrade pip

# 2. Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# 3. Aplicar migraciones
echo "🗄️ Aplicando migraciones..."
python manage.py migrate --noinput

# 4. Recoger archivos estáticos
echo "📁 Recogiendo archivos estáticos..."
python manage.py collectstatic --noinput

# 5. Crear superusuario si las variables existen
echo "👤 Verificando superusuario..."
if [[ -n \"\$DJANGO_SUPERUSER_USERNAME\" ]] && [[ -n \"\$DJANGO_SUPERUSER_PASSWORD\" ]] && [[ -n \"\$DJANGO_SUPERUSER_EMAIL\" ]]; then
    echo "Creando superusuario..."
    python manage.py shell << EOF
import os
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get(\"DJANGO_SUPERUSER_USERNAME\")
email = os.environ.get(\"DJANGO_SUPERUSER_EMAIL\")
password = os.environ.get(\"DJANGO_SUPERUSER_PASSWORD\")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f\"✅ Superusuario {username} creado\")
else:
    print(f\"⚠️ Superusuario {username} ya existe\")
EOF
else
    echo "⚠️ Variables de superusuario no configuradas, saltando creación"
fi

echo "✅ Construcción completada!"' > build.sh

