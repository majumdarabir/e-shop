from django import forms
from .models import Review


class SearchForm(forms.Form):
    search = forms.CharField(required=True, max_length=200)

    class Meta:
        widgets = {
            'search': forms.TextInput(
                attrs={
                    'type': 'text',
                    'placeholder': 'Enter products',
                    'class': 'form-control'
                }
            ),
        }


class ReviewForms(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('review', 'ratings', 'user', 'product')
        widgets = {
            'review': forms.TextInput(attrs={
                'placeholder': 'Enter your review',
                'type': 'text',
                'class': 'form-control',
                'data-mdb-showcounter': True,
                'maxlength': 50
            }),
            'ratings': forms.NumberInput(attrs={
                'class': 'form-control', 'min': 0, 'max': 5
            }),
            'user': forms.TextInput(attrs={'type': 'hidden'}),
            'product': forms.TextInput(attrs={'type': 'hidden'})
        }
        labels = {
            'review': 'Add your Review'
        }
