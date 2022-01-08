from django.db import models
from django.conf import global_settings
# Create your models here.



# 多对一、多对多、一对一
class Car(models.Model):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    # manufacturer_id  1,2,3,4
    # ORM manufacturer

class Manufacturer(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        default_permissions = []
        unique_together = []

class Topping(models.Model):
    # ...
    name = models.CharField(max_length=123, default='配料',blank=True)
    def __str__(self):
        return self.name

# ORM API 不推荐在CRUD某个模型的时候同时修改它关联的多对多对象，而是分开操作
class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
    size = models.CharField(max_length=123, default=10)

    def __str__(self):
        return self.size


# class Person(models.Model):
#     name = models.CharField(max_length=50)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()


class Group(models.Model):

    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',       ## 自定义中间表
        through_fields=('group', 'person'),
    )

class Membership(models.Model):  # 这就是具体的中间表模型
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}


class Artist(models.Model):
    MEDIA_CHOICES = [
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        ('unknown', 'Unknown'),
    ]

    album = models.CharField(choices=MEDIA_CHOICES[0][1], max_length=10)
    video = models.CharField(choices=MEDIA_CHOICES[1][1], max_length=10)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    pass

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    pass


class BookReview(Book, Article):
    pass


from django.core.exceptions import ValidationError

def validate_even(value):

    if value % 2 != 0:

        raise ValidationError('%(value)s 不是一个偶数', params={'value':value})

from django.core.validators import RegexValidator

class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])


    # 自动的模型验证
    def save(self, *args, **kwargs):
        try:
            self.full_clean()
            super().save(*args, **kwargs)
        except ValidationError as e:
            print('模型没有通过验证： %s' % e.message_dict)

    def clean(self):
        pass


# 模型的验证器不会在调用save()方法的时候自动执行
# 表单的验证器会在调用save()方法的时候自动执行 is_valid()方法


# full_clean()
# clean_fields()
# clean()
# validate_unique()

# 如果你手动调用了`full_clean()`方法，那么会依次自动调用下面的三个方法
# `clean_fields()`：验证各个字段的合法性
# `clean()`：验证模型级别的合法性
# `validate_unique()`：验证字段的独一无二性



class MyModel2(models.Model):
    content = models.CharField(max_length=128, validators=[RegexValidator(regex='django', message='没有以django开头')])

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        try:
            self.full_clean()
            super().save(*args, **kwargs)
        except ValidationError as e:
            print('模型没有通过验证： %s' % e.message_dict)


