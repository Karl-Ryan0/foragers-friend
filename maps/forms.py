from django import forms
from .models import Location
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import LoginForm
from django.contrib.auth.models import User


class LocationForm(forms.ModelForm):
    """
    A form for creating and editing Location instances.

    This form is used to input data for Location objects. Certain fields like latitude and longitude
    are set to read-only to prevent manual editing.
    """
    class Meta:
        model = Location
        fields = ['notes', 'type', 'latitude', 'longitude']

    def __init__(self, *args, **kwargs):
        """
        Initialize the form, setting specific fields to read-only.
        """
        super().__init__(*args, **kwargs)
        for field_name in ['latitude', 'longitude']:
            self.fields[field_name].widget.attrs['readonly'] = True


class ContactForm(forms.Form):
    """
    A form for submitting contact messages.

    This form allows users to send messages including their name, email,
    subject, and message content.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


class CustomLoginForm(LoginForm):
    """
    Customized login form inheriting from allauth's LoginForm.
    """
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    def login(self, request, redirect_url=None):
        return super(CustomLoginForm, self).login(request, redirect_url)


class RegistrationForm(UserCreationForm):
    """
    A form for registering new users, extending Django's UserCreationForm.

    Includes an additional email field which is required for registration.
    """
    email = forms.EmailField(
        required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LocationEditForm(forms.ModelForm):
    """
    A form for editing existing Location instances.

    This form is used to edit data for Location objects, specifically the type and notes fields.
    """
    class Meta:
        model = Location
        fields = ['type', 'notes']
