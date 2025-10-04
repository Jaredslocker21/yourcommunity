"""
Django settings for yourcommunity project.
"""

from pathlib import Path
import os
import dj_database_url
from django.contrib.messages import constants as messages

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# --- Security / Debug ---
SECRET_KEY = os.getenv("SECRET_KEY", "dev-please-change-me")
DEBUG = os.getenv("DEBUG", "1") == "1"
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".gitpod.io", "yourcommunityblog.herokuapp.com"]

X_FRAME_OPTIONS = "SAMEORIGIN"

# --- Django apps ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    "django_summernote",

    "crispy_forms",
    "crispy_bootstrap5",

    "blog",
]

# Optionally enable Cloudinary in environments where CLOUDINARY_URL is set
if os.getenv("CLOUDINARY_URL"):
    INSTALLED_APPS += [
        "cloudinary_storage",
        "cloudinary",
    ]

SITE_ID = 1

# --- Auth / Allauth ---
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_EMAIL_VERIFICATION = "none"
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# --- Messages -> Bootstrap classes ---
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# --- Crispy Forms (Bootstrap 5) ---
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",

    # 👇 REQUIRED by django-allauth (newer versions)
    "allauth.account.middleware.AccountMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]



ROOT_URLCONF = "yourcommunity.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "yourcommunity.wsgi.application"

# --- Database ---
db_url = os.getenv("DATABASE_URL")
if db_url:
    DATABASES = {
        "default": dj_database_url.parse(db_url, conn_max_age=600, ssl_require=False)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- I18N ---
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --- Static / Media ---
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"

# Only use Cloudinary storages when CLOUDINARY_URL is present
if os.getenv("CLOUDINARY_URL"):
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
