from django.contrib import admin
from .models import Location, ContactMessage, LocationType

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name','type', 'description', 'verified')
    list_filter = ('type', 'name', 'verified')
    search_fields = ('type', 'name', 'verified')

admin.site.register(Location, LocationAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')

admin.site.register(ContactMessage, ContactMessageAdmin)

admin.site.register(LocationType)