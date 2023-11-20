from django.contrib import admin
from .models import Location, ContactMessage, LocationType


class LocationAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Location model.

    Provides specific configurations for how the Location
    model should be displayed and managed
    in the Django admin interface.
    """

    list_display = ('notes', 'type', 'user', 'display_favorites')
    list_filter = ('type', 'verified')
    search_fields = ('type', 'verified')
    filter_horizontal = ('favorited_by',)

    def display_favorites(self, obj):
        """
        A custom method to display a comma-separated
        list of usernames who have favorited a location.
        """
        return ", ".join([user.username for user in obj.favorited_by.all()])
    display_favorites.short_description = 'Favorited By'


admin.site.register(Location, LocationAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the ContactMessage model.

    Provides specific configurations for how the ContactMessage
    model should be displayed
    and managed in the Django admin interface.
    """

    list_display = ('subject', 'name', 'email', 'created_at')


admin.site.register(ContactMessage, ContactMessageAdmin)

admin.site.register(LocationType)
