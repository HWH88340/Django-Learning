from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Job(models.Model):
    department = models.CharField(max_length=16)
    position = models.CharField(max_length=16)
    responsiblities = models.CharField(max_length=128)
