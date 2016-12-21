# -*- coding: utf-8 -*-
import datetime
import random
import string

from django.db import models

EXPIRY_CHOICES = (
    (1, '1 Day'),
    (2, '2 Days'),
    (5, '5 Days'),
    (7, '1 Week'),
    (14, '2 Weeks'),
)


class EncryptedPaste(models.Model):

    id = models.CharField(max_length=16, primary_key=True, editable=False)

    text = models.TextField()
    expiry = models.PositiveSmallIntegerField(choices=EXPIRY_CHOICES)

    expiry_date = models.DateField(editable=False)
    created_date = models.DateField(editable=False)

    def generate_id(self):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = datetime.date.today()
            self.expiry_date = self.created_date + datetime.timedelta(days=self.expiry)
            self.id = self.generate_id()
        return super(EncryptedPaste, self).save(*args, **kwargs)
