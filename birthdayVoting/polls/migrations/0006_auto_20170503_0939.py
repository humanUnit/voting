# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170503_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notes_field',
            field=models.TextField(max_length=3000, verbose_name=b'notes field'),
        ),
    ]
