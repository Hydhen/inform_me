from __future__ import unicode_literals

from django.db import models
from . import Staff

class Comment(models.Model):
    author = models.ForeignKey('Staff', on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{auth}".format(auth=self.author)
