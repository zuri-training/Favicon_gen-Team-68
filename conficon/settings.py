import os
from pathlib import Path

import dj_database_url
from decouple import config
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "DJANGO_SECRET_KEY",
    default="django-insecure-j!4f4gj5j((ohm&4bj0gt8^stu#np3xzx6!tzgsu@=n&6v8@jt",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = [
    "148.251.6.230",
    "zurifordummies.com",
    "conficon.zurifordummies.com",
    "www.conficon.zurifordummies.com",
    "127.0.0.1",
    "conficon.herokuapp.com",
    "localhost",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Cloudinary apps
    "cloudinary_storage",
    "cloudinary",
    # Local app
    "conficon_app.apps.ConficonAppConfig",
    # Third party app
    "django_extensions",
    # Social accounts
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
]

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "conficon",
    "API_KEY": "315576426699662",
    "API_SECRET": "CHXEK8JOnuizHCwiL1DsNGPIy1w",
}
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

ROOT_URLCONF = "conficon.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

AUTHENTICATION_BACKEND = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id":
            # os.getenv('GOOGlE_CLIENT_ID'),
            "570722611011-luldu717veovbbnovt2mcsmq68eifhbi.apps.googleusercontent.com",
            "secret":
            # os.getenv('GOOGLE_SECRET'),
            "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",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
    },
    "facebook": {
        "METHOD": "oauth2",
        "SDK_URL": "//connect.facebook.net/{locale}/sdk.js",
        "SCOPE": ["email", "public_profile"],
        "AUTH_PARAMS": {"auth_type": "reauthenticate", "access_type": "online"},
        "INIT_PARAMS": {"cookie": True},
        "FIELDS": [
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "name",
            "name_format",
            "picture",
            "short_name",
        ],
        "EXCHANGE_TOKEN": True,
        "LOCALE_FUNC": "path.to.callable",
        "VERIFIED_EMAIL": False,
        "VERSION": "v13.0",
        "APP": {
            "client_id": "598815134931532",  # os.getenv("APP_ID"),  # !!! THIS App ID
            "secret":
            # os.getenv("APP_SECRET"),  # !!! THIS App Secret
            "2bf5d62e37d9793d23d586f8f536023f",
            "key": "",
        },
    },
    "github": {
        "METHOD": "oauth2",
        "APP": {
            "client_id": "b84a070a76abde434e99",
            "secret": "02f7bf7243065181f50594c93a118d7cd7b35bd0  ",
        },
        "SCOPE": [
            "user",
            "repo",
            "read:org",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
}

WSGI_APPLICATION = "conficon.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# In case you are having problems with mysql setup for now we use sqlite3 for dev database
# and if its installed successfully make sure you add 'USE_PROD=1' and 'DB_PWD='your root password'' and you install requirements
if os.getenv("USE_PROD") == "1" and os.getenv("DB_PWD"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PWD"),
            "HOST": "localhost",
            "PORT": "",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/files/"
MEDIA_ROOT = BASE_DIR / "media/files"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "conficon_app.Profile"

# Django allauth for social signin
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 4
LOGIN_REDIRECT_URL = "conficon.herokuapp.com/"

# Additional configuration settings
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'

# SMTP (Simple Mail Transfer Protocol) Config
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_HOST_USER = "youngmaurizz@gmail.com"
EMAIL_HOST_PASSWORD = "ojbivzjwdstaxcbv"
# EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

if os.getenv("USE_HEROKU"):
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES["default"].update(db_from_env)
