# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20170503_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='choice_fields',
            field=models.IntegerField(choices=[(1, b'I would like if my colleagues organize party for me.'), (2, b'I would like if my colleagues make present and I make party.'), (3, b'I would like if my colleagues give me money on my birthday and I will organize party by my self.'), (4, b'I would like organize a party by my self without the present from my colleagues.')], default=1),
        ),
    ]
