from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, blank=True)
    leader = models.CharField(max_length=8, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    logins = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{fname} {lname}".format(fname=self.first_name,
                                         lname=self.last_name)
