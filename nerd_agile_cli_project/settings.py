"""
Django settings for nerd_agile_cli_project project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from time import sleep

from Crypto.PublicKey import RSA

rsa_private_key_path = os.environ.get('RSA_PRIVATE_KEY') or 'rsa_private.pem'
rsa_public_key_path = os.environ.get('RSA_PUBLIC_KEY') or 'rsa_public.pem'
PROD = os.getenv("APP_PROD_ENV") is not None and os.getenv("APP_PROD_ENV").upper() == 'TRUE'

if not os.path.exists(rsa_private_key_path) or not os.path.exists(rsa_public_key_path):
    print('[+] generating RSA keys')
    keys = RSA.generate(4096)
    with open(rsa_private_key_path, 'w') as f:
        f.write(keys.exportKey('PEM', pkcs=1).decode('utf-8'))
    with open(rsa_public_key_path, 'w') as f:
        f.write(keys.publickey().exportKey('PEM', pkcs=1).decode('utf-8'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not PROD or (os.getenv("APP_DEBUG") is not None and os.getenv("APP_DEBUG").upper() == 'TRUE')
DEBUG = False
if not PROD:
    with os.popen('docker ps | grep docker_nerd_agile_cli_db') as p:
        if (p.read() == ''):
            print("[+] Starting docker env")
            os.system("docker-compose -f ./docker/docker-compose.yml up -d --remove-orphans")
            sleep(10)
            print("[+] docker env started")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_ROOT = os.path.join(BASE_DIR, "frontend/templates")
STATIC_ROOT = os.path.join(BASE_DIR, "frontend/static")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3)+bd8z*zx+yf0e^ii$!zcl5d23l5e+-ww$cnnvxhvx-%g8v_x' if not PROD else os.getenv("DJANGO_SECRET_KEY")


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nerd_agile_cli_rest_api'
]

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

ROOT_URLCONF = 'nerd_agile_cli_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_ROOT],
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

WSGI_APPLICATION = 'nerd_agile_cli_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {}
if PROD:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            'NAME': os.getenv("APP_DATABASE_NAME"),
            'USER': os.getenv("APP_DATABASE_USER"),
            'PASSWORD': os.getenv("APP_DATABASE_PASSWORD"),
            'HOST': os.getenv("APP_DATABASE_HOST"),
            'PORT': os.getenv("APP_DATABASE_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            'NAME': 'nerdagilecli',
            'USER': 'nerdagilecli_user',
            'PASSWORD': 'nerdagilecli_pass',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
