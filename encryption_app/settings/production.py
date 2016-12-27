# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .common import *

ROOT_DIR = environ.Path(__file__) - 3
environ.Env.read_env("{}{}".format(ROOT_DIR, '/.env'))
env = environ.Env()

DEBUG = env.bool('DJANGO_DEBUG')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

STATIC_ROOT = env('DJANGO_STATIC_ROOT')
MEDIA_ROOT = env('DJANGO_MEDIA_ROOT')

SECRET_KEY = env('DJANGO_SECRET_KEY')

ADMINS = tuple([tuple(admins.split(':')) for admins in env.list('DJANGO_ADMINS')])

DATABASES = {
    'default': env.db('DJANGO_DATABASE_URL')
}

# CELERY

CELERY_BROKER_URL = env('CELERY_BROKER_URL')


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when =False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins'],
            'propagate': True
        },
    }
}


