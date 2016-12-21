# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-21 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EncryptedPaste',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('expiry', models.PositiveSmallIntegerField(choices=[(1, b'1 Day'), (2, b'2 Days'), (5, b'5 Days'), (7, b'1 Week'), (14, b'2 Weeks')])),
                ('expiry_date', models.DateField(editable=False)),
                ('created_date', models.DateField(editable=False)),
            ],
        ),
    ]
