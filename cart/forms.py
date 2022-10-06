from typing import Optional, Any
from django import forms
from django.core.exceptions import ValidationError

from base.models import Customer
from .models import Cart, OrderedItem
from .choices import ItemCountChoices


class AddToCartForms(forms.Form):
    item_count = forms.ChoiceField(choices=ItemCountChoices.choices)


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = '__all__'

    def clean(self) -> Optional[dict[str, Any]]:
        errors: list[ValidationError] = []
        user: Customer = self.cleaned_data['user']
        items: list[OrderedItem] = self.cleaned_data['items']
        for item in items:
            if item.user != user:
                errors.append(f"{user} can't have this items  of {item.user}")
                break
        if errors:
            raise ValidationError(*errors)
        return super().clean()
