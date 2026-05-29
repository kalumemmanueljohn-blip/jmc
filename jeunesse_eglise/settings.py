from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================
# SÉCURITÉ
# ============================================

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-change-this-in-production-123456789')

# DEBUG - Forcé à True pour le développement local
DEBUG = True

# Configuration de ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com', '192.168.1.*', '::1']
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com', 'http://localhost:8000', 'http://127.0.0.1:8000']

# ============================================
# APPLICATIONS INSTALLÉES
# ============================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'storages',  # ✅ AJOUTÉ pour Supabase Storage
    
    # Applications du projet
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

# ============================================
# MIDDLEWARE
# ============================================

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

# ============================================
# ROOT URLCONF
# ============================================

ROOT_URLCONF = 'jeunesse_eglise.urls'

# ============================================
# TEMPLATES
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

# ============================================
# AUTHENTIFICATION
# ============================================

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# ============================================
# DATABASE - Supabase PostgreSQL
# ============================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.nrviznchvybomvjrjnrs',
        'PASSWORD': 'Kalumeemmanuel21@',
        'HOST': 'aws-1-ca-central-1.pooler.supabase.com',
        'PORT': '6543',
    }
}

# ============================================
# SUPABASE STORAGE (pour les fichiers médias)
# ============================================

# Variables d'environnement pour Supabase (à définir sur Render)
SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://nrviznchvybomvjrjnrs.supabase.co')
SUPABASE_ACCESS_KEY = os.environ.get('SUPABASE_ACCESS_KEY', '')
SUPABASE_SECRET_KEY = os.environ.get('SUPABASE_SECRET_KEY', '')

# Configuration S3 compatible avec Supabase Storage
if SUPABASE_ACCESS_KEY and SUPABASE_SECRET_KEY:
    # Utiliser Supabase Storage en production
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    
    AWS_ACCESS_KEY_ID = SUPABASE_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY = SUPABASE_SECRET_KEY
    AWS_STORAGE_BUCKET_NAME = 'media'
    AWS_S3_ENDPOINT_URL = f'{SUPABASE_URL}/storage/v1/s3'
    AWS_S3_REGION_NAME = 'ca-central-1'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = 'public-read'
    AWS_QUERYSTRING_AUTH = False
    
    # URL publique pour les médias
    MEDIA_URL = f'{SUPABASE_URL}/storage/v1/object/public/media/'
    print(f"☁️  Utilisation de Supabase Storage: {MEDIA_URL}")
else:
    # Fallback: stockage local (développement)
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    print("📁 Utilisation du stockage local")

# ============================================
# CHANNELS / WEBSOCKET
# ============================================

ASGI_APPLICATION = 'jeunesse_eglise.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# ============================================
# INTERNATIONALISATION
# ============================================

USE_TZ = True
TIME_ZONE = 'Africa/Kinshasa'
LANGUAGE_CODE = 'fr-fr'
USE_I18N = True

# ============================================
# FICHIERS STATIQUES
# ============================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Configuration du stockage statique
if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ============================================
# UPLOAD DE FICHIERS
# ============================================

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

# ============================================
# CONFIGURATION DU CHAT
# ============================================

CHAT_TYPING_TIMEOUT = 3
CHAT_MAX_FILES_PER_MESSAGE = 5

CHAT_ALLOWED_FILE_TYPES = {
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'],
    'video': ['.mp4', '.mov', '.avi', '.mkv', '.webm'],
    'audio': ['.mp3', '.wav', '.ogg', '.m4a', '.webm'],
    'document': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx'],
}

CHAT_MAX_FILE_SIZES = {
    'image': 5 * 1024 * 1024,
    'video': 20 * 1024 * 1024,
    'audio': 10 * 1024 * 1024,
    'document': 10 * 1024 * 1024,
    'default': 10 * 1024 * 1024,
}

CHAT_MESSAGES_PER_PAGE = 50
CHAT_MAX_CONVERSATIONS = 50
CHAT_AUTO_MODERATION_DELAY = 0
CHAT_FILTERED_WORDS = []

# ============================================
# SÉCURITÉ PRODUCTION
# ============================================

if not DEBUG:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_BROWSER_XSS_FILTER = False
    SECURE_CONTENT_TYPE_NOSNIFF = False

# ============================================
# INFORMATIONS DE DÉBOGAGE
# ============================================

if DEBUG:
    print("=" * 50)
    print("🔧 MODE DÉVELOPPEMENT ACTIVÉ")
    print(f"✅ DEBUG = {DEBUG}")
    print(f"🌐 MEDIA_URL: {MEDIA_URL}")
    print(f"🌐 STATIC_URL: {STATIC_URL}")
    print(f"🌍 ALLOWED_HOSTS: {ALLOWED_HOSTS}")
    if SUPABASE_ACCESS_KEY:
        print("☁️  Supabase Storage: CONNECTÉ")
    else:
        print("📁 Stockage local: ACTIF")
    print("=" * 50)
else:
    print("🚀 MODE PRODUCTION ACTIVÉ")
