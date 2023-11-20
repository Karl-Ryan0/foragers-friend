from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class LocationType(models.Model):
    """
    Represents a type or category for a location.

    Attributes:
        name (CharField): The name of the location type.
        description (TextField): An optional description of the location type.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    Represents a geographical location.

    Attributes:
        notes (TextField): Descriptive notes or information about the location.
        type (ForeignKey): The type or category
        of the location, linked to LocationType.
        latitude (DecimalField): The latitude of the location.
        longitude (DecimalField): The longitude of the location.
        verified (BooleanField): A flag indicating whether
        the location has been verified.
        created_on (DateTimeField): The date and time when
        the location was created.
        user (ForeignKey): The user who created the location.
        favorited_by (ManyToManyField): Users who have marked the
        location as a favorite.
    """
    notes = models.TextField(null=True)
    type = models.ForeignKey('LocationType', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    favorited_by = models.ManyToManyField(
        User, related_name='favorite_locations', blank=True)

    def __str__(self):
        return self.notes[:50]


class ContactMessage(models.Model):
    """
    Represents a contact message sent by a user.

    Attributes:
        name (CharField): The name of the person sending the message.
        email (EmailField): The email address of the person
        sending the message.
        subject (CharField): The subject of the message.
        message (TextField): The content of the message.
        created_at (DateTimeField): The date and time when
        the message was created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
