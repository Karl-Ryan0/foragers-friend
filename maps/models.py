from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.

TYPE_CHOICE = [
    ('Strawberries', 'Strawberries'),
    ('Blackberries', 'Blackberries'),
    ('Nettles', 'Nettles'),
]


STATUS = ((0, "Unconfirmed"), (1, "Confirmed"))


class Location(models.Model):
    name = models.CharField(max_length=100, default='placeholder')
    description = models.TextField(default='placeholder')
    type = models.CharField(max_length=20, choices=TYPE_CHOICE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
