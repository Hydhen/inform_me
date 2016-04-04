from __future__ import unicode_literals

from django.db import models

class Staff(models.Model):
    login = models.CharField(max_length=8, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{fname} {lname}".format(fname=self.first_name,
                                         lname=self.last_name)
