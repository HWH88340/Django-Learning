from django.contrib import admin
from .models import Manufacturer, Car, Topping, Pizza, Person, Group, Membership, Student, Artist, MyModel

# Register your models here.

admin.site.register(Manufacturer)

admin.site.register(Car)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Student)
admin.site.register(Artist)
admin.site.register(MyModel)