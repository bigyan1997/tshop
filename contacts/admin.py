from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['name', 'email', 'subject', 'date_submitted', 'updated', 'replied']
    list_filter = ['email']
    list_editable = ['replied']
