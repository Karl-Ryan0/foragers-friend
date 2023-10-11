from django.contrib import admin
from .models import Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('type', 'created_on', 'status', 'created_by', 'country')
    list_filter = ('type', 'status')
    search_fields = ('type', 'created_by__username')

admin.site.register(Location, LocationAdmin)