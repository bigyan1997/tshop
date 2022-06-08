from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Roaster

@admin.register(Roaster)
class RoasterAdmin(admin.ModelAdmin):
    list_display = ['user', 'week_starting', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                    'sunday']