from __future__ import unicode_literals

from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{name}".format(name=self.name)
