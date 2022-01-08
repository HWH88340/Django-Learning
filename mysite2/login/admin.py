from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class MyUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#         ('新增字段', {
#             'fields': ('address', 'education', 'birthday'),
#         }),
#     )

# admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MyUser)

from guardian.admin import GuardedModelAdmin
from .models import Task

class TaskAdmin(GuardedModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)