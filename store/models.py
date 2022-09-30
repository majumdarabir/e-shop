from email.policy import default
from django.db import models
from base.models import Customer
from products.models import Product
from .validators import check_valid_ratings


class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review = models.CharField(max_length=250, null=False)
    reviewed_at = models.DateTimeField(auto_now=True)
    ratings = models.IntegerField(null=True, validators=[check_valid_ratings])

    def __str__(self) -> str:
        return f"{self.user}:{self.review}"


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
