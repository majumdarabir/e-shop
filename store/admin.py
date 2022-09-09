from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


@admin.register(Category)
class AdminCatagory(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


# Register your models here.
# admin.site.register(Product, AdminProduct)
# admin.site.register(Category, AdminCatagory)
admin.site.register(Customer)
