from django.contrib import admin
from .models import Location, ContactMessage, LocationType

# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ('notes', 'type', 'user', 'display_favorites')
    list_filter = ('type', 'verified')
    search_fields = ('type', 'verified')
    filter_horizontal = ('favorited_by',)

    def display_favorites(self, obj):
        return ", ".join([user.username for user in obj.favorited_by.all()])
    display_favorites.short_description = 'Favorited By'


admin.site.register(Location, LocationAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')


admin.site.register(ContactMessage, ContactMessageAdmin)

admin.site.register(LocationType)
