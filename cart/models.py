from django.db import models
from base.models import Customer
from products.models import Product
from .choices import PaymentChoice


class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    payment_options = models.CharField(
        max_length=100, choices=PaymentChoice.choices)
    is_delivered = models.BooleanField(default=False)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=False)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    had_checkout = models.BooleanField(default=False, null=False)
    items = models.ManyToManyField(Product, blank=True)
