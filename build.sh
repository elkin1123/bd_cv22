#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== INICIANDO DESPLIEGUE EN RENDER ==="

# 1. Instalar dependencias
echo "1. Instalando dependencias..."
pip install -r requirements.txt

# 2. Colectar archivos estáticos
echo "2. Colectando archivos estáticos..."
python manage.py collectstatic --no-input

# 3. Aplicar migraciones
echo "3. Aplicando migraciones..."
python manage.py migrate

# 4. Importar datos (si existe el archivo)
echo "4. Verificando datos para importar..."
if [ -f "datos_backup.json" ]; then
    echo "   Encontrado datos_backup.json, importando..."
    python import_data.py
else
    echo "   No hay datos_backup.json, creando superusuario por defecto..."
    python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Admin123')
    print('Superusuario admin creado')
else:
    print('Superusuario ya existe')
"
fi

echo "=== DESPLIEGUE COMPLETADO ==="