# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 13:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170418_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='choices',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]