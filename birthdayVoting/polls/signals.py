# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='create_profile')
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
