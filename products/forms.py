from django import forms
from django.core.exceptions import ValidationError


class PricePickerForm(forms.Form):
    min = forms.FloatField(required=True, label="Min", widget=forms.NumberInput(
        attrs={'placeholder': 0}))
    max = forms.FloatField(required=True, label="Max", widget=forms.NumberInput(
        attrs={'placeholder': 0}))

    def is_valid(self) -> bool:
        if self.min > self.max:
            raise ValidationError("min value is gr max value", code="invalid")
        return super().is_valid()
