# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-22 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedpaste',
            name='id',
            field=models.CharField(editable=False, max_length=16, primary_key=True, serialize=False),
        ),
    ]
