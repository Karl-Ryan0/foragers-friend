from django import forms
from .models import Location

TYPE_CHOICE = [
    ('Strawberries', 'Strawberries'),
    ('Blackberries', 'Blackberries'),
    ('Nettles', 'Nettles'),
]

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'type', 'latitude', 'longitude']

