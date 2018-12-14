"""
Django settings for XP project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import datetime
import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# TODO: SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1(+89v5d#vrkc)9@jdka5rb5shkd(wa69zu9szi0xkevjp#o(-'

# TODO: SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# admins which get error messages when DEBUG is set to false
ADMINS = [('sajad', 'majidstic@yahoo.com'), ('mahdi', '')]

# settings for caching
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': '/var/tmp/django_cache',
#     }
# }

# A string containing a dotted path to a function (or any callable) that defines how to compose a prefix,
# version and key into a final cache key.
# KEY_FUNCTION : def make_key(key, key_prefix, version):
#     return ':'.join([key_prefix, str(version), key])

# A string that will be automatically included (prepended by default) to all cache keys used by the Django server.
# KEY_PREFIX = ''

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'game',
    'maingame',
    'rest_framework',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'XP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'XP.wsgi.application'

# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xp_db',
        'USER': 'xp_user',  # username of database
        'PASSWORD': '1234',  # password of database
        'HOST': '127.0.0.1',  # set to localhost or '127.0.0.1' for tcp connection
        'PORT': '',
        'CONN_MAX_AGE': 0, # if set to 'None' it will create persistent connection with db
    }
}

# maximum request body before raising exception
DATA_UPLOAD_MAX_MEMORY_SIZE = 5221440

# default email address for automated email response
# DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# the backend to use for sending emails
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# json web token settings
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'fa-IR'

LANGUAGES = [
    ('en', _('English')),
    ('fa-IR', _('Farsi')),
]

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
