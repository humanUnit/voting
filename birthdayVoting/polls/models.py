from django.conf import settings
from django.db import models
from polls.choices import *


class Notes(models.Model):
    notes_field = models.TextField('notes field', max_length=3000)


class Choices(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice_fields = models.IntegerField(choices=CHOICES, default=1)
    notes = models.OneToOneField(Notes, related_name='choices', blank=True, null=True)
