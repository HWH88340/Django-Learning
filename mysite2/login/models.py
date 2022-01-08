from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        permissions = (
            ('can_drive', '可以驾驶'),
            ('can_fix', '可以维修'),
        )


class MyUser(AbstractUser):
    """新的用户模型，取代内置的User模型"""
    address = models.CharField(max_length=128, null=True,blank=True)
    education = models.CharField(max_length=128, null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)


def get_anonymous_user_instance(User):
    return User(username='Anonymous', address='beijing', education='master')


# 工作任务模型
class Task(models.Model):
    summary = models.CharField(max_length=32)			# 任务摘要
    content = models.TextField()			# 任务文本
    reported_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)   # 报告人
    created_at = models.DateTimeField(auto_now_add=True)	    # 创建时间

    class Meta:
        permissions = (
            ('assign_task', '分配任务的权限'),    # 自定义一个权限
        )