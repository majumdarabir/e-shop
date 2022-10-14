from django import forms
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet

from base.models import Customer
from .models import Cart, Coupon, OrderedItem


class CouponForm(forms.Form):
    code = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={"type": "text",
                       "class": "form-control",
                       "placeholder": "Coupon code"
               }
    ), label="", required=True)


class CouponAdminForm(forms.ModelForm):
    class Meta:
        model = Coupon
        # fields = 'code', 'short_description', 'valid_till', 'discount_amount'
        fields = '__all__'


class OrderItemForm(forms.ModelForm):
    class Meta:
        fields = 'item_count', 'item'


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = '__all__'

    def clean(self):
        errors: list[ValidationError] = []
        user: Customer = self.cleaned_data['user']
        items: QuerySet[OrderedItem] = self.cleaned_data['items']
        if items.filter(user=user):
            errors.append(f"{user} can't have this items")
        if errors:
            raise ValidationError(*errors)
        return super().clean()
