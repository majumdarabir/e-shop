from django.db import models


class Category(models.Model):
    name: models.Field = models.CharField(max_length=50)
    description: models.Field = models.TextField(blank=True, null=True)
    created_at: models.Field = models.DateTimeField(auto_now_add=True)
    updated_at: models.Field = models.DateTimeField(auto_now=True)
    image: models.Field = models.ImageField(upload_to="categories", null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Tag(models.Model):
    name: models.Model = models.CharField(max_length=20)
    description: models.Model = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    name: models.Field = models.CharField(
        max_length=50, blank=False, null=False)
    price: models.Field = models.FloatField(default=0, null=False)
    category: models.Field = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    created_at: models.Field = models.DateTimeField(auto_now_add=True)
    updated_at: models.Field = models.DateTimeField(auto_now=True)
    description: models.Field = models.TextField(blank=True, null=True)
    image: models.Field = models.ImageField(upload_to='products')
    tag: models.Field = models.ManyToManyField(Tag, null=True)

    def __str__(self) -> str:
        return f"{self.name}"
