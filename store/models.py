from django.db import models
from base.models import Customers
from products.models import Product


class Review(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, null=False)
    reviewed_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}"


class Like(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False, null=False)
    liked_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}"


class Item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)

    def __str__(self) -> str:
        return f"{self.product.name}"
