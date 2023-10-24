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

