from statistics import mode
from unicodedata import category
from .category import Category
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    description = models.CharField(max_length=100,  default='')
    image = models.ImageField(upload_to='products')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
