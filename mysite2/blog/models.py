from django.db import models

# Create your models here.
from django.db import models

# 博客栏目
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# 作者
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

# 文章
# 希望查询的结果是哪个模型的实例，就用哪个模型去调用！
class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries')  # 外键关联到一个博客栏目
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)    # 多对多关联到一些作者
    number_of_comments = models.IntegerField()  # 评论数
    number_of_pingbacks = models.IntegerField()  # 点赞数
    rating = models.IntegerField()   # 好评率星

    def __str__(self):
        return self.headline

import uuid


class MyManager(models.Manager):

    def info(self, id):
        obj = super().get(id=id)
        return "%s  %s  %s  %s" %(obj.name, obj.sex, obj.tel, obj.uuid)



class Student(models.Model):

    sex_choice = [
        ('man', '男性'),
        ('woman', '女性'),
    ]

    name = models.CharField(max_length=128)
    sex = models.CharField(max_length=8, choices=sex_choice)
    tel = models.PositiveIntegerField()
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    objects = models.Manager()  # 显式的指定
    info_manager = MyManager()  # 自定义的管理器

    def __str__(self):
        return self.name

    #admin,drf,feed
    def get_absolute_url(self):
        from django.urls import reverse
        if self.sex == 'man':
            return reverse('blog:man', args=(self.id,))
        else:
            return reverse('blog:woman', args=(self.id,))

from django.db.models import Lookup
from django.db.models import Field, IntegerField


@Field.register_lookup
class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' %(lhs, rhs), params

from django.db.models import Transform

class AbsoluteValue(Transform):
    lookup_name = 'abs'
    function = 'ABS'  # 数据库内置的一个绝对值方法

IntegerField.register_lookup(AbsoluteValue)






