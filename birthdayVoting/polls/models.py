from django.conf import settings
from django.db import models
from .choices import CHOICES


class Notes(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    notes_field = models.TextField('notes field', max_length=3000)


class Choices(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice_fields = models.IntegerField(choices=CHOICES, default=1)
