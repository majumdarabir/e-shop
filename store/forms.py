from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=True)

    class Meta:
        widgets = {
            'search': forms.TextInput(
                attrs={
                    'placeholder': 'Enter products',
                    'class': 'form-control'
                }
            ),
        }
