from django.contrib import admin
from website.models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'message', 'created_date', 'updated_date')
    list_filter = ('email', 'name')
    search_fields = ('name', 'message')
