from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    search = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={

                "type": "search",
                "class": "form-control",
                "placeholder": "Type query",
                "aria-label": "Search"
            }
        ),
        label=""
    )
