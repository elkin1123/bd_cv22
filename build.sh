#!/usr/bin/env bash
echo "=========================================="
echo "🚀 INSTALANDO DEPENDENCIAS"
echo "=========================================="

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate --noinput

# Colectar archivos estáticos
python manage.py collectstatic --noinput

echo "=========================================="
echo "✅ CONSTRUCCIÓN COMPLETADA"
echo "=========================================="