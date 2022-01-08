from django.contrib import admin
from models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'number', 'address')
    # exclude = ('birthday', 'address')
    # fieldsets = (
        # ['base', {'fields':('name', 'number')}],
        # ['personal', {'fields': ('birthday', 'address')}]
    # )
    # list_display = ('name', 'address', 'number')
    # list_filter = ('address', )
    search_fields = ('address', )

admin.site.register(Contact, ContactAdmin)
