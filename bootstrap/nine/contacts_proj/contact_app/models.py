from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.DateField()
    number = models.CharField(max_length=13)
    address = models.CharField(max_length=20)

