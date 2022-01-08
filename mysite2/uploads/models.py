from django.db import models

# Create your models here


class User(models.Model):
    name = models.CharField(max_length=128)
    img = models.ImageField(upload_to='images/', verbose_name='用户头像')
    introduce = models.FileField(upload_to='introduce/', verbose_name='个人简历')

    def __str__(self):
        return self.name

