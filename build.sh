#!/usr/bin/env bash
# build.sh para Render.com

echo "=========================================="
echo "🚀 INICIANDO DESPLIEGUE EN RENDER"
echo "=========================================="

# 1. Verificar Python
python --version

# 2. Actualizar pip
echo "📦 Actualizando pip..."
pip install --upgrade pip

# 3. Instalar dependencias CRÍTICAS primero
echo "📦 Instalando Django y dependencias..."
pip install Django==4.2.16
pip install gunicorn==23.0.0
pip install whitenoise==6.11.0
pip install psycopg2-binary==2.9.11
pip install dj-database-url==3.1.0
pip install python-dotenv==1.0.0

# 4. Instalar el resto de requirements.txt
echo "📦 Instalando otras dependencias..."
pip install -r requirements.txt

# 5. EJECUTAR MIGRACIONES - ESTO ES LO MÁS IMPORTANTE
echo "🗄️  CREANDO MIGRACIONES Y TABLAS..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# 6. Archivos estáticos
echo "📁 Recogiendo archivos estáticos..."
python manage.py collectstatic --noinput

# 7. Crear superusuario si no existe (OPCIONAL)
echo "👤 Configurando superusuario..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✅ Superusuario creado: admin / admin123')
else:
    print('✅ Superusuario ya existe')
"

echo "=========================================="
echo "✅ DESPLIEGUE COMPLETADO EXITOSAMENTE"
echo "=========================================="