"""
Django settings para Render.com
Configuración optimizada para producción
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# ============================================
# 1. CARGA DE VARIABLES DE ENTORNO
# ============================================
load_dotenv()

# Directorio base
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================
# 2. SEGURIDAD - VARIABLES CRÍTICAS
# ============================================
# SECRET_KEY - OBLIGATORIO EN PRODUCCIÓN
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY and os.environ.get('RENDER'):
    raise ValueError("❌ ERROR: SECRET_KEY no configurada en producción")

# DEBUG - Siempre False en Render
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ============================================
# 3. HOSTS PERMITIDOS
# ============================================
# En la sección ALLOWED_HOSTS:
ALLOWED_HOSTS = ['bd-cv22.onrender.com', 'localhost', '127.0.0.1']

# Render automáticamente agrega el hostname
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    
# DEBUG debe ser False en producción
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ============================================
# 4. APLICACIONES
# ============================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tus aplicaciones
    'tasks',  # Cambia esto por tu app
]

# ============================================
# 5. MIDDLEWARE
# ============================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # IMPORTANTE: Debe ir después de SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_proyecto.urls'

# ============================================
# 6. TEMPLATES
# ============================================
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

# ============================================
# 7. BASE DE DATOS
# ============================================
# Configuración automática para Render
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # SQLite para desarrollo local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ============================================
# 8. VALIDACIÓN DE CONTRASEÑAS
# ============================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================
# 9. INTERNACIONALIZACIÓN
# ============================================
LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# ============================================
# 10. ARCHIVOS ESTÁTICOS (CRÍTICO PARA RENDER)
# ============================================
STATIC_URL = '/static/'

# En producción (Render), usa esta ruta
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    
    # Configuración de WhiteNoise
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    # En desarrollo
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

# ============================================
# 11. ARCHIVOS MEDIA
# ============================================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ============================================
# 12. CONFIGURACIÓN DEFAULT
# ============================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================
# 13. CONFIGURACIÓN DE SEGURIDAD EN PRODUCCIÓN
# ============================================
if not DEBUG:
    # HTTPS
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    
    # Cookies seguras
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Headers de seguridad
    SECURE_HSTS_SECONDS = 31536000  # 1 año
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # CSRF
    CSRF_TRUSTED_ORIGINS = [
        'https://*.onrender.com',
        f'https://{RENDER_EXTERNAL_HOSTNAME}',
    ]

# ============================================
# 14. LOGGING - Para ver errores en Render
# ============================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# ============================================
# 15. CONFIGURACIONES ESPECÍFICAS DE RENDER
# ============================================
# Esta variable existe cuando estamos en Render
if os.environ.get('RENDER'):
    print("✅ Ejecutando en Render.com")
    print(f"✅ Hostname: {RENDER_EXTERNAL_HOSTNAME}")
    print(f"✅ DEBUG: {DEBUG}")