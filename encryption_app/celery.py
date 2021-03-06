# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'encryption_app.settings.production')

app = Celery('encryption_app')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'clean_expired_pastes': {
        'task': 'pastes.tasks.clean_expired_pastes',
        'schedule': crontab(minute='1', hour='0', day_of_week='*'),
    },
}
