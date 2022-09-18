from django import forms


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
