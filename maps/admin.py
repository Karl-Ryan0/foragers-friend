from django.contrib import admin
from .models import Location, ContactMessage

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'verified')
    list_filter = ('type', 'name', 'verified')
    search_fields = ('type', 'name')

admin.site.register(Location, LocationAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')

admin.site.register(ContactMessage, ContactMessageAdmin)