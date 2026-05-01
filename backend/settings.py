import os
from pathlib import Path

# --- CHEMINS DE BASE ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SÉCURITÉ ---
SECRET_KEY = 'django-insecure-8o9n15n9kh$*o!q-h5d(nu208h(c)n!p^&mr&-%5bv=i_5%t44'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# --- APPLICATIONS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Librairies tierces
    'rest_framework',
    'corsheaders',
    # Ton application
    'core',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Toujours en premier
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- CONFIGURATION CORS (Pour React) ---
CORS_ALLOW_ALL_ORIGINS = True  # Autorise React en local sans friction
CORS_ALLOW_CREDENTIALS = True

# --- BASE DE DONNÉES ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- URLs ---
ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'

# --- TEMPLATES ---
# On simplifie : Django cherche les templates dans le dossier FRONTEND du build
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend', 'dist')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend/dist')], 
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

# --- FICHIERS STATIQUES & MÉDIAS ---
# Configuration propre pour le développement local
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/dist'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Stockage des images hors du build React

# --- INTERNATIONALISATION ---
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Indian/Antananarivo'
USE_I18N = True
USE_TZ = True

# --- CONFIGURATION DE L'EMAIL (Gmail) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kookiesunshine23@gmail.com'
EMAIL_HOST_PASSWORD = 'hxze gfhj wsbt knac' 

# --- AUTRES ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
APPEND_SLASH = True