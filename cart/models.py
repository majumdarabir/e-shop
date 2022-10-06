
from store.models import Item
from base.models import Customer
from django.utils import timezone
from django.db import models


from .choices import PaymentChoice
from.validators import item_count_ge_zero


# class Checkout(models.Model):
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     address = models.TextField(blank=False, null=False)
#     address2 = models.TextField(blank=True)
#     zip_code = models.PositiveIntegerField()
#     country = models.CharField(max_length=70, choices=CountryChoices.choices)


class PromoCode(models.Model):
    code = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    valid_till = models.DateField(default=timezone.now)
    discount_amount = models.PositiveIntegerField(null=False)


class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    payment_options = models.CharField(
        max_length=50, choices=PaymentChoice.choices)
    is_delivered = models.BooleanField(default=False)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=False)


class OrderedItem(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_count = models.IntegerField(validators=[item_count_ge_zero])

    def __str__(self) -> str:
        return f"{self.user}:{self.item}"


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem, blank=True)

    class Meta:
        ordering = '-updated_at',

    def __str__(self) -> str:
        return f"{self.user}"
