# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20170614_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.CharField(blank=True, max_length=30, verbose_name=b'birth date'),
        ),
    ]
