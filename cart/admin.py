from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Cart, Order


@admin.register(Cart)
class CartAdmin(ModelAdmin):
    pass


@admin.register(Order)
class OrdersAdmin(ModelAdmin):
    pass
