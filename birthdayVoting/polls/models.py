from django.db import models
from polls.choices import *


class Notes(models.Model):
    notes_field = models.TextField('notes field', max_length=30)


class Choices(models.Model):
    choice_fields = models.IntegerField(choices=CHOICES, default=1)
    notes = models.OneToOneField(Notes, related_name='choices', default=True)
