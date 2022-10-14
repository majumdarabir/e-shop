from store.models import Item
from base.models import Customer
from django.utils import timezone
from django.db import models

from .choices import PaymentChoice
from.validators import item_count_ge_zero, coupon_validation


# class Checkout(models.Model):
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     address = models.TextField(blank=False, null=False)
#     address2 = models.TextField(blank=True)
#     zip_code = models.PositiveIntegerField()
#     country = models.CharField(max_length=70, choices=CountryChoices.choices)


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    user = models.ManyToManyField(
        Customer, related_name="promo_code", blank=True)
    short_description = models.CharField(max_length=100)
    valid_till = models.DateField(
        default=timezone.now, validators=[coupon_validation])
    discount_amount = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.code}"

    @property
    def valid(self):
        return self.valid_till > timezone.now().date()


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
    item_count = models.IntegerField(
        default=1, validators=[item_count_ge_zero])

    def __str__(self) -> str:
        return f"{self.user}:{self.item}"

    @property
    def total_price(self):
        return self.item_count*self.item.product.price

    @property
    def product(self):
        return self.item.product

    @property
    def item_price(self):
        return self.item.product.price


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem, blank=True)
    coupons = models.ManyToManyField(Coupon, blank=True)

    class Meta:
        ordering = '-updated_at',

    def __str__(self) -> str:
        return f"{self.user}"

    @property
    def total_price(self):
        return sum([item.total_price for item in self.items.all()])

    @property
    def discount(self):
        return sum([coupon.discount_amount for coupon in self.coupons.all()])

    @property
    def final_price(self):
        return self.total_price - self.discount
