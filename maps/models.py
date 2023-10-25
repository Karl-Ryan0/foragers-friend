from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField

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

    def __str__(self):
        return self.name
