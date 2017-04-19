# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170404_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name=b'email address')),
                ('username', models.CharField(max_length=30, verbose_name=b'username')),
                ('password', models.CharField(max_length=30, verbose_name=b'password')),
            ],
        ),
        migrations.AddField(
            model_name='choices',
            name='notes',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Notes'),
        ),
        migrations.AlterField(
            model_name='choices',
            name='choice_fields',
            field=models.IntegerField(choices=[(1, b'Your colleges organize party for you'), (2, b'Your colleges make present and you make party'), (3, b'Receive money on my birthday and organize party by my self'), (4, b'Organize a party by my self without the present from my colleagues')], default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='choices',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='polls.Choices'),
        ),
    ]