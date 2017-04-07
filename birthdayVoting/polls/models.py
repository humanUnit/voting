from django.db import models

from polls.widgets import *


class Choices(models.Model):
    choice_fields = models.IntegerField(max_length=2, choices=CHOICES, default=1)


class Notes(models.Model):
    notes_field = models.TextField('notes field', max_length=30)


class Login(models.Model):
    email_address = models.CharField('email address', max_length=50)
    password = models.CharField('password', max_length=50)
    remember_me_on_this_computer = models.BooleanField(max_length=1, choices=CHECK_BOX, default=1)


class CreateAccount(models.Model):
    name = models.CharField('name', max_length=50)
    surname = models.CharField('surname', max_length=50)
    email_address = models.CharField('email address', max_length=50)
    password = models.CharField('password', max_length=50)
    confirm_password = models.CharField('confirm password', max_length=50)
