from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ==================================================
# SÉCURITÉ
# ==================================================

SECRET_KEY = 'django-insecure-change-this-in-production-123456789'

# DEBUG forcé à True pour le développement local
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '::1']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000']

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
    
    # Tes apps
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
# BASE DE DONNÉES - SQLite (pour local)
# ==================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==================================================
# FICHIERS MÉDIAS (stockage local)
# ==================================================

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Stockage local
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

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
    'document': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
}

CHAT_MAX_FILE_SIZES = {
    'image': 5 * 1024 * 1024,
    'video': 20 * 1024 * 1024,
    'audio': 10 * 1024 * 1024,
    'document': 10 * 1024 * 1024,
    'default': 10 * 1024 * 1024,
}

# ==================================================
# CRÉATION AUTO DES DOSSIERS MEDIA
# ==================================================

os.makedirs(MEDIA_ROOT, exist_ok=True)

MEDIA_SUBFOLDERS = [
    'gallery',
    'gallery/videos',
    'gallery/thumbnails',
    'blog',
    'events',
    'teachings',
    'profiles',
    'chat',
    'donations',
]

for subfolder in MEDIA_SUBFOLDERS:
    folder_path = os.path.join(MEDIA_ROOT, subfolder)
    os.makedirs(folder_path, exist_ok=True)

# ==================================================
# DEBUG INFO
# ==================================================

print("=" * 50)
print("🔧 MODE DÉVELOPPEMENT LOCAL ACTIVÉ")
print(f"✅ DEBUG: {DEBUG}")
print(f"📁 MEDIA_ROOT: {MEDIA_ROOT}")
print(f"📁 STATIC_ROOT: {STATIC_ROOT}")
print(f"🌐 MEDIA_URL: {MEDIA_URL}")
print(f"🌐 STATIC_URL: {STATIC_URL}")
print("=" * 50)
