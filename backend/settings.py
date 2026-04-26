import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8o9n15n9kh$*o!q-h5d(nu208h(c)n!p^&mr&-%5bv=i_5%t44'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# AJOUT : Ton nom d'utilisateur PythonAnywhere pour que le site fonctionne en ligne
ALLOWED_HOSTS = ['fehizoro.pythonanywhere.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://fehizoro.pythonanywhere.com", # AJOUT pour ton futur déploiement
]

ROOT_URLCONF = 'backend.urls'

# CHEMIN VERS LE FRONTEND (Vite génère un dossier 'dist')
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend', 'dist')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [FRONTEND_DIR], # Django cherchera ton index.html ici
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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- CONFIGURATION DES FICHIERS STATIQUES ---
STATIC_URL = 'static/'

# Où Django va collecter tous les fichiers statiques pour la production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Où Django doit aller chercher les fichiers générés par React (CSS, JS)
STATICFILES_DIRS = [
    os.path.join(FRONTEND_DIR, 'assets'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CONFIGURATION DES MÉDIAS (Images des projets) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- CONFIGURATION DE L'EMAIL ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kookiesunshine23@gmail.com'
EMAIL_HOST_PASSWORD = 'hxze gfhj wsbt knac' # Ton mot de passe d'application