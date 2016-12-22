# -*- coding: utf-8 -*-

import datetime

from celery import shared_task

from .models import EncryptedPaste


@shared_task
def clean_expired_pastes():
    today = datetime.date.today()
    for paste in EncryptedPaste.objects.all():
        if today > paste.expiry_date:
            paste.delete()
