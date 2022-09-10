from dataclasses import Field
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


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
