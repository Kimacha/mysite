from __future__ import unicode_literals
from django.db import models


# Create your models here.
class mypost(models.Model):
    tittle = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.tittle

    def __str__(self):
        return self.tittle


