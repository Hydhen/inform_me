from __future__ import unicode_literals

from django.db import models
from . import Staff
from . import Project

class Comment(models.Model):
    author = models.ForeignKey('Staff', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{auth}".format(auth=self.author)
