# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sensors(models.Model):

    #__Sensors_FIELDS__
    temperature setpoint auto = models.IntegerField(null=True, blank=True)
    temperature setpoint manual = models.IntegerField(null=True, blank=True)
    temperature measured = models.IntegerField(null=True, blank=True)
    battery status = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(null=True, blank=True)

    #__Sensors_FIELDS__END

    class Meta:
        verbose_name        = _("Sensors")
        verbose_name_plural = _("Sensors")


class Loghistory(models.Model):

    #__Loghistory_FIELDS__
    log = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Loghistory_FIELDS__END

    class Meta:
        verbose_name        = _("Loghistory")
        verbose_name_plural = _("Loghistory")



#__MODELS__END
