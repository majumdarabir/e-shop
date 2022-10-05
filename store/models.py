from django.db import models
from base.models import Customer
from products.models import Product
from .validators import check_valid_ratings


class Item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    favorite_users = models.ManyToManyField(
        Customer, related_name="item_favorite_users", blank=True)
    wishlist_users = models.ManyToManyField(
        Customer, related_name="item_wishlist_users", blank=True)

    def __str__(self) -> str:
        return f"{self.product}"


class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review = models.CharField(max_length=250, null=False)
    reviewed_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(
        Customer, blank=True, related_name="review_likes_count")
    unliked_by = models.ManyToManyField(
        Customer, blank=True, related_name="review_unlikes_count")
    ratings = models.IntegerField(null=True, validators=[check_valid_ratings])
    product = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        ordering = 'reviewed_at',

    def __str__(self) -> str:
        return f"{self.user}:{self.review}"
