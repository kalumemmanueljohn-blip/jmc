from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ==================================================
# SÉCURITÉ
# ==================================================

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-change-this-in-production'
)

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
    '::1',
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# ==================================================
# APPLICATIONS INSTALLÉES
# ==================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'whitenoise.runserver_nostatic',
    'storages',

    # Apps
    'core',
    'accounts',
    'events',
    'teachings',
    'blog',
    'donations',
    'gallery',
    'chat',
    'channels',
]

# ==================================================
# MIDDLEWARE
# ==================================================

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

# ==================================================
# URLS
# ==================================================

ROOT_URLCONF = 'jeunesse_eglise.urls'

# ==================================================
# TEMPLATES
# ==================================================

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

WSGI_APPLICATION = 'jeunesse_eglise.wsgi.application'
ASGI_APPLICATION = 'jeunesse_eglise.asgi.application'

# ==================================================
# BASE DE DONNÉES - SUPABASE POSTGRESQL
# ==================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'postgres'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '6543'),
    }
}

# ==================================================
# AUTHENTIFICATION
# ==================================================

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# ==================================================
# INTERNATIONALISATION
# ==================================================

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Kinshasa'

USE_I18N = True
USE_TZ = True

# ==================================================
# FICHIERS STATIQUES
# ==================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

# ==================================================
# SUPABASE STORAGE (MÉDIAS)
# ==================================================

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_ACCESS_KEY = os.environ.get('SUPABASE_ACCESS_KEY')
SUPABASE_SECRET_KEY = os.environ.get('SUPABASE_SECRET_KEY')

# IMPORTANT
# Ton bucket doit s'appeler : media

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = SUPABASE_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = SUPABASE_SECRET_KEY

AWS_STORAGE_BUCKET_NAME = 'media'

AWS_S3_ENDPOINT_URL = f'{SUPABASE_URL}/storage/v1/s3'

AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_FILE_OVERWRITE = False

# URL publique des fichiers
MEDIA_URL = f'{SUPABASE_URL}/storage/v1/object/public/media/'

# ==================================================
# UPLOAD DE FICHIERS
# ==================================================

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

# ==================================================
# CHANNELS
# ==================================================

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# ==================================================
# CHAT
# ==================================================

CHAT_TYPING_TIMEOUT = 3
CHAT_MAX_FILES_PER_MESSAGE = 5

CHAT_ALLOWED_FILE_TYPES = {
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    'video': ['.mp4', '.mov', '.avi', '.mkv'],
    'audio': ['.mp3', '.wav', '.ogg'],
    'document': [
        '.pdf',
        '.doc',
        '.docx',
        '.txt',
        '.xls',
        '.xlsx',
        '.ppt',
        '.pptx',
    ],
}

CHAT_MAX_FILE_SIZES = {
    'image': 5 * 1024 * 1024,
    'video': 20 * 1024 * 1024,
    'audio': 10 * 1024 * 1024,
    'document': 10 * 1024 * 1024,
    'default': 10 * 1024 * 1024,
}

# ==================================================
# SÉCURITÉ PRODUCTION
# ==================================================

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ==================================================
# DEBUG
# ==================================================

print("=" * 50)
print("🚀 CONFIG DJANGO")
print(f"DEBUG: {DEBUG}")
print(f"MEDIA_URL: {MEDIA_URL}")
print(f"SUPABASE: {SUPABASE_URL}")
print("=" * 50)
