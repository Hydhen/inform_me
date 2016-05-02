from __future__ import unicode_literals

from django.db import models
from . import Status

class Project(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description_short = models.CharField(max_length=140, blank=True)
    description = models.TextField(blank=True)
    leader = models.CharField(max_length=8, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    logins = models.TextField(blank=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{name}".format(name=self.name)
