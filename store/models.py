
from django.db import models
from base.models import Customers
from products.models import Product


class Review(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, null=False)
    reviewed_at = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False, null=False)
    liked_at = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
