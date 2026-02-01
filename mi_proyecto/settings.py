"""
Django settings for mi_proyecto project.
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# =========================
# 1. CARGA VARIABLES DE ENTORNO
# =========================
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# 2. CONFIGURACIÓN BÁSICA
# =========================
SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-local-desarrollo-123')
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# =========================
# 3. HOSTS PERMITIDOS
# =========================
ALLOWED_HOSTS = []

# Render proporciona esta variable
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    print(f"✅ Render hostname: {RENDER_EXTERNAL_HOSTNAME}")

# Hosts locales para desarrollo
ALLOWED_HOSTS.extend(['localhost', '127.0.0.1', '0.0.0.0'])

# =========================
# 4. APLICACIONES INSTALADAS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tu aplicación principal
    'tasks',
]

# =========================
# 5. MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # PARA STATIC FILES EN RENDER
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_proyecto.urls'

# =========================
# 6. TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

# =========================
# 7. BASE DE DATOS (POSTGRESQL EN RENDER / SQLITE LOCAL)
# =========================
# BASE DE DATOS
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
# =========================
# 8. VALIDACIÓN DE CONTRASEÑAS
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================
# 9. INTERNACIONALIZACIÓN
# =========================
LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# =========================
# 10. ARCHIVOS ESTÁTICOS (CRÍTICO PARA RENDER)
# =========================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Render recoge archivos aquí
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# WhiteNoise para servir archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# =========================
# 11. ARCHIVOS MEDIA
# =========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =========================
# 12. CAMPO AUTO POR DEFECTO
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# 13. SEGURIDAD PARA PRODUCCIÓN (RENDER)
# =========================
if not DEBUG:
    # Solo en producción
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Dominios permitidos para CSRF
    CSRF_TRUSTED_ORIGINS = [
        f'https://{host}' for host in ALLOWED_HOSTS if host not in ['localhost', '127.0.0.1', '0.0.0.0']
    ]
    CSRF_TRUSTED_ORIGINS.append('https://*.onrender.com')
    
    print("🔒 Modo producción activado")

# =========================
# 14. CREACIÓN AUTOMÁTICA DE SUPERUSUARIO
# =========================
# (Esto se manejará mejor en build.sh)