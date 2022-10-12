from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer
from django.utils import timezone


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)
        help_texts = {
            'password1': None,
            'password2': None,
            'username': None,
        }


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        max_length=100, required=True, label="", help_text="Old Password",
        widget=forms.TextInput)
    new_password = forms.CharField(
        max_length=100, required=True, label="", help_text="New Password",
        widget=forms.TextInput)

    def clean(self):
        old_password = self.cleaned_data.get('old_password' or None)
        new_password = self.cleaned_data.get('new_password' or None)
        if old_password == new_password:
            raise ValidationError("New password is same as the old one ")
        return super().clean()


class UpgradeCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = 'first_name', 'last_name', 'address', 'email', 'phone_number', 'date_of_birth', 'image'
        help_texts = {
            "date_of_birth": f"If not updated, default to 1st Jan ,{timezone.now().year-5}"
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type here',
                'class': 'form-control'

            }),
            'last_name': forms.TextInput(attrs={

                'placeholder': 'Type here',
                'class': 'form-control'

            }), 'email': forms.EmailInput(attrs={
                'placeholder': 'example@example.com',
                'class': 'form-control'

            }), 'phone_number': forms.NumberInput(attrs={
                'placeholder': '+0987654321',
                'class': 'form-control'

            }), 'address': forms.Textarea(attrs={
                'placeholder': 'Your address goes here',
                'class': 'form-control',
                'rows': 5

            }), 'date_of_birth': forms.TextInput(attrs={
                'type': 'date',
                'placeholder': 'Your birthdate',
                'class': 'form-control'

            }), 'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': "image/x-png,image/jpeg",
                "multiple": False
            })
        }
