from django.db import models
from base.models import Customers
from products.models import Product


class PaymentChoice(models.TextChoices):
    CASH_ON_DELIVERY = 1, "cash on delivery"
    NET_BANKING = 2, 'net banking'
    CREDIT_CARD = 3, 'credit-card'
    DEBIT_CARD = 4, 'debit-card'


class Orders(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    payment_options = models.CharField(
        max_length=100, choices=PaymentChoice.choices)
    is_delivered = models.BooleanField(default=False)
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=False)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    had_checkout = models.BooleanField(default=False, null=False)
    items = models.ManyToManyField(Product, blank=True)
