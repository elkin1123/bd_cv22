#!/usr/bin/env bash
# build.sh FORZADO

echo "=========================================="
echo "🚀 EJECUTANDO MIGRACIONES FORZADAS"
echo "=========================================="

# 1. Instalar dependencias MÍNIMAS
pip install Django==4.2.16
pip install psycopg2-binary==2.9.11

# 2. EJECUTAR MIGRACIONES - ESTO ES LO CRÍTICO
echo "🗄️  EJECUTANDO MIGRACIONES DE BASE DE DATOS..."
python manage.py migrate --noinput

# 3. Si falla, mostrar error específico
if [ $? -eq 0 ]; then
    echo "✅ MIGRACIONES EXITOSAS"
else
    echo "❌ ERROR EN MIGRACIONES"
    # Mostrar qué migraciones están pendientes
    python manage.py showmigrations
fi

# 4. Instalar el resto
pip install -r requirements.txt

# 5. Archivos estáticos
python manage.py collectstatic --noinput

echo "=========================================="
echo "✅ CONSTRUCCIÓN COMPLETADA"
echo "=========================================="