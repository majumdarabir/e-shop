from django import forms
from .models import Review


class SearchForm(forms.Form):
    search = forms.CharField(required=True, max_length=200)

    class Meta:
        widgets = {
            'search': forms.TextInput(
                attrs={
                    'placeholder': 'Enter products',
                    'class': 'form-control'
                }
            ),
        }


class ReviewForms(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('comment',)
        help_texts = {
            'comment': 'Add your commnet',
        }
        labels = {
            'comment': None
        }
