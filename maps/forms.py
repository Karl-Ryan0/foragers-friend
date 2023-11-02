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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['latitude', 'longitude']:
            self.fields[field_name].widget.attrs['readonly'] = True


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

