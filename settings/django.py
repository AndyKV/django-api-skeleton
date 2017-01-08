import os
import sys
import environ
from ._django_apps import DJANGO_APPS, CONTRIB_APPS, GARAGE_APPS


env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

root = environ.Path(__file__) - 2

SITE_ROOT = root()

sys.path.append(os.path.join(SITE_ROOT))

DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

SECRET_KEY = env.str('SECRET_KEY')

FEATURES = env.tuple('FEATURES', default=())

BASE_URL = env('BASE_URL')

INSTALLED_APPS = DJANGO_APPS + CONTRIB_APPS + GARAGE_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'garage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SITE_ROOT, 'templates')],
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

WSGI_APPLICATION = 'garage.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': env.db()
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(SITE_ROOT, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(SITE_ROOT, 'static'),
]

AUTH_USER_MODEL = 'user.UserProfile'

if 'SWAGGER' in FEATURES:  # pragma: no cover
    INSTALLED_APPS += ['rest_framework_swagger']

if 'DJANGO_EXTENSIONS' in FEATURES:  # pragma: no cover
    INSTALLED_APPS += ['django_extensions']

if 'SENTRY' in FEATURES:
    INSTALLED_APPS += ['raven.contrib.django.raven_compat']
