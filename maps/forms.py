from django import forms


class LocationForm(forms.Form):
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()
