# settings.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%)%=c0w!d7uu6d)3sxg!b#$^pt!-v(3z3zpsdb8citp6ru@iaf'

# Modo “producción local” (web embebida)
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8001", "http://localhost:8001"]

# ======= Apps ==============================================================
INSTALLED_APPS = [
    'core',
    # 'stocktoner',  # (si tenés templates/archivos dentro de esa app)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # (OPCIONAL) formularios lindos con Bootstrap 5
    # 'crispy_forms',
    # 'crispy_bootstrap5',
]

# ======= Middleware ========================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise: sirve archivos estáticos con DEBUG=False
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stocktoner.urls'

# ======= Templates =========================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Si querés una carpeta global de templates además de los de cada app:
        'DIRS': [
            # BASE_DIR / "templates",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.static',   # <-- agregado
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stocktoner.wsgi.application'

# ======= Base de datos =====================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Para un build one-folder de PyInstaller, esto funciona bien.
        # (Si más adelante instalás en "C:\Program Files", conviene mover la DB
        # a %LOCALAPPDATA% y ajustarlo aquí.)
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ======= Password validators ==============================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ======= i18n / zona horaria ==============================================
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Cordoba'
USE_I18N = True
USE_TZ = True

# ======= Static / archivos estáticos ======================================
# En templates usás: {% load static %}  y  href="{% static 'vendor/bootstrap/css/bootstrap.min.css' %}"
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"   # acá vive todo en el build

# WhiteNoise: compresión y cacheo (simple, sin manifest para evitar sorpresas)
# Si querés hashing de archivos (cache busting), cambiá a CompressedManifestStaticFilesStorage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Si tenés una carpeta "static" de proyecto además de "core/static/", habilitala:
# STATICFILES_DIRS = [ BASE_DIR / "static" ]

# ======= Cookies/HTTPS para entorno local embebido =========================
# Estamos sirviendo http://127.0.0.1:8001 dentro de pywebview, sin HTTPS:
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# ======= Primary key por defecto ==========================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ======= (OPCIONAL) crispy-forms con Bootstrap 5 ==========================
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
# CRISPY_TEMPLATE_PACK = "bootstrap5"

# ======= (OPCIONAL) Login redirects =======================================
# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'home'
