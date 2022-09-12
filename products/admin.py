from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Category, Product, Tag
# Register your models here.


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(Tag)
class TagsAdmin(ModelAdmin):
    pass
