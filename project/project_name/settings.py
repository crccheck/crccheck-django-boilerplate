"""
Django settings for {{ app_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import dj_database_url
from project_runpy import env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get('SECRET_KEY', 'Rotom')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get('DEBUG', False)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']  # TODO


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # support
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ app_name }}.urls'

WSGI_APPLICATION = '{{ app_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(default='sqlite:///{{ app_name }}.db')}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': os.environ.get('LOGGING_LEVEL', 'WARNING'),
        'handlers': ['console'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'readable_sql': {
            '()': 'project_runpy.ReadableSqlFilter',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'project_runpy.ColorizingStreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG' if env.get('SQL', False) else 'INFO',
            'handlers': ['console'],
            'filters': ['require_debug_true', 'readable_sql'],
            'propagate': False,
        },
        'factory': {
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
