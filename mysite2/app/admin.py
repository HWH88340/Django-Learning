from django.contrib import admin
# Register your models here.
from .models import Author, Book, Person,Comment

admin.AdminSite.empty_value_display = '没填'


class BookInline(admin.StackedInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('=name','title')
    list_per_page = 2
    list_filter = ('birth_date',)
    list_editable = ('birth_date',)
    list_display_links = ('name', 'title')
    actions_on_bottom = True
    # actions_selection_counter = False
    date_hierarchy = 'birth_date'
    # empty_value_display = '--empty--'
    list_display = ['name', 'title', 'birth_date', 'view_birthday', 'colored_name']
    # fields = (('title', 'name'), 'birth_date')
    # exclude = ('birth_date',)
    fieldsets = (
        (
            'info',{
                'fields':('name','title'),
            }
        ),
        (
            'date',{
                'classes': ('collapse',),
                'fields':('birth_date',),
                'description':'你的生日不快乐'
            }
        )
    )

    def view_birthday(self, obj):
        return obj.birth_date

    view_birthday.empty_value_display = '生日不详'
    view_birthday.short_description = '查看生日日期'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('authors',)
    # radio_fields = {"editor": admin.VERTICAL}
    raw_id_fields = ('editor',)
    pass

from django.db.models import F

def reverse_flag(modeladmin, request, queryset):
    # for obj in queryset:
    #     obj.flag = not F('flag')
    #     obj.save()
    queryset.update(flag=1-F('flag'))

    modeladmin.message_user(request, '转换了%s个数据' % queryset.count())

reverse_flag.short_description = '标识取反'



@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ['name','flag', 'flag_is_true']
    actions = [reverse_flag]

    # def reverse_flag(self, request, queryset):
    #     for obj in queryset:
    #         obj.flag = not obj.flag
    #         obj.save()
    #     # queryset.update(flag=(not F('flag')))
    #
    # reverse_flag.short_description = '标识取反'



admin.site.add_action(reverse_flag)
admin.site.register(Comment)