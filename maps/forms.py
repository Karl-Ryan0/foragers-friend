from django import forms
from .models import Location
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from allauth.account.forms import LoginForm
from django.contrib.auth.models import User


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['notes', 'type', 'latitude', 'longitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['latitude', 'longitude']:
            self.fields[field_name].widget.attrs['readonly'] = True


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    def login(self, request, redirect_url=None):
        return super(CustomLoginForm, self).login(request, redirect_url)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LocationEditForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['type', 'notes']