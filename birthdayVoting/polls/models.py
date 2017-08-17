from django.conf import settings
from django.db import models

from .choices import CHOICES

from django.contrib.auth.models import User


class Notes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    notes_field = models.TextField('notes field', max_length=3000,)


class Choices(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice_fields = models.IntegerField(choices=CHOICES, default=1)

    def __unicode__(self):
        #TODO: (change it)
        return CHOICES[self.choice_fields][1]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)


class ChoicesCreate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    choice_field = models.TextField('choice field', max_length=400)
