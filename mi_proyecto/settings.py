"""
Django settings for mi_proyecto project.
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# SECURITY / DEBUG
# =========================
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-dev-key-temporal-cambiar-en-produccion'
)

DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# =========================
# ALLOWED HOSTS (Render)
# =========================
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
else:
    ALLOWED_HOSTS.extend(['localhost', '127.0.0.1'])

# =========================
# APPS (SOLO APPS NECESARIAS)
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Cloudinary (si lo usas)
    'cloudinary_storage',
    'cloudinary',

    # Tu aplicación personalizada
    'tasks',
]

# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# URLS / WSGI
# =========================
ROOT_URLCONF = 'mi_proyecto.urls'
WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

# =========================
# TEMPLATES
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

# =========================
# DATABASE
# =========================
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# =========================
# STATIC FILES
# =========================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / 'static',
] if os.path.exists(BASE_DIR / 'static') else []

# =========================
# MEDIA / CLOUDINARY
# =========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# CONFIGURACIÓN CORREGIDA PARA DJANGO 4.2+
# Usa SOLO STORAGES, NO DEFAULT_FILE_STORAGE
if all([CLOUDINARY_STORAGE['CLOUD_NAME'], 
        CLOUDINARY_STORAGE['API_KEY'], 
        CLOUDINARY_STORAGE['API_SECRET']]):
    # Si Cloudinary está configurado
    STORAGES = {
        "default": {
            "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
else:
    # Si NO hay Cloudinary, usa sistema de archivos local
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

# =========================
# DEFAULT AUTO FIELD
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# SECURITY (Render)
# =========================
CSRF_TRUSTED_ORIGINS = []

if RENDER_EXTERNAL_HOSTNAME:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_TRUSTED_ORIGINS = [
        f'https://{RENDER_EXTERNAL_HOSTNAME}',
        'https://*.onrender.com',
    ]
else:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    CSRF_TRUSTED_ORIGINS = [
        'http://localhost:8000',
        'http://127.0.0.1:8000',
    ]

# =========================
# X-FRAME
# =========================
X_FRAME_OPTIONS = 'SAMEORIGIN'