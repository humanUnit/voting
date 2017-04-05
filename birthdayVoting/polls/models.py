from django.db import models

from polls.choices import *


class Choices(models.Model):
    choice_fields = models.IntegerField(max_length=2, choices=CHOICES, default=1)


class Notes(models.Model):
    notes_field = models.TextField('notes field', max_length=30)
