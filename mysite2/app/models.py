from django.db import models
# Create your models here.
from django.utils.html import format_html
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    def colored_name(self):
        # 关键是这句！！！！！请自己调整缩进。
        return format_html('<span style="color: red;">%s</span>' % self.name)
    colored_name.short_description = '带颜色的名字'
    colored_name.admin_order_field = 'name'


class Person(models.Model):
    name = models.CharField(max_length=100)
    flag = models.BooleanField(default=True)

    def flag_is_true(self):
        return self.flag == True

    flag_is_true.boolean = True

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    editor = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name='编辑',null=True,blank=True)

    # comments = GenericRelation('Comment')





class Comment(models.Model):
    """
    评论模型，可以针对book、author、person评论
    """
    body = models.CharField(max_length=200)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return self.body