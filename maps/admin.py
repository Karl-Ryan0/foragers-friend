from django.contrib import admin
from .models import Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type')
    list_filter = ('type', 'name')
    search_fields = ('type', 'name')

admin.site.register(Location, LocationAdmin)