from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Customer


class RegistrationForm(UserCreationForm):
    email: forms.Field = forms.EmailField(label="Email", required=True)
    password1: forms.Field = forms.CharField(
        label="Password", widget=forms.PasswordInput)
    password2: forms.Field = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)
        help_texts = {
            'password1': None,
            'password2': None,
            'username': None,
        }


class CustomerUpgradeForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
