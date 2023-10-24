from django import forms

TYPE_CHOICE = [
    ('Strawberries', 'Strawberries'),
    ('Blackberries', 'Blackberries'),
    ('Nettles', 'Nettles'),
]

class LocationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name', required=True)
    description = forms.CharField(widget=forms.Textarea, label='Description')
    type = forms.ChoiceField(choices=TYPE_CHOICE, label='Type')
    latitude = forms.DecimalField(max_digits=9, decimal_places=6, label='Latitude', required=False)
    longitude = forms.DecimalField(max_digits=9, decimal_places=6, label='Longitude', required=False)

