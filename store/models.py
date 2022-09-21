from django.db import models
from base.models import Customer
from products.models import Product


class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, null=False)
    reviewed_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}:{self.comment}"


class Like(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False, null=False)
    liked_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}"


class Item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.product.name}"
